# Prompts de investigación — Parcial N.º 1 de Informática Industrial

## Alcance

Estas investigaciones están limitadas a los conceptos que deben comprenderse y defenderse en el **Parcial N.º 1: Proyecto Integrador de Infraestructura Industrial (De Local a la Nube)**, tomando como base el programa de la asignatura y los TP N.º 1 y N.º 2.

No desarrollar todavía SCADA/HMI, IoT, Big Data, IA/ML ni otros contenidos de las Unidades 3 y 4, salvo una mención estrictamente necesaria para contextualizar un ejemplo industrial.

---

## 01 — `01_Servidores_de_Aplicacion_Industrial.md`

### Prompt de investigación

Investigar de manera técnica y aplicada el concepto de **servidor de aplicación industrial** para una defensa oral de Informática Industrial.

La investigación debe desarrollar únicamente:

- Qué es un servidor y qué significa específicamente “servidor de aplicación”.
- Diferencia entre servidor como hardware, sistema operativo servidor, servicio y aplicación servidor.
- Función de un servidor de aplicación dentro de una arquitectura informática industrial.
- Qué recursos o servicios puede ofrecer a clientes de una red industrial o corporativa.
- Diferencia conceptual entre servidor local (on-premise), servidor virtualizado y servicio equivalente alojado en la nube.
- Ejemplos industriales simples: aplicación web interna, servicio de datos, API/servicio web, archivos o aplicaciones de supervisión.
- Qué características interesan en industria: disponibilidad, conectividad, administración, seguridad, escalabilidad y mantenimiento.
- Relación concreta con Windows Server y Ubuntu Server utilizados en los TP.
- Preparar al final posibles preguntas de defensa oral y respuestas breves.

No convertir la investigación en una explicación general de redes ni desarrollar SCADA, IoT o Industria 4.0 más allá de ejemplos puntuales.

---

## 02 — `02_Virtualizacion_e_Infraestructura_Industrial.md`

### Prompt de investigación

Investigar **virtualización de servidores y máquinas virtuales aplicada a infraestructura informática industrial**, con foco en lo necesario para justificar los TP realizados con Oracle VirtualBox.

Desarrollar:

- Qué es virtualización.
- Conceptos de host, guest, máquina virtual, imagen ISO, disco virtual y recursos virtualizados.
- Qué es un hipervisor y dónde se ubica VirtualBox dentro de esta arquitectura.
- Diferencia conceptual entre ejecutar un sistema directamente sobre hardware y hacerlo dentro de una VM.
- Asignación de CPU, RAM, almacenamiento y adaptadores de red virtuales.
- Ventajas de virtualizar servidores: aislamiento, consolidación, pruebas, recuperación, portabilidad y aprovechamiento de hardware.
- Limitaciones y riesgos: competencia por recursos, dependencia del host, rendimiento y disponibilidad.
- Por qué la virtualización resulta útil en entornos industriales y de laboratorio.
- Relación práctica con las VM de Windows Server y Ubuntu Server del parcial.
- Preparar preguntas probables de defensa oral y respuestas técnicas breves.

No profundizar en contenedores, Kubernetes ni tecnologías no utilizadas en los TP.

---

## 03 — `03_Redes_Virtuales_y_Modo_Bridged.md`

### Prompt de investigación

Investigar la **configuración de red de una máquina virtual en modo Bridged (adaptador puente)** y justificar por qué fue utilizada en los TP de Windows Server y Ubuntu Server.

Desarrollar:

- Qué es un adaptador de red virtual.
- Qué significa modo Bridged o puente.
- Cómo se relacionan la NIC física del host, la NIC virtual de la VM y la red LAN.
- Qué dirección IP recibe normalmente la VM y por qué puede comportarse como otro equipo de la red.
- Diferencias esenciales entre Bridged, NAT y Host-Only, sin extenderse más de lo necesario.
- Comunicación VM ↔ host, VM ↔ otros equipos de la LAN y VM ↔ Internet.
- DHCP, IP, máscara, gateway y DNS únicamente en el nivel necesario para explicar la conectividad.
- Ventajas y riesgos de exponer una VM directamente a la red local.
- Cómo verificar conectividad desde Windows Server o Ubuntu Server mediante herramientas básicas.
- Aplicación concreta al parcial: por qué el modo Bridged permite demostrar un servidor accesible desde otras máquinas.
- Incluir posibles preguntas de defensa oral con respuestas concisas.

