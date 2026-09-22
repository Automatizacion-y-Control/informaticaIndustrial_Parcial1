# 06 — Cloud Computing y migración de local a la nube

## Alcance

Definición de Cloud Computing, modelos IaaS/PaaS/SaaS, qué cambia cuando una
base de datos pasa de local a un servicio administrado, y por qué "migrar a
la nube" no es simplemente copiar una computadora a Internet.

## Qué es Cloud Computing

El NIST define Cloud Computing como acceso bajo demanda a un conjunto
compartido de recursos configurables (redes, servidores, almacenamiento,
aplicaciones y servicios) que pueden aprovisionarse y liberarse rápidamente,
con esfuerzo de gestión o interacción del proveedor mínimos. AWS describe
Cloud Computing, en la misma línea, como la provisión bajo demanda de
recursos de TI.

## IaaS, PaaS y SaaS

El NIST formaliza tres modelos de servicio, que se diferencian por **cuánto
administra el proveedor frente al usuario**:

- **IaaS (Infraestructura como servicio):** el proveedor da cómputo,
  almacenamiento y red; el cliente conserva mayor control (sistema
  operativo, aplicaciones).
- **PaaS (Plataforma como servicio):** el proveedor administra además la
  plataforma de ejecución; el cliente se enfoca en la aplicación.
- **SaaS (Software como servicio):** el proveedor administra toda la pila;
  el cliente solo usa la aplicación.

Amazon RDS (ver
[`08_AWS_RDS_SQL_Server_y_Endpoint.md`](08_AWS_RDS_SQL_Server_y_Endpoint.md))
se ubica conceptualmente entre IaaS y PaaS para el caso de bases de datos: el
usuario no administra el hardware ni buena parte del sistema operativo o el
mantenimiento del motor, pero sigue siendo responsable de la conectividad
autorizada, credenciales, estructura de datos y uso de la base.

## Qué cambia al migrar una base de datos a un servicio administrado

Migrar a la nube no significa copiar una computadora a Internet. Significa
**cambiar el modelo de responsabilidad y el nivel de abstracción**: algunas
capas que antes administraba la organización (hardware, sistema operativo,
parcheado del motor) pasan a ser administradas por un proveedor. Lo que
**no** cambia es la responsabilidad del usuario sobre quién puede conectarse
(Security Group), con qué credenciales (autenticación SQL) y qué hace la
aplicación con los datos.

## Ventajas y riesgos

**Ventajas posibles:** escalabilidad, aprovisionamiento rápido, acceso desde
cualquier ubicación autorizada, mantenimiento y respaldo delegados,
disponibilidad gestionada por el proveedor.

**Riesgos e impactos:** dependencia de la conectividad a Internet, latencia,
costos recurrentes, y cuestiones de seguridad y gobernanza. Literatura
académica reciente en español identifica fuga de datos, secuestro de cuentas
y ataques de denegación de servicio (DDoS) como riesgos relevantes de la
nube, junto con la necesidad de políticas y monitoreo — es decir, **no existe
una "seguridad automática" por el simple hecho de usar un proveedor cloud**.
Una revisión sistemática de 2025 sobre adopción de IaaS/PaaS/SaaS en
educación superior resalta beneficios de adopción junto con barreras de
infraestructura, recursos y organización, reforzando que el modelo cloud
**cambia quién administra cada capa**, no elimina la necesidad de administrar.

## Aplicación al parcial

El Bloque 2 del parcial es exactamente este paso: de un servidor SQL Server
que podría instalarse localmente en una VM, a un servicio administrado
(Amazon RDS) donde AWS opera gran parte de la infraestructura y el motor,
mientras el grupo conserva la responsabilidad de configurar correctamente el
Security Group (ver
[`07_AWS_Security_Groups_Puerto_1433_y_Acceso_Remoto.md`](07_AWS_Security_Groups_Puerto_1433_y_Acceso_Remoto.md))
y de administrar la base de datos resultante (ver
[`09_Bases_de_Datos_Relacionales_SQL_y_Uso_Industrial.md`](09_Bases_de_Datos_Relacionales_SQL_y_Uso_Industrial.md)).

## Preguntas de defensa oral

| Pregunta | Respuesta técnica breve |
|---|---|
| ¿Qué es Cloud Computing? | Provisión bajo demanda de recursos de TI mediante una infraestructura de servicios compartida y aprovisionable. |
| ¿Qué es IaaS? | Infraestructura de cómputo, almacenamiento y red consumida como servicio, con mayor control del cliente que en PaaS o SaaS. |
| ¿Qué diferencia hay entre una VM con SQL Server y RDS? | En una VM administramos sistema y motor; en RDS, AWS administra más capas operativas del servicio de base de datos. |
| ¿"Migrar a la nube" elimina responsabilidades del usuario? | No; las transfiere parcialmente. El usuario sigue administrando accesos, credenciales y datos. |

## Fuentes principales

NIST (definición formal de Cloud Computing, SP 800-145); documentación de
AWS sobre Cloud Computing y modelo de responsabilidad compartida; revisión
sistemática en español (2025) sobre adopción de IaaS/PaaS/SaaS; literatura
académica (2024) sobre riesgos de seguridad en la nube.
