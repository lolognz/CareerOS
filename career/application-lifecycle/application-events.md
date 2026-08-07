# Eventos estándar de candidatura

Todos los eventos requieren `date`, `event_type`, `channel`, `contact`, `factual_detail` y `status_after`. Los campos opcionales comunes son `output_affected`, `evidence`, `interpretation` y `next_step`. Los ejemplos son genéricos y no aportan hechos a ninguna candidatura real.

## Captura y análisis

### `offer_detected`

- **Requeridos:** campos comunes; referencia identificable a la oportunidad.
- **Opcionales:** URL, plataforma, empresa publicada, puesto.
- **Ejemplo:** `2026-01-10 | offer_detected | portal | ninguno | Oferta de Backend Engineer detectada. | detected`.
- **No inventar:** empresa oculta, cliente final, vigencia, encaje o intención de aplicar.

### `application_scaffolded`

- **Requeridos:** campos comunes; ruta creada.
- **Opcionales:** comando o versión del scaffold.
- **Ejemplo:** `2026-01-10 | application_scaffolded | interno | ninguno | Creado el expediente career/applications/2026-01-example-backend. | scaffolded`.
- **No inventar:** captura de oferta, análisis o decisión.

### `job_description_captured`

- **Requeridos:** campos comunes; confirmación de captura.
- **Opcionales:** URL, advertencia de truncamiento o formato.
- **Ejemplo:** `2026-01-10 | job_description_captured | interno | ninguno | Texto original preservado en job-description.md. | intake_pending`.
- **No inventar:** contenido ausente, requisitos o metadatos desconocidos.

### `intake_completed`

- **Requeridos:** campos comunes; referencia a los documentos completados.
- **Opcionales:** recomendación y blockers registrados.
- **Ejemplo:** `2026-01-11 | intake_completed | interno | ninguno | Intake y plan revisados; recomendación: aplicar tras aclarar. | intake_completed`.
- **No inventar:** contacto, aprobación o autorización para outputs no incluidos en el plan.

## Contacto y materiales

### `recruiter_contact_received`

- **Requeridos:** campos comunes; contenido factual del contacto.
- **Opcionales:** organización, puesto del contacto, preguntas recibidas.
- **Ejemplo:** `2026-01-12 | recruiter_contact_received | LinkedIn | recruiter de Example Recruiting | Preguntó por disponibilidad para conversar. | sin cambio`.
- **No inventar:** interés firme, entrevista confirmada, cliente final o avance.

### `recruiter_message_sent`

- **Requeridos:** campos comunes; destinatario y naturaleza del mensaje.
- **Opcionales:** `output_affected`, asunto o preguntas incluidas.
- **Ejemplo:** `2026-01-12 | recruiter_message_sent | LinkedIn | recruiter de Example Recruiting | Enviado mensaje con dos preguntas de aclaración. | clarification_sent`.
- **No inventar:** lectura, recepción, respuesta o acuerdo.

### `clarification_received`

- **Requeridos:** campos comunes; respuesta factual recibida.
- **Opcionales:** preguntas resueltas, preguntas aún pendientes, revisión recomendada.
- **Ejemplo:** `2026-01-13 | clarification_received | email | recruiter | Confirmó modalidad remota; salario no indicado. | intake_completed`.
- **No inventar:** condiciones no mencionadas, fit o decisión de continuar.

### `cv_requested`

- **Requeridos:** campos comunes; petición explícita y solicitante.
- **Opcionales:** formato, idioma o plazo pedido.
- **Ejemplo:** `2026-01-13 | cv_requested | email | recruiter | Solicitó el CV en inglés. | cv_requested`.
- **No inventar:** envío, revisión, entrevista o aceptación.

### `cv_generated`

- **Requeridos:** campos comunes; ruta del CV generado en `output_affected`.
- **Opcionales:** idioma, estado de revisión.
- **Ejemplo:** `2026-01-13 | cv_generated | interno | ninguno | Generado generated/cv.md. | cv_generated`.
- **No inventar:** finalización, PDF o envío.

### `cv_finalized`

- **Requeridos:** campos comunes; rutas finales en `output_affected`.
- **Opcionales:** activo de foto y exportación PDF si ocurrió realmente.
- **Ejemplo:** `2026-01-14 | cv_finalized | interno | ninguno | Creados y revisados final/cv-send-en.md y final/cv-print-en.html. | cv_finalized`.
- **No inventar:** PDF exportado, entrega o recepción.

### `cv_sent`

- **Requeridos:** campos comunes; destinatario/portal, canal y versión enviada.
- **Opcionales:** confirmación técnica de carga, nombre del archivo PDF.
- **Ejemplo:** `2026-01-14 | cv_sent | email | recruiter | Enviado el PDF exportado desde final/cv-print-en.html. | cv_sent`.
- **No inventar:** lectura, feedback, entrevista o resultado.

