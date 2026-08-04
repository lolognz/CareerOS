# Registro de riesgos: Talent-R / scale-up no identificada — Senior Backend Engineer

## Escala

- Probabilidad: alta / media / baja / desconocida.
- Impacto: alto / medio / bajo.
- Estado: abierto / pendiente de aclaración / mitigado / aceptado.

## Riesgos de sobreafirmación

| Riesgo | Evidencia o límite afectado | Probabilidad | Impacto | Mitigación | Estado |
|---|---|---|---|---|---|
| Atribuirse 4,5M req/s o sub-100ms | `project:deutsche-bank-payments-systems` no contiene métricas | alta | alto | Tratar las cifras solo como contexto de la empresa y declarar que no existe métrica propia comparable. | mitigado |
| Convertir criticidad bancaria en experiencia real-time/low-latency | `skill:critical-systems-operation` | alta | alto | Hablar de criticidad, producción y tipos de flujo; no extrapolar arquitectura ni latencia. | mitigado |
| Afirmar administración profunda de servidores o SRE | `technology:docker`, `technology:kubernetes`, `technology:ibm-mq` | alta | alto | Describir tareas concretas y conservar los límites de cada tecnología. | mitigado |
| Afirmar ownership total de pagos o producción | Rol y proyecto de Deutsche Bank | media | alto | Usar “dentro del equipo” y delimitar desarrollo, despliegues, colas, certificados, vulnerabilidades y soporte. | mitigado |
| Presentarse como Tech Lead formal | `skill:technical-leadership-without-title`, `achievement:mercury-functional-reference-areas` | alta | alto | Conservar títulos formales y presentar conductas/potencial de evolución. | mitigado |
| Generalizar testing propio end-to-end | Evidencia operativa parcial | media | medio | No afirmarlo como práctica general; preguntar por expectativas y usar solo ejemplos verificables. | abierto |
| Convertir exposición DevOps/cloud/Linux en profundidad | Conversación del recruiter y `technology:docker`, `technology:kubernetes`, `technology:ci-cd` | alta | alto | Indicar que DevOps no era el rol principal, siempre hubo equipos dedicados y no había permisos de comandos en producción. | mitigado |
| Tratar la validación del recruiter como aprobación técnica | Conversación de candidatura | media | alto | Registrar que solo permite avanzar; el cliente debe evaluar los gaps. | mitigado |
| Sobreatribuir IntegrationBase | `story:mercury-integration-base` | media | medio | Indicar siempre colaboración con un compañero y alcance concreto. | mitigado |

## Áreas de evidencia débil

| Área | Fuerza disponible | Qué no demuestra | Mitigación |
|---|---|---|---|
| Escala y latencia | Sistemas de pagos críticos; algunos servicios con tráfico alto sin cifras. | 4,5M req/s, sub-100ms, SLOs o tuning de baja latencia. | Mantener como gap y preguntar por definición/perímetro. |
| Servidores e infraestructura | Despliegues, MQ, certificados, vulnerabilidades; Docker/Kubernetes limitados; exposición declarada a Azure/GCP/Linux. | Sysadmin, Linux/redes/cloud profundos, instancias, balanceadores, clústeres o plataforma. | Enumerar tareas canónicas; tratar lo conversacional como contexto y no como claim de CV. |
| Terminal y permisos en producción | Monitorización y responsabilidad de equipo; cambios canalizados mediante DevOps. | Autonomía para reiniciar servicios, cambiar recursos o administrar servidores en producción. | Declararlo directamente en entrevista; no ocultarlo ni presentarlo como bloqueo del envío. |
| Testing | Testing local habitual declarado y entornos de test documentados. | Ownership completo de estrategia, automatización o pirámide de tests. | Mantenerlo como hábito sin inventar herramientas ni cobertura. |
| Liderazgo | Revisión, apoyo, estimación y referencia funcional. | Tech Lead formal, people management o autoridad organizativa. | Posicionarlo como capacidad y siguiente paso. |
| Idiomas | Contextos internacionales y comunicación, sin entidad lingüística. | Fluidez actual evaluada en español e inglés. | Confirmación directa antes de cualquier claim. |

## Requisitos ausentes

