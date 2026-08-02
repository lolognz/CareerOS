# Plan de candidatura: knowmad mood — Senior Backend Java

## Decisión

- **recommendation:** aplicar tras aclarar
- **rationale:** El núcleo Java/Spring Boot/microservicios tiene respaldo fuerte y reciente. La candidatura es razonable, pero la arquitectura desde cero es central y solo está parcialmente respaldada; conviene confirmar también si IBM MQ satisface mensajería y qué experiencia esperan en liderazgo, IA y SDD.
- **primary_target_profile:** `target-profile:backend-senior`
- **time_priority:** Alta si la vacante sigue abierta; contactar pronto para resolver los puntos que pueden cambiar el encaje antes de invertir en outputs extensos.

## Estrategia de CV

- Objetivo: demostrar seniority backend Java, trabajo sostenido con Spring/microservicios, experiencia en sistemas distribuidos y mensajería, y capacidad técnica transversal sin fingir un rol arquitecto o Tech Lead previo.
- Orden de evidencia: Deutsche Bank y pagos críticos; CGI y migración Java/Spring; Mercury y plataforma compleja; habilidades de liderazgo/arquitectura como apoyo, no como título.
- Elementos obligatorios: `role:deutsche-bank-senior-backend-software-engineer`, `project:deutsche-bank-payments-systems`, `technology:java`, `technology:spring-boot`, `skill:microservices`, `technology:ibm-mq`, `achievement:mercury-functional-reference-areas`.
- Elementos a reducir u omitir: investigación, Unity3D, negocio familiar, facturas, PulseCore y DEOS salvo que una conversación confirme que IA aplicada pesa más de lo aparente.
- Límites de redacción: nombrar IBM MQ, no Kafka; liderazgo sin título; arquitectura como pensamiento y contribución, no ownership formal desde cero; no listar DDD, SOLID, Clean Code, testing o SDD como experiencia demostrada.

## Estrategia de carta de presentación

- Tesis: experiencia backend sénior en sistemas bancarios complejos y distribuidos, con evolución hacia mayor responsabilidad técnica hands-on.
- Evidencia principal: `project:deutsche-bank-payments-systems`, `skill:microservices`, `technology:ibm-mq`, `story:mercury-integration-base`, `achievement:mercury-functional-reference-areas`.
- Motivación respaldada: interés potencial por un producto nuevo, autonomía y combinación de diseño/desarrollo; tratarlo como ajuste a la oferta, no como hecho personal ya documentado.
- Caveats que deben tratarse: no hay Kafka probado; arquitectura desde cero y liderazgo formal no son experiencia equivalente; IA profesional en SDLC no está respaldada.

## Estrategia de mensaje a recruiter

- Objetivo: confirmar rápidamente los requisitos que deciden el encaje antes de generar una candidatura completa.
- Señales prioritarias: Senior Backend Java; Spring Boot; microservicios; IBM MQ; sistemas críticos; APIs; liderazgo técnico hands-on.
- Pregunta o caveat principal: confirmar si aceptan experiencia sólida en otra mensajería, si la arquitectura será compartida y qué esperan exactamente respecto a IA y SDD.
- No redactar todavía el mensaje final.

## Estrategia de LinkedIn

- **usefulness:** no útil para una modificación específica de esta candidatura.
- Ajuste recomendado: ninguno; el posicionamiento durable adecuado sigue siendo Backend Senior.
- Restricción: no adoptar títulos de Tech Lead, arquitecto o AI Engineer para reflejar requisitos de esta oferta.

## Prioridades de entrevista

- Temas técnicos: microservicios y límites funcionales; mensajería con IBM MQ; APIs e integración; mantenimiento de sistemas distribuidos; decisiones y trade-offs arquitectónicos dentro del alcance conocido; calidad y testing solo con ejemplos reales que puedan documentarse antes.
- Historias canónicas a preparar: [`story:mercury-integration-base`, `story:deutsche-bank-transfer-to-payments-team`, `story:mercury-account-fields`]
- Límites que verbalizar: ausencia de Kafka profesional; ausencia de título Tech Lead/arquitecto; arquitectura global desde cero no demostrada; IA profesional en SDLC no demostrada; sin métricas de escala.
- Preguntas previsibles que requieren investigar en la propia oferta o preguntar: enfoque API First; patrones DDD; estrategia de testing; definición de SDD; uso permitido/esperado de IA; arquitectura objetivo; cloud y observabilidad.
- No redactar respuestas terminadas.

