# Prompt reutilizable: generar Application Outcome

Copia este prompt en Codex o ChatGPT y sustituye los parámetros. Debe ejecutarse desde un repositorio CareerOS con acceso al expediente completo.

```text
Genera el análisis global de outcome/post-mortem de una candidatura de CareerOS.

Parámetros:
- source_application_folder: [career/applications/<application-slug> o examples/applications/<example-slug>]
- language: [es / en / auto]
- output_path: [generated/application-outcome.md por defecto]
- focus_areas: [lista opcional o ninguno]

Lee primero:
- knowledge/CONSTITUTION.md
- career/application-lifecycle/README.md
- career/application-lifecycle/application-statuses.md
- career/application-lifecycle/application-events.md
- career/application-lifecycle/submission-record-guidelines.md
- generators/application-outcome/README.md
- generators/application-outcome/application-outcome.schema.md
- generators/application-outcome/application-outcome-workflow.md
- templates/generated/application-outcome.template.md

Después aplica exactamente el orden de fuentes definido por el workflow: submission-record.md primero; fuentes raw/factuales después; intake, plan y riesgos; selecciones; y solo al final outputs analíticos generados. No leas CVs como fuentes factuales.

Reglas de ejecución:

1. Valida que source_application_folder exista bajo career/applications/ o examples/applications/, que application_id coincida y que output_path permanezca dentro de generated/ del mismo expediente.
2. Lee submission-record.md antes que cualquier otro archivo. Interpreta estados, eventos y outcome mediante las definiciones reales de Application Lifecycle; no inventes estados ni semántica.
3. Confirma que existe un outcome significativo documentado: rejected, withdrawn, offer_received, offer_negotiation, accepted, declined o closed. Puede admitirse excepcionalmente otro estado si eventos factuales prueban inequívocamente un cierre material; registra la discrepancia como lifecycle_implication. Si no hay outcome o cierre material, detente sin generar.
4. Establece un timeline factual desde submission-record.md, recruiter-conversation.md y notas bajo interviews/. Conserva fechas desconocidas, mediación y orden incierto. No deduzcas rechazo por silencio ni etapas por patrones habituales.
5. Separa siempre process_fact, explicit_feedback, candidate_impression, inference, unknown, lesson y experiment.
6. Extrae explicit_feedback solo cuando fue comunicado. Conserva cita literal o paráfrasis fiel según la fuente, emisor, rol/organización, canal, fecha, archivo y límites.
7. Mantén feedback_provenance: distingue empresa/cliente, recruiter/intermediario y transmisor. No conviertas feedback recruiter-mediated en feedback directo de empresa salvo evidencia explícita.
8. Lee job-intake.md, application-plan.md y risk-register.md y revisa cada riesgo o hipótesis relevante como confirmed, disconfirmed, unresolved o not_relevant_to_outcome_analysis.
9. No trates un riesgo previo como causa del outcome sin evidencia posterior que conecte explícitamente ambos. Falta de mención no equivale a disconfirmed ni prueba irrelevancia.
10. Lee target-profile-selection.md y evidence-selection.md solo para entender el posicionamiento ya documentado. No inventes experiencia ni amplíes evidencia.
11. Lee debriefs, opportunity dossier e interview prep solo después de fijar los hechos. Son contexto analítico y nunca prevalecen sobre conversaciones, notas o lifecycle. Interview prep no demuestra qué ocurrió.
12. Para cada new_hypothesis incluye: supporting evidence; contradictory or missing evidence; confidence low/medium/high; plausible alternative explanation; y further evidence needed.
13. No generalices un único rechazo, oferta, aceptación o comentario a la identidad del candidato, todo el mercado o todas las empresas similares.
14. Formula lessons acotadas. Si dependen de una hipótesis incierta, conviértelas en experiments testables en lugar de reglas permanentes.
15. Cada experiment debe indicar: hypothesis being tested; change to try; applicable context; signal to observe; what supports it; what weakens it; y qué variables mantener estables. Evita cambiar varias variables mayores a la vez.
16. positioning_implications solo puede proponer presentar de otra forma evidencia existente. No crea hechos ni modifica outputs.
17. target_profile_implications debe elegir no_change_recommended, review_suggested, possible_experiment o insufficient_evidence. Un outcome aislado normalmente no basta para un cambio importante.
18. knowledge_implications normalmente será []; una percepción de recruiter o empresa no es conocimiento canónico. Solo propone verificar hechos profesionales nuevos realmente revelados.
19. Incluye obligatoriamente things_not_to_change para proteger hechos exactos, experiencia real, cronología, identidad, riesgos no resueltos y perfiles frente a sobrerreacción.
20. Mantén process_observations como hechos neutrales. Seguimiento proactivo, demora, feedback tras petición o ausencia de entrevista técnica no demuestran mala cultura, desorganización, falta de respeto, mala calidad o incompetencia.
21. El generador también debe funcionar para ofertas, negociación, aceptación, declinación, retirada y cierre. Una oferta no prueba que todo el posicionamiento causó el éxito; una aceptación no prueba buen encaje futuro.
22. Propón downstream updates en lifecycle_implications, follow_up_items u otras secciones, pero no los apliques.
23. Completa las 22 secciones de la plantilla, elimina placeholders, usa desconocido/ninguno/[] cuando proceda, conserva procedencia cerca de los claims y marca status: draft.
24. Escribe únicamente source_application_folder/output_path, por defecto source_application_folder/generated/application-outcome.md.
25. Detente. No modifiques fuentes, aplicaciones, lifecycle, perfiles objetivo, conocimiento canónico, scripts, CVs ni otros outputs.

Si no existe evidencia suficiente para establecer el outcome o un cierre material inequívoco, detente sin generar según el workflow. Si el outcome sí está establecido pero no hay evidencia suficiente para determinar su causa, resolver un riesgo previo, sostener una implicación o generalizar una lección, genera igualmente `application-outcome.md`: conserva esos elementos como `unknown`, `unresolved` o `insufficient_evidence`, o evita la conclusión no respaldada. La falta de evidencia analítica reduce el alcance del análisis; no invalida un post-mortem cuyo outcome está documentado.
```
