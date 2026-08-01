# Esquema de entidad de historia

## Propósito

Una historia representa un episodio profesional concreto: un problema, una decisión, un error, una transición o una entrega delimitada. Conserva hechos y relaciones reutilizables para futuras salidas, pero no es una respuesta de entrevista, una viñeta de CV ni el resumen de un rol, empresa o proyecto completo.

## Principios de diseño

- Cada historia debe tener un ID estable y un único archivo canónico.
- La historia debe mantenerse compacta y centrada en un episodio.
- La cronología debe usar únicamente la precisión respaldada por las fuentes.
- Las acciones y decisiones deben distinguir la contribución individual del trabajo compartido.
- Los resultados reportados, las impresiones recordadas y las métricas ambiguas deben conservar sus reservas.
- Las relaciones solo deben usar IDs canónicos cuando exista el archivo de destino.
- Las habilidades, tecnologías y logros sin entidad canónica solo pueden aparecer como texto plano en `Entidades candidatas pendientes`.

## Campos canónicos

| Campo | Obligatorio | Descripción |
|---|---:|---|
| `id` | Sí | Identificador único y estable con formato `story:<slug>`. |
| `title` | Sí | Nombre factual y reconocible del episodio. |
| `type` | Sí | Naturaleza del episodio: entrega, decisión, error y aprendizaje, transición, resolución técnica, operación u otra respaldada. |
| `chronology` | Sí | Periodo con la máxima precisión disponible y sus reservas. |
| `organization` | Sí | Organización o contexto independiente donde ocurrió. |
| `organization_id` | Sí | ID canónico de organización cuando exista; `[]` cuando no exista o no sea aplicable. |
| `related_roles` | Sí | IDs canónicos de roles claramente relacionados. |
| `related_projects` | Sí | IDs canónicos de proyectos claramente relacionados. |
| `context` | Sí | Entorno mínimo necesario para entender el episodio. |
| `situation` | Sí | Estado o desencadenante concreto del episodio. |
| `problem` | Sí | Dificultad, necesidad o riesgo abordado. |
| `constraints` | Sí | Límites de tiempo, conocimiento, recursos, proceso o atribución documentados. |
| `actions` | Sí | Actuaciones observables de la persona, separando el trabajo compartido. |
| `decisions` | Sí | Elecciones documentadas; valor explícitamente desconocido cuando no consten. |
| `outcome` | Sí | Resultado respaldado, sin inflar impacto ni convertir intención en causalidad probada. |
| `evidence` | Sí | Rutas raw, IDs o notas de procedencia que respaldan la historia. |
| `uncertainty` | Sí | Fechas, alcance, causalidad, autoría, métricas o detalles no confirmados. |
| `reusable_angles` | Sí | Perspectivas factuales para reutilización futura, no respuestas ya redactadas. |
| `related_entities` | Sí | Otros IDs canónicos relacionados no cubiertos por los campos anteriores. |

## Reglas de validación

- Todos los campos deben estar presentes, incluso con `[]` o un valor explícitamente desconocido.
- `organization_id`, `related_roles`, `related_projects` y `related_entities` solo pueden contener IDs cuyo archivo canónico exista.
- Una historia no debe abarcar un rol o proyecto entero salvo que el proyecto solo tenga sentido como episodio pequeño.
- No debe adoptar STAR como prosa final, aunque conserve material suficiente para una futura generación.
- No debe contener viñetas de CV, lenguaje promocional, impacto inventado ni métricas verificadas por inferencia.
- Cuando la fuente solo permita una historia mínima, deben conservarse los vacíos en lugar de completarlos por plausibilidad.
- Las relaciones inversas en empresas, roles y proyectos deben añadirse únicamente cuando sean claras.

## Esqueleto

```markdown
# Historia: [Título]

## Canonical Fields

| Field | Value |
|---|---|
| id | `story:...` |
| title |  |
| type |  |
| chronology |  |
| organization |  |
| organization_id | [] |
| related_roles | [] |
| related_projects | [] |
| context |  |
| situation |  |
| problem |  |
| constraints |  |
| actions |  |
| decisions |  |
| outcome |  |
| evidence |  |
| uncertainty |  |
| reusable_angles |  |
| related_entities | [] |

## Entidades candidatas pendientes
```
