# Workflow del generador de mensajes a recruiters

## Objetivo operativo

Crear un contacto breve, honesto y trazable desde un expediente de candidatura ya analizado, sin añadir conocimiento nuevo ni iniciar otros materiales de candidatura.

## 1. Preconditions

- Recibir una única ruta bajo `career/applications/` o `examples/applications/`.
- Confirmar que la carpeta existe, contiene un `application_id` coherente y conserva la oferta original.
- Confirmar que Job Intake ha terminado: la decisión, el perfil, la evidencia, el plan y los riesgos no deben seguir como placeholders.
- Confirmar que la generación ha sido solicitada explícitamente y que `generated/` es una ubicación desechable.
- No continuar si la corrección necesaria pertenece primero al conocimiento canónico o al intake.

## 2. Inputs

Leer todos estos archivos de la misma carpeta, sin mezclar candidaturas:

1. `job-description.md`: literalidad de la oferta, idioma y contexto publicado.
2. `job-intake.md`: requisitos, gaps, preguntas, límites e incertidumbre.
3. `target-profile-selection.md`: recomendación y señales fuertes o débiles.
4. `evidence-selection.md`: única selección autorizada de experiencia y claims.
5. `application-plan.md`: decisión y estrategia prevista para el mensaje.
6. `risk-register.md`: sobreafirmaciones, requisitos ausentes y mitigaciones.
7. `submission-record.md`: estado, contacto previo y hechos de envío.

Registrar en `source_files_used` solo las rutas realmente leídas. No buscar fuera del expediente para completar hechos, salvo para resolver las referencias canónicas ya seleccionadas y verificar sus límites.

## 3. Message type selection

Si se indicó un tipo explícito, comprobar primero su coherencia. En modo automático, aplicar este orden:

1. Elegir `follow-up` solo cuando exista una interacción previa documentada y la intención sea retomarla.
2. Elegir `polite-decline` cuando la decisión sea `no aplicar`, se haya decidido no continuar o el usuario pida un rechazo compatible con el expediente.
3. Elegir `clarification-first` cuando la recomendación sea `aplicar tras aclarar` o queden incógnitas materiales que puedan cambiar la decisión, el alcance o las condiciones.
4. Elegir `apply` cuando el encaje sea suficiente y no existan aclaraciones bloqueantes.

`Aplicar de forma selectiva` no determina por sí solo un tipo: usar `clarification-first` si sus condiciones siguen abiertas y `apply` si ya están resueltas. Registrar en `review_notes` la razón de la selección.

## 4. Evidence and risk check

- Extraer de dos a tres señales de encaje como máximo; para un rechazo pueden no ser necesarias.
- Vincular cada señal y cada claim a `evidence-selection.md` y conservar el límite indicado.
- Cruzar todos los claims con gaps, riesgos de sobreafirmación e incertidumbre.
- Trasladar a `claims_avoided` cualquier tecnología, responsabilidad, métrica, seniority, título, motivación o condición sin soporte suficiente.
- Priorizar entre dos y cuatro preguntas que cambien una decisión o eviten una candidatura mal orientada; no convertir una lista exhaustiva del intake en interrogatorio.
- No afirmar salario, disponibilidad, interés ni contacto previo si no están documentados.

## 5. Draft generation

- Aplicar el tono por defecto: profesional, claro, breve y humano.
- Usar español o inglés según la oferta y el contexto conocido del destinatario.
- Redactar primero el mensaje principal conforme a las reglas de su tipo.
- Mantenerlo apto para LinkedIn o para abrir un email; eliminar biografía, contexto y saludos que no aporten.
- Crear dos o tres variantes solo cuando se soliciten y exista una diferencia útil de énfasis, longitud o canal. No variar hechos ni límites.
- Completar toda la metadata y trazabilidad de la plantilla, con `status: draft`.

## 6. Review checklist

- [ ] El tipo coincide con la recomendación, los riesgos y el historial del expediente.
- [ ] El idioma y el canal tienen una base documentada o la incertidumbre está explícita.
- [ ] Cada claim presente tiene fuente y respeta atribución, alcance, seniority, cronología y métricas.
- [ ] Ningún requisito de la oferta se presenta automáticamente como experiencia.
- [ ] Los gaps se omiten como claims o se convierten en preguntas honestas.
- [ ] No se inventan interés, disponibilidad, salario, motivación, identidad ni interacción previa.
- [ ] `clarification-first` contiene entre dos y cuatro preguntas de alto impacto.
- [ ] `apply` utiliza entre dos y tres señales de encaje como máximo.
- [ ] `follow-up` se apoya en una interacción documentada y no suena insistente.
- [ ] `polite-decline` rechaza con claridad y no promete interés futuro inventado.
- [ ] El texto es breve y no funciona como una carta de presentación encubierta.
- [ ] Claims evitados, riesgos, límites e incertidumbre siguen visibles fuera del mensaje.
- [ ] Las variantes, si existen, mantienen exactamente las mismas fronteras de evidencia.

Una revisión de contenido puede cambiar `status` de `draft` a `reviewed`. No marcar `sent` sin evidencia de envío.

## 7. Output location

Crear o reemplazar exclusivamente:

```text
<source_application_folder>/generated/recruiter-message.md
```

Usar `templates/generated/recruiter-message.template.md`. El output pertenece al mismo expediente que sus inputs, es desechable y puede regenerarse. Una corrección factual exige corregir primero la fuente apropiada; no consolidar el dato nuevo solo en el mensaje.

## 8. Stop conditions

Detenerse sin generar el mensaje cuando:

- falta cualquiera de los siete inputs o conserva placeholders materiales;
- la oferta original no está preservada o el `application_id` no coincide;
- no existe una recomendación utilizable o los documentos se contradicen en una decisión material;
- un claim necesario no tiene evidencia o resolverlo exigiría inventar;
- el tipo solicitado contradice el estado, la decisión o la ausencia de interacción previa;
- el idioma o destinatario son indispensables para redactar y no pueden determinarse;
- los riesgos bloqueantes requieren primero una respuesta del usuario o recruiter;
- la solicitud exige corregir conocimiento canónico o el intake antes de generar.

Tras crear y revisar `generated/recruiter-message.md`, detenerse. No generar CV, carta, LinkedIn, portfolio, bio, preparación de entrevista ni respuestas de entrevista.
