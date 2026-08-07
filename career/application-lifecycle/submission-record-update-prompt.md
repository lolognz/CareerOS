# Prompt reutilizable: actualizar `submission-record.md`

Copia este prompt en Codex o ChatGPT y sustituye los parámetros. Una ejecución procesa un evento y modifica un único archivo.

```text
Actualiza el lifecycle de una candidatura real de CareerOS.

Parámetros:
- application_folder: [career/applications/<application-slug>]
- event_type: [tipo permitido de application-events.md]
- event_date: [YYYY-MM-DD o desconocida]
- channel: [canal conocido, interno o desconocido]
- contact: [persona/organización conocida, ninguno o desconocido]
- output_affected: [ruta/tipo conocido o ninguno]
- factual_detail: [hecho ocurrido, sin interpretación]
- new_status: [estado estándar respaldado o sin cambio]
- outcome: [pending / rejected / withdrawn / accepted / declined / closed_without_outcome]
- next_step: [acción o espera concreta, o ninguno]

Lee primero:
- career/application-lifecycle/README.md
- career/application-lifecycle/application-lifecycle.schema.md
- career/application-lifecycle/application-statuses.md
- career/application-lifecycle/application-events.md
- career/application-lifecycle/submission-record-guidelines.md
- application_folder/submission-record.md

Después:

1. Confirma que application_folder existe, pertenece a una única candidatura y contiene submission-record.md.
2. Valida event_type, sus campos requeridos, new_status y outcome contra el lifecycle. Si falta evidencia para marcar algo como enviado, programado, completado, rechazado, retirado, ofrecido, aceptado, declinado o cerrado, no lo infieras: conserva el estado/outcome soportado y señala la incertidumbre.
3. Lee el registro completo y preserva todos los hechos y eventos anteriores.
4. Añade al timeline un único evento con event_date, event_type, channel, contact, factual_detail, output_affected cuando corresponda y estado posterior. Mantén la cronología; no inventes una fecha para ordenar.
5. Actualiza el estado actual solo si factual_detail y la evidencia proporcionada soportan new_status y la transición está permitida. Un evento puede dejar el estado sin cambio.
6. Si el evento confirma por primera vez empresa o cliente final, actualiza identificación y registra el descubrimiento en el evento; conserva recruiter o intermediario por separado.
7. Actualiza outputs generados o enviados solo según el evento. Una petición de CV no es envío; generación, finalización, exportación y envío son hechos distintos.
8. Si el evento es interview_scheduled o interview_completed, conserva el tipo de entrevista explícito. No conviertas una conversación con recruiter en entrevista técnica.
9. Si new_status es waiting_feedback, identifica en el estado o próximo paso quién debe responder y después de qué etapa. No inventes plazo.
10. Actualiza next_step con el valor proporcionado cuando esté respaldado. No conviertas una recomendación en acuerdo externo.
11. Actualiza outcome solo con evidencia explícita. Silencio o espera conservan outcome: pending.
12. Mantén separados hechos, interpretaciones, recomendaciones, outputs generados y outputs enviados. No añadas interpretaciones que no estén en factual_detail.
13. Modifica únicamente application_folder/submission-record.md. No modifiques otros documentos, outputs, conocimiento canónico, perfiles objetivo, scripts ni otras candidaturas.
14. Revisa el diff del único archivo y detente. No generes materiales, no envíes nada y no hagas commit.
```

