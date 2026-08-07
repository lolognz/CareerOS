# Guía de `submission-record.md`

## Objetivo

`submission-record.md` conserva el historial operativo de una candidatura real: acciones, contactos, outputs, etapas y resultado. Debe poder responder qué ocurrió, qué se sabe, qué se recomienda y qué falta sin mezclar esas categorías.

## Estructura recomendada

```markdown
# Registro de candidatura — [empresa o intermediario] — [puesto]

## Identificación

- Application ID: `application:[slug]`
- Puesto: [conocido o desconocido]
- Empresa: [conocida o desconocida]
- Cliente final: [conocido o desconocido]
- Recruiter / intermediario: [conocido o desconocido]
- Contacto: [nombre, organización y canal conocidos]

## Estado actual

- Estado: [status estándar]
- Desde: [YYYY-MM-DD o desconocida]
- Evidencia: [evento que soporta el estado]

## Recomendación actual

- Recomendación: [decisión documentada o no evaluada]
- Fuente: [application-plan.md u otra decisión explícita]

## Outputs generados

- [fecha | tipo | ruta | estado de revisión]

## Outputs enviados

- [fecha | tipo/versión | canal | destinatario]

## Timeline / Eventos

| Fecha | Tipo | Canal | Contacto | Hecho | Estado posterior |
|---|---|---|---|---|---|
| [fecha] | [event_type] | [canal] | [contacto] | [detalle factual] | [status o sin cambio] |

## Preguntas pendientes

- [pregunta y responsable esperado]

## Próximo paso

- [acción o espera concreta, responsable y etapa]

## Outcome

- Outcome: [pending / rejected / withdrawn / accepted / declined / closed_without_outcome]
- Evidencia: [evento o pendiente]

## Notas

- Hecho: [dato auxiliar verificable que no duplica el timeline].
- Interpretación: [hipótesis etiquetada y su límite].
```

Eliminar placeholders y usar `[]`, `ninguno` o `desconocido` según corresponda. No crear secciones llenas de suposiciones.

## Reglas de actualización

1. Leer el registro completo antes de editar.
2. Identificar el hecho nuevo y escoger un `event_type` estándar.
3. Añadir una fila o entrada al timeline; no borrar ni reescribir eventos válidos.
4. Mantener orden cronológico. Si un hecho antiguo se registra tarde, insertarlo por su fecha y anotar la fecha de registro solo si aporta claridad.
5. Cambiar el estado únicamente si el evento soporta una transición permitida.
6. Actualizar el próximo paso con sujeto y etapa: por ejemplo, “Esperar feedback de recruiter después del recruiter screen”.
7. Actualizar outcome únicamente ante evidencia explícita.
8. Cambiar identificación cuando se confirme empresa o cliente final y registrar ese descubrimiento como evento fechado.
9. Conservar hipótesis bajo `Interpretación`; nunca presentarlas como causa confirmada.
10. Modificar solo `submission-record.md` y detenerse.

## Separaciones obligatorias

- **Hechos:** comunicaciones, acciones y resultados observables.
- **Interpretaciones:** lecturas o hipótesis etiquetadas, sin efecto automático sobre estado.
- **Recomendaciones:** decisiones estratégicas provenientes del plan o del usuario.
- **Outputs generados:** archivos creados localmente; no implican revisión o envío.
- **Outputs finales/exportados:** versiones preparadas o PDF exportado; no implican envío.
- **Outputs enviados:** materiales transmitidos con evidencia de fecha, canal y destino.

## Casos frecuentes

- “El recruiter pidió el CV” → evento `cv_requested`, estado `cv_requested`; no añadirlo a outputs enviados.
- “Se generó `generated/cv.md`” → `cv_generated`; no afirmar que está finalizado.
- “Se crearon Markdown/HTML finales y se exportó un PDF” → `cv_finalized` y detalle de exportación; no usar `cv_sent`.
- “Se envió el PDF por email” → `cv_sent` y entrada en outputs enviados.
- “Hablé con el recruiter” → `interview_completed` + `recruiter_screen_done` solo si se confirma que fue un recruiter screen; no marcar entrevista técnica.
- “Nos responderán después de la entrevista” → `waiting_feedback`, indicando quién responde y tras qué entrevista.
- “Ahora sabemos quién es el cliente final” → evento `other`, actualización de identificación y estado sin cambio si la etapa no varía.
- “No contestan” → mantener la espera o próximo paso; no inferir `rejected` ni `closed`.

## Checklist

- [ ] El evento nuevo es factual y tiene fecha real o `desconocida`.
- [ ] El estado está respaldado y la transición es válida.
- [ ] Se conservó todo el historial previo.
- [ ] Petición, generación, finalización/exportación y envío no se confundieron.
- [ ] El tipo de entrevista es explícito.
- [ ] La espera identifica contacto y etapa.
- [ ] Rechazo, oferta, aceptación, declinación y cierre tienen evidencia.
- [ ] Outcome no supera lo conocido.
- [ ] No se modificó ningún otro archivo.

