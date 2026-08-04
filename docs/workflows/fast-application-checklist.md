# Checklist rápida de candidatura

Ruta de trabajo: `career/applications/<application-slug>/`

## Captura y scaffold

- [ ] La oferta merece análisis o una aclaración concreta.
- [ ] Es una candidatura real bajo `career/applications/`, no un fixture bajo `examples/applications/`.
- [ ] He creado el scaffold con `create_application.py` sin inventar argumentos.
- [ ] He pegado la oferta íntegra en `job-description.md` sin corregirla ni resumirla.
- [ ] He completado o marcado como desconocidos los metadatos relevantes.

```bash
python scripts/applications/validate_application.py RUTA
```

- [ ] La validación devuelve `PASS` o he revisado conscientemente cada `WARN`.
- [ ] No queda ningún `FAIL`.

## Intake y decisión

- [ ] He ejecutado Job Intake sin generar outputs.
- [ ] El perfil primario existe o `[]` está justificado.
- [ ] Todos los IDs seleccionados resuelven a evidencia canónica.
- [ ] Gaps, blockers, riesgos e incertidumbre siguen visibles.
- [ ] He revisado la recomendación:
  - [ ] `no aplicar`
  - [ ] `aplicar tras aclarar`
  - [ ] `aplicar de forma selectiva`
  - [ ] `aplicar`

## Siguiente acción

- [ ] `no aplicar`: no genero CV; uso `polite-decline` solo si hubo contacto.
- [ ] `aplicar tras aclarar`: genero `clarification-first`; espero antes del CV si el plan lo condiciona.
- [ ] `aplicar de forma selectiva`: elijo mensaje o CV según riesgos y dependencias.
- [ ] `aplicar`: genero CV si pasa sus precondiciones; mensaje `apply` solo si aporta valor.
- [ ] He generado un solo output autorizado, no una cadena de materiales.

## Revisión y registro

- [ ] Cada claim del output tiene evidencia y conserva sus límites.
- [ ] Ningún requisito de la oferta aparece como experiencia sin respaldo.
- [ ] No se ocultan gaps ni se infla fit parcial, liderazgo, ownership o métricas.
- [ ] He revisado manualmente idioma, fechas, títulos, contacto y audiencia.
- [ ] El estado solo cambia a `reviewed`, `sent` o `submitted` cuando corresponde.
- [ ] He actualizado `submission-record.md` después de enviar, descartar, recibir respuesta o cerrar.
- [ ] Los outputs bajo `generated/` siguen tratados como desechables.
- [ ] Antes de versionar, he revisado `git status --short` y el diff del expediente.
- [ ] Solo preparo un commit con artefactos significativos y apropiados; nunca mezclo fixtures con candidaturas reales.
