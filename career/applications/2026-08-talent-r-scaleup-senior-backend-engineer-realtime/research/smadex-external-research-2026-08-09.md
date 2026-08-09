# Investigación externa — Smadex

Fecha de consulta: 2026-08-09

## Propósito

Fuentes externas recopiladas para generar el Opportunity Dossier de la candidatura Senior Backend Engineer gestionada por Talent-R.

Estas notas describen a Smadex y su contexto empresarial/técnico.
No son evidencia profesional del candidato.

## Fuente 1 — Smadex About

URL:
https://smadex.com/about/

Tipo:
Fuente oficial de empresa.

Datos relevantes:
- Smadex se presenta como una Mobile Growth Platform.
- Trabaja en performance, direct response y brand advertising.
- Opera en in-app, CTV y mobile web.
- Describe su enfoque como privacy-centric y basado en contextual targeting.
- Declara utilizar algoritmos de machine learning personalizables y first-party data.
- Menciona verticales como gaming, finance y entertainment.

Límite:
Claims corporativos de Smadex; no constituyen verificación independiente.

## Fuente 2 — Smadex homepage

URL:
https://smadex.com/

Tipo:
Fuente oficial de empresa.

Datos relevantes:
- Smadex se describe como una AI-Powered DSP.
- Sus líneas visibles incluyen:
  - Mobile User Acquisition.
  - Connected TV.
  - Retargeting.
  - Mobile Subscription Services.
- Presenta funcionalidades de machine learning y optimización de campañas.

Límite:
Descripción comercial de la propia empresa.

## Fuente 3 — Performance and Transparency

URL:
https://smadex.com/performance-transparency/

Tipo:
Fuente oficial de producto/tecnología.

Datos relevantes:
- Smadex declara usar algoritmos de IA y Deep Neural Networks para optimización.
- Declara reporting multidimensional con más de 350 variables.
- La web afirma actualmente que la plataforma procesa más de 3.000.000 de bid request queries por segundo.
- La web afirma que puede evaluar y comprar espacio publicitario en menos de 100 ms.

Límite:
Son métricas publicadas por Smadex, no verificadas independientemente.
No convertirlas en experiencia del candidato.

Nota:
El recruiter indicó durante el proceso aproximadamente 4,5 millones de requests por segundo y sub-100 ms.
Mantener ambas cifras separadas:
- cifra pública de Smadex;
- declaración del recruiter.
No asumir que miden exactamente lo mismo ni tratarlas automáticamente como contradicción.

## Fuente 4 — Entravision

URL:
https://entravision.com/

Tipo:
Fuente oficial de empresa matriz.

Datos relevantes:
- Entravision se define como media and advertising technology company.
- Entravision identifica a Smadex como su plataforma de compra publicitaria programática.
- Indica que permite a clientes, principalmente desarrolladores de apps móviles, comprar publicidad electrónicamente y gestionar campañas data-driven.
- La actividad AdTech de Entravision opera globalmente.

Límite:
Descripción corporativa de Entravision.

## Fuente 5 — Entravision investor relations

URL:
https://investor.entravision.com/news/news-details/2026/Entravision-to-Announce-Fourth-Quarter-and-Full-Year-2025-Financial-Results/default.aspx

Tipo:
Fuente corporativa / investor relations.

Datos relevantes:
- Entravision seguía describiendo en 2026 su advertising technology business como compuesto por Smadex y Adwake.
- Smadex aparece descrita como su programmatic ad purchasing platform.

Límite:
Fuente corporativa, aunque útil para confirmar la relación actual Entravision–Smadex.

## Fuente 6 — Adquisición por Entravision

URL:
https://smadex.com/entravision-completes-acquisition-of-smadex/

Tipo:
Fuente histórica oficial.

Datos relevantes:
- Entravision completó la adquisición de Smadex en 2018.
- El objetivo declarado incluía continuar desarrollando la plataforma DSP y ampliar capacidades programáticas.

Límite:
Fuente histórica; usar la fuente actual de Entravision para confirmar la relación presente.

## Fuente 7 — Programmatic Mobile Subscriptions

URL:
https://smadex.com/programmatic-mobile-subscriptions/

Tipo:
Fuente oficial de producto.

Datos relevantes:
- Explica el funcionamiento general del real-time bidding:
  - compradores definen campaña, presupuesto y objetivos;
  - llegan oportunidades de impresión;
  - DSPs participan en subastas;
  - se decide si pujar;
  - si se gana, se sirve el anuncio;
  - conversiones posteriores alimentan optimización.
- Identifica como actores DSPs, SSPs, ad exchanges, publishers y buyers.
- Explica que las decisiones programáticas ocurren en tiempo real y en escalas de milisegundos.

Límite:
Contenido educativo/comercial de Smadex.
No inferir la arquitectura interna concreta a partir de la explicación conceptual.

## Fuente 8 — Contact / entidad legal

URL:
https://smadex.com/contact/

Tipo:
Fuente oficial.

Datos relevantes:
- Entidad legal mostrada: SMADEX S.L.U.
- Dirección registrada mostrada:
  C/ Diputació 303, Primera Planta, 08009 Barcelona, Spain.

Límite:
No inferir a partir de la dirección modalidad presencial, oficina habitual del equipo backend o requisitos de residencia.

## Síntesis provisional

Smadex parece ser una compañía AdTech centrada en una DSP propia que participa en compra programática de publicidad en tiempo real.

El producto requiere, por la naturaleza descrita públicamente y por las métricas publicadas, procesamiento de un volumen muy alto de solicitudes con ventanas de decisión muy reducidas.

Esto hace especialmente relevantes para la candidatura:
- sistemas distribuidos;
- rendimiento y latencia;
- alta disponibilidad;
- networking y comunicación entre servicios;
- observabilidad;
- operación de producción;
- infraestructura;
- CI/CD;
- debugging;
- capacidad para diagnosticar problemas bajo restricciones temporales.

IMPORTANTE:
La lista anterior es una implicación para investigar/preparar.
No demuestra que el candidato tenga experiencia directa en todos esos ámbitos.

## Incógnitas importantes

- Arquitectura concreta del backend.
- Stack real del equipo, más allá de Java indicado por recruiter.
- Uso actual exacto de cloud y proveedor.
- Qué significa exactamente "algo de DevOps" para un backend engineer.
- Nivel de acceso real a producción.
- Qué operaciones debe ejecutar un developer directamente.
- Uso de Kubernetes y/o contenedores.
- Observabilidad y tooling.
- On-call y frecuencia.
- Cómo se reparte ownership entre backend y plataforma.
- Tamaño y estructura del equipo.
- Qué parte del sistema procesa el equipo al que pertenece la vacante.
- Qué métricas de performance son responsabilidad directa del backend engineer.
- Qué esperan durante los primeros 3–6 meses.
