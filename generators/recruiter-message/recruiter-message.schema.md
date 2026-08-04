# Esquema de mensaje a recruiter

## Propósito

Un mensaje a recruiter es una vista breve generada a partir de un expediente de candidatura existente. Su archivo conserva el texto listo para revisión junto con la trazabilidad mínima necesaria para auditarlo. Es desechable, no canónico y no puede introducir hechos nuevos.

## Campos obligatorios

| Campo | Descripción |
|---|---|
| `id` | Identificador estable del output con formato `recruiter-message:<application-slug>`. |
| `application_id` | Identificador del expediente con formato `application:<application-slug>`. |
| `source_application_folder` | Ruta relativa exacta a la carpeta de candidatura o fixture utilizada. |
| `message_type` | Uno de los cuatro tipos permitidos. |
| `audience` | Destinatario conocido, rol del destinatario o `desconocido`; no inventar nombre ni cargo. |
| `channel` | Canal previsto, por ejemplo `LinkedIn`, `email` u `otro`; usar `desconocido` si no consta. |
| `language` | Idioma del mensaje y base de la elección. |
| `tone` | Tono aplicado; por defecto `profesional, claro, breve, humano`. |
| `status` | Estado permitido del output. |
| `source_files_used` | Rutas de todos los archivos realmente consultados para generar el mensaje. |
| `key_fit_signals` | De dos a tres señales relevantes cuando el tipo las requiera, cada una vinculada a evidencia del expediente. Puede ser `[]` en un rechazo. |
| `clarifying_questions` | Preguntas incluidas o consideradas. Deben ser de alto impacto; usar `[]` cuando no correspondan. |
| `claims_used` | Afirmaciones presentes en el mensaje, con su respaldo y sus límites. |
| `claims_avoided` | Afirmaciones omitidas por falta de evidencia, riesgo o irrelevancia. |
| `risks_considered` | Riesgos del expediente que afectaron a selección, redacción o decisión. |
| `generated_message` | Texto final principal, sin información externa al expediente. |
| `variants` | Entre dos y tres alternativas útiles o `[]`; cada variante debe cumplir las mismas reglas. |
| `review_notes` | Resultado de la revisión humana o automática, cambios pendientes y decisiones de redacción. |
| `evidence_boundaries` | Límites de alcance, atribución, seniority, métricas, cronología o madurez conservados. |
| `uncertainty` | Datos ausentes, inferidos o ambiguos que afectan al mensaje; nunca resolverlos por plausibilidad. |

## Valores permitidos

- `message_type`: `clarification-first`, `apply`, `follow-up` o `polite-decline`.
- `status`: `draft`, `reviewed`, `sent` o `discarded`.

Todo archivo recién generado comienza con `status: draft`. Solo una revisión explícita permite usar `reviewed`; solo evidencia de envío permite usar `sent`. `discarded` conserva que el output no debe utilizarse, sin convertirlo en fuente histórica de hechos.

## Reglas por tipo

### `clarification-first`

- Es la opción preferida cuando la recomendación sea `aplicar tras aclarar` o existan incógnitas materiales.
- Expresa interés solo si está documentado, resume el mejor encaje en una o dos líneas y formula entre dos y cuatro preguntas de alto impacto.
- No intenta compensar gaps con lenguaje promocional ni envía un pitch equivalente a un CV.

### `apply`

- Se usa cuando la recomendación y los riesgos permiten aplicar sin aclaraciones bloqueantes.
- Incluye de dos a tres señales de encaje respaldadas, interés documentado y una petición breve de siguientes pasos.
- Solo comparte disponibilidad si aparece en las fuentes.

### `follow-up`

- Requiere evidencia en `submission-record.md` u otra fuente del expediente de una interacción previa.
- Reitera interés sin presionar y puede añadir una única aclaración o nota de disponibilidad respaldada.
- No inventa fecha, canal, conversación, respuesta ni compromiso previo.

### `polite-decline`

- Declina de forma clara y agradecida.
- El motivo es opcional, de alto nivel y debe proceder del expediente.
- Mantiene la puerta abierta solo si esa intención está documentada; no inventa interés futuro.

## Reglas de validación

- Deben aparecer todos los campos obligatorios, aunque su valor sea `[]`, `desconocido` o una explicación de ausencia.
- `source_application_folder` debe existir y corresponder con `application_id`.
- `source_files_used` solo enumera archivos leídos; el mínimo necesario depende de las precondiciones del workflow.
- Cada elemento de `claims_used` debe resolver a una fuente y respetar sus `evidence_boundaries`.
- Un requisito descrito como gap, no respaldado o desconocido no puede aparecer como capacidad demostrada.
- `claims_avoided`, `risks_considered`, `evidence_boundaries` y `uncertainty` no pueden omitirse por hacer el mensaje más limpio.
- Las preguntas no deben presuponer hechos ausentes ni afirmar implícitamente que el candidato cumple un requisito.
- El idioma puede ser español o inglés según la oferta y el contexto documentado.
- El mensaje debe ser breve y adecuado para LinkedIn o para un primer contacto por email; no debe convertirse en carta de presentación.
- El output debe escribirse únicamente en `generated/recruiter-message.md` dentro del expediente de origen.
- El generador no modifica inputs, entidades canónicas, perfiles objetivo ni registros de evidencia.

## Esqueleto

```markdown
# Mensaje a recruiter: [empresa] — [rol]

## Metadata

- **id:** `recruiter-message:[application-slug]`
- **application_id:** `application:[application-slug]`
- **source_application_folder:** `[ruta]`
- **message_type:** [valor permitido]
- **audience:** [valor]
- **channel:** [valor]
- **language:** [idioma + base]
- **tone:** profesional, claro, breve, humano
- **status:** draft
- **source_files_used:** [rutas]

## Trazabilidad

- **key_fit_signals:** [señales + respaldo o `[]`]
- **clarifying_questions:** [preguntas o `[]`]
- **claims_used:** [claim + fuente + límite]
- **claims_avoided:** [claim + motivo]
- **risks_considered:** [riesgos]
- **evidence_boundaries:** [límites]
- **uncertainty:** [incertidumbres]

## Mensaje generado

- **generated_message:**

  [texto]

## Variantes

- **variants:** [dos o tres variantes, o `[]`]

## Revisión

- **review_notes:** [notas]
```
