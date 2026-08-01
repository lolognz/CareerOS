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
| responsibilities | Revisión operativa diaria, desarrollo, gestión de despliegues, colas MQ, certificados, vulnerabilidades, investigación de errores, soporte a otros equipos y respuesta rápida ante problemas graves. |
| systems | Microservicios de pagos, principalmente Java y Spring y algunos Node.js; transferencias entrantes y salientes, pagos desde cuenta, pagos recurrentes e inmediatos, SEPA y transferencias transfronterizas. |
| projects | [`project:deutsche-bank-payments-systems`] |
| stories | [] |
| technologies | [`technology:ibm-mq`, `technology:java`, `technology:node-js`, `technology:spring`, `technology:spring-boot`] |
| skills | [`skill:backend-development`, `skill:critical-systems-operation`, `skill:microservices`, `skill:production-support-and-debugging`] |
| achievements | [] |
| evidence | `knowledge/raw/interviews/2026-07-cto-adjunto-fast-track.md` |
| uncertainty | No constan día exacto de contratación, ubicación, título contractual literal, nombres de sistemas, métricas de tráfico ni delimitación temporal de cada responsabilidad. No se afirma que el usuario sea CTO ni Tech Lead. |
| related_entities | [`company:deutsche-bank`] |

## Contexto

Deutsche Bank contrató directamente al usuario en septiembre de 2024 después de su etapa como consultor externo mediante CGI. Las responsabilidades siguieron siendo ampliamente similares después de la transición. El usuario continúa en Deutsche Bank según la fuente actualizada en julio de 2026.

El equipo de pagos es pequeño, experimentado, autónomo y con capacidad de autoorganización. Las tareas no siempre están muy detalladas en Jira y el equipo coordina internamente el trabajo mediante comunicación frecuente. El usuario se describe como la persona con menos experiencia del equipo.

## Responsabilidades

El inicio habitual del día incluye revisar sitios internos de datos o análisis, vulnerabilidades, incidentes, avance de pasos de despliegue y correo, además de participar en reuniones diarias. Según las necesidades, el trabajo abarca desarrollo, gestión de despliegues en producción, gestión de colas MQ, certificados, vulnerabilidades, investigación de errores y soporte a otros equipos.

Algunas semanas tienen poco o ningún desarrollo de código porque las tareas operativas y de coordinación tienen prioridad. Cuando otros equipos informan de errores de comunicación con sistemas mantenidos por el equipo, el usuario participa en su investigación y soporte. Los problemas graves requieren resolución rápida y pueden generar presión fuera del horario habitual.

## Sistemas y ámbito de trabajo

El equipo mantiene microservicios, principalmente en Java y Spring, además de algunos servicios Node.js. El dominio incluye transferencias entrantes y salientes, pagos desde cuentas bancarias distintos de tarjetas, pagos recurrentes, pagos inmediatos, transferencias SEPA y transferencias transfronterizas.

Algunos servicios tienen tráfico muy alto y otros presentan menor actividad. Existen dos entornos de pruebas y dos de producción: producción normal y producción para recuperación ante desastres. La criticidad deriva del impacto empresarial que puede tener un fallo en los sistemas de pagos.

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