---

## 04 — `04_Windows_Server_Roles_IIS_ASPNET_WCF.md`

### Prompt de investigación

Investigar los **roles y características instalados en Windows Server durante el TP N.º 1**, explicando qué función cumple cada uno y por qué puede formar parte de un servidor de aplicación.

Desarrollar:

- Qué significa “rol” y qué significa “característica” en Windows Server.
- IIS: qué es, qué servicio ofrece y cómo participa como servidor web.
- ASP.NET: para qué sirve dentro de aplicaciones web alojadas en IIS.
- .NET Framework 3.5 y 4.8: función general dentro del entorno de ejecución de aplicaciones.
- WCF Services: concepto de servicio/comunicación entre aplicaciones y relación con servicios web.
- ISAPI Extensions: función general dentro de IIS, sin entrar en programación avanzada.
- IIS Management Console: para qué sirve administrativamente.
- File and Print Services: qué servicio de red representa.
- Remote Desktop Services: función y por qué puede utilizarse para administración remota, aclarando que en el TP era opcional.
- Relación entre estos componentes y el concepto de servidor de aplicación industrial.
- Preparar una tabla final: componente / función / por qué se instaló / ejemplo industrial.
- Añadir preguntas de defensa oral y respuestas breves.

No desarrollar programación ASP.NET ni configuración avanzada de IIS.

---

## 05 — `05_Ubuntu_Server_CLI_y_Administracion_Basica.md`

### Prompt de investigación

Investigar **Ubuntu Server como sistema operativo de servidor y su administración mediante CLI**, limitado a los conceptos necesarios para defender el TP N.º 2.

Desarrollar:

- Qué es Ubuntu Server y qué lo diferencia conceptualmente de un sistema de escritorio.
- Qué es una CLI, shell y terminal, explicadas de forma clara y diferenciada.
- Por qué un servidor puede administrarse sin entorno gráfico.
- Ventajas habituales de una administración por línea de comandos: consumo de recursos, automatización, acceso remoto y reproducibilidad.
- Conceptos básicos de usuario, privilegios administrativos y `sudo`.
- Configuración básica que se realizó en el TP: hostname, fecha/hora y red.
- Comandos básicos únicamente si sirven para verificar identidad, red, archivos, procesos o estado del sistema durante la defensa.
- Relación entre Ubuntu Server, virtualización y el modo Bridged utilizado en el laboratorio.
- Comparación conceptual mínima con Windows Server, sin convertirla en una competencia entre sistemas operativos.
- Preparar preguntas probables de defensa oral y respuestas breves.

No incluir administración Linux avanzada ni servicios que no fueron parte del TP.

---

## 06 — `06_Cloud_Computing_y_Migracion_Local_a_Nube.md`

### Prompt de investigación

Investigar **Cloud Computing y la migración de infraestructura local hacia la nube en un contexto industrial**, orientado específicamente al Bloque 2 del parcial.

Desarrollar:

- Definición técnica de Cloud Computing.
- Diferencia entre infraestructura on-premise y recursos consumidos desde la nube.
- Conceptos mínimos de IaaS, PaaS y SaaS, priorizando su utilidad para interpretar AWS y RDS.
- Qué cambia cuando una base de datos deja de ejecutarse localmente y pasa a un servicio administrado en la nube.
- Ventajas posibles: escalabilidad, aprovisionamiento, acceso, mantenimiento, respaldo y disponibilidad.
- Impactos y riesgos: dependencia de conectividad, latencia, costos, seguridad, privacidad y dependencia del proveedor.
- Responsabilidades que continúan siendo del usuario aunque el servicio esté en la nube.
- Aplicación industrial: acceso desde aplicaciones o estaciones autorizadas hacia una base de datos remota.
- Explicar por qué “migrar a la nube” no significa simplemente copiar una computadora a Internet.
- Relacionar el análisis con el recorrido del parcial: servidor local virtualizado → servicio de base de datos en AWS.
- Añadir preguntas de defensa oral con respuestas breves.

