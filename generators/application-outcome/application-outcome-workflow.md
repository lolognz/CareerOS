# Workflow de Application Outcome

## Objetivo operativo

Analizar un proceso concluido de forma trazable y útil, separando resultado, feedback, impresión, hipótesis, lección y experimento, sin modificar las fuentes ni ejecutar implicaciones posteriores.

## 1. Validar la carpeta

- Recibir una única ruta bajo `career/applications/` o `examples/applications/`.
- Confirmar que existe `submission-record.md` y que `application_id` coincide con el slug.
- Recibir `language`; aceptar `focus_areas` opcional.
- Resolver `output_path` como `generated/application-outcome.md` por defecto.
- Confirmar que el output permanece dentro de `generated/` del mismo expediente y no apunta a otro output.
- Revisar el singleton existente antes de reemplazarlo, especialmente si contiene cambios locales.

## 2. Leer primero el lifecycle factual

Leer `submission-record.md` completo antes de cualquier otro archivo. Leer también las definiciones vigentes de Application Lifecycle para interpretar literalmente estado, outcome, eventos y transiciones.

Extraer:

- estado actual y evidencia;
- outcome separado;
- timeline acumulado;
- fecha demostrable del resultado;
- partes, canales y mediación;
- follow-ups todavía abiertos.

No corregir contradicciones dentro de esta ejecución. Conservarlas en `uncertainty` y proponer una actualización separada en `lifecycle_implications` cuando corresponda.

## 3. Confirmar elegibilidad

La ejecución ordinaria continúa si el lifecycle documenta `rejected`, `withdrawn`, `offer_received`, `offer_negotiation`, `accepted`, `declined` o `closed`.

Puede continuar excepcionalmente con otro estado solo si eventos factuales demuestran inequívocamente un proceso materialmente concluido. Registrar:

- la evidencia concreta;
- por qué el estado no representa todavía esa evidencia;
- la actualización lifecycle que debe evaluarse por separado.

Detenerse si solo hay silencio, espera, impresión, riesgo, promesa condicional o inferencia de cierre.

## 4. Establecer el timeline factual

Leer después, si existen:

1. `recruiter-conversation.md`;
2. todas las notas relevantes bajo `interviews/`;
3. `job-description.md`.

Construir una cronología mínima de hechos que explique el recorrido y el outcome. Conservar fechas desconocidas y no deducir etapas por patrones habituales. Separar lo que ocurrió de lo prometido, esperado o inferido.

## 5. Extraer feedback explícito

Para cada feedback:

- conservar cita exacta cuando la fuente sea una transcripción literal; en otro caso usar paráfrasis fiel;
- registrar emisor, rol/organización, destinatario, canal, fecha y archivo fuente;
- distinguir autor original de transmisor cuando se conozca;
- marcar como recruiter-mediated si llega mediante intermediario;
- registrar incertidumbre sobre autoría o alcance.

No convertir feedback sobre background reciente en rasgo esencial del candidato. No añadir causas que el mensaje no menciona.

## 6. Leer análisis y riesgos previos

Leer, en este orden:

1. `job-intake.md`;
2. `application-plan.md`;
3. `risk-register.md`;
4. `target-profile-selection.md`;
5. `evidence-selection.md`.

Inventariar hipótesis, blockers, gaps y riesgos existentes antes del outcome. No confundir un requisito de la oferta con una evaluación posterior.

Clasificar cada elemento relevante como:

- `confirmed`;
- `disconfirmed`;
- `unresolved`;
- `not_relevant_to_outcome_analysis`.

Exigir evidencia posterior explícita para `confirmed` o `disconfirmed`. Ausencia de feedback produce normalmente `unresolved`, no refutación.

## 7. Leer contexto analítico generado al final

Solo después de fijar hechos y riesgos previos, leer si existen:

