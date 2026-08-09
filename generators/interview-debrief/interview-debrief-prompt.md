# Prompt reutilizable: generar debrief de entrevista

Copia este prompt en Codex o ChatGPT y sustituye los parámetros. La nota bruta debe existir antes de ejecutarlo.

```text
Genera un debrief trazable y constructivo de una entrevista de CareerOS.

Parámetros:
- source_application_folder: [career/applications/<application-slug> o examples/applications/<example-slug>]
- source_interview_notes: [interviews/<note-stem>.md; por ejemplo interviews/2026-08-07-recruiter_screen.md]
- interview_type: [recruiter_screen / technical_interview / hiring_manager / leadership / final / unknown]
- language: [es / en / auto]
- output_path: [opcional; por defecto generated/interview-debriefs/<source-note-stem>.md]

Lee primero y por completo:
- source_application_folder/source_interview_notes

No leas aún otros archivos. Extrae de la nota únicamente lo recordado: contexto, preguntas, respuestas, evidencia usada, declaraciones de interlocutores, impresiones, compromisos, citas precisas e incertidumbre. No reconstruyas huecos.

Después lee el contrato:
- generators/interview-debrief/README.md
- generators/interview-debrief/interview-debrief.schema.md
- generators/interview-debrief/interview-debrief-workflow.md
- templates/generated/interview-debrief.template.md

Lee después el contexto disponible y relevante:
- source_application_folder/submission-record.md
- source_application_folder/job-description.md
- source_application_folder/recruiter-conversation.md, si existe
- source_application_folder/job-intake.md
- source_application_folder/application-plan.md
- source_application_folder/risk-register.md
- source_application_folder/target-profile-selection.md
- source_application_folder/evidence-selection.md
- source_application_folder/generated/opportunity-dossier.md, si existe
- source_application_folder/generated/interview-prep.md, solo si existía antes de la entrevista o su anterioridad está documentada

Reglas:

1. Verifica carpeta, application_id, nota, interview_type y language. La nota debe estar dentro de interviews/ del mismo expediente.
2. Deriva source-note-stem retirando únicamente la extensión `.md` del filename de source_interview_notes. No reconstruyas el nombre desde interview_date o interview_type ni inventes esos datos. El output por defecto es generated/interview-debriefs/<source-note-stem>.md.
3. Si output_path se proporciona explícitamente, exige que permanezca bajo generated/interview-debriefs/ del mismo expediente, que corresponda inequívocamente a source_interview_notes y que no apunte al debrief de otra entrevista. Nunca uses generated/interview-debrief.md.
4. Antes de reemplazar el debrief correspondiente, revisa si contiene cambios locales. No modifiques debriefs asociados a otras notas.
5. Nunca modifiques source_interview_notes. Es la fuente primaria de lo que el usuario recuerda que ocurrió; el debrief nunca la sustituye.
6. Clasifica cada afirmación relevante como factual_recollection, candidate_impression, interviewer_statement, inference o uncertainty.
7. Conserva “creo”, “aproximadamente”, “no recuerdo” y cualquier grado de duda. Usa cita textual solo si la nota indica recuerdo exacto; en otro caso, paráfrasis atribuida.
8. Determina application_status_before_interview desde el último evento demostrable anterior. Si no puede reconstruirse, usa desconocido. No lo infieras del tipo de entrevista ni del estado posterior.
9. Distingue planned de actual. Interview Prep solo muestra qué se preparó; no demuestra qué se preguntó o respondió. Su ausencia en notas incompletas tampoco demuestra que no se usara.
10. Opportunity Dossier solo muestra contexto e incógnitas previas. Una respuesta del interviewer conserva atribución y no se convierte automáticamente en hecho público verificado.
11. No reconstruyas la entrevista desde job-description.md, preguntas esperables, patrones habituales o memoria general.
12. Registra preguntas realmente recordadas y respuestas/talking points realmente recordados. Si no puede enlazarse una respuesta con una pregunta, dilo.
13. Identifica evidencia e historias que el candidato recuerda haber usado. No completes fechas, resultados, métricas, ownership o reacciones ausentes.
14. Identifica información nueva sobre empresa, rol, equipo, sistema técnico, proceso y condiciones comparando con el contexto anterior. Señala fuente, emisor, precisión y necesidad de verificación.
15. Analiza qué fue bien usando hechos observables, autoevaluación etiquetada o feedback explícito. Un tono positivo no es feedback de contratación.
16. Analiza respuestas o áreas a mejorar sin convertir una pregunta difícil, una respuesta breve o el silencio del interviewer en evaluación negativa.
17. Identifica oportunidades perdidas como posibilidades, no como causas de un resultado. Con notas incompletas, admite que quizá no quedaron capturadas.
18. Separa compromisos explícitos del candidato, compromisos atribuidos a la otra parte, acciones recomendadas e incertidumbres. Silencio posterior no es rechazo.
19. Propón lifecycle_implications con event_type, fecha/canal/contacto/hecho disponibles, estado posible y campos faltantes, pero no actualices submission-record.md ni lifecycle.
20. Propón, sin ejecutar, implicaciones para application-plan.md, risk-register.md, Opportunity Dossier e Interview Prep futura.
21. Si aparece un hecho profesional del candidato antes no documentado, añádelo a canonical_knowledge_candidates con fuente, dudas y evidencia requerida. No crees entidades ni achievements; elogios del interviewer no son conocimiento canónico.
22. No inventes feedback, decisión, siguiente etapa, oferta, rechazo, reacción o probabilidad de éxito.
23. Completa las 19 secciones de templates/generated/interview-debrief.template.md, elimina placeholders, usa desconocido/[] cuando proceda y marca status: draft.
24. Revisa cada descripción de lo ocurrido contra la nota y completa el checklist.
25. Escribe únicamente el output correspondiente a source_interview_notes bajo source_application_folder/generated/interview-debriefs/. Si no se proporcionó output_path, usa source_application_folder/generated/interview-debriefs/<source-note-stem>.md.
26. Detente. No modifiques la nota, otros debriefs, submission-record.md, plan, riesgos, dossier, prep, conocimiento canónico, perfiles, CVs ni otros outputs; no envíes follow-ups.

Si las notas son incompletas, genera un debrief limitado y explícito. Si están vacías, solo contienen placeholders o no confirman que ocurrió una entrevista, detente sin generar y explica la condición.
```