---

## 07 — `07_AWS_Security_Groups_Puerto_1433_y_Acceso_Remoto.md`

### Prompt de investigación

Investigar el **perímetro de ciberseguridad utilizado para acceder a Microsoft SQL Server en AWS**, con foco en Security Groups y el puerto TCP 1433.

Desarrollar:

- Qué es un AWS Security Group y qué recurso protege.
- Concepto de reglas de entrada y salida.
- Qué significa permitir tráfico TCP hacia un puerto específico.
- Por qué Microsoft SQL Server utiliza habitualmente TCP 1433 para conexiones de clientes.
- Qué significa restringir una regla a “My IP”.
- Qué representa una red expresada como CIDR y qué significa `0.0.0.0/0`.
- Diferencia de riesgo entre autorizar una única IP pública y exponer el puerto a todo Internet.
- Qué amenazas aumenta una exposición innecesaria de un servicio de base de datos.
- Principio de mínimo privilegio aplicado a reglas de red.
- Diferencia conceptual entre Security Group, firewall del sistema operativo y autenticación de SQL Server.
- Qué sucede en el recorrido de conexión cliente → Internet/red → Security Group → endpoint de RDS → motor SQL Server.
- Preparar respuestas claras para justificar oralmente por qué el parcial exige TCP 1433 limitado a “Mi IP”.

No desarrollar pentesting ni técnicas ofensivas.

---

## 08 — `08_AWS_RDS_SQL_Server_y_Endpoint.md`

### Prompt de investigación

Investigar **Amazon RDS para Microsoft SQL Server** únicamente en el nivel necesario para comprender y defender el aprovisionamiento solicitado en el parcial.

Desarrollar:

- Qué es Amazon RDS.
- Qué significa que sea un servicio administrado de base de datos relacional.
- Diferencia entre instalar SQL Server manualmente en una VM y utilizar RDS.
- Qué es un motor de base de datos y qué significa seleccionar Microsoft SQL Server.
- Conceptos de instancia de base de datos, almacenamiento, credenciales y conectividad.
- Qué es el Endpoint de RDS y para qué lo utiliza el cliente de base de datos.
- Relación entre endpoint, DNS, puerto TCP 1433 y Security Group.
- Qué tareas administra AWS y cuáles siguen dependiendo del usuario.
- Ventajas y limitaciones de un servicio administrado frente a un servidor local.
- Relación con el objetivo del parcial de pasar desde infraestructura local hacia una base de datos en la nube.
- Incluir un esquema lógico textual del recorrido cliente → endpoint → RDS → SQL Server → base de datos.
- Preparar preguntas de defensa oral y respuestas breves.

Evitar servicios de AWS que no intervengan directamente en el parcial.

---

## 09 — `09_Bases_de_Datos_Relacionales_SQL_y_Uso_Industrial.md`

### Prompt de investigación

Investigar los **fundamentos de bases de datos relacionales y SQL** que deben dominarse para defender la Unidad 2 y la implementación de la base `Planta_Industrial`.

Desarrollar:

