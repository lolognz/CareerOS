# Esquema de dossier de oportunidad

## Propósito

Un dossier de oportunidad es una vista reemplazable de investigación y decisión ligada a una candidatura. Organiza lo que se sabe sobre empresa, producto, negocio, mercado y rol sin mezclarlo con evidencia profesional del candidato ni con el historial del proceso.

## Campos obligatorios

| Campo | Descripción |
|---|---|
| `id` | ID estable con formato `opportunity-dossier:<application-slug>`. |
| `application_id` | ID del expediente con formato `application:<application-slug>`. |
| `source_application_folder` | Ruta relativa exacta de la candidatura o fixture. |
| `output_type` | Tipo del output; en v1 solo admite `opportunity-dossier`. |
| `research_mode` | Modo de investigación utilizado. |
| `language` | Idioma final y base documentada de la elección. |
| `status` | Estado permitido del output. |
| `source_files_used` | Rutas de archivos del expediente realmente leídos, con su función. |
| `external_sources_used` | Fuentes externas realmente disponibles y utilizadas, con título o descripción, tipo, URL o ruta, fecha si consta y limitaciones; `[]` en `source_only`. |
| `application_status_at_generation` | Snapshot literal del estado leído en `submission-record.md`, con fecha/evidencia o incertidumbre; no es una actualización de lifecycle. |
| `company_or_client_known` | `true`, `false` o `partial`, identificando por separado empresa publicada, intermediario y cliente final. |
| `company_summary` | Síntesis relevante para la oportunidad, con procedencia y desconocidos. |
| `product_summary` | Qué hace el producto o servicio, para quién y qué no se sabe. |
| `business_model` | Cómo parece crear y capturar valor, solo cuando las fuentes lo respaldan; si no, `desconocido`. |
| `market_context` | Mercado, clientes, alternativas o entorno regulatorio relevantes y respaldados. |
| `role_context` | Propósito, responsabilidades, etapa y expectativas del puesto, separando literalidad e inferencia. |
| `technical_context` | Stack, arquitectura, escala, latencia, datos, infraestructura y ownership conocidos o pendientes. |
| `operating_context` | Equipo, organización, proceso, despliegue, producción, guardias, modalidad y condiciones conocidas o pendientes. |
| `candidate_fit_implications` | Consecuencias para el encaje y la preparación basadas solo en el expediente; no introduce evidencia ni claims del candidato. |
| `risks_and_unknowns` | Riesgos, contradicciones, red flags e incógnitas, con impacto y forma de resolverlos. |
| `questions_to_answer_before_next_step` | Preguntas cuya respuesta puede cambiar la decisión de continuar, preparar, negociar o retirarse. |
| `questions_for_recruiter` | Preguntas apropiadas para recruiter, priorizadas y sin presuponer hechos. |
| `questions_for_technical_interview` | Preguntas apropiadas para interlocutores técnicos, sin asumir que la entrevista está confirmada. |
| `decision_notes` | Opciones y criterios de decisión; no cambia el plan ni el lifecycle. |
| `do_not_assume` | Lista de afirmaciones que no deben tratarse como ciertas ni trasladarse a otros outputs. |
| `review_checklist` | Controles de procedencia, utilidad y separación completados antes de usar el dossier. |
| `uncertainty` | Desconocidos, inferencias, conflictos, fuentes débiles y preguntas pendientes. |

## Valores permitidos

- `output_type`: `opportunity-dossier`.
- `research_mode`: `source_only`, `external_research`.
- `status`: `draft`, `reviewed`, `used`, `discarded`.
- `company_or_client_known`: `true`, `false`, `partial`.

Todo dossier nuevo comienza en `draft`. `reviewed` exige una revisión real de procedencia y utilidad; `used`, evidencia de uso como preparación o soporte de decisión; `discarded`, decisión de no utilizar esa versión. Ninguno de estos valores modifica el estado de la candidatura.

## Modelo de procedencia

Cada hecho o afirmación material debe etiquetarse como uno de estos tipos y apuntar a su fuente:

| Tipo | Uso |
|---|---|
| `application_fact` | Oferta, intake, plan, riesgos o submission record. |
| `recruiter_statement` | Declaración documentada del recruiter o interlocutor del proceso. |
| `external_research` | Fuente pública o externa entregada explícitamente. |
| `user_note` | Nota u observación aportada por el usuario. |
| `inference` | Interpretación derivada, con base, confianza y límite. |
| `uncertainty` | Ausencia, conflicto o imposibilidad de verificación. |

Una misma afirmación puede tener varias fuentes, pero conserva su categoría y no gana más certeza de la que estas permiten. Una declaración de recruiter no pasa a ser investigación pública; una inferencia nunca se presenta como hecho.

## Correspondencia con el documento

El output debe incluir, en este orden:

1. Metadata.
2. Qué se sabe por la candidatura.
3. Qué se sabe por investigación externa o de empresa.
4. Resumen de la empresa.
5. Producto y modelo de negocio.
6. Mercado y contexto de clientes.
7. Contexto del rol.
8. Contexto técnico y operativo.
9. Implicaciones para el encaje del candidato.
10. Riesgos, incógnitas y red flags.
11. Preguntas que resolver antes de continuar.
12. Preguntas para recruiter.
13. Preguntas para entrevista técnica.
14. Notas de decisión.
15. Lista de supuestos prohibidos.
16. Checklist final de revisión.
17. Incertidumbre.

## Reglas de validación

- `source_application_folder` existe, corresponde a `application_id` y está bajo `career/applications/` o `examples/applications/`.
- Se leen siempre `job-description.md`, `job-intake.md`, `application-plan.md`, `risk-register.md` y `submission-record.md`; `recruiter-conversation.md` se lee si existe.
- `target-profile-selection.md` y `evidence-selection.md` son opcionales y solo informan `candidate_fit_implications`; no autorizan explorar entidades canónicas.
- CVs generados o finales nunca aparecen en `source_files_used` como fuentes factuales.
- `interview-prep.md` solo puede leerse por instrucción explícita y se registra como fuente de deduplicación de preguntas, no de hechos.
- En `source_only`, `external_sources_used` es `[]` y no aparecen afirmaciones externas.
- En `external_research`, cada afirmación externa referencia una fuente realmente disponible. Una URL sin contenido accesible se registra como pendiente, no como `external_sources_used` que respalda hechos.
- Cada afirmación material incluye tipo de procedencia, referencia, fecha cuando conste y nivel de confianza o límite cuando sea relevante.
- Empresa publicada, intermediario y cliente final se distinguen. Si el cliente final no consta, `company_or_client_known` no puede ocultarlo.
- Hechos ausentes sobre producto, clientes, ingresos, financiación, tamaño, arquitectura, escala, latencia, infraestructura, ownership, equipo o guardias permanecen desconocidos.
- Los requisitos de la oferta no se convierten en realidad técnica actual ni en experiencia del candidato.
- `candidate_fit_implications` deriva únicamente de análisis ya documentado y no añade evidencia, entidades ni claims.
- Investigación pública y declaraciones de empresa no se trasladan a CV, evidencia o conocimiento canónico.
- Las preguntas se priorizan por impacto y destinatario; no presuponen entrevista confirmada, oferta, tecnología, escala o ownership.
- `decision_notes` presenta criterios y opciones; no cambia `application-plan.md`, `risk-register.md` ni `submission-record.md`.
- No quedan placeholders en el output generado.
- El único archivo creado o reemplazado es `<source_application_folder>/generated/opportunity-dossier.md`, salvo un `output_path` válido dentro de `generated/` del mismo expediente.
