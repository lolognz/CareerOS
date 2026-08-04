# Workflow del generador de CV

## Objetivo operativo

Crear un CV Markdown adaptado, conciso y auditable desde una candidatura ya analizada, preservando la frontera entre estrategia, evidencia canónica y output desechable.

## 1. Preconditions

- Recibir una única ruta bajo `career/applications/` o `examples/applications/`.
- Confirmar que la carpeta existe, su `application_id` es coherente y la oferta original está preservada.
- Confirmar que Job Intake está completo y que el CV figura como output permitido por `application-plan.md`.
- Confirmar que la generación fue solicitada explícitamente y que `generated/` es una ubicación desechable.
- No continuar si un dato necesario exige corregir primero el intake o una entidad canónica.

## 2. Inputs

Leer, sin mezclar candidaturas:

1. `job-description.md`: título, idioma y requisitos literales de la oportunidad.
2. `job-intake.md`: encaje, requisitos, gaps, instrucciones y límites.
3. `target-profile-selection.md`: perfil primario, alternativas rechazadas y señales.
4. `evidence-selection.md`: IDs autorizados, fuerza, usos y cautelas.
5. `application-plan.md`: decisión, estrategia específica de CV y dependencias.
6. `risk-register.md`: sobreafirmaciones, evidencia débil y mitigaciones.
7. `submission-record.md`: estado de la candidatura y hechos posteriores relevantes.

Resolver además:

- el archivo de `target_profile` bajo `career/target-profiles/`;
- todas las entidades canónicas referenciadas por los IDs de `evidence-selection.md` y `target-profile-selection.md`, aunque solo un subconjunto llegue al CV;
- las entidades directamente relacionadas que sean imprescindibles para verificar empresa, fechas, título, atribución o contexto, sin ampliar por ello la selección.

Buscar cada ID por su valor exacto y registrar toda ruta leída en `source_files_used`. No usar un perfil, otro output generado ni la oferta como sustituto de evidencia canónica.

## 3. Target profile and strategy check

- Confirmar que existe cero o un perfil primario y que coincide entre selección, intake y plan.
- Leer `primary_positioning`, `narrative_strategy`, `cv_strategy`, elementos a enfatizar o reducir, `avoid_claims`, riesgos e incertidumbre del perfil.
- Confirmar la recomendación y las dependencias del CV. `Aplicar tras aclarar` no autoriza a ignorar aclaraciones que el plan marque como previas.
- Determinar `target_role_title` desde el título de la oferta o una instrucción explícita. Tratarlo como objetivo, nunca como título histórico.
- Elegir el idioma de la oferta por defecto; una instrucción del usuario o del plan puede sustituirlo. Registrar la base y cualquier ambigüedad.
- Detenerse ante contradicciones materiales de perfil, estrategia, recomendación o idioma.

## 4. Evidence selection

- Partir exclusivamente de los IDs autorizados en `evidence-selection.md`.
- Verificar cada entidad antes de usarla; el ID o una tabla de selección no bastan por sí solos.
- Ordenar la evidencia por: relevancia para el rol, fuerza, actualidad, carácter profesional y capacidad de demostrar algo distinto.
- Elegir solo los roles, proyectos, historias, skills, tecnologías y logros necesarios para sostener un CV de una o dos páginas.
- Preservar cronología inversa en experiencia, incluidos solapamientos e incertidumbre.
- Usar historias y logros para construir bullets, no para duplicar secciones o hechos.
- Incluir proyectos personales solo en una sección separada, etiquetados como personales y únicamente si el plan los considera relevantes.
- Incluir educación, investigación, idiomas o información adicional solo cuando exista evidencia canónica seleccionada o una fuente autorizada suficiente.

## 5. Claim filtering

Para cada posible línea del CV:

1. Formular el claim mínimo necesario.
2. Vincularlo a uno o más IDs canónicos leídos.
3. Comprobar título, empleador, fechas, atribución, alcance, seniority, contexto y fuerza.
4. Cruzarlo con `avoid_claims`, gaps, riesgos e incertidumbre del perfil y del expediente.
5. Aprobarlo, reducirlo a su alcance demostrado u omitirlo.

Registrar los claims aprobados en `claims_used` y los descartados en `claims_avoided`. Trasladar todos los requisitos no respaldados o parciales a `gaps_not_included`.

No convertir tecnologías o responsabilidades de la oferta en experiencia. No completar verbos con resultados plausibles. No transformar colaboración en autoría exclusiva, contribución parcial en ownership total, liderazgo informal en Tech Lead formal ni un proyecto personal en empleo.

