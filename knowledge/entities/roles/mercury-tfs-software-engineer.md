# Rol: Software Engineer — Mercury TFS

## Canonical Fields

| Field | Value |
|---|---|
| id | `role:mercury-tfs-software-engineer` |
| title | Software Engineer |
| organization | Mercury TFS |
| organization_id | `company:mercury-tfs` |
| start_date | 2020-01 aprox. |
| end_date | 2023 |
| date_precision | Inicio aproximado en enero de 2020; no consta el mes exacto de finalización. |
| location | Desconocida en la evidencia disponible |
| employment_type | Empleo; modalidad contractual exacta desconocida |
| seniority | Comenzó con experiencia práctica limitada; evolucionó hacia autonomía y referencia funcional en generación documental y contabilidad. No consta un cambio formal de título. |
| context | Desarrollo de software bancario de trade finance en una aplicación compleja con herencia monolítica y microservicios. |
| responsibilities | Desarrollo, estimación, reuniones con cliente, gestión de tareas y prioridades, revisión de código, apoyo a compañeros y responsabilidad funcional sobre generación documental y contabilidad durante parte del periodo. |
| systems | Plataforma de trade finance, microservicios de generación documental, área contable y procesos de generación de esquema de base de datos y despliegue. |
| projects | [] |
| stories | [] |
| technologies | [] |
| skills | [] |
| achievements | [] |
| evidence | `knowledge/raw/interviews/2026-07-cto-adjunto-fast-track.md` |
| uncertainty | No constan día o mes de salida, título contractual exacto, ubicación ni fechas exactas de cada etapa interna. La condición de referente se limita a determinadas áreas funcionales y periodos. |
| related_entities | [`company:mercury-tfs`] |

## Contexto

Mercury TFS desarrollaba una plataforma bancaria de trade finance para operaciones de importación y exportación intermediadas por bancos. La aplicación combinaba componentes heredados de un monolito y microservicios, y se encontraba en una fase con bastante desarrollo nuevo cuando llegó el usuario.

## Evolución del rol

Al inicio, el usuario tenía conocimientos universitarios de Java y SQL, pero no experiencia profesional con ellos. Spring, Sencha y Kubernetes eran nuevos, y los microservicios se conocían solo en teoría. Necesitaba documentación técnica detallada y encontraba especialmente difícil comprender la estructura de APIs REST.

Después de aproximadamente un año, trabajaba con mayor autonomía a partir de reuniones regulares con cliente, gestionaba sus tareas y prioridades y participaba en contacto con negocio. Tras una reorganización posterior, quedó a cargo de tareas de generación documental y trabajó en contabilidad junto a un compañero sénior. Cuando ese compañero salió, durante un periodo fue el único desarrollador que atendía ambas áreas.

En esa etapa estimaba su propio trabajo, revisaba código y ayudaba a compañeros con menos experiencia a comprender la aplicación y resolver problemas. La fuente limita su condición de referencia a determinadas áreas funcionales del equipo técnico.

## Sistemas y ámbito de trabajo

El entorno incluía Java, Spring, Spring Boot, Hibernate, SQL, Elasticsearch y Sencha, con Docker, Kubernetes, CI/CD y automatización de despliegues. No se asignan aún IDs tecnológicos porque esas entidades no existen.

Uno de los cambios técnicos documentados fue IntegrationBase. El objeto Base heredado del monolito impedía generar correctamente tablas de base de datos en microservicios y obligaba a usar scripts durante los despliegues. El usuario y un compañero identificaron la causa después de más de dos años y crearon IntegrationBase para conservar el comportamiento necesario sin esos scripts.

## Relaciones

Las áreas de contabilidad, generación documental y la plataforma de trade finance todavía no tienen entidades canónicas con IDs definidos. Los casos “account fields” e IntegrationBase tampoco tienen aún entidades de historia canónicas y no se reproducen completos en esta entidad.

## Entidades candidatas pendientes

- Proyecto candidato: plataforma de trade finance.
- Proyecto candidato: generación documental.
- Proyecto candidato: área contable.
- Historia candidata: IntegrationBase.
- Historia candidata: account fields.
- Tecnología candidata: Java.
- Tecnología candidata: Spring.
- Tecnología candidata: Spring Boot.
- Tecnología candidata: Hibernate.
- Tecnología candidata: SQL.
- Tecnología candidata: Elasticsearch.
- Tecnología candidata: Sencha.
- Tecnología candidata: Docker.
- Tecnología candidata: Kubernetes.
- Tecnología candidata: CI/CD y automatización de despliegues.

## Incertidumbre

La adquisición parcial por Banco Santander y la reorganización están documentadas en la entrevista, pero no se infieren de ellas cambios contractuales o de título. Tampoco se convierte la autonomía adquirida en una promoción formal no confirmada.

## Evidencia

- `knowledge/raw/interviews/2026-07-cto-adjunto-fast-track.md`, sección “Previous Experience: Mercury TFS”.
