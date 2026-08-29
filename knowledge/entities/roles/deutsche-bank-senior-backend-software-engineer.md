# Rol: Senior Backend Software Engineer — Deutsche Bank

## Canonical Fields

| Field | Value |
|---|---|
| id | `role:deutsche-bank-senior-backend-software-engineer` |
| title | Senior Backend Software Engineer |
| organization | Deutsche Bank |
| organization_id | `company:deutsche-bank` |
| start_date | 2024-09 |
| end_date | presente |
| date_precision | Mes de inicio confirmado; el rol seguía vigente en la actualización de la fuente de julio de 2026. |
| location | Desconocida en la evidencia disponible |
| employment_type | Empleo directo |
| seniority | Senior; el usuario se considera la persona con menos experiencia dentro de un equipo pequeño y experimentado. |
| context | Equipo de pagos bancarios crítico, con autonomía y responsabilidad sobre desarrollo, operación y soporte de microservicios. |
| responsibilities | Revisión operativa diaria, desarrollo, creación o modificación y consumo de APIs, mantenimiento personal de cuatro microservicios Node.js heredados, coordinación recurrente de despliegues fuera de horario, colas MQ, certificados, vulnerabilidades, diagnóstico de incidentes y soporte entre equipos. |
| systems | Microservicios de pagos, principalmente Java y Spring y algunos Node.js; APIs mayoritariamente REST y algunas SOAP; transferencias entrantes y salientes, pagos desde cuenta, pagos recurrentes e inmediatos, SEPA y transferencias transfronterizas. |
| projects | [`project:deutsche-bank-payments-systems`] |
| stories | [] |
| technologies | [`technology:ibm-mq`, `technology:java`, `technology:kubernetes`, `technology:node-js`, `technology:openshift`, `technology:spring`, `technology:spring-boot`] |
| skills | [`skill:api-design-and-integration`, `skill:backend-development`, `skill:critical-systems-operation`, `skill:microservices`, `skill:production-support-and-debugging`] |
| achievements | [`achievement:deutsche-bank-direct-hire-after-consulting`] |
| evidence | `knowledge/raw/interviews/2026-07-cto-adjunto-fast-track.md`; `knowledge/raw/interviews/2026-08-29-post-smadex-knowledge-verification.md` |
| uncertainty | No constan día exacto de contratación, ubicación, título contractual literal, nombres de sistemas, métricas de tráfico ni delimitación temporal de cada responsabilidad. No se afirma que el usuario sea CTO ni Tech Lead. |
| related_entities | [`company:deutsche-bank`] |

## Contexto

Deutsche Bank contrató directamente al usuario en septiembre de 2024 después de su etapa como consultor externo mediante CGI. Las responsabilidades siguieron siendo ampliamente similares después de la transición. El usuario continúa en Deutsche Bank según la fuente actualizada en julio de 2026.

El equipo de pagos es pequeño, experimentado, autónomo y con capacidad de autoorganización. Las tareas no siempre están muy detalladas en Jira y el equipo coordina internamente el trabajo mediante comunicación frecuente. El usuario se describe como la persona con menos experiencia del equipo.

## Responsabilidades

El inicio habitual del día incluye revisar sitios internos de datos o análisis, vulnerabilidades, incidentes, avance de pasos de despliegue y correo, además de participar en reuniones diarias. Según las necesidades, el trabajo abarca desarrollo, gestión de despliegues en producción, gestión de colas MQ, certificados, vulnerabilidades, investigación de errores y soporte a otros equipos.

Algunas semanas tienen poco o ningún desarrollo de código porque las tareas operativas y de coordinación tienen prioridad. Cuando otros equipos informan de errores de comunicación con sistemas mantenidos por el equipo, el usuario participa en su investigación y soporte. Los problemas graves requieren resolución rápida y pueden generar presión fuera del horario habitual.

## Sistemas y ámbito de trabajo

