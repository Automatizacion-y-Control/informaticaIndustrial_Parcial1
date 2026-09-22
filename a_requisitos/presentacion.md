# presentacion.md

# Presentación — Parcial N.º 1 · Informática Industrial

## De local a la nube  
**Infraestructura informática industrial: servidores virtuales y base de datos en AWS**

Este documento define, diapositiva por diapositiva, la estructura de la defensa.  
El contenido actual de las 28 láminas se considera **obligatorio y se conserva**. El rediseño puede reorganizarlo, jerarquizarlo, convertirlo en diagramas o mejorar su composición. El speech se utiliza de manera **sumativa**: agrega contexto, causas, consecuencias, decisiones o conclusiones breves sin sustituir lo que ya comunica cada diapositiva.

La identidad visual debe seguir `diseño.md`.

---

# Criterios generales

- Formato 16:9.
- Estilo editorial técnico-industrial contemporáneo.
- Fondo claro en la mayoría de las diapositivas.
- Fondos oscuros solo en portada, separadores y cierre cuando corresponda.
- Títulos alineados a la izquierda.
- Pie uniforme:
  - izquierda: `UTN FRC · Licenciatura en Automatización y Control`
  - centro: `Informática Industrial · Parcial N.º 1`
  - derecha: `N / 28`
- Capturas técnicas grandes, recortadas y legibles.
- Código en Consolas.
- No eliminar ningún dato técnico del contenido original.
- El speech no se vuelca completo en pantalla: se usa para enriquecer visualmente.
- Nombres y legajos se mantienen visibles.
- Datos sensibles se anonimizan según `diseño.md`.

---

# Índice de diapositivas

| N.º | Nombre |
|---:|---|
| 01 | De local a la nube |
| 02 | Estructura de la defensa |
| 03 | Servidor de aplicación industrial |
| 04 | Virtualización en producción |
| 05 | Windows Server 2022 en VMware |
| 06 | Creación de la VM y partición del disco |
| 07 | Red Bridged y conectividad |
| 08 | Roles instalados y para qué sirven |
| 09 | Roles y características instalados |
| 10 | IIS y ASP.NET funcionando desde la red |
| 11 | Ubuntu Server 26.04.1 LTS en VMware |
| 12 | Partición: usar los 40 GB con LVM |
| 13 | Red, hora y conectividad |
| 14 | Ubuntu Server y la línea de comandos |
| 15 | Red en modo Bridged |
| 16 | Migrar la infraestructura a la nube |
| 17 | Creación de la cuenta de AWS |
| 18 | Responsabilidad compartida |
| 19 | Security Group para SQL Server |
| 20 | 1433: Mi IP versus todo Internet |
| 21 | SQL Server Express en Amazon RDS |
| 22 | Instancia disponible y punto de enlace |
| 23 | Del cliente local a la base en AWS |
| 24 | Conexión desde SSMS al Endpoint |
| 25 | Base de datos y tabla de monitoreo |
| 26 | Carga de datos y consulta |
| 27 | Conclusiones |
| 28 | Preguntas |

---

# 01 — De local a la nube

## Tipo
Portada.

## Expone
**Emiliano Casali**

## Tiempo orientativo
**20 s**

## Objetivo
Presentar el tema, el grupo y el hilo conductor de toda la defensa: la evolución desde servidores virtualizados en una PC local hasta una base de datos administrada en AWS, manteniendo la seguridad como criterio transversal.

## Contenido obligatorio
- `Parcial N.º 1 · Proyecto integrador`
- **De local a la nube**
- `Infraestructura informática industrial: servidores virtuales y base de datos en AWS`
- `Informática Industrial · UTN FRC · Licenciatura en Automatización y Control`
- Integrantes:
  - Casali, Emiliano — 210237
  - Del Soto, Juan Gustavo — 421822
  - Ferrero, Facundo José — 420841
  - Vera, Cristian Gonzalo — 420581

## Aporte del speech
La apertura debe establecer en una frase el recorrido completo:

> servidores virtuales locales → nube → base de datos administrada, con seguridad en cada capa.

No hace falta imprimir esta frase completa si la composición ya la expresa mediante el gráfico.

## Composición visual
- Fondo `azul_profundo`.
- Lado izquierdo: bloque tipográfico con título y subtítulo.
- Lado derecho: diagrama lineal simple:
  - PC local
  - máquinas virtuales
  - red
  - nube AWS
  - base de datos
- Conectores en `teal`.
- Logo UTN pequeño y monocromático.
- Integrantes y legajos en la zona inferior.
- Sin numeración visible.

## Elemento dominante
El título **DE LOCAL A LA NUBE**.

---

# 02 — Estructura de la defensa

## Tipo
Agenda visual.

## Expone
**Emiliano Casali**

## Tiempo orientativo
**20 s**

## Objetivo
Mostrar el recorrido de la exposición antes de comenzar el contenido técnico.

## Contenido obligatorio
Tres bloques:

### 1. Infraestructura local y virtualización
Servidor de aplicación industrial, TP1 Windows Server y TP2 Ubuntu Server en VMware.

