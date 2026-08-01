# Esquema de entidad de proyecto

## Propósito

Una entidad de proyecto representa un cuerpo de trabajo delimitado: un producto, sistema, iniciativa, área técnica o proyecto personal, profesional, académico o de investigación. Conecta el problema abordado, la contribución de la persona, los sistemas implicados, la cronología, las organizaciones, los roles y la evidencia.

Un proyecto no es un rol, una historia concreta ni una redacción para CV. Tampoco sustituye a una entidad de empresa. Debe conservar hechos reutilizables sin copiar el contenido completo de esas entidades relacionadas.

## Principios de diseño

- Cada proyecto debe tener un archivo canónico y un ID estable.
- La unidad debe ser suficientemente delimitada para distinguirla de un rol completo, pero puede representar un sistema o área mantenida durante un periodo.
- Las fechas deben conservar la precisión de la evidencia.
- Los resultados deben distinguir hechos observados de cifras reportadas, objetivos y efectos posibles.
- Las relaciones solo deben usar IDs canónicos cuando el archivo de destino exista.
- Las tecnologías, historias, habilidades o logros sin entidad canónica deben quedar como candidatos en texto plano.
- Los proyectos personales con madurez desconocida deben conservar esa incertidumbre.

## Campos canónicos

| Campo | Obligatorio | Descripción |
|---|---:|---|
| `id` | Sí | Identificador canónico único y estable con formato `project:<slug>`. |
| `name` | Sí | Nombre canónico del proyecto, producto, sistema o área. |
| `type` | Sí | Tipo factual: producto, investigación y desarrollo, sistema, migración, automatización o proyecto personal, entre otros. |
| `status` | Sí | Estado respaldado; si no se conoce, debe indicarse explícitamente. |
| `chronology` | Sí | Periodo del proyecto con la máxima precisión disponible y sus reservas. |
| `organization` | Sí | Organización o contexto independiente del proyecto. |
| `organization_id` | Sí | ID canónico de organización cuando exista; `[]` para un proyecto independiente o cuando no haya entidad canónica aplicable. |
| `related_roles` | Sí | IDs canónicos de roles claramente relacionados. |
| `stories` | Sí | IDs canónicos de historias concretas claramente relacionadas. |
| `skills` | Sí | IDs canónicos de habilidades demostradas de forma clara en el proyecto. |
| `context` | Sí | Entorno factual necesario para comprender el proyecto. |
| `problem` | Sí | Necesidad o problema que dio origen o sentido al proyecto. |
| `contribution` | Sí | Alcance documentado de la contribución de la persona, sin atribuir trabajo ajeno. |
| `systems` | Sí | Componentes, flujos o límites técnicos documentados. |
| `technologies` | Sí | IDs canónicos de tecnologías existentes; `[]` cuando aún no existan esas entidades. |
| `users_or_stakeholders` | Sí | Usuarios, clientes, colaboradores o partes interesadas conocidas. |
| `outcomes` | Sí | Resultados documentados, con reservas explícitas para cifras reportadas o significado incierto. |
| `evidence` | Sí | Rutas o IDs de fuentes que respaldan los hechos. |
| `uncertainty` | Sí | Vacíos, fechas aproximadas, estado desconocido, atribuciones parciales o métricas no verificadas. |
| `related_entities` | Sí | Otros IDs canónicos relacionados no cubiertos por organización o roles. |

## Secciones estructuradas

Después de la tabla `Canonical Fields`, el archivo puede ampliar de forma compacta:

- Contexto y problema.
- Contribución.
- Sistemas.
- Usuarios y partes interesadas.
- Resultados documentados.
- Entidades candidatas pendientes.
- Incertidumbre y evidencia.

## Reglas de validación

- Todos los campos deben estar presentes, incluso con valor explícitamente desconocido o `[]`.
- `organization_id`, `related_roles`, `stories`, `skills`, `technologies` y `related_entities` solo pueden contener IDs de archivos canónicos existentes.
- Un proyecto independiente puede usar `organization_id | []` y `related_roles | []`.
- Los detalles completos de roles e historias no deben copiarse.
- Las habilidades deben enlazarse cuando estén respaldadas por la contribución, los sistemas, los resultados o historias del proyecto; no deben asignarse por plausibilidad.
- Los resultados no deben formularse como impacto probado cuando la evidencia solo registra intención, visibilidad reportada o una métrica ambigua.
- IntegrationBase debe tratarse como candidata a historia mientras no exista una razón estructural y evidencia para modelarla de otro modo.
- Una salida generada no debe usarse como única fuente de hechos canónicos.

## Esqueleto

```markdown
# Proyecto: [Nombre]

## Canonical Fields

| Field | Value |
|---|---|
| id | `project:...` |
| name |  |
| type |  |
| status |  |
| chronology |  |
| organization |  |
| organization_id | [] |
| related_roles | [] |
| stories | [] |
| skills | [] |
| context |  |
| problem |  |
| contribution |  |
| systems |  |
| technologies | [] |
| users_or_stakeholders |  |
| outcomes |  |
| evidence |  |
| uncertainty |  |
| related_entities | [] |
```