El equipo mantiene microservicios, principalmente en Java y Spring. Desde aproximadamente principios de 2025, el usuario tiene responsabilidad profesional personal sobre el mantenimiento de cuatro microservicios Node.js heredados de otro equipo, ya implementados y en funcionamiento. Aplicó ingeniería inversa para entenderlos y ha realizado pequeños cambios de código; el mantenimiento posterior existe, pero hasta ahora ha requerido una carga limitada. Java continúa siendo su tecnología backend principal.

La mayoría de las APIs son REST y algunas SOAP. Manuel crea o modifica y consume APIs, aunque los servicios del equipo son consumidos por otros sistemas con mayor frecuencia. Participa en el diseño de contratos internos y se adapta a contratos impuestos por partes externas cuando corresponde. Escribe y modifica OpenAPI, utilizado como documentación y cada vez más para generación de código; en SOAP modifica contratos y trabaja con clientes generados mediante WSDL.

La plataforma de destino es OpenShift. Manuel trabaja con pods, logs, reinicios o borrado, deployments, escalado de réplicas, Services, ConfigMaps, Secrets y troubleshooting. Edita plantillas predefinidas utilizadas por Helm para desplegar en distintos entornos y trabaja con OpenShift Routes. Esto no implica administración de clústeres o plataforma, instalación o upgrades, ownership de infraestructura, experiencia con Ingress ni acceso productivo irrestricto.

El dominio incluye transferencias entrantes y salientes, pagos desde cuentas bancarias distintos de tarjetas, pagos recurrentes, pagos inmediatos, transferencias SEPA y transferencias transfronterizas.

Algunos servicios tienen tráfico muy alto y otros presentan menor actividad. Existen dos entornos de pruebas y dos de producción: producción normal y producción para recuperación ante desastres. La criticidad deriva del impacto empresarial que puede tener un fallo en los sistemas de pagos.

## Operación fuera de horario e incidentes

El usuario participa regularmente en trabajo fuera del horario normal: algunos meses incluyen varios días y es inusual que no haya ninguno. La causa más frecuente son cambios o despliegues en producción, no una guardia clásica de pager. Se programan en periodos de menor tráfico determinados con monitorización como New Relic y Splunk, a menudo alrededor de medianoche. El equipo prepara, organiza y controla el despliegue y entrega las instrucciones técnicas; por separación de permisos, otro equipo autorizado ejecuta los comandos restringidos en producción.

Cuando aparece un incidente, el usuario y su equipo investigan y resuelven lo que pertenece a sus sistemas. Si la evidencia apunta a otro sistema, enrutan o escalan el caso y colaboran en el diagnóstico con el equipo correspondiente, incluidas interacciones con aplicaciones móviles o sistemas mainframe. Los incidentes críticos pueden activar escalado telefónico fuera de horario, aunque el usuario no ha recibido personalmente una llamada crítica. Los incidentes no críticos también pueden detectarse a primera hora y provocar la repriorización del trabajo planificado.

## Entorno arquitectónico

La experiencia expuso al usuario a arquitectura en una organización más grande, internacional y especializada que Mercury TFS, con equipos específicos de arquitectura y desarrollo de soluciones. La fuente señala que el impacto de un fallo en producción es mayor que en roles anteriores, sin aportar métricas concretas.

## Relaciones

Las tecnologías respaldadas se enlazan en los campos canónicos. Todavía no existen entidades específicas para los sistemas internos ni para las historias operativas de este rol.

## Entidades candidatas pendientes

- Historia candidata: investigación y resolución de un incidente grave en producción.
- Historia candidata: soporte ante errores de comunicación reportados por otros equipos.
- Sistema candidato: producción para recuperación ante desastres.

## Incertidumbre

La fuente no distingue con precisión qué responsabilidades comenzaron durante la consultoría y cuáles aparecieron después de la contratación directa. Se registran aquí porque forman parte del rol vigente, pero no se atribuye una fecha individual a cada una.

El usuario se considera más próximo a un posible recorrido de Tech Lead que a CTO; no ocupa ninguno de esos cargos según la evidencia disponible.

## Evidencia

- `knowledge/raw/interviews/2026-07-cto-adjunto-fast-track.md`, sección “Current Experience: Deutsche Bank”.
- `knowledge/raw/interviews/2026-08-29-post-smadex-knowledge-verification.md`.