- Qué es una base de datos.
- Qué es un DBMS/SGBD y diferenciarlo de la base de datos propiamente dicha.
- Qué caracteriza al modelo relacional.
- Conceptos de tabla, fila/registro, columna/campo, tipo de dato, clave primaria y relaciones, en el nivel necesario para el parcial.
- Qué es SQL y para qué sirve.
- Diferenciar de forma práctica DDL, DML y consultas, asociando cada categoría con las instrucciones utilizadas en el parcial.
- Usos industriales de una base de datos: fallas, eventos, producción, variables históricas o trazabilidad, sin profundizar en SCADA.
- Diferencia entre almacenar datos en archivos sueltos y utilizar una base de datos relacional.
- Qué problemas resuelve una estructura de datos organizada para monitoreo industrial.
- Relacionar estos conceptos con Microsoft SQL Server en AWS RDS.
- Preparar preguntas de defensa oral y respuestas breves.

No desarrollar NoSQL salvo una mención comparativa muy breve si ayuda a delimitar qué es una base relacional.

---

## 10 — `10_Transact_SQL_Aplicado_a_Planta_Industrial.md`

### Prompt de investigación

Investigar y explicar el **script Transact-SQL requerido en el parcial**, de forma que pueda ser defendido línea por línea y relacionado con conceptos de bases de datos.

La investigación debe cubrir:

- Qué es Transact-SQL (T-SQL) y su relación con SQL y Microsoft SQL Server.
- Sentencia `CREATE DATABASE` y qué objeto crea.
- Selección/uso de una base de datos cuando corresponda.
- Sentencia `CREATE TABLE`.
- Definición de columnas y tipos de datos adecuados para un ejemplo de monitoreo industrial.
- Concepto y utilidad de una clave primaria.
- Sentencia `INSERT` para cargar datos de prueba.
- Sentencia `SELECT` para consultar y verificar la información almacenada.
- Diferencia entre definir estructura, insertar datos y consultarlos.
- Proponer un ejemplo simple y defendible para `Planta_Industrial`, con una tabla de fallas, eventos o producción.
- Explicar qué resultado debe observarse para demostrar que la conexión remota y el script funcionaron correctamente.
- Identificar errores conceptuales frecuentes que podrían aparecer durante una defensa oral.
- Preparar preguntas de defensa y respuestas breves.

Mantener el script deliberadamente simple: el objetivo es demostrar comprensión de creación, carga y consulta, no programación avanzada de bases de datos.

---

## 11 — `11_Arquitectura_Integrada_Local_a_Nube_para_la_Defensa.md`

### Prompt de investigación

Construir una investigación de síntesis sobre la **arquitectura completa “de local a la nube” desarrollada en el Parcial N.º 1 de Informática Industrial**, utilizando solamente conceptos ya tratados en los informes anteriores.

La investigación debe explicar, como una única secuencia lógica:

1. PC física utilizada como host.
2. VirtualBox como plataforma de virtualización.
3. Máquinas virtuales Windows Server y Ubuntu Server.
4. Recursos asignados a cada VM.
5. Adaptador de red en modo Bridged y presencia de la VM en la LAN.
6. Windows Server como ejemplo de servidor de aplicación mediante sus roles y servicios.
7. Ubuntu Server como ejemplo de administración de servidor mediante CLI.
8. Paso conceptual desde infraestructura local hacia Cloud Computing.
9. AWS como proveedor cloud utilizado en la práctica.
10. Amazon RDS como servicio administrado de base de datos.
11. Microsoft SQL Server como motor seleccionado.
12. Security Group restringiendo TCP 1433 a la IP autorizada.
13. Endpoint de RDS como destino de la conexión remota.
14. Cliente SQL que se conecta al servidor.
15. Creación de `Planta_Industrial`, tabla industrial, `INSERT` y `SELECT`.

El informe debe incluir:

- Un diagrama lógico textual de extremo a extremo.
- Qué componente cumple cada función.
- Qué parte está en local y qué parte está en la nube.
- Qué protocolos o mecanismos intervienen únicamente cuando puedan afirmarse con seguridad a partir de la implementación.
- Puntos de seguridad críticos.
- Una sección final titulada **“Cómo explicar todo el parcial en 5 minutos”**.
- Una batería de preguntas integradoras que podría realizar la docente durante la defensa.

No incorporar tecnologías no utilizadas en el parcial.
