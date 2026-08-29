# Verificación de conocimiento posterior a Smadex — 2026-08-29

## Node.js / Deutsche Bank

- Manuel mantiene cuatro microservicios Node.js y ha realizado pequeños desarrollos en ellos.
- Los microservicios fueron heredados de otro equipo y ya estaban implementados y en funcionamiento.
- La responsabilidad comenzó aproximadamente a principios de 2025.
- El mantenimiento continuado ha requerido hasta ahora relativamente poco trabajo.
- La tarea inicial más difícil fue aplicar ingeniería inversa a los cuatro servicios para entender qué hacían y cómo funcionaban.

## Python / Mercury

- Mercury había adquirido software externo que utilizaba inteligencia artificial para analizar documentos a partir de imágenes.
- El software externo no había sido integrado con éxito en Mercury.
- Manuel analizó cómo funcionaba.
- Manuel desarrolló un pequeño programa Python que integró el software externo con el sistema de Mercury.
- El trabajo duró aproximadamente tres meses de forma intermitente, no a tiempo completo.

## Linux / Mercury

- Linux era el entorno profesional de trabajo.
- Manuel hacía un uso sustancial de la terminal.
- Utilizaba scripting Bash.
- Gestionaba Docker.
- Utilizaba Kubernetes desde la terminal, incluida la gestión y operación de pods.

## APIs / Mercury y Deutsche Bank

- El trabajo de Manuel con Java en Mercury utilizaba APIs REST.
- La integración profesional en Python del software externo de análisis documental se realizó mediante una API REST.
- En Deutsche Bank, la mayoría de las APIs con las que trabaja Manuel son REST.
- En Deutsche Bank, Manuel también trabaja con algunas APIs o servicios SOAP.

### Mercury — trabajo REST/API

- Manuel creaba y consumía APIs REST en Mercury.
- Su trabajo incluía definiciones de request y response, DTOs, códigos de estado HTTP, validaciones, gestión de errores, rutas o endpoints e implementación de APIs REST.
- Al principio del periodo en Mercury, los ingenieros sénior elaboraban los diseños técnicos y Manuel los implementaba.
- Más adelante, Manuel también elaboraba personalmente los diseños técnicos y los implementaba.
- En este trabajo de Mercury no se utilizaban Swagger ni OpenAPI.
- Para las pruebas y la verificación de APIs se utilizaban pruebas unitarias, pruebas de integración y herramientas como Insomnia o Postman.
- Las pruebas de CI/CD se ejecutaban en pipelines y, si fallaban, impedían el despliegue.
- Sonar se utilizaba para comprobaciones de calidad del código.
- No quedan verificados frameworks de testing ni productos de pipeline concretos más allá de la evidencia canónica ya existente.

### Mercury — integración REST en Python

- El software externo de análisis documental exponía una API REST.
- Manuel analizó la respuesta REST externa e implementó un consumidor de esa API.
- Después creó una API en su programa de integración para que la aplicación de Mercury pudiera consumir más fácilmente la capacidad externa.
- El programa de integración estaba todavía en una fase temprana.
- Manuel preparó también su configuración de Docker para poder desplegarlo o probarlo y para aprender y utilizar el modelo de ejecución en contenedores.
- Docker Compose se utilizó específicamente para esta integración Python.

### Deutsche Bank — REST, SOAP y OpenAPI

- Manuel crea o modifica APIs y también consume APIs.
- Los servicios del equipo son consumidos por otros sistemas con más frecuencia de la que el equipo consume servicios externos o internos.
- La mayoría de las APIs con las que trabaja Manuel son REST y algunas son SOAP.
- En SOAP, Manuel puede modificar contratos y trabaja con clientes generados.
- WSDL se utiliza para generar código; los payloads o modelos XML pueden ser suficientemente grandes como para recurrir a código generado.
- En APIs internas de Deutsche Bank, Manuel participa en la decisión y el diseño del contrato.
- Con proveedores u organizaciones externas, el equipo puede tener que adaptarse al contrato o protocolo impuesto por la parte externa.
- Un ejemplo concreto de organización externa no se considera por ello un socio de integración permanente.
- Manuel puede escribir y modificar directamente especificaciones OpenAPI, incluidos esquemas, endpoints y definiciones de request y response.
- OpenAPI se utiliza a veces como documentación y, cada vez más, también para generar código.
- Estos hechos no demuestran gobierno de APIs en toda la organización ni ownership universal de contratos.

## Docker

- Las operaciones profesionales verificadas incluyen `docker build`, `docker run`, `docker ps`, `docker logs` y `docker exec`.
- Manuel crea o modifica Dockerfiles ocasionalmente.
- Utilizó Docker Compose en la integración Python de Mercury.
- No están verificados el ownership de registros o gestión de imágenes, la configuración avanzada de volúmenes o redes ni la administración de la plataforma Docker.

## Kubernetes / OpenShift

### Mercury

- El uso de Kubernetes en Mercury se produjo en entornos de preproducción.
- Cuando Manuel dejó Mercury, el producto acababa de llegar a producción y otro equipo se encargaba de la operación de Kubernetes en producción.
- Manuel utilizaba personalmente logs de pods o contenedores, ejecutaba comandos dentro de pods, reiniciaba o eliminaba pods y realizaba troubleshooting y diagnóstico.
- Esto no implica administración de clústeres de producción, responsabilidad de escalado ni ownership de plataforma en Mercury.

### Deutsche Bank

- Manuel visualiza pods y sus logs, reinicia o elimina pods, visualiza deployments y escala réplicas.
- Trabaja con Services, ConfigMaps, Secrets, troubleshooting y diagnóstico, Helm, plantillas de despliegue y OpenShift Routes.
- Las plantillas de despliegue parten de plantillas predefinidas, pero Manuel edita las utilizadas por Helm para desplegar en distintos entornos.
- La plataforma de destino en Deutsche Bank es OpenShift.
- Las Routes son objetos OpenShift Route utilizados para exponer servicios.
- Esto no implica administración, instalación o actualización de clústeres Kubernetes/OpenShift, ownership de infraestructura o plataforma, experiencia con Ingress ni acceso irrestricto a comandos de infraestructura en producción.

## Trabajo fuera de horario / Deutsche Bank

- Algunos meses contienen varios días de trabajo fuera de horario y es inusual que un mes no contenga ninguno.
- Lo más habitual son cambios o despliegues en producción, no una guardia telefónica clásica.
- Los cambios en producción se realizan fuera del horario laboral, en periodos de poco tráfico identificados mediante monitorización como New Relic y Splunk, a menudo alrededor de medianoche.
- Manuel y su equipo organizan y controlan los despliegues y preparan las instrucciones.
- Otro equipo autorizado ejecuta los comandos restringidos en producción.
- Manuel y su equipo diagnostican los incidentes, resuelven los que pertenecen a sus sistemas y enrutan, escalan o colaboran cuando la evidencia apunta a aplicaciones móviles, mainframe u otro sistema.
- Los incidentes críticos pueden provocar un escalado telefónico fuera del horario laboral, aunque Manuel no ha recibido personalmente una llamada crítica de este tipo.
- Los incidentes no críticos pueden descubrirse a primera hora de la mañana y provocar que se repriorice el trabajo planificado para el día.
