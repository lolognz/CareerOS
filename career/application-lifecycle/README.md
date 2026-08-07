# Application Lifecycle v1

Application Lifecycle define un lenguaje común para registrar la evolución de candidaturas reales en CareerOS. Estandariza estados, eventos, transiciones y actualizaciones de `submission-record.md` sin convertir el historial de candidatura en conocimiento profesional canónico.

## Alcance

Esta capa se aplica a expedientes bajo `career/applications/`. Describe qué ocurrió, qué se sabe ahora y qué acción sigue. No analiza ofertas, no selecciona evidencia, no genera materiales y no modifica outputs.

Sus componentes son:

- [application-lifecycle.schema.md](application-lifecycle.schema.md): contrato del registro y reglas de validación.
- [application-statuses.md](application-statuses.md): catálogo de estados y transiciones permitidas.
- [application-events.md](application-events.md): catálogo de eventos observables.
- [submission-record-guidelines.md](submission-record-guidelines.md): estructura recomendada de `submission-record.md`.
- [submission-record-update-prompt.md](submission-record-update-prompt.md): prompt para actualizar un único registro.

## Principios

- Un estado resume la situación actual; un evento conserva un hecho fechado.
- El timeline es acumulativo: actualizar el estado no borra la ruta seguida.
- Hecho, interpretación, recomendación, output generado y output enviado son categorías distintas.
- Un cambio de estado exige evidencia explícita registrada en un evento.
- Generar, finalizar, exportar y enviar son acciones distintas.
- Pedir un CV no prueba que se haya enviado.
- Una conversación con recruiter no es una entrevista técnica.
- `waiting_feedback` identifica quién debe responder y después de qué etapa.
- La identidad de empresa o cliente final puede aclararse después; se actualiza en identificación y se conserva como evento fechado.
- Lo desconocido permanece desconocido. No se infieren fechas, canales, respuestas, resultados ni siguientes pasos.

## Uso práctico

1. Identificar un hecho nuevo y escoger su `event_type`.
2. Verificar la evidencia y la fecha disponibles.
3. Añadir el evento sin reescribir eventos anteriores.
4. Cambiar `current_status` solo si el hecho soporta una transición permitida.
5. Actualizar outputs, preguntas, próximo paso y outcome solo cuando corresponda.
6. Detenerse después de modificar `submission-record.md`.

Los registros históricos pueden conservar formatos anteriores. La estructura recomendada se adopta al crear registros nuevos o cuando exista una migración explícita; esta capa no autoriza migraciones automáticas.

La preparación creada por [Interview Prep Generator v1](../../generators/interview-prep/README.md) es un output desechable bajo `generated/`, no un estado ni un evento del lifecycle. Generarla no confirma una entrevista ni avanza la candidatura.