| Requisito de la oferta | Estado | Impacto en el encaje | Mitigación honesta |
|---|---|---|---|
| 4–5+ años; idealmente 6 | respaldado | positivo | Java profesional desde 2020 y backend anterior; no recalcular más precisión de la documentada. |
| Seniority sólido | respaldado | positivo | Usar roles formales y alcance; conservar que es la persona con menos experiencia del equipo actual. |
| Java muy fuerte | respaldado | positivo | `technology:java` tiene evidencia fuerte y sostenida. |
| Español fluido | desconocido | medio | Confirmar con el usuario; no inferir por idioma del repositorio. |
| Inglés fluido | desconocido | alto | Confirmar nivel y uso actual; no inferir fluidez solo por Harvard o contextos internacionales. |
| Perfil 360 / más allá del IDE | respaldado con límites | positivo | El recruiter valida mentalidad y hábitos; preservar dependencia de equipos DevOps y permisos limitados. |
| DevOps práctico sin equipo dedicado | parcial | alto | Preparar ejemplos transferibles y reconocer que DevOps nunca fue el rol principal. |
| Linux, cloud, instancias y balanceos | parcial | alto | No afirmar administración; aclarar tareas mínimas exigidas por el cliente. |
| Debugging en terminal en producción | parcial | alto | Diferenciar monitorización/debug de ejecución de comandos operativos, para los que no había permisos. |
| Testing propio | parcial | medio | Usar la declaración de testing local habitual sin inventar estrategia o herramientas. |
| Calidad y ownership en producción | respaldado | positivo | Apoyar en operación de pagos, siempre como responsabilidad dentro del equipo. |
| Sistema real-time, high-scale y low-latency | no respaldado como experiencia equivalente | alto | Reconocer transferencia desde sistemas críticos, no equivalencia. |
| Soft skills fuertes | parcial | medio | Usar `skill:stakeholder-communication` y ejemplos concretos; criterio final subjetivo. |
| Compromiso real con el proyecto | desconocido | medio | No convertir motivación futura en hecho; evaluar producto y expectativas primero. |
| Potencial hacia Tech Lead | parcial | positivo | Usar liderazgo sin título y referencia funcional; sin título formal. |

## Expectativas del puesto poco claras

| Incertidumbre | Interpretaciones posibles | Riesgo | Pregunta necesaria |
|---|---|---|---|
| DevOps propio sin equipo dedicado | Operación acotada del servicio o responsabilidad amplia de plataforma. | Desajuste si exige autonomía infra inmediata. | ¿Qué tareas, permisos y frecuencia se esperan exactamente? |
| Linux/terminal/cloud | Debug aplicativo, comandos operativos, instancias, balanceos o administración. | El candidato tiene experiencia parcial, no profundidad. | ¿Qué comandos, herramientas y conocimientos son imprescindibles desde el primer día? |
| Real-time y métricas | Evento crítico, streaming, publicidad, gaming u otro dominio; pico o agregado. | Preparación errónea y comparación inválida. | ¿Cuál es el dominio, arquitectura y perímetro de las métricas? |
| Producción | Ownership de servicio, on-call, incident response o responsabilidad compartida. | Disponibilidad no anticipada. | ¿Hay guardias y cómo se reparte el soporte? |
| Testing/calidad | Unit, integración, performance, contract, chaos o validación manual. | Gap técnico oculto. | ¿Qué estrategia y herramientas usa el equipo? |
| Tech Lead | Crecimiento técnico, coordinación, people management o sucesión próxima. | Inflar el perfil o aceptar alcance distinto. | ¿Qué responsabilidades y criterios definen la evolución? |

## Ubicación, contrato y compensación

| Riesgo | Dato disponible | Dato faltante | Mitigación |
|---|---|---|---|
| Remoto con restricciones ocultas | “Full remote”. | País, residencia, zona horaria, viajes y equipo proporcionado. | Aclarar antes de avanzar a fase final. |
| Contrato desconocido | Ninguno. | Empleador legal, indefinido/B2B, periodo de prueba y beneficios. | Preguntar en la primera call. |
| Rango incompleto | “60–80K budget”. | Moneda, bruto/neto, anualidad, fijo/variable y criterio de nivel. | No asumir euros brutos anuales; pedir desglose. |

## Red flags

- Empresa final no identificada: limita due diligence y motivación informada.
- “360”, “committed” e “invested” sin límites: posible amplitud de rol o disponibilidad no declarada.
- Métricas llamativas sin definición: riesgo de marketing o de expectativas técnicas mal entendidas.
- Urgencia por vacaciones: no es un bloqueo, pero tampoco justifica omitir aclaraciones esenciales.
- Ausencia de equipo DevOps dedicado: riesgo real de amplitud operativa, aunque el recruiter ha aceptado avanzar con los gaps declarados.

## Recomendación consolidada

- Riesgos bloqueantes: ninguno para generar y enviar un CV conservador o realizar la entrevista.
- Riesgos aceptables: gaps de DevOps/cloud/Linux/terminal, escala/latencia y liderazgo formal, ya transparentados al recruiter y pendientes de validación técnica.
- Condiciones para continuar: no ocultar que siempre hubo equipos DevOps ni la falta de permisos operativos en producción; aclarar tareas, on-call, empresa, métricas, contrato y compensación durante el proceso.
- Recomendación: aplicar de forma selectiva; CV autorizado ahora.
