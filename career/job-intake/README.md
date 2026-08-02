# Job Intake

Job Intake es el puente entre una oferta de empleo y la preparación de una candidatura. Conserva la oferta original, extrae sus requisitos, compara la oportunidad con los perfiles objetivo, selecciona evidencia canónica y define un plan de aplicación. No genera todavía CV, carta, mensajes ni respuestas de entrevista.

## Lugar en CareerOS

```text
knowledge/                 hechos profesionales canónicos
career/target-profiles/    estrategias de posicionamiento reutilizables
career/job-intake/         método para analizar oportunidades
career/applications/       expedientes de candidaturas concretas
generated/                 salidas desechables generales
```

Dentro de una candidatura, `generated/` contiene las salidas desechables específicas de esa oportunidad. Ninguna salida se convierte en fuente canónica.

## Componentes

- [job-intake.schema.md](job-intake.schema.md): contrato del análisis estructurado.
- [job-intake-workflow.md](job-intake-workflow.md): secuencia operativa y controles.
- [job-intake-prompt.md](job-intake-prompt.md): prompt reutilizable para ejecutar el análisis.
- [index.md](index.md): navegación de la capa.
- `templates/applications/`: plantillas para cada documento de un expediente.

## Principios

- Preservar primero el texto original de la oferta, sin corregirlo ni resumirlo.
- Separar lo que dice la oferta de cualquier interpretación.
- Usar una recomendación primaria de perfil y alternativas opcionales; admitir que ninguno encaje.
- Referenciar solo IDs canónicos existentes y verificar sus límites.
- Registrar requisitos ausentes como gaps y afirmaciones inseguras como riesgos.
- Priorizar una decisión útil y auditable en menos de 24 horas.
- Detenerse tras el plan: generar materiales es una fase posterior y explícita.
