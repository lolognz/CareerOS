# Esquema de entidad de rol

## Propósito

Una entidad de rol representa una relación profesional, académica, investigadora o empresarial desempeñada por la persona durante un periodo determinado y en el contexto de una organización.

El rol conecta la cronología profesional con responsabilidades, sistemas, proyectos, historias, tecnologías, habilidades, logros y evidencia. No es una sección de CV, una descripción comercial ni un relato completo de los proyectos asociados.

## Principios de diseño

- Cada periodo o relación laboral diferenciable debe tener un único archivo canónico.
- La cronología debe conservar la precisión real de las fuentes.
- Las responsabilidades recurrentes pertenecen al rol; el detalle completo de proyectos e historias pertenece a sus propias entidades.
- Las relaciones deben expresarse mediante IDs canónicos cuando exista la entidad relacionada.
- Los datos desconocidos, aproximados o discutibles deben aparecer en `uncertainty` y no resolverse mediante inferencias.
- Todo hecho debe poder rastrearse hasta evidencia o quedar señalado como pendiente de evidencia.
- El contenido debe ser factual, reutilizable y ajeno a un formato de candidatura concreto.

## Campos canónicos

| Campo | Obligatorio | Descripción |
|---|---:|---|
| `id` | Sí | Identificador canónico, único y estable del rol. |
| `title` | Sí | Título formal o funcional del rol, sin embellecimiento. |
| `organization` | Sí | Nombre de la organización o contexto organizativo en el que se desempeñó el rol. |
| `organization_id` | Sí | ID canónico de la entidad de organización. Si todavía no existe, se registra la relación como pendiente sin inventar una entidad. |
| `start_date` | Sí | Fecha de inicio con la máxima precisión respaldada. |
| `end_date` | Sí | Fecha de fin respaldada, `presente` para un rol vigente o valor explícitamente desconocido. |
| `date_precision` | Sí | Precisión y posibles aproximaciones de las fechas de inicio y fin. |
| `location` | Sí | Lugar o modalidad de trabajo cuando se conoce; en otro caso, valor explícitamente desconocido. |
| `employment_type` | Sí | Tipo de relación: empleo, prácticas, trabajo autónomo, investigación, consultoría u otro tipo respaldado. |
| `seniority` | Sí | Nivel formal o funcional respaldado, incluida su evolución cuando corresponda. |
| `context` | Sí | Contexto factual necesario para interpretar el rol, la organización, el equipo o el dominio. |
| `responsibilities` | Sí | Áreas recurrentes de responsabilidad durante el rol. |
| `systems` | Sí | Sistemas, productos o ámbitos técnicos mantenidos o desarrollados. |
| `projects` | Sí | IDs canónicos de proyectos relacionados. Lista vacía cuando no existan entidades canónicas. |
| `stories` | Sí | IDs canónicos de historias relacionadas. Lista vacía cuando no existan entidades canónicas. |
| `technologies` | Sí | IDs canónicos de tecnologías relacionadas. Lista vacía cuando no existan entidades canónicas. |
| `skills` | Sí | IDs canónicos de habilidades relacionadas. Lista vacía cuando no existan entidades canónicas. |
| `achievements` | Sí | IDs canónicos de logros relacionados. Lista vacía cuando no existan entidades canónicas. |
| `evidence` | Sí | Fuentes que respaldan el contenido del rol, mediante ID canónico o ruta de una fuente raw. |
| `uncertainty` | Sí | Fechas aproximadas, títulos no confirmados, límites de alcance, discrepancias y vacíos de evidencia. |
| `related_entities` | Sí | Otros IDs canónicos relacionados que no estén cubiertos por campos anteriores. |

## Secciones estructuradas

Cada archivo debe comenzar con una tabla `Canonical Fields` que contenga todos los campos del esquema. Después puede desarrollar los hechos en secciones como:

- Contexto.
- Responsabilidades.
- Sistemas y ámbito de trabajo.
- Evolución del rol.
- Relaciones con proyectos e historias.
- Logros y resultados documentados.
- Incertidumbre y vacíos.
- Evidencia.

Estas secciones deben ampliar los campos sin copiar historias completas ni transformar los hechos en texto de CV.

## Reglas de validación

- El `id` debe ser único y estable, con el formato `role:<slug>`.
- `organization_id` y las relaciones deben usar IDs canónicos, no nombres libres, cuando la entidad exista.
- `start_date`, `end_date` y `date_precision` deben ser coherentes entre sí.
- Un rol vigente debe usar `presente` como `end_date`; no debe prolongarse por inferencia un rol finalizado.
- El título formal y el funcional deben distinguirse cuando la fuente no permita tratarlos como equivalentes.
- Las responsabilidades deben describir trabajo recurrente, no afirmaciones promocionales.
- Los proyectos y las historias deben enlazarse, no reproducirse íntegramente.
- Los logros sin entidad canónica pueden describirse como hechos respaldados, pero no recibir un ID inventado.
- Las tecnologías y habilidades solo deben asociarse cuando la evidencia las sitúe en el rol.
- La evidencia raw puede citarse por su ruta dentro del repositorio.
- Toda ambigüedad relevante debe conservarse en `uncertainty`.

## Antipatrones

Una entidad de rol no debe contener:

- Viñetas redactadas para un CV.
- Lenguaje de marketing o posicionamiento profesional.
- Responsabilidades o impacto inventados.
- Títulos inflados, incluidos títulos de dirección tecnológica no desempeñados.
- Historias o proyectos copiados por completo.
- Tecnologías asignadas por plausibilidad.
- Fechas presentadas con mayor precisión que la fuente.
- Datos educativos ajenos al rol o no completados.
- Hechos exclusivos de una salida generada.

## Esqueleto

```markdown
# Rol: [Título y contexto]

## Canonical Fields

| Field | Value |
|---|---|
| id | role:... |
| title |  |
| organization |  |
| organization_id | company:... |
| start_date |  |
| end_date |  |
| date_precision |  |
| location |  |
| employment_type |  |
| seniority |  |
| context |  |
| responsibilities |  |
| systems |  |
| projects | [] |
| stories | [] |
| technologies | [] |
| skills | [] |
| achievements | [] |
| evidence |  |
| uncertainty |  |
| related_entities | [] |

## Contexto

## Responsabilidades

## Sistemas y ámbito de trabajo

## Relaciones

## Incertidumbre

## Evidencia
```
