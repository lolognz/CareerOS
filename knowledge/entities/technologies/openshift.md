# Tecnología: OpenShift

## Canonical Fields

| Field | Value |
|---|---|
| id | `technology:openshift` |
| name | OpenShift |
| type | platform |
| category | devops |
| description | Plataforma profesional de destino en Deutsche Bank, utilizada directamente para despliegue, observación y troubleshooting acotados. |
| evidence_level | strong |
| chronology | Uso profesional durante el periodo de Deutsche Bank; fecha inicial exacta de cada tarea no documentada. |
| contexts | Microservicios de pagos desplegados en entornos OpenShift de Deutsche Bank. |
| related_roles | [`role:deutsche-bank-senior-backend-software-engineer`] |
| related_projects | [`project:deutsche-bank-payments-systems`] |
| related_stories | [] |
| related_skills | [`skill:microservices`, `skill:production-support-and-debugging`] |
| usage_summary | Manuel trabaja personalmente con pods y logs, reinicio o borrado de pods, deployments, escalado de réplicas, Services, ConfigMaps, Secrets y troubleshooting. Edita plantillas predefinidas utilizadas por Helm para desplegar entre entornos y trabaja con objetos OpenShift Route para exponer servicios. |
| representative_examples | `project:deutsche-bank-payments-systems` documenta el uso recurrente de OpenShift y las tareas y recursos concretos. |
| boundaries | La evidencia fuerte refleja uso profesional directo y recurrente, no expertise de administrador. No demuestra instalación o actualización de clústeres, administración u ownership de plataforma, ownership de infraestructura, experiencia con Ingress ni acceso irrestricto a comandos de infraestructura en producción. |
| evidence | `knowledge/raw/interviews/2026-08-29-post-smadex-knowledge-verification.md`; rol y proyecto relacionados. |
| uncertainty | No constan versiones, fecha inicial exacta, frecuencia por operación ni alcance completo de permisos fuera de las restricciones productivas documentadas. |
| related_entities | [`technology:kubernetes`] |
