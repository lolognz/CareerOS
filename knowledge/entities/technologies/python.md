# Tecnología: Python

## Canonical Fields

| Field | Value |
|---|---|
| id | `technology:python` |
| name | Python |
| type | language |
| category | general-purpose |
| description | Lenguaje utilizado tanto en DEOS como profesionalmente en una integración acotada durante el rol en Mercury TFS. |
| evidence_level | moderate |
| chronology | Uso profesional intermitente durante aproximadamente tres meses en Mercury TFS entre 2020 y 2023; fechas de DEOS no documentadas. |
| contexts | Integración profesional de software externo de análisis documental por imágenes; proyecto personal de extracción y organización de conocimiento. |
| related_roles | [`role:mercury-tfs-software-engineer`] |
| related_projects | [`project:deos`, `project:mercury-trade-finance-platform`] |
| related_stories | [`story:deos-knowledge-extraction-pipeline`] |
| related_skills | [`skill:api-design-and-integration`, `skill:automation-and-process-improvement`, `skill:knowledge-management`] |
| usage_summary | En Mercury, el usuario analizó la respuesta de la API REST de un software externo de análisis documental, implementó en Python un consumidor e hizo que el programa de integración expusiera una API para facilitar su consumo desde Mercury. Preparó Docker y Docker Compose para desplegar o probar esta integración temprana y utilizar el modelo de ejecución en contenedores. Fue trabajo intermitente durante aproximadamente tres meses. Python también está confirmado en DEOS. |
| representative_examples | `project:mercury-trade-finance-platform` conserva el uso profesional acotado; `project:deos` y `story:deos-knowledge-extraction-pipeline` delimitan el uso personal. |
| boundaries | El usuario no desarrolló el producto externo de IA ni entrenó o construyó modelos. No demuestra ownership sobre ese software, backend extenso en Python, especialización a largo plazo, librerías concretas ni que Python fuera su lenguaje principal en Mercury. |
| evidence | `knowledge/raw/interviews/2026-08-29-post-smadex-knowledge-verification.md`; solicitud del usuario para Technology Entities v1; entidades relacionadas. |
| uncertainty | No constan fechas exactas, librerías, despliegue final, volumen de código ni las partes exactas de DEOS implementadas con Python. |
| related_entities | [`technology:docker`, `technology:fastapi`] |
