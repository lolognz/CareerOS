# Job Intake: Talent-R / scale-up no identificada — Senior Backend Engineer

## Identificación

- **id:** `job-intake:2026-08-talent-r-scaleup-senior-backend-engineer-realtime`
- **application_id:** `application:2026-08-talent-r-scaleup-senior-backend-engineer-realtime`
- **source_job_description:** `career/applications/2026-08-talent-r-scaleup-senior-backend-engineer-realtime/job-description.md`
- **company_name:** Talent-R / scale-up no identificada. Talent-R actúa como intermediaria; la empresa final no se identifica.
- **role_title:** Senior Backend Engineer.
- **detected_role_family:** Backend sénior Java; inferido del título y del requisito de dominio fuerte de Java.
- **seniority_level:** Senior explícito; se solicitan 4–5+ años, idealmente 6, y “solid seniority”.
- **location_model:** Full remote; no constan país de contratación, residencia exigida, zona horaria ni viajes.
- **contract_model:** Desconocido.

## Requisitos extraídos

### Responsabilidades principales

- **core_responsibilities:**
  - Desarrollar backend Java para un sistema real-time de alto rendimiento; explícito por título, stack y contexto, aunque no se detallan componentes.
  - Probar el propio código y responsabilizarse de su calidad una vez en producción; explícito.
  - Completar el ciclo código → pruebas locales → review → CI/CD → staging → producción → monitorización/debug en servidor; aclaración explícita del recruiter.
  - Realizar DevOps práctico alrededor del propio trabajo porque el cliente no tiene un equipo DevOps dedicado; explícito, con profundidad todavía no delimitada.
  - Observar el código en ejecución y depurar desde terminal cuando sea necesario; explícito.
  - Asumir ownership operativo del software en producción; explícito.
  - Crecer potencialmente hacia Tech Lead; expectativa futura, no responsabilidad formal inicial confirmada.

### Requisitos obligatorios

- **must_have_requirements:**
  - 4–5+ años de experiencia, idealmente 6; el mínimo se formula como búsqueda directa y los 6 años como preferencia.
  - Seniority sólido; explícito.
  - Español e inglés fluidos; explícito.
  - Java muy fuerte; explícito.
  - Perfil “360” que cubra el ciclo completo hasta monitorización y debugging en servidor; aclarado explícitamente por el recruiter.
  - Experiencia práctica con cloud —AWS, GCP o Azure—, instancias y balanceos; expresado por el recruiter como parte del perfil buscado, aunque “ya está todo montado”.
  - Linux y capacidad de debugging en terminal; explícito.
  - Capacidad de probar el propio código y mantener su calidad en producción; explícito.
  - Soft skills fuertes, compromiso real e implicación en el proyecto; explícito, aunque subjetivo.

### Requisitos deseables

- **nice_to_have_requirements:**
  - Llegar idealmente a 6 años de experiencia.
  - Potencial para crecer hacia Tech Lead; se presenta como recorrido posible, no como experiencia formal previa exigida.
  - Interés en mantener una call durante la semana del contacto; urgencia de proceso, no requisito de capacidad.

### Contexto técnico y de dominio

- **technologies_detected:** Java, Linux y cloud mediante AWS, GCP o Azure; el recruiter también menciona instancias, balanceos, CI/CD y terminal. Estas menciones describen la oferta y no implican experiencia del candidato.
- **domain_detected:** Sistema técnico real-time, high-scale, high-performance y low-latency de una scale-up no identificada. No consta el dominio de negocio.
- **leadership_expectations:** Potencial de evolución hacia Tech Lead y señales de ownership; no constan people management, autoridad, tamaño de equipo ni título formal de entrada.
- **operational_expectations:** Participación desde pruebas locales y review hasta CI/CD, staging, producción, monitorización y debugging en servidor; Linux; DevOps práctico del propio trabajo al no existir equipo DevOps dedicado. No constan guardias/on-call, permisos exactos, herramientas, proveedor cloud definitivo ni profundidad esperada en administración, redes o balanceadores.
- **language_requirements:** Español e inglés fluidos.
- **compensation:** 60–80K; moneda, periodicidad, fijo/variable y beneficios no especificados. Por contexto español podría ser salario bruto anual en euros, pero no debe asumirse.

## Ambigüedad y señales tempranas

- **unclear_points:**
  - Identidad, producto y dominio de negocio de la empresa final.
  - Verificación y perímetro de las cifras aproximadas de 4,5M requests/second y sub-100ms; no consta si son globales, pico, promedio, extremo a extremo o de un componente.
  - Significado de “real-time” y requisitos concretos de consistencia, disponibilidad y latencia.
  - Profundidad exacta de DevOps, Linux, terminal, instancias, balanceos, cloud y cambios operativos en producción.
  - Stack completo, arquitectura, prácticas de testing, observabilidad, on-call y permisos operativos.
  - Tipo de contrato, país, residencia, horario, moneda y composición del rango.
  - Nivel de inglés esperado en el trabajo diario y forma de evaluación.
  - Alcance y criterios reales del recorrido hacia Tech Lead.
