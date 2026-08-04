# Selección de perfil objetivo: Talent-R / scale-up no identificada — Senior Backend Engineer

## Recomendación

- **primary_target_profile:** `target-profile:backend-senior`
- **qualitative_fit:** fuerte
- **recommendation:** aplicar de forma selectiva
- **reasons:**
  - El título y Java muy fuerte coinciden directamente con el posicionamiento Backend Senior.
  - La evidencia reciente cubre backend Java/Spring, microservicios, sistemas críticos, producción, despliegues, mensajería, vulnerabilidades y soporte.
  - El perfil principal ya contiene los límites esenciales de esta candidatura: sin métricas de tráfico/disponibilidad y sin convertir operación en SRE o administración profunda.
  - El recruiter validó la mentalidad y los hábitos “360”, consideró que los gaps DevOps no son descarte automático, aceptó entrevistar y solicitó CV y email.
  - El CV puede enviarse de forma conservadora; la decisión final sigue condicionada a validar con el cliente la profundidad DevOps/Linux/cloud, on-call y condiciones.

## Perfiles secundarios posibles

| Perfil objetivo existente | Encaje | Aporte específico | Riesgo de mezclarlo |
|---|---|---|---|
| `target-profile:backend-tech-lead` | moderado | Permite encuadrar revisión, acompañamiento, referencia funcional y potencial futuro de Tech Lead. | Puede sugerir falsamente título formal, autoridad o people management; debe ser un ángulo secundario. |

## Perfiles descartados

| Perfil objetivo existente | Motivo del descarte | Señal decisiva |
|---|---|---|
| `target-profile:ai-backend-engineer` | No se menciona IA, Python ni producto de IA. | Java y sistema real-time son el núcleo explícito. |
| `target-profile:automation-process-engineer` | La automatización no es el propósito central. | Se busca Senior Backend Engineer. |
| `target-profile:research-software-engineer` | No existe contexto de investigación, educación o cultura. | Sistema comercial de scale-up orientado a rendimiento. |
| `target-profile:solutions-architect` | No se solicita un rol formal de arquitectura o discovery. | El trabajo se presenta como backend hands-on y producción. |
| `target-profile:technical-lead-small-company` | “360” aporta cierta amplitud, pero no constan herramientas internas, operaciones de negocio ni responsabilidad técnica transversal de empresa pequeña. | El título y Java delimitan un rol backend; la empresa es una scale-up, no necesariamente un equipo pequeño. |

## Señales de encaje

- **strongest_fit_signals:**
  - Java muy fuerte ↔ núcleo Java/Spring del perfil ↔ `technology:java`, `technology:spring`, `role:deutsche-bank-senior-backend-software-engineer`.
  - Backend senior ↔ desarrollo y mantenimiento de servicios complejos ↔ `skill:backend-development`, `project:deutsche-bank-payments-systems`.
  - Producción, calidad y ownership ↔ operación práctica ↔ `skill:critical-systems-operation`, `skill:production-support-and-debugging`.
  - Ciclo completo y hábitos 360 ↔ análisis, review, CI/CD, despliegue y monitorización descritos transparentemente en la conversación ↔ evidencia canónica parcial en producción, CI/CD y code review.
  - Más allá del IDE ↔ despliegues, MQ, certificados, vulnerabilidades y soporte ↔ rol actual y `technology:ibm-mq`.
  - Potencial Tech Lead ↔ liderazgo técnico sin título ↔ `skill:technical-leadership-without-title`, `skill:code-review-and-mentoring`, `achievement:mercury-functional-reference-areas`.
- **weakest_fit_signals:**
  - Alto rendimiento, real-time, 4,5M req/s y sub-100ms ↔ no hay métricas ni experiencia canónica equivalente.
  - DevOps/Linux/cloud/terminal ↔ hay exposición y hábitos operativos, pero siempre existieron equipos DevOps y no había permisos de comandos en producción.
  - Testing propio ↔ la conversación afirma pruebas locales dentro del ciclo habitual, pero el detalle y las prácticas no están estructurados en entidades canónicas.
  - Español e inglés fluidos ↔ no existe entidad canónica de competencia lingüística.

## Riesgos específicos del perfil

- Confundir criticidad bancaria o “tráfico muy alto” sin cifras con la escala concreta de la empresa.
- Ampliar responsabilidades operativas acotadas hasta SRE, plataforma o administración de servidores.
- Presentar potencial de Tech Lead como título o experiencia formal.
- Diluir el núcleo backend intentando cubrir todo lo que el recruiter llama “360”.
- Convertir la validación del recruiter sobre mentalidad y hábitos en una validación técnica del cliente, que todavía no existe.

## Incertidumbre

- El recruiter ha permitido avanzar con los gaps, pero una entrevista técnica puede revelar que infraestructura, Linux, low latency o autonomía operativa pesan más que backend Java.
- No se conocen dominio, stack completo, tamaño de equipo, proveedor cloud definitivo, permisos, on-call ni condiciones.
