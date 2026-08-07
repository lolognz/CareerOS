# Esquema de Application Lifecycle

## Propósito

El esquema define la representación mínima y auditable del ciclo de una candidatura. `submission-record.md` es el registro operativo del expediente, no una fuente de hechos profesionales ni un output generado.

## Campos recomendados

| Campo | Descripción |
|---|---|
| `application_id` | ID estable con formato `application:<application-slug>`. |
| `application_folder` | Ruta relativa exacta del expediente. |
| `role` | Puesto conocido, con literalidad o incertidumbre preservada. |
| `company` | Empresa conocida; puede ser recruiter/intermediario cuando el cliente sea desconocido. |
| `final_client` | Cliente o empresa final, solo si está confirmado; `desconocido` en otro caso. |
| `recruiter_contact` | Nombre, organización y canal solo cuando consten. |
| `current_status` | Un único estado permitido del catálogo. |
| `status_as_of` | Fecha del evento que respalda el estado; `desconocida` si no consta. |
| `status_evidence` | Referencia breve al evento o evidencia explícita que soporta el estado. |
| `current_recommendation` | Decisión estratégica vigente o `no evaluada`; no equivale al estado. |
| `outputs_generated` | Outputs creados, con ruta, tipo y fecha conocida. |
| `outputs_sent` | Outputs realmente enviados, con fecha, canal y destinatario conocidos. |
| `events` | Timeline cronológico de eventos tipados. |
| `pending_questions` | Preguntas abiertas; `[]` si no existen. |
| `next_step` | Siguiente acción o espera concreta, responsable y etapa. |
| `outcome` | Resultado: `pending`, `rejected`, `withdrawn`, `accepted`, `declined` o `closed_without_outcome`. |
| `notes` | Hechos auxiliares e interpretaciones etiquetadas, sin duplicar el timeline. |

## Estructura de evento

Cada elemento de `events` contiene:

| Campo | Obligación | Descripción |
|---|---|---|
| `date` | Obligatorio | `YYYY-MM-DD` o `desconocida`; nunca una fecha estimada presentada como real. |
| `event_type` | Obligatorio | Uno de los valores definidos en `application-events.md`. |
| `channel` | Obligatorio | Canal conocido o `desconocido`; `interno` para acciones locales. |
| `contact` | Obligatorio | Persona/organización conocida, `ninguno` o `desconocido`. |
| `factual_detail` | Obligatorio | Qué ocurrió, sin causalidad o reacción inventada. |
| `status_after` | Obligatorio | Estado resultante respaldado, o `sin cambio`. |
| `output_affected` | Opcional | Ruta o tipo de output generado, finalizado o enviado. |
| `evidence` | Opcional | Mensaje, email, portal, archivo o nota que respalda el hecho. |
| `interpretation` | Opcional | Lectura explícitamente etiquetada; nunca sustituye el hecho. |
| `next_step` | Opcional | Acción confirmada o espera concreta derivada del evento. |

## Valores controlados

- `current_status`: uno de los estados de [application-statuses.md](application-statuses.md).
- `event_type`: uno de los eventos de [application-events.md](application-events.md).
- `outcome`: `pending`, `rejected`, `withdrawn`, `accepted`, `declined`, `closed_without_outcome`.

`pending` no significa feedback positivo ni continuidad asegurada. `closed_without_outcome` se usa solo cuando el expediente se cierra administrativamente sin rechazo, retirada, aceptación o declinación confirmados.

## Invariantes

- `current_status` debe corresponder al evento más reciente que cambió el estado.
- Toda transición debe estar permitida por el catálogo o justificarse como corrección explícita de un registro erróneo.
- Los eventos se conservan en orden cronológico; los hechos añadidos tarde mantienen su fecha real y pueden anotarse como registrados posteriormente.
- `outputs_generated` y `outputs_sent` no se deducen entre sí.
- `cv_finalized` no prueba exportación a PDF; una exportación puede anotarse en el evento sin equivaler a envío.
- `cv_sent` exige evidencia de envío, canal y destinatario cuando se conozcan.
- `interview_scheduled` exige fecha u otra confirmación explícita del acuerdo; una propuesta sin aceptar no basta.
- `interview_completed` identifica la clase de entrevista. Una conversación de recruiter no se reclasifica como técnica.
- `waiting_feedback` incluye contacto/organización esperada y etapa precedente.
- `rejected`, `accepted`, `declined` y `closed` requieren evidencia explícita; silencio no equivale a ninguno.
- Un cliente final descubierto sustituye `desconocido` en identificación y genera un evento fechado; no borra al intermediario.
- Interpretaciones e hipótesis se etiquetan y nunca cambian por sí solas estado u outcome.
- Las recomendaciones no se presentan como hechos ni como promesas de siguiente etapa.

## Validación mínima

- [ ] El estado pertenece al catálogo y tiene evidencia.
- [ ] La transición desde el estado anterior está permitida.
- [ ] El nuevo evento contiene todos los campos obligatorios de su tipo.
- [ ] El timeline preserva los eventos anteriores y la cronología.
- [ ] Los outputs generados y enviados están separados.
- [ ] El próximo paso nombra responsable y etapa cuando se espera respuesta.
- [ ] Outcome y estado no sobreafirman el resultado.
- [ ] Hechos, interpretaciones y recomendaciones son distinguibles.
- [ ] Solo se modificó el `submission-record.md` solicitado.

