# 🔎 b_investigacion

Investigación previa a la resolución del Parcial N.º 1, organizada en once
ejes temáticos que cubren de punta a punta la arquitectura "de local a la
nube": servidores de aplicación, virtualización, redes Bridged, roles de
Windows Server, Ubuntu Server y CLI, Cloud Computing, Security Groups y
puerto 1433, Amazon RDS, bases de datos relacionales, Transact-SQL y la
arquitectura integrada final.

## Contenido

| Archivo | Tema |
|---|---|
| [`promptsInvestigacion.md`](promptsInvestigacion.md) | Los once prompts de investigación originales: delimitan el alcance exacto de cada eje y qué queda fuera (SCADA/HMI, IoT, Big Data, IA/ML y unidades posteriores). |
| [`investigacion.md`](investigacion.md) | Informe de investigación consolidado (fuente original, sin dividir), del que se derivaron los once archivos temáticos siguientes. |
| [`01_Servidores_de_Aplicacion_Industrial.md`](01_Servidores_de_Aplicacion_Industrial.md) | Qué es un servidor de aplicación y sus distintas acepciones. |
| [`02_Virtualizacion_e_Infraestructura_Industrial.md`](02_Virtualizacion_e_Infraestructura_Industrial.md) | Host, guest, VM, hipervisor, ventajas y límites de virtualizar. |
| [`03_Redes_Virtuales_y_Modo_Bridged.md`](03_Redes_Virtuales_y_Modo_Bridged.md) | Bridged, NAT y Host-Only; por qué se usó Bridged en los TP. |
| [`04_Windows_Server_Roles_IIS_ASPNET_WCF.md`](04_Windows_Server_Roles_IIS_ASPNET_WCF.md) | Roles y características instalados en el TP1: IIS, ASP.NET, .NET Framework, WCF. |
| [`05_Ubuntu_Server_CLI_y_Administracion_Basica.md`](05_Ubuntu_Server_CLI_y_Administracion_Basica.md) | Terminal, shell, CLI y administración de Ubuntu Server en el TP2. |
| [`06_Cloud_Computing_y_Migracion_Local_a_Nube.md`](06_Cloud_Computing_y_Migracion_Local_a_Nube.md) | Cloud Computing, IaaS/PaaS/SaaS y qué cambia al migrar a un servicio administrado. |
| [`07_AWS_Security_Groups_Puerto_1433_y_Acceso_Remoto.md`](07_AWS_Security_Groups_Puerto_1433_y_Acceso_Remoto.md) | Security Groups, puerto 1433, "Mi IP" vs. `0.0.0.0/0` y mínimo privilegio. |
| [`08_AWS_RDS_SQL_Server_y_Endpoint.md`](08_AWS_RDS_SQL_Server_y_Endpoint.md) | Amazon RDS como servicio administrado, y el endpoint de conexión. |
| [`09_Bases_de_Datos_Relacionales_SQL_y_Uso_Industrial.md`](09_Bases_de_Datos_Relacionales_SQL_y_Uso_Industrial.md) | Base de datos, SGBD, modelo relacional y categorías DDL/DML/consulta. |
| [`10_Transact_SQL_Aplicado_a_Planta_Industrial.md`](10_Transact_SQL_Aplicado_a_Planta_Industrial.md) | El script T-SQL del parcial explicado línea por línea. |
| [`11_Arquitectura_Integrada_Local_a_Nube_para_la_Defensa.md`](11_Arquitectura_Integrada_Local_a_Nube_para_la_Defensa.md) | Síntesis de extremo a extremo y guion para defender el parcial en 5 minutos. |

Cada archivo temático incluye, además del desarrollo conceptual, una sección
de **preguntas de defensa oral** con respuestas breves y enlaces cruzados a
los demás archivos cuando un concepto se retoma en otro eje.

## Metodología

La investigación siguió una estrategia de **triangulación documental**, con
fecha de consulta al 22 de septiembre de 2026:

1. **El documento del parcial** (`a_requisitos/`) como fuente de alcance:
   determina exactamente qué debe estudiarse y qué debe excluirse.
2. **Fuentes primarias/oficiales** para las cuestiones técnicas: Oracle
   (virtualización y redes de VirtualBox), Microsoft Learn (Windows Server,
   IIS, .NET, WCF, SQL Server y T-SQL), Canonical (Ubuntu Server), AWS
   (Cloud Computing, RDS, Security Groups, endpoints) y NIST (definición
   formal de Cloud Computing).
3. **Literatura académica en español reciente**, para contextualizar
   beneficios y riesgos sin depender únicamente de documentación de
   proveedores (estudios sobre laboratorios virtualizados y sobre
   seguridad/adopción de servicios cloud).

El criterio de síntesis fue la **aplicabilidad directa al parcial**:
tecnologías contemporáneas relevantes pero fuera de alcance (contenedores,
Kubernetes, serverless, IA) se excluyeron deliberadamente porque el material
de la cátedra indica que no forman parte de este parcial.

## Vacíos de investigación y preguntas abiertas

El principal vacío es deliberado: se estudia una **arquitectura didáctica**,
no una infraestructura industrial de producción completa. El laboratorio
demuestra correctamente las capas fundamentales, pero no mide por sí mismo
disponibilidad, rendimiento, recuperación ante fallos, latencia, costos o
comportamiento bajo carga real.

Quedan además abiertas, entre otras: qué versiones exactas de Windows
Server, Ubuntu Server y VirtualBox se usaron (no altera el argumento
conceptual, pero sí rutas de configuración concretas); si las VM recibieron
IP por DHCP o configuración estática; y cómo se gestionaría en un caso real
una IP pública dinámica que invalide una regla de Security Group basada en
"Mi IP". Una implementación industrial posterior podría además profundizar
en integridad referencial, índices, respaldo, auditoría y concurrencia sobre
la base `Planta_Industrial`, deliberadamente simple en este parcial.
