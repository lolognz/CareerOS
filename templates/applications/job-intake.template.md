# Job Intake: [empresa] — [rol]

## Identificación

- **id:** `job-intake:[slug de candidatura]`
- **application_id:** `application:[slug de candidatura]`
- **source_job_description:** `career/applications/[slug de candidatura]/job-description.md`
- **company_name:** [literal]
- **role_title:** [literal]
- **detected_role_family:** [familia + base de la inferencia]
- **seniority_level:** [explícito / inferido / desconocido + base]
- **location_model:** [ubicación, presencial/remoto/híbrido, residencia o desconocido]
- **contract_model:** [tipo o desconocido]

## Requisitos extraídos

### Responsabilidades principales

- **core_responsibilities:**
  - [responsabilidad + indicación de si es explícita o inferida]

### Requisitos obligatorios

- **must_have_requirements:**
  - [requisito + evidencia textual + condición de obligatoriedad]

### Requisitos deseables

- **nice_to_have_requirements:**
  - [requisito + evidencia textual]

### Contexto técnico y de dominio

- **technologies_detected:** [tecnologías mencionadas; no implican experiencia del candidato]
- **domain_detected:** [dominio + base textual]
- **leadership_expectations:** [técnicas, gestión, autoridad o desconocidas]
- **operational_expectations:** [producción, soporte, guardias, despliegues, infraestructura o desconocidas]
- **language_requirements:** [idiomas y nivel literal o desconocidos]
- **compensation:** [rango, moneda, periodicidad y variables o desconocida]

## Ambigüedad y señales tempranas

- **unclear_points:**
  - [punto ambiguo y por qué importa]
- **red_flags:**
  - [señal textual, interpretación conservadora e impacto posible]

## Campos consolidados del esquema

- **target_profile_recommendation:** [completar tras la comparación; un ID existente o `[]`]
- **target_profile_alternatives:** [IDs existentes o `[]`]
- **target_profiles_rejected:** [IDs existentes con motivo o `[]`]
- **strongest_fit_signals:** [lista o `[]`]
- **weakest_fit_signals:** [lista o `[]`]
- **selected_roles:** [IDs canónicos existentes o `[]`]
- **selected_projects:** [IDs canónicos existentes o `[]`]
- **selected_stories:** [IDs canónicos existentes o `[]`]
- **selected_skills:** [IDs canónicos existentes o `[]`]
- **selected_technologies:** [IDs canónicos existentes o `[]`]
- **selected_achievements:** [IDs canónicos existentes o `[]`]
- **risks:** [resumen o referencias al registro]
- **gaps:** [requisitos no respaldados o `[]`]
- **questions_to_clarify:** [preguntas priorizadas o `[]`]
- **recommended_outputs:** [outputs y estado, o recomendación de no aplicar]
- **generation_instructions:** [directrices futuras; no texto final]
- **evidence_boundaries:** [límites que toda salida debe conservar]
- **uncertainty:** [incertidumbres de oferta, inferencia y evidencia]
