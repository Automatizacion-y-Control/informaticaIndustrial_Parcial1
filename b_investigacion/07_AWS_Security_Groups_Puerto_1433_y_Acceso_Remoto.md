# 07 — AWS Security Groups, puerto 1433 y acceso remoto

## Alcance

Qué es un Security Group, por qué SQL Server usa el puerto TCP 1433, qué
significa restringir una regla a "Mi IP" frente a `0.0.0.0/0`, y el
principio de mínimo privilegio aplicado a reglas de red.

## Qué es un Security Group

Un Security Group es un **firewall virtual con estado** que controla el
tráfico entrante y saliente hacia un recurso de AWS (en este caso, la
instancia de Amazon RDS), según reglas de **protocolo, puerto y
origen/destino**. Es un control de tráfico de red, no un mecanismo de
autenticación de usuarios.

## Reglas de entrada y el puerto 1433

Se creó una regla de entrada de tipo **MSSQL**, protocolo **TCP**, puerto
**1433** (el puerto TCP predeterminado utilizado para conexiones de
Microsoft SQL Server), con origen **Mi IP**.

## "Mi IP" frente a `0.0.0.0/0`

AWS define **"Mi IP"** como la dirección IPv4 pública del equipo desde el
que se configura la regla; la consola completa automáticamente ese origen
con la máscara `/32`, es decir, **una única dirección autorizada**.
`0.0.0.0/0`, en cambio, representa **cualquier dirección IPv4**: usarlo como
origen amplía radicalmente la superficie de exposición, permitiendo
conexiones desde cualquier origen de Internet capaz de alcanzar ese puerto.

Una precisión importante: **"Mi IP" no es una identidad personal ni una
autenticación permanente**. Es una dirección IP pública observada en ese
momento; si el proveedor de Internet la cambia, la regla puede dejar de
coincidir y habrá que actualizarla.

## Por qué restringir en lugar de abrir a todo Internet: mínimo privilegio

Por el **principio de mínimo privilegio**: con la regla limitada a una sola
dirección, solo el equipo del grupo puede intentar conectarse, y la
superficie de ataque es mínima. Si el origen se hubiera dejado en
`0.0.0.0/0`, la base habría quedado publicada a todo Internet, donde existen
escáneres que recorren continuamente el puerto 1433: intentos de fuerza
bruta contra el usuario administrador, explotación de vulnerabilidades del
motor, robo o cifrado de datos mediante ransomware, y consumo de recursos
con el consiguiente costo. En un entorno industrial real, la base de datos
no se expone directamente a Internet: se ubica en una subred privada, con
acceso por VPN y usuarios con permisos mínimos; en el laboratorio se utilizó
acceso público únicamente por necesidad práctica.

## Security Group, firewall del sistema operativo y autenticación SQL: tres capas distintas

Conviene no confundir tres controles diferentes:

1. **Security Group:** decide qué tráfico de red puede *llegar* al recurso
   (capa de red/AWS).
2. **Firewall del sistema operativo:** otra capa de filtrado, dentro del
   propio servidor (no aplica del mismo modo en RDS, donde el sistema
   operativo subyacente es administrado por AWS).
3. **Autenticación SQL:** decide si las **credenciales** presentadas al
   motor son válidas, una vez que el tráfico ya fue admitido.

Un Security Group **no reemplaza** la contraseña de SQL Server: son controles
independientes y complementarios.

## El recorrido completo de la conexión

```text
Cliente SQL
   ↓
resolución DNS del endpoint
   ↓
red / Internet
   ↓
regla del Security Group
   ↓ TCP 1433 permitido desde origen autorizado
Amazon RDS
   ↓
motor Microsoft SQL Server
   ↓
autenticación SQL
   ↓
Planta_Industrial
```

## Preguntas de defensa oral

| Pregunta | Respuesta técnica breve |
|---|---|
| ¿Qué es un Security Group? | Un control de red que permite o deniega tráfico según reglas de protocolo, puerto y origen/destino. |
| ¿Por qué puerto 1433? | Es el puerto TCP predeterminado utilizado para conexiones de Microsoft SQL Server. |
| ¿Qué significa "Mi IP"? | La IPv4 pública del equipo desde el que se define la regla. |
| ¿Qué significa `0.0.0.0/0`? | Todas las direcciones IPv4; usarlo como origen expone el puerto a cualquier origen de Internet capaz de alcanzarlo. |
| ¿Un Security Group reemplaza la contraseña de SQL? | No. Una capa autoriza el tráfico de red; otra, distinta, autentica al usuario en el motor SQL Server. |

## Fuentes principales

Documentación de AWS sobre Security Groups (EC2/VPC) y sobre conexión a
instancias de RDS para SQL Server (puerto por defecto, formato CIDR).
