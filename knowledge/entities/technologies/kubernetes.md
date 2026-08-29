# Tecnología: Kubernetes

## Canonical Fields

| Field | Value |
|---|---|
| id | `technology:kubernetes` |
| name | Kubernetes |
| type | platform |
| category | devops |
| description | Plataforma utilizada profesionalmente de forma sostenida para despliegue, observación y troubleshooting acotados, sin administración de clústeres. |
| evidence_level | strong |
| chronology | Uso en preproducción en Mercury TFS aproximadamente entre 2020 y 2023; uso profesional posterior en el entorno OpenShift de Deutsche Bank. |
| contexts | Plataforma de trade finance en preproducción; microservicios de pagos desplegados sobre OpenShift en Deutsche Bank. |
| related_roles | [`role:deutsche-bank-senior-backend-software-engineer`, `role:mercury-tfs-software-engineer`] |
| related_projects | [`project:deutsche-bank-payments-systems`, `project:mercury-trade-finance-platform`] |
| related_stories | [] |
| related_skills | [`skill:microservices`] |
| usage_summary | En Mercury utilizó Kubernetes en preproducción para consultar logs de pods o contenedores, ejecutar comandos dentro de pods, reiniciar o eliminar pods y diagnosticar problemas; la operación de producción correspondía a otro equipo cuando dejó la empresa. En Deutsche Bank trabaja sobre OpenShift con pods, logs, reinicios o borrado, deployments, escalado de réplicas, Services, ConfigMaps, Secrets y troubleshooting, además de editar plantillas de despliegue usadas por Helm y trabajar con OpenShift Routes. |
| representative_examples | `project:mercury-trade-finance-platform` delimita el uso de preproducción; `project:deutsche-bank-payments-systems` documenta el uso recurrente en OpenShift y los recursos y tareas concretos. |
| boundaries | La evidencia fuerte refleja uso directo, sostenido y concreto, no expertise administrativa. No demuestra administración, instalación o actualización de clústeres, ownership de plataforma o infraestructura, experiencia con Ingress, operación productiva de Kubernetes en Mercury ni acceso irrestricto a comandos de infraestructura en producción. |
| evidence | Fuente raw, sección “Mercury TFS”; `knowledge/raw/interviews/2026-08-29-post-smadex-knowledge-verification.md`; rol y proyecto relacionados. |
| uncertainty | No constan versiones, distribución de frecuencia por tarea ni permisos exactos fuera de las restricciones productivas documentadas. |
| related_entities | [`technology:ci-cd`, `technology:docker`, `technology:linux`, `technology:openshift`] |
