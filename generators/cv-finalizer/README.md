# Finalizador de CV

Esta capa convierte un CV ya generado y revisado en dos vistas limpias de entrega: Markdown editable y HTML listo para imprimir. No genera un CV nuevo, no vuelve a posicionar al candidato y no es una fuente de verdad.

## Lugar en el flujo

El input principal es:

```text
<application-folder>/generated/cv.md
```

CV Generator v1 conserva en ese archivo un bloque candidato y una auditoría interna. CV Finalizer v1 extrae únicamente el bloque candidato aprobado y produce:

```text
<application-folder>/final/
|-- cv-send-<lang>.md
|-- cv-print-<lang>.html
|-- export-instructions.md
`-- assets/
    `-- <nombre-del-archivo-de-foto>
```

`<lang>` es `es` o `en`. El prefijo predeterminado es `cv`. No se crea PDF: la exportación se realiza manualmente desde el navegador.

## Responsabilidad

El finalizador:

- extrae el bloque comprendido entre los marcadores de candidato de `generated/cv.md`, o, si no existen, todo lo anterior al separador de auditoría inequívoco;
- elimina comentarios HTML/Markdown, IDs, metadatos, warnings, notas internas y la auditoría;
- conserva el orden, la cronología y todos los claims del bloque candidato;
- aplica cambios de redacción solo si el usuario los solicita explícitamente y sin alterar hechos;
- crea un Markdown limpio y editable;
- representa exactamente ese contenido en HTML con CSS local y comportamiento de impresión A4;
- copia una foto válida a `final/assets/` cuando se proporciona;
- documenta la exportación manual a PDF.

No lee la oferta para buscar mejor posicionamiento ni consulta conocimiento canónico para ampliar el CV. Puede leer `application-plan.md` y `submission-record.md` únicamente para confirmar idioma, estado y nombres de salida. Puede usar un CV final existente solo como referencia visual, nunca como fuente de contenido.

## Componentes

- [cv-finalizer.schema.md](cv-finalizer.schema.md): contrato, valores permitidos y reglas de validación.
- [cv-finalizer-workflow.md](cv-finalizer-workflow.md): secuencia operativa y condiciones de parada.
- [cv-finalizer-prompt.md](cv-finalizer-prompt.md): prompt directamente utilizable con Codex o ChatGPT.
- [`templates/final/cv-send.template.md`](../../templates/final/cv-send.template.md): estructura Markdown limpia.
- [`templates/final/cv-print.template.html`](../../templates/final/cv-print.template.html): estructura HTML/CSS para A4.
- [`templates/final/export-instructions.template.md`](../../templates/final/export-instructions.template.md): guía de exportación manual.

## Límites de v1

- No crea ni modifica `generated/cv.md`.
- No corrige conocimiento canónico, intake, perfiles objetivo ni planes.
- No añade, elimina o combina claims por iniciativa propia.
- No genera PDF, DOCX, Google Docs, cartas, mensajes ni otros materiales.
- No marca un CV como enviado sin evidencia externa y una actualización separada del registro de candidatura.

