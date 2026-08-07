# Workflow del finalizador de CV

## Objetivo operativo

Convertir un CV generado y revisado en un Markdown enviable y un HTML imprimible, sin alterar sus hechos ni convertir la finalización visual en una nueva fase de generación.

## 1. Preconditions

- Recibir una única `source_application_folder` bajo `career/applications/` o `examples/applications/`.
- Confirmar que existe `generated/cv.md` y que contiene un bloque candidato inequívoco.
- Confirmar `language` (`es` o `en`) y `output_prefix` (`cv` por defecto).
- Confirmar que el CV fue revisado para contenido. Finalizar no sustituye la revisión factual.
- Confirmar que la operación fue solicitada explícitamente y que solo escribirá bajo `final/`.
- Revisar cambios locales antes de reemplazar cualquier output final existente.

## 2. Inputs

Obligatorios:

1. `<source_application_folder>/generated/cv.md`.
2. `templates/final/cv-send.template.md`.
3. `templates/final/cv-print.template.html`.
4. `templates/final/export-instructions.template.md`.
5. Este esquema y workflow.

Opcionales:

- `photo_source_path`, si apunta a una imagen local válida;
- `style_reference`, solo para observar jerarquía, espaciado, tipografía de sistema y comportamiento de impresión;
- `<source_application_folder>/application-plan.md` y `submission-record.md`, únicamente para confirmar idioma, estado y nombres de salida.

No leer la oferta para buscar posicionamiento. No leer conocimiento canónico, perfiles objetivo u otras candidaturas para incorporar contenido. Una referencia visual nunca autoriza a copiar texto.

## 3. Candidate block extraction

1. Preferir el contenido entre `<!-- Inicio del bloque destinado a candidatura -->` y `<!-- Fin del bloque destinado a candidatura -->`.
2. Excluir ambos marcadores y cualquier otro comentario HTML/Markdown.
3. Si los marcadores no existen, aceptar solo un límite inequívoco: todo lo anterior al separador que introduce `## Notas de generación / Auditoría` y su aviso de no envío.
4. No asumir que cualquier `---` termina el CV: puede ser contenido legítimo.
5. Conservar literalmente estructura, orden, títulos, párrafos, bullets, enlaces y claims del bloque extraído antes de cualquier limpieza autorizada.
6. Registrar el método en `candidate_facing_block_extracted` y lo retirado en `audit_removed`.

## 4. Safe cleanup rules

Sin una petición explícita de `safe_wording_cleanups`, solo se permiten operaciones no semánticas:

- eliminar comentarios y espacios finales;
- normalizar líneas en blanco sin cambiar agrupaciones;
- retirar placeholders residuales únicamente si la sección completa carece de contenido real; si hay duda, detenerse;
- corregir escapes o artefactos puramente mecánicos cuando el texto pretendido sea inequívoco.

Una limpieza solicitada puede corregir gramática, puntuación, repetición o fluidez, pero debe conservar significado, alcance, atribución, seniority y grado de certeza. Registrar antes/después en `wording_cleanups`.

Nunca añadir o inferir claims, tecnologías, fechas, empleadores, métricas, skills, títulos, educación, idiomas, niveles, responsabilidades o contacto. Nunca retirar un claim porque dificulte el diseño. Si el usuario solicita un cambio factual, detenerse y señalar que debe corregirse y regenerarse desde la fuente adecuada.

## 5. Markdown final creation

- Crear `final/<output_prefix>-send-<lang>.md` desde el bloque extraído.
- Mantener encabezado, título objetivo y todas las secciones respaldadas en el mismo orden.
- Eliminar auditoría, metadatos, IDs, warnings y comentarios.
- No añadir explicación de la finalización ni frontmatter interno.
- Mantener Markdown simple, limpio, editable y apto para copiar.
- Comparar el resultado con el bloque extraído y completar conceptualmente `content_changes`, `claims_added`, `claims_removed` y `claims_preserved`.

## 6. HTML print creation

