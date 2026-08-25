# Esquema de Application Outcome

## Propósito

Application Outcome es un análisis trazable del resultado global de una candidatura. Reúne cronología, feedback, riesgos previos, hipótesis, lecciones y experimentos sin sustituir las fuentes del expediente ni ejecutar cambios derivados.

## Campos obligatorios

| Campo | Descripción |
|---|---|
| `id` | ID estable: `application-outcome:<application-slug>`. |
| `application_id` | ID del expediente: `application:<application-slug>`. |
| `source_application_folder` | Ruta relativa exacta de la candidatura o fixture. |
| `output_type` | En v1, `application-outcome`. |
| `language` | Idioma final y base de elección. |
| `status` | Estado del output generado. |
| `generated_date` | Fecha real de generación en `YYYY-MM-DD`; no sustituye la fecha del outcome. |
| `application_outcome` | Resultado operativo leído del lifecycle o descripción fiel del cierre material excepcional. |
| `outcome_date` | Fecha demostrable del outcome en `YYYY-MM-DD` o `desconocida`. |
| `outcome_source` | Evento, comunicación o fuente exacta que respalda el resultado. |
| `source_files_used` | Rutas realmente leídas, función y fuerza factual de cada una. |
| `process_summary` | Síntesis cronológica y neutral de las etapas documentadas. |
| `confirmed_outcome` | Resultado documentado, separado de sus posibles causas. |
| `explicit_feedback` | Feedback realmente comunicado, con contenido, emisor, relación con la empresa, fecha, canal, fuente y límites. |
| `feedback_provenance` | Mapa de quién originó y quién transmitió cada feedback; conserva mediación e incertidumbre. |
| `process_observations` | Patrones observables del proceso sin juicios sobre personas, cultura o calidad. |
| `prior_hypotheses_or_risks` | Hipótesis, gaps o riesgos previos relevantes y su fuente original. |
| `hypotheses_confirmed` | Elementos previos confirmados explícitamente por evidencia posterior. |
| `hypotheses_disconfirmed` | Elementos previos contradichos explícitamente por evidencia posterior. |
| `hypotheses_unresolved` | Elementos que la evidencia posterior no confirma ni refuta. |
| `new_hypotheses` | Interpretaciones nuevas con apoyo, evidencia ausente/contradictoria, confianza, alternativa y necesidad de más evidencia. |
| `candidate_impressions` | Sensaciones y autoevaluaciones del candidato, separadas de feedback externo. |
| `lessons` | Takeaways prácticos, acotados y respaldados; indican alcance y límite de generalización. |
| `positioning_implications` | Posibles cambios de presentación usando únicamente evidencia existente. |
| `target_profile_implications` | `no_change_recommended`, `review_suggested`, `possible_experiment` o `insufficient_evidence`, con justificación. |
| `future_application_implications` | Aplicaciones concretas para procesos futuros, limitadas al contexto respaldado. |
| `knowledge_implications` | Hechos candidatos a verificación canónica o `[]`; una percepción externa no es conocimiento del candidato. |
| `experiments` | Pruebas futuras con hipótesis, cambio, contexto, señal y criterios de apoyo/debilitamiento. |
| `things_not_to_change` | Protecciones explícitas contra reacciones excesivas o claims inventados. |
| `lifecycle_implications` | Actualizaciones factuales que otro workflow debería evaluar, o `[]`; no se aplican aquí. |
| `follow_up_items` | Acciones externas o internas todavía justificadas, distinguiendo obligación, opción y propuesta. |
| `do_not_assume` | Conclusiones prohibidas por ausencia de evidencia o causalidad. |
| `uncertainty` | Fechas, fuentes, causalidad, conflictos y límites que permanecen abiertos. |
| `review_checklist` | Controles realizados antes de usar o incorporar el análisis. |

Todos los campos deben aparecer aunque su valor sea `[]`, `ninguno` o `desconocido`.

## Valores permitidos

- `output_type`: `application-outcome`.
- `status`: `draft`, `reviewed`, `incorporated`, `discarded`.
- `target_profile_implications.decision`: `no_change_recommended`, `review_suggested`, `possible_experiment`, `insufficient_evidence`.
- clasificación de un riesgo previo: `confirmed`, `disconfirmed`, `unresolved`, `not_relevant_to_outcome_analysis`.
- confianza de una inferencia: `low`, `medium`, `high`.

Todo output nuevo comienza en `draft`. `reviewed` exige revisión humana contra las fuentes. `incorporated` significa que propuestas aceptadas ya fueron procesadas mediante workflows separados; no autoriza al outcome a ejecutarlas. `discarded` indica que la versión no debe utilizarse.

`application_outcome` debe conservar el resultado documentado por el lifecycle. Los estados ordinariamente elegibles de v1 son `rejected`, `withdrawn`, `offer_received`, `offer_negotiation`, `accepted`, `declined` y `closed`. No se inventa `negotiation` como estado.

