# Esquema de entidad de logro

## Propósito

Una entidad de logro representa un resultado, hito o progresión profesional respaldados por hechos conservados en CareerOS. Su función es aislar una afirmación reutilizable junto con su evidencia, atribución y límites, sin convertirla en una viñeta de CV ni exagerar su impacto.

## Principios de diseño

- Cada logro debe tener un ID estable y un único archivo canónico.
- La afirmación debe ser la versión más breve que siga siendo exacta.
- Los hechos, métricas y recuerdos reportados deben distinguirse por su fuerza de evidencia.
- La atribución individual, compartida, de equipo o de proyecto debe declararse explícitamente.
- Un logro puede describir un resultado modesto o parcial; no necesita lenguaje promocional.
- Las limitaciones deben impedir inferencias sobre causalidad, autoría, alcance o madurez que la evidencia no sostenga.
- Las relaciones solo deben usar IDs canónicos cuando exista el archivo de destino.

## Campos canónicos

| Campo | Obligatorio | Descripción |
|---|---:|---|
| `id` | Sí | Identificador único y estable con formato `achievement:<slug>`. |
| `title` | Sí | Título factual y reconocible del logro. |
| `type` | Sí | Clasificación factual: financiación, resultado académico, publicación/release, validación con usuarios, visibilidad, mejora técnica, progresión profesional, automatización o hito de proyecto personal, entre otras. |
| `evidence_strength` | Sí | `strong`, `moderate`, `limited` o `reported-by-user`. |
| `chronology` | Sí | Periodo o momento con la máxima precisión respaldada. |
| `organization` | Sí | Organización o contexto independiente en el que se produjo. |
| `organization_id` | Sí | ID canónico de organización cuando exista; `[]` cuando no sea aplicable. |
| `related_roles` | Sí | IDs canónicos de roles relacionados. |
| `related_projects` | Sí | IDs canónicos de proyectos relacionados. |
| `related_stories` | Sí | IDs canónicos de historias que preservan el episodio o sus hechos. |
| `related_skills` | Sí | IDs canónicos de habilidades respaldadas por el logro. |
| `related_technologies` | Sí | IDs canónicos de tecnologías claramente implicadas. |
| `claim` | Sí | Versión más corta y exacta del logro. |
| `supporting_facts` | Sí | Hechos que sostienen la afirmación, sin duplicar narrativas completas. |
| `metric_or_result` | Sí | Resultado o métrica, conservando cifras exactas solo cuando estén respaldadas y su condición de reportadas cuando corresponda. |
| `attribution` | Sí | Alcance individual, compartido, de equipo, de proyecto o incierto. |
| `limitations` | Sí | Lo que el logro no prueba sobre impacto, causalidad, autoría, alcance, título o madurez. |
| `reusable_for` | Sí | Usos futuros apropiados: CV, entrevista, LinkedIn, carta de presentación, portfolio o caso de promoción. |
| `evidence` | Sí | Rutas raw, entidades o confirmaciones explícitas que respaldan el logro. |
| `uncertainty` | Sí | Vacíos de fecha, atribución, verificación, métrica, alcance o causalidad. |
| `related_entities` | Sí | Otros IDs canónicos relacionados no cubiertos por los campos anteriores. |

## Fuerza de evidencia

- `strong`: el resultado y sus elementos esenciales están descritos de forma directa y coherente por las fuentes canónicas.
- `moderate`: el resultado está respaldado de forma directa, pero faltan detalles relevantes de fecha, atribución, alcance o documentación primaria.
- `limited`: existe una afirmación o hito delimitado, pero la evidencia disponible es escasa o incompleta.
- `reported-by-user`: el resultado se conserva como recuerdo o dato aportado por el usuario sin verificación independiente dentro del repositorio.

## Reglas de validación

- Todos los campos deben estar presentes, incluso con `[]` o incertidumbre explícita.
- `organization_id`, `related_roles`, `related_projects`, `related_stories`, `related_skills`, `related_technologies` y `related_entities` solo pueden contener IDs de archivos canónicos existentes.
- `claim` no debe contener una métrica con más precisión que la evidencia ni presentar un recuerdo reportado como verificación externa.
- `supporting_facts` debe explicar el sustento del claim sin copiar por completo proyectos o historias.
- `metric_or_result` debe diferenciar cifras exactas, aproximadas, ambiguas y reportadas.
- `attribution` nunca debe asignar autoría individual exclusiva cuando la fuente describe trabajo compartido.
- `limitations` debe conservar límites de causalidad, madurez, alcance y autoridad formal.
- `reusable_for` identifica posibles vistas futuras; no autoriza a convertir la entidad en texto final de candidatura.
- Los backlinks solo se añaden a esquemas que admitan logros.

## Esqueleto

```markdown
# Logro: [Título]

## Canonical Fields

| Field | Value |
|---|---|
| id | `achievement:...` |
| title |  |
| type |  |
| evidence_strength |  |
| chronology |  |
| organization |  |
| organization_id | [] |
| related_roles | [] |
| related_projects | [] |
| related_stories | [] |
| related_skills | [] |
| related_technologies | [] |
| claim |  |
| supporting_facts |  |
| metric_or_result |  |
| attribution |  |
| limitations |  |
| reusable_for |  |
| evidence |  |
| uncertainty |  |
| related_entities | [] |
```
