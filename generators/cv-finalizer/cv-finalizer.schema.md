# Esquema del finalizador de CV

## Propósito

El esquema describe una operación reproducible que transforma el bloque candidato de un `generated/cv.md` en artefactos finales de entrega. Sus campos sirven para revisar la operación; no deben insertarse como auditoría privada en el Markdown o HTML enviable.

## Campos obligatorios

| Campo | Descripción |
|---|---|
| `id` | Identificador estable con formato `cv-final:<application-slug>:<lang>`. |
| `application_id` | Identificador del expediente: `application:<application-slug>`. |
| `source_application_folder` | Ruta relativa exacta de la candidatura o fixture. |
| `source_generated_cv` | Ruta exacta a `<source_application_folder>/generated/cv.md`. |
| `output_type` | Tipo del output; en v1 solo admite `cv-final`. |
| `language` | `es` o `en`, confirmado con el CV fuente o con las fuentes auxiliares permitidas. |
| `status` | Estado permitido de la finalización. |
| `source_files_used` | Rutas realmente leídas: fuente, plantillas, referencia visual opcional y fuentes auxiliares permitidas. |
| `final_markdown_output` | Ruta a `final/<output_prefix>-send-<lang>.md`. |
| `final_html_output` | Ruta a `final/<output_prefix>-print-<lang>.html`. |
| `assets_used` | Activos usados y relación origen → copia final; `[]` si no hay foto. |
| `style_reference_used` | Ruta de la referencia visual utilizada o `[]`; nunca aporta contenido. |
| `candidate_facing_block_extracted` | Delimitación o método exacto usado para aislar el bloque candidato. |
| `content_changes` | Diferencias de contenido entre el bloque extraído y el Markdown final, con motivo; `[]` si no existen. |
| `wording_cleanups` | Limpiezas solicitadas explícitamente, con texto anterior, posterior y motivo; `[]` si no existen. |
| `claims_added` | Claims nuevos; debe ser siempre `[]` en una finalización válida. |
| `claims_removed` | Claims eliminados; debe ser `[]` salvo petición explícita del usuario que autorice la eliminación. |
| `claims_preserved` | Confirmación de que los claims del bloque candidato permanecen, incluyendo cualquier excepción autorizada. |
| `audit_removed` | Secciones, comentarios y metadatos internos excluidos de los outputs enviables. |
| `export_instructions` | Ruta a `final/export-instructions.md` y confirmación de exportación manual. |
| `review_notes` | Resultado de comparación, revisión visual y pendientes. |
| `uncertainty` | Ambigüedades no resueltas; `[]` cuando no existen. |

## Valores permitidos

- `output_type`: `cv-final`.
- `language`: `es`, `en`.
- `status`: `draft`, `reviewed`, `exported`, `sent`, `discarded`.

Una finalización recién creada comienza en `draft`. `reviewed` exige revisión de contenido y visual; `exported`, un PDF exportado y verificado; `sent`, evidencia de envío; `discarded`, decisión de no usar los artefactos. El finalizador v1 solo crea archivos en estado conceptual `draft`: no exporta el PDF ni registra envíos.

## Invariantes

- `source_generated_cv` debe existir dentro del mismo `source_application_folder` y contener un bloque candidato identificable.
- `final_markdown_output` y `final_html_output` deben usar el mismo idioma y prefijo.
- El Markdown final contiene exclusivamente contenido dirigido al candidato; no contiene comentarios, auditoría, IDs, warnings ni metadatos de generación.
- El HTML representa el mismo contenido y orden que el Markdown final. El diseño puede cambiar jerarquía visual, no significado.
- `claims_added` es siempre `[]`.
- Todos los claims del bloque candidato se conservan salvo una eliminación solicitada explícitamente; una limpieza de estilo no puede cambiar alcance, atribución, título, fecha, métrica o nivel.
- No se añaden tecnologías, empleadores, responsabilidades, logros, métricas, skills, títulos, educación, idiomas, contactos ni fechas.
- La oferta no se usa como fuente de contenido o reposicionamiento.
- La referencia de estilo no se usa como fuente factual ni como texto para copiar.
- Los activos se copian; no se enlazan desde otra candidatura, no se cargan desde remoto y no se incrustan en base64.
- El HTML usa rutas relativas, CSS interno, fuentes del sistema y ninguna dependencia externa.
- `export-instructions.md` describe exportación manual; v1 no crea PDF.
- Los únicos cambios permitidos están bajo `<source_application_folder>/final/`.

## Revisión mínima de campos

Antes de terminar, la ejecución debe poder responder este registro sin incluirlo en los outputs:

```yaml
id: cv-final:<application-slug>:<lang>
application_id: application:<application-slug>
source_application_folder: <ruta>
source_generated_cv: <ruta>/generated/cv.md
output_type: cv-final
language: es|en
status: draft
source_files_used: []
final_markdown_output: <ruta>/final/cv-send-<lang>.md
final_html_output: <ruta>/final/cv-print-<lang>.html
assets_used: []
style_reference_used: []
candidate_facing_block_extracted: <método y límites>
content_changes: []
wording_cleanups: []
claims_added: []
claims_removed: []
claims_preserved: <confirmación>
audit_removed: []
export_instructions: <ruta>/final/export-instructions.md
review_notes: []
uncertainty: []
```

