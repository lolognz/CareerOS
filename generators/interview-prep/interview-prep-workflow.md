# Workflow del generador de preparación de entrevistas

## Objetivo operativo

Crear en 30–60 minutos un material de preparación conversacional, específico para la etapa y respaldado por evidencia, sin cambiar el expediente ni simular experiencia ausente.

## 1. Preconditions

- Recibir una única ruta bajo `career/applications/` o `examples/applications/`.
- Confirmar que el expediente y su `application_id` son coherentes.
- Confirmar que Job Intake está completo y que existe evidencia seleccionada suficiente.
- Recibir un `interview_type` permitido; usar `unknown` cuando la etapa no esté confirmada.
- Confirmar que la preparación fue solicitada explícitamente.
- Revisar si el output existente contiene cambios locales antes de reemplazarlo.

La preparación es especialmente útil cuando hay una entrevista programada o cuando `waiting_feedback` hace probable una siguiente conversación, pero esta posibilidad no convierte una entrevista en confirmada ni cambia el lifecycle.

## 2. Application inputs

Leer primero, sin mezclar expedientes:

1. `job-description.md`: texto de la oportunidad; es contexto, no evidencia profesional.
2. `recruiter-conversation.md`, si existe: hechos y aclaraciones del contacto.
3. `job-intake.md`: requisitos, gaps, inferencias e incógnitas.
4. `target-profile-selection.md`: perfil primario y límites de posicionamiento.
5. `evidence-selection.md`: únicas evidencias autorizadas por defecto.
6. `application-plan.md`: estrategia, preguntas y outputs permitidos.
7. `risk-register.md`: sobreclaims, blockers y mitigaciones.
8. `submission-record.md`: estado, eventos, interlocutores y etapa actuales.

Leer los documentos de Application Lifecycle solo para interpretar estado y etapa. Registrar todas las rutas en `source_files_used`.

No usar `generated/cv.md`, CVs finales, mensajes generados ni otros outputs como fuentes factuales. Si el usuario exige leer un CV para coherencia, contrastar cualquier contenido utilizado con las fuentes autorizadas y registrar esa lectura; el CV nunca añade evidencia.

## 3. Profile and canonical evidence

- Resolver y leer el perfil objetivo referenciado por el expediente.
- Extraer los IDs canónicos citados en `evidence-selection.md`, `target-profile-selection.md` y `application-plan.md`.
- Resolver cada ID por valor exacto usando el índice y leer únicamente esas entidades.
- No seguir relaciones ni añadir entidades cercanas que no estén referenciadas por alguno de los tres inputs.
- Detenerse si un ID necesario no existe, la entidad contradice el análisis o falta evidencia para el posicionamiento previsto.

## 4. Stage and interview context

- Determinar `application_status_at_generation` desde `submission-record.md` con su evidencia y fecha disponible.
- Contrastar el estado con `interview_type` y `known_interview_details`.
- Separar:
  - **conocido:** tipo, fecha, canal, participantes o formato explícitos;
  - **inferido:** temas plausibles por etapa u oferta, siempre etiquetados;
  - **por preguntar:** agenda, alcance, entrevistadores o siguiente fase desconocidos;
  - **no afirmar:** cualquier detalle sin respaldo.
- Si se solicita `technical_interview` pero solo consta un recruiter screen, detenerse o usar `unknown` únicamente con autorización explícita.

## 5. Opportunity and positioning

- Resumir puesto, empresa/cliente/intermediario, requisitos y contexto sin copiar toda la oferta.
- Diferenciar requisitos literales de interpretaciones del intake.
- Construir `candidate_positioning` desde perfil, plan y evidencia seleccionada.
- Elegir de tres a cinco ideas centrales útiles para esa etapa.
- Preservar títulos formales y alcance. Presentar potencial como potencial, no como experiencia formal.
- Si existe `focus_areas`, priorizarlas solo cuando estén respaldadas; no usarlas para ampliar claims.

## 6. Pitches

- Preparar un pitch de unos 30 segundos: identidad profesional, evidencia principal y motivo/contexto respaldado.
- Preparar uno de unos 60 segundos: trayectoria relevante, dos señales de ajuste y transición hacia la conversación.
- Escribir puntos naturales y adaptables, no un texto grandilocuente.
- No inventar motivación, disponibilidad, resultados, escala, ownership o interés específico.

## 7. Evidence and STAR selection

- Priorizar evidencia fuerte, reciente, profesional y distinta.
- Elegir entre tres y cinco bloques de evidencia para enfatizar.
- Preparar entre dos y cuatro historias STAR reutilizables.
- Para cada STAR registrar: pregunta que responde, situación, tarea, acción, resultado, fuentes, límites y variante breve.
- No forzar una historia a cubrir un competency gap. Si falta un resultado, decir qué se sabe y evitar completarlo.
- Mantener atribución compartida cuando la acción fue de equipo o colaboración.