### 2. Migración a la nube y ciberseguridad
Ventajas del cloud, cuenta de AWS y Security Group con el puerto 1433.

### 3. Implementación y demostración
RDS SQL Server Express, conexión desde SSMS y script Transact-SQL.

También debe conservarse la asignación de expositores:
- Emiliano: apertura, servidor, virtualización y TP1.
- Gustavo: roles e IIS, TP2 y red.
- Facundo: nube, AWS y Security Group.
- Cristian: RDS, SSMS, T-SQL y cierre.

## Aporte del speech
Reforzar verbalmente que el recorrido es progresivo:
**local → nube → implementación**.

## Composición visual
- Fondo claro.
- Una línea de recorrido horizontal con tres grandes estaciones numeradas.
- Cada bloque tiene:
  - número;
  - nombre;
  - una frase descriptiva.
- Los nombres de los expositores aparecen abajo como una banda secundaria, no como texto protagonista.

## Elemento dominante
El recorrido de tres bloques.

---

# 03 — Servidor de aplicación industrial

## Tipo
Concepto + diagrama.

## Expone
**Emiliano Casali**

## Tiempo orientativo
**35 s**

## Objetivo
Definir qué es un servidor de aplicación industrial y relacionarlo con servicios concretos de planta.

## Contenido obligatorio
Definición:

> Equipo, físico o virtual, que ejecuta de forma continua los servicios de los que depende la planta.

Servicios:
- **SCADA:** supervisión y control de procesos.
- **Historiador:** registro de datos y tendencias.
- **Servidor OPC:** enlace con PLC y equipos de campo.
- **Base de datos:** eventos, producción y trazabilidad.

Condición de operación:
- disponibilidad;
- usuarios y permisos;
- respaldos;
- monitoreo;
- funcionamiento 24/7.

## Aporte del speech
Agregar la relación con la propia defensa:
- Windows Server + IIS;
- Ubuntu Server;
- SQL Server en AWS.

La idea adicional es que un servidor no es simplemente “una PC”; su función está definida por continuidad, servicios, seguridad y administración.

## Composición visual
- Diagrama central.
- Nodo principal: **Servidor de aplicación industrial**.
- Cuatro nodos conectados: SCADA, Historiador, OPC, Base de datos.
- En una banda inferior: `24/7 · permisos · backups · monitoreo`.
- En un lateral pequeño: `En esta defensa: Windows · Ubuntu · SQL Server`.

## Elemento dominante
El diagrama funcional del servidor.

---

# 04 — Virtualización en producción

## Tipo
Comparativa técnica.

## Expone
**Emiliano Casali**

## Tiempo orientativo
**35 s**

## Objetivo
Diferenciar hipervisores tipo 1 y tipo 2 y justificar el uso de VMware Workstation en el laboratorio.

## Contenido obligatorio

### Tipo 1 — bare metal
- corre directamente sobre el hardware;
- ejemplos: VMware ESXi y Hyper-V;
- uso de producción.

### Tipo 2 — hosted
- corre sobre un sistema operativo anfitrión;
- ejemplos: VMware Workstation y VirtualBox;
- utilizado en laboratorio.

### Ventajas
- consolidación;
- aislamiento;
- snapshots;
- migración de VMs;
- recuperación ante desastres.

## Aporte del speech
- VMware Workstation y VirtualBox pertenecen al mismo tipo.
- La elección de VMware no altera el objetivo del TP.
- Riesgo conceptual: si no existe redundancia, el host puede ser un punto único de falla.

## Composición visual
Dos columnas simétricas:
- izquierda: Tipo 1, esquema `hardware → hipervisor → VMs`;
- derecha: Tipo 2, esquema `hardware → SO host → hipervisor → VMs`.

Abajo:
- una línea horizontal con las ventajas.
- un callout pequeño: `Laboratorio: VMware Workstation`.

## Elemento dominante
La comparación gráfica Tipo 1 / Tipo 2.

---

# 05 — Windows Server 2022 en VMware

## Tipo
Evidencia + ficha técnica.

## Expone
**Emiliano Casali**

## Tiempo orientativo
**35 s**

## Objetivo
Presentar el resultado general del TP1 y resumir la configuración implementada.

## Contenido obligatorio
- Hipervisor: VMware Workstation.
- Sistema: Windows Server 2022 Standard — Desktop Experience.
- Memoria: 4 GB.
- Disco: 40 GB.
- Red: Bridged (VMnet0).
- Nombre: `SRV-IND01`.
- Zona horaria: Argentina.
- Evidencia: Administrador del servidor en funcionamiento.

## Aporte del speech
- 4 GB supera el mínimo de 2 GB.
- Se eligió Desktop Experience porque el TP requiere trabajar con el Administrador del servidor.
- Postinstalación: hostname, zona horaria, conectividad.
- Snapshots y VMware Tools como buenas prácticas.
- Existieron problemas de arranque EFI y Bridged, desarrollados luego.

## Imagen
`09_cp10_administrador_servidor.png`

