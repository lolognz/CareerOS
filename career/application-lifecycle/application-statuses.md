# Estados estándar de candidatura

Un estado describe la mejor lectura factual del momento actual. No sustituye el timeline ni expresa probabilidad de éxito. Los siguientes estados son los únicos valores estándar de v1.

## Preparación

### `detected`

- **Significado:** se ha identificado una oportunidad, todavía sin expediente.
- **Cuándo usarlo:** existe una oferta o contacto identificable que merece triage.
- **Evidencia requerida:** URL, captura, mensaje o nota fechada de detección.
- **Siguientes permitidos:** `scaffolded`, `closed`.
- **No asumir:** interés, elegibilidad, aplicación iniciada o contacto con la empresa.

### `scaffolded`

- **Significado:** se creó la carpeta de candidatura.
- **Cuándo usarlo:** el scaffold existe, aunque la oferta aún no esté capturada.
- **Evidencia requerida:** ruta creada y fecha conocida de creación.
- **Siguientes permitidos:** `intake_pending`, `closed`.
- **No asumir:** oferta preservada, intake realizado o decisión de aplicar.

### `intake_pending`

- **Significado:** la oferta está preservada o el expediente está listo para análisis, pero el intake no terminó.
- **Cuándo usarlo:** después de capturar la descripción y antes de completar Job Intake.
- **Evidencia requerida:** `job-description.md` capturado o validación estructural equivalente.
- **Siguientes permitidos:** `intake_completed`, `closed`.
- **No asumir:** encaje, perfil seleccionado, recomendación o outputs autorizados.

### `intake_completed`

- **Significado:** Job Intake y la recomendación actual están completos.
- **Cuándo usarlo:** los documentos de análisis fueron completados y revisados.
- **Evidencia requerida:** intake, selección, plan y riesgos coherentes.
- **Siguientes permitidos:** `waiting_clarification`, `clarification_sent`, `cv_requested`, `cv_generated`, `withdrawn`, `closed`.
- **No asumir:** que se aplicará, que existe contacto o que un material fue enviado.

## Aclaraciones y CV

### `waiting_clarification`

- **Significado:** falta una respuesta concreta antes de decidir o continuar.
- **Cuándo usarlo:** hay preguntas pendientes, pero todavía no consta su envío, o se espera una aclaración ya solicitada por otro medio documentado.
- **Evidencia requerida:** preguntas abiertas y responsable esperado; si ya se enviaron, evento de envío.
- **Siguientes permitidos:** `clarification_sent`, `intake_completed`, `cv_requested`, `rejected`, `withdrawn`, `closed`.
- **No asumir:** que la pregunta fue enviada, que habrá respuesta o que la candidatura avanza.

### `clarification_sent`

- **Significado:** se enviaron preguntas o un mensaje de aclaración.
- **Cuándo usarlo:** existe evidencia del envío y se espera respuesta.
- **Evidencia requerida:** fecha, canal, destinatario y contenido o referencia al mensaje enviado.
- **Siguientes permitidos:** `waiting_clarification`, `intake_completed`, `cv_requested`, `recruiter_screen_scheduled`, `rejected`, `withdrawn`, `closed`.
- **No asumir:** recepción, respuesta, interés o invitación a entrevista.

### `cv_requested`

- **Significado:** un contacto pidió el CV.
- **Cuándo usarlo:** la solicitud es explícita y el CV aún no consta como enviado.
- **Evidencia requerida:** petición, fecha, canal y contacto conocidos.
- **Siguientes permitidos:** `cv_generated`, `cv_finalized`, `cv_sent`, `withdrawn`, `closed`.
- **No asumir:** que el CV ya existe, está finalizado, exportado o enviado.

### `cv_generated`

- **Significado:** existe `generated/cv.md` para la candidatura.
- **Cuándo usarlo:** CV Generator terminó, pero no consta una versión final enviada.
- **Evidencia requerida:** ruta del output generado y fecha conocida.
- **Siguientes permitidos:** `cv_finalized`, `cv_sent`, `withdrawn`, `closed`.
- **No asumir:** revisión, finalización, PDF, entrega o recepción.

### `cv_finalized`

- **Significado:** existe una versión candidata limpia y lista para exportar o enviar.
- **Cuándo usarlo:** CV Finalizer terminó y los artefactos finales fueron revisados.
- **Evidencia requerida:** rutas finales y revisión; anotar por separado si se exportó PDF.
- **Siguientes permitidos:** `cv_sent`, `withdrawn`, `closed`.
- **No asumir:** que el PDF fue exportado o que el CV fue enviado.

### `cv_sent`

- **Significado:** el CV fue transmitido al recruiter, empresa o portal.
- **Cuándo usarlo:** existe evidencia explícita de envío o presentación.
- **Evidencia requerida:** fecha, canal, destinatario/portal y archivo o versión enviada cuando consten.
- **Siguientes permitidos:** `recruiter_screen_scheduled`, `waiting_feedback`, `technical_interview_scheduled`, `rejected`, `offer_received`, `withdrawn`, `closed`.
- **No asumir:** recepción humana, revisión, entrevista o feedback positivo.

## Entrevistas y espera

### `recruiter_screen_scheduled`

- **Significado:** hay una conversación inicial con recruiter confirmada.
- **Cuándo usarlo:** fecha/hora o acuerdo de celebración constan explícitamente.
- **Evidencia requerida:** confirmación, contacto, canal y momento conocido.
- **Siguientes permitidos:** `recruiter_screen_done`, `rejected`, `withdrawn`, `closed`.
- **No asumir:** que ya ocurrió, que es técnica o que garantiza otra fase.

