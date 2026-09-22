# 04 — Windows Server: roles, IIS, ASP.NET y WCF

## Alcance

Qué función cumple cada rol y característica instalados en Windows Server
durante el TP N.º 1, y por qué forman parte de un servidor de aplicación.

## Roles vs. características

En Windows Server, un **rol** es una función principal que el servidor presta
a la red o a la organización (por ejemplo, servidor web); una
**característica** es una capacidad de soporte que complementa uno o varios
roles. Server Manager permite instalar y desinstalar roles y características
tanto local como remotamente.

## Componentes instalados en el TP

| Componente | Función conceptual | Por qué tiene sentido en el TP | Ejemplo industrial sencillo |
|---|---|---|---|
| **IIS** | Servidor web y plataforma de hospedaje | Demuestra que Windows Server presta un servicio a clientes | Web interna de mantenimiento |
| **ASP.NET** | Entorno para aplicaciones web .NET | Permite que IIS ejecute aplicaciones dinámicas | Registro de órdenes o fallas |
| **.NET Framework 3.5 / 4.x** | Runtime requerido por determinadas aplicaciones | Compatibilidad con software .NET | Aplicación industrial existente |
| **WCF Services** | Comunicación orientada a servicios | Ejemplifica intercambio entre cliente y servidor | Servicio que entrega información de producción |
| **ISAPI Extensions** | Integración/extensión del procesamiento en IIS | Forma parte de capacidades del servidor web | Componente web heredado |
| **IIS Management Console** | Administración de IIS | Configuración y gestión del servidor | Crear/revisar un sitio interno |
| **File and Print Services** | Compartir archivos/impresión por red | Ejemplo clásico de servicio de infraestructura | Carpeta compartida de documentos |
| **Remote Desktop Services** | Acceso remoto a sesiones/administración | Administración sin presencia física; opcional en el TP | Administrar servidor desde oficina técnica |

IIS está explícitamente diseñado para hospedar contenido en Internet o
intranet, y WCF puede operar con endpoints de servicio alojados en IIS.

## IIS, ASP.NET y WCF en detalle

**IIS** procesa solicitudes web mediante componentes como HTTP.sys, el
servicio WWW y WAS, y se integra con ASP.NET. **ASP.NET** permite ejecutar
aplicaciones web dinámicas basadas en .NET sobre ese servidor web. **WCF**
(Windows Communication Foundation) permite construir aplicaciones orientadas
a servicios, con endpoints que pueden alojarse dentro de IIS; representa el
concepto de comunicación entre aplicaciones (por ejemplo, un servicio que
entrega datos de producción a otro sistema).

## .NET Framework: evitar una respuesta histórica incorrecta

Conviene evitar decir simplemente que ".NET Framework 3.5 está obsoleto y no
debería usarse". Actualmente Microsoft señala que .NET Framework 3.5 es
tecnología antigua y aconseja buscar versiones más modernas cuando sea
posible; Windows Server 2022 incluye .NET Framework 4.8 y puede admitir
4.8.1, mientras Windows Server 2025 incluye 4.8.1. Esto convierte a 3.5
fundamentalmente en **una cuestión de compatibilidad** con aplicaciones que
aún lo requieren, no en un error de instalación: puede haberse instalado para
reproducir requisitos de compatibilidad o demostrar un componente de una
arquitectura Windows existente. La respuesta rigurosa es: ".NET Framework 3.5
puede seguir siendo necesario para aplicaciones legadas; para proyectos
nuevos Microsoft recomienda tecnologías más actuales".

## Relación con el concepto de servidor de aplicación

Estos componentes son, en conjunto, un ejemplo concreto de **servidor de
aplicación industrial** (ver
[`01_Servidores_de_Aplicacion_Industrial.md`](01_Servidores_de_Aplicacion_Industrial.md)):
un entorno (Windows Server) que ejecuta y expone aplicaciones o lógica de
negocio (IIS/ASP.NET/WCF) a clientes de una red.

## Preguntas de defensa oral

| Pregunta | Respuesta técnica breve |
|---|---|
| ¿Qué diferencia hay entre un rol y una característica? | El rol es la función principal que presta el servidor; la característica es una capacidad de soporte complementaria. |
| ¿Qué función cumple IIS? | Hospeda y atiende aplicaciones o contenido web en Windows Server. |
| ¿Para qué sirve ASP.NET? | Para ejecutar aplicaciones web basadas en .NET dentro de IIS. |
| ¿Qué es WCF? | Un framework para crear aplicaciones orientadas a servicios y comunicación entre endpoints. |
| ¿.NET Framework 3.5 es un error de instalación? | No. Sigue siendo necesario para aplicaciones legadas; para proyectos nuevos se recomiendan tecnologías más actuales. |

## Fuentes principales

Microsoft Learn: documentación de Server Manager, Internet Information
Services (IIS), ASP.NET, Windows Communication Foundation (WCF) y ciclo de
vida de .NET Framework en Windows Server 2022/2025.