- **red_flags:**
  - La empresa final no se identifica, lo que impide evaluar producto, estabilidad, cultura y dominio antes de la call.
  - Las expresiones “360”, “genuinely committed” y “get invested” son amplias y podrían ocultar expectativas operativas o de disponibilidad superiores a las descritas.
  - La urgencia por vacaciones del recruiter es circunstancial y no debe forzar una decisión sin aclarar condiciones.
  - Las métricas extraordinarias se presentan sin perímetro técnico verificable.
  - La ausencia de equipo DevOps dedicado puede ampliar materialmente el alcance y la disponibilidad del rol; el recruiter considera los gaps actuales compatibles con continuar, pero el cliente aún debe validarlos.

## Campos consolidados del esquema

- **target_profile_recommendation:** `target-profile:backend-senior`
- **target_profile_alternatives:** [`target-profile:backend-tech-lead`]
- **target_profiles_rejected:** [`target-profile:ai-backend-engineer`, `target-profile:automation-process-engineer`, `target-profile:research-software-engineer`, `target-profile:solutions-architect`, `target-profile:technical-lead-small-company`]
- **strongest_fit_signals:** Java profesional sostenido desde 2020; backend sénior; microservicios bancarios críticos; análisis, desarrollo, review, CI/CD, despliegues, monitorización, producción, mensajería, vulnerabilidades, diagnóstico y soporte; recruiter valida mentalidad y hábitos “360”; experiencia de liderazgo técnico sin título formal.
- **weakest_fit_signals:** Sin métricas canónicas comparables de tráfico o latencia; trabajo previo siempre con equipos DevOps; sin permisos para ejecutar comandos operativos en producción; DevOps, cloud, Linux, terminal, Docker y Kubernetes con profundidad parcial; fluidez lingüística no está registrada como entidad canónica.
- **selected_roles:** [`role:deutsche-bank-senior-backend-software-engineer`, `role:cgi-deutsche-bank-consultant`, `role:mercury-tfs-software-engineer`]
- **selected_projects:** [`project:deutsche-bank-payments-systems`, `project:deutsche-bank-low-code-migration`, `project:mercury-trade-finance-platform`, `project:mercury-document-generation`]
- **selected_stories:** [`story:deutsche-bank-transfer-to-payments-team`, `story:mercury-integration-base`]
- **selected_skills:** [`skill:backend-development`, `skill:microservices`, `skill:critical-systems-operation`, `skill:production-support-and-debugging`, `skill:legacy-system-diagnosis`, `skill:code-review-and-mentoring`, `skill:technical-leadership-without-title`, `skill:stakeholder-communication`]
- **selected_technologies:** [`technology:java`, `technology:spring`, `technology:spring-boot`, `technology:ibm-mq`, `technology:ci-cd`, `technology:docker`, `technology:kubernetes`]
- **selected_achievements:** [`achievement:deutsche-bank-direct-hire-after-consulting`, `achievement:deutsche-bank-transfer-to-critical-payments-team`, `achievement:mercury-functional-reference-areas`, `achievement:mercury-integration-base-deployment-simplification`]
- **risks:** Sobreafirmar escala/latencia, servidores, Linux, terminal, cloud, DevOps, ownership total, liderazgo formal o profundidad de infraestructura; ausencia previa de autonomía operativa en producción; condiciones esenciales de empresa, contrato y operación desconocidas.
- **gaps:** Experiencia demostrada en 4,5M req/s o sub-100ms; DevOps como función principal; administración profunda de Linux, servidores, cloud, instancias o balanceadores; terminal debugging con permisos operativos en producción; experiencia real-time/low-latency delimitada; fluidez formalmente documentada en español e inglés; título formal Tech Lead.
- **questions_to_clarify:** Identidad y producto; alcance de métricas y real-time; proveedor/stack y profundidad DevOps/Linux/cloud; permisos, testing, producción y on-call; equipo y transición a Tech Lead; contrato, país y compensación.
- **recommended_outputs:** CV adaptado: recomendado y autorizado ahora como borrador conservador para revisión del recruiter; preparación de entrevista: recomendada; mensaje adicional: opcional porque la conversación ya está activa; carta: no recomendada salvo petición; LinkedIn: no útil.
- **generation_instructions:** CV Generator v1 puede generar `generated/cv.md` en una fase posterior autorizada, sin generar todavía en esta actualización. Anclarlo en Java/Spring y sistemas de pagos críticos; mostrar ciclo de entrega y responsabilidad de equipo con tareas canónicas; presentar DevOps/cloud/Linux como exposición parcial, nunca profundidad; tratar el CV de CTO adjunto solo como referencia futura de estilo, no como evidencia; no usar métricas de la empresa como logros propios.
- **evidence_boundaries:** No afirmar experiencia en 4,5M req/s, sub-100ms o sistemas real-time/low-latency sin evidencia; no afirmar DevOps o SRE como rol principal, administración profunda de Linux/servidores/cloud, gestión de instancias o balanceadores, autonomía de comandos en producción, performance engineering, ownership total, título Tech Lead ni people management; atribuir IntegrationBase al usuario y un compañero; mantener Spring Boot separado de usos de Spring no delimitados.
- **uncertainty:** La conversación aclara el significado de “360” y permite avanzar, pero empresa, dominio, contrato, arquitectura, herramientas, permisos, on-call y profundidad DevOps siguen sin verificar con el cliente. Azure, GCP, Linux, Windows, migración/rollback y hábitos de ciclo completo proceden de la conversación de candidatura y no se convierten aquí en conocimiento canónico.
