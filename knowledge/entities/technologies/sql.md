# Tecnología: SQL

## Canonical Fields

| Field | Value |
|---|---|
| id | `technology:sql` |
| name | SQL |
| type | database/query-language |
| category | database |
| description | Lenguaje de consulta usado en el contexto de la plataforma bancaria de Mercury TFS y mencionado entre los lenguajes del usuario. |
| evidence_level | moderate |
| chronology | Visto en la universidad; primer uso profesional documentado en Mercury TFS entre 2020 y 2023. |
| contexts | Trade finance, contabilidad, generación documental y persistencia de microservicios. |
| related_roles | [`role:mercury-tfs-software-engineer`] |
| related_projects | [`project:mercury-document-generation`, `project:mercury-trade-finance-platform`] |
| related_stories | [`story:mercury-integration-base`] |
| related_skills | [`skill:backend-development`, `skill:legacy-system-diagnosis`] |
| usage_summary | El usuario llegó a Mercury con conocimiento universitario sin experiencia profesional y trabajó en un sistema que usaba SQL, incluida funcionalidad contable y problemas de generación de tablas. |
| representative_examples | `story:mercury-integration-base` registra un problema persistente en la generación de información de base de datos para microservicios. |
| boundaries | No constan motor concreto para cada sistema, consultas escritas, optimización, administración de bases de datos ni profundidad en modelado. |
| evidence | Fuente raw, secciones “Mercury TFS” y “Technical Skills Mentioned”; entidades relacionadas. |
| uncertainty | MySQL y Oracle se mencionan en una lista separada, pero no se asignan aquí a proyectos concretos. |
| related_entities | [`technology:hibernate`] |
