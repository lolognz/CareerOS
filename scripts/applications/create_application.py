#!/usr/bin/env python3
"""Create a safe CareerOS application scaffold from Job Intake templates."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path


SLUG_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DATE_PATTERN = re.compile(r"^(\d{4})-(\d{2})$")

TEMPLATE_FILES = {
    "job-description.template.md": "job-description.md",
    "job-intake.template.md": "job-intake.md",
    "target-profile-selection.template.md": "target-profile-selection.md",
    "evidence-selection.template.md": "evidence-selection.md",
    "application-plan.template.md": "application-plan.md",
    "application-risk-register.template.md": "risk-register.md",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Crea un expediente vacío de candidatura desde las plantillas de "
            "Job Intake. No genera outputs de candidatura."
        )
    )
    parser.add_argument("--date", required=True, help="Mes en formato YYYY-MM.")
    parser.add_argument("--company-slug", required=True, help="Slug de empresa.")
    parser.add_argument("--role-slug", required=True, help="Slug del puesto.")
    parser.add_argument("--company-name", required=True, help="Nombre de la empresa.")
    parser.add_argument("--role-title", required=True, help="Título del puesto.")
    parser.add_argument("--source-url", help="URL de la oferta, si existe.")
    parser.add_argument("--platform", help="Plataforma o fuente, si se conoce.")
    parser.add_argument("--location", help="Ubicación o modalidad, si se conoce.")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Sobrescribe únicamente los archivos administrados por el scaffold.",
    )
    return parser.parse_args()


def validate_month(value: str) -> str:
    match = DATE_PATTERN.fullmatch(value)
    if not match:
        raise ValueError("--date debe usar el formato YYYY-MM.")
    month = int(match.group(2))
    if not 1 <= month <= 12:
        raise ValueError("--date contiene un mes fuera del intervalo 01-12.")
    return value


def validate_slug(flag: str, value: str) -> str:
    if not SLUG_PATTERN.fullmatch(value):
        raise ValueError(
            f"{flag} debe contener solo minúsculas, números y guiones simples, "
            "sin guiones iniciales, finales o consecutivos."
        )
    return value


def validate_text(flag: str, value: str | None, *, required: bool) -> str | None:
    if value is None:
        if required:
            raise ValueError(f"{flag} es obligatorio.")
        return None
    cleaned = value.strip()
    if not cleaned:
        if required:
            raise ValueError(f"{flag} no puede estar vacío.")
        return None
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError(f"{flag} debe ocupar una sola línea.")
    return cleaned


def render_template(
    source: Path,
    *,
    application_slug: str,
    company_name: str,
    role_title: str,
    source_url: str | None,
    platform: str | None,
) -> str:
    content = source.read_text(encoding="utf-8")
    replacements = {
        "[empresa]": company_name,
        "[rol]": role_title,
        "[slug de candidatura]": application_slug,
    }
    for placeholder, replacement in replacements.items():
        content = content.replace(placeholder, replacement)

    if source.name == "job-description.template.md":
        table_company_name = company_name.replace("|", "\\|")
        table_role_title = role_title.replace("|", "\\|")
        table_source_url = (source_url or "desconocida").replace("|", "\\|")
        table_platform = (platform or "desconocida").replace("|", "\\|")
        content = content.replace(
            "| company_name_as_published | [literal o desconocido] |",
            f"| company_name_as_published | {table_company_name} |",
        )
        content = content.replace(
            "| role_title_as_published | [literal o desconocido] |",
            f"| role_title_as_published | {table_role_title} |",
        )
        content = content.replace(
            "| source_url | [URL o desconocida] |",
            f"| source_url | {table_source_url} |",
        )
        content = content.replace(
            "| source_platform | [plataforma o desconocida] |",
            f"| source_platform | {table_platform} |",
        )
        content = content.replace(
            "| captured_at | [fecha/hora] |",
            f"| captured_at | {date.today().isoformat()} |",
        )
    return content


def build_submission_record(
    *,
    application_slug: str,
    company_name: str,
    role_title: str,
    source_url: str | None,
    platform: str | None,
    location: str | None,
) -> str:
    return f"""# Registro de candidatura — {company_name} — {role_title}

