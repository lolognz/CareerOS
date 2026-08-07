# Scripts de candidaturas

Para el recorrido completo desde el triage de una oferta real, consultar [Fast Application Workflow](../../docs/workflows/fast-application-workflow.md).

Los estados, eventos y actualizaciones posteriores de `submission-record.md` siguen [Application Lifecycle v1](../../career/application-lifecycle/README.md). Los scripts de esta carpeta no avanzan el lifecycle automáticamente.

## Crear un expediente nuevo

`create_application.py` crea la estructura inicial de una candidatura a partir de las seis plantillas de Job Intake. No analiza la oferta, selecciona perfiles o evidencia ni genera materiales de candidatura.

```bash
python scripts/applications/create_application.py \
  --date 2026-08 \
  --company-slug example-company \
  --role-slug senior-backend-engineer \
  --company-name "Example Company" \
  --role-title "Senior Backend Engineer" \
  --source-url "https://example.com/job"
```

Argumentos obligatorios:

- `--date`: mes de identificación en formato `YYYY-MM`.
- `--company-slug`: slug de empresa en minúsculas, con números y guiones simples.
- `--role-slug`: slug de rol con las mismas reglas.
- `--company-name`: nombre de la empresa tal como se conoce en la oportunidad.
- `--role-title`: título del puesto.

Argumentos opcionales:

- `--source-url`: URL de la oferta.
- `--platform`: plataforma o fuente de publicación.
- `--location`: ubicación o modalidad conocida.
- `--force`: permite sobrescribir los archivos administrados por el scaffold dentro de una carpeta ya existente.

Por seguridad, el script rechaza por defecto una carpeta de candidatura existente. `--force` no borra la carpeta ni archivos adicionales: vuelve a escribir solo los seis documentos basados en plantillas, `submission-record.md` y `generated/README.md`.

El resultado queda bajo `career/applications/YYYY-MM-company-slug-role-slug/` y, por tanto, se considera un expediente activo por defecto. El siguiente paso obligatorio es pegar la oferta original en `job-description.md`; el scaffold no inventa ni completa contenido de la oferta.

El scaffold deja `generated/` sin materiales. `generated/recruiter-message.md` y `generated/cv.md` solo se crean posteriormente mediante sus capas bajo `generators/`; no son responsabilidad de `create_application.py`.

Los expedientes creados únicamente como ejemplos deben prepararse intencionadamente bajo `examples/applications/` o moverse allí manualmente, dejando claro en su registro que son fixtures no canónicos y no candidaturas reales.

## Validar un expediente

Después de pegar la descripción original y antes de ejecutar Job Intake, validar la estructura:

```bash
python scripts/applications/validate_application.py \
  career/applications/2026-08-example-company-senior-backend-engineer
```

El resultado puede ser:

- `PASS`: estructura lista para Job Intake.
- `WARN`: usable, pero quedan precauciones como metadatos o encabezados pendientes. Devuelve código 0.
- `FAIL`: falta estructura obligatoria, la oferta original no está presente o existen outputs prematuros. Devuelve código 1.

Opciones:

```bash
# Tratar también los avisos como errores
python scripts/applications/validate_application.py RUTA --strict

# Permitir archivos ya existentes bajo generated/
python scripts/applications/validate_application.py RUTA --allow-generated
```

La validación es estructural y de solo lectura. No interpreta semánticamente la oferta, no comprueba el encaje profesional y no ejecuta el análisis de Job Intake.
