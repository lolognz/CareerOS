# Generador de CV

Esta capa define cómo transformar el intake completo de una candidatura y su evidencia canónica seleccionada en un CV Markdown adaptado. El CV es una salida desechable: no añade hechos, no corrige entidades y no se convierte en fuente de verdad.

## Alcance de v1

El generador trabaja sobre una única carpeta bajo `career/applications/<application-slug>/` o `examples/applications/<example-slug>/` y crea exclusivamente:

```text
<application-folder>/generated/cv.md
```

El resultado contiene dos bloques claramente separados:

1. Un CV limpio para la candidatura, pensado para una extensión aproximada de una o dos páginas al renderizarse.
2. Una auditoría no destinada al envío, con fuentes, selección, claims, límites, gaps, riesgos e incertidumbre.

v1 genera Markdown estructurado. No implementa diseño visual ni conversión a PDF, DOCX o HTML, y no genera carta de presentación, mensaje a recruiter ni preparación de entrevista.

## Componentes

- [Fast Application Workflow](../../docs/workflows/fast-application-workflow.md): sitúa el CV después de la decisión y sus posibles aclaraciones bloqueantes.
- [cv.schema.md](cv.schema.md): contrato del output y reglas de validación.
- [cv-workflow.md](cv-workflow.md): proceso de selección, redacción y revisión.
- [cv-prompt.md](cv-prompt.md): prompt directamente utilizable con Codex o ChatGPT.
- [`templates/generated/cv.template.md`](../../templates/generated/cv.template.md): estructura del CV y de su auditoría.

## Fuentes

El generador usa los siete documentos del expediente:

- `job-description.md`
- `job-intake.md`
- `target-profile-selection.md`
- `evidence-selection.md`
- `application-plan.md`
- `risk-register.md`
- `submission-record.md`

También debe resolver y leer el perfil objetivo elegido y todas las entidades canónicas referenciadas por `evidence-selection.md` y `target-profile-selection.md`, aunque después utilice solo un subconjunto. La oferta define el objetivo; no demuestra experiencia del candidato. El perfil define estrategia; tampoco crea hechos.

## Principios de generación

- Seleccionar evidencia por relevancia y fuerza, no por volumen.
- Priorizar experiencia profesional reciente y sólida; usar evidencia antigua, personal o débil solo cuando aporte un ajuste concreto.
- Conservar títulos formales, empleadores, fechas, cronología, atribución y alcance de las entidades.
- No convertir encaje parcial en dominio, liderazgo informal en título formal ni proyectos personales en experiencia profesional.
- No inventar experiencia, métricas, fechas, tecnologías, responsabilidades, títulos, empleadores, educación, certificaciones, idiomas, salario, disponibilidad ni datos de contacto.
- No convertir requisitos de la oferta en skills o experiencia del candidato.
- Omitir del CV visible los gaps y conservarlos en la auditoría.
- Redactar bullets específicos y respaldados, sin lenguaje corporativo inflado ni adjetivos genéricos.
- Seguir por defecto el idioma de la oferta, salvo instrucción distinta del plan o del usuario.
- Tratar `generated/cv.md` como reemplazable y no canónico.

El fixture `examples/applications/job-intake-knowmad-mood-senior-backend-java/` puede utilizarse en una prueba posterior, pero no es una dependencia ni determina la estructura o el contenido del generador.
