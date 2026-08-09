# Dossier de oportunidad — [Empresa, intermediario o cliente desconocido] — [Puesto]

## 1. Metadata

- **id:** `opportunity-dossier:[application-slug]`
- **application_id:** `application:[application-slug]`
- **source_application_folder:** `[ruta]`
- **output_type:** `opportunity-dossier`
- **research_mode:** `[source_only / external_research]`
- **language:** `[idioma + base]`
- **status:** `draft`
- **application_status_at_generation:** `[estado literal + fecha/evidencia o incertidumbre]`
- **company_or_client_known:** `[true / partial / false + empresa publicada, intermediario, empleador y cliente final]`
- **source_files_used:**
  - `[ruta → uso]`
- **external_sources_used:**
  - `[ID → título/descripción → tipo → URL/ruta → autor/editor y fecha si constan → limitaciones]`
- **company_summary:** `[referencia a sección 4]`
- **product_summary:** `[referencia a sección 5]`
- **business_model:** `[referencia a sección 5 o desconocido]`
- **market_context:** `[referencia a sección 6]`
- **role_context:** `[referencia a sección 7]`
- **technical_context:** `[referencia a sección 8]`
- **operating_context:** `[referencia a sección 8]`
- **candidate_fit_implications:** `[referencia a sección 9]`
- **risks_and_unknowns:** `[referencia a sección 10]`
- **questions_to_answer_before_next_step:** `[referencia a sección 11]`
- **questions_for_recruiter:** `[referencia a sección 12]`
- **questions_for_technical_interview:** `[referencia a sección 13]`
- **decision_notes:** `[referencia a sección 14]`
- **do_not_assume:** `[referencia a sección 15]`
- **review_checklist:** `[referencia a sección 16]`
- **uncertainty:** `[referencia a sección 17]`

## 2. Qué se sabe por la candidatura

| Afirmación | Procedencia | Fuente | Confianza o límite | Relevancia |
|---|---|---|---|---|
| [Hecho de la oferta/intake/plan/registro] | `application_fact` | [ruta/sección] | [límite] | [por qué importa] |
| [Lo dicho durante el proceso] | `recruiter_statement` | [ruta/sección] | [no verificado / límite] | [por qué importa] |

### Identidad de la oportunidad

- **Empresa publicada:** [nombre o desconocido]
- **Intermediario / recruiter:** [nombre o desconocido]
- **Empleador contractual:** [nombre o desconocido]
- **Cliente final:** [nombre o desconocido]
- **Conflictos o ambigüedades:** [lista o ninguno]

## 3. Qué se sabe por investigación externa o de empresa

> En `source_only`: indicar que no se usó investigación externa y mantener `external_sources_used: []`.

| Afirmación | Procedencia | Fuente externa o nota | Fecha | Confianza o límite |
|---|---|---|---|---|
| [Dato relevante] | `external_research` | [ID de fuente] | [fecha o desconocida] | [claim corporativo / verificación / límite] |
| [Observación aportada] | `user_note` | [ID de nota] | [fecha o desconocida] | [límite] |

### Referencias pendientes sin contenido verificable

- [URL o referencia → qué habría que comprobar; no usar como respaldo]

## 4. Resumen de la empresa

- **Qué organización es:** [síntesis respaldada o desconocido]
- **Relación con esta oportunidad:** [empresa directa / intermediario / cliente / desconocido]
- **Qué parece relevante para decidir:** [hechos con procedencia]
- **Qué sigue sin saberse:** [lista]

## 5. Producto y modelo de negocio

### Producto o servicio

- **Qué hace:** [hecho respaldado o desconocido]
- **Problema que aborda:** [hecho, claim atribuido o desconocido]
- **Usuarios:** [conocidos o desconocidos]
- **Compradores / clientes:** [conocidos o desconocidos]
- **Madurez o alcance:** [respaldado o desconocido]

### Modelo de negocio

- **Cómo crea valor:** [respaldado o desconocido]
- **Cómo captura valor:** [respaldado o desconocido]
- **Quién paga:** [respaldado o desconocido]
- **Inferencias que no deben tratarse como hechos:** [lista o ninguna]

## 6. Mercado y contexto de clientes

- **Mercado o dominio:** [hecho + fuente o desconocido]
- **Tipos de cliente:** [hecho + fuente o desconocido]
- **Alternativas o competidores relevantes:** [solo si constan]
- **Regulación o restricciones:** [solo si constan]
- **Señales útiles para esta candidatura:** [lista]
- **Preguntas abiertas:** [lista]

## 7. Contexto del rol

### Conocido

- **Propósito del rol:** [literal o declaración atribuida]
- **Responsabilidades:** [lista]
- **Seniority y alcance:** [hecho o desconocido]
- **Etapa del proceso:** [snapshot factual]
- **Expectativas iniciales:** [hecho o desconocido]

### Inferido, no confirmado

- [Inferencia → base → confianza → cómo confirmarla]

### Pendiente

- [Dato del trabajo diario, alcance o éxito que falta]

## 8. Contexto técnico y operativo