## Composición visual
- Captura protagonista a la derecha, aproximadamente 60 %.
- Ficha técnica a la izquierda.
- Los valores importantes (`4 GB`, `40 GB`, `Bridged`, `SRV-IND01`) se resaltan tipográficamente.

## Elemento dominante
La evidencia del servidor operativo.

---

# 06 — Creación de la VM y partición del disco

## Tipo
Doble evidencia.

## Expone
**Emiliano Casali**

## Tiempo orientativo
**20 s**

## Objetivo
Probar que la VM fue creada con los recursos pedidos y que Windows utiliza prácticamente la totalidad del disco asignado.

## Contenido obligatorio
- 2 CPU.
- 4 GB de RAM.
- disco virtual de 40 GB.
- red Bridged.
- disco de 39,98 GB utilizado.
- sistema C: de 39,33 GB NTFS.

## Aporte del speech
La lectura visual debe ser:
**configuración asignada → comprobación dentro del sistema operativo**.

## Imágenes
- `04_cp04_resumen_creacion_vm.png`
- `10_cp11_administracion_discos.png`

## Composición visual
Dos grandes capturas 50/50:
1. resumen del asistente;
2. Administración de discos.

Cada imagen lleva una etiqueta corta:
- `RECURSOS ASIGNADOS`
- `ESPACIO UTILIZADO`

Debajo: una línea de verificación:
`40 GB asignados → 39,98 GB detectados`.

## Elemento dominante
La comparación entre asignación y uso real.

---

# 07 — Red Bridged y conectividad

## Tipo
Problema → causa → corrección → resultado.

## Expone
**Emiliano Casali**

## Tiempo orientativo
**35 s**

## Objetivo
Mostrar un problema real de configuración de red y cómo fue diagnosticado y resuelto.

## Contenido obligatorio
- VMnet0 en Bridged.
- placa Wi-Fi física.
- conectividad a Internet.
- ping sin pérdidas.
- problema: VMnet0 apuntaba al adaptador Wi-Fi Direct virtual.
- solución: asociarlo al adaptador físico.

## Aporte del speech
Secuencia técnica:
1. VM obtiene `169.254.xxx.xxx`: no recibió DHCP.
2. Causa: VMnet0 enlazada al adaptador Wi-Fi Direct virtual.
3. Solución transitoria: NAT.
4. Solución definitiva: Virtual Network Editor → placa Intel física.
5. Resultado: VM integrada a la red local y ping correcto.

## Imágenes
- `12_cp22_vmnet0_bridged_wifi.png`
- `14_cp26_ping_vm_internet.png`

## Datos sensibles
- Las IP locales deben mostrarse con último octeto anonimizado:
  - `192.168.1.xxx`
  - `192.168.64.xxx`
- No mostrar IP pública.

## Composición visual
Una franja superior con cuatro etapas:
`PROBLEMA → CAUSA → CORRECCIÓN → RESULTADO`

Debajo:
- captura de VMnet0;
- captura de ping;
- flechas y etiquetas muy breves.

## Elemento dominante
La historia de resolución del problema.

---

# 08 — Roles instalados y para qué sirven

## Tipo
Matriz funcional.

## Expone
**Gustavo Del Soto**

## Tiempo orientativo
**40 s**

## Objetivo
Justificar cada rol de Windows Server desde un caso de uso industrial.

## Contenido obligatorio
- IIS → servidor web, HMI web, reportes y APIs.
- ASP.NET → páginas y servicios dinámicos.
- ISAPI Extensions → compatibilidad/extensión de IIS.
- Consola de IIS → administración.
- .NET 3.5 y 4.8 → runtimes para software heredado y actual.
- WCF → integración entre sistemas.
- Archivos e impresión → recetas, registros e impresión de etiquetas.

## Aporte del speech
Relacionar cada componente con un ejemplo industrial concreto:
- tablero de producción;
- SCADA ↔ base de datos;
- compatibilidad con software industrial heredado;
- carpetas de recetas y registros.

## Composición visual
No usar una tabla pesada de siete filas.

Agrupar en tres familias:
1. **Web** — IIS, ASP.NET, ISAPI.
2. **Compatibilidad e integración** — .NET, WCF.
3. **Servicios de planta** — archivos e impresión.

Cada familia con una breve explicación.

## Elemento dominante
La relación **rol técnico → utilidad industrial**.

---

# 09 — Roles y características instalados

## Tipo
Evidencia técnica.

## Expone
**Gustavo Del Soto**

## Tiempo orientativo
**15 s**

## Objetivo
Demostrar que los roles y características indicados en la diapositiva anterior están realmente instalados.

## Contenido obligatorio
Comando:
`Get-WindowsFeature | Where-Object Installed`

Elementos verificados:
- IIS;
- ASP.NET 4.8;
- ISAPI;
- Consola;
- .NET Framework 3.5 y 4.8;
- WCF;
- servicios de archivos;
- servicios de impresión.

## Aporte del speech
Dato adicional relevante:
`.NET 3.5` requirió montar la ISO y utilizar:
`D:\sources\sxs`.

