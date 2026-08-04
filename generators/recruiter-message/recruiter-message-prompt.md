# Prompt reutilizable: generar mensaje a recruiter

Copia este prompt en Codex o ChatGPT y sustituye los valores entre corchetes. Debe ejecutarse desde un repositorio CareerOS con acceso a la carpeta indicada.

```text
Genera un mensaje breve a recruiter para una única candidatura de CareerOS.

Parámetros:
- source_application_folder: [career/applications/<application-slug> o examples/applications/<example-slug>]
- message_type: [clarification-first / apply / follow-up / polite-decline / auto]
- channel: [LinkedIn / email / otro / auto]
- language: [es / en / auto]
- variants: [0 / 2 / 3]

Lee primero, dentro de source_application_folder:
- job-description.md
- job-intake.md
- target-profile-selection.md
- evidence-selection.md
- application-plan.md
- risk-register.md
- submission-record.md

Si falta un archivo, no lo sustituyas con suposiciones. Evalúa las condiciones de parada y explica qué falta.

Después:

1. Confirma que el expediente tiene un intake y una selección de evidencia completos y coherentes, y que la oferta original está preservada.
2. Si message_type es auto, elige exactamente uno:
   - clarification-first cuando la recomendación sea "aplicar tras aclarar" o haya incógnitas materiales;
   - apply cuando el encaje permita aplicar sin aclaraciones bloqueantes;
   - follow-up únicamente si submission-record.md demuestra una interacción previa;
   - polite-decline cuando la decisión documentada sea no continuar o no aplicar.
3. Si se proporcionó message_type, valida que sea compatible con la recomendación, los riesgos y el historial. Detente si la contradicción no puede resolverse sin inventar.
4. Selecciona solo hechos respaldados por evidence-selection.md y por las fuentes que este referencia. Conserva los límites de risk-register.md, job-intake.md y application-plan.md.
5. No inventes experiencia, responsabilidades, tecnologías, métricas, salario, disponibilidad, interés, motivación, identidad del destinatario ni interacciones previas.
6. No conviertas requisitos de la oferta en experiencia. Si un requisito figura como gap, parcial, no respaldado o desconocido, puedes preguntar por él, pero no afirmar que se cumple.
7. Elige el idioma según la oferta y el contexto documentado del recruiter. Si no hay base suficiente y language es auto, detente y registra la incertidumbre.
8. Usa el tono profesional, claro, breve y humano. Produce un texto apto para LinkedIn o para la apertura de un email, nunca una carta larga.
9. Para clarification-first, expresa interés solo si consta, resume el encaje más fuerte en una o dos líneas y formula de dos a cuatro preguntas decisivas.
10. Para apply, presenta brevemente al candidato, usa de dos a tres señales respaldadas y pide siguientes pasos; menciona disponibilidad solo si consta.
11. Para follow-up, retoma con cortesía una interacción demostrada, reitera interés documentado y añade como máximo una aclaración o nota de disponibilidad respaldada.
12. Para polite-decline, agradece y declina claramente; da un motivo general o deja la puerta abierta solo si está respaldado.
13. Genera entre dos y tres variantes solo si el parámetro variants lo solicita. Cada variante debe cambiar de forma útil el enfoque, no los hechos.
14. Crea o reemplaza únicamente:
    source_application_folder/generated/recruiter-message.md
    Usa templates/generated/recruiter-message.template.md y cumple generators/recruiter-message/recruiter-message.schema.md.
15. Incluye en el output los claims usados y su respaldo, los claims evitados y su motivo, los riesgos, los límites de evidencia y la incertidumbre. Inicia el estado en draft.
16. Revisa el resultado con generators/recruiter-message/recruiter-message-workflow.md.
17. Detente. No generes CV, carta de presentación, cambios de LinkedIn, preparación ni respuestas de entrevista. No modifiques conocimiento canónico, perfiles objetivo ni archivos fuente del expediente.
```
