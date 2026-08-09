# Esquema de debrief de entrevista

## Propósito

Un debrief es un análisis trazable de una entrevista concreta a partir de notas brutas informadas por el usuario. Ayuda a aprender y planificar sin convertir recuerdos incompletos en historial exacto ni ejecutar actualizaciones derivadas.

## Campos obligatorios

| Campo | Descripción |
|---|---|
| `id` | ID estable: `interview-debrief:<application-slug>:<note-stem>`, derivado de la nota fuente sin inventar fecha o tipo. |
| `application_id` | ID del expediente: `application:<application-slug>`. |
| `source_application_folder` | Ruta relativa exacta de candidatura o fixture. |
| `output_type` | En v1, `interview-debrief`. |
| `interview_type` | Tipo documentado o `unknown`. |
| `interview_date` | Fecha recogida en la nota, `YYYY-MM-DD` o `desconocida`. |
| `language` | Idioma final y base de elección. |
| `status` | Estado del output. |
| `source_interview_notes` | Ruta de la única nota bruta principal; su filename stem determina el ID y el output por defecto. |
| `source_files_used` | Todas las rutas realmente leídas y su función; distingue contexto de fuente de lo ocurrido. |
| `application_status_before_interview` | Último estado demostrable anterior a la entrevista, con evento/fecha o `desconocido`; no es el estado al generar. |
| `interview_context` | Participantes, canal, duración, agenda y contexto conocidos, con ausencias visibles. |
| `questions_asked` | Preguntas recordadas como realmente formuladas, con grado de precisión. |
| `answers_given` | Respuestas o talking points recordados, enlazados a preguntas cuando sea posible. |
| `evidence_used` | Historias, ejemplos o hechos profesionales que el candidato recuerda haber usado; no los amplía. |
| `new_company_information` | Información atribuida a interlocutores sobre la empresa, pendiente de verificación cuando corresponda. |
| `new_role_information` | Información nueva sobre alcance, expectativas y éxito del rol. |
| `new_technical_information` | Información nueva sobre sistema, stack, arquitectura u operación, preservando atribución. |
| `new_process_information` | Etapa, feedback, plazo o siguiente paso comunicado; desconocido si no consta. |
| `conditions_discussed` | Compensación, contrato, modalidad, horario, disponibilidad u otras condiciones tratadas. |
| `strengths_observed` | Fortalezas inferidas de hechos de la conversación y autoevaluación etiquetada; no feedback inventado. |
| `weak_answers_or_gaps` | Respuestas que el candidato considera incompletas y gaps observables, separados de dificultad o impresión. |
| `missed_opportunities` | Puntos que podrían haberse preguntado o explicado, sin afirmar que habrían cambiado el resultado. |
| `follow_up_items` | Compromisos explícitos de cada parte y acciones recomendadas, distinguidos. |
| `lifecycle_implications` | Eventos/estados que una ejecución separada debería evaluar, con evidencia y campos faltantes. |
| `application_plan_implications` | Cambios propuestos al plan, o `[]`; no modifica el plan. |
| `risk_register_implications` | Riesgos a añadir, resolver o recalibrar de forma propuesta, o `[]`. |
| `canonical_knowledge_candidates` | Hechos profesionales potencialmente nuevos que requieren verificación canónica, o `[]`. |
| `next_interview_preparation_implications` | Ajustes propuestos para una ronda futura; no asume que exista. |
| `do_not_assume` | Conclusiones prohibidas por falta de evidencia o procedencia. |
| `uncertainty` | Recuerdos aproximados, ausencias, conflictos e inferencias. |
| `review_checklist` | Controles completados antes de usar o incorporar el debrief. |

## Valores permitidos

- `output_type`: `interview-debrief`.
- `interview_type`: `recruiter_screen`, `technical_interview`, `hiring_manager`, `leadership`, `final`, `unknown`.
- `status`: `draft`, `reviewed`, `incorporated`, `discarded`.

Todo output nuevo comienza en `draft`. `reviewed` requiere revisión del usuario contra sus recuerdos. `incorporated` significa que las propuestas aceptadas ya se procesaron mediante workflows separados; no autoriza al debrief a hacer esos cambios. `discarded` indica que esta versión no debe usarse.

## Categorías de procedencia

