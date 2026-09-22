# 09 — Bases de datos relacionales, SQL y uso industrial

## Alcance

Qué es una base de datos, qué es un DBMS/SGBD, qué caracteriza al modelo
relacional, y las categorías de SQL (DDL/DML/consulta) aplicadas a un caso
industrial simple.

## Base de datos, DBMS y T-SQL: tres niveles distintos

Conviene defender el bloque de bases de datos desde tres niveles bien
diferenciados:

- **Base de datos:** el conjunto estructurado de datos (en el parcial,
  `Planta_Industrial`).
- **SGBD / DBMS:** el software que gestiona esas bases; en este caso,
  **Microsoft SQL Server**.
- **T-SQL:** el dialecto de SQL utilizado específicamente por SQL Server
  (desarrollado en detalle en
  [`10_Transact_SQL_Aplicado_a_Planta_Industrial.md`](10_Transact_SQL_Aplicado_a_Planta_Industrial.md)).

**Base de datos y SQL Server no son lo mismo:** SQL Server es el motor/SGBD;
`Planta_Industrial` es una base de datos gestionada por ese motor.

## El modelo relacional

Una base de datos relacional organiza la información en **tablas** compuestas
por **filas** (registros) y **columnas** (campos), cada una con un **tipo de
dato**. Una **clave primaria** identifica de forma única cada fila de una
tabla. Este modelo permite relacionar tablas entre sí, aunque en el alcance
del parcial no se profundiza más allá de lo necesario para una tabla simple
de eventos industriales.

## DDL, DML y consultas

| Categoría | Qué hace | Sentencias del parcial |
|---|---|---|
| **DDL** (Data Definition Language) | Define estructuras | `CREATE DATABASE`, `CREATE TABLE` |
| **DML** (Data Manipulation Language) | Modifica datos | `INSERT` |
| **Consulta** | Recupera información | `SELECT` |

## Por qué una base de datos y no archivos sueltos

Una estructura de datos organizada resuelve problemas que un archivo suelto
no resuelve bien: consistencia de tipos, identificación única de cada
registro (clave primaria), consultas estructuradas sobre grandes volúmenes,
y una base común para múltiples aplicaciones o usuarios. En un contexto de
monitoreo industrial, esto permite registrar de forma ordenada **fallas,
alarmas, eventos de producción o mantenimiento**, con fecha, equipo, valor y
unidad — precisamente el modelo adoptado en la tabla `Eventos_Planta` del
informe (ver
[`10_Transact_SQL_Aplicado_a_Planta_Industrial.md`](10_Transact_SQL_Aplicado_a_Planta_Industrial.md)),
sin necesidad de introducir todavía SCADA ni historiadores de proceso.

## Relación con Microsoft SQL Server en AWS RDS

Estos conceptos (base de datos, SGBD, modelo relacional, DDL/DML/consulta)
son independientes de dónde se ejecute el motor. Lo que cambia al usar
Amazon RDS (ver
[`08_AWS_RDS_SQL_Server_y_Endpoint.md`](08_AWS_RDS_SQL_Server_y_Endpoint.md))
es la infraestructura que sostiene al SGBD, no el modelo relacional ni el
lenguaje SQL en sí.

## Preguntas de defensa oral

| Pregunta | Respuesta técnica breve |
|---|---|
| ¿Base de datos y SQL Server son lo mismo? | No. SQL Server es el SGBD/motor; `Planta_Industrial` es una base gestionada por ese motor. |
| ¿Qué es una clave primaria? | La columna (o combinación de columnas) que identifica de forma única cada fila de una tabla. |
| ¿Qué diferencia hay entre DDL y DML? | DDL define estructuras (`CREATE DATABASE`, `CREATE TABLE`); DML modifica los datos que esas estructuras contienen (`INSERT`). |
| ¿Por qué usar una base de datos y no archivos sueltos para registrar eventos de planta? | Por consistencia de tipos, identificación única de cada evento y capacidad de consulta estructurada sobre el histórico. |

## Fuentes principales

Documentación de Microsoft Learn sobre Transact-SQL: sentencias `CREATE
DATABASE`, `CREATE TABLE`, `INSERT` y `SELECT`, y conceptos fundamentales del
modelo relacional en SQL Server.