### `recruiter_screen_done`

- **Significado:** terminó la conversación inicial con recruiter.
- **Cuándo usarlo:** la conversación ocurrió; registrar solo hechos conocidos.
- **Evidencia requerida:** fecha, contacto y confirmación de realización.
- **Siguientes permitidos:** `cv_requested`, `technical_interview_scheduled`, `waiting_feedback`, `rejected`, `offer_received`, `withdrawn`, `closed`.
- **No asumir:** feedback, aprobación, requisitos técnicos o siguiente fase.

### `technical_interview_scheduled`

- **Significado:** hay una entrevista técnica confirmada.
- **Cuándo usarlo:** el carácter técnico y la cita constan explícitamente.
- **Evidencia requerida:** confirmación, fecha/hora o acuerdo, contacto y etapa técnica.
- **Siguientes permitidos:** `technical_interview_done`, `rejected`, `withdrawn`, `closed`.
- **No asumir:** contenido, evaluadores, dificultad, resultado o asistencia completada.

### `technical_interview_done`

- **Significado:** una entrevista técnica se completó.
- **Cuándo usarlo:** la sesión técnica ocurrió.
- **Evidencia requerida:** fecha y confirmación de realización y naturaleza técnica.
- **Siguientes permitidos:** `waiting_feedback`, `technical_interview_scheduled`, `rejected`, `offer_received`, `withdrawn`, `closed`.
- **No asumir:** evaluación, aprobación, oferta o ausencia de más rondas.

### `waiting_feedback`

- **Significado:** la próxima acción corresponde a otra persona u organización después de una etapa identificada.
- **Cuándo usarlo:** se espera respuesta tras envío, aclaración o entrevista.
- **Evidencia requerida:** contacto/organización esperada y etapa precedente; plazo solo si fue comunicado.
- **Siguientes permitidos:** `intake_completed`, `cv_requested`, `recruiter_screen_scheduled`, `technical_interview_scheduled`, `rejected`, `offer_received`, `withdrawn`, `closed`.
- **No asumir:** plazo, silencio como rechazo, feedback positivo o siguiente ronda.

## Resultados y cierre

### `rejected`

- **Significado:** la empresa o intermediario comunicó que la candidatura no continúa.
- **Cuándo usarlo:** existe rechazo explícito o estado inequívoco en el portal.
- **Evidencia requerida:** comunicación o estado fechado.
- **Siguientes permitidos:** `closed`.
- **No asumir:** motivo, valoración, persona decisora o imposibilidad de futuras oportunidades.

### `withdrawn`

- **Significado:** el candidato retiró la candidatura.
- **Cuándo usarlo:** la decisión o comunicación de retirada está documentada.
- **Evidencia requerida:** decisión explícita y, si se comunicó, fecha/canal/destinatario.
- **Siguientes permitidos:** `closed`.
- **No asumir:** rechazo, aceptación de otra oferta o motivo no declarado.

### `offer_received`

- **Significado:** se recibió una propuesta explícita de incorporación.
- **Cuándo usarlo:** existe oferta verbal o escrita identificable; conservar su grado de formalidad.
- **Evidencia requerida:** comunicación de oferta, fecha, emisor y condiciones conocidas sin completar huecos.
- **Siguientes permitidos:** `offer_negotiation`, `accepted`, `declined`, `withdrawn`, `closed`.
- **No asumir:** acuerdo, condiciones finales, contrato firmado o aceptación.

### `offer_negotiation`

- **Significado:** existen conversaciones activas sobre condiciones de la oferta.
- **Cuándo usarlo:** alguna parte propuso o discutió cambios concretos.
- **Evidencia requerida:** intercambio documentado y condiciones tratadas solo cuando consten.
- **Siguientes permitidos:** `accepted`, `declined`, `withdrawn`, `closed`.
- **No asumir:** mejora, acuerdo salarial, aceptación o firma.

### `accepted`

- **Significado:** el candidato aceptó explícitamente la oferta.
- **Cuándo usarlo:** la aceptación fue comunicada o firmada.
- **Evidencia requerida:** fecha, canal/documento y oferta aceptada.
- **Siguientes permitidos:** `closed`.
- **No asumir:** inicio efectivo, onboarding completado o cierre de otras candidaturas.

### `declined`

- **Significado:** el candidato rechazó explícitamente una oferta recibida.
- **Cuándo usarlo:** la declinación fue decidida y, cuando corresponda, comunicada.
- **Evidencia requerida:** decisión explícita y comunicación si existe.
- **Siguientes permitidos:** `closed`.
- **No asumir:** retirada anterior a una oferta, rechazo empresarial o motivo no indicado.

### `closed`

- **Significado:** no quedan acciones activas en el expediente.
- **Cuándo usarlo:** después de un resultado terminal o de un cierre administrativo explícito.
- **Evidencia requerida:** motivo de cierre y fecha; outcome separado.
- **Siguientes permitidos:** ninguno en v1.
- **No asumir:** rechazo por silencio, outcome concreto o eliminación del historial.

## Reglas de transición

- No es obligatorio recorrer todos los estados: una candidatura puede saltar fases cuando un hecho explícito lo justifica.
- Un evento puede no cambiar el estado; por ejemplo, identificar al cliente final mientras se sigue esperando feedback.
- Las repeticiones de entrevista se modelan con nuevos eventos y pueden volver a un estado `*_scheduled` permitido.
- Para corregir un estado históricamente erróneo, registrar la corrección y su evidencia; no fabricar una transición intermedia.
- `closed` es terminal. Reabrir un expediente requiere una decisión explícita y una nueva versión del modelo o un expediente nuevo.