| Categoría | Significado |
|---|---|
| `factual_recollection` | El usuario recuerda que ocurrió o se dijo, con precisión declarada. |
| `candidate_impression` | Sensación, interpretación inmediata o autoevaluación del candidato. |
| `interviewer_statement` | Declaración atribuida a interviewer/recruiter, no verificación independiente. |
| `inference` | Análisis derivado de una o más fuentes, con confianza y límites. |
| `uncertainty` | Memoria aproximada, información ausente, ambigua o conflictiva. |

## Correspondencia con el documento

El output incluye, en este orden:

1. Metadata.
2. Resumen de la entrevista.
3. Qué ocurrió realmente.
4. Preguntas formuladas.
5. Respuestas dadas.
6. Evidencia e historias utilizadas.
7. Información nueva aprendida: empresa, rol, equipo, sistema técnico, proceso y condiciones.
8. Qué fue bien.
9. Respuestas o áreas a mejorar.
10. Oportunidades perdidas.
11. Follow-ups y compromisos.
12. Implicaciones para lifecycle.
13. Implicaciones para el plan de candidatura.
14. Implicaciones para el registro de riesgos.
15. Posibles actualizaciones de conocimiento canónico.
16. Implicaciones de preparación para una siguiente ronda.
17. Lista de supuestos prohibidos.
18. Incertidumbre.
19. Checklist final de revisión.

## Reglas de validación

- `source_interview_notes` existe dentro de `interviews/` del mismo expediente, se lee primero y no se modifica.
- La fuente sigue la convención `interviews/<note-stem>.md`. Se recomienda `<YYYY-MM-DD>-<interview-type>` cuando ambos datos constan; si no, se usa un stem estable sin inventarlos.
- El output por defecto se deriva de forma determinista como `generated/interview-debriefs/<note-stem>.md`, retirando únicamente la extensión del filename de `source_interview_notes`.
- Varias notas de entrevista deben producir debriefs distintos que coexistan bajo `generated/interview-debriefs/`; nunca se usa el singleton `generated/interview-debrief.md`.
- Una ejecución solo puede crear o reemplazar el debrief correspondiente a `source_interview_notes`. Antes de reemplazarlo debe revisarse si contiene cambios locales.
- `application_id` y carpeta son coherentes.
- El tipo y la fecha proceden de la nota o de contexto factual explícito; una contradicción se conserva.
- Solo `source_interview_notes` demuestra qué se recuerda que ocurrió. El resto aporta contexto o comparación.
- Preguntas de `interview-prep.md` son planificadas, no preguntas formuladas. Solo se compara si el archivo existía antes de la entrevista o su anterioridad está documentada.
- `opportunity-dossier.md` aporta incógnitas previas/contexto de empresa, nunca evidencia candidata ni prueba de lo dicho en entrevista.
- No se reconstruyen preguntas, respuestas, agenda, reacciones o feedback a partir de la oferta, preparación o patrones habituales.
- Citas textuales requieren que la nota las marque como recordadas con precisión; si no, usar paráfrasis y conservar incertidumbre.
- “Creo”, “aproximadamente”, “no recuerdo” y equivalentes nunca se eliminan al sintetizar.
- `strengths_observed` separa hechos observables, autoevaluación y feedback explícito. Un tono cordial no es feedback positivo.
- `weak_answers_or_gaps` no clasifica automáticamente como mala una respuesta difícil, breve o sin reacción. Explica la evidencia y el límite.
- `follow_up_items` distingue compromiso explícito de acción recomendada; silencio posterior no es rechazo.
- Cada `lifecycle_implication` propone un `event_type`, estado posible y evidencia/campos faltantes conformes al lifecycle; no modifica el registro.
- `application_status_before_interview` no se deriva del tipo solicitado ni del estado posterior. Si el timeline no permite reconstruirlo, es `desconocido`.
- Información empresarial comunicada en entrevista conserva atribución y no se promueve automáticamente a hecho público verificado.
- Un hecho profesional previamente no documentado se incluye en `canonical_knowledge_candidates` con fuente, detalle, dudas y evidencia necesaria; no se crea una entidad ni un logro.
- El elogio o reacción del entrevistador nunca crea evidencia profesional o un achievement.
- Todos los campos obligatorios están presentes, aunque valgan `[]`, `desconocido` o `ninguno`.
- No quedan placeholders en el output.
- El único archivo creado o reemplazado es `<source_application_folder>/generated/interview-debriefs/<note-stem>.md`. Un `output_path` explícito debe permanecer bajo `generated/interview-debriefs/` del mismo expediente, corresponder inequívocamente a la nota indicada y no apuntar al debrief de otra entrevista.
