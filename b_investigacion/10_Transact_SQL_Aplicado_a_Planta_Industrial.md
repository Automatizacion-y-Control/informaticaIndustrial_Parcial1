# 10 — Transact-SQL aplicado a Planta_Industrial

## Alcance

El script Transact-SQL del parcial explicado línea por línea: qué es T-SQL,
qué hace cada sentencia, y qué resultado debe observarse para demostrar que
la conexión remota y el script funcionaron correctamente.

## Qué es Transact-SQL

**T-SQL** es el dialecto de SQL que utiliza Microsoft SQL Server, con
extensiones propias sobre el estándar SQL (por ejemplo, `GO` como separador
de lotes, o funciones como `SYSDATETIME()`). Es el lenguaje con el que se
definió, cargó y consultó la base `Planta_Industrial` en Amazon RDS.

## Sentencia por sentencia

- **`CREATE DATABASE Planta_Industrial;`** — crea la base de datos. Es una
  sentencia **DDL** (Data Definition Language): define una estructura.
- **`USE Planta_Industrial;`** — cambia el contexto de ejecución a la base
  recién creada; las sentencias siguientes actúan sobre ella.
- **`GO`** — no es una instrucción de T-SQL propiamente dicha, sino un
  **separador de lotes** propio de SSMS: indica al cliente dónde termina un
  grupo de sentencias a enviar al servidor.
- **`CREATE TABLE dbo.Eventos_Planta (...)`** — define la estructura de la
  tabla, también DDL. Dentro de ella:
  - **`IDENTITY(1,1)`** numera automáticamente cada evento.
  - **`PRIMARY KEY`** garantiza que cada fila tenga un identificador único
    (ver también
    [`09_Bases_de_Datos_Relacionales_SQL_y_Uso_Industrial.md`](09_Bases_de_Datos_Relacionales_SQL_y_Uso_Industrial.md)).
  - **`NOT NULL`** obliga a cargar el dato.
  - **`DEFAULT SYSDATETIME()`** sella la fecha y hora del evento sin
    necesidad de cargarla manualmente.
  - **`CHECK`** garantiza la integridad de los datos, admitiendo solo los
    tipos de evento definidos (por ejemplo, `FALLA`, `ALARMA`,
    `PRODUCCION`, `MANTENIMIENTO`).
- **`INSERT INTO dbo.Eventos_Planta (...) VALUES (...);`** — sentencia
  **DML** (Data Manipulation Language): agrega filas con eventos de ejemplo
  de una planta industrial.
- **`SELECT ...`** — recupera y verifica los datos cargados. Una primera
  consulta simple (`SELECT * FROM ...`) muestra todas las filas; una segunda
  agrupa con `GROUP BY` y cuenta cuántos eventos hay de cada tipo con
  `COUNT(*)`.

En síntesis: **DDL** define estructuras (`CREATE`, `ALTER`, `DROP`) y
**DML** manipula los datos que esas estructuras contienen (`INSERT`,
`SELECT`, `UPDATE`, `DELETE`).

## Un ejemplo simple y defendible

El script se mantuvo deliberadamente simple: el objetivo es demostrar
comprensión de creación, carga y consulta, no programación avanzada de
bases de datos. Una versión mínima equivalente, con una tabla de fallas,
sería:

```sql
CREATE DATABASE Planta_Industrial;
GO

USE Planta_Industrial;
GO

CREATE TABLE Fallas (
    IdFalla INT IDENTITY(1,1) PRIMARY KEY,
    Equipo VARCHAR(50) NOT NULL,
    Descripcion VARCHAR(150) NOT NULL,
    FechaHora DATETIME2 NOT NULL,
    Estado VARCHAR(20) NOT NULL
);
GO

INSERT INTO Fallas (Equipo, Descripcion, FechaHora, Estado)
VALUES
    ('Bomba_01', 'Sobretemperatura', '2026-09-20 10:15:00', 'Resuelta'),
    ('Motor_02', 'Vibracion elevada', '2026-09-20 11:40:00', 'Pendiente');
GO

SELECT IdFalla, Equipo, Descripcion, FechaHora, Estado
FROM Fallas;
GO
```

El script finalmente implementado en el informe (`dbo.Eventos_Planta`, ver
`c_prototipado/informeParcial1_infoInd.md`, sección 4.3) sigue exactamente
esta misma lógica de tres pasos — crear estructura, cargar datos, consultar
— con una tabla algo más completa (agrega `CHECK` sobre el tipo de evento,
`valor` y `unidad`) para acercarse más a un registro real de planta.

## Qué demuestra el resultado

Si la consulta se ejecutó **desde un cliente remoto conectado al endpoint de
RDS** (ver
[`08_AWS_RDS_SQL_Server_y_Endpoint.md`](08_AWS_RDS_SQL_Server_y_Endpoint.md)),
observar las filas devueltas demuestra conjuntamente varias cosas: hubo
resolución del endpoint, hubo conectividad hasta AWS, el Security Group
admitió la conexión (ver
[`07_AWS_Security_Groups_Puerto_1433_y_Acceso_Remoto.md`](07_AWS_Security_Groups_Puerto_1433_y_Acceso_Remoto.md)),
las credenciales fueron aceptadas, el motor ejecutó T-SQL y los datos
quedaron almacenados. Esto **no demuestra por sí solo que toda la seguridad
esté bien configurada**, pero sí valida funcionalmente el recorrido completo
de la conexión.

## Errores conceptuales frecuentes a evitar en la defensa

- Confundir `GO` con una instrucción de T-SQL (es un separador de lotes de
  SSMS).
- Decir que `CREATE TABLE` "guarda datos" (define estructura; `INSERT` es
  quien carga datos).
- Tratar el Security Group como si autenticara al usuario en SQL Server (son
  capas distintas).

## Preguntas de defensa oral

| Pregunta | Respuesta técnica breve |
|---|---|
| ¿Qué hace `CREATE DATABASE`? | Crea una nueva base de datos. |
| ¿Qué hace `CREATE TABLE`? | Define una nueva tabla y sus columnas/restricciones. |
| ¿Qué hace `INSERT`? | Agrega filas a una tabla existente. |
| ¿Qué hace `SELECT`? | Recupera filas o columnas para consultarlas. |
| ¿Qué demuestra ver los datos tras un `SELECT` remoto? | Que la conexión, autenticación, contexto de base y ejecución de la consulta funcionaron hasta devolver los datos. |

## Fuentes principales

Documentación de Microsoft Learn sobre Transact-SQL (`CREATE DATABASE`,
`CREATE TABLE`, `INSERT`, `SELECT`) y sobre el separador de lotes `GO` en
SQL Server Management Studio.
