# Registro de riesgos: knowmad mood — Senior Backend Java

## Escala

- Probabilidad: alta / media / baja / desconocida.
- Impacto: alto / medio / bajo.
- Estado: abierto / pendiente de aclaración / mitigado / aceptado.

## Riesgos de sobreafirmación

| Riesgo | Evidencia o límite afectado | Probabilidad | Impacto | Mitigación | Estado |
|---|---|---|---|---|---|
| Presentar experiencia con Kafka | `technology:ibm-mq`; no existe evidencia canónica de Kafka | Alta | Alto | Nombrar IBM MQ y experiencia en mensajería; declarar Kafka como gap. | Mitigado en el plan |
| Afirmar arquitectura escalable desde cero | `skill:software-architecture`, `skill:microservices` | Alta | Alto | Hablar de pensamiento arquitectónico y contribuciones acotadas; aclarar ownership esperado. | Pendiente de aclaración |
| Usar título Tech Lead o liderazgo formal | `skill:technical-leadership-without-title`, `achievement:mercury-functional-reference-areas` | Media | Alto | Conservar títulos formales y describir conductas observables. | Mitigado en el plan |
| Afirmar experiencia profesional de IA/ML | `project:deos`, `achievement:deos-knowledge-extraction-working-pipeline` | Alta | Alto | Identificar DEOS como personal y limitado; no usarlo como prueba de IA profesional en SDLC. | Mitigado en el plan |
| Afirmar API First o gobierno completo de APIs | `skill:api-design-and-integration` | Media | Medio | Describir integración y experiencia con APIs; mantener API First como gap. | Abierto |
| Enumerar SOLID, Clean Code, DDD, testing o SDD como experiencia probada | No hay evidencia canónica específica seleccionable | Alta | Alto | Omitir claims; obtener evidencia canónica o reconocer el gap. | Abierto |
| Inflar escala, disponibilidad o autoría | `project:deutsche-bank-payments-systems`, `story:mercury-integration-base` | Media | Alto | No inventar métricas; conservar trabajo de equipo y atribución compartida. | Mitigado en el plan |

## Áreas de evidencia débil

| Área | Fuerza disponible | Qué no demuestra | Mitigación |
|---|---|---|---|
| Arquitectura de software | Moderada en `skill:software-architecture` | Cargo formal, diseño global, escalabilidad cuantificada o arquitectura completa desde cero | Usar ejemplos delimitados y preguntar por alcance. |
| APIs | Moderada en `skill:api-design-and-integration` | API First, contratos públicos, gobierno o versionado atribuibles | Enfatizar integración; no ampliar el claim. |
| Liderazgo | Moderada en `skill:technical-leadership-without-title` | Tech Lead formal, people management o autoridad final | Describir revisión, apoyo, estimación y referencia funcional. |
| Spring Boot | Moderada en `technology:spring-boot` | Módulos, versiones o dominio avanzado específico | Vincularlo a Mercury y no inventar detalle. |
| Kubernetes/CI/CD/Docker | Limitada o contextual según sus entidades | Administración profunda o ownership de plataforma | Mantener como contexto secundario, no como eje. |
| IA aplicada | Limitada y personal en DEOS | Uso profesional en SDLC, ML Engineering, producción o escala | Tratar como interés/proyecto personal solo si resulta necesario. |

## Requisitos ausentes

| Requisito de la oferta | Estado | Impacto en el encaje | Mitigación honesta |
|---|---|---|---|
| Kafka | No respaldado | Medio; la oferta acepta “o sistemas de mensajería” | Presentar IBM MQ y confirmar equivalencia. |
| Arquitectura escalable desde cero | Parcial | Alto | Aclarar responsabilidad y presentar solo pensamiento arquitectónico respaldado. |
| API First | Parcial | Medio | No equiparar APIs/integración con API First. |
| SOLID | Desconocido/no respaldado explícitamente | Medio | No reclamarlo sin nueva evidencia. |
| Clean Code | Desconocido/no respaldado explícitamente | Medio | No reclamarlo sin nueva evidencia. |
| DDD | No respaldado explícitamente | Medio a alto | Preguntar profundidad esperada; no inferirlo de microservicios o dominio bancario. |
| Testing técnico | No respaldado explícitamente | Medio | Preguntar estrategia y herramientas; user testing no cubre el requisito. |
| Spec Driven Development | No respaldado | Medio | Aclarar definición y expectativas de experiencia previa. |
| IA en el ciclo profesional de desarrollo | Parcial como interés, no como práctica profesional | Medio | No usar DEOS como equivalencia; aclarar la expectativa concreta. |

