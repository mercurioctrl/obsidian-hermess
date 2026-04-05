---
jira_key: "PED-375"
aliases: ["PED-375"]
summary: "API - Listar productos - Incidencias varias"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2023-12-21 14:35"
updated: "2023-12-22 16:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-375"
---

# PED-375: API - Listar productos - Incidencias varias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2023-12-21 14:35 |
| Actualizado | 2023-12-22 16:18 |
| Etiquetas | ninguna |
| Jira | [PED-375](https://bluinc.atlassian.net/browse/PED-375) |

## Relaciones

- **relates to:** [[PED-66]] API - Feat - Listar productos

## Descripcion

En el listado de productos, por ejemplo, el producto `117749` me aparece que su existencia en ordenes es 0

[adjunto]
Sin embargo, al ejecutar el recurso de `itemReservations`, me devuelve que hay, de ese mismo producto, 4 cantidades reservadas en diferentes órdenes.

[adjunto]
