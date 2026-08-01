# Esquema de entidad de habilidad

## Propósito

Una entidad de habilidad representa una capacidad demostrada o un comportamiento profesional recurrente. Conecta conductas observables con roles, proyectos, historias y evidencia, sin convertir herramientas o tecnologías en habilidades ni presentar una autoevaluación como hecho probado.

## Principios de diseño

- Cada habilidad debe tener un ID estable y un único archivo canónico.
- La evidencia debe prevalecer sobre el atractivo del nombre de la habilidad.
- Los comportamientos observados deben ser acciones concretas, no rasgos de personalidad.
- Los ejemplos deben enlazar entidades existentes en lugar de reescribirlas.
- El nivel de evidencia debe ser conservador y puede variar cuando aparezcan nuevas fuentes.
- Los límites deben indicar qué títulos, alcance, dominio o resultados no demuestra la evidencia.
- Lenguajes, frameworks, plataformas y herramientas pertenecen a tecnologías, no a habilidades.

## Campos canónicos

| Campo | Obligatorio | Descripción |
|---|---:|---|
| `id` | Sí | Identificador único y estable con formato `skill:<slug>`. |
| `name` | Sí | Nombre canónico de la capacidad. |
| `type` | Sí | Clasificación factual: técnica, arquitectónica, operativa, comunicación, liderazgo, investigación, negocio o aprendizaje, entre otras. |
| `description` | Sí | Definición compacta de la capacidad tal como está respaldada en CareerOS. |
| `evidence_level` | Sí | `strong`, `moderate`, `limited` o `inferred-from-pattern`. |
| `chronology` | Sí | Periodos en los que se observa, conservando precisión y vacíos. |
| `contexts` | Sí | Dominios y entornos donde aparece la capacidad. |
| `related_roles` | Sí | IDs canónicos de roles que aportan evidencia. |
| `related_projects` | Sí | IDs canónicos de proyectos que aportan evidencia. |
| `related_stories` | Sí | IDs canónicos de historias que aportan ejemplos concretos. |
| `observed_behaviors` | Sí | Acciones recurrentes o verificables asociadas a la habilidad. |
| `representative_examples` | Sí | Referencias compactas a roles, proyectos o historias representativas. |
| `boundaries` | Sí | Lo que la evidencia no demuestra: títulos, alcance, dominio, impacto o profundidad no confirmados. |
| `evidence` | Sí | Rutas o entidades que respaldan el contenido. |
| `uncertainty` | Sí | Vacíos, inferencias, cronología aproximada y límites de atribución. |
| `related_entities` | Sí | Otros IDs canónicos relacionados no cubiertos por los campos anteriores. |

## Niveles de evidencia

- `strong`: capacidad observada de forma recurrente, sostenida o en varios contextos con ejemplos concretos.
- `moderate`: evidencia directa y clara, pero limitada a uno o pocos contextos o episodios.
- `limited`: indicio directo con poco detalle, alcance o madurez documentada.
- `inferred-from-pattern`: patrón razonable derivado de varias conductas, sin una demostración directa suficientemente delimitada.

## Reglas de validación

- Todos los campos deben estar presentes, incluso con `[]` o incertidumbre explícita.
- `related_roles`, `related_projects`, `related_stories` y `related_entities` solo pueden contener IDs de archivos canónicos existentes.
- `representative_examples` debe referenciar entidades enlazadas en la tabla y no duplicar sus narrativas.
- Una habilidad no puede ser una tecnología, título, rasgo personal, aspiración o logro.
- Las declaraciones de filosofía profesional pueden complementar la evidencia, pero no bastan por sí solas para asignar un nivel fuerte.
- Los proyectos personales sin madurez o uso documentados no deben elevar por sí solos una habilidad por encima de `limited`.
- Los backlinks en empresas, roles y proyectos solo deben añadirse cuando la asociación esté claramente respaldada.
- Las tecnologías y logros candidatos no reciben IDs de habilidad.

## Esqueleto

```markdown
# Habilidad: [Nombre]

## Canonical Fields

| Field | Value |
|---|---|
| id | `skill:...` |
| name |  |
| type |  |
| description |  |
| evidence_level |  |
| chronology |  |
| contexts |  |
| related_roles | [] |
| related_projects | [] |
| related_stories | [] |
| observed_behaviors |  |
| representative_examples |  |
| boundaries |  |
| evidence |  |
| uncertainty |  |
| related_entities | [] |
```