## Gaps a abordar

| Gap | Impacto | Acción honesta antes de generar | Bloquea candidatura |
|---|---|---|---|
| Kafka específico | Medio | Confirmar si IBM MQ u otra mensajería es suficiente; estudiar conceptos de Kafka sin presentarlos como experiencia. | No, si “o sistemas de mensajería” es literal. |
| Arquitectura escalable desde cero | Alto | Aclarar ownership, apoyo y criterios de escala; usar solo ejemplos arquitectónicos parciales. | Desconocido. |
| API First | Medio | Confirmar profundidad esperada; diferenciar integración/diseño de gobierno API First. | No conocido. |
| SOLID, Clean Code y DDD explícitos | Medio | Obtener evidencia canónica adicional si existe; mientras tanto, no listarlos como claims. | No conocido. |
| Testing técnico | Medio | Aclarar tipos, herramientas y responsabilidad; no sustituirlo por user testing. | No conocido. |
| SDD | Medio | Preguntar qué definición y proceso utiliza el equipo. | No conocido. |
| IA en ciclo de desarrollo | Medio | Confirmar si esperan uso de herramientas, gobernanza o construcción técnica; reconocer que DEOS no es experiencia profesional de SDLC. | No conocido. |
| Idioma de trabajo | Medio | Confirmar nivel y frecuencia de inglés en el proyecto internacional. | Desconocido. |
| Rango salarial y remoto geográfico | Alto para decisión personal | Solicitar rango, ubicación contractual y países admitidos. | Desconocido. |

## Preguntas para recruiter o empresa

1. ¿La arquitectura backend se definirá de forma compartida con arquitectura/equipo o recaerá como ownership principal en esta persona?
2. ¿La experiencia con IBM MQ u otros sistemas de mensajería cubre el requisito, o Kafka productivo es imprescindible?
3. ¿Qué significa en este proyecto “impulsar el uso de IA en el ciclo de vida”: uso de asistentes, automatización, definición de prácticas o desarrollo de componentes de IA?
4. ¿Qué definición y herramientas utiliza el equipo para Spec Driven Development?
5. ¿Qué nivel de liderazgo esperan: influencia técnica, coordinación, mentoring, decisiones finales o gestión de personas?
6. ¿Cuál es el stack completo, incluido cloud, datos, observabilidad, testing y CI/CD?
7. ¿Qué idioma se usa en el día a día y cómo está compuesto el equipo internacional?
8. ¿Desde qué países se permite el remoto, quién es el empleador contractual y cuál es el rango salarial?

## Outputs recomendados

| Output futuro | Estado | Propósito | Dependencias |
|---|---|---|---|
| CV | Recomendado tras aclarar | Mostrar el encaje backend fuerte con límites honestos. | Confirmar alcance arquitectónico y Kafka/mensajería. |
| Carta de presentación | Opcional | Explicar transición hacia mayor diseño y liderazgo hands-on. | Confirmar que el canal la admite y qué aspecto diferencial prioriza. |
| Mensaje a recruiter | Recomendado | Resolver rápidamente los puntos decisivos. | Ninguna generación extensa previa. |
| Preparación de entrevista | Recomendado si avanza | Preparar arquitectura, APIs, mensajería y liderazgo con evidencia. | Respuestas del recruiter y detalles técnicos. |

## Instrucciones consolidadas de generación

- Mantener `target-profile:backend-senior` como posicionamiento principal.
- Priorizar Java, Spring/Spring Boot, microservicios, pagos, sistemas distribuidos y mensajería IBM MQ.
- Presentar liderazgo y arquitectura como capacidades demostradas parcialmente, nunca como títulos formales o ownership global.
- No afirmar Kafka, API First, DDD, SOLID, Clean Code, testing técnico, SDD ni IA profesional en SDLC sin nueva evidencia canónica.
- No usar DEOS para transformar interés/proyecto personal en experiencia profesional de AI Engineering.
- Conservar atribución compartida y ausencia de métricas en IntegrationBase y otros logros.