## Entrevistas y feedback

### `interview_scheduled`

- **Requeridos:** campos comunes; tipo de entrevista y cita confirmada.
- **Opcionales:** fecha/hora, zona horaria, participantes, enlace si constan.
- **Ejemplo:** `2026-01-15 | interview_scheduled | email | recruiter | Recruiter screen confirmado para 2026-01-17 a las 10:00 CET. | recruiter_screen_scheduled`.
- **No inventar:** carácter técnico, asistentes, contenido o resultado.

### `interview_completed`

- **Requeridos:** campos comunes; tipo, fecha y confirmación de realización.
- **Opcionales:** participantes y hechos expresamente tratados.
- **Ejemplo:** `2026-01-17 | interview_completed | videollamada | recruiter | Recruiter screen completado. | recruiter_screen_done`.
- **No inventar:** feedback, evaluación, requisitos o siguiente fase.

### `feedback_received`

- **Requeridos:** campos comunes; feedback literal o paráfrasis fiel y emisor.
- **Opcionales:** siguiente etapa confirmada, plazo o preguntas nuevas.
- **Ejemplo:** `2026-01-18 | feedback_received | email | recruiter | Confirmó entrevista técnica para 2026-01-20 a las 11:00 CET. | technical_interview_scheduled`.
- **No inventar:** razones, valoración adicional, participantes, contenido técnico u oferta.

### `rejection_received`

- **Requeridos:** campos comunes; comunicación o estado explícito de rechazo.
- **Opcionales:** motivo solo si fue comunicado.
- **Ejemplo:** `2026-01-20 | rejection_received | portal | empresa | El portal muestra que la candidatura no continúa. | rejected`.
- **No inventar:** causa, comparación con candidatos o automatización del rechazo.

## Oferta y cierre

### `offer_received`

- **Requeridos:** campos comunes; emisor y existencia de la oferta.
- **Opcionales:** condiciones explícitas, formato verbal/escrito, vigencia.
- **Ejemplo:** `2026-01-25 | offer_received | email | hiring manager | Recibida oferta escrita; condiciones registradas según el documento. | offer_received`.
- **No inventar:** salario ausente, acuerdo, firma o aceptación.

### `offer_accepted`

- **Requeridos:** campos comunes; aceptación explícita y oferta afectada.
- **Opcionales:** documento, fecha prevista de incorporación si consta.
- **Ejemplo:** `2026-01-27 | offer_accepted | email | empresa | Aceptación de la oferta comunicada por email. | accepted`.
- **No inventar:** contrato firmado, onboarding o cierre de otros procesos.

### `offer_declined`

- **Requeridos:** campos comunes; declinación explícita.
- **Opcionales:** motivo solo si el candidato decidió registrarlo.
- **Ejemplo:** `2026-01-27 | offer_declined | email | empresa | Oferta declinada por email. | declined`.
- **No inventar:** contraoferta, reacción o motivo.

### `application_withdrawn`

- **Requeridos:** campos comunes; decisión explícita de retirada.
- **Opcionales:** comunicación externa y motivo documentado.
- **Ejemplo:** `2026-01-19 | application_withdrawn | email | recruiter | Retirada de la candidatura comunicada. | withdrawn`.
- **No inventar:** rechazo empresarial, otra oferta o razón no declarada.

### `application_closed`

- **Requeridos:** campos comunes; motivo y outcome conocido.
- **Opcionales:** referencia al evento terminal previo.
- **Ejemplo:** `2026-01-21 | application_closed | interno | ninguno | Expediente cerrado después del rechazo registrado. | closed`.
- **No inventar:** outcome por silencio ni causa del resultado.

### `other`

- **Requeridos:** campos comunes; descripción suficientemente precisa para no confundirlo con un evento estándar.
- **Opcionales:** evidencia y relación con un evento anterior.
- **Ejemplo:** `2026-01-16 | other | email | recruiter | Cliente final identificado y actualizado en el registro. | sin cambio`.
- **No inventar:** cambio de etapa; usar un tipo estándar cuando corresponda.

## Elección del tipo

- Usar `recruiter_contact_received` para un contacto entrante general; `clarification_received` o `feedback_received` cuando su función sea inequívoca.
- Usar `interview_scheduled` y `interview_completed` con el tipo de entrevista en el detalle y un estado consistente.
- Registrar la identificación posterior del cliente final como `other`, con fecha y fuente, sin borrar al recruiter/intermediario.
- Un evento puede usar `status_after: sin cambio` cuando aporta un hecho sin alterar la fase actual.
