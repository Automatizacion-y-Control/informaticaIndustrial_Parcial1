# 03 — Redes virtuales y modo Bridged

## Alcance

Qué es un adaptador de red virtual, qué significa el modo Bridged, sus
diferencias con NAT y Host-Only, y por qué se usó en los TP de Windows Server
y Ubuntu Server.

## Los tres modos de red de una VM

| Modo | VM → LAN/Internet | LAN → VM | Uso conceptual |
|---|---:|---:|---|
| **Bridged** | Sí | Sí | Servidor que debe aparecer como otro equipo de la LAN. |
| **NAT** | Sí | No directamente, salvo redirección de puertos | Guest que necesita salida sin exposición directa. |
| **Host-Only** | No hacia la LAN externa | Host ↔ VM | Laboratorio aislado entre host y VM. |

Oracle documenta comunicación directa host↔VM, VM↔VM y VM↔LAN en Bridged; con
NAT, el acceso entrante requiere port forwarding; Host-Only no llega a la red
externa.

## Qué es el modo Bridged

VirtualBox conecta la NIC virtual con una interfaz instalada en el host e
intercambia paquetes directamente con la red; desde el punto de vista de la
LAN, el guest puede aparentar estar físicamente conectado. La cadena
conceptual es:

```text
NIC física del host
        ↓
filtro/bridge de VirtualBox
        ↓
NIC virtual presentada a la VM
        ↓
TCP/IP del guest
        ↓
dirección de la LAN
        ↓
otros equipos pueden alcanzar el servidor
```

Oracle explica a nivel arquitectónico que VirtualBox intercepta/inserta
tráfico sobre la interfaz física, creando para el guest una interfaz que
aparenta conexión física a la red.

## Direccionamiento IP de la VM

Si la LAN utiliza DHCP y la VM en Bridged participa de esa misma red, puede
obtener una configuración IP coherente con ella: **dirección IP, máscara,
gateway y DNS**. El gateway permite alcanzar otras redes; DNS traduce nombres
a direcciones; DHCP automatiza el suministro de parámetros. Lo importante
para la defensa no es memorizar protocolos avanzados, sino poder explicar por
qué una VM con dirección de la LAN puede ser accedida por otros equipos.

Un punto que suele confundirse: **la VM no "copia" la IP del host**. Al
compartir la interfaz física del host, normalmente obtiene su **propia**
dirección dentro de la misma LAN, ya sea por DHCP o configuración estática.

## Cómo verificar conectividad

En Windows se puede verificar con herramientas como `ipconfig` y `ping`; en
Linux, con `ip addr`, `ip route`, `ping` y herramientas de resolución de
nombres. Ubuntu Server documenta que su configuración de red se administra
actualmente mediante Netplan y cubre DNS, DHCP y las interfaces de red (ver
también [`05_Ubuntu_Server_CLI_y_Administracion_Basica.md`](05_Ubuntu_Server_CLI_y_Administracion_Basica.md)).

## Ventajas y riesgos de exponer una VM en Bridged

Bridged es una elección coherente cuando el objetivo del laboratorio es
demostrar que el servidor virtual es accesible desde otros equipos: es
exactamente lo que exige el parcial. El riesgo es igualmente importante:
Bridged **expone más directamente la VM a la LAN**, con un acceso de red
comparable al del host, por lo que conviene considerar un firewall propio en
el guest.

## Aplicación concreta al parcial

El modo Bridged fue la elección coherente en ambos TP porque el objetivo era
demostrar un servidor accesible desde otras máquinas de la red, no solo desde
el propio host (que es lo único que garantizaría Host-Only) ni una VM que
solo necesita salida a Internet sin ser alcanzable (que alcanzaría con NAT).

## Preguntas de defensa oral

| Pregunta | Respuesta técnica breve |
|---|---|
| ¿Por qué Bridged? | Porque necesitamos que la VM pueda aparecer como otro equipo de la LAN y ser alcanzada desde otras máquinas. |
| ¿Por qué no NAT? | NAT es adecuado para salida de la VM, pero el acceso entrante no es directo sin configurar redirección de puertos. |
| ¿La VM usa la misma IP que el host? | No necesariamente; en Bridged normalmente participa en la LAN con una dirección propia. |
| ¿Qué riesgo introduce Bridged? | Expone la VM a la LAN con un nivel de acceso comparable al del host; conviene firewall propio. |

## Fuentes principales

Manual de usuario de Oracle VirtualBox (capítulo de redes: Bridged, NAT,
Host-Only); documentación de Canonical sobre configuración de red en Ubuntu
Server (Netplan, DNS, DHCP).
