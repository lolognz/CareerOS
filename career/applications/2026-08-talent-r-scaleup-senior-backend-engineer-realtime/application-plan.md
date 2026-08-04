# Plan de candidatura: Talent-R / scale-up no identificada — Senior Backend Engineer

## Decisión

- **recommendation:** aplicar de forma selectiva
- **rationale:** El encaje con backend sénior Java y producción es fuerte. El recruiter validó la mentalidad y hábitos “360”, aceptó los gaps DevOps como no bloqueantes, solicitó CV/email y propuso entrevista. Procede enviar un CV conservador mientras Linux, cloud, terminal y autonomía DevOps quedan abiertos para entrevista.
- **primary_target_profile:** `target-profile:backend-senior`
- **time_priority:** alta; preparar CV para enviarlo cuanto antes y cerrar entrevista para mañana por la tarde si es posible.

## Estrategia de CV

- Objetivo: demostrar profundidad profesional en Java/Spring y responsabilidad práctica sobre servicios críticos desde desarrollo hasta producción.
- Orden de evidencia: Deutsche Bank actual; etapa CGI y migración; Mercury TFS como profundidad previa y liderazgo técnico acotado.
- Elementos obligatorios: `role:deutsche-bank-senior-backend-software-engineer`, `project:deutsche-bank-payments-systems`, `technology:java`, `technology:spring`, `skill:critical-systems-operation`, `skill:production-support-and-debugging`.
- Elementos a reducir u omitir: investigación, proyectos personales, negocio familiar y tecnologías no relacionadas; Docker/Kubernetes salvo que la call confirme relevancia.
- Límites de redacción: no usar 4,5M req/s, sub-100ms, real-time, performance engineering, disponibilidad o low latency como experiencia propia; no afirmar DevOps/SRE, cloud, Linux o servidores profundos, autonomía de terminal en producción, ownership total, título Tech Lead ni people management.
- Autorización: CV Generator v1 puede generar ahora `generated/cv.md` como borrador conservador para revisión antes del envío. Esta actualización no debe generarlo.
- Referencia de estilo: el CV de CTO adjunto puede consultarse posteriormente solo para estilo y estructura, nunca como evidencia o fuente factual.

## Estrategia de carta de presentación

- Tesis: no preparar carta salvo que el proceso la solicite; si se autoriza después, conectar backend crítico y operación con la responsabilidad end-to-end descrita.
- Evidencia principal: `project:deutsche-bank-payments-systems`, `story:mercury-integration-base`.
- Motivación respaldada: interés por conocer un reto backend Java con producción y crecimiento técnico; no atribuir motivación hacia una empresa o producto aún desconocidos.
- Caveats que deben tratarse: empresa no identificada, escala no comparable y alcance de infraestructura pendiente.

## Estrategia de mensaje a recruiter

- Objetivo: acompañar el envío del CV y confirmar entrevista mañana por la tarde; la aceptación exploratoria ya ocurrió.
- Señales prioritarias: Java/Spring profesional, backend sénior, microservicios de pagos críticos y responsabilidades de producción/soporte.
- Pregunta o caveat principal: confirmar hora de entrevista; reservar identidad/producto y alcance DevOps/Linux/cloud para la conversación.
- No redactar todavía el mensaje final.

## Estrategia de LinkedIn

- **usefulness:** no útil
- Ajuste recomendado: ninguno; el perfil Backend Senior ya es una identidad durable y no necesita adaptarse a una empresa desconocida.
- Restricción: no convertir una oferta concreta en identidad profesional no demostrada.

## Prioridades de entrevista

- Temas técnicos: Java/Spring, arquitectura de microservicios dentro de lo conocido, despliegues, MQ, certificados, vulnerabilidades, diagnóstico y soporte; preguntar por testing, observabilidad y low latency antes de preparar detalle específico.
- Historias canónicas a preparar: `story:mercury-integration-base`, `story:deutsche-bank-transfer-to-payments-team`.
- Límites que verbalizar: ausencia de métricas comparables; IBM MQ, Docker y Kubernetes con sus profundidades reales; liderazgo sin título formal; atribución compartida de IntegrationBase.
- Preguntas previsibles que requieren investigar en la propia oferta o preguntar: decisiones de rendimiento, modelo de concurrencia, SLO/SLI, cuellos de botella, estrategia de testing, incidentes, on-call y responsabilidades de Tech Lead.
- No redactar respuestas terminadas.