## Imagen
`17_cp16_caracteristicas_instaladas.png`

## Composición visual
- Captura PowerShell grande.
- A la derecha, checklist de verificación.
- Callout pequeño de `.NET 3.5 → ISO / sources\sxs`.

## Elemento dominante
La captura real de verificación.

---

# 10 — IIS y ASP.NET funcionando desde la red

## Tipo
Prueba funcional.

## Expone
**Gustavo Del Soto**

## Tiempo orientativo
**25 s**

## Objetivo
Demostrar que IIS y ASP.NET no solo están instalados, sino que funcionan y son accesibles desde otro equipo de la red.

## Contenido obligatorio
- IIS accesible desde la PC anfitriona.
- `test.aspx` operativo.
- el rol IIS responde por red.
- ASP.NET ejecuta código del servidor.
- la VM es alcanzable.

## Aporte del speech
- `test.aspx` muestra el hostname del servidor.
- Se tomaron snapshots en tres hitos para permitir recuperación.

## Imágenes
- `20_cp28_iis_desde_host.png`
- `21_cp19_aspnet_test.png`

## Datos sensibles
La URL debe mostrarse como:
`http://192.168.1.xxx`

## Composición visual
Dos evidencias grandes:
- IIS;
- ASP.NET.

Abajo, tres verificaciones:
`RESPONDE POR RED`
`EJECUTA CÓDIGO`
`SERVIDOR ALCANZABLE`

## Elemento dominante
Las dos evidencias de funcionamiento.

---

# 11 — Ubuntu Server 26.04.1 LTS en VMware

## Tipo
Evidencia + ficha técnica.

## Expone
**Gustavo Del Soto**

## Tiempo orientativo
**30 s**

## Objetivo
Presentar el entorno base del TP2 y su configuración general.

## Contenido obligatorio
- VMware Workstation 16.
- Ubuntu Server 26.04.1 LTS.
- 4 GB RAM.
- disco de 40 GB.
- `/` ampliado posteriormente a 38 GB.
- red Bridged.
- hostname `srv-ubuntu01`.
- usuario con `sudo`.
- zona horaria Córdoba.
- primer login.

## Aporte del speech
- versión LTS elegida por soporte a largo plazo;
- usuario con sudo en lugar de root por seguridad y trazabilidad;
- OpenSSH instalado para administración remota;
- el primer login evidencia versión, kernel, IP y espacio inicial de `/`.

## Imagen
`34_ubuntu_primer_inicio_consola.png`

## Datos sensibles
- IP: `192.168.1.xxx`
- Usuario de login puede representarse como `usuario@srv-ubuntu01` si aparece en una recreación gráfica.
- Si la captura original muestra el usuario real, puede recortarse si no aporta.

## Composición visual
Similar a la slide 5 para crear paralelismo Windows/Ubuntu:
- ficha técnica;
- captura grande.

## Elemento dominante
La consola real del primer login.

---

# 12 — Partición: usar los 40 GB con LVM

## Tipo
Proceso técnico.

## Expone
**Gustavo Del Soto**

## Tiempo orientativo
**35 s**

## Objetivo
Explicar cómo se extendió el volumen lógico raíz para utilizar todo el espacio disponible.

## Contenido obligatorio
Comandos:
- `lsblk`
- `sudo lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv`
- `sudo resize2fs /dev/ubuntu-vg/ubuntu-lv`
- `df -h /`

Resultado:
`/ pasa de 19 GB a 38 GB, en línea y sin reiniciar.`

## Aporte del speech
Explicar la cadena:
- disco físico de 40 GB;
- partición LVM de aproximadamente 38 GB;
- volumen lógico raíz creado inicialmente con ~19 GB;
- extensión del LV;
- expansión del filesystem;
- verificación final.

## Imágenes
- `36_ubuntu_lsblk_antes.png`
- `37_ubuntu_lvextend.png`
- `38_ubuntu_resize2fs_df.png`

## Composición visual
Diagrama horizontal:
`19 GB → lvextend → resize2fs → 38 GB`

Debajo, las capturas o terminales correspondientes.

## Elemento dominante
El cambio **19 GB → 38 GB**.

---

# 13 — Red, hora y conectividad

## Tipo
Panel de verificaciones técnicas.

## Expone
**Gustavo Del Soto**

## Tiempo orientativo
**35 s**

## Objetivo
Demostrar que Ubuntu quedó correctamente configurado en red, hora y nombre, y registrar los problemas reales encontrados.

## Contenido obligatorio
- `ip a`.
- IP de la interfaz.
- ping a `8.8.8.8` sin pérdidas.
- zona horaria: `America/Argentina/Cordoba`.
- ping PC ↔ VM.
- problema de teclado.
- problema IPv6 con `google.com`.

## Aporte del speech
- teclado virtual incorrecto → administración por SSH.
- IPv6 sin ruta → `ping -4` funciona.
- hostname configurado con `hostnamectl`.
- hora configurada con `timedatectl`.

