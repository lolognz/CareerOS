# Tecnología: Hibernate

## Canonical Fields

| Field | Value |
|---|---|
| id | `technology:hibernate` |
| name | Hibernate |
| type | library |
| category | backend |
| description | Tecnología de persistencia presente en la plataforma y los microservicios de Mercury TFS. |
| evidence_level | moderate |
| chronology | Uso situado en la etapa Mercury TFS, aproximadamente entre 2020 y 2023. |
| contexts | Trade finance, generación documental, herencia monolítica y generación de tablas en microservicios. |
| related_roles | [`role:mercury-tfs-software-engineer`] |
| related_projects | [`project:mercury-document-generation`, `project:mercury-trade-finance-platform`] |
| related_stories | [`story:mercury-integration-base`] |
| related_skills | [`skill:backend-development`, `skill:legacy-system-diagnosis`] |
| usage_summary | Formó parte del stack de Mercury y del contexto de persistencia en el que un objeto heredado impedía generar correctamente tablas para microservicios. |
| representative_examples | `story:mercury-integration-base` delimita el problema de generación de tablas y la sustitución del comportamiento heredado. |
| boundaries | La evidencia no detalla mappings, consultas, rendimiento, versión ni responsabilidad exclusiva sobre el diseño de persistencia. |
| evidence | Fuente raw, sección “Mercury TFS”; `story:mercury-integration-base`; proyectos relacionados. |
| uncertainty | La fuente vincula Hibernate al entorno, pero no identifica qué parte exacta del episodio IntegrationBase dependía directamente de él. |
| related_entities | [`technology:java`, `technology:spring`, `technology:sql`] |
