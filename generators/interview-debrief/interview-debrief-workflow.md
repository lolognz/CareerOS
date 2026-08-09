# Workflow del generador de debrief de entrevista

## Objetivo operativo

Preservar el recuerdo bruto de una entrevista y producir un análisis útil para aprender y decidir el siguiente paso, sin reconstruir lo desconocido ni aplicar cambios a otras capas.

## 1. Captura bruta previa

Crear manualmente una nota a partir de `templates/applications/interview-notes.template.md` en:

```text
<application-folder>/interviews/<note-stem>.md
```

Usar preferentemente `<YYYY-MM-DD>-<interview-type>` cuando ambos datos sean conocidos. Si alguno no consta, elegir un stem estable que no lo invente y conservarlo en todas las capas.

- Capturar pronto, conservando el orden recordado cuando sea posible.
- Separar palabras recordadas, paráfrasis, impresiones e incertidumbre.
- No pulir la nota para que la entrevista parezca más coherente.
- No completar desde la oferta ni desde Interview Prep.
- Usar `desconocido` o “no recuerdo” frente a una reconstrucción plausible.

La creación y edición humana de esta fuente queda fuera de la ejecución del generador. El generador nunca reescribe la nota.

## 2. Precondiciones

- Recibir una carpeta única bajo `career/applications/` o `examples/applications/`.
- Recibir una ruta `source_interview_notes` existente dentro de `interviews/` de ese expediente.
- Recibir un `interview_type` permitido y comprobarlo contra la nota; usar `unknown` si no puede confirmarse.
- Recibir `language`; `output_path` es opcional y por defecto se deriva como `generated/interview-debriefs/<note-stem>.md`.
- Si se proporciona `output_path`, confirmar que permanece dentro de `generated/interview-debriefs/` del mismo expediente y que corresponde inequívocamente a la nota indicada.
- Confirmar `application_id` y revisar el debrief correspondiente existente antes de reemplazarlo, especialmente si contiene cambios locales.
- Rechazar `generated/interview-debrief.md`: v1 no admite un output singleton.

Notas incompletas no bloquean el debrief. Una nota vacía, compuesta solo por placeholders o sin confirmación de que ocurrió alguna entrevista sí activa parada.

## 3. Leer la nota primero

Leer `source_interview_notes` completa antes de cualquier contexto. Crear un inventario inicial de:

- datos contextuales;
- preguntas recordadas;
- respuestas/talking points recordados;
- declaraciones atribuidas a la otra parte;
- impresiones y autoevaluaciones;
- compromisos explícitos;
- citas recordadas con precisión;
- recuerdos aproximados y ausencias.

No reinterpretar aún. Esta primera lectura fija el límite de lo que puede describirse como ocurrido.

## 4. Leer contexto de aplicación

Leer después, cuando existan y sean relevantes:

1. `submission-record.md`, para estado previo, cronología y hechos ya registrados.
2. `job-description.md`, para contexto del rol, no para reconstruir preguntas.
3. `recruiter-conversation.md`, para distinguir información anterior de nueva.
4. `job-intake.md`.
5. `application-plan.md`.
6. `risk-register.md`.
7. `target-profile-selection.md`.
8. `evidence-selection.md`.
9. `generated/opportunity-dossier.md`, si existe, para comparar incógnitas previas.
10. `generated/interview-prep.md`, solo si existía antes de la entrevista o hay evidencia de su anterioridad.

Registrar rutas y finalidad en `source_files_used`. No leer CVs como fuentes ni resolver nuevas entidades canónicas.

## 5. Separar planned vs actual

Cuando se lea Interview Prep:

- etiquetar sus preguntas, historias y respuestas como `planned`;
- etiquetar solo lo presente en la nota como `actual_recollection`;
- marcar coincidencias sin suponer que se siguió el guion;
- registrar preparación no utilizada solo si las notas permiten afirmarlo; la mera ausencia en notas incompletas no lo demuestra.

Cuando se lea Opportunity Dossier:

- comparar incógnitas anteriores con declaraciones recordadas;
- conservar la atribución del interviewer;
- proponer una actualización separada del dossier;
- no convertir la declaración en investigación pública verificada.

## 6. Reconstruir el contexto mínimo

- Determinar fecha, tipo, participantes, canal, duración y agenda solo desde la nota y hechos explícitos del expediente.
- Determinar `application_status_before_interview` desde el último evento demostrable anterior a la entrevista.
- Si el timeline solo contiene estado posterior o no permite ordenar hechos, usar `desconocido` y explicar el límite.
- No inferir evaluación, intención de contratar o resultado por tono, duración o cordialidad.

## 7. Analizar preguntas, respuestas y evidencia

Para cada pregunta recordada:

- conservar formulación exacta o aproximada;
- enlazar la respuesta solo si la nota permite hacerlo;
- separar contenido dicho de contenido que, en retrospectiva, habría sido útil;
- identificar evidencia/historia usada sin ampliar hechos;
- distinguir gap real, respuesta incompleta, nervios o simple autoevaluación.

