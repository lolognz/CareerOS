# Prompt reutilizable: generar CV adaptado

Copia este prompt en Codex o ChatGPT y sustituye los valores entre corchetes. Debe ejecutarse desde un repositorio CareerOS con acceso a la carpeta indicada.

```text
Genera un CV Markdown adaptado para una única candidatura de CareerOS.

Parámetros:
- source_application_folder: [career/applications/<application-slug> o examples/applications/<example-slug>]
- language: [es / en / auto]
- target_length: [1-2 páginas]

Lee primero, dentro de source_application_folder:
- job-description.md
- job-intake.md
- target-profile-selection.md
- evidence-selection.md
- application-plan.md
- risk-register.md
- submission-record.md

Lee también:
- el perfil objetivo primario referenciado por el expediente bajo career/target-profiles/;
- todas las entidades canónicas referenciadas por evidence-selection.md y target-profile-selection.md, aunque después utilices solo un subconjunto;
- cualquier entidad directamente relacionada imprescindible para verificar empleador, título, fechas, atribución o contexto.

Busca los IDs por su valor exacto. No uses el nombre del ID, el perfil, la oferta ni otro output generado como prueba suficiente. Si falta un archivo o un ID no resuelve, evalúa las condiciones de parada y no lo sustituyas con una suposición.

Después:

1. Confirma que el expediente está completo, su application_id es coherente, la oferta original está preservada y el plan permite generar el CV ahora.
2. Confirma que target-profile-selection.md, evidence-selection.md y application-plan.md coinciden en el perfil y la estrategia. Si la recomendación condiciona el CV a aclaraciones aún pendientes, detente.
3. Usa el idioma de la oferta por defecto. Si language no es auto, sigue el parámetro. Una instrucción explícita del usuario prevalece; registra siempre la base de la decisión.
4. Selecciona solo la evidencia necesaria para el rol objetivo. Prioriza evidencia profesional fuerte, reciente y relevante sobre evidencia antigua, débil, redundante o personal.
5. Lee y respeta todos los títulos, empleadores, fechas, relaciones, límites, uncertainty y evidence boundaries de cada entidad elegida.
6. No inventes experiencia, métricas, fechas, tecnologías, responsabilidades, títulos, empleadores, educación, certificaciones, niveles de idioma, salario, disponibilidad, nombre ni datos de contacto.
7. No conviertas requisitos de la oferta en experiencia del candidato. No uses tecnologías o responsabilidades que evidence-selection.md marque como gaps, no respaldadas o desconocidas.
8. No conviertas fit parcial en ownership completo, liderazgo informal en responsabilidad formal de Tech Lead, colaboración en autoría exclusiva ni proyectos personales en experiencia profesional.
9. Conserva títulos formales y cronología. Etiqueta cualquier proyecto personal como personal y colócalo fuera de experiencia profesional.
10. Genera únicamente source_application_folder/generated/cv.md usando templates/generated/cv.template.md y cumpliendo generators/cv/cv.schema.md y generators/cv/cv-workflow.md.
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
14. Mantén una extensión objetivo de una o dos páginas al renderizar. No incluyas todas las entidades: selecciona lo que demuestre mejor el ajuste.
15. Después de un separador --- añade "## Notas de generación / Auditoría" y declara que esta sección no está destinada al envío.
16. En la auditoría incluye todos los campos obligatorios del esquema: fuentes usadas, perfil, posicionamiento, evidencia seleccionada, claims usados con respaldo y límites, claims evitados, gaps excluidos, riesgos, evidence boundaries, uncertainty, revisión y status draft.
17. Revisa cada frase y bullet contra su fuente canónica y completa el checklist del workflow. No marques reviewed ni submitted sin una acción explícita que lo justifique.
18. Detente. No generes ni modifiques PDF, DOCX, HTML, carta de presentación, mensaje a recruiter, LinkedIn, preparación o respuestas de entrevista. No modifiques el expediente, perfiles objetivo ni conocimiento canónico.
```
