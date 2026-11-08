import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).with_name("extract_candidate.py")
spec = importlib.util.spec_from_file_location("extract_candidate", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

CANDIDATE = "# Name\n\n## Engineer\n\n- Approved claim.\n"
AUDIT = "\n---\n\n## Notas de generación / Auditoría\n\n> Esta sección no está destinada al envío.\n"


class FinalizerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()

    def source(self, relative, mode=None, marked=True):
        text = (module.START + "\n" + CANDIDATE + module.END if marked else CANDIDATE)
        text += AUDIT + (f"\n- **source_mode:** `{mode}`\n" if mode else "")
        text += "\n- **claims_used:** PRIVATE-AUDIT-SENTINEL\n"
        p = self.root / relative
        p.parent.mkdir(parents=True)
        p.write_text(text)
        return p

    def test_legacy_application_without_mode(self):
        self.source("career/applications/legacy/generated/cv.md", marked=False)
        mode, output, candidate = module.resolve_input(
            self.root, source_application_folder="career/applications/legacy")
        self.assertEqual(mode, "application")
        self.assertEqual(output, self.root / "career/applications/legacy/final")
        self.assertEqual(candidate, CANDIDATE)

    def test_explicit_application_and_example(self):
        self.source("examples/applications/example/generated/cv.md", "application")
        mode, output, candidate = module.resolve_input(
            self.root, source_application_folder="examples/applications/example")
        self.assertEqual(mode, "application")
        self.assertEqual(output, self.root / "examples/applications/example/final")
        self.assertEqual(candidate, CANDIDATE)

    def test_reusable_without_application_metadata_or_dossier(self):
        self.source("generated/freelance/cv.md", "reusable_strategy")
        mode, output, candidate = module.resolve_input(
            self.root, source_generated_cv="generated/freelance/cv.md")
        self.assertEqual(mode, "reusable_strategy")
        self.assertEqual(output, self.root / "generated/freelance/final")
        self.assertEqual(candidate, CANDIDATE)
        self.assertFalse((self.root / "career").exists())

    def test_reusable_cli_preserves_content_and_excludes_all_audit(self):
        source = self.source("generated/freelance/cv.md", "reusable_strategy")
        original = source.read_bytes()
        result = subprocess.run([
            sys.executable, str(SCRIPT), "--root", str(self.root),
            "--source-generated-cv", "generated/freelance/cv.md",
            "--language", "es", "--content-approved"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((source.parent / "final/cv-send-es.md").read_text(), CANDIDATE)
        self.assertEqual(source.read_bytes(), original)

    def test_malformed_markers_fail_closed(self):
        for text in [module.START + CANDIDATE + AUDIT,
                     module.END + CANDIDATE + module.START,
                     module.START + CANDIDATE + module.END + module.END,
                     CANDIDATE]:
            with self.subTest(text=text), self.assertRaises(ValueError):
                module.extract_candidate(text)

    def test_legitimate_separator_and_links_are_preserved(self):
        candidate = '# Name\n\n---\n\n[LinkedIn](https://www.linkedin.com/in/example/)\n'
        self.assertEqual(module.extract_candidate(candidate + AUDIT), candidate)

    def test_conflicting_modes_and_fake_application_rejected(self):
        p = self.source("generated/freelance/cv.md", "reusable_strategy")
        with self.assertRaises(ValueError):
            module.resolve_input(self.root, source_generated_cv=str(p), source_mode="application")
        p.write_text(p.read_text() + "\n- **application_id:** `application:fake`\n")
        with self.assertRaises(ValueError):
            module.resolve_input(self.root, source_generated_cv=str(p))

    def test_output_cannot_escape_repo_through_symlink(self):
        p = self.source("generated/freelance/cv.md", "reusable_strategy")
        with tempfile.TemporaryDirectory() as external:
            (p.parent / "final").symlink_to(external, target_is_directory=True)
            with self.assertRaises(ValueError):
                module.resolve_input(self.root, source_generated_cv=str(p))

    def test_existing_application_sources_still_extract(self):
        root = SCRIPT.resolve().parents[2]
        sources = list((root / "career/applications").glob("*/generated/cv.md"))
        self.assertTrue(sources)
        for source in sources:
            with self.subTest(source=source):
                mode, output, candidate = module.resolve_input(
                    root, source_application_folder=str(source.parent.parent))
                self.assertEqual(mode, "application")
                self.assertEqual(output, source.parent.parent / "final")
                self.assertNotIn(module.AUDIT, candidate)


if __name__ == "__main__":
    unittest.main()
