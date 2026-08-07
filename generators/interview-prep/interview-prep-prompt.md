# Prompt reutilizable: generar preparación de entrevista

Copia este prompt en Codex o ChatGPT y sustituye los parámetros. Debe ejecutarse desde un repositorio CareerOS con acceso al expediente indicado.

```text
Genera material práctico y basado en evidencia para preparar una entrevista de CareerOS.

Parámetros:
- source_application_folder: [career/applications/<application-slug> o examples/applications/<example-slug>]
- interview_type: [recruiter_screen / technical_interview / hiring_manager / leadership / final / unknown]
- language: [es / en / auto]
- focus_areas: [lista opcional o ninguno]
- known_interview_details: [tipo, fecha, formato, participantes o agenda confirmados; opcional]
- output_path: [generated/interview-prep.md por defecto]

Lee primero el expediente, en este orden:
- source_application_folder/job-description.md
- source_application_folder/recruiter-conversation.md, si existe
- source_application_folder/job-intake.md
- source_application_folder/target-profile-selection.md
- source_application_folder/evidence-selection.md
- source_application_folder/application-plan.md
- source_application_folder/risk-register.md
- source_application_folder/submission-record.md

Lee después el contrato del generador y el lifecycle:
- generators/interview-prep/README.md
- generators/interview-prep/interview-prep.schema.md
- generators/interview-prep/interview-prep-workflow.md
- templates/generated/interview-prep.template.md
- career/application-lifecycle/README.md
- career/application-lifecycle/application-statuses.md

Después:

1. Verifica que la carpeta, application_id, inputs obligatorios y output_path cumplen las precondiciones. output_path debe permanecer dentro de generated/ del mismo expediente.
2. Determina el estado y la etapa actuales exclusivamente desde submission-record.md. No confundas una conversación con recruiter con una entrevista técnica ni una etapa probable con una entrevista confirmada.
3. Lee el perfil objetivo referenciado por el expediente.
4. Extrae los IDs canónicos citados en evidence-selection.md, target-profile-selection.md y application-plan.md. Resuélvelos por su valor exacto usando knowledge/indexes/entity-index.md y lee únicamente esas entidades. No sigas relaciones ni añadas evidencia cercana no referenciada.
5. No uses generated/cv.md, CVs finales, mensajes u otros outputs como fuentes factuales salvo instrucción explícita. Incluso entonces, contrasta cada claim con las fuentes autorizadas; un output no aporta evidencia nueva.
6. Separa en todo el documento: hechos conocidos, inferencias etiquetadas, información que debe preguntarse y claims que no deben hacerse.
7. Resume la oportunidad, empresa/cliente/intermediario y contexto de entrevista sin convertir requisitos de la oferta en experiencia del candidato.
8. Construye un posicionamiento específico para interview_type usando solo el perfil, plan y evidencia leídos. Respeta títulos, fechas, atribución, seniority, métricas, alcance e incertidumbre.
9. Prepara pitches naturales de 30 y 60 segundos. Cada afirmación debe tener fuente y límite; no inventes motivación, disponibilidad, escala, ownership o resultados.
10. Selecciona evidencia clave y entre dos y cuatro historias STAR. Para cada historia incluye situación, tarea, acción, resultado, fuente, límite y versión breve. No completes piezas ausentes ni conviertas contribución compartida en autoría individual.
11. Mantén visibles riesgos y gaps. Para cada gap prepara: reconocimiento directo, alcance real, evidencia adyacente respaldada y una pregunta de aclaración. No presentes colaboración DevOps como ownership, exposición parcial a Linux/cloud como dominio, liderazgo sin título como Tech Lead formal ni sistemas críticos como prueba automática de alta escala o baja latencia.
12. Prepara preguntas probables de recruiter, técnicas y conductuales, adaptando prioridad al tipo de entrevista. Etiquétalas como hipótesis salvo que known_interview_details las confirme.
13. Crea un banco de respuestas en bullets para las preguntas prioritarias. Incluye mensaje central, evidencia, límites, follow-up probable y claim que evitar.
14. Formula preguntas concretas para empresa o recruiter sobre rol, equipo, sistema, operación, proceso y siguiente fase. Convierte gaps y red flags en aclaraciones honestas.
15. Separa compensación, modalidad, ubicación, contrato y disponibilidad conocidos de lo pendiente. No estimes datos ausentes.
16. Completa las 18 secciones de templates/generated/interview-prep.template.md. Elimina placeholders, conserva uncertainty y marca status: draft.
17. Revisa cada claim contra sus fuentes y completa el checklist del workflow. El documento debe ser escaneable y utilizable en una preparación real de 30–60 minutos.
18. Escribe únicamente source_application_folder/output_path, que por defecto es source_application_folder/generated/interview-prep.md.
19. Detente. No envíes mensajes, no actualices lifecycle o submission-record.md, no generes CVs, no modifiques análisis, conocimiento canónico, perfiles, otras candidaturas ni otros outputs.
```
