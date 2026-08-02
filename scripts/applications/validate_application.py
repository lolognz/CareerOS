#!/usr/bin/env python3
"""Validate whether a CareerOS application is structurally ready for Job Intake."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


REQUIRED_FILES = (
    "job-description.md",
    "job-intake.md",
    "target-profile-selection.md",
    "evidence-selection.md",
    "application-plan.md",
    "risk-register.md",
    "submission-record.md",
    "generated/README.md",
)

ANALYSIS_HEADINGS = {
    "job-intake.md": (
        "## Identificación",
        "## Requisitos extraídos",
        "## Campos consolidados del esquema",
    ),
    "target-profile-selection.md": (
        "## Recomendación",
        "## Perfiles secundarios posibles",
        "## Perfiles descartados",
        "## Señales de encaje",
        "## Riesgos específicos del perfil",
        "## Incertidumbre",
    ),
    "evidence-selection.md": (
        "## Criterio",
        "## Entidades seleccionadas",
        "## Uso recomendado",
        "## Evidencia a enfatizar",
        "## Evidencia a evitar",
        "## Evidencia que exige redacción cuidadosa",
        "## Requisitos sin evidencia seleccionable",
    ),
    "application-plan.md": (
        "## Decisión",
        "## Estrategia de CV",
        "## Estrategia de carta de presentación",
        "## Estrategia de mensaje a recruiter",
        "## Prioridades de entrevista",
        "## Gaps a abordar",
        "## Outputs recomendados",
    ),
    "risk-register.md": (
        "## Riesgos de sobreafirmación",
        "## Áreas de evidencia débil",
        "## Requisitos ausentes",
        "## Expectativas del puesto poco claras",
        "## Ubicación, contrato y compensación",
        "## Recomendación consolidada",
    ),
}

JOB_DESCRIPTION_PLACEHOLDERS = (
    "[TEXTO ORIGINAL DE LA OFERTA]",
    "[fecha/hora o desconocida]",
    "[fecha o desconocida]",
    "[idioma de la oferta]",
    "[completa / parcial / desconocida]",
    "[ninguna conocida / detalle]",
    "[hechos sobre la captura; no análisis de encaje]",
)


@dataclass
class ValidationResult:
    failures: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    information: list[str] = field(default_factory=list)

    def fail(self, message: str) -> None:
        self.failures.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def info(self, message: str) -> None:
        self.information.append(message)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Valida de forma estructural un expediente antes de ejecutar Job Intake. "
            "No analiza semánticamente la oferta ni modifica archivos."
        )
    )
    parser.add_argument("application_folder", type=Path, help="Ruta del expediente.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Hace que las advertencias también produzcan código de salida 1.",
    )
    parser.add_argument(
        "--allow-generated",
        action="store_true",
        help="Permite archivos adicionales dentro de generated/.",
    )
    return parser.parse_args()


def read_text(path: Path, result: ValidationResult) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        result.fail(f"No se puede leer como UTF-8: {path.name}")
    except OSError as error:
        result.fail(f"No se puede leer {path.name}: {error}")
    return None


def validate_required_structure(folder: Path, result: ValidationResult) -> bool:
    if not folder.exists():
        result.fail(f"La ruta no existe: {folder}")
        return False
    if not folder.is_dir():
        result.fail(f"La ruta no es una carpeta: {folder}")
        return False

    for relative_name in REQUIRED_FILES:
        path = folder / relative_name
        if not path.is_file():
            result.fail(f"Falta el archivo requerido: {relative_name}")

    generated_dir = folder / "generated"
    if not generated_dir.exists():
        result.fail("Falta la carpeta requerida: generated/")
    elif not generated_dir.is_dir():
        result.fail("generated/ existe, pero no es una carpeta.")
    return True


def validate_generated(
    folder: Path, result: ValidationResult, *, allow_generated: bool
) -> None:
    generated_dir = folder / "generated"
    if not generated_dir.is_dir():
        return

    extra_files = sorted(
        path.relative_to(folder).as_posix()
        for path in generated_dir.rglob("*")
        if path.is_file() and path != generated_dir / "README.md"
    )
    if not extra_files:
        return
    if allow_generated:
        result.info(
            "Se permiten por --allow-generated estos archivos: "
            + ", ".join(extra_files)
        )
    else:
        result.fail(
            "Hay outputs o archivos no permitidos antes de Job Intake: "
            + ", ".join(extra_files)
        )


def extract_original_offer(content: str) -> str | None:
    section_match = re.search(
        r"(?ms)^## Texto original preservado\s*$\n(.*?)(?=^##\s|\Z)", content
    )
    if not section_match:
        return None
    section = re.sub(r"<!--.*?-->", "", section_match.group(1), flags=re.DOTALL)
    lines = [
        line
        for line in section.splitlines()
        if line.strip() not in {"```", "```text"}
    ]
    return "\n".join(lines).strip()


def validate_job_description(folder: Path, result: ValidationResult) -> None:
    path = folder / "job-description.md"
    if not path.is_file():
        return
    content = read_text(path, result)
    if content is None:
        return

    original_offer = extract_original_offer(content)
    if original_offer is None:
        result.fail(
            "job-description.md no contiene la sección '## Texto original preservado'."
        )
        return
    if not original_offer:
        result.fail("La sección de texto original de job-description.md está vacía.")
        return
    if "[TEXTO ORIGINAL DE LA OFERTA]" in original_offer:
        result.fail(
            "La oferta original no se ha pegado: permanece el placeholder principal."
        )
        return

    remaining = [item for item in JOB_DESCRIPTION_PLACEHOLDERS[1:] if item in content]
    if remaining:
        result.warn(
            "job-description.md conserva metadatos o notas pendientes: "
            + ", ".join(remaining)
        )


def validate_analysis_documents(folder: Path, result: ValidationResult) -> None:
    for filename, headings in ANALYSIS_HEADINGS.items():
        path = folder / filename
        if not path.is_file():
            continue
        content = read_text(path, result)
        if content is None:
            continue
        if not content.strip():
            result.warn(f"{filename} está vacío; debe conservar al menos su estructura.")
            continue
        missing = [heading for heading in headings if heading not in content]
        if missing:
            result.warn(
                f"{filename} no contiene encabezados esperados: " + ", ".join(missing)
            )


def validate_submission_record(folder: Path, result: ValidationResult) -> None:
    path = folder / "submission-record.md"
    if not path.is_file():
        return
    content = read_text(path, result)
    if content is None:
        return

    fields = {
        "Application ID": r"(?im)^\s*-\s*Application ID\s*:",
        "Estado": r"(?im)^\s*-\s*Estado\s*:",
        "Outcome": r"(?im)^\s*-\s*Outcome\s*:",
    }
    for label, pattern in fields.items():
        if not re.search(pattern, content):
            result.fail(f"submission-record.md no contiene el campo {label}.")


def validate_application(folder: Path, *, allow_generated: bool) -> ValidationResult:
    result = ValidationResult()
    if not validate_required_structure(folder, result):
        return result
    validate_generated(folder, result, allow_generated=allow_generated)
    validate_job_description(folder, result)
    validate_analysis_documents(folder, result)
    validate_submission_record(folder, result)
    return result


def print_result(result: ValidationResult, *, strict: bool) -> int:
    for message in result.failures:
        print(f"FAIL: {message}")
    for message in result.warnings:
        print(f"WARN: {message}")
    for message in result.information:
        print(f"INFO: {message}")

    if result.failures:
        print(
            f"FAIL — {len(result.failures)} error(es) y "
            f"{len(result.warnings)} advertencia(s)."
        )
        return 1
    if result.warnings:
        if strict:
            print(
                f"FAIL — modo estricto: {len(result.warnings)} advertencia(s) "
                "requieren corrección."
            )
            return 1
        print(
            f"WARN — estructura utilizable con {len(result.warnings)} advertencia(s)."
        )
        return 0
    print("PASS — expediente estructuralmente listo para Job Intake.")
    return 0


def main() -> int:
    args = parse_args()
    result = validate_application(
        args.application_folder.expanduser(),
        allow_generated=args.allow_generated,
    )
    return print_result(result, strict=args.strict)


if __name__ == "__main__":
    raise SystemExit(main())
