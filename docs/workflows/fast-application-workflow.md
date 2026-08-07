# Fast Application Workflow v1

## Objetivo

Procesar una oferta real con rapidez sin sacrificar evidencia, incertidumbre ni condiciones de parada. El flujo convierte una oferta preservada en una decisión auditable y genera solo el siguiente output que esa decisión permita.

Este workflow coordina herramientas existentes; no añade automatización. `create_application.py` crea el scaffold, `validate_application.py` comprueba su estructura y los análisis o outputs posteriores se ejecutan mediante sus prompts y workflows documentados.

## Regla de ubicación

- Candidatura real: `career/applications/<application-slug>/`.
- Fixture de prueba: `examples/applications/<example-slug>/`.

No iniciar una candidatura real bajo `examples/` ni tratar un fixture como historial profesional o de aplicación. Los outputs bajo `generated/` son desechables y no son fuente de verdad.

## Flujo rápido

### 1. Decidir si merece un expediente

Hacer un triage corto antes de crear archivos:

- ¿La familia de rol tiene relación razonable con algún perfil objetivo?
- ¿Existe algún requisito excluyente ya incompatible?
- ¿Ubicación, permiso de trabajo o modalidad bloquean claramente la oportunidad?
- ¿La oferta contiene suficiente información para identificar empresa y puesto?
- ¿La oportunidad merece análisis o una aclaración aunque falten salario u otros datos?

No crear expediente si el desajuste es inequívoco y no hubo contacto que responder. Sí puede merecer expediente una oferta incierta cuando una pregunta concreta puede cambiar la decisión.

### 2. Crear el scaffold

Desde la raíz del repositorio:

```bash
python scripts/applications/create_application.py \
  --date YYYY-MM \
  --company-slug company-slug \
  --role-slug role-slug \
  --company-name "Nombre publicado" \
  --role-title "Título publicado" \
  --source-url "https://example.com/job" \
  --platform "LinkedIn" \
  --location "Remoto"
```

Solo `--date`, `--company-slug`, `--role-slug`, `--company-name` y `--role-title` son obligatorios. Omitir argumentos opcionales desconocidos en vez de inventarlos. No usar `--force` salvo que se haya revisado expresamente qué archivos administrados sobrescribirá.

Guardar la ruta devuelta por el script, por ejemplo:

```text
career/applications/YYYY-MM-company-slug-role-slug
```

### 3. Preservar la oferta

Abrir `<RUTA>/job-description.md` y pegar el texto íntegro dentro de `## Texto original preservado`.

- No corregir, traducir, resumir ni reordenar.
- Completar metadatos solo cuando consten.
- Marcar truncamiento, formato perdido o secciones ausentes.
- No empezar el análisis mientras el placeholder principal siga presente.

### 4. Validar el expediente

```bash
python scripts/applications/validate_application.py \
  career/applications/YYYY-MM-company-slug-role-slug
```

- `PASS`: continuar.
- `WARN`: revisar los metadatos o encabezados señalados; puede continuar si la advertencia es conocida y aceptable.
- `FAIL`: corregir antes de Job Intake.

Para exigir una captura sin advertencias:

```bash
python scripts/applications/validate_application.py RUTA --strict
```

`--allow-generated` solo sirve para validar un expediente que ya tiene outputs. No debe usarse para justificar outputs creados antes del intake.

### 5. Ejecutar Job Intake

Usar el bloque «Job Intake» de [fast-application-prompts.md](fast-application-prompts.md) con la ruta real. Esta fase lee la oferta, compara perfiles, verifica entidades canónicas y completa:

- `job-intake.md`
- `target-profile-selection.md`
- `evidence-selection.md`
- `application-plan.md`
- `risk-register.md`

Job Intake no genera mensajes, CV, carta ni preparación de entrevista. Los gaps y blockers permanecen visibles; un requisito de la oferta nunca se convierte automáticamente en experiencia.

### 6. Revisar la decisión

Leer conjuntamente `target-profile-selection.md`, `application-plan.md` y `risk-register.md`. Comprobar que la recomendación, los outputs permitidos y sus dependencias coinciden.

#### `no aplicar`

- No generar CV.
- Si no hubo contacto, cerrar el expediente y actualizar `submission-record.md`.
- Si hubo contacto documentado, se puede generar un mensaje `polite-decline` y revisarlo antes de enviarlo.

#### `aplicar tras aclarar`

