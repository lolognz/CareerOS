# Prompts rápidos de candidatura

Sustituir `RUTA` por una carpeta real bajo `career/applications/`. Estos prompts no convierten fixtures de `examples/applications/` en candidaturas reales.

## Ejecutar Job Intake

```text
Ejecuta Job Intake de CareerOS sobre esta candidatura real:

RUTA: career/applications/YYYY-MM-company-role/

Lee primero:
- knowledge/CONSTITUTION.md
- docs/entity-model.md
- career/job-intake/job-intake.schema.md
- career/job-intake/job-intake-workflow.md
- career/job-intake/job-intake-prompt.md
- career/target-profiles/target-profile.schema.md
- career/target-profiles/index.md
- todos los perfiles objetivo vigentes
- templates/applications/*.md
- todos los archivos actuales de RUTA

Precondiciones:
- La carpeta ya fue creada con scripts/applications/create_application.py.
- La oferta original ya está preservada en RUTA/job-description.md.
- scripts/applications/validate_application.py RUTA no devuelve FAIL.

Completa únicamente los documentos de análisis del expediente:
- job-intake.md
- target-profile-selection.md
- evidence-selection.md
- application-plan.md
- risk-register.md

Verifica cada ID contra conocimiento canónico. Separa oferta, inferencia y evidencia. Conserva gaps, blockers, riesgos, límites e incertidumbre. Emite exactamente una recomendación permitida: no aplicar, aplicar tras aclarar, aplicar de forma selectiva o aplicar.

No modifiques el texto original de job-description.md, conocimiento canónico, perfiles objetivo, submission-record.md ni generated/. No generes CV, carta, mensaje, LinkedIn ni preparación de entrevista. Detente al entregar el plan coherente.
```

## Generar mensaje `clarification-first`

```text
Ejecuta Recruiter Message Generator v1 sobre esta candidatura:

source_application_folder: career/applications/YYYY-MM-company-role/
message_type: clarification-first
channel: auto
language: auto
variants: 0

Lee generators/recruiter-message/README.md, recruiter-message.schema.md, recruiter-message-workflow.md, recruiter-message-prompt.md, la plantilla y los siete inputs del expediente.

Confirma que la recomendación es aplicar tras aclarar o que existen incógnitas materiales. Genera únicamente career/applications/YYYY-MM-company-role/generated/recruiter-message.md. Resume el encaje más fuerte sin sobreafirmar y formula entre dos y cuatro preguntas que puedan cambiar la decisión. Los gaps pueden convertirse en preguntas, nunca en claims.

No generes CV ni otros materiales. No modifiques inputs ni conocimiento canónico. Si una precondición falla, no generes y explica la condición de parada.
```

## Generar mensaje `apply`

```text
Ejecuta Recruiter Message Generator v1 sobre esta candidatura:

source_application_folder: career/applications/YYYY-MM-company-role/
message_type: apply
channel: auto
language: auto
variants: 0

Lee generators/recruiter-message/README.md, recruiter-message.schema.md, recruiter-message-workflow.md, recruiter-message-prompt.md, la plantilla y los siete inputs del expediente.

Confirma que el plan permite aplicar sin aclaraciones bloqueantes. Genera únicamente career/applications/YYYY-MM-company-role/generated/recruiter-message.md. Usa solo dos o tres señales de encaje respaldadas y pide siguientes pasos. Menciona interés, disponibilidad o contacto previo únicamente si constan.

No generes CV ni otros materiales. No modifiques inputs ni conocimiento canónico. Si el tipo contradice la decisión o queda un blocker, detente sin generar.
```

## Generar mensaje `polite-decline`

```text
Ejecuta Recruiter Message Generator v1 sobre esta candidatura:

source_application_folder: career/applications/YYYY-MM-company-role/
message_type: polite-decline
channel: auto
language: auto
variants: 0

Lee generators/recruiter-message/README.md, recruiter-message.schema.md, recruiter-message-workflow.md, recruiter-message-prompt.md, la plantilla y los siete inputs del expediente.

Confirma que la decisión documentada es no aplicar o no continuar y que hubo un contacto que justifica responder. Genera únicamente career/applications/YYYY-MM-company-role/generated/recruiter-message.md. Agradece y rechaza con claridad; incluye un motivo general o deja la puerta abierta solo si está respaldado.

No inventes contacto, intención futura ni motivos. No generes CV ni otros materiales. Si falta evidencia de contacto o el tipo contradice el expediente, detente sin generar.
```

## Generar CV cuando el plan lo permita

```text
Ejecuta CV Generator v1 sobre esta candidatura:

source_application_folder: career/applications/YYYY-MM-company-role/
language: auto
target_length: 1-2 páginas

Lee generators/cv/README.md, cv.schema.md, cv-workflow.md, cv-prompt.md, templates/generated/cv.template.md y los siete inputs del expediente. Lee también el perfil objetivo y todas las entidades canónicas referenciadas por evidence-selection.md y target-profile-selection.md.

Antes de redactar, confirma que application-plan.md permite generar el CV ahora. Si la recomendación es aplicar tras aclarar y el plan condiciona el CV a blockers todavía abiertos, detente sin crear el archivo.

Si pasa todas las precondiciones, genera únicamente career/applications/YYYY-MM-company-role/generated/cv.md con un bloque candidato limpio y una auditoría separada. Conserva títulos, empleadores, fechas, cronología, atribución y límites. No conviertas requisitos en experiencia, fit parcial en ownership completo, liderazgo informal en Tech Lead formal ni proyectos personales en empleo.

No generes carta, recruiter message, PDF, DOCX, HTML, LinkedIn ni entrevista. No modifiques inputs ni conocimiento canónico.
```

## Actualizar `submission-record.md`

Esta actualización debe seguir [Application Lifecycle v1](../../career/application-lifecycle/README.md). Para nuevas ejecuciones se recomienda usar directamente su [prompt de actualización](../../career/application-lifecycle/submission-record-update-prompt.md).

```text
Actualiza el registro de esta candidatura real:

RUTA: career/applications/YYYY-MM-company-role/
Evento: [enviado / descartado / respuesta recibida / candidatura cerrada / otro hecho]
Fecha: [YYYY-MM-DD o desconocida]
Canal: [LinkedIn / email / portal / desconocido]
Output afectado: [recruiter-message.md / cv.md / ninguno]
Destinatario: [dato conocido o desconocido]
Detalle factual: [qué ocurrió, sin interpretación inventada]
Nuevo estado: [estado conocido]
Outcome: [resultado conocido o pendiente]
Próximo paso: [acción acordada o pendiente]

Lee primero todos los archivos de RUTA necesarios para conservar coherencia y cronología. Modifica únicamente RUTA/submission-record.md.

Añade el evento sin borrar hechos históricos. No marques un mensaje como enviado, un CV como presentado ni una respuesta como recibida sin evidencia proporcionada. No inventes fechas, destinatarios, respuestas, interés, outcome ni próximos pasos. Si el evento cambia materialmente el encaje o resuelve blockers, registra el hecho y señala que job-intake.md, application-plan.md y risk-register.md requieren una revisión separada; no los modifiques en esta ejecución.

No modifiques generated/, conocimiento canónico, perfiles ni otros documentos del expediente. Detente después de actualizar el registro.
```
