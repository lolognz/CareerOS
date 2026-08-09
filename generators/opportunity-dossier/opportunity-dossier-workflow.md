# Workflow del generador de dossier de oportunidad

## Objetivo operativo

Crear un dossier breve, trazable y útil para decidir y preparar el siguiente paso de una candidatura, dejando visibles los límites de lo conocido y sin investigar ni afirmar más allá de las fuentes entregadas.

## 1. Precondiciones

- Recibir una única ruta bajo `career/applications/` o `examples/applications/`.
- Confirmar que carpeta y `application_id` son coherentes.
- Confirmar que Job Intake está completo y no contiene placeholders materiales.
- Recibir `research_mode`, `language` y, opcionalmente, fuentes externas y áreas de foco.
- Confirmar que `output_path` queda dentro de `generated/` del mismo expediente.
- Revisar un dossier existente antes de reemplazarlo para no pisar cambios ajenos.

El dossier requiere una oportunidad concreta. No se genera a partir de un nombre de empresa aislado.

## 2. Leer primero el expediente

Leer en este orden y sin mezclar candidaturas:

1. `job-description.md`: lo que la oferta afirma y solicita.
2. `recruiter-conversation.md`, si existe: lo dicho durante el proceso.
3. `job-intake.md`: extracción, interpretaciones y gaps.
4. `application-plan.md`: decisión, estrategia y condiciones.
5. `risk-register.md`: riesgos, blockers y mitigaciones.
6. `submission-record.md`: estado factual, eventos e identidad aclarada.

Puede leerse después:

- `target-profile-selection.md`, para comprender el ángulo de encaje documentado;
- `evidence-selection.md`, para comprender límites ya seleccionados.

No resolver entidades del índice ni ampliar evidencia canónica. No leer CVs finales o generados como fuentes. Leer `interview-prep.md` solo si el usuario lo pide expresamente, únicamente para detectar preguntas ya preparadas.

Registrar en `source_files_used` solo los archivos realmente leídos y para qué se usaron.

## 3. Determinar identidad y estado

- Leer `application_status_at_generation` literalmente de `submission-record.md` y registrar su evidencia o incertidumbre.
- Separar empresa publicada, recruiter/intermediario, empleador contractual y cliente final.
- Asignar `company_or_client_known`:
  - `true`: la organización relevante y el cliente final, si existe, están identificados explícitamente;
  - `partial`: se conoce una parte, existen nombres ambiguos o el cliente final sigue oculto;
  - `false`: no puede identificarse la organización sobre la que investigar.
- Si el cliente final es desconocido, escribirlo de forma visible. No inferirlo por sector, stack, ubicación o descripción.

Un cambio posterior de identidad exige nuevas fuentes explícitas y una regeneración o actualización separada; no modifica lifecycle desde este generador.

## 4. Aplicar el modo de investigación

### `source_only`

- Trabajar solo con los archivos del expediente.
- Establecer `external_sources_used: []`.
- No completar contexto empresarial con memoria general del modelo.
- Convertir ausencias importantes en incertidumbre o preguntas.

### `external_research`

- Inventariar las notas, fragmentos, URLs con contenido, resultados ya obtenidos y archivos proporcionados.
- Comprobar qué contenido está realmente disponible. v1 no navega URLs ni llama APIs.
- Para cada fuente usada registrar: identificador local, título o descripción, tipo, URL o ruta, autor/editor si consta, fecha de publicación o consulta si consta y limitaciones.
- Separar notas del usuario de investigación pública y de declaraciones de recruiter.
- Extraer solo hechos relevantes para esta candidatura; no copiar largos fragmentos ni resumir sitios enteros.
- Cuando las fuentes discrepen, conservar el conflicto. Cuando falte contenido, dejar la pregunta abierta.

No degradar silenciosamente `external_research` a conocimiento interno del modelo. Si no hay investigación utilizable, el dossier puede continuar con hechos del expediente, `external_sources_used: []` y una incertidumbre explícita.

## 5. Construir un ledger de procedencia

Antes de sintetizar, clasificar cada afirmación como:

- `application_fact`;
- `recruiter_statement`;
- `external_research`;
- `user_note`;
- `inference`;
- `uncertainty`.

Registrar referencia concreta y, para inferencias, premisas, confianza y qué evidencia podría confirmarlas. Evitar fusionar dos categorías en una frase que parezca más cierta que sus fuentes.

## 6. Sintetizar empresa, producto y negocio

- Explicar solo lo necesario para entender la oportunidad.
- Separar lo que hace la empresa de lo que hace el producto o servicio asociado al rol.
- Identificar usuarios, compradores y clientes solo cuando consten; no asumir que son la misma parte.
- Describir el modelo de negocio únicamente si está respaldado. Usar `desconocido` frente a etiquetas plausibles como SaaS, consultoría, marketplace o fintech.
- Distinguir claims públicos de la empresa de hechos verificados independientemente cuando las fuentes lo permitan.
- Evitar hype, elogios genéricos y conclusiones sobre calidad, liderazgo de mercado o crecimiento no demostradas.

## 7. Sintetizar mercado, rol, tecnología y operación