- Generar primero `generated/recruiter-message.md` con `message_type: clarification-first` si existe un canal adecuado.
- Formular solo preguntas que puedan cambiar la decisión o el output.
- No generar CV mientras el plan lo condicione a blockers pendientes.
- Registrar el contacto y las respuestas en `submission-record.md`.
- Si las respuestas cambian el encaje, actualizar primero intake, plan y riesgos; después revisar de nuevo la recomendación.

#### `aplicar de forma selectiva`

- Revisar riesgos abiertos y dependencias del plan.
- Elegir mensaje a recruiter si una aclaración puede cambiar el posicionamiento, la decisión o las condiciones.
- Elegir CV si los riesgos restantes pueden mitigarse honestamente mediante omisión o redacción conservadora y el plan permite generarlo.
- No generar ambos por inercia.

#### `aplicar`

- Generar `generated/cv.md` mediante CV Generator v1 cuando el plan lo permita.
- Generar un mensaje `apply` solo si el canal o la estrategia lo justifican.
- Cada output se ejecuta por separado y se detiene al terminar; uno no autoriza los demás.

## Tabla de siguiente acción

| Decisión | Siguiente acción por defecto | CV |
|---|---|---|
| `no aplicar` | Cerrar o `polite-decline` si hubo contacto. | No generar. |
| `aplicar tras aclarar` | Mensaje `clarification-first`. | Esperar si el plan lo condiciona. |
| `aplicar de forma selectiva` | Mensaje o CV según riesgos abiertos. | Solo si el plan lo permite. |
| `aplicar` | CV; mensaje `apply` si aporta valor. | Generar si pasa precondiciones. |

### 7. Generar solo el output autorizado

Usar un único prompt de [fast-application-prompts.md](fast-application-prompts.md):

- `clarification-first`, `apply` o `polite-decline` para `generated/recruiter-message.md`;
- CV para `generated/cv.md` únicamente cuando no exista una condición de parada.

No encadenar prompts para crear carta, LinkedIn, PDF, DOCX, HTML o entrevista. Si el generador se detiene, conservar el blocker; no suavizarlo para obtener un output.

### 8. Revisar manualmente

Antes de usar cualquier output:

- comparar claims con `evidence-selection.md` y las entidades citadas;
- comprobar gaps, riesgos y claims evitados;
- revisar idioma, audiencia, fechas, títulos y datos de contacto;
- eliminar cualquier exageración, pero corregir primero la fuente si el problema es factual;
- cambiar el estado a `reviewed` solo después de una revisión real.

La auditoría del CV no está destinada al envío. Después de revisar `generated/cv.md`, [CV Finalizer v1](../../generators/cv-finalizer/README.md) puede extraer el bloque candidato y crear Markdown enviable, HTML imprimible e instrucciones de exportación manual. Finalizar no autoriza cambios factuales ni genera el PDF.

### 9. Registrar cada acción

Después de enviar, descartar, recibir respuesta o cerrar una candidatura, usar el prompt de actualización de `submission-record.md`.

Registrar únicamente hechos conocidos:

- fecha y canal;
- output enviado o descartado;
- destinatario, si consta;
- respuesta o ausencia de respuesta, solo cuando pueda afirmarse;
- estado actual, outcome y próximo paso.

No editar un output generado para convertirlo en historial. El historial de la candidatura pertenece a `submission-record.md`.

### 10. Versionar con intención

Revisar antes de preparar un commit:

```bash
git status --short
git diff -- career/applications/YYYY-MM-company-slug-role-slug
```

Versionar solo artefactos de candidatura que aporten historial o análisis significativo y sean apropiados para el repositorio. Los outputs generados siguen siendo desechables aunque se decida conservar alguno por una política explícita. No incluir secretos, datos privados inesperados, placeholders irrelevantes ni cambios ajenos.

Este workflow no ejecuta `git add`, `git commit` ni `git push` automáticamente.

## Condiciones globales de parada

Detener el flujo cuando:

- la oferta original no está preservada;
- la validación devuelve `FAIL`;
- falta evidencia canónica o un ID no resuelve;
- intake, perfil, plan y riesgos se contradicen materialmente;
- un blocker exigido por el plan sigue abierto;
- generar requiere inventar o esconder un gap;
- el siguiente paso requiere una decisión humana no documentada.

La salida correcta puede ser `no aplicar`, esperar una respuesta o no generar nada.