`confirmed_outcome` normaliza el resultado como `rejection`, `withdrawal`, `offer`, `acceptance`, `decline`, `closed_without_outcome` u `other`, pero solo cuando la fuente lo permite. Un `closed` administrativo conserva el outcome separado documentado en `submission-record.md`; no se traduce automáticamente a rechazo.

## Categorías de procedencia

| Categoría | Significado | Requisito mínimo |
|---|---|---|
| `process_fact` | Algo documentado como ocurrido. | Fuente y fecha o incertidumbre explícita. |
| `explicit_feedback` | Valoración o razón comunicada expresamente. | Contenido, emisor, canal, fecha y mediación. |
| `candidate_impression` | Percepción o autoevaluación del candidato. | Fuente que la identifica como impresión. |
| `inference` | Hipótesis analítica derivada. | Apoyo, contraevidencia/ausencia, confianza y alternativa. |
| `unknown` | Aspecto no resuelto. | Explicación de qué falta. |
| `lesson` | Takeaway práctico limitado. | Hechos de apoyo y límite de generalización. |
| `experiment` | Prueba futura de una hipótesis. | Variable, contexto, señal y criterios de lectura. |

## Correspondencia con el documento

El output incluye, en este orden:

1. Metadata.
2. Resumen del outcome.
3. Timeline factual del proceso.
4. Outcome confirmado.
5. Feedback explícito.
6. Observaciones del proceso.
7. Riesgos e hipótesis anteriores revisitados.
8. Qué parece confirmado.
9. Qué parece refutado.
10. Qué permanece sin resolver.
11. Hipótesis nuevas.
12. Lecciones.
13. Implicaciones de posicionamiento.
14. Implicaciones para Target Profiles.
15. Implicaciones para futuras candidaturas.
16. Implicaciones para conocimiento.
17. Experimentos.
18. Cosas que no deben cambiar.
19. Implicaciones de lifecycle y follow-up.
20. Lista de supuestos prohibidos.
21. Incertidumbre.
22. Checklist final de revisión.

## Reglas de causalidad

- `confirmed_outcome` describe el resultado, no su causa.
- `explicit_feedback` contiene solo lo comunicado, sin completar motivos plausibles.
- Un feedback transmitido por recruiter se registra como recruiter-mediated salvo prueba de comunicación directa o autoría empresarial explícita.
- Un riesgo previo pasa a `confirmed` solo cuando evidencia posterior respalda esa proposición y, si se presenta como causa, conecta explícitamente el riesgo con el outcome.
- Falta de mención no equivale a `disconfirmed`; normalmente produce `unresolved` o `not_relevant_to_outcome_analysis`.
- Una entrevista no celebrada no autoriza conclusiones sobre rendimiento técnico.
- Una oferta no demuestra que todas las fortalezas, materiales o decisiones causaran el éxito.

## Reglas de hipótesis, lecciones y experimentos

- Cada nueva hipótesis incluye evidencia de apoyo, evidencia contradictoria o ausente, confianza, explicación alternativa y necesidad de más evidencia.
- La confianza `high` exige evidencia directa y convergente; no se usa por mera plausibilidad.
- Una lección debe ser más estrecha que una regla universal e indicar dónde podría aplicar.
- Un único outcome no justifica por defecto una modificación importante de Target Profiles.
- Cada experimento cambia el menor número razonable de variables y define: hipótesis, cambio, contexto, señal, qué la apoyaría y qué la debilitaría.
- Un experimento no se presenta como nueva política permanente.

## Reglas de validación

- `source_application_folder` existe bajo `career/applications/` o `examples/applications/` y coincide con `application_id`.
- `submission-record.md` se lee primero y contiene outcome significativo o evidencia inequívoca de cierre material.
- Si el estado no es ordinariamente elegible, la excepción se justifica con eventos concretos y se propone corregir lifecycle por separado.
- El timeline deriva de fuentes factuales y conserva fechas desconocidas, orden incierto y mediación.
- `source_files_used` distingue fuente factual primaria de contexto analítico generado.
- Las conversaciones y notas brutas prevalecen sobre debriefs, dossiers y preparación.
- Los CVs no se usan como fuentes factuales.
- No se explora conocimiento canónico salvo validación explícitamente requerida de una implicación; nunca se modifica.
- Cada feedback conserva texto literal o paráfrasis fiel, emisor, relación, canal, fecha, fuente y límite.
- Process observation no se convierte en juicio sobre cultura, organización, respeto, calidad o competencia.
- `prior_hypotheses_or_risks` revisa como mínimo intake, plan y risk register cuando existen.
- Todos los riesgos relevantes reciben una clasificación permitida y una justificación basada en evidencia posterior.
- `things_not_to_change` existe y protege hechos exactos, ausencia de experiencia, identidad y perfiles frente a sobrerreacción.
- `knowledge_implications` no convierte opiniones empresariales o del recruiter en hechos canónicos del candidato.
- Las implicaciones downstream son propuestas; ningún destino se modifica.
- No quedan placeholders.
- El único archivo creado o reemplazado es `<source_application_folder>/generated/application-outcome.md`, o el `output_path` válido equivalente dentro de `generated/` del mismo expediente.