## 8. Gap handling

Para cada gap relevante preparar cuatro piezas:

1. **Reconocimiento directo:** qué experiencia no se afirma.
2. **Alcance real:** exposición o responsabilidad demostrada.
3. **Evidencia adyacente:** capacidad transferible respaldada, sin equivalencias falsas.
4. **Pregunta de aclaración:** profundidad y expectativas reales del puesto.

Ejemplos de distinciones genéricas que deben poder manejarse cuando el expediente las contenga:

- backend Java senior frente a ownership integral de plataforma;
- operación de sistemas en producción frente a administración de infraestructura;
- uso y seguimiento de CI/CD frente a diseño completo de la plataforma;
- colaboración con DevOps frente a responsabilidad formal DevOps;
- exposición parcial a Linux/cloud frente a dominio operativo;
- liderazgo técnico, revisión o mentoring frente a título formal de Tech Lead;
- sistemas críticos frente a experiencia demostrada en alta escala o baja latencia.

No incluir estas áreas por defecto: solo cuando aparezcan en los inputs y evidencias de la candidatura.

## 9. Questions and answer bank

- Preparar preguntas probables separadas en recruiter, técnicas y conductuales.
- Ajustar el peso por `interview_type`; con `unknown`, mantener cobertura equilibrada y marcar incertidumbre.
- No presentar una pregunta como confirmada salvo que `known_interview_details` o una conversación la documenten.
- Para cada pregunta prioritaria, crear una respuesta en puntos con: mensaje principal, evidencia, límites, posible follow-up y claim prohibido.
- Incluir respuestas prácticas sobre trayectoria, cambio, motivación o condiciones solo si existen hechos suficientes.
- No redactar soluciones técnicas específicas para un sistema desconocido como si fueran decisiones tomadas.

## 10. Questions to ask and conditions

- Priorizar entre cinco y ocho preguntas que ayuden a entender responsabilidad, equipo, arquitectura, operación, proceso y siguiente fase.
- Adaptar el destinatario: recruiter, técnico, hiring manager o liderazgo.
- Convertir gaps y red flags en preguntas neutrales, concretas y no defensivas.
- Separar compensación, ubicación, modalidad, contrato y disponibilidad; registrar lo conocido y lo pendiente.
- No preguntar algo ya resuelto sin explicar qué matiz sigue abierto.

## 11. Draft and review

- Completar `templates/generated/interview-prep.template.md` y eliminar placeholders sin respaldo.
- Mantener el material escaneable, con bullets cortos, prioridades y checklists.
- Incluir todos los campos del esquema en Metadata o en secciones trazables.
- Revisar cada pitch, respuesta y STAR contra sus fuentes.
- Confirmar que gaps, incertidumbre y do-not-claim son visibles.
- Marcar el output nuevo como `draft`.

Checklist mínimo:

- [ ] Estado y tipo de entrevista no se confundieron ni se inventaron.
- [ ] Solo se leyeron entidades canónicas autorizadas.
- [ ] Cada claim preparado tiene fuente y límite.
- [ ] Las preguntas probables están etiquetadas como hipótesis.
- [ ] Los gaps tienen respuesta honesta y pregunta de aclaración.
- [ ] Colaboración, exposición parcial, liderazgo y escala conservan su alcance.
- [ ] STAR preserva atribución, cronología y resultados reales.
- [ ] Condiciones desconocidas siguen pendientes.
- [ ] El documento puede repasarse en 30–60 minutos.
- [ ] Solo se creó o reemplazó el output permitido.

## 12. Output location

Crear o reemplazar exclusivamente:

```text
<source_application_folder>/generated/interview-prep.md
```

Una ruta alternativa solo es válida si el parámetro `output_path` sigue dentro de `generated/` del mismo expediente. El generador no modifica lifecycle, intake, perfiles, entidades, CVs ni otros outputs.

## 13. Stop conditions

Detenerse sin generar cuando:

- falta cualquiera de los siete inputs obligatorios o contiene placeholders materiales;
- el `application_id` o la carpeta son incoherentes;
- intake, perfil, plan, riesgos y estado se contradicen materialmente;
- el perfil referenciado no existe;
- un ID autorizado no resuelve o contradice el claim necesario;
- `interview_type` contradice la etapa documentada y no se puede usar `unknown` con seguridad;
- el idioma no puede determinarse;
- no existe evidencia suficiente para preparar pitches o respuestas honestos;
- el trabajo exigiría inventar hechos, esconder gaps o leer entidades no autorizadas;
- `output_path` sale de `generated/` del expediente;
- el output existente no puede reemplazarse sin pisar cambios ajenos.

Tras generar y revisar `interview-prep.md`, detenerse. No crear CV, mensajes, respuestas enviadas, eventos, notas de entrevista posterior ni cambios de estado.

