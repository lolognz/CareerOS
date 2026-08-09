# Generador de debrief de entrevista

Interview Debrief transforma las notas brutas de una entrevista concreta en un análisis práctico de lo ocurrido, lo aprendido, los gaps observados y los siguientes pasos posibles. Conserva la diferencia entre recuerdo factual, impresión del candidato, inferencia e incertidumbre.

## Dos capas, dos responsabilidades

```text
<application-folder>/interviews/<note-stem>.md
<application-folder>/generated/interview-debriefs/<note-stem>.md
```

- La nota bajo `interviews/` es material fuente informado por el usuario. Puede ser incompleta, aproximada o contener impresiones.
- El debrief correspondiente bajo `generated/interview-debriefs/` es una interpretación reemplazable. Nunca es una fuente más fuerte que la nota y no reescribe lo que ocurrió.

Por ejemplo:

```text
interviews/2026-08-07-recruiter_screen.md
→ generated/interview-debriefs/2026-08-07-recruiter_screen.md
```

El nombre por defecto se deriva retirando únicamente la extensión de `source_interview_notes`. Si la fecha o el tipo son desconocidos, se conserva el stem estable elegido para la nota: no se inventan datos para renombrarla. Varias entrevistas de una candidatura producen varios debriefs coexistentes.

El generador trabaja sobre una única carpeta bajo `career/applications/<application-slug>/` o `examples/applications/<example-slug>/` y una única nota de entrevista explícitamente indicada.

## Tipos admitidos

- `recruiter_screen`
- `technical_interview`
- `hiring_manager`
- `leadership`
- `final`
- `unknown`

Si el tipo no puede demostrarse, usar `unknown`. Un recruiter screen no es una entrevista técnica y una conversación difícil no demuestra una evaluación negativa.

## Componentes

- [interview-debrief.schema.md](interview-debrief.schema.md): contrato, procedencia y validación.
- [interview-debrief-workflow.md](interview-debrief-workflow.md): captura, análisis, propuestas y condiciones de parada.
- [interview-debrief-prompt.md](interview-debrief-prompt.md): prompt directamente utilizable con Codex o ChatGPT.
- [`templates/applications/interview-notes.template.md`](../../templates/applications/interview-notes.template.md): estructura de captura bruta.
- [`templates/generated/interview-debrief.template.md`](../../templates/generated/interview-debrief.template.md): estructura del output analítico.

## Fuentes

Leer primero y por completo la nota indicada por `source_interview_notes`. Después puede leerse:

- `submission-record.md`;
- `job-description.md`;
- `recruiter-conversation.md`, si aporta contexto;
- `job-intake.md`;
- `application-plan.md`;
- `risk-register.md`;
- `target-profile-selection.md`;
- `evidence-selection.md`;
- `generated/opportunity-dossier.md`, si existe;
- `generated/interview-prep.md`, solo si existía antes de la entrevista.

Interview Prep permite comparar lo preparado con lo que se recuerda que ocurrió. No demuestra que una pregunta se formulara ni que una respuesta se usara. Opportunity Dossier permite comparar incógnitas previas con información comunicada en la entrevista. No es evidencia del candidato.

Los CVs finales o generados no son fuentes del debrief. Las entidades canónicas no se amplían ni se modifican desde este generador.

## Modelo de procedencia

- **`factual_recollection`:** recuerdo afirmado por el usuario sobre lo ocurrido, con la precisión disponible.
- **`candidate_impression`:** sensación o autoevaluación del candidato; no es feedback externo.
- **`interviewer_statement`:** algo atribuido al interlocutor; no queda verificado independientemente por haber sido dicho en entrevista.
- **`inference`:** lectura derivada, con base, confianza y alternativa posible.
- **`uncertainty`:** recuerdo parcial, aproximado, contradictorio o ausente.

Una frase como “creo que dijeron” conserva esa formulación. Solo usar comillas para palabras recordadas con suficiente exactitud; una paráfrasis no se convierte en cita.

## Principios

- No inventar preguntas, respuestas, feedback, reacciones, silencios, citas, decisiones ni siguientes etapas.
- No reconstruir la entrevista desde la oferta o desde `interview-prep.md`.
- Un tono positivo no es feedback de contratación; silencio no es rechazo.
- Una pregunta difícil no demuestra por sí sola una mala respuesta.
- La valoración del candidato permanece autoevaluación.
- El elogio de un entrevistador no crea un logro profesional.
- Un hecho profesional nuevo recordado por el candidato se registra como candidato a conocimiento canónico, pendiente de verificación; no se incorpora automáticamente.
- Mantener el análisis constructivo, concreto y proporcional a las notas.
- Si faltan detalles, usar `desconocido`; un debrief incompleto pero honesto sigue siendo útil.

## Propuestas, no mutaciones

El debrief puede identificar cambios que deberían evaluarse por separado en:

- `submission-record.md` y Application Lifecycle;
- `application-plan.md`;
- `risk-register.md`;
- Opportunity Dossier;
- Interview Prep de una siguiente ronda;
- conocimiento canónico.

Interview Debrief v1 no modifica ninguno de esos destinos. Tampoco envía follow-ups, genera otros materiales o cambia estados/eventos. Cada ejecución crea o reemplaza únicamente `generated/interview-debriefs/<note-stem>.md`, correspondiente a la nota indicada explícitamente, y se detiene. No existe un singleton `generated/interview-debrief.md` en v1.
