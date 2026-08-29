# Proyecto: Plataforma de trade finance de Mercury TFS

## Canonical Fields

| Field | Value |
|---|---|
| id | `project:mercury-trade-finance-platform` |
| name | Plataforma de trade finance de Mercury TFS |
| type | Producto de software bancario y sistema empresarial |
| status | Estado posterior a 2023 desconocido |
| chronology | Relacionado con el rol desde 2020-01 aproximadamente hasta algún momento de 2023. |
| organization | Mercury TFS |
| organization_id | `company:mercury-tfs` |
| related_roles | [`role:mercury-tfs-software-engineer`] |
| stories | [`story:mercury-account-fields`, `story:mercury-integration-base`] |
| skills | [`skill:api-design-and-integration`, `skill:backend-development`, `skill:legacy-system-diagnosis`, `skill:microservices`, `skill:requirements-analysis`] |
| context | Plataforma para operaciones de importación y exportación en las que bancos median entre empresas que no se conocen o no confían entre sí. |
| problem | Dar soporte de software a procesos complejos de trade finance. |
| contribution | Creación y consumo de APIs REST en Java, primero implementando diseños técnicos sénior y después elaborando también diseño e implementación; estimación, reuniones con cliente, gestión de tareas, revisión de código y apoyo a compañeros. En una integración Python intermitente de unos tres meses, consumió la API REST de software externo y expuso otra API para facilitar su consumo por Mercury. |
| systems | Aplicación compleja con herencia monolítica y microservicios, incluida funcionalidad de contabilidad y generación documental. |
| technologies | [`technology:bash`, `technology:ci-cd`, `technology:docker`, `technology:elasticsearch`, `technology:hibernate`, `technology:java`, `technology:kubernetes`, `technology:linux`, `technology:python`, `technology:spring`, `technology:spring-boot`, `technology:sql`] |
| achievements | [`achievement:mercury-functional-reference-areas`, `achievement:mercury-integration-base-deployment-simplification`] |
| users_or_stakeholders | Clientes bancarios, interlocutores de negocio, equipo técnico y responsables del proyecto. |
| outcomes | No constan resultados globales del producto ni métricas de negocio o adopción atribuibles a la contribución del usuario. |
| evidence | `knowledge/raw/interviews/2026-07-cto-adjunto-fast-track.md`; `knowledge/raw/interviews/2026-08-29-post-smadex-knowledge-verification.md`; `knowledge/entities/roles/mercury-tfs-software-engineer.md` |
| uncertainty | No constan nombre comercial del producto, fechas internas, alcance completo, clientes concretos ni estado posterior a 2023. Sobre la integración Python no constan fechas exactas, librerías, despliegue final ni producto externo concreto. |
| related_entities | [`project:mercury-document-generation`] |

## Entidades candidatas pendientes

- Proyecto candidato: área contable.
- Tecnología candidata: Sencha.
- Historia candidata: account fields.
- Historia candidata: IntegrationBase.

## Incertidumbre y evidencia

IntegrationBase se conserva como candidata a historia, no como proyecto de esta primera versión. Fuente principal: `knowledge/raw/interviews/2026-07-cto-adjunto-fast-track.md`.

## Integración de software externo de análisis documental

Mercury había adquirido software externo que utilizaba inteligencia artificial para analizar documentos a partir de imágenes, pero no había conseguido integrarlo en su sistema. El software exponía una API REST: Manuel analizó su respuesta, implementó un consumidor Python y después expuso una API desde su programa de integración para que Mercury consumiera más fácilmente la capacidad externa. Preparó Docker y Docker Compose para desplegar o probar el programa, todavía temprano, y utilizar el modelo de ejecución en contenedores. El trabajo ocupó aproximadamente tres meses de forma intermitente, no a tiempo completo.

Esta contribución demuestra análisis e integración profesional con Python, pero no desarrollo ni propiedad del producto externo, construcción o entrenamiento de modelos, backend extenso en Python ni especialización prolongada. El desarrollo Java de Manuel en Mercury también utilizaba APIs REST; esto no demuestra API First, gobierno de APIs, ownership completo de contratos ni diseño de toda la arquitectura API.

## Entorno Linux

Linux era el entorno profesional de trabajo. Manuel lo utilizaba activamente mediante uso sustancial de terminal y scripting Bash, y gestionaba Docker. En Kubernetes operaba en preproducción: logs, ejecución dentro de pods, reinicio o borrado y troubleshooting. Cuando dejó Mercury, la producción era reciente y otro equipo la operaba. Este alcance no implica administración de sistemas, servidores o clústeres, escalado ni ownership de platform engineering.