## Imágenes sugeridas
- `39_ubuntu_timedatectl.png`
- `40_ubuntu_hostnamectl.png`
- `43_ubuntu_ip_ping_8_8_8_8.png`
- `44_ubuntu_ping_ipv4_google.png`
- `45_ubuntu_ping_host_vm.png`

No es obligatorio mostrar todas simultáneamente: se pueden componer como evidencia principal + miniaturas.

## Datos sensibles
- IP local anonimizada como `192.168.1.xxx`.
- IPv6 parcialmente ocultada.

## Composición visual
Tres verificaciones grandes:
- RED
- HORA
- HOSTNAME

Abajo, dos pequeñas incidencias:
- teclado;
- IPv6.

## Elemento dominante
La condición **servidor configurado y alcanzable**.

---

# 14 — Ubuntu Server y la línea de comandos

## Tipo
Concepto + evidencia.

## Expone
**Gustavo Del Soto**

## Tiempo orientativo
**25 s**

## Objetivo
Justificar el uso de una administración sin GUI y mostrar el acceso remoto por SSH.

## Contenido obligatorio
Ventajas:
- menos RAM y disco;
- menor superficie de ataque;
- administración por SSH;
- automatización mediante scripts;
- uso habitual en servidores y edge.

## Aporte del speech
La VM se administra como se haría con un servidor real: desde otra máquina, mediante SSH.

## Imágenes
- `35_ubuntu_ssh_desde_host.png`
o
- `41_ubuntu_ssh_hostname_nuevo.png`

## Datos sensibles
- IP local anonimizada.
- usuario real puede ocultarse en la captura si no es necesario.
- hostname `srv-ubuntu01` se conserva.

## Composición visual
- Terminal SSH grande a la derecha.
- A la izquierda, cuatro razones de uso de CLI.
- Cada razón con icono lineal pequeño.

## Elemento dominante
La sesión SSH activa.

---

# 15 — Red en modo Bridged

## Tipo
Comparativa de arquitectura de red.

## Expone
**Gustavo Del Soto**

## Tiempo orientativo
**35 s**

## Objetivo
Explicar por qué Bridged es apropiado para un servidor que debe ser alcanzado desde otros equipos de planta.

## Contenido obligatorio

| Modo | IP de la VM | Visible desde otros equipos | Uso |
|---|---|---|---|
| Bridged | red local | Sí | servidor accesible |
| NAT | privada detrás del host | No | salida a Internet |
| Host-only | solo host | No | pruebas aisladas |

## Aporte del speech
Relacionar con industria:
- HMI;
- PLC;
- cliente SCADA;
- otros equipos de red.

## Composición visual
Tres mini-arquitecturas en paralelo:
- BRIDGED
- NAT
- HOST-ONLY

Bridged debe resaltarse en `teal`.

Debajo:
`Servidor de planta → debe ser alcanzable`.

## Elemento dominante
La comparación de topologías.

---

# 16 — Migrar la infraestructura a la nube

## Tipo
Inicio conceptual del Bloque 2.

## Expone
**Facundo Ferrero**

## Tiempo orientativo
**40 s**

## Objetivo
Presentar ventajas y riesgos de llevar parte de la infraestructura a servicios cloud.

## Contenido obligatorio

### Ventajas
- menor inversión inicial;
- CAPEX → OPEX;
- escalabilidad en minutos;
- backups;
- alta disponibilidad;
- acceso remoto desde distintas plantas.

### Impactos y riesgos
- dependencia de Internet;
- latencia;
- no apto para control en tiempo real;
- costos variables;
- gobernanza de datos;
- mayor superficie de ataque.

## Aporte del speech
Idea clave:
**el control en tiempo real permanece local; la nube se utiliza para históricos, analítica, reportes y servicios administrados.**

## Composición visual
Dos grandes campos:
- `LO QUE GANAMOS`
- `LO QUE DEBEMOS GESTIONAR`

En la franja inferior:
`CONTROL EN TIEMPO REAL → LOCAL`

## Elemento dominante
El equilibrio ventajas / riesgos.

---

# 17 — Creación de la cuenta de AWS

## Tipo
Secuencia de implementación.

## Expone
**Facundo Ferrero**

## Tiempo orientativo
**35 s**

## Objetivo
Mostrar los pasos de alta de la cuenta y la región utilizada.

## Contenido obligatorio
- email;
- nombre de cuenta;
- contraseña;
- Free plan;
- datos de contacto;
- tarjeta;
- verificación por email;
- verificación por teléfono;
- región `us-east-1`;
- MFA como buena práctica.

## Aporte del speech
La captura confirma que se está operando en `us-east-1`.

No afirmar que MFA está activado si no lo está; mostrarlo como recomendación.

## Imagen
`50_aws_consola_region_us_east_1.png`

## Datos sensibles
Ocultar:
- Account ID;
- nombre de sesión/cuenta si aparece;
- email;
- teléfono;
- datos de pago.

## Composición visual
- Timeline de registro en la izquierda.
- Captura AWS grande a la derecha.
- `REGIÓN: us-east-1` como dato destacado.

