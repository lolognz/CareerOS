# Proyecto: Sistemas de pagos de Deutsche Bank

## Canonical Fields

| Field | Value |
|---|---|
| id | `project:deutsche-bank-payments-systems` |
| name | Sistemas de pagos de Deutsche Bank |
| type | Área de sistemas críticos y mantenimiento evolutivo y operativo |
| status | Activo en julio de 2026 |
| chronology | Vinculado al empleo directo desde 2024-09 hasta el presente; el trabajo en pagos comenzó durante la consultoría anterior, sin fecha exacta documentada. |
| organization | Deutsche Bank |
| organization_id | `company:deutsche-bank` |
| related_roles | [`role:deutsche-bank-senior-backend-software-engineer`] |
| stories | [`story:deutsche-bank-transfer-to-payments-team`] |
| skills | [`skill:backend-development`, `skill:critical-systems-operation`, `skill:microservices`, `skill:production-support-and-debugging`] |
| context | Conjunto de microservicios bancarios mantenidos por un equipo pequeño, experimentado y autónomo. |
| problem | Mantener y operar flujos de pagos cuya interrupción puede tener consecuencias importantes para el negocio. |
| contribution | Desarrollo, despliegues, gestión de colas MQ y certificados, tratamiento de vulnerabilidades, investigación de errores y soporte a otros equipos dentro del rol directo. |
| systems | Microservicios para transferencias entrantes y salientes, pagos desde cuentas, pagos recurrentes e inmediatos, SEPA y transferencias transfronterizas; entornos de pruebas, producción y recuperación ante desastres. |
| technologies | [`technology:ibm-mq`, `technology:java`, `technology:node-js`, `technology:spring`, `technology:spring-boot`] |
| achievements | [`achievement:deutsche-bank-transfer-to-critical-payments-team`] |
| users_or_stakeholders | Equipo de pagos, otros equipos que se comunican con los sistemas y áreas de negocio dependientes de los flujos de pagos. |
| outcomes | El mantenimiento y la operación forman parte del trabajo documentado; no se aportan métricas de disponibilidad, volumen o impacto atribuible al usuario. |
| evidence | `knowledge/raw/interviews/2026-07-cto-adjunto-fast-track.md`; `knowledge/entities/roles/deutsche-bank-senior-backend-software-engineer.md` |
| uncertainty | No constan nombres internos, métricas de tráfico, fecha exacta de entrada al equipo ni delimitación temporal de cada responsabilidad entre consultoría y empleo directo. |
| related_entities | [] |

## Entidades candidatas pendientes

- Historia candidata: investigación de un incidente grave en producción.
- Historia candidata: soporte ante errores de comunicación reportados por otros equipos.

## Incertidumbre y evidencia

La criticidad está respaldada por la fuente, pero no se convierte en una afirmación de resultados individuales. Fuente principal: `knowledge/raw/interviews/2026-07-cto-adjunto-fast-track.md`.