## 6. CV drafting

- Construir el bloque candidato con la estructura indicada por el esquema y eliminar secciones sin soporte.
- En el encabezado, incluir únicamente nombre, ubicación y contacto respaldados. No usar placeholders visibles.
- Escribir un resumen profesional factual y específico, sin `passionate`, `results-driven`, `expert in everything` ni equivalentes no demostrados.
- Mostrar skills y stack seleccionados; no copiar la lista de requisitos de la oferta.
- Conservar en cada experiencia el empleador, título formal y fechas canónicas.
- Redactar pocos bullets de alto valor. Cada bullet debe describir contexto, contribución o resultado demostrado sin métricas inventadas.
- Evitar repetir la misma evidencia en resumen, skills, experiencia y proyectos cuando no aporte información nueva.
- Mantener una extensión objetivo de una o dos páginas al renderizar; si hay exceso, retirar primero evidencia débil, antigua, redundante o secundaria.
- No insertar IDs, cautelas internas ni gaps en el bloque candidato.

## 7. Audit section

Después de un separador `---`, añadir `## Notas de generación / Auditoría` y declarar que no está destinada al envío.

Completar todos los campos del esquema:

- fuentes del expediente, perfil y entidades realmente leídas;
- perfil y posicionamiento utilizados;
- subconjunto de evidencia efectivamente usado;
- mapa de claims a fuentes y límites;
- claims evitados y gaps excluidos;
- riesgos, fronteras de evidencia e incertidumbre;
- referencia de `generated_cv` al bloque candidato anterior;
- notas de revisión y `status: draft`.

La auditoría puede ser más detallada que el CV, pero no debe introducir hechos nuevos.

## 8. Review checklist

- [ ] El expediente, la recomendación y las dependencias permiten generar el CV.
- [ ] El perfil objetivo y el título objetivo son coherentes y no alteran títulos históricos.
- [ ] El idioma sigue la oferta o una instrucción explícita documentada.
- [ ] Todos los IDs usados existen, fueron leídos y estaban autorizados por la selección.
- [ ] Nombre, contacto, empleadores, títulos, fechas, educación, certificaciones e idiomas están respaldados o se omitieron.
- [ ] Cada frase y bullet visible aparece trazado en `claims_used`.
- [ ] Se preservan cronología, atribución, alcance, seniority y cualificación de métricas.
- [ ] Ningún requisito de la oferta se convirtió en experiencia sin evidencia.
- [ ] El encaje parcial no se presenta como ownership completo.
- [ ] El liderazgo informal no aparece como título Tech Lead ni gestión formal.
- [ ] Los proyectos personales, si existen, están separados y etiquetados.
- [ ] Los gaps no aparecen en el CV candidato y sí en `gaps_not_included`.
- [ ] No se incluyó evidencia irrelevante solo para llenar espacio.
- [ ] El lenguaje es directo, específico y no inflado.
- [ ] La extensión estimada es de una o dos páginas.
- [ ] La auditoría está separada y marcada como no destinada al envío.
- [ ] El estado inicial es `draft`.

Una revisión explícita puede cambiar el estado a `reviewed`. No usar `submitted` sin evidencia documentada de envío.

## 9. Output location

Crear o reemplazar exclusivamente:

```text
<source_application_folder>/generated/cv.md
```

Usar `templates/generated/cv.template.md`. El archivo pertenece al expediente de origen, es desechable y puede regenerarse. Si la revisión descubre un error factual, corregir primero su fuente canónica o el intake correspondiente.

## 10. Stop conditions

Detenerse sin generar el CV cuando:

- falta cualquiera de los siete inputs o contiene placeholders materiales para la generación;
- la oferta original no está preservada o el `application_id` no coincide;
- el CV está marcado como no recomendado, bloqueado o condicionado a aclaraciones todavía pendientes;
- el perfil primario es inexistente, ambiguo o contradictorio sin una justificación explícita para `[]`;
- un ID seleccionado no resuelve, su entidad no puede leerse o contradice el claim previsto;
- faltan nombre, título, empresa o fechas necesarios para una experiencia que deba incluirse;
- el idioma no puede determinarse con seguridad;
- la selección no contiene evidencia suficiente para un CV honesto y útil;
- generar exigiría inventar, elevar evidencia parcial o tratar un proyecto personal como experiencia profesional;
- la corrección necesaria pertenece antes al conocimiento canónico o al intake.

Tras crear y revisar `generated/cv.md`, detenerse. No generar PDF, DOCX, HTML, carta de presentación, mensaje a recruiter, LinkedIn ni preparación o respuestas de entrevista.
