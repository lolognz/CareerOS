# Generador de outcome y post-mortem de candidatura

Application Outcome analiza una candidatura completa cuando existe un resultado significativo o el proceso está materialmente concluido. Su objetivo es conservar aprendizajes útiles, revisar riesgos previos y proponer experimentos sin reescribir la cronología, inventar causalidad ni convertir un único proceso en una verdad general sobre el candidato o el mercado.

## Alcance de v1

El generador trabaja sobre una única carpeta bajo `career/applications/<application-slug>/` o `examples/applications/<example-slug>/` y crea o reemplaza exclusivamente:

```text
<application-folder>/generated/application-outcome.md
```

Es un singleton por candidatura: representa el análisis vigente del outcome global. Puede regenerarse cuando aparece feedback factual posterior. Git conserva las versiones anteriores; el archivo actual refleja el análisis más reciente.

El output es análisis generado y desechable. `submission-record.md`, las conversaciones y las notas brutas siguen siendo las fuentes factuales. Application Outcome no actualiza el lifecycle ni ninguna otra capa.

## Cuándo puede ejecutarse

La ejecución ordinaria requiere que `submission-record.md` documente un estado significativo definido por [Application Lifecycle v1](../../career/application-lifecycle/README.md):

- `rejected`;
- `withdrawn`;
- `offer_received`;
- `offer_negotiation`;
- `accepted`;
- `declined`;
- `closed`.

También puede ejecutarse excepcionalmente si el timeline documenta de forma inequívoca que el proceso está materialmente concluido aunque falte una actualización administrativa. Esa excepción debe quedar visible en `lifecycle_implications`; no autoriza a inventar ni corregir el estado durante esta ejecución.

Si no existe un outcome o cierre material documentado, el generador se detiene sin crear el archivo. Silencio, demora, una impresión negativa o un riesgo abierto no prueban un outcome.

## Componentes

- [application-outcome.schema.md](application-outcome.schema.md): campos, categorías, valores y validación.
- [application-outcome-workflow.md](application-outcome-workflow.md): secuencia operativa y condiciones de parada.
- [application-outcome-prompt.md](application-outcome-prompt.md): prompt reutilizable para Codex o ChatGPT.
- [`templates/generated/application-outcome.template.md`](../../templates/generated/application-outcome.template.md): estructura completa del output.

## Fuentes y precedencia

Leer las fuentes factuales antes que los análisis, en este orden recomendado:

1. `submission-record.md`;
2. `recruiter-conversation.md`, si existe;
3. notas bajo `interviews/`, si existen;
4. `job-description.md`;
5. `job-intake.md`;
6. `application-plan.md`;
7. `risk-register.md`;
8. `target-profile-selection.md`;
9. `evidence-selection.md`;
10. debriefs bajo `generated/interview-debriefs/`, si existen;
11. `generated/opportunity-dossier.md`, si existe;
12. `generated/interview-prep.md`, si resulta relevante.

Los archivos generados aportan contexto analítico, nunca evidencia más fuerte que sus fuentes subyacentes. Los CVs generados o finales no son fuentes factuales y no se leen. No se explora conocimiento canónico salvo que el contrato o el usuario exijan validar una implicación concreta sobre el perfil; incluso entonces solo se propone una revisión, no se modifica conocimiento.

## Modelo de procedencia

- **`process_fact`:** hecho del proceso documentado directamente.
- **`explicit_feedback`:** feedback comunicado explícitamente por recruiter, intermediario, interviewer, empresa o cliente, con emisor y canal.
- **`candidate_impression`:** interpretación, sensación o autoevaluación del candidato.
- **`inference`:** hipótesis razonada con evidencia, límites, confianza y alternativa.
- **`unknown`:** aspecto no resuelto o sin soporte suficiente.
- **`lesson`:** takeaway práctico y acotado respaldado por hechos; no es una regla universal.
- **`experiment`:** acción futura diseñada para probar si una hipótesis o lección se generaliza.

## Causalidad y generalización

Un riesgo anterior solo se clasifica como causa confirmada cuando feedback posterior lo conecta explícitamente con el outcome. Que AWS, DevOps o low latency aparezcan en `risk-register.md` no demuestra que causaran un rechazo. La falta de mención tampoco los descarta: normalmente permanecen `unresolved`.

Un único rechazo, oferta, aceptación o comentario de recruiter tampoco define al candidato ni al mercado. Las implicaciones deben ser proporcionales a la evidencia. Ante una explicación plausible pero no confirmada, crear una hipótesis y, si aporta valor, un experimento que cambie pocas variables y observe una señal concreta.

## Casos no centrados en rechazo

Ante una oferta, el generador puede analizar fortalezas valoradas explícitamente, hipótesis sobre lo que funcionó, negociación y riesgos todavía abiertos. Una oferta no prueba que todas las decisiones de posicionamiento fueran correctas. Una aceptación no demuestra buen encaje a largo plazo, del mismo modo que un rechazo no demuestra debilidad general del candidato.

## Propuestas, no mutaciones

El outcome puede proponer revisiones futuras de:

- `submission-record.md` y lifecycle;
- `application-plan.md`;
- `risk-register.md`;
- perfiles objetivo;
- conocimiento canónico;
- estrategia de futuras candidaturas;
- Opportunity Dossier.

No modifica ninguno de esos destinos. Tampoco crea eventos, cambia estados, genera mensajes, CVs u otros outputs. Tras escribir y revisar `generated/application-outcome.md`, se detiene.

