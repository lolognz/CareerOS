# Generador de CV

Esta capa define cómo transformar una selección autorizada de evidencia canónica en un CV Markdown adaptado o reutilizable. El CV es una salida desechable: no añade hechos, no corrige entidades y no se convierte en fuente de verdad.

## Alcance de v1

El generador admite dos modos de fuente:

- `application`: conserva el flujo existente para una única carpeta bajo `career/applications/<application-slug>/` o `examples/applications/<example-slug>/` y crea exclusivamente:

```text
<application-folder>/generated/cv.md
```

- `reusable_strategy`: recibe un único archivo estratégico, por ejemplo `career/freelance/cv-strategy.md`, y escribe exclusivamente en el `output_path` declarado y validado por esa estrategia. La primera estrategia aprobada declara:

```text
generated/freelance/cv.md
```

El modo reutilizable no crea una candidatura ni exige inputs propios de una aplicación. Ambos modos comparten las mismas reglas de evidencia, claim filtering, estructura y auditoría.

Para compatibilidad con invocaciones existentes, una ejecución que proporcione únicamente `source_application_folder` se interpreta como `application`. `reusable_strategy` siempre debe declararse explícitamente.

El resultado contiene dos bloques claramente separados:

1. Un CV limpio para la candidatura, pensado para una extensión aproximada de una o dos páginas al renderizarse.
2. Una auditoría no destinada al envío, con fuentes, selección, claims, límites, gaps, riesgos e incertidumbre.

v1 genera Markdown estructurado. No implementa diseño visual ni conversión a PDF, DOCX o HTML, y no genera carta de presentación, mensaje a recruiter ni preparación de entrevista.

El Markdown generado no es la versión enviable porque conserva una auditoría interna. En modo `application`, tras su revisión, [CV Finalizer v1](../cv-finalizer/README.md) puede extraer el bloque candidato y crear las vistas limpias bajo `final/` sin añadir ni modificar hechos. El finalizador todavía no admite `reusable_strategy`.

## Componentes

- [Fast Application Workflow](../../docs/workflows/fast-application-workflow.md): sitúa el CV después de la decisión y sus posibles aclaraciones bloqueantes.
- [cv.schema.md](cv.schema.md): contrato del output y reglas de validación.
- [cv-workflow.md](cv-workflow.md): proceso de selección, redacción y revisión.
- [cv-prompt.md](cv-prompt.md): prompt directamente utilizable con Codex o ChatGPT.
- [`templates/generated/cv.template.md`](../../templates/generated/cv.template.md): estructura del CV y de su auditoría.

## Fuentes por modo

### `application`

El generador usa los siete documentos del expediente:

- `job-description.md`
- `job-intake.md`
- `target-profile-selection.md`
- `evidence-selection.md`
- `application-plan.md`
- `risk-register.md`
- `submission-record.md`

También debe resolver y leer el perfil objetivo elegido y todas las entidades canónicas referenciadas por `evidence-selection.md` y `target-profile-selection.md`, aunque después utilice solo un subconjunto. La oferta define el objetivo; no demuestra experiencia del candidato. El perfil define estrategia; tampoco crea hechos.

### `reusable_strategy`

El generador usa un archivo estratégico que debe declarar:

- perfil objetivo primario y perfiles secundarios opcionales;
- idioma, título de posicionamiento y extensión objetivo;
- selección explícita de IDs canónicos autorizados;
- prioridades de evidencia y experiencia;
- claims prohibidos, límites y gaps conocidos;
- ruta única del output.

Debe resolver y leer todos los perfiles y todos los IDs canónicos declarados antes de redactar. La estrategia selecciona y posiciona; no demuestra hechos. No requiere `application_id`, oferta, intake, plan, riesgos, lifecycle ni ninguna otra fuente de candidatura.

## Principios de generación

- Seleccionar evidencia por relevancia y fuerza, no por volumen.
- Priorizar experiencia profesional reciente y sólida; usar evidencia antigua, personal o débil solo cuando aporte un ajuste concreto.
- Conservar títulos formales, empleadores, fechas, cronología, atribución y alcance de las entidades.
- No convertir encaje parcial en dominio, liderazgo informal en título formal ni proyectos personales en experiencia profesional.
- No inventar experiencia, métricas, fechas, tecnologías, responsabilidades, títulos, empleadores, educación, certificaciones, idiomas, salario, disponibilidad ni datos de contacto.
- No convertir requisitos de la oferta en skills o experiencia del candidato.
- Omitir del CV visible los gaps y conservarlos en la auditoría.
- Redactar bullets específicos y respaldados, sin lenguaje corporativo inflado ni adjetivos genéricos.
- En `application`, seguir por defecto el idioma de la oferta, salvo instrucción distinta del plan o del usuario; en `reusable_strategy`, usar el idioma declarado por la estrategia.
- Tratar el Markdown generado en la ruta permitida por el modo como reemplazable y no canónico.

El fixture `examples/applications/job-intake-knowmad-mood-senior-backend-java/` puede utilizarse en una prueba posterior, pero no es una dependencia ni determina la estructura o el contenido del generador.