## Elemento dominante
La consola de AWS con la región seleccionada.

---

# 18 — Responsabilidad compartida

## Tipo
Comparativa conceptual.

## Expone
**Facundo Ferrero**

## Tiempo orientativo
**25 s**

## Objetivo
Diferenciar claramente qué protege AWS y qué debe proteger el usuario.

## Contenido obligatorio

### AWS — seguridad DE la nube
- datacenters;
- hardware;
- red física;
- virtualización;
- parches del motor RDS.

### Nosotros — seguridad EN la nube
- quién se conecta;
- contraseñas;
- reglas del Security Group;
- usuarios;
- datos.

Conclusión:
`El Security Group es responsabilidad del cliente.`

## Aporte del speech
No agregar contenido externo: enfatizar que usar un servicio administrado no elimina la responsabilidad de configuración y acceso.

## Composición visual
Dos grandes mitades.
Entre ambas, un límite vertical.

Izquierda:
`AWS`

Derecha:
`CLIENTE`

La frase final ocupa una banda inferior.

## Elemento dominante
La distinción **DE / EN** la nube.

---

# 19 — Security Group para SQL Server

## Tipo
Evidencia de ciberseguridad.

## Expone
**Facundo Ferrero**

## Tiempo orientativo
**35 s**

## Objetivo
Mostrar la regla creada para permitir acceso a SQL Server de forma restringida.

## Contenido obligatorio
- tipo: MSSQL;
- protocolo: TCP;
- puerto: 1433;
- origen: Mi IP;
- máscara `/32`;
- nombre del Security Group.

## Aporte del speech
- el Security Group funciona como firewall virtual con estado;
- `1433` es el puerto predeterminado de SQL Server;
- `/32` representa una sola IP.

## Imagen
`51_aws_security_group_mssql_1433.png`

## Datos sensibles
- ocultar completamente la IP pública.
- si aparece Account ID u otro identificador de cuenta, ocultarlo.

## Composición visual
Captura protagonista.

A la derecha o abajo, tres datos grandes:
`TCP`
`1433`
`/32`

Y una sola conclusión:
`UNA DIRECCIÓN AUTORIZADA`

## Elemento dominante
La regla de entrada.

---

# 20 — 1433: Mi IP versus todo Internet

## Tipo
Comparativa de seguridad.

## Expone
**Facundo Ferrero**

## Tiempo orientativo
**45 s**

## Objetivo
Justificar por qué se restringe el acceso al puerto 1433.

## Contenido obligatorio

### Mi IP /32
- una dirección;
- mínimo privilegio;
- superficie de ataque mínima.

### 0.0.0.0/0
- todo Internet;
- escaneo de puerto;
- fuerza bruta;
- robo/cifrado de datos;
- ransomware.

### Planta real
- subred privada;
- VPN;
- usuarios con permisos mínimos.

## Aporte del speech
El acceso público utilizado en laboratorio es una decisión práctica y no el diseño recomendado para producción.

## Composición visual
Comparativa 50/50:
- izquierda en verde/teal: `/32`
- derecha en rojo: `0.0.0.0/0`

Una franja inferior:
`PRODUCCIÓN → SUBRED PRIVADA + VPN`

## Elemento dominante
`/32` frente a `0.0.0.0/0`.

---

# 21 — SQL Server Express en Amazon RDS

## Tipo
Ficha de aprovisionamiento.

## Expone
**Cristian Vera**

## Tiempo orientativo
**35 s**

## Objetivo
Presentar cómo fue configurada la instancia RDS utilizada en el laboratorio.

## Contenido obligatorio
- Motor: Microsoft SQL Server.
- Edición: Express.
- Método: Standard create.
- Disponibilidad: Single-AZ.
- Identificador: `planta-industrial-db`.
- Usuario maestro.
- 20 GiB SSD.
- acceso público;
- Security Group;
- puerto 1433.

## Aporte del speech
- RDS es un servicio administrado.
- AWS gestiona SO, parches y backups.
- Single-AZ es suficiente para laboratorio.
- Express se eligió para la práctica.
- el acceso público queda condicionado por el Security Group.

## Imagen sugerida
`52_rds_resumen_instancia.png`

## Datos sensibles
- usuario maestro no debe mostrarse como dato de conexión operativo; puede representarse como `usuario maestro`.
- cualquier identificador de cuenta, IP o endpoint visible en una captura se oculta.

## Composición visual
- Captura RDS a la derecha.
- A la izquierda, ficha técnica de siete líneas.
- Etiqueta superior:
`SERVICIO ADMINISTRADO`

## Elemento dominante
La configuración de la instancia.

---

# 22 — Instancia disponible y punto de enlace

## Tipo
Evidencia de estado + conectividad.

## Expone
**Cristian Vera**

## Tiempo orientativo
**15 s**

## Objetivo
Demostrar que la instancia está activa y señalar qué información se utiliza para conectarse.

## Contenido obligatorio
- estado: Disponible;
- SQL Server Express;
- `db.t3.micro`;
- región `us-east-1`;
- endpoint;
- puerto 1433;
- acceso público;
- Security Group.

