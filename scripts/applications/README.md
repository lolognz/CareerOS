# Scripts de candidaturas

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

El resultado queda bajo `career/applications/YYYY-MM-company-slug-role-slug/`. El siguiente paso obligatorio es pegar la oferta original en `job-description.md`; el scaffold no inventa ni completa contenido de la oferta.
