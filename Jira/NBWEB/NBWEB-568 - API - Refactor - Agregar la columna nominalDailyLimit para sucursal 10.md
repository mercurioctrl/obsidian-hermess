---
jira_key: "NBWEB-568"
aliases: ["NBWEB-568"]
summary: "API - Refactor - Agregar la columna nominalDailyLimit para sucursal 10"
status: "Code Review"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-08-01 10:20"
updated: "2023-08-01 16:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-568"
---

# NBWEB-568: API - Refactor - Agregar la columna nominalDailyLimit para sucursal 10

| Campo | Valor |
|-------|-------|
| Estado | Code Review (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-01 10:20 |
| Actualizado | 2023-08-01 16:14 |
| Etiquetas | ninguna |
| Jira | [NBWEB-568](https://bluinc.atlassian.net/browse/NBWEB-568) |

## Relaciones

- **Padre:** [[NBWEB-529]] CMS -  Personal
- **blocks:** [[NBWEB-569]] APP - Refactor - Agregar la columna nominalDailyLimit para sucursal 10

## Descripcion

Modificaremos el recurso [link](https://lioteam.atlassian.net/browse/NBWEB-530)  para agregar el parámetro `nominalDailyLimit0010` que se encuentra en la tabla `[NewBytes_DBF].[dbo].[agentes]`

Adicionalmente tambien modificaremos, de ser necesario el recurso [link](https://lioteam.atlassian.net/browse/NBWEB-531)  para poder editar el mismo, como hacemos con `nominalDailyLimit`comun.

Adicionalmente ordenaremos el recurso que hoy esta alfabetico, por la suma de nominalDailyLimit0010 y nominalDailyLimit descendente.
