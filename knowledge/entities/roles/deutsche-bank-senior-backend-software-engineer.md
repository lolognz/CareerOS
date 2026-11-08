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
| date_precision | Mes de inicio confirmado; el rol seguía vigente en la actualización de la fuente de noviembre de 2026. |
| location | Desconocida en la evidencia disponible |
| employment_type | Empleo directo |
| seniority | Senior; el usuario se considera la persona con menos experiencia dentro de un equipo pequeño y experimentado. |
| context | Equipo de pagos bancarios crítico, con autonomía y responsabilidad sobre desarrollo, operación y soporte de microservicios. |
| responsibilities | Revisión operativa diaria, desarrollo, creación o modificación y consumo de APIs, mantenimiento personal de cuatro microservicios Node.js heredados, coordinación recurrente de despliegues fuera de horario, colas MQ, certificados, vulnerabilidades, diagnóstico de incidentes y soporte entre equipos. |
| systems | Microservicios de pagos, principalmente Java y Spring y algunos Node.js; APIs mayoritariamente REST y algunas SOAP; transferencias entrantes y salientes, pagos desde cuenta, pagos recurrentes e inmediatos, SEPA y transferencias transfronterizas. |
| projects | [`project:deutsche-bank-payments-systems`] |
| stories | [] |
| technologies | [`technology:ibm-mq`, `technology:java`, `technology:kubernetes`, `technology:node-js`, `technology:openshift`, `technology:spring`, `technology:spring-boot`] |
| skills | [`skill:api-design-and-integration`, `skill:backend-development`, `skill:code-review-and-mentoring`, `skill:stakeholder-communication`, `skill:technical-leadership-without-title`, `skill:critical-systems-operation`, `skill:microservices`, `skill:production-support-and-debugging`] |
| achievements | [`achievement:deutsche-bank-direct-hire-after-consulting`] |
| evidence | `knowledge/raw/interviews/2026-07-cto-adjunto-fast-track.md`; `knowledge/raw/interviews/2026-08-29-post-smadex-knowledge-verification.md`; `knowledge/raw/interviews/2026-11-08-professional-knowledge-verification.md` |
| uncertainty | No constan día exacto de contratación, ubicación, título contractual literal, nombres de sistemas, métricas de tráfico ni delimitación temporal de cada responsabilidad. No se afirma que el usuario sea CTO ni Tech Lead. |
| related_entities | [`company:deutsche-bank`] |

## Contexto

Deutsche Bank contrató directamente al usuario en septiembre de 2024 después de su etapa como consultor externo mediante CGI. Las responsabilidades siguieron siendo ampliamente similares después de la transición. El usuario continúa en Deutsche Bank según la verificación de noviembre de 2026.

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

## Verificación actual — 2026-11-08

### Equipo, revisión y acompañamiento

El equipo sénior cuenta efectivamente con dos desarrolladores y una tercera persona que actúa más como enlace negocio-técnica. Los perfiles júnior son poco habituales por la criticidad del equipo. Cada PR requiere la aprobación del otro desarrollador: la revisión es recíproca entre pares, sin autoridad jerárquica. El compañero tiene más años de experiencia y es técnicamente fuerte; ambos aprenden del otro. Revisan corrección funcional, errores, código innecesario, dependencias sin uso, mantenibilidad y la opción técnica más sencilla y sostenible.

Durante un periodo anterior con una desarrolladora menos experimentada, Manuel la acompañó en varios desarrollos, explicando cómo abordar las implementaciones y por qué una solución funcionalmente correcta podía ser peor en diseño o mantenibilidad. En un ejemplo reciente explicó a un compañero cada paso para llevar un desarrollo a producción, su propósito y la importancia del orden. Prefiere explicar el porqué frente a instrucciones mecánicas. Esto acredita mentoring y transferencia de conocimiento, no people management ni un título formal de Tech Lead.

### Ejemplo reciente: proxy entre mainframe y API de otro equipo

Partiendo únicamente de la definición Swagger/OpenAPI de la API externa al equipo, Manuel elaboró el documento técnico, diseñó y creó el microservicio, coordinó con mainframe la comunicación y la estructura de mensajes/datos, implementó la solución y sus pruebas, realizó testing y la llevó al entorno de desarrollo. En esta verificación todavía NO ha llegado a producción: depende de otros equipos. No se atribuyen despliegue ni resultados productivos a este caso; no consta la fecha exacta del desarrollo.

### Coordinación de integraciones

Los equipos son organizativamente independientes. Manuel participa regularmente en acordar la comunicación/integración con consumidores de las APIs de su equipo y en diagnosticar fallos reportados por ellos. Según su experiencia, la mayoría de esos fallos se deben a contenido o estructura de datos incorrectos en el consumidor; es una observación suya, no una métrica general. No implica gobierno organizativo de APIs ni ownership de otros equipos.

### Testing y herramientas actuales

Manuel se responsabiliza del testing de las soluciones que desarrolla: pruebas unitarias, de integración, Acceptance Testing (ACT) y end-to-end. Las E2E pueden requerir coordinación con varios equipos. Las herramientas profesionales actuales incluyen JUnit, Mockito, Spring Boot Test, WireMock, SOAPUI, Bruno y Karate; Karate se utiliza para Acceptance Testing. No se asigna a las demás herramientas una modalidad concreta no verificada.

Utiliza TDD ocasionalmente, sin ser habitual ni una preferencia central de posicionamiento. Sonar está presente con relativamente poco énfasis actual y tuvo más importancia en proyectos anteriores. También se usan Waltz y Prisma, descritos por Manuel en el contexto de análisis de vulnerabilidades; no se infiere un alcance de producto adicional.

### Uso profesional de inglés

La documentación, el código, Jira y los correos con participantes no hispanohablantes se realizan mayoritariamente en inglés. Una parte significativa de TDI está en India y Manuel participa regularmente en reuniones profesionales/técnicas en inglés. La comprensión auditiva es su principal dificultad, especialmente con algunos acentos: suele entender el contexto, pero puede perder una palabra clave o pregunta y necesitar repetición. Se acredita uso profesional habitual escrito y oral, sin nivel CEFR ni etiquetas nativo, bilingüe o «fluent» sin restricciones.

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

- `knowledge/raw/interviews/2026-11-08-professional-knowledge-verification.md`.
