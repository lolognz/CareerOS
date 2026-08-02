# Prompt reutilizable de Job Intake

## Prompt

```text
Analiza esta oportunidad mediante el workflow Job Intake de CareerOS.

Lee antes de actuar:
- knowledge/CONSTITUTION.md
- docs/entity-model.md
- los esquemas y entidades canónicas relevantes bajo knowledge/
- career/target-profiles/target-profile.schema.md
- career/target-profiles/index.md
- todos los perfiles objetivo vigentes
- career/job-intake/job-intake.schema.md
- career/job-intake/job-intake-workflow.md
- las plantillas bajo templates/applications/

Entrada:
- Slug de candidatura: [YYYY-MM-company-role]
- Texto o archivo de la oferta: [entrada]
- URL o fuente: [si existe]
- Fecha de detección: [si se conoce]
- Notas del usuario: [si existen]

Objetivo:
Crear los documentos de análisis y planificación de una candidatura concreta. No generar todavía CV, carta de presentación, mensaje de recruiter, resumen de LinkedIn ni respuestas de entrevista.

Orden obligatorio:
1. Preserva primero la oferta original en job-description.md, sin corregirla, traducirla, resumirla ni reordenarla.
2. Extrae los requisitos en job-intake.md y separa texto explícito de inferencias.
3. Compara todos los perfiles objetivo en target-profile-selection.md. Recomienda como máximo uno primario, perfiles secundarios opcionales y registra descartes. Si ninguno encaja, dilo.
4. Verifica y selecciona evidencia canónica en evidence-selection.md. Usa IDs solo si sus archivos existen.
5. Registra riesgos y gaps en risk-register.md; no ocultes requisitos sin respaldo.
6. Define la decisión y las instrucciones para futuras salidas en application-plan.md. Puedes recomendar no aplicar.
7. Valida trazabilidad y detente.

Reglas:
- Escribe en español.
- No busques en la web salvo autorización explícita posterior.
- No inventes hechos ni completes la oferta por plausibilidad.
- No conviertas requisitos de la oferta en experiencia del candidato.
- No infles seniority, autoridad, atribución, métricas ni madurez.
- No modifiques conocimiento canónico ni perfiles objetivo durante el intake.
- Si descubres un enlace roto, repórtalo; no lo repares dentro de esta ejecución sin autorización.
- Marca cada requisito como respaldado, parcial, no respaldado, desconocido o no aplicable.
- Conserva incertidumbre y límites de evidencia en todos los documentos afectados.
- Prioriza una decisión útil y auditable que permita preparar la candidatura en menos de 24 horas.

Resultado esperado:
- job-description.md
- job-intake.md
- target-profile-selection.md
- evidence-selection.md
- application-plan.md
- risk-register.md

No crees ni completes generated/ ni submission-record.md en esta fase.
```

## Criterio de finalización

El prompt termina cuando los seis documentos son coherentes y verificables. Una recomendación de `no aplicar` o `sin encaje suficiente` es un resultado válido.
