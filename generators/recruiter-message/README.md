# Generador de mensajes a recruiters

Esta capa define cómo convertir el intake ya completado de una candidatura en un mensaje breve, trazable y revisable. El mensaje es una salida desechable: no añade conocimiento, no corrige el intake y no se convierte en fuente de verdad.

## Alcance de v1

El generador trabaja sobre una única carpeta bajo `career/applications/<application-slug>/` o `examples/applications/<example-slug>/`. Lee los documentos del expediente, selecciona un tipo de mensaje y crea:

```text
<application-folder>/generated/recruiter-message.md
```

El archivo puede incluir un mensaje principal y entre dos y tres variantes cuando aporten una diferencia útil de canal, tono o énfasis. No genera CV, carta de presentación, preparación de entrevista ni cambios en LinkedIn.

## Componentes

- [recruiter-message.schema.md](recruiter-message.schema.md): contrato del output y reglas de validación.
- [recruiter-message-prompt.md](recruiter-message-prompt.md): prompt directamente utilizable con Codex o ChatGPT.
- [recruiter-message-workflow.md](recruiter-message-workflow.md): secuencia operativa, revisión y condiciones de parada.
- [`templates/generated/recruiter-message.template.md`](../../templates/generated/recruiter-message.template.md): estructura del archivo generado.

## Tipos de mensaje

| Tipo | Cuándo usarlo | Objetivo |
|---|---|---|
| `clarification-first` | La recomendación es `aplicar tras aclarar` o quedan incógnitas materiales. | Mostrar interés y encaje relevante, y formular de dos a cuatro preguntas decisivas sin lanzar todavía un pitch extenso. |
| `apply` | El encaje permite aplicar con la evidencia disponible. | Presentar brevemente al candidato, destacar de dos a tres señales respaldadas y pedir siguientes pasos o compartir disponibilidad solo si consta. |
| `follow-up` | Ya hubo una interacción previa documentada. | Retomar el contacto con cortesía, reiterar interés y añadir como máximo una aclaración o dato de disponibilidad respaldado. |
| `polite-decline` | La oportunidad no encaja o la decisión documentada es no continuar. | Agradecer, rechazar con claridad y dejar la puerta abierta únicamente cuando sea coherente y esté respaldado. |

Si el tipo se proporciona explícitamente, debe comprobarse que no contradiga la decisión ni el estado documentado. Si no se proporciona, el generador lo elige conforme al workflow.

## Principios de generación

- Usar únicamente hechos y límites presentes en el expediente y en la evidencia canónica que este referencia.
- Dar prioridad a `evidence-selection.md`, `risk-register.md` y `application-plan.md` para decidir qué afirmar, evitar o preguntar.
- No convertir requisitos de la oferta en experiencia del candidato.
- No inventar experiencia, tecnologías, métricas, motivación, salario, disponibilidad, interés ni interacciones previas.
- Mantener los gaps como gaps: pueden originar una pregunta, nunca un claim.
- Preservar atribución, cronología, alcance, seniority e incertidumbre.
- Usar por defecto un tono profesional, claro, breve y humano.
- Elegir el idioma según la oferta y el contexto documentado del recruiter; si no puede determinarse con seguridad, dejar la decisión en `uncertainty` y detenerse.
- Mantener el mensaje apto para un contacto inicial por LinkedIn o para la apertura de un email; no escribir una carta larga.

El fixture `examples/applications/job-intake-knowmad-mood-senior-backend-java/` puede utilizarse para probar la selección `clarification-first`, pero no forma parte del generador ni fija su contenido.