## Aporte del speech
El endpoint y el puerto constituyen el par fundamental de conexión desde SSMS.

## Imágenes
- `52_rds_resumen_instancia.png`
- `53_rds_conectividad_endpoint_vpc.png`

## Datos sensibles
- endpoint anonimizado;
- VPC ID anonimizada;
- Account ID oculto;
- IP pública oculta.

## Composición visual
Dos capturas:
1. estado de la instancia;
2. conectividad.

Entre ambas:
`ENDPOINT + 1433`

## Elemento dominante
El estado **Disponible**.

---

# 23 — Del cliente local a la base en AWS

## Tipo
Arquitectura.

## Expone
**Cristian Vera**

## Tiempo orientativo
**20 s**

## Objetivo
Integrar visualmente todos los bloques anteriores en una única cadena de conexión.

## Contenido obligatorio
- PC local;
- SSMS;
- Internet;
- conexión cifrada;
- Security Group;
- TCP 1433;
- Mi IP;
- RDS SQL Server;
- Express;
- base `Planta_Industrial`.

## Aporte del speech
El Security Group se interpreta como el punto que filtra origen y puerto antes de permitir llegar a RDS.

## Composición visual
Diagrama de izquierda a derecha:

`MI PC / SSMS`
→
`INTERNET`
→
`SECURITY GROUP`
→
`AWS RDS / SQL SERVER`

Debajo del Security Group:
`TCP 1433 · origen autorizado`

Debajo de RDS:
`Planta_Industrial`

## Elemento dominante
La arquitectura completa.

---

# 24 — Conexión desde SSMS al Endpoint

## Tipo
Evidencia de conexión remota.

## Expone
**Cristian Vera**

## Tiempo orientativo
**25 s**

## Objetivo
Mostrar cómo SSMS se conecta a la instancia de AWS.

## Contenido obligatorio
- tipo de servidor: Database Engine;
- nombre: endpoint + coma + `1433`;
- autenticación SQL Server;
- usuario;
- captura del diálogo de conexión.

## Aporte del speech
Punto didáctico:
`endpoint,1433` utiliza **coma**, no dos puntos.

La conexión exitosa demuestra que:
- RDS está disponible;
- el Security Group permite la conexión;
- SSMS llega al motor.

## Imagen
`54_ssms_conexion_rds.png`

## Datos sensibles
- endpoint anonimizado;
- contraseña completamente oculta;
- no mostrar longitud aproximada mediante puntos si se puede evitar;
- usuario maestro puede reemplazarse visualmente por `usuario_admin`;
- cualquier opción “remember password” puede recortarse si no aporta.

## Composición visual
- Captura SSMS grande.
- En un lateral:
  - `Database Engine`
  - `endpoint,1433`
  - `SQL Server Authentication`
- La coma se resalta visualmente.

## Elemento dominante
La conexión SSMS → RDS.

---

# 25 — Base de datos y tabla de monitoreo

## Tipo
Código + explicación.

## Expone
**Cristian Vera**

## Tiempo orientativo
**40 s**

## Objetivo
Explicar la primera parte del script T-SQL: creación de la base y estructura de la tabla.

## Contenido obligatorio
Código:
- `CREATE DATABASE Planta_Industrial`
- `USE Planta_Industrial`
- `CREATE TABLE dbo.Eventos_Planta`
- `IDENTITY`
- `PRIMARY KEY`
- `DEFAULT SYSDATETIME()`
- `CHECK`
- campos de equipo, tipo, descripción, valor y unidad.
- `GO`

Conceptos:
- CREATE = DDL;
- IDENTITY;
- PRIMARY KEY;
- DEFAULT;
- CHECK;
- GO separa lotes en SSMS.

## Aporte del speech
La tabla modela eventos industriales:
- falla;
- alarma;
- producción;
- mantenimiento.

Debe quedar claro que DDL **define estructura**, no carga datos.

## Composición visual
- Izquierda: bloque de código.
- Derecha: cinco conceptos explicados.
- Resaltar con color dentro del código:
  - `IDENTITY`
  - `PRIMARY KEY`
  - `DEFAULT`
  - `CHECK`
- Abajo:
`DDL → DEFINE ESTRUCTURAS`

## Elemento dominante
El fragmento de `CREATE TABLE`.

---

# 26 — Carga de datos y consulta

## Tipo
Código + resultado real.

## Expone
**Cristian Vera**

## Tiempo orientativo
**40 s**

## Objetivo
Explicar la segunda parte del script: carga de registros y consultas de verificación.

## Contenido obligatorio
Cuatro INSERT:
- Motor M-101 — FALLA — Sobrecorriente.
- Bomba B-201 — ALARMA — Presión alta.
- Línea 1 — PRODUCCIÓN — Piezas del turno.
- Horno H-301 — ALARMA — Temperatura alta.

Consultas:
- `SELECT *`
- `GROUP BY tipo_evento`
- `COUNT(*)`

Resultado:
- cuatro filas;
- conteo por tipo.

