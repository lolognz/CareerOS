# Esquema de Job Intake

## Propósito

Un Job Intake representa el análisis estructurado de una oferta concreta. Vincula la fuente preservada con requisitos extraídos, perfiles objetivo, evidencia canónica, riesgos y una estrategia de generación futura. Es un artefacto de candidatura, no una entidad canónica ni una salida final.

## Campos obligatorios

| Campo | Descripción |
|---|---|
| `id` | Identificador estable del intake con formato `job-intake:<application-slug>`. |
| `application_id` | Identificador local del expediente con formato `application:<application-slug>`. |
| `source_job_description` | Ruta al archivo que conserva literalmente la oferta original y sus metadatos. |
| `company_name` | Nombre presentado por la oferta; no implica que exista una entidad canónica de empresa. |
| `role_title` | Título literal de la oferta. |
| `detected_role_family` | Familia funcional inferida, separada del título literal. |
| `seniority_level` | Seniority explícito o inferido; indicar la base y la incertidumbre. |
| `location_model` | Ubicación, presencialidad, remoto, híbrido y requisitos de residencia conocidos. |
| `contract_model` | Tipo de contratación indicado; desconocido si no consta. |
| `core_responsibilities` | Responsabilidades centrales extraídas, sin mezclarlas con requisitos. |
| `must_have_requirements` | Requisitos obligatorios o presentados como excluyentes. |
| `nice_to_have_requirements` | Requisitos deseables, opcionales o ambiguamente prioritarios. |
| `technologies_detected` | Tecnologías nombradas en la oferta, manteniendo el texto original y sin asumir experiencia del candidato. |
| `domain_detected` | Dominio de negocio o técnico detectado y base textual. |
| `leadership_expectations` | Expectativas de liderazgo técnico, gestión o autoridad formal. |
| `operational_expectations` | Producción, soporte, guardias, despliegues, infraestructura o disponibilidad esperados. |
| `target_profile_recommendation` | Un ID de perfil objetivo existente o `[]` si ninguno encaja bien. |
| `target_profile_alternatives` | IDs opcionales de perfiles existentes que aportan ángulos secundarios. |
| `target_profiles_rejected` | Perfiles considerados y descartados, con motivos; usar IDs existentes. |
| `strongest_fit_signals` | Coincidencias principales entre oferta, perfil y evidencia. |
| `weakest_fit_signals` | Desajustes, requisitos débiles o señales de perfil incorrecto. |
| `selected_roles` | IDs canónicos existentes de roles elegidos o `[]`. |
| `selected_projects` | IDs canónicos existentes de proyectos elegidos o `[]`. |
| `selected_stories` | IDs canónicos existentes de historias elegidas o `[]`. |
| `selected_skills` | IDs canónicos existentes de habilidades elegidas o `[]`. |
| `selected_technologies` | IDs canónicos existentes de tecnologías elegidas o `[]`. |
| `selected_achievements` | IDs canónicos existentes de logros elegidos o `[]`. |
| `risks` | Riesgos de encaje, candidatura, interpretación y sobreafirmación. |
| `gaps` | Requisitos no respaldados o evidencia insuficiente, sin ocultarlos. |
| `questions_to_clarify` | Preguntas que pueden cambiar la decisión, el perfil o la estrategia. |
| `recommended_outputs` | Salidas que conviene generar después, o recomendación de no generarlas/no aplicar. |
| `generation_instructions` | Directrices específicas para una generación posterior; nunca texto final. |
| `evidence_boundaries` | Límites de seniority, alcance, atribución, cronología, métricas y madurez que deben conservarse. |
| `uncertainty` | Información ausente, ambigua o inferida tanto de la oferta como de CareerOS. |

## Valores auxiliares recomendados

- `fit`: `fuerte`, `moderado`, `débil` o `sin encaje suficiente`.
- `requirement_status`: `respaldado`, `parcial`, `no respaldado`, `desconocido` o `no aplicable`.
- `recommendation`: `aplicar`, `aplicar tras aclarar`, `aplicar de forma selectiva` o `no aplicar`.
- `output_status`: `recomendado`, `opcional`, `no recomendado` o `bloqueado por información faltante`.

## Reglas de validación

- Todos los campos obligatorios deben aparecer, incluso con `[]` o `desconocido`.
- `source_job_description` debe existir antes de iniciar el análisis y conservar el texto original sin reescritura silenciosa.
- `target_profile_recommendation` admite como máximo un perfil primario.
- Todo ID de perfil debe resolver a un archivo existente bajo `career/target-profiles/`.
- Todo ID de evidencia debe resolver a una entidad existente bajo `knowledge/entities/`.
- Una tecnología de la oferta no puede pasar a `selected_technologies` si no existe evidencia canónica correspondiente.
- Las coincidencias nominales no bastan: la selección debe respetar nivel, contexto y límites de cada entidad.
- Los requisitos no respaldados permanecen en `gaps` y, si pueden inducir exageración, también en `risks`.
- El intake puede recomendar no aplicar y no debe forzar un perfil objetivo.
- `generation_instructions` guía una fase futura; no debe contener un CV, carta, mensaje o respuesta terminados.
- Las inferencias deben identificarse y conservarse en `uncertainty`.

## Esqueleto

```markdown
# Job Intake: [empresa] — [rol]

## Identificación

- **id:**
- **application_id:**
- **source_job_description:**
- **company_name:**
- **role_title:**
- **detected_role_family:**
- **seniority_level:**
- **location_model:**
- **contract_model:**

## Oferta estructurada

- **core_responsibilities:**
- **must_have_requirements:**
- **nice_to_have_requirements:**
- **technologies_detected:**
- **domain_detected:**
- **leadership_expectations:**
- **operational_expectations:**

## Encaje y evidencia

- **target_profile_recommendation:**
- **target_profile_alternatives:**
- **target_profiles_rejected:**
- **strongest_fit_signals:**
- **weakest_fit_signals:**
- **selected_roles:**
- **selected_projects:**
- **selected_stories:**
- **selected_skills:**
- **selected_technologies:**
- **selected_achievements:**

## Decisión y preparación

- **risks:**
- **gaps:**
- **questions_to_clarify:**
- **recommended_outputs:**
- **generation_instructions:**
- **evidence_boundaries:**
- **uncertainty:**
```
