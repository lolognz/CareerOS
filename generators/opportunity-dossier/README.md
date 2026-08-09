# Generador de dossier de oportunidad

Esta capa convierte la información disponible sobre una candidatura concreta en un dossier práctico para entender la empresa o cliente, el producto, el modelo de negocio, el contexto del rol y las preguntas que siguen abiertas. Es investigación y soporte de decisión específicos de la oportunidad: no añade conocimiento profesional canónico ni describe evidencia del candidato.

## Alcance de v1

El generador trabaja sobre una única carpeta bajo `career/applications/<application-slug>/` o `examples/applications/<example-slug>/` y crea exclusivamente:

```text
<application-folder>/generated/opportunity-dossier.md
```

Puede utilizarse después del intake, cuando se conoce la empresa o cliente final, antes de una conversación con recruiter, antes de una entrevista técnica o antes de decidir si continuar, negociar o retirarse. No es un perfil corporativo para curiosidad general: siempre está ligado a un expediente.

v1 define el contrato documental. No implementa navegación web, APIs ni automatización de investigación.

## Componentes

- [opportunity-dossier.schema.md](opportunity-dossier.schema.md): campos, valores y reglas de validación.
- [opportunity-dossier-workflow.md](opportunity-dossier-workflow.md): secuencia operativa, revisión y condiciones de parada.
- [opportunity-dossier-prompt.md](opportunity-dossier-prompt.md): prompt directamente utilizable con Codex o ChatGPT.
- [`templates/generated/opportunity-dossier.template.md`](../../templates/generated/opportunity-dossier.template.md): estructura práctica del output.

## Modos de investigación

### `source_only`

Usa únicamente archivos ya presentes en la carpeta de la candidatura. No consulta fuentes externas. Todo dato empresarial ausente permanece desconocido y se transforma, cuando sea útil, en una pregunta.

### `external_research`

Además del expediente, usa fuentes entregadas explícitamente por el usuario: notas pegadas, URLs, fragmentos, resultados web ya obtenidos o rutas de archivos. El generador no visita las URLs en v1. Registra cada fuente realmente disponible y separa sus afirmaciones de los hechos del expediente.

Si una URL no viene acompañada de contenido accesible, solo puede registrarse como referencia pendiente; no demuestra lo que supuestamente contiene.

## Fuentes y fronteras

Leer primero en el expediente:

- `job-description.md`
- `recruiter-conversation.md`, si existe
- `job-intake.md`
- `application-plan.md`
- `risk-register.md`
- `submission-record.md`

Puede leerse `target-profile-selection.md` y `evidence-selection.md` solo para interpretar implicaciones de encaje ya documentadas. No se resuelven ni leen entidades canónicas para investigar la empresa o ampliar evidencia. Los CV generados y finales no son fuentes factuales. `interview-prep.md` solo puede leerse por instrucción explícita y únicamente para evitar duplicar preguntas.

El dossier distingue en cada afirmación relevante:

- **hecho de aplicación:** procede de la oferta, intake, plan, riesgos o registro;
- **declaración de recruiter:** lo dicho en una conversación documentada, sin elevarlo a hecho público verificado;
- **investigación pública o externa:** contenido de una fuente externa identificada;
- **nota del usuario:** observación o contexto aportado por el usuario;
- **inferencia:** interpretación razonable con base y límite explícitos;
- **incertidumbre:** dato desconocido, contradictorio o no verificable.

La oferta explica qué busca la empresa. La investigación pública explica empresa, producto o mercado. Las conversaciones explican qué se dijo en el proceso. El conocimiento canónico explica al candidato. Ninguna categoría sustituye a otra.

## Principios

- No inventar hechos de empresa, cliente, producto, mercado, financiación, escala, tecnología, equipo o proceso.
- Si el cliente final es desconocido, decirlo expresamente.
- Referenciar la fuente externa junto a cada afirmación cuando sea posible; una fuente no identificada conserva menor confianza.
- No copiar pasajes largos ni resumir sitios completos. Extraer solo lo que afecta a esta oportunidad.
- Evitar lenguaje promocional, valoraciones grandilocuentes y conclusiones de encaje no respaldadas.
- La investigación de empresa no es evidencia del candidato y ningún claim público puede convertirse en claim de CV.
- Ayudar a formular mejores preguntas y decisiones, no simular certeza.
- Si la identidad o el contexto cambian, regenerar o actualizar el dossier únicamente desde fuentes explícitas.

## Límites

El generador no modifica conocimiento canónico, perfiles objetivo, intake, plan, riesgos, aplicaciones existentes ni lifecycle. No crea eventos ni cambia estados. No genera CV, mensaje a recruiter, preparación de entrevista u otros outputs. Tras escribir y revisar el único dossier permitido, se detiene.