| Tema | Conocido | Procedencia/fuente | Pendiente | Pregunta útil |
|---|---|---|---|---|
| Stack real vs. solicitado | [hecho] | [tipo + referencia] | [incógnita] | [pregunta] |
| Arquitectura y datos | [hecho] | [tipo + referencia] | [incógnita] | [pregunta] |
| Escala y latencia | [hecho] | [tipo + referencia] | [incógnita] | [pregunta] |
| Infraestructura y cloud | [hecho] | [tipo + referencia] | [incógnita] | [pregunta] |
| Despliegue y observabilidad | [hecho] | [tipo + referencia] | [incógnita] | [pregunta] |
| Ownership backend/plataforma | [hecho] | [tipo + referencia] | [incógnita] | [pregunta] |
| Producción y on-call | [hecho] | [tipo + referencia] | [incógnita] | [pregunta] |
| Equipo y estructura | [hecho] | [tipo + referencia] | [incógnita] | [pregunta] |
| Forma de trabajo y condiciones | [hecho] | [tipo + referencia] | [incógnita] | [pregunta] |

## 9. Implicaciones para el encaje del candidato

> Contexto derivado del análisis existente; no es evidencia nueva del candidato.

### Señales favorables ya documentadas

- [Implicación → fuente del expediente → límite]

### Aspectos que requieren aclaración o preparación

- [Implicación → qué falta → acción]

### Lo que esta investigación no demuestra

- [Claim de candidato que no puede derivarse de empresa/oferta/investigación]

## 10. Riesgos, incógnitas y red flags

| Tema | Tipo | Evidencia o ausencia | Impacto | Confianza | Cómo resolverlo |
|---|---|---|---|---|---|
| [tema] | [riesgo / incógnita / posible red flag / conflicto] | [fuente] | [decisión/preparación/negociación] | [alta/media/baja] | [acción/pregunta] |

## 11. Preguntas que resolver antes de continuar

1. **[Pregunta decisiva]**
   - **Por qué importa:** [impacto]
   - **Quién puede responder:** [recruiter / técnico / usuario / fuente]
   - **Decisión afectada:** [continuar / preparar / negociar / retirarse]

## 12. Preguntas para recruiter

### Prioridad alta

1. [¿Qué hace exactamente el producto?]
2. [¿Quiénes son los usuarios y clientes?]
3. [¿Cómo se estructura el equipo?]
4. [¿Cuál es la siguiente etapa?]
5. [¿Qué haría que alguien tuviera éxito en los primeros 3–6 meses?]

### Si queda tiempo

- [Pregunta adicional no resuelta]

## 13. Preguntas para entrevista técnica

> Preguntas preparadas para un posible interlocutor técnico; no implican que la etapa esté confirmada.

1. [¿De qué es responsable el equipo backend?]
2. [¿Qué partes de infraestructura pertenecen a los desarrolladores?]
3. [¿Qué expectativas de latencia o escala tiene este rol?]
4. [¿Cómo funciona el on-call?]
5. [Pregunta específica derivada de una incógnita real]

## 14. Notas de decisión

- **Razones respaldadas para continuar:** [lista]
- **Razones para esperar una aclaración:** [lista]
- **Aspectos que preparar:** [lista]
- **Aspectos potencialmente negociables:** [lista]
- **Criterios para retirarse:** [lista]
- **Revisión separada necesaria en plan/riesgos:** [sí/no + motivo; no modificar aquí]

## 15. Lista de supuestos prohibidos

- [No asumir que el stack pedido es el stack usado actualmente.]
- [No asumir que empresa publicada, empleador y cliente final son la misma organización.]
- [No asumir modelo de negocio, usuarios, escala, latencia, financiación o crecimiento sin fuente.]
- [No asumir ownership de infraestructura, plataforma, producción u on-call.]
- [No convertir claims públicos de empresa en hechos verificados ni en claims del candidato.]
- [No convertir una declaración de recruiter o una nota del usuario en hecho externo confirmado.]

## 16. Checklist final de revisión

- [ ] He separado empresa, intermediario, empleador y cliente final.
- [ ] Cada afirmación material tiene procedencia y fuente.
- [ ] He distinguido hechos de aplicación, declaraciones de recruiter, investigación externa, notas, inferencias e incertidumbre.
- [ ] No he usado URLs sin contenido como evidencia.
- [ ] No he inventado empresa, producto, modelo de negocio, mercado ni contexto técnico.
- [ ] Los desconocidos importantes están visibles y generan preguntas útiles.
- [ ] No he confundido requisitos del rol con realidad actual ni con experiencia del candidato.
- [ ] Company research no se ha convertido en evidencia o claim de CV.
- [ ] Las red flags están proporcionadas a la evidencia disponible.
- [ ] Las preguntas están priorizadas y dirigidas al interlocutor adecuado.
- [ ] El dossier ayuda a continuar, preparar, negociar o retirarse.
- [ ] No he cambiado plan, riesgos, conocimiento, lifecycle ni otros outputs.

## 17. Incertidumbre

- **Desconocido:** [dato → por qué importa → pregunta]
- **Inferencia:** [interpretación → premisas → confianza → límite]
- **Conflicto:** [fuentes en desacuerdo → qué no puede concluirse]
- **Fuente débil o incompleta:** [referencia → limitación]
- **Pendiente de investigación explícita:** [dato → fuente o persona potencial]

<!-- Eliminar del output generado todos los placeholders e instrucciones. Conservar secciones con `desconocido`, `[]` o `ninguno` cuando su ausencia sea informativa. -->