## Identificación

- Application ID: `application:{application_slug}`
- Empresa: {company_name}
- Puesto: {role_title}
- Fecha de creación: {date.today().isoformat()}
- URL de la oferta: {source_url or 'No proporcionada'}
- Plataforma: {platform or 'No proporcionada'}
- Ubicación: {location or 'No proporcionada'}

## Estado

- Estado: intake pendiente

## Notas

- []

## Resultado

- Outcome: pendiente

## Próximos pasos

1. Pegar la descripción original de la oferta en `job-description.md`.
2. Ejecutar el workflow de Job Intake.
3. Revisar la selección de perfil objetivo.
4. Revisar la selección de evidencia.
5. Decidir si se generan outputs.
"""


def create_scaffold(args: argparse.Namespace) -> Path:
    month = validate_month(args.date)
    company_slug = validate_slug("--company-slug", args.company_slug)
    role_slug = validate_slug("--role-slug", args.role_slug)
    company_name = validate_text("--company-name", args.company_name, required=True)
    role_title = validate_text("--role-title", args.role_title, required=True)
    source_url = validate_text("--source-url", args.source_url, required=False)
    platform = validate_text("--platform", args.platform, required=False)
    location = validate_text("--location", args.location, required=False)

    assert company_name is not None
    assert role_title is not None

    repository_root = Path(__file__).resolve().parents[2]
    templates_dir = repository_root / "templates" / "applications"
    applications_dir = repository_root / "career" / "applications"
    application_slug = f"{month}-{company_slug}-{role_slug}"
    destination = applications_dir / application_slug

    missing_templates = [
        name for name in TEMPLATE_FILES if not (templates_dir / name).is_file()
    ]
    if missing_templates:
        missing = ", ".join(sorted(missing_templates))
        raise RuntimeError(f"Faltan plantillas requeridas: {missing}")

    if destination.exists() and not args.force:
        raise FileExistsError(
            f"La carpeta ya existe: {destination}. Usa --force solo si quieres "
            "sobrescribir los archivos administrados por el scaffold."
        )
    if destination.exists() and not destination.is_dir():
        raise RuntimeError(f"El destino existe pero no es una carpeta: {destination}")

    destination.mkdir(parents=True, exist_ok=True)
    generated_dir = destination / "generated"
    generated_dir.mkdir(exist_ok=True)

    for template_name, output_name in TEMPLATE_FILES.items():
        source = templates_dir / template_name
        rendered = render_template(
            source,
            application_slug=application_slug,
            company_name=company_name,
            role_title=role_title,
            source_url=source_url,
            platform=platform,
        )
        (destination / output_name).write_text(rendered, encoding="utf-8")

    submission_record = build_submission_record(
        application_slug=application_slug,
        company_name=company_name,
        role_title=role_title,
        source_url=source_url,
        platform=platform,
        location=location,
    )
    (destination / "submission-record.md").write_text(
        submission_record, encoding="utf-8"
    )

    generated_readme = """# Outputs generados

Esta carpeta está reservada para salidas desechables de una fase posterior.
El scaffold no genera CV, carta, mensaje de recruiter ni preparación de entrevista.
"""
    (generated_dir / "README.md").write_text(generated_readme, encoding="utf-8")
    return destination


def main() -> int:
    args = parse_args()
    try:
        destination = create_scaffold(args)
    except (ValueError, FileExistsError, RuntimeError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Candidatura preparada en: {destination}")
    print("Próximos pasos:")
    print("1. Pega la oferta original en job-description.md.")
    print("2. Ejecuta el workflow de Job Intake.")
    print("3. Revisa la selección de perfil objetivo.")
    print("4. Revisa la selección de evidencia.")
    print("5. Decide si procede generar outputs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