- Capturar contexto de mercado o regulación solo si afecta al puesto o a la decisión.
- Separar responsabilidades literales del rol de inferencias sobre el trabajo diario.
- Distinguir stack solicitado de stack actualmente usado.
- Mantener desconocidos arquitectura, madurez, deuda, escala, latencia, tráfico, disponibilidad, despliegue, cloud, observabilidad, datos y seguridad cuando no consten.
- Distinguir propiedad del backend, plataforma, infraestructura, CI/CD, producción y on-call.
- Registrar equipo, reporting line, colaboración, modalidad, contrato y proceso solo desde fuentes explícitas.

## 8. Derivar implicaciones y riesgos

- Usar `job-intake.md`, `application-plan.md`, `risk-register.md` y, si se leyeron, selección de perfil/evidencia para formular implicaciones de encaje.
- No leer entidades nuevas ni crear evidencia candidata.
- Expresar cada implicación como consecuencia práctica: qué aclarar, preparar, negociar o considerar al decidir.
- Separar red flags observadas de señales ambiguas y simples ausencias de información.
- Para cada riesgo registrar fuente, impacto, nivel de confianza y acción para resolverlo.

## 9. Formular preguntas

Priorizar preguntas que puedan cambiar una decisión o mejorar una conversación:

- Antes de continuar: identidad, producto, condiciones, alcance o incompatibilidades materiales.
- Para recruiter: proceso, equipo, modalidad, contrato, cliente, expectativas y siguiente etapa.
- Para entrevista técnica: ownership, arquitectura, operación, escala, latencia, despliegue, guardias y éxito inicial.

Ejemplos genéricos que pueden adaptarse cuando sigan abiertos:

- ¿Qué hace exactamente el producto?
- ¿Quiénes son sus usuarios y clientes?
- ¿De qué es responsable el equipo backend?
- ¿Qué partes de infraestructura pertenecen a los desarrolladores?
- ¿Qué expectativas de latencia o escala tiene este rol?
- ¿Cómo funciona el on-call?
- ¿Cómo se estructura el equipo?
- ¿Cuál es la siguiente etapa?
- ¿Qué haría que alguien tuviera éxito en los primeros 3–6 meses?

No repetir preguntas ya resueltas. Si se leyó `interview-prep.md`, usarlo solo para evitar duplicación.

## 10. Notas de decisión

Organizar hechos que favorecen continuar, hechos que aconsejan cautela, blockers y criterios para:

- continuar;
- preparar el siguiente paso;
- negociar;
- esperar una aclaración;
- retirarse.

No sustituir la decisión de `application-plan.md` ni actualizarla. Si el dossier revela información que podría cambiarla, anotarlo como revisión necesaria fuera de este workflow.

## 11. Redacción y revisión

- Completar `templates/generated/opportunity-dossier.template.md`.
- Eliminar placeholders sin respaldo y usar `desconocido`, `[]` o una pregunta concreta cuando corresponda.
- Mantener bullets breves, referencias cercanas y foco práctico.
- Marcar un dossier nuevo como `draft`.
- Comprobar que las 17 secciones y todos los campos del esquema están presentes.

Checklist mínimo:

- [ ] Empresa, intermediario y cliente final están separados.
- [ ] Cada afirmación material tiene tipo de procedencia y fuente.
- [ ] Oferta, recruiter, investigación externa, notas, inferencias e incertidumbre no se mezclan.
- [ ] Las URLs sin contenido no respaldan hechos.
- [ ] Stack requerido no se presenta como stack real.
- [ ] Company research no aparece como evidencia o claim del candidato.
- [ ] Los desconocidos relevantes siguen visibles.
- [ ] Riesgos y red flags no se presentan con certeza excesiva.
- [ ] Las preguntas tienen destinatario e impacto práctico.
- [ ] Las notas ayudan a continuar, preparar, negociar o retirarse sin cambiar lifecycle.
- [ ] Solo se creó o reemplazó el output permitido.

## 12. Output y parada

Crear o reemplazar exclusivamente:

```text
<source_application_folder>/generated/opportunity-dossier.md
```

Una ruta alternativa es válida solo dentro de `generated/` del mismo expediente. Después de revisar el archivo, detenerse. No actualizar intake, plan, riesgos, selección, conocimiento canónico, CV, recruiter message, interview prep, `submission-record.md`, estados o eventos.

## 13. Condiciones de parada

Detenerse sin generar cuando:

- falta un input obligatorio o conserva placeholders materiales;
- carpeta y `application_id` no coinciden;
- las fuentes se contradicen de modo que impide identificar la oportunidad básica;
- `research_mode` o `language` no son válidos;
- el idioma no puede resolverse con `auto`;
- se exige afirmar un dato empresarial sin fuente disponible;
- el trabajo requiere navegar, usar una API o acceder a una fuente no proporcionada;
- `output_path` sale de `generated/` del expediente;
- reemplazar el dossier pisaría cambios ajenos no revisados.

No detenerse solo porque falten datos de empresa: si la oportunidad está identificada, registrar lo desconocido y formular preguntas es un resultado válido.
