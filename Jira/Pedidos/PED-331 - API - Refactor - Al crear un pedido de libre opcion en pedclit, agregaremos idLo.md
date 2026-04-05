---
jira_key: "PED-331"
aliases: ["PED-331"]
summary: "API - Refactor - Al crear un pedido de libre opcion en pedclit, agregaremos idLo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-12-14 12:34"
updated: "2023-12-15 11:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-331"
---

# PED-331: API - Refactor - Al crear un pedido de libre opcion en pedclit, agregaremos idLo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-14 12:34 |
| Actualizado | 2023-12-15 11:36 |
| Etiquetas | ninguna |
| Jira | [PED-331](https://bluinc.atlassian.net/browse/PED-331) |

## Relaciones

- **Padre:** [[PED-329 - Listado de ordenes|PED-329]] Listado de ordenes

## Descripcion

Agregaremos la columna `idLo` a la tabla `[NewBytes_DBF].[dbo].[pedclit]` en donde guardaremos el id de la tabla `[LO].[dbo].[pedidosCabecera]` al crear una nueva orden desde la plataforma Libre Opcion