## Gaps a abordar

| Gap | Impacto | Acción honesta antes de generar | Bloquea candidatura |
|---|---|---|---|
| 4,5M req/s y sub-100ms | alto | Preguntar perímetro; no establecer equivalencia con pagos. | no |
| Real-time/low-latency medible | alto | Aclarar definición y requisitos; reconocer ausencia de métrica propia. | desconocido |
| DevOps sin equipo dedicado | alto | Presentar experiencia de ciclo completo y declarar que siempre hubo equipos DevOps; preparar aprendizaje/transferencia. | no para enviar CV; riesgo de entrevista |
| Linux/cloud/servidores/terminal | alto | Preguntar tareas y permisos exactos; presentar solo exposición parcial y monitorización. | no para enviar CV; riesgo de entrevista |
| Testing propio end-to-end | medio | La conversación respalda testing local habitual; mantener sin detalle técnico inventado. | no |
| Fluidez de español e inglés sin entidad canónica | medio | Confirmar directamente con el usuario antes de afirmarla en outputs. | desconocido |
| Tech Lead formal | bajo | Presentar potencial y conductas sin título; no intentar cerrar el gap mediante redacción. | no |
| Empresa, contrato y moneda | alto | Resolver durante el proceso antes de aceptar una eventual oferta. | no para enviar CV |

## Preguntas para recruiter o empresa

1. ¿Qué empresa y producto hay detrás de la oportunidad, y cuál es su dominio de negocio?
2. ¿Qué miden exactamente los 4,5M requests/second y el sub-100ms: pico o promedio, sistema completo o componente, y qué SLOs se esperan del equipo?
3. ¿Qué significa “real-time” en este producto y qué parte del sistema asumiría el puesto?
4. ¿Cuál es el stack completo y qué profundidad concreta se espera en servidores, Linux, redes, cloud, contenedores y observabilidad?
5. ¿Cómo se reparten desarrollo, testing, despliegues, soporte, incidentes y on-call?
6. ¿Qué tamaño y composición tiene el equipo, y qué comportamientos o hitos definen el crecimiento hacia Tech Lead?
7. ¿Qué tipo de contrato, país de contratación, horario/zona, moneda y composición tiene el rango 60–80K?
8. ¿Cómo se usa y evalúa el inglés en el día a día?

## Outputs recomendados

| Output futuro | Estado | Propósito | Dependencias |
|---|---|---|---|
| CV | recomendado y autorizado | Mostrar ajuste Java/backend/producción mediante borrador conservador para recruiter. | CV Generator v1; revisión humana antes del envío. |
| Carta de presentación | no recomendado | Solo tendría valor si la empresa la solicita. | Identidad, producto y motivación concreta. |
| Mensaje a recruiter | opcional | Acompañar CV y confirmar hora. | CV revisado y disponibilidad concreta. |
| Preparación de entrevista | recomendado | Preparar evidencia técnica y límites. | Descripción completa y respuestas del recruiter. |

## Instrucciones consolidadas de generación

- CV Generator v1 queda autorizado para generar `generated/cv.md` en la siguiente ejecución; no generarlo durante esta actualización.
- Mantener español salvo que una fase posterior pida otro idioma.
- Abrir con Java/Spring, backend sénior y pagos críticos; usar tareas operativas concretas para demostrar amplitud.
- Describir el sistema de la empresa y sus métricas solo como contexto de la oportunidad.
- No afirmar escala, latencia, real-time, performance engineering, testing integral, DevOps/SRE, cloud/Linux/servidores profundos, autonomía operativa en producción, ownership total ni Tech Lead formal.
- Presentar como fortaleza el ciclo de entrega y la responsabilidad de equipo; hacer visibles como gaps parciales la dependencia histórica de equipos DevOps y los permisos limitados en producción.
- Usar el CV de CTO adjunto solo como referencia futura de estilo, no como evidencia.
- Conservar títulos, fechas, atribuciones y fuerza de evidencia canónicas.
