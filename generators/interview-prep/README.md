# Generador de preparación de entrevistas

Esta capa transforma el expediente analizado de una candidatura y su evidencia canónica seleccionada en material práctico para preparar una conversación real. El resultado es una salida desechable: no añade conocimiento, no modifica el análisis y no actualiza el lifecycle.

## Alcance de v1

El generador trabaja sobre una única carpeta bajo `career/applications/<application-slug>/` o `examples/applications/<example-slug>/` y crea exclusivamente:

```text
<application-folder>/generated/interview-prep.md
```

Tipos admitidos:

- `recruiter_screen`
- `technical_interview`
- `hiring_manager`
- `leadership`
- `final`
- `unknown`

El material incluye contexto, pitches, evidencia priorizada, historias STAR, manejo de gaps, preguntas probables, banco de respuestas, preguntas para la otra parte y un checklist final. Está pensado para una preparación útil de 30–60 minutos, no para producir un informe académico ni un guion que deba recitarse literalmente.

## Componentes

- [interview-prep.schema.md](interview-prep.schema.md): contrato y reglas de validación.
- [interview-prep-workflow.md](interview-prep-workflow.md): secuencia operativa y condiciones de parada.
- [interview-prep-prompt.md](interview-prep-prompt.md): prompt directamente utilizable con Codex o ChatGPT.
- [`templates/generated/interview-prep.template.md`](../../templates/generated/interview-prep.template.md): estructura práctica del output.

## Fuentes

Leer primero en el expediente:

- `job-description.md`
- `recruiter-conversation.md`, si existe
- `job-intake.md`
- `target-profile-selection.md`
- `evidence-selection.md`
- `application-plan.md`
- `risk-register.md`
- `submission-record.md`

Después, leer el perfil objetivo referenciado y únicamente las entidades canónicas citadas por `evidence-selection.md`, `target-profile-selection.md` y `application-plan.md`. No ampliar la búsqueda a entidades relacionadas no seleccionadas.

Los documentos del lifecycle sirven solo para interpretar el estado y la etapa. Los CV finales o generados no son fuentes factuales y no se leen salvo instrucción explícita; aun entonces solo pueden ayudar a mantener coherencia de presentación, no a demostrar claims.

## Principios

- Toda respuesta preparada debe apoyarse en el expediente o en una entidad canónica autorizada.
- La oferta describe la oportunidad; no demuestra experiencia del candidato.
- Las preguntas probables son hipótesis de preparación, no agenda confirmada.
- Distinguir siempre lo conocido, lo inferido, lo que debe preguntarse y lo que no debe afirmarse.
- Conservar títulos, fechas, atribución, alcance, seniority, métricas e incertidumbre.
- Convertir gaps en reconocimiento honesto, evidencia adyacente y pregunta de alcance; nunca ocultarlos ni rellenarlos.
- Distinguir colaboración con una función de ownership formal de esa función.
- Distinguir liderazgo técnico demostrado de un título formal de Tech Lead.
- Si falta experiencia directa en escala, latencia, cloud, Linux o plataforma, describir solo la exposición real y no transformar proximidad en dominio.
- Preparar respuestas breves, naturales y adaptables, no afirmaciones memorizadas sin contexto.

## Límites

El generador no envía mensajes, no genera CV, no cambia intake, plan, riesgos o `submission-record.md`, no crea eventos y no avanza estados del lifecycle. Tras escribir y revisar el único output permitido, se detiene.

