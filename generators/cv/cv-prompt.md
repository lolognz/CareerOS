# Prompt reutilizable: generar CV

Copia este prompt en Codex o ChatGPT y sustituye los valores entre corchetes. Debe ejecutarse desde un repositorio CareerOS con acceso a la carpeta indicada.

```text
Genera un CV Markdown auditable desde una única fuente de CareerOS.

Parámetros:
- source_mode: [application / reusable_strategy; si se omite con un source_application_folder existente, usar application por compatibilidad]
- source_application_folder: [ruta de candidatura/fixture cuando source_mode=application; [] en otro caso]
- source_strategy_file: [ruta del archivo estratégico cuando source_mode=reusable_strategy; [] en otro caso]
- language: [es / en / auto]
- target_length: [1-2 páginas]

Si source_mode=application, conserva el contrato existente y lee primero dentro de source_application_folder:
- job-description.md
- job-intake.md
- target-profile-selection.md
- evidence-selection.md
- application-plan.md
- risk-register.md
- submission-record.md

Después lee el perfil primario, todas las entidades referenciadas por evidence-selection.md y target-profile-selection.md y cualquier relación imprescindible para verificar identidad, título, fechas, atribución o contexto. No alteres ninguna precondición, ruta de salida ni regla de evidencia de este modo.

Si source_mode=reusable_strategy, lee primero source_strategy_file y extrae:
- perfil objetivo primario;
- perfiles objetivo secundarios opcionales;
- idioma, título de posicionamiento y extensión objetivo;
- selección explícita de IDs canónicos autorizados;
- prioridades de evidencia y experiencia;
- claims prohibidos, límites y gaps conocidos;
- output_path.

Después lee el perfil primario, todos los perfiles secundarios y todas las entidades canónicas autorizadas, aunque finalmente uses solo un subconjunto. No requieras ni inventes application_id, oferta, intake, conversación, submission record, plan, registro de riesgos ni evidence selection de candidatura.

Busca los IDs por su valor exacto. No uses el nombre del ID, el perfil, la oferta ni otro output generado como prueba suficiente. Si falta un archivo o un ID no resuelve, evalúa las condiciones de parada y no lo sustituyas con una suposición.

Después:

1. Confirma que source_mode es válido, que se proporcionó exactamente la fuente correspondiente y que no se mezclan contratos.
2. En application, valida el expediente, application_id, oferta, plan, selección y dependencias exactamente como antes. En reusable_strategy, valida que la estrategia contiene todos los campos requeridos y que output_path permanece bajo generated/.
3. En application, usa el idioma de la oferta por defecto salvo instrucción documentada. En reusable_strategy, usa el idioma de la estrategia. Registra siempre la base.
4. Selecciona solo la evidencia necesaria para el rol objetivo. Prioriza evidencia profesional fuerte, reciente y relevante sobre evidencia antigua, débil, redundante o personal.
5. Lee y respeta todos los títulos, empleadores, fechas, relaciones, límites, uncertainty y evidence boundaries de cada entidad elegida.
6. No inventes experiencia, métricas, fechas, tecnologías, responsabilidades, títulos, empleadores, educación, certificaciones, niveles de idioma, salario, disponibilidad, nombre ni datos de contacto.
7. No conviertas requisitos, preferencias o posicionamiento en experiencia del candidato. En application, respeta los gaps de evidence-selection.md; en reusable_strategy, respeta los gaps y claims prohibidos de la estrategia.
8. No conviertas fit parcial en ownership completo, liderazgo informal en responsabilidad formal de Tech Lead, colaboración en autoría exclusiva ni proyectos personales en experiencia profesional.
9. Conserva títulos formales y cronología. Etiqueta cualquier proyecto personal como personal y colócalo fuera de experiencia profesional.
10. Genera únicamente la ruta permitida por el modo: source_application_folder/generated/cv.md en application, o el output_path validado de la estrategia en reusable_strategy. Usa templates/generated/cv.template.md y cumple generators/cv/cv.schema.md y generators/cv/cv-workflow.md.
11. Construye primero un bloque candidato limpio con, cuando exista evidencia:
    - encabezado;
    - título objetivo;
    - resumen profesional;
    - fortalezas o skills centrales;
    - stack técnico seleccionado;
    - experiencia profesional;
    - proyectos o logros seleccionados si aportan valor;
    - educación o investigación si es relevante;
    - idiomas o información adicional si están respaldados.
12. Elimina cualquier sección sin evidencia. No dejes placeholders, IDs canónicos, notas internas, riesgos o gaps dentro del bloque candidato.
13. Usa bullets breves, específicos y respaldados. Evita lenguaje corporativo inflado y claims genéricos como "passionate", "results-driven" o "expert in everything" salvo evidencia extraordinaria explícita.
14. Mantén la extensión objetivo declarada por el input; por defecto una o dos páginas. No incluyas todas las entidades: selecciona lo que demuestre mejor el posicionamiento.
15. Después de un separador --- añade "## Notas de generación / Auditoría" y declara que esta sección no está destinada al envío.
16. En la auditoría incluye todos los campos obligatorios del esquema: fuentes usadas, perfil, posicionamiento, evidencia seleccionada, claims usados con respaldo y límites, claims evitados, gaps excluidos, riesgos, evidence boundaries, uncertainty, revisión y status draft.
17. Revisa cada frase y bullet contra su fuente canónica y completa el checklist del workflow. No marques reviewed ni submitted sin una acción explícita que lo justifique.
18. Detente. No generes ni modifiques PDF, DOCX, HTML, carta de presentación, mensaje a recruiter, LinkedIn, preparación o respuestas de entrevista. No modifiques la fuente, el expediente, perfiles objetivo ni conocimiento canónico.
```
