# Prompt reutilizable: finalizar CV para envío e impresión

Copia este prompt en Codex o ChatGPT y sustituye los parámetros. Debe ejecutarse desde un repositorio CareerOS con acceso a la carpeta indicada.

```text
Finaliza un CV ya generado de CareerOS. No generes un CV nuevo ni cambies su posicionamiento.

Parámetros:
- source_application_folder: [career/applications/<application-slug> o examples/applications/<example-slug>]
- language: [es / en]
- photo_source_path: [ruta local válida o ninguno]
- style_reference: [ruta local opcional o ninguno]
- safe_wording_cleanups: [lista explícita opcional o ninguno]
- output_prefix: [cv por defecto]

Lee primero:
- generators/cv-finalizer/README.md
- generators/cv-finalizer/cv-finalizer.schema.md
- generators/cv-finalizer/cv-finalizer-workflow.md
- templates/final/cv-send.template.md
- templates/final/cv-print.template.html
- templates/final/export-instructions.template.md
- source_application_folder/generated/cv.md

Puedes leer style_reference únicamente como referencia visual. Puedes leer source_application_folder/application-plan.md y source_application_folder/submission-record.md solo si necesitas confirmar idioma, estado o nombres de salida. No leas la oferta para mejorar el posicionamiento. No uses conocimiento canónico, perfiles objetivo, otras candidaturas ni la referencia visual para añadir contenido.

Después:

1. Comprueba las precondiciones y condiciones de parada del workflow. Confirma que language es es o en y que output_prefix es cv cuando no se indique otro.
2. Extrae únicamente el bloque candidato de generated/cv.md. Prefiere los marcadores explícitos de inicio y fin. Si no existen, usa solo el separador inequívoco anterior a "## Notas de generación / Auditoría". Si el límite es ambiguo, detente.
3. Elimina del contenido enviable la auditoría completa, comentarios HTML/Markdown, IDs, warnings, metadatos de generación y notas internas.
4. Conserva todos los claims, secciones y orden del bloque candidato. No añadas tecnologías, fechas, empleadores, métricas, skills, títulos, educación, idiomas, niveles, responsabilidades, datos de contacto ni ningún otro hecho.
5. No retires claims para ajustar páginas. Solo puedes eliminar uno si safe_wording_cleanups lo solicita explícitamente; registra esa excepción durante la revisión.
6. Si safe_wording_cleanups contiene instrucciones, aplica únicamente correcciones de gramática, puntuación, repetición o fluidez que no cambien significado, alcance, atribución, seniority ni certeza. Si una instrucción exige un cambio factual, detente y explica que debe corregirse en la fuente adecuada.
7. Crea source_application_folder/final/<output_prefix>-send-<language>.md usando la plantilla Markdown. Debe ser limpio, editable y no contener auditoría, comentarios, frontmatter interno ni placeholders.
8. Crea source_application_folder/final/<output_prefix>-print-<language>.html desde el Markdown final usando la plantilla HTML. Conserva exactamente el contenido y orden; solo cambia la representación visual.
9. El HTML debe ser autónomo excepto por una ruta relativa de foto, usar CSS interno, fuentes del sistema, ajustes A4, texto legible, colores de impresión y reglas razonables contra saltos tras encabezados o dentro de experiencias. No uses CDN, web fonts, scripts, imágenes remotas ni base64.
10. Si photo_source_path se proporciona, valida la imagen, cópiala a source_application_folder/final/assets/ conservando un nombre seguro y usa desde el HTML la ruta relativa assets/<archivo>. Si no se proporciona, elimina el elemento de foto y usa la cabecera sin foto.
11. Crea source_application_folder/final/export-instructions.md desde la plantilla. Explica cómo abrir el HTML, imprimir, guardar como PDF en A4, activar fondos si hace falta, revisar márgenes, escala y saltos, verificar el PDF y no enviar la auditoría. No generes el PDF.
12. Revisa Markdown contra el bloque extraído y HTML contra Markdown. Confirma conceptualmente todos los campos de cv-finalizer.schema.md, especialmente claims_added: [], claims_removed, claims_preserved, audit_removed, content_changes y uncertainty. No insertes ese registro interno en los outputs enviables.
13. Revisa que solo hayas modificado source_application_folder/final/ y que no hayas ejecutado la exportación.
14. Detente. No modifiques generated/cv.md, intake, plan, registro, conocimiento canónico, perfiles objetivo, otras candidaturas ni otros outputs. No generes PDF, DOCX, carta, mensaje o contenido adicional.
```

