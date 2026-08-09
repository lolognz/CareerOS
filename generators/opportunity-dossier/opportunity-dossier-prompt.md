# Prompt reutilizable: generar dossier de oportunidad

Copia este prompt en Codex o ChatGPT y sustituye los parámetros. Debe ejecutarse desde un repositorio CareerOS con acceso al expediente y a las fuentes indicadas. En v1 no debe navegar por Internet ni llamar APIs.

```text
Genera un dossier práctico de investigación y decisión para una oportunidad concreta de CareerOS.

Parámetros:
- source_application_folder: [career/applications/<application-slug> o examples/applications/<example-slug>]
- research_mode: [source_only / external_research]
- language: [es / en / auto]
- external_research_sources: [opcional: notas pegadas, URLs con contenido o contexto, snippets, resultados web ya obtenidos o rutas de archivos; [] si no hay]
- focus_areas: [lista opcional o ninguno]
- output_path: [generated/opportunity-dossier.md por defecto]

Lee primero, en este orden:
- source_application_folder/job-description.md
- source_application_folder/recruiter-conversation.md, si existe
- source_application_folder/job-intake.md
- source_application_folder/application-plan.md
- source_application_folder/risk-register.md
- source_application_folder/submission-record.md

Puedes leer después, solo si aportan contexto necesario:
- source_application_folder/target-profile-selection.md
- source_application_folder/evidence-selection.md

Lee también:
- generators/opportunity-dossier/README.md
- generators/opportunity-dossier/opportunity-dossier.schema.md
- generators/opportunity-dossier/opportunity-dossier-workflow.md
- templates/generated/opportunity-dossier.template.md

Reglas de ejecución:

1. Verifica que source_application_folder, application_id, inputs obligatorios, research_mode, language y output_path cumplen el contrato. output_path debe permanecer dentro de generated/ del mismo expediente.
2. Determina application_status_at_generation únicamente desde submission-record.md. Es un snapshot; no actualices el lifecycle.
3. Determina si se conocen la empresa publicada, el intermediario, el empleador contractual y el cliente final. Usa company_or_client_known: true, partial o false. Si el cliente final es desconocido, dilo expresamente; no lo infieras.
4. Mantén separadas estas categorías en cada afirmación material: application_fact, recruiter_statement, external_research, user_note, inference y uncertainty. Incluye fuente y límite; toda inference debe indicar base y confianza.
5. En source_only, usa únicamente archivos del expediente, establece external_sources_used: [] y no completes huecos con conocimiento general del modelo.
6. En external_research, usa solo contenido entregado en external_research_sources. No navegues URLs, no llames APIs y no supongas el contenido de una URL. Si solo hay una URL sin contenido accesible, regístrala como referencia pendiente y no como respaldo factual.
7. Para cada fuente externa realmente usada registra título o descripción, tipo, URL o ruta, autor/editor y fecha cuando consten, fecha de consulta si fue aportada y limitaciones. Distingue investigación pública de notas del usuario.
8. No leas CVs finales ni generated/cv.md como fuentes factuales. No leas generated/interview-prep.md salvo instrucción explícita del usuario; si se autoriza, úsalo únicamente para evitar repetir preguntas y registra ese límite.
9. No resuelvas entidades canónicas ni amplíes evidence-selection.md. Company research no es evidencia del candidato y ninguna afirmación pública puede convertirse en claim de CV.
10. Resume empresa, producto y modelo de negocio solo desde evidencia disponible. Distingue usuarios, compradores y clientes; si el modelo de negocio no consta, escribe desconocido.
11. Resume mercado y contexto de clientes solo en lo relevante para esta candidatura. No copies textos largos, no resumas sitios completos y evita hype.
12. Resume el rol separando oferta literal, declaraciones del proceso e inferencias. Un requisito no prueba la realidad técnica actual ni experiencia del candidato.
13. Describe contexto técnico y operativo con lo conocido y lo pendiente: stack real frente a solicitado, arquitectura, datos, escala, latencia, infraestructura, despliegue, observabilidad, ownership, on-call, equipo y forma de trabajo. No rellenes ausencias.
14. Formula candidate_fit_implications únicamente desde el análisis ya documentado en el expediente. No añadas evidencia, experiencia, tecnologías, motivación ni claims del candidato.
15. Identifica riesgos, incógnitas, contradicciones y posibles red flags. Para cada una indica procedencia, impacto, confianza y cómo resolverla. No presentes una ausencia de información como prueba negativa.
16. Crea preguntas priorizadas para: a) resolver antes del siguiente paso, b) recruiter y c) interlocutor técnico. Deben ayudar a decidir si continuar, preparar, negociar o retirarse, sin asumir una etapa confirmada.
17. Incluye, cuando sigan abiertas y sean relevantes, preguntas como: qué hace exactamente el producto; quiénes son usuarios/clientes; qué posee el equipo backend; qué infraestructura poseen los desarrolladores; expectativas de latencia/escala; cómo es on-call; estructura del equipo; siguiente etapa; y éxito esperado en 3–6 meses.
18. Escribe decision_notes como criterios y opciones, no como cambio de application-plan.md. Si nueva información exige revisar plan o riesgos, señálalo para una ejecución separada.
19. Completa las 17 secciones de templates/generated/opportunity-dossier.template.md, elimina placeholders, conserva desconocidos e incertidumbre, y marca status: draft.
20. Revisa procedencia, separación de fuentes, utilidad de preguntas y do_not_assume.
21. Escribe únicamente source_application_folder/output_path, por defecto source_application_folder/generated/opportunity-dossier.md.
22. Detente. No modifiques conocimiento canónico, perfiles, expediente, lifecycle, estados, eventos ni otros outputs. No generes CV, recruiter message o interview prep.

Si research_mode es external_research pero no hay contenido externo utilizable, no inventes ni navegues: continúa solo si el expediente permite un dossier útil, establece external_sources_used: [], explica la limitación en uncertainty y deja preguntas abiertas. Si falla otra precondición material, no generes el archivo y explica la condición de parada.
```
