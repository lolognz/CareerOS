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
| skills | [`skill:api-design-and-integration`, `skill:backend-development`, `skill:critical-systems-operation`, `skill:microservices`, `skill:production-support-and-debugging`] |
| context | Conjunto de microservicios bancarios mantenidos por un equipo pequeño, experimentado y autónomo. |
| problem | Mantener y operar flujos de pagos cuya interrupción puede tener consecuencias importantes para el negocio. |
| contribution | Desarrollo; creación o modificación y consumo de APIs, mayoritariamente REST y algunas SOAP, con participación en contratos internos, adaptación a contratos externos, OpenAPI y clientes SOAP generados mediante WSDL; mantenimiento personal desde aproximadamente principios de 2025 de cuatro microservicios Node.js heredados, incluida su ingeniería inversa inicial y pequeños cambios de código; despliegue y troubleshooting acotados sobre OpenShift; coordinación recurrente de despliegues fuera de horario; gestión de colas MQ y certificados; tratamiento de vulnerabilidades; diagnóstico de incidentes y soporte entre equipos. |
| systems | Microservicios para transferencias entrantes y salientes, pagos desde cuentas, pagos recurrentes e inmediatos, SEPA y transferencias transfronterizas; APIs mayoritariamente REST y algunas SOAP; entornos de pruebas, producción y recuperación ante desastres. |
| technologies | [`technology:ibm-mq`, `technology:java`, `technology:kubernetes`, `technology:node-js`, `technology:openshift`, `technology:spring`, `technology:spring-boot`] |
| achievements | [`achievement:deutsche-bank-transfer-to-critical-payments-team`] |
| users_or_stakeholders | Equipo de pagos, otros equipos que se comunican con los sistemas y áreas de negocio dependientes de los flujos de pagos. |
| outcomes | El mantenimiento y la operación forman parte del trabajo documentado; no se aportan métricas de disponibilidad, volumen o impacto atribuible al usuario. |
| evidence | `knowledge/raw/interviews/2026-07-cto-adjunto-fast-track.md`; `knowledge/raw/interviews/2026-08-29-post-smadex-knowledge-verification.md`; `knowledge/entities/roles/deutsche-bank-senior-backend-software-engineer.md` |
| uncertainty | No constan nombres internos, métricas de tráfico, fecha exacta de entrada al equipo ni delimitación temporal de cada responsabilidad entre consultoría y empleo directo; tampoco nombres, frameworks o versiones de los servicios Node.js. |
| related_entities | [] |

## Entidades candidatas pendientes

- Historia candidata: investigación de un incidente grave en producción.
- Historia candidata: soporte ante errores de comunicación reportados por otros equipos.

## Incertidumbre y evidencia

La criticidad está respaldada por la fuente, pero no se convierte en una afirmación de resultados individuales. Fuente principal: `knowledge/raw/interviews/2026-07-cto-adjunto-fast-track.md`.

## Operación de producción e incidentes

El equipo actúa con más frecuencia como proveedor de APIs que como consumidor. Manuel crea o modifica y consume APIs: la mayoría son REST y algunas SOAP. Participa en contratos internos, mientras que proveedores u organizaciones externas pueden imponer el contrato o protocolo. Escribe y modifica especificaciones OpenAPI y trabaja con su generación de código; en SOAP modifica contratos y utiliza clientes generados mediante WSDL.

Los servicios se despliegan sobre OpenShift. Manuel trabaja directamente con pods y logs, reinicios o borrado, deployments, escalado de réplicas, Services, ConfigMaps, Secrets y troubleshooting; edita plantillas predefinidas usadas por Helm entre entornos y utiliza OpenShift Routes para exponer servicios. No administra clústeres o plataforma ni tiene acceso irrestricto a comandos de infraestructura en producción.

El trabajo fuera del horario normal es recurrente: algunos meses contienen varios días y es inusual que un mes no incluya ninguno. Normalmente corresponde a cambios o despliegues en producción durante ventanas de menor tráfico, identificadas mediante monitorización como New Relic y Splunk y a menudo situadas alrededor de medianoche, más que a una guardia clásica de pager.

El equipo de Manuel organiza y controla los despliegues, prepara las instrucciones técnicas y se las entrega a otro equipo autorizado, que ejecuta los comandos restringidos en producción. Manuel y su equipo no tienen permiso para ejecutar directamente esos comandos.

Ante incidentes, investigan y resuelven los problemas de sus sistemas; cuando la evidencia apunta a otro sistema, enrutan o escalan el caso y colaboran con el equipo correspondiente. El diagnóstico puede abarcar interacciones con aplicaciones móviles o mainframe. Existe escalado telefónico fuera de horario para incidentes críticos, pero Manuel no ha recibido personalmente una llamada crítica. Los incidentes no críticos pueden encontrarse a primera hora y repriorizar el trabajo planificado.