Una pregunta difícil no implica fallo. Una ausencia de reacción no permite evaluar desempeño. Feedback explícito debe conservar emisor y literalidad/paráfrasis.

## 8. Identificar información nueva

Comparar la nota con el contexto previo y clasificar novedades sobre:

- empresa;
- rol;
- equipo;
- sistema técnico;
- proceso/siguiente etapa;
- condiciones.

Para cada novedad registrar quién la dijo, grado de recuerdo, fuente previa con la que se compara y si queda pendiente de verificación. Si ya estaba documentada, marcarla como confirmación conversacional, no como novedad.

## 9. Evaluar de forma constructiva

### Qué fue bien

Basarse en conductas o contenidos recordados: respuesta clara, ejemplo pertinente, pregunta útil, transparencia o feedback explícito. Separar `candidate_impression` de `interviewer_statement`.

### Áreas a mejorar

Describir qué faltó y cómo prepararlo: estructura, precisión, ejemplo, límite o pregunta de aclaración. No diagnosticar el resultado del proceso.

### Oportunidades perdidas

Identificar información o evidencia que podría haberse explorado, sin afirmar que habría mejorado la evaluación. Si las notas son incompletas, marcar que quizá ocurrió pero no quedó capturado.

## 10. Follow-ups y propuestas

Separar:

- **compromiso del candidato:** prometido explícitamente;
- **compromiso de la otra parte:** atribuido y con plazo solo si consta;
- **acción recomendada:** conclusión del debrief, no promesa;
- **pendiente de confirmar:** recuerdo o responsabilidad ambiguos.

No enviar nada desde este workflow.

## 11. Implicaciones por destino

### Lifecycle

Proponer, sin ejecutar, el evento estándar adecuado —normalmente `interview_completed`, `feedback_received` u `other`—, los campos requeridos, un estado posterior posible y cualquier dato faltante. No asumir que una entrevista terminó bien ni que existe siguiente fase.

### Plan y riesgos

Enumerar decisiones o riesgos que la nueva información podría cambiar. Usar `resolver`, `recalibrar`, `añadir` o `mantener abierto`, siempre como propuesta.

### Conocimiento canónico

Registrar solo hechos profesionales del candidato que emergieron durante su propia respuesta y no estaban documentados. Para cada candidato incluir formulación recordada, fuente bruta, dudas, entidad potencial y evidencia que debería verificarse. No crear achievements desde elogios.

### Siguiente preparación

Proponer temas, respuestas, historias o preguntas a preparar únicamente como posibilidad. No afirmar que habrá otra ronda.

## 12. Redactar y revisar

- Completar `templates/generated/interview-debrief.template.md` con las 19 secciones.
- Derivar `<note-stem>` retirando únicamente `.md` del filename de `source_interview_notes`; no reconstruirlo desde `interview_date` o `interview_type`.
- Usar bullets y tablas breves; mantener cerca fuentes y etiquetas.
- Usar `desconocido`, `[]` o `ninguno` cuando falte información.
- Marcar `status: draft`.
- Revisar cada afirmación de “ocurrió” contra `source_interview_notes`.

Checklist mínimo:

- [ ] La nota bruta se leyó primero y no se modificó.
- [ ] Solo la nota demuestra qué se recuerda que ocurrió.
- [ ] Planned y actual están separados.
- [ ] Impresión, inferencia y feedback explícito no se mezclan.
- [ ] Las citas conservan su grado de precisión.
- [ ] No se inventaron preguntas, respuestas, reacciones ni resultados.
- [ ] Las novedades empresariales conservan atribución.
- [ ] Las propuestas para lifecycle contienen evidencia y datos faltantes.
- [ ] Los candidatos canónicos siguen pendientes de verificación.
- [ ] Solo se creó o reemplazó el debrief.

## 13. Output y parada

Crear o reemplazar exclusivamente:

```text
<source_application_folder>/generated/interview-debriefs/<note-stem>.md
```

Cada ejecución modifica únicamente el debrief asociado a la nota suministrada. Los debriefs de otras entrevistas deben permanecer intactos. Después, detenerse. No modificar la nota, `submission-record.md`, plan, riesgos, dossier, Interview Prep, conocimiento canónico, perfiles, CVs ni otros outputs.

## 14. Condiciones de parada

Detenerse sin generar cuando:

- la nota no existe, está vacía o solo contiene placeholders;
- no puede confirmarse que la nota pertenece al expediente;
- `application_id`, carpeta, note stem u `output_path` son incoherentes;
- `output_path` sale de `generated/interview-debriefs/`, apunta al debrief de otra nota o usa el singleton prohibido `generated/interview-debrief.md`;
- el tipo solicitado contradice la nota y no puede usarse `unknown` con seguridad;
- el idioma no puede resolverse;
- el usuario exige reconstruir lo ocurrido desde fuentes de preparación;
- el análisis exige inventar feedback, citas o hechos;
- reemplazar el output pisaría cambios ajenos no revisados.

No detenerse por notas incompletas: reducir conclusiones, conservar incertidumbre y producir un debrief limitado es el comportamiento correcto.
