# Esquema de perfil objetivo

## Propósito

Un perfil objetivo es una estrategia reutilizable para seleccionar, ordenar y presentar hechos canónicos ante una familia de oportunidades. Puede guiar la generación de CV, carta de presentación, LinkedIn y material de entrevista, pero no es una entidad canónica ni una salida final.

Los perfiles objetivo interpretan evidencia existente. No crean hechos, títulos, experiencia ni relaciones nuevas. Cuando cambia un hecho profesional, debe corregirse primero su entidad bajo `knowledge/`; cuando cambia una estrategia de posicionamiento, debe actualizarse el perfil objetivo.

## Campos

| Campo | Obligatorio | Descripción |
|---|---:|---|
| `id` | Sí | Identificador estable con formato `target-profile:<slug>`. |
| `name` | Sí | Nombre reconocible del perfil. |
| `purpose` | Sí | Familia de oportunidades y uso estratégico del perfil. |
| `target_titles` | Sí | Puestos o familias de títulos que puede orientar. |
| `best_fit_offer_signals` | Sí | Señales de una oferta que favorecen este posicionamiento. |
| `weak_fit_offer_signals` | Sí | Señales que indican encaje débil o perfil inadecuado. |
| `primary_positioning` | Sí | Ángulo profesional central, formulado como directriz. |
| `secondary_positioning` | Sí | Ángulos de apoyo que pueden activarse según la oferta. |
| `narrative_strategy` | Sí | Orden y lógica recomendados para seleccionar evidencia. |
| `must_emphasize` | Sí | Hechos o temas canónicos que normalmente deben aparecer. |
| `should_include` | Sí | Elementos útiles pero opcionales. |
| `should_deemphasize` | Sí | Hechos reales de menor relevancia para este objetivo. |
| `avoid_claims` | Sí | Afirmaciones que no deben generarse con la evidencia actual. |
| `strongest_evidence` | Sí | IDs canónicos más importantes para sostener el perfil. |
| `relevant_roles` | Sí | IDs canónicos de roles utilizables. |
| `relevant_projects` | Sí | IDs canónicos de proyectos utilizables. |
| `relevant_stories` | Sí | IDs canónicos de historias utilizables. |
| `relevant_skills` | Sí | IDs canónicos de habilidades utilizables. |
| `relevant_technologies` | Sí | IDs canónicos de tecnologías utilizables. |
| `relevant_achievements` | Sí | IDs canónicos de logros utilizables. |
| `cv_strategy` | Sí | Criterios de selección, jerarquía y extensión para futuros CV. |
| `cover_letter_strategy` | Sí | Criterios para una futura carta, no prosa final. |
| `interview_strategy` | Sí | Evidencia y límites que deben orientar la preparación. |
| `linkedin_strategy` | Sí | Criterios para una futura vista general de LinkedIn. |
| `risks` | Sí | Riesgos de encaje, percepción o sobreposicionamiento. |
| `uncertainty` | Sí | Vacíos y límites de la evidencia relevante. |
| `related_entities` | Sí | Otros IDs canónicos relacionados, sin duplicar las listas especializadas. |

## Reglas de validación

- Escribir en español y mantener el contenido compacto, estratégico y reutilizable.
- Usar un ID canónico solo si existe el archivo de la entidad correspondiente.
- Tratar `strongest_evidence` como un subconjunto priorizado de las entidades relacionadas.
- Distinguir siempre experiencia probada, transición plausible y aspiración.
- No convertir las estrategias en texto terminado de candidatura.
- No copiar narrativas completas de entidades ni crear hechos exclusivos del perfil.
- Conservar los límites de evidencia, atribución, seniority, métricas y cronología.
- Usar listas vacías cuando una categoría no aporte evidencia útil.

## Esqueleto

```markdown
# Perfil objetivo: [Nombre]

## Identidad y encaje

- **id:** `target-profile:...`
- **name:**
- **purpose:**
- **target_titles:**
- **best_fit_offer_signals:**
- **weak_fit_offer_signals:**

## Posicionamiento

- **primary_positioning:**
- **secondary_positioning:**
- **narrative_strategy:**
- **must_emphasize:**
- **should_include:**
- **should_deemphasize:**
- **avoid_claims:**

## Evidencia canónica

- **strongest_evidence:**
- **relevant_roles:**
- **relevant_projects:**
- **relevant_stories:**
- **relevant_skills:**
- **relevant_technologies:**
- **relevant_achievements:**

## Estrategia por salida

- **cv_strategy:**
- **cover_letter_strategy:**
- **interview_strategy:**
- **linkedin_strategy:**

## Límites

- **risks:**
- **uncertainty:**
- **related_entities:**
```
