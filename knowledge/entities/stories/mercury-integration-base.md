# Historia: IntegrationBase en Mercury TFS

## Canonical Fields

| Field | Value |
|---|---|
| id | `story:mercury-integration-base` |
| title | IntegrationBase en Mercury TFS |
| type | Diagnóstico y resolución técnica colaborativa |
| chronology | Durante el rol en Mercury TFS, aproximadamente entre 2020 y 2023; la causa se identificó después de más de dos años según el recuerdo. |
| organization | Mercury TFS |
| organization_id | `company:mercury-tfs` |
| related_roles | [`role:mercury-tfs-software-engineer`] |
| related_projects | [`project:mercury-trade-finance-platform`] |
| context | La plataforma combinaba herencia monolítica y microservicios, con generación de esquema de base de datos y despliegues automatizados. |
| situation | Un objeto Base heredado del monolito impedía generar correctamente las tablas de base de datos de los microservicios. |
| problem | Los despliegues necesitaban scripts para producir la información correcta de base de datos. |
| constraints | Comportamiento heredado difícil de aislar y causa no identificada durante más de dos años. |
| actions | El usuario y un compañero identificaron que Base era la causa y crearon conjuntamente IntegrationBase para conservar el comportamiento necesario sin bloquear la generación. |
| decisions | Separar el comportamiento requerido en IntegrationBase en vez de seguir dependiendo del objeto Base heredado y de scripts de despliegue. |
| outcome | La generación de base de datos pudo funcionar correctamente sin los scripts de despliegue asociados al problema. |
| evidence | `knowledge/raw/interviews/2026-07-cto-adjunto-fast-track.md`, sección “Previous Experience: Mercury TFS”; `knowledge/entities/roles/mercury-tfs-software-engineer.md`. |
| uncertainty | No constan fecha, servicios afectados, pruebas, métricas, alcance del cambio ni reparto detallado de contribuciones entre el usuario y su compañero. |
| reusable_angles | Diagnóstico de legado; colaboración técnica; simplificación de despliegues; eliminación de una solución auxiliar. |
| related_entities | [] |

## Entidades candidatas pendientes

- Tecnología candidata: Java.
- Tecnología candidata: Spring.
- Tecnología candidata: Hibernate.
- Habilidad candidata: diagnóstico de sistemas heredados.
