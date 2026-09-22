# 08 — Amazon RDS para SQL Server y el endpoint

## Alcance

Qué es Amazon RDS, qué significa que sea un servicio administrado, qué es el
endpoint y cómo se relaciona con el puerto y el Security Group, y qué tareas
administra AWS frente a las que siguen dependiendo del usuario.

## Qué es Amazon RDS

Amazon RDS es un **servicio administrado de base de datos relacional**. En
RDS se crea una "instancia de base de datos" eligiendo motor, almacenamiento,
CPU/memoria, redes y otras propiedades. Para este parcial, el motor
seleccionado es **Microsoft SQL Server**, aunque la infraestructura
subyacente sea operada por AWS.

## RDS frente a instalar SQL Server manualmente en una VM

| | SQL Server en una VM propia | SQL Server en Amazon RDS |
|---|---|---|
| Hardware | Organización | AWS |
| Sistema operativo base | Organización | AWS administra la plataforma subyacente |
| Parcheado y mantenimiento del motor | Organización | AWS gestiona gran parte de la operación |
| Backups | Organización debe configurarlos | AWS los administra como parte del servicio |
| Estructura de datos, credenciales, uso | Organización | Usuario/organización (**no cambia**) |
| Conectividad de acceso | Firewall propio | VPC + Security Group + endpoint |

AWS administra tareas como aprovisionamiento, backups y parcheado que en una
instalación autogestionada recaerían sobre el administrador; esto **no
elimina** las responsabilidades del usuario sobre el diseño, el acceso y el
uso de la base (ver también
[`06_Cloud_Computing_y_Migracion_Local_a_Nube.md`](06_Cloud_Computing_y_Migracion_Local_a_Nube.md)).

## Qué es el endpoint

El **endpoint** no es "la base de datos" ni una contraseña: es el **nombre
DNS** mediante el cual un cliente localiza la instancia, asociado además a un
**puerto**. Para conectarse con un cliente SQL son necesarios el endpoint y
el puerto; en SQL Server Management Studio (SSMS), ambos pueden proporcionarse
en el campo de nombre del servidor.

Un punto importante para no confundir: **el endpoint no equivale a una IP
fija**. Es un nombre DNS administrado por AWS; el cliente debe usar ese
nombre en lugar de construir dependencias sobre una dirección IP física
concreta, que podría cambiar.

## Relación entre endpoint, puerto y Security Group

```text
Cliente SQL (SSMS)
   ↓
Endpoint (nombre DNS) : Puerto (1433)
   ↓
Security Group evalúa el origen de la conexión
   ↓ (si está autorizado)
Instancia de RDS
   ↓
Motor Microsoft SQL Server
```

El puerto 1433 y la regla de origen del Security Group se desarrollan en
detalle en
[`07_AWS_Security_Groups_Puerto_1433_y_Acceso_Remoto.md`](07_AWS_Security_Groups_Puerto_1433_y_Acceso_Remoto.md).

## Accesibilidad pública frente a "puerto abierto"

Conviene distinguir **accesibilidad pública** de simplemente tener un
"puerto abierto" en el Security Group. Para conectar desde un equipo situado
fuera de la VPC, RDS debe ser alcanzable desde ese origen: una instancia
privada solo es accesible desde recursos con conectividad dentro de la VPC,
mientras que una conexión externa (como la del cliente SSMS del grupo, fuera
de AWS) requiere que la instancia tenga la arquitectura de acceso
correspondiente (en este caso, accesibilidad pública habilitada, sumada a la
regla del Security Group).

## Preguntas de defensa oral

| Pregunta | Respuesta técnica breve |
|---|---|
| ¿Qué es Amazon RDS? | Un servicio administrado de base de datos relacional: AWS opera buena parte de la infraestructura y el mantenimiento del motor. |
| ¿Qué diferencia hay entre una VM con SQL Server y RDS? | En una VM administramos sistema y motor; en RDS, AWS administra más capas operativas del servicio. |
| ¿Qué es el endpoint de RDS? | El nombre DNS utilizado por el cliente para llegar a la instancia, asociado a un puerto. |
| ¿El endpoint es una IP fija? | No, es un nombre DNS administrado por AWS; no debe asumirse como una IP fija. |
| ¿Alcanza con abrir el puerto en el Security Group para conectarse desde fuera de la VPC? | No necesariamente; además debe existir accesibilidad apropiada desde ese origen (por ejemplo, accesibilidad pública habilitada). |

## Fuentes principales

Documentación de AWS sobre Amazon RDS para SQL Server: creación de
instancias, endpoints, conectividad desde clientes externos a la VPC y
modelo de tareas administradas por el servicio.
