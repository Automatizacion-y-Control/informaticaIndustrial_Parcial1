# 01 — Servidores de aplicación industrial

## Alcance

Qué es un servidor de aplicación, sus distintas acepciones, su función dentro
de una arquitectura industrial y su relación con Windows Server y Ubuntu
Server utilizados en los TP.

## ¿Qué es un servidor?

"Servidor" no es un único concepto: en la práctica se usa para referirse a
varias cosas distintas que conviene separar antes de hablar de "servidor de
aplicación industrial":

| Concepto | Qué significa | Ejemplo del parcial |
|---|---|---|
| **Servidor como hardware** | Equipo físico que aporta CPU, RAM, almacenamiento y red para ejecutar cargas de servidor. | La PC física podría cumplir esta función directamente, aunque en el TP actúa principalmente como host. |
| **Sistema operativo servidor** | SO preparado para administrar recursos y prestar servicios a otros equipos. | Windows Server o Ubuntu Server. |
| **Servicio servidor** | Proceso que escucha o responde a solicitudes de clientes mediante algún mecanismo de comunicación. | IIS, un servicio de archivos o el motor SQL Server. |
| **Aplicación servidor** | Software que implementa lógica y ofrece funciones o datos a clientes. | Una aplicación ASP.NET interna o una API. |
| **Servidor de aplicación** | Entorno que ejecuta y expone aplicaciones o lógica de negocio a clientes. | Windows Server con IIS/ASP.NET/WCF, según la aplicación instalada. |

Por tanto, **"servidor de aplicación industrial" no implica necesariamente un
hardware especial**. Es, conceptualmente, un servidor de aplicaciones situado
dentro de una arquitectura informática utilizada por una organización
industrial. IIS, por ejemplo, puede publicar un sitio o aplicación en Internet
o intranet; WCF permite implementar puntos de servicio que intercambian
información entre aplicaciones.

## Qué interesa de un servidor en un contexto industrial

Un servidor industrial interesa por atributos como **disponibilidad,
conectividad, seguridad, administración, escalabilidad y mantenibilidad**. No
basta con que "funcione": debe poder ser accedido por los clientes correctos,
impedir accesos indebidos, ser administrable y mantener un comportamiento
predecible. La importancia de esos criterios se vuelve evidente al pasar de
una VM aislada a modo Bridged (ver [`03_Redes_Virtuales_y_Modo_Bridged.md`](03_Redes_Virtuales_y_Modo_Bridged.md))
y luego a un recurso cloud accesible mediante Internet: una VM configurada en
Bridged adquiere acceso equivalente al de un equipo de esa red y puede
requerir firewall propio, mientras que en la nube el control de acceso, la
visibilidad y la seguridad pasan a ser cuestiones de primer orden.

## Local, virtualizado y en la nube: la misma función, distinto lugar

Un servidor de aplicación puede existir en tres formas equivalentes en
función, distintas en dónde y quién las administra:

- **Servidor local (on-premise):** la organización posee y administra
  hardware, sistema operativo, servicio y datos.
- **Servidor virtualizado:** el hardware físico es compartido mediante un
  hipervisor, pero la organización sigue administrando sistema operativo,
  servicio y datos dentro de cada máquina virtual (ver
  [`02_Virtualizacion_e_Infraestructura_Industrial.md`](02_Virtualizacion_e_Infraestructura_Industrial.md)).
- **Servicio equivalente en la nube:** un proveedor administra buena parte del
  hardware, la virtualización y hasta el sistema operativo o el motor,
  mientras el usuario conserva responsabilidad sobre acceso, credenciales y
  datos (ver [`06_Cloud_Computing_y_Migracion_Local_a_Nube.md`](06_Cloud_Computing_y_Migracion_Local_a_Nube.md)).

## Relación con Windows Server y Ubuntu Server del parcial

Windows Server demuestra el concepto instalando roles y características desde
Server Manager: IIS puede hospedar aplicaciones web y ASP.NET, mientras WCF
representa comunicación orientada a servicios (desarrollado en detalle en
[`04_Windows_Server_Roles_IIS_ASPNET_WCF.md`](04_Windows_Server_Roles_IIS_ASPNET_WCF.md)).
Ubuntu Server demuestra que un servidor no requiere entorno gráfico: puede
configurarse, verificarse y administrarse mediante terminal, shell y
utilidades de línea de comandos (ver
[`05_Ubuntu_Server_CLI_y_Administracion_Basica.md`](05_Ubuntu_Server_CLI_y_Administracion_Basica.md)).
Ambos sistemas representan **dos estrategias administrativas distintas para
la misma función de servidor**, no dos conceptos de servidor diferentes.

## Preguntas de defensa oral

| Pregunta | Respuesta técnica breve |
|---|---|
| ¿Un servidor es necesariamente una computadora física? | No. "Servidor" puede referirse al equipo, al sistema operativo o al software que presta un servicio. Una VM también puede funcionar como servidor. |
| ¿Qué función cumple IIS? | Hospeda y atiende aplicaciones o contenido web en Windows Server. |
| ¿Para qué sirve ASP.NET? | Para ejecutar aplicaciones web basadas en .NET dentro del entorno correspondiente. |
| ¿Qué es WCF? | Un framework para crear aplicaciones orientadas a servicios y comunicación entre endpoints. |
| ¿Qué diferencia hay entre un servidor local, uno virtualizado y un servicio en la nube? | La función es la misma; cambia quién administra cada capa (hardware, SO, motor) y dónde reside físicamente. |

## Fuentes principales

Documentación oficial de Microsoft Learn (Server Manager, IIS, ASP.NET, WCF)
y AWS (modelo de responsabilidad compartida), consultadas como fuentes
primarias para este eje de investigación.
