# Esquema de preparación de entrevista

## Propósito

Una preparación de entrevista es una vista práctica y trazable de una candidatura concreta. Combina hechos de la oportunidad, estrategia documentada y evidencia profesional seleccionada sin crear claims nuevos. Es un output reemplazable, no conocimiento canónico ni historial del proceso.

## Campos obligatorios

| Campo | Descripción |
|---|---|
| `id` | ID estable con formato `interview-prep:<application-slug>:<interview-type>`. |
| `application_id` | ID del expediente con formato `application:<application-slug>`. |
| `source_application_folder` | Ruta relativa exacta de la candidatura o fixture. |
| `output_type` | Tipo del output; en v1 solo admite `interview-prep`. |
| `interview_type` | Tipo de entrevista solicitado o `unknown`. |
| `language` | Idioma del material y base documentada de la elección. |
| `status` | Estado permitido del output. |
| `source_files_used` | Rutas de inputs, perfil y entidades autorizadas realmente leídas. |
| `application_status_at_generation` | Estado factual leído de `submission-record.md`, con fecha/evidencia o incertidumbre. |
| `target_profile` | ID del perfil objetivo utilizado, o `[]` si el expediente lo justifica. |
| `role_summary` | Resumen factual de puesto, responsabilidades y etapa; separa literalidad e inferencia. |
| `company_context` | Empresa, cliente, intermediario y contexto conocidos; incógnitas explícitas. |
| `candidate_positioning` | Posicionamiento para esta conversación, respaldado y limitado. |
| `evidence_selected` | IDs canónicos y uso conversacional previsto. |
| `stories_selected` | Historias o combinaciones de evidencia preparadas, con fuentes y límites. |
| `risks_and_gaps` | Riesgos, gaps y requisitos parciales relevantes para la conversación. |
| `gap_handling_strategy` | Respuesta honesta para cada gap: reconocer, delimitar, conectar evidencia adyacente y preguntar. |
| `likely_questions` | Preguntas probables por categoría, etiquetadas como hipótesis. |
| `answer_bank` | Puntos de respuesta trazables; no nuevos hechos ni guiones inflados. |
| `star_stories` | Situación, tarea, acción y resultado respaldados; incertidumbre preservada. |
| `questions_to_ask` | Preguntas priorizadas para recruiter, empresa o entrevistador. |
| `red_flags_to_clarify` | Señales y condiciones que requieren aclaración, sin convertirlas en conclusiones. |
| `compensation_or_conditions_notes` | Compensación, modalidad, ubicación, contrato y disponibilidad conocidos o pendientes. |
| `do_not_claim` | Claims prohibidos por falta de evidencia, atribución, alcance o título. |
| `review_checklist` | Controles factuales y prácticos completados antes de usar el material. |
| `uncertainty` | Datos desconocidos, inferencias, conflictos y preguntas pendientes. |

## Valores permitidos

- `output_type`: `interview-prep`.
- `interview_type`: `recruiter_screen`, `technical_interview`, `hiring_manager`, `leadership`, `final`, `unknown`.
- `status`: `draft`, `reviewed`, `used`, `discarded`.

Todo output nuevo comienza en `draft`. `reviewed` exige revisión factual y práctica; `used`, evidencia de que se utilizó para preparar o realizar una entrevista; `discarded`, decisión de no usarlo. Generar el archivo no actualiza el estado de la candidatura.

## Correspondencia con el documento

El output debe incluir, en este orden:

1. Metadata.
2. Contexto de la entrevista.
3. Resumen de la oportunidad.
4. Posicionamiento del candidato para esta entrevista.
5. Pitch de 30 segundos.
6. Pitch de 60 segundos.
7. Evidencia clave a enfatizar.
8. Historias STAR a preparar.
9. Manejo de gaps.
10. Preguntas probables de recruiter.
11. Preguntas técnicas probables.
12. Preguntas conductuales probables.
13. Banco de respuestas.
14. Preguntas para empresa o recruiter.
15. Red flags y condiciones que aclarar.
16. Lista de claims que no deben hacerse.
17. Checklist final antes de la llamada.
18. Incertidumbre e información pendiente.

Los campos `likely_questions`, `answer_bank` y `star_stories` pueden distribuirse entre sus secciones visibles, pero deben seguir siendo trazables desde Metadata.

## Reglas de validación

- Los siete documentos obligatorios del expediente deben leerse siempre. `recruiter-conversation.md` se lee cuando existe. Falta de cualquiera de los siete obligatorios activa una condición de parada.
- `application_status_at_generation` procede de `submission-record.md`; no se deriva de la presencia de outputs.
- `interview_type` no se infiere como técnico por el título del puesto ni por una conversación con recruiter.
- El perfil objetivo debe existir cuando el expediente referencia uno.
- Solo se leen entidades canónicas cuyos IDs aparecen en `evidence-selection.md`, `target-profile-selection.md` o `application-plan.md`.
- Cada claim de pitches, evidencia, respuestas y STAR debe mapearse a una fuente leída y conservar sus límites.
- La descripción de la oferta y las preguntas probables no se convierten en experiencia del candidato.
- Un gap permanece visible en `risks_and_gaps`, `gap_handling_strategy`, `do_not_claim` o `uncertainty` según corresponda.
- Una respuesta de gap no afirma experiencia directa inexistente. Puede usar evidencia adyacente solo si se etiqueta como tal.
- Colaboración con DevOps no equivale a ownership de plataforma; exposición parcial a Linux/cloud no equivale a administración o dominio; liderazgo sin título no equivale a Tech Lead formal; experiencia en sistemas críticos no prueba por sí sola escala o baja latencia.
- STAR no completa resultados, métricas, decisiones o responsabilidades ausentes.
- Compensación, disponibilidad, modalidad y condiciones se registran como conocidas o pendientes, nunca se estiman.
- Las preguntas para la otra parte deben resolver alcance, riesgos o decisión; no pueden presuponer una oferta o una fase no confirmada.
- No quedan placeholders en el output generado.
- El único archivo creado o reemplazado es `<source_application_folder>/generated/interview-prep.md`.