Concepto:
- INSERT y SELECT como DML.

## Aporte del speech
Diferencia final:
- DDL → estructura.
- DML → manipulación de datos.

## Imagen
`55_ssms_resultado_script.png`

## Composición visual
- Izquierda: código resumido.
- Derecha: resultado real en SSMS.
- Franja inferior:
`INSERT → CARGA`
`SELECT → CONSULTA`
`GROUP BY → AGREGA`

## Elemento dominante
El resultado real en SSMS.

---

# 27 — Conclusiones

## Tipo
Síntesis.

## Expone
**Cristian Vera**

## Tiempo orientativo
**30 s**

## Objetivo
Cerrar el recorrido con cinco aprendizajes directamente vinculados al trabajo realizado.

## Contenido obligatorio
1. Virtualización: permite construir y probar servidores sin hardware dedicado.
2. Windows Server y Ubuntu Server: cubren distintos roles de planta.
3. Cloud: aporta escala y respaldo, pero exige seguridad de acceso.
4. Security Group con Mi IP: reduce superficie de ataque.
5. RDS + SQL: base de eventos preparada para un histórico industrial.

## Aporte del speech
Reforzar el hilo conductor completo:
**infraestructura → red → seguridad → datos**.

## Composición visual
Cinco conclusiones, pero no como cinco tarjetas iguales.

Propuesta:
- una línea de recorrido con cinco hitos;
- cada hito con una frase corta;
- fondo claro;
- el último hito termina en `HISTÓRICO INDUSTRIAL`.

## Elemento dominante
La síntesis del recorrido completo.

---

# 28 — Preguntas

## Tipo
Cierre.

## Expone
**Cristian Vera**

## Tiempo orientativo
**10 s**

## Objetivo
Cerrar formalmente la exposición y abrir la instancia de preguntas.

## Contenido obligatorio
- **Preguntas**
- **Gracias por su atención**
- nombres de los cuatro integrantes;
- `Informática Industrial · UTN FRC`.

## Aporte del speech
Indicar verbalmente que están disponibles para mostrar:
- consola AWS;
- SSMS;
- Windows Server;
- Ubuntu Server.

No es necesario colocar esa lista completa en pantalla.

## Composición visual
- Fondo `azul_profundo`.
- `PREGUNTAS` muy grande.
- Debajo: `Gracias por su atención`.
- Línea técnica sutil conectando:
  `VM → RED → AWS → SQL`
- Nombres de integrantes en la zona inferior.
- Sin numeración o con `28 / 28` muy discreto.

## Elemento dominante
**PREGUNTAS**

---

# Distribución de expositores

| Expositor | Diapositivas | Tema |
|---|---:|---|
| Emiliano Casali | 01–07 | Apertura, servidor, virtualización, TP1 VM y red |
| Gustavo Del Soto | 08–15 | Roles, IIS, Ubuntu Server, LVM, CLI y Bridged |
| Facundo Ferrero | 16–20 | Cloud, AWS, responsabilidad compartida y Security Group |
| Cristian Vera | 21–28 | RDS, SSMS, T-SQL, conclusiones y cierre |

---

# Ritmo de la presentación

La exposición debe sentirse como un único recorrido y no como cuatro presentaciones separadas.

## Secuencia conceptual

`SERVIDOR`
→
`VIRTUALIZACIÓN`
→
`WINDOWS`
→
`UBUNTU`
→
`RED`
→
`CLOUD`
→
`SEGURIDAD`
→
`RDS`
→
`SQL`
→
`HISTÓRICO INDUSTRIAL`

## Pases de palabra

- Slide 07 → Gustavo.
- Slide 15 → Facundo.
- Slide 20 → Cristian.

Los cambios de expositor deben coincidir visualmente con cambios naturales de tema.

---

# Política de datos sensibles

Debe aplicarse antes de montar cualquier captura en la versión final.

## Se conserva visible
- nombres;
- apellidos;
- legajos;
- hostname `SRV-IND01`;
- hostname `srv-ubuntu01`;
- `8.8.8.8`;
- `0.0.0.0/0`;
- `1433`;
- región AWS;
- nombres de servicios y tecnologías.

## Se anonimiza
- IP privadas: último octeto oculto;
- IP pública: completa oculta;
- IPv6: parcialmente oculta;
- MAC: últimos bytes ocultos;
- contraseñas: completamente ocultas;
- AWS Account ID;
- endpoint RDS;
- VPC ID;
- rutas personales `C:\Users\...`;
- correo, teléfono o datos de facturación;
- cualquier dato de sesión AWS que no sea necesario para explicar el TP.

---

# Regla final de implementación

Cada diapositiva debe cumplir simultáneamente tres condiciones:

1. **Conservar todo el contenido académico original.**
2. **Incorporar del speech únicamente aquello que enriquece la comprensión visual.**
3. **Respetar íntegramente el sistema visual definido en `diseño.md`.**

La presentación final debe seguir siendo reconocible como el mismo trabajo académico, pero con una composición visual más clara, técnica, consistente y profesional.
