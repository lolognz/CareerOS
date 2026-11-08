#!/usr/bin/env python3
"""Shared, dependency-free input/extraction step for the agent-run CV finalizer.

Rendering still follows generators/cv-finalizer using templates/final.
This helper writes only the clean Markdown; it never exports a PDF.
"""

import argparse
from pathlib import Path
import re


START = "<!-- Inicio del bloque destinado a candidatura -->"
END = "<!-- Fin del bloque destinado a candidatura -->"
AUDIT = "## Notas de generación / Auditoría"


def extract_candidate(text):
    """Prefer exact markers; reject malformed markers instead of leaking audit."""
    if START in text or END in text:
        if text.count(START) != 1 or text.count(END) != 1:
            raise ValueError("Expected exactly one candidate marker pair")
        start = text.index(START) + len(START)
        end = text.index(END)
        if end <= start:
            raise ValueError("Candidate markers are reversed or empty")
        candidate = text[start:end]
    else:
        boundaries = list(re.finditer(
            r"(?m)^---[ \t]*\n\s*## Notas de generación / Auditoría[ \t]*\n"
            r"\s*>[^\n]*no está destinada al envío[^\n]*", text))
        if len(boundaries) != 1:
            raise ValueError("No unambiguous candidate/audit boundary")
        candidate = text[:boundaries[0].start()]
    if AUDIT in candidate:
        raise ValueError("Audit heading inside candidate block")
    candidate = re.sub(r"<!--.*?-->", "", candidate, flags=re.S)
    candidate = re.sub(r"(?m)^\[//\]:\s*#.*$", "", candidate)
    candidate = "\n".join(line.rstrip() for line in candidate.splitlines()).strip()
    if not candidate or not candidate.startswith("# "):
        raise ValueError("Candidate must contain a name heading")
    return candidate + "\n"


def metadata(text, key):
    """Read generation metadata only after the audit heading."""
    audit = text.partition(AUDIT)[2]
    match = re.search(r"(?m)^- \*\*" + re.escape(key) + r":\*\*\s*(.+)$", audit)
    return match.group(1).strip().strip("`") if match else None


def resolve_input(root, source_application_folder=None, source_generated_cv=None,
                  source_mode=None):
    """Keep legacy application-folder invocation; reusable has no dossier."""
    root = Path(root).resolve()
    if bool(source_application_folder) == bool(source_generated_cv):
        raise ValueError("Provide exactly one application folder or generated CV")
    source = root / (Path(source_application_folder) / "generated/cv.md"
                     if source_application_folder else Path(source_generated_cv))
    source = source.resolve()
    relative = source.relative_to(root)
    text = source.read_text(encoding="utf-8")
    declared = metadata(text, "source_mode")
    mode = source_mode or declared or "application"
    if mode not in {"application", "reusable_strategy"} or (declared and declared != mode):
        raise ValueError("Invalid or conflicting source mode")
    if mode == "application":
        parts = relative.parts
        if (len(parts) != 5 or parts[:2] not in
                {("career", "applications"), ("examples", "applications")}
                or parts[-2:] != ("generated", "cv.md")):
            raise ValueError("Application input must be <application-folder>/generated/cv.md")
        output = source.parent.parent / "final"
    else:
        if source_application_folder or declared != "reusable_strategy":
            raise ValueError("Reusable input must declare reusable_strategy; no application folder")
        if (len(relative.parts) < 3 or relative.parts[0] != "generated"
                or relative.name != "cv.md" or "final" in relative.parts):
            raise ValueError("Reusable input must be generated/<scope>/cv.md")
        for key in ("application_id", "source_application_folder"):
            if metadata(text, key) not in (None, "[]"):
                raise ValueError("Reusable input cannot reference an application")
        output = source.parent / "final"
    output.resolve().relative_to(root)
    return mode, output, extract_candidate(text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    inputs = parser.add_mutually_exclusive_group(required=True)
    inputs.add_argument("--source-application-folder")
    inputs.add_argument("--source-generated-cv")
    parser.add_argument("--source-mode", choices=("application", "reusable_strategy"))
    parser.add_argument("--language", required=True, choices=("es", "en"))
    parser.add_argument("--output-prefix", default="cv")
    parser.add_argument("--content-approved", action="store_true")
    args = parser.parse_args()
    if not args.content_approved:
        parser.error("Confirm content approval with --content-approved")
    if not re.fullmatch(r"[A-Za-z0-9_-]+", args.output_prefix):
        parser.error("Unsafe output prefix")
    try:
        mode, output, candidate = resolve_input(
            args.root, args.source_application_folder, args.source_generated_cv, args.source_mode)
        target = output / f"{args.output_prefix}-send-{args.language}.md"
        if target.exists():
            raise ValueError("Output exists; review it before replacing through the workflow")
        output.mkdir(parents=True, exist_ok=True)
        target.write_text(candidate, encoding="utf-8")
    except (ValueError, OSError) as error:
        parser.error(str(error))
    print(f"{mode}: {target}")


if __name__ == "__main__":
    main()
