# Esquema de entidad de tecnología

## Propósito

Una entidad de tecnología representa un lenguaje, framework, biblioteca, plataforma, herramienta, sistema de mensajería o contexto de tooling cuya utilización aparece en la trayectoria del usuario. Describe el uso respaldado en CareerOS; no documenta la tecnología en general ni equivale a una habilidad.

## Principios de diseño

- Cada tecnología debe tener un ID estable y un único archivo canónico.
- La entidad debe describir cómo aparece la tecnología en la evidencia, no sus características genéricas.
- El nivel de evidencia refleja la calidad, recurrencia y detalle del uso documentado, no una autoevaluación de dominio.
- Las relaciones deben usar IDs canónicos solo cuando exista el archivo de destino.
- La presencia en un entorno no demuestra propiedad, administración o profundidad de uso.
- Las tecnologías se enlazan con habilidades únicamente cuando la relación está respaldada; una tecnología nunca se modela como habilidad.

## Campos canónicos

| Campo | Obligatorio | Descripción |
|---|---:|---|
| `id` | Sí | Identificador único y estable con formato `technology:<slug>`. |
| `name` | Sí | Nombre canónico de la tecnología. |
| `type` | Sí | Clase factual: lenguaje, framework, biblioteca, database/query-language, plataforma, herramienta, messaging, devops o process/tooling, entre otras. |
| `category` | Sí | Agrupación contextual principal, como backend, database, devops, game-development, automation, messaging, testing o personal-projects. |
| `description` | Sí | Descripción compacta del lugar que ocupa la tecnología en la trayectoria documentada. |
| `evidence_level` | Sí | `strong`, `moderate`, `limited` o `candidate`. |
| `chronology` | Sí | Periodos de uso o exposición, con la precisión y reservas disponibles. |
| `contexts` | Sí | Entornos profesionales, académicos o personales en los que aparece. |
| `related_roles` | Sí | IDs canónicos de roles que aportan evidencia. |
| `related_projects` | Sí | IDs canónicos de proyectos que aportan evidencia. |
| `related_stories` | Sí | IDs canónicos de historias que aportan ejemplos concretos. |
| `related_skills` | Sí | IDs canónicos de habilidades claramente relacionadas con el uso observado. |
| `usage_summary` | Sí | Síntesis factual de cómo se utilizó o apareció, sin explicación genérica de la tecnología. |
| `representative_examples` | Sí | Referencias compactas a entidades relacionadas que delimitan ejemplos representativos. |
| `boundaries` | Sí | Capacidades, profundidad, propiedad, administración o alcance que la evidencia no demuestra. |
| `evidence` | Sí | Rutas raw, entidades o confirmaciones explícitas que respaldan el contenido. |
| `uncertainty` | Sí | Vacíos de cronología, alcance, atribución, versión, contexto o intensidad de uso. |
| `related_entities` | Sí | Otros IDs canónicos relacionados no cubiertos por los campos anteriores. |

## Niveles de evidencia

- `strong`: uso directo, sostenido o recurrente con varios contextos o ejemplos concretos.
- `moderate`: uso directo y claro, pero limitado a uno o pocos contextos o con detalle parcial.
- `limited`: mención directa o exposición concreta con poco detalle sobre tareas, continuidad o profundidad.
- `candidate`: la tecnología está mencionada o confirmada, pero falta evidencia suficiente para describir un uso delimitado.

## Reglas de validación

- Todos los campos deben estar presentes, incluso con `[]` o incertidumbre explícita.
- `related_roles`, `related_projects`, `related_stories`, `related_skills` y `related_entities` solo pueden contener IDs cuyos archivos canónicos existan.
- `usage_summary` y `representative_examples` deben limitarse a hechos respaldados y no convertirse en documentación genérica, viñetas de CV o texto promocional.
- Una tecnología no debe recibir un nivel alto por aparecer únicamente en una lista, una oferta objetivo o un entorno del equipo.
- La exposición a una plataforma o herramienta no prueba su administración, diseño, operación profunda ni propiedad.
- Los backlinks en roles, proyectos y empresas solo se añaden cuando el uso está situado con claridad en ese contexto.
- La incertidumbre relevante debe conservarse y no resolverse por plausibilidad técnica.

## Esqueleto

```markdown
# Tecnología: [Nombre]

## Canonical Fields

| Field | Value |
|---|---|
| id | `technology:...` |
| name |  |
| type |  |
| category |  |
| description |  |
| evidence_level |  |
| chronology |  |
| contexts |  |
| related_roles | [] |
| related_projects | [] |
| related_stories | [] |
| related_skills | [] |
| usage_summary |  |
| representative_examples |  |
| boundaries |  |
| evidence |  |
| uncertainty |  |
| related_entities | [] |
```
