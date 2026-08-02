# Selección de perfil objetivo: knowmad mood — Senior Backend Java

## Recomendación

- **primary_target_profile:** `target-profile:backend-senior`
- **qualitative_fit:** moderado
- **recommendation:** aplicar tras aclarar
- **reasons:**
  - El núcleo del puesto coincide fuertemente con Java, Spring Boot, microservicios, APIs, sistemas distribuidos y desarrollo hands-on.
  - La experiencia reciente en pagos y la trayectoria en Mercury aportan contexto de sistemas complejos, producción y evolución backend.
  - El encaje global baja de fuerte a moderado porque diseñar una arquitectura escalable desde cero es central y la evidencia solo demuestra pensamiento arquitectónico moderado, no ownership formal equivalente.
  - Mensajería está respaldada mediante IBM MQ, pero Kafka específico no.
  - Liderazgo técnico es una transición plausible basada en conductas observadas, no en un título formal.
  - IA en el ciclo de desarrollo, SDD y varias prácticas nombradas no tienen evidencia profesional específica.

## Perfiles secundarios posibles

| Perfil objetivo existente | Encaje | Aporte específico | Riesgo de mezclarlo |
|---|---|---|---|
| `target-profile:backend-tech-lead` | Moderado | Revisión de código, apoyo a compañeros, estimación, referencia funcional y liderazgo hands-on. | Puede sugerir un título formal de Tech Lead o autoridad de personas que no están demostrados. |
| `target-profile:solutions-architect` | Débil a moderado | Análisis de requisitos, descomposición, integración y pensamiento arquitectónico. | Es un perfil aspiracional; puede inflar la responsabilidad sobre arquitectura desde cero y escalabilidad. |

## Perfiles descartados

| Perfil objetivo existente | Motivo del descarte | Señal decisiva |
|---|---|---|
| `target-profile:ai-backend-engineer` | La IA es una responsabilidad complementaria y no el núcleo técnico de la oferta. | Java/Spring Boot y arquitectura backend dominan; no se solicita construir modelos o productos de IA. |
| `target-profile:automation-process-engineer` | Automatización de procesos no es la familia principal del puesto. | El foco es producto backend de nueva creación. |
| `target-profile:research-software-engineer` | No existe contexto de investigación, cultura o software científico. | Proyecto corporativo de People/retail. |
| `target-profile:technical-lead-small-company` | La oferta describe una compañía grande y un proyecto para una gran multinacional, no un rol técnico híbrido de empresa pequeña. | Más de 3.000 personas y cliente multinacional; no aparecen operaciones internas generalistas. |

## Señales de encaje

- **strongest_fit_signals:**
  - Senior Backend Java ↔ `target-profile:backend-senior` ↔ `role:deutsche-bank-senior-backend-software-engineer`, `technology:java`, `skill:backend-development`.
  - Spring Boot y microservicios ↔ núcleo del perfil ↔ `technology:spring-boot`, `technology:spring`, `skill:microservices`.
  - Sistemas distribuidos y mensajería ↔ pagos críticos ↔ `project:deutsche-bank-payments-systems`, `technology:ibm-mq`.
  - APIs ↔ diseño e integración ↔ `skill:api-design-and-integration`, con límites explícitos sobre API First y gobierno.
  - Liderazgo hands-on ↔ transición Tech Lead ↔ `skill:technical-leadership-without-title`, `skill:code-review-and-mentoring`, `achievement:mercury-functional-reference-areas`.
- **weakest_fit_signals:**
  - Arquitectura escalable desde cero ↔ solo apoyo parcial de `skill:software-architecture`; no consta responsabilidad formal de diseño global ni métricas de escala.
  - Kafka ↔ no existe entidad ni uso profesional canónico; IBM MQ solo cubre mensajería general.
  - SOLID, Clean Code, DDD, testing técnico y SDD ↔ no existen evidencias canónicas específicas que permitan afirmarlos como experiencia demostrada.
  - IA en el ciclo de desarrollo ↔ DEOS muestra un proyecto personal relacionado con IA, pero no uso profesional de IA dentro de un SDLC.

## Riesgos específicos del perfil

- Presentar el buen encaje backend como prueba automática de arquitectura desde cero.
- Confundir IBM MQ con Kafka en lugar de describir experiencia transferible en mensajería.
- Transformar liderazgo sin título en Tech Lead formal.
- Usar DEOS para afirmar experiencia profesional de IA o madurez no documentada.
- Enumerar DDD, SOLID, Clean Code, testing o API First solo porque aparecen en la oferta.

## Incertidumbre

- Una aclaración que sitúe la arquitectura como trabajo compartido y acepte mensajería no Kafka elevaría el encaje.
- Una exigencia de ownership arquitectónico individual probado, Kafka productivo, DDD profundo o liderazgo formal reduciría el encaje.
- No se conoce el peso evaluativo de IA y SDD ni si se espera experiencia previa o capacidad de adopción.

No forzar el perfil secundario de Tech Lead o arquitectura en las salidas; el ancla factual debe seguir siendo Backend Senior.