1. `generated/interview-debriefs/*.md`;
2. `generated/opportunity-dossier.md`;
3. `generated/interview-prep.md`, si es relevante para comparar preparación, no para reconstruir lo ocurrido.

Registrar estos archivos como contexto analítico. No permitir que eleven una impresión o inferencia sobre sus fuentes primarias. No leer CVs.

## 8. Formular hipótesis conservadoras

Cada `new_hypothesis` debe incluir:

- proposición acotada;
- evidencia de apoyo;
- evidencia contradictoria o ausente;
- confianza `low`, `medium` o `high`;
- explicación alternativa plausible;
- evidencia adicional necesaria.

Una explicación explícita del outcome puede soportar una conclusión sobre ese proceso, pero no una regla general sobre todos los empleadores o el candidato. Usar confianza baja o media cuando solo existe una observación.

## 9. Derivar lecciones e implicaciones

- Convertir hechos en lecciones prácticas acotadas, nunca identidades universales.
- Proponer cambios de posicionamiento solo usando evidencia ya existente.
- Para Target Profiles elegir una decisión permitida y justificar por qué un único outcome suele ser insuficiente para cambios mayores.
- Tratar feedback externo sobre percepción como dato del proceso, no como conocimiento canónico.
- Identificar hechos profesionales nuevos solo como candidatos pendientes de verificación.
- Mantener separados aprendizaje de aplicación, cambio de fuente y regeneración de outputs.

## 10. Diseñar experimentos

Cuando una lección dependa de una hipótesis incierta, diseñar una prueba futura:

- hipótesis que se prueba;
- cambio único o conjunto mínimo de cambios;
- contexto donde aplica;
- señal observable;
- resultado que apoyaría la hipótesis;
- resultado que la debilitaría;
- variables que deben mantenerse estables cuando sea posible.

No prometer que un experimento causará éxito ni convertirlo en norma permanente.

## 11. Proteger lo que no debe cambiar

Completar obligatoriamente `things_not_to_change`. Incluir protecciones específicas respaldadas por el expediente, por ejemplo:

- conservar experiencia y cronología exactas;
- no inventar experiencia ausente;
- no borrar contexto válido para encajar con una opinión;
- no atribuir causalidad a riesgos no resueltos;
- no cambiar Target Profiles o conocimiento por una sola señal insuficiente.

## 12. Identificar downstream sin aplicarlo

Listar posibles revisiones separadas de lifecycle, plan, riesgos, perfiles, conocimiento, estrategia futura u Opportunity Dossier. Para cada propuesta indicar evidencia, motivo y workflow/destino. No aplicar ninguna modificación.

## 13. Redactar y revisar

Completar las 22 secciones de `templates/generated/application-outcome.template.md`.

- Marcar un output nuevo como `draft`.
- Mantener procedencia cerca de cada claim.
- Usar tablas para feedback, riesgos, hipótesis y experimentos.
- Eliminar placeholders y conservar `desconocido`, `ninguno` o `[]` cuando corresponda.
- Mantener el análisis legible y proporcional al proceso.

## 14. Escribir y detenerse

Crear o reemplazar exclusivamente:

```text
<source_application_folder>/generated/application-outcome.md
```

No modificar lifecycle, conversaciones, entrevistas, intake, plan, riesgos, perfiles, conocimiento, dossier, preparación, CVs ni otros outputs. Detenerse después de validar el archivo.

## Condiciones de parada

Detenerse sin generar cuando:

- falta la carpeta, `submission-record.md` o un parámetro obligatorio;
- carpeta y `application_id` no coinciden;
- no existe outcome significativo ni cierre material inequívoco;
- el resultado solo se deduce de silencio o demora;
- las fuentes se contradicen de modo que impide determinar el outcome;
- el usuario exige atribuir una causa sin evidencia;
- el idioma no puede resolverse;
- `output_path` sale de `generated/` del mismo expediente;
- reemplazar el singleton pisaría cambios ajenos no revisados.

