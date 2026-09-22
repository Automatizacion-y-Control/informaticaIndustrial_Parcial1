# 05 — Ubuntu Server, CLI y administración básica

## Alcance

Qué es Ubuntu Server, qué son terminal/shell/CLI, por qué un servidor puede
administrarse sin entorno gráfico, y los comandos básicos usados para
verificar el TP N.º 2.

## Ubuntu Server frente a un sistema de escritorio

Ubuntu Server es una distribución orientada a prestar servicios de red y de
sistema, sin depender de un entorno gráfico para funcionar. Canonical incluye
explícitamente en su documentación secciones sobre línea de comandos, redes,
seguridad y administración del sistema como el modelo normal de trabajo.

## Terminal, shell y CLI

Conviene diferenciar tres términos que suelen confundirse:

- **Terminal:** la interfaz donde el usuario interactúa (recibe lo que se
  escribe y muestra la salida).
- **Shell:** el intérprete que recibe los comandos escritos y los ejecuta.
- **CLI (Command Line Interface):** el paradigma de interacción mediante
  texto, en contraposición a una interfaz gráfica.

## Por qué un servidor puede administrarse sin GUI

Un servidor no necesita un escritorio gráfico para cumplir su función:
servicios, configuración, red y procesos pueden administrarse íntegramente
desde la shell. Esto trae ventajas habituales: menor consumo de recursos,
mayor facilidad de automatización (scripts), acceso remoto simple (SSH) y
reproducibilidad de la configuración.

## Privilegios y `sudo`

`sudo` permite ejecutar una operación puntual con privilegios elevados según
la política configurada. Para la defensa basta entender que **no todas las
tareas deben realizarse permanentemente como administrador/root**: se elevan
privilegios únicamente cuando una acción específica lo requiere.

## Configuración básica realizada en el TP

Durante el TP se configuraron, desde la CLI: el **hostname** (nombre del
equipo), la **fecha/hora** y la **red** (dirección IP, en modo Bridged —
ver [`03_Redes_Virtuales_y_Modo_Bridged.md`](03_Redes_Virtuales_y_Modo_Bridged.md)).

## Comandos básicos para la defensa

No es necesario memorizar decenas de comandos. Es mejor poder responder **qué
verifica cada uno**:

```bash
hostname
hostnamectl
date
ip addr
ip route
ping <destino>
ls
pwd
ps
systemctl status <servicio>
```

En orden: identidad del equipo, identidad y metadatos del sistema, hora,
interfaces de red, rutas, conectividad, archivos, directorio actual,
procesos y estado de un servicio.

## Comparación mínima con Windows Server

La comparación no debe plantearse como "cuál es mejor": para este parcial
representan **dos estrategias administrativas distintas** para la misma
función de servidor (ver también
[`01_Servidores_de_Aplicacion_Industrial.md`](01_Servidores_de_Aplicacion_Industrial.md)).

| Windows Server | Ubuntu Server |
|---|---|
| Administración fuertemente integrada con Server Manager y herramientas gráficas/PowerShell | Administración habitualmente basada en CLI y archivos/configuración declarativa |
| Roles y características como modelo visible de instalación | Paquetes y servicios como modelo habitual |
| IIS/.NET/WCF en el TP | CLI, hostname, red, fecha/hora en el TP |
| Puede administrarse también por terminal | Puede disponer de GUI, pero no la necesita para funcionar como servidor |

## Preguntas de defensa oral

| Pregunta | Respuesta técnica breve |
|---|---|
| ¿Qué diferencia hay entre terminal, shell y CLI? | Terminal es la interfaz; shell es el intérprete; CLI es el modo de interacción mediante comandos. |
| ¿Por qué Ubuntu Server puede funcionar sin GUI? | Porque los servicios y la configuración pueden administrarse mediante CLI; un servidor no necesita escritorio para prestar servicios. |
| ¿Para qué se usa `sudo`? | Para ejecutar puntualmente una operación con privilegios elevados, sin operar permanentemente como root. |
| ¿Qué verifica `ip addr`? | Las interfaces de red y sus direcciones IP asignadas. |

## Fuentes principales

Documentación oficial de Canonical (Ubuntu Server Documentation): línea de
comandos, redes (Netplan), seguridad y administración del sistema.