- Crear `final/<output_prefix>-print-<lang>.html` desde el Markdown final, no desde la auditoría.
- Representar el mismo contenido y orden; no resumir para que quepa.
- Usar HTML semántico, CSS dentro del archivo y fuentes locales del sistema.
- Configurar `@page` para A4, márgenes legibles y `print-color-adjust`.
- Evitar saltos inmediatamente después de `h2`/`h3` y dentro de encabezado, bloques cortos y experiencias cuando sea razonable.
- Usar tamaños y espaciado legibles. El objetivo es una o dos páginas, pero nunca comprimir texto hasta hacerlo ilegible.
- No usar scripts, CDNs, web fonts, recursos remotos, base64 ni notas de auditoría.
- Incluir la foto solo cuando exista una copia local válida; si no hay foto, usar la variante de cabecera sin imagen y sin placeholder roto.

## 7. Asset handling

Cuando se proporcione `photo_source_path`:

1. Confirmar que existe, es un archivo de imagen legible y no es remoto.
2. Crear `final/assets/` si no existe.
3. Copiarlo conservando un nombre seguro y descriptivo; por defecto, el nombre original.
4. Referenciarlo desde el HTML como `assets/<archivo>`.
5. Registrar origen y destino en `assets_used`.

No enlazar directamente a `assets/` global ni a otra candidatura. No convertir la imagen a base64. Si la copia colisiona con un archivo diferente o el formato no es válido, detenerse.

## 8. Export instructions

Crear `final/export-instructions.md` desde la plantilla e indicar:

- qué HTML abrir;
- impresión desde navegador y destino PDF;
- papel A4;
- gráficos de fondo cuando sean necesarios;
- revisión de márgenes, escala, foto y saltos de página;
- verificación del PDF antes de enviarlo;
- prohibición de enviar la auditoría.

No ejecutar la exportación ni crear un PDF.

## 9. Review checklist

- [ ] El input es el `generated/cv.md` del mismo expediente.
- [ ] El bloque candidato quedó delimitado sin incluir auditoría.
- [ ] Markdown y HTML conservan los mismos claims y el mismo orden.
- [ ] `claims_added` es `[]` y ninguna fuente visual aportó contenido.
- [ ] `claims_removed` es `[]` o contiene solo eliminaciones solicitadas explícitamente.
- [ ] Cada limpieza solicitada conserva significado y está registrada.
- [ ] No quedan comentarios, IDs, warnings, metadatos ni placeholders.
- [ ] El idioma y los nombres de salida son coherentes.
- [ ] Nombre, título, contacto, empleadores, fechas, métricas y niveles no cambiaron.
- [ ] La foto, si se proporcionó, está copiada bajo `final/assets/` y usa ruta relativa.
- [ ] El HTML no depende de red, base64, scripts ni fuentes externas.
- [ ] La vista de impresión usa A4, texto legible y saltos razonables.
- [ ] Las instrucciones describen exportación manual y revisión del PDF.
- [ ] Solo se modificó `final/` dentro del expediente.

## 10. Output location

Crear o reemplazar exclusivamente:

```text
<source_application_folder>/final/<output_prefix>-send-<lang>.md
<source_application_folder>/final/<output_prefix>-print-<lang>.html
<source_application_folder>/final/export-instructions.md
<source_application_folder>/final/assets/<foto>  # solo si se proporciona
```

## 11. Stop conditions

Detenerse sin crear o reemplazar outputs cuando:

- falta `generated/cv.md` o no se puede delimitar con seguridad el bloque candidato;
- el CV no ha sido revisado o todavía contiene placeholders materiales;
- `language` no es `es` o `en`, o contradice el contenido sin instrucción explícita;
- finalizar exigiría leer la oferta o inventar un posicionamiento;
- se solicita añadir o corregir un hecho que no está en el bloque candidato;
- una limpieza cambiaría significado, alcance, atribución o certeza;
- Markdown y HTML no pueden mantener todos los claims con legibilidad razonable;
- la foto no existe, no es válida o colisiona con un activo distinto;
- un output existente contiene cambios locales que no pueden preservarse con seguridad;
- la ruta de salida queda fuera de `final/` del expediente.

Tras crear, comparar y revisar los cuatro tipos de output permitidos, detenerse. No exportar PDF, no actualizar el registro de candidatura y no generar otros materiales.