## Expectativas del puesto poco claras

| Incertidumbre | Interpretaciones posibles | Riesgo | Pregunta necesaria |
|---|---|---|---|
| “Definir arquitectura desde cero” | Diseño compartido; ownership individual; implementación sobre estándares del cliente | Puede elevar el rol a arquitecto/lead sin apoyo suficiente | ¿Quién decide y valida la arquitectura y qué artefactos/resultados esperan? |
| “Capacidad de liderazgo” | Influencia técnica; mentoring; coordinación; people management | Desajuste si exige título o gestión formal previa | ¿Qué autoridad, equipo y responsabilidades de personas incluye? |
| “Kafka o mensajería” | Cualquier broker; Kafka preferente; Kafka obligatorio en la práctica | Filtro técnico pese al texto abierto | ¿IBM MQ u otra mensajería se considera experiencia válida? |
| “Impulsar IA” | Uso de asistentes; automatización; gobernanza; construcción de producto | Puede exigir experiencia profesional no disponible | ¿Qué casos de uso, herramientas, restricciones y ownership contempla? |
| SDD | Spec-driven development con herramientas concretas u otra convención interna | Gap difícil de preparar sin definición | ¿Qué proceso y tooling llaman SDD? |
| Proyecto internacional de People | Producto interno, plataforma HR o servicio al cliente | Dominio, privacidad e idioma desconocidos | ¿Cuál es el producto, usuarios, idioma y contexto regulatorio? |
| Operación posterior | Solo construcción; ownership de producción; soporte/guardias | Cambia el valor de la experiencia operativa y las condiciones | ¿Incluye producción, guardias, observabilidad o soporte? |

## Ubicación, contrato y compensación

| Riesgo | Dato disponible | Dato faltante | Mitigación |
|---|---|---|---|
| Alcance geográfico del remoto | Remoto a elección, oficinas opcionales | Países permitidos, residencia y ubicación contractual | Confirmar antes de avanzar. |
| Contratación | Indefinido; 12 o 14 pagas | Empleador, periodo de prueba y convenio/condiciones | Solicitar detalle contractual. |
| Compensación | Retribución flexible y beneficios | Rango fijo, variable y valoración de beneficios | Pedir rango salarial al inicio. |
| Horario | Franja publicada, viernes y verano intensivos | Zona horaria y flexibilidad real con equipo internacional | Confirmar coordinación horaria. |

## Red flags

- Título de Senior Backend con responsabilidad potencial de arquitecto principal y liderazgo; requiere aclarar alcance, no descartar automáticamente.
- Ausencia de rango salarial y de detalles del equipo/cliente/producto.
- Terminología amplia de IA y SDD sin definición operativa.
- No se identifican responsabilidades de producción, pese a pedir sistemas distribuidos y arquitectura escalable.

## Recomendación consolidada

- Riesgos bloqueantes: ninguno confirmado; arquitectura individual obligatoria, Kafka excluyente o liderazgo formal podrían convertirse en bloqueantes tras aclaración.
- Riesgos aceptables: falta de Kafka si IBM MQ satisface mensajería; transición hacia mayor liderazgo hands-on; adopción de prácticas nuevas si no exigen experiencia previa demostrada.
- Condiciones para aplicar: mantener posicionamiento Backend Senior, resolver alcance arquitectónico/mensajería/IA/SDD y conocer rango salarial y remoto geográfico.
- Recomendación: aplicar tras aclarar.
