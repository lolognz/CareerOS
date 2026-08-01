# Proyecto: Generación documental de Mercury TFS

## Canonical Fields

| Field | Value |
|---|---|
| id | `project:mercury-document-generation` |
| name | Generación documental de Mercury TFS |
| type | Área funcional y conjunto de microservicios |
| status | Estado posterior a 2023 desconocido |
| chronology | Parte de la etapa Mercury TFS 2020–2023; el periodo concreto de responsabilidad principal no está documentado. |
| organization | Mercury TFS |
| organization_id | `company:mercury-tfs` |
| related_roles | [`role:mercury-tfs-software-engineer`] |
| stories | [] |
| skills | [`skill:backend-development`, `skill:microservices`] |
| context | Área de generación de documentos dentro de la plataforma de trade finance, reorganizada en un equipo pequeño durante una etapa posterior. |
| problem | Generar distintos tipos de documentos dentro de la plataforma y mantener los microservicios asociados. |
| contribution | Responsabilidad sobre tareas de generación documental; durante un periodo el usuario fue el único desarrollador que atendía esta área junto con contabilidad. |
| systems | Microservicios separados por tipo de documento y componentes heredados que afectaban la generación del esquema de base de datos. |
| technologies | [`technology:ci-cd`, `technology:hibernate`, `technology:java`, `technology:spring`, `technology:spring-boot`, `technology:sql`] |
| achievements | [`achievement:mercury-functional-reference-areas`, `achievement:mercury-integration-base-deployment-simplification`] |
| users_or_stakeholders | Equipo técnico, responsables del proyecto, interlocutores de cliente y áreas usuarias de documentos; detalle no documentado. |
| outcomes | Mantenimiento y evolución del área. IntegrationBase eliminó la necesidad de ciertos scripts de despliegue, pero su detalle queda reservado para una futura historia. |
| evidence | `knowledge/raw/interviews/2026-07-cto-adjunto-fast-track.md`; `knowledge/entities/roles/mercury-tfs-software-engineer.md` |
| uncertainty | No constan fechas exactas, tipos de documento, número de servicios, usuarios, volumen ni métricas operativas. |
| related_entities | [`project:mercury-trade-finance-platform`] |

## Entidades candidatas pendientes

- Historia candidata: IntegrationBase.

## Incertidumbre y evidencia

La condición de único desarrollador se limita al periodo y las áreas descritas; no implica responsabilidad exclusiva sobre toda la plataforma. Fuente principal: `knowledge/raw/interviews/2026-07-cto-adjunto-fast-track.md`.
