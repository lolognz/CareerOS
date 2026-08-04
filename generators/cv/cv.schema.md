# Esquema de CV generado

## Propósito

Un CV generado es una vista adaptada y concisa de conocimiento profesional canónico para una candidatura concreta. Combina una sección limpia destinada al candidato con una auditoría separada. Es un output desechable, no una entidad canónica ni evidencia nueva.

## Campos obligatorios

| Campo | Descripción |
|---|---|
| `id` | Identificador estable del output con formato `cv:<application-slug>`. |
| `application_id` | Identificador del expediente con formato `application:<application-slug>`. |
| `source_application_folder` | Ruta relativa exacta a la carpeta de candidatura o fixture. |
| `output_type` | Tipo del output; en v1 solo admite `cv`. |
| `target_profile` | ID del perfil objetivo primario utilizado; `[]` solo si el expediente justifica generar sin perfil. |
| `language` | Idioma del CV y base documentada de la elección. |
| `status` | Estado permitido del output. |
| `source_files_used` | Rutas de los siete inputs, el perfil y todas las entidades canónicas referenciadas que se leyeron antes de generar el CV. |
| `target_role_title` | Título objetivo literal o estrategia de título respaldada; no sustituye los títulos históricos. |
| `positioning_summary` | Síntesis factual que guía el resumen profesional, con fuentes y límites. |
| `selected_roles` | IDs canónicos de roles que aparecen o respaldan contenido visible, o `[]`. |
| `selected_projects` | IDs canónicos de proyectos utilizados, o `[]`. |
| `selected_stories` | IDs canónicos de historias utilizadas para construir bullets, o `[]`. |
| `selected_skills` | IDs canónicos de habilidades incluidas o demostradas, o `[]`. |
| `selected_technologies` | IDs canónicos de tecnologías incluidas, o `[]`. |
| `selected_achievements` | IDs canónicos de logros utilizados, o `[]`. |
| `claims_used` | Mapa entre cada afirmación o bullet visible, sus fuentes y sus límites. |
| `claims_avoided` | Afirmaciones omitidas por falta de evidencia, riesgo, debilidad o desajuste. |
| `gaps_not_included` | Requisitos parciales, no respaldados o desconocidos excluidos del CV visible. |
| `risks_considered` | Riesgos que condicionaron la selección, jerarquía o redacción. |
| `evidence_boundaries` | Límites de título, seniority, atribución, cronología, alcance, métricas y madurez conservados. |
| `uncertainty` | Datos ausentes, ambiguos, inferidos o en conflicto que no se resolvieron por plausibilidad. |
| `generated_cv` | Bloque candidato del archivo, desde el encabezado hasta la sección adicional final, antes del separador de auditoría. |
| `review_notes` | Resultado de revisión, decisiones y pendientes antes del uso. |

Las listas `selected_*` registran el subconjunto efectivamente usado, no copian automáticamente toda la selección disponible en el intake.

## Valores permitidos

- `output_type`: `cv`.
- `status`: `draft`, `reviewed`, `submitted` o `discarded`.

Todo CV recién generado comienza con `status: draft`. Solo una revisión explícita permite `reviewed`; solo un envío documentado permite `submitted`. `discarded` indica que el output no debe usarse.

## Estructura del bloque candidato

El bloque `generated_cv` sigue este orden, omitiendo secciones opcionales sin soporte:

1. Encabezado con nombre y contacto únicamente cuando estén respaldados.
2. Título objetivo, claramente posicional y nunca presentado como título histórico.
3. Resumen profesional.
4. Fortalezas o skills centrales.
5. Stack técnico seleccionado.
6. Experiencia profesional en cronología inversa, con títulos y empleadores formales.
7. Proyectos o logros seleccionados, si añaden evidencia distinta.
8. Educación o investigación, si es relevante y está respaldada.
9. Idiomas o información adicional, solo cuando existan hechos suficientes, incluido el nivel cuando se mencione.

No deben quedar placeholders en un output generado. Una sección sin evidencia se elimina completa.

## Reglas de validación

- Todos los campos obligatorios deben aparecer en la auditoría, incluso con `[]`, `desconocido` o una explicación de ausencia.
- `source_application_folder` debe existir y corresponder con `application_id`.
- Los siete inputs del expediente deben leerse y registrarse; cualquier excepción debe activar una condición de parada.
- `target_profile` debe resolver a un perfil existente cuando no sea `[]`.
- Todos los IDs canónicos referenciados por `evidence-selection.md` y `target-profile-selection.md` deben resolverse y leerse; cada ID `selected_*` usado en el CV debe haber sido autorizado por la selección del expediente.
- Cada línea del resumen, skill, tecnología, bullet, proyecto, logro, formación, idioma o dato adicional debe estar respaldada en `claims_used`.
- Los requisitos de la oferta no pueden convertirse en experiencia, skills o tecnologías sin evidencia canónica seleccionada.
- Los títulos históricos, empleadores y fechas se copian de sus entidades; no se normalizan de forma que cambie su significado.
- El orden de experiencia debe preservar la cronología. Los periodos simultáneos o inciertos mantienen esa condición.
- Un fit parcial no autoriza ownership completo. Liderazgo sin título no se presenta como Tech Lead formal.
- Los proyectos personales se etiquetan como personales y no se insertan dentro de experiencia profesional.
- No se inventan ni calculan métricas. Las métricas reportadas o aproximadas conservan esa cualificación.
- Los gaps se excluyen del bloque candidato y aparecen en `gaps_not_included`.
- El CV usa bullets respaldados, evita lenguaje inflado y apunta a una o dos páginas renderizadas por defecto.
- El idioma sigue la oferta salvo instrucción documentada distinta; la inferencia y sus límites se registran.
- La auditoría comienza después de un separador y declara que no está destinada al envío.
- El único output permitido es `<source_application_folder>/generated/cv.md`; el generador no modifica inputs ni conocimiento canónico.

## Esqueleto de auditoría

```markdown
---

## Notas de generación / Auditoría

> Esta sección no está destinada al envío.

- **id:** `cv:[application-slug]`
- **application_id:** `application:[application-slug]`
- **source_application_folder:** `[ruta]`
- **output_type:** cv
- **target_profile:** [ID o `[]`]
- **language:** [idioma + base]
- **status:** draft
- **source_files_used:** [rutas]
- **target_role_title:** [título]
- **positioning_summary:** [síntesis trazable]
- **selected_roles:** [IDs o `[]`]
- **selected_projects:** [IDs o `[]`]
- **selected_stories:** [IDs o `[]`]
- **selected_skills:** [IDs o `[]`]
- **selected_technologies:** [IDs o `[]`]
- **selected_achievements:** [IDs o `[]`]
- **claims_used:** [claim → fuentes → límites]
- **claims_avoided:** [claim → motivo]
- **gaps_not_included:** [gap → fuente]
- **risks_considered:** [riesgos]
- **evidence_boundaries:** [límites]
- **uncertainty:** [incertidumbres]
- **generated_cv:** bloque candidato anterior a este separador
- **review_notes:** [notas]
```
