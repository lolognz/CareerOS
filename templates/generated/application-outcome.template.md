# Application Outcome — [empresa/intermediario] — [puesto]

## 1. Metadata

- **id:** `application-outcome:[application-slug]`
- **application_id:** `application:[application-slug]`
- **source_application_folder:** `[ruta]`
- **output_type:** `application-outcome`
- **language:** `[es / en]`
- **status:** `draft`
- **generated_date:** `[YYYY-MM-DD]`
- **application_outcome:** `[resultado lifecycle documentado]`
- **outcome_date:** `[YYYY-MM-DD / desconocida]`
- **outcome_source:** `[evento, comunicación y ruta]`
- **source_files_used:**
  - `[ruta]` — `[fuente factual primaria / contexto analítico y función]`

## 2. Resumen del outcome

- **process_summary:**
- **Resultado:** `[síntesis factual]`
- **Etapa alcanzada:** `[última etapa demostrable]`
- **Feedback principal:** `[feedback explícito o ninguno]`
- **Lectura limitada:** `[qué puede concluirse y qué no]`

## 3. Timeline factual del proceso

| Fecha | Categoría | Hecho | Fuente | Límite |
|---|---|---|---|---|
| [fecha o desconocida] | `process_fact` | [hecho documentado] | [ruta/evento] | [incertidumbre o ninguno] |

## 4. Outcome confirmado

- **confirmed_outcome:** `[rejection / withdrawal / offer / acceptance / decline / closed_without_outcome / other]`
- **Evidencia:** `[fuente directa]`
- **Fecha:** `[fecha o desconocida]`
- **Quién lo comunicó o ejecutó:** `[parte y rol]`
- **Qué no demuestra:** `[causas o conclusiones no soportadas]`

## 5. Feedback explícito

- **explicit_feedback:**

| Fecha | Feedback | Forma | Emisor/origen | Transmisor y canal | Fuente | Límite |
|---|---|---|---|---|---|---|
| [fecha] | [cita exacta o paráfrasis fiel] | `[literal / paráfrasis]` | [empresa/recruiter/desconocido] | [persona, mediación y canal] | [ruta] | [alcance/incertidumbre] |

### Procedencia del feedback

- **feedback_provenance:** `[cadena de origen/transmisión conocida]`
- **Mediación:** `[directo / recruiter-mediated / desconocida]`
- **Autoría no demostrada:** `[detalle o ninguno]`

## 6. Observaciones del proceso

- **process_observations:**

| Observación factual | Evidencia | Qué no se infiere |
|---|---|---|
| [process_fact] | [fuente] | [juicio no autorizado] |

## 7. Riesgos e hipótesis anteriores revisitados

- **prior_hypotheses_or_risks:**

| Riesgo o hipótesis previa | Fuente original | Clasificación | Evidencia posterior | Lectura conservadora |
|---|---|---|---|---|
| [elemento] | [ruta/sección] | `[confirmed / disconfirmed / unresolved / not_relevant_to_outcome_analysis]` | [fuente o ninguna] | [límite causal] |

## 8. Qué parece confirmado

- **hypotheses_confirmed:**
  - [hipótesis, evidencia explícita y alcance]

## 9. Qué parece refutado

- **hypotheses_disconfirmed:**
  - [hipótesis, evidencia contradictoria y alcance]

## 10. Qué permanece sin resolver

- **hypotheses_unresolved:**
  - [riesgo/hipótesis y evidencia que falta]

## 11. Hipótesis nuevas

- **new_hypotheses:**

| Hipótesis | Evidencia de apoyo | Evidencia contradictoria o ausente | Confianza | Alternativa plausible | Evidencia adicional necesaria |
|---|---|---|---|---|---|
| [proposición acotada] | [fuentes] | [límites] | `[low / medium / high]` | [explicación alternativa] | [cómo comprobar] |

### Impresiones del candidato

- **candidate_impressions:**
  - [impresión o autoevaluación, fuente y límite]

## 12. Lecciones

- **lessons:**

| Lección acotada | Base factual | Contexto de aplicación | Límite de generalización |
|---|---|---|---|
| [takeaway práctico] | [fuente] | [cuándo podría aplicar] | [qué no convierte en regla] |

## 13. Implicaciones de posicionamiento

- **positioning_implications:**
  - **Propuesta:** [presentación posible de evidencia existente]
  - **Evidencia disponible:** [IDs/rutas ya existentes]
  - **Límite:** [claim que no debe crearse]
  - **Estado:** `[propuesta / insuficiente evidencia]`

## 14. Implicaciones para Target Profiles

- **target_profile_implications:**
- **decision:** `[no_change_recommended / review_suggested / possible_experiment / insufficient_evidence]`
- **Perfil afectado:** `[ID o ninguno]`
- **Motivo:** `[evidencia y proporcionalidad]`
- **Cambio directo:** ninguno; requiere workflow separado.

## 15. Implicaciones para futuras candidaturas

- **future_application_implications:**
  - [acción contextual y evidencia que la respalda]

## 16. Implicaciones para conocimiento

- **knowledge_implications:**
  - **Hecho candidato:** [detalle o ninguno]
  - **Fuente:** [ruta]
  - **Verificación necesaria:** [evidencia requerida]
  - **No incorporar todavía porque:** [límite]

## 17. Experimentos

- **experiments:**

| Hipótesis probada | Cambio a probar | Contexto | Señal observable | Apoyaría la hipótesis | La debilitaría | Variables a mantener |
|---|---|---|---|---|---|---|
| [hipótesis] | [cambio mínimo] | [tipo de candidatura] | [señal] | [resultado] | [resultado] | [controles] |

## 18. Cosas que no deben cambiar

- **things_not_to_change:**
  - [hecho, experiencia, cronología, límite o perfil protegido]

## 19. Implicaciones de lifecycle y follow-up

### Lifecycle

- **lifecycle_implications:**

| Propuesta para workflow separado | Evidencia | Destino | Estado |
|---|---|---|---|
| [actualización o ninguna] | [fuente] | [submission-record.md u otro] | `[pendiente / no necesaria]` |

### Follow-up

- **follow_up_items:**
  - [acción, responsable y carácter obligatorio/opcional/propuesto]

## 20. Lista de supuestos prohibidos

- **do_not_assume:**
  - [conclusión no respaldada]

## 21. Incertidumbre

- **uncertainty:**
- **unknown:** [dato no resuelto]
- **Fuente del límite:** [ruta o ausencia]
- **Impacto en el análisis:** [qué conclusión impide]

## 22. Checklist final de revisión

- **review_checklist:**
- [ ] El outcome está documentado y no se dedujo del silencio.
- [ ] El timeline usa fuentes factuales antes que outputs generados.
- [ ] Feedback explícito e inferencias están separados.
- [ ] La mediación del recruiter se conserva.
- [ ] Ningún riesgo previo se convirtió en causa sin evidencia.
- [ ] Falta de mención no se trató como refutación.
- [ ] Impresiones del candidato siguen etiquetadas.
- [ ] Las observaciones del proceso no se convirtieron en juicios de empresa o recruiter.
- [ ] Un único outcome no se generalizó al candidato o mercado.
- [ ] Las lecciones son acotadas y los experimentos son testables.
- [ ] `things_not_to_change` protege contra sobrerreacción.
- [ ] Target Profiles y conocimiento solo reciben propuestas, no cambios.
- [ ] Los CVs no se usaron como fuentes factuales.
- [ ] No se modificó ninguna fuente ni otro output.
- [ ] El documento sigue en `draft` hasta revisión humana.
