# Workflow de Job Intake

## Objetivo operativo

Convertir una oferta detectada en un plan de candidatura fiable y utilizable en menos de 24 horas, sin generar todavía materiales finales y sin sacrificar trazabilidad por velocidad.

## Estructura recomendada de una candidatura

```text
career/applications/YYYY-MM-company-role/
  job-description.md
  job-intake.md
  target-profile-selection.md
  evidence-selection.md
  application-plan.md
  risk-register.md
  generated/
    cv.md
    cover-letter.md
    recruiter-message.md
    interview-prep.md
  submission-record.md
```

La carpeta `generated/` y `submission-record.md` se crean o completan en fases posteriores. El Job Intake termina con los seis documentos de análisis y planificación.

## Secuencia obligatoria

### 0. Crear el expediente

- Elegir un slug estable `YYYY-MM-company-role` sin inventar datos no presentes.
- Ejecutar `scripts/applications/create_application.py` con fecha, slugs, empresa y título del puesto; consultar `scripts/applications/README.md` para los argumentos opcionales.
- El script copia y renombra las seis plantillas de `templates/applications/`, crea `submission-record.md` pendiente y deja `generated/` sin materiales de candidatura.
- No usar `--force` sobre un expediente existente sin revisar antes qué archivos administrados serán sobrescritos.
- No crear salidas generadas en esta fase.

### 1. Preservar la oferta original

- Completar primero `job-description.md`.
- Guardar el texto original íntegro en un bloque claramente delimitado.
- Registrar URL, plataforma, fechas y estado solo cuando consten.
- No corregir, traducir, reordenar ni resumir el original.
- Registrar aparte cualquier nota sobre truncamiento, pérdida de formato o ausencia de secciones.

Control de salida: no continuar si falta el texto original o no está identificada su incompletitud.

Ejecutar `scripts/applications/validate_application.py RUTA` antes del análisis. Corregir cualquier `FAIL`; revisar los `WARN` o usar `--strict` cuando se requiera una captura sin advertencias.

### 2. Extraer requisitos

- Completar `job-intake.md` desde la oferta preservada.
- Separar literalidad e interpretación.
- Clasificar responsabilidades, must-have, nice-to-have, tecnologías, dominio, liderazgo y operación.
- No convertir una tecnología mencionada en experiencia del candidato.
- Registrar ubicación, contrato, idioma y compensación como desconocidos si no aparecen.
- Añadir ambigüedades, red flags y preguntas iniciales.

### 3. Seleccionar perfil objetivo

- Comparar la oferta con todos los perfiles del índice vigente.
- Elegir cero o un perfil primario.
- Añadir perfiles secundarios solo si aportan un ángulo distinto y compatible.
- Registrar perfiles rechazados y el motivo.
- Valorar señales favorables y débiles; no calcular una precisión falsa.
- Si ningún perfil encaja, declararlo y evaluar `no aplicar` o recopilar más información.

### 4. Seleccionar evidencia canónica

- Partir de la recomendación de perfil, pero verificar cada entidad en su archivo canónico.
- Elegir roles, proyectos, historias, habilidades, tecnologías y logros relevantes para esta oferta.
- Separar evidencia a enfatizar, evitar y redactar con cautela.
- No usar IDs inexistentes ni convertir candidatos pendientes en entidades.
- Trasladar todos los límites relevantes a `evidence_boundaries` y al registro de riesgos.

### 5. Evaluar encaje y riesgos

- Comparar cada requisito importante con la evidencia seleccionada.
- Registrar estado: respaldado, parcial, no respaldado, desconocido o no aplicable.
- Conservar requisitos ausentes como gaps.
- Identificar riesgos de sobreclaiming, seniority, título, atribución, métricas, actualidad, ubicación, compensación y alcance real del rol.
- Definir una mitigación que nunca consista en exagerar.

### 6. Decidir y planificar

- Emitir una recomendación: aplicar, aplicar tras aclarar, aplicar de forma selectiva o no aplicar.
- Completar estrategias para CV, carta, mensaje de recruiter, LinkedIn si aporta valor e entrevista.
- Recomendar solo las salidas necesarias.
- Formular preguntas priorizadas para recruiter o empresa.
- Mantener toda estrategia como instrucciones, no como prosa final.

### 7. Validar y detenerse

- Confirmar que la oferta original sigue intacta.
- Confirmar que cada ID enlazado existe.
- Confirmar que cada afirmación futura propuesta tiene evidencia o está marcada como gap.
- Confirmar coherencia entre perfil, evidencia, riesgos y recomendación.
- Confirmar que no se generaron CV, carta, mensajes ni respuestas de entrevista.
- Detener el workflow y entregar el plan para revisión o para una fase de generación autorizada.

## Vía rápida de menos de 24 horas

1. **Captura inmediata:** preservar la oferta y fecha de detección.
2. **Triage:** identificar requisitos excluyentes, ubicación, compensación conocida y red flags.
3. **Decisión temprana:** descartar pronto si el encaje es insuficiente o existe un bloqueo material.
4. **Análisis enfocado:** seleccionar un perfil primario y solo la evidencia necesaria.
5. **Plan mínimo viable:** definir outputs, riesgos y preguntas antes de redactar.

La velocidad reduce tiempo de preparación, no el estándar de evidencia.
