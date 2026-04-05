---
jira_key: "PED-184"
aliases: ["PED-184"]
summary: "API - Feat - Filtros de ordenes -> Filtrar por estado de pedido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2023-10-27 15:20"
updated: "2023-10-31 17:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-184"
---

# PED-184: API - Feat - Filtros de ordenes -> Filtrar por estado de pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2023-10-27 15:20 |
| Actualizado | 2023-10-31 17:21 |
| Etiquetas | ninguna |
| Jira | [PED-184](https://bluinc.atlassian.net/browse/PED-184) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra
- **blocks:** [[PED-185]] APP - Feat - Filtros de ordenes -> Filtrar por estado de pedido

## Descripcion

Basándonos en el recurso [link](https://lioteam.atlassian.net/browse/PED-178) agregaremos filtrado por estado del pedido.

```
GET {API_URL}/v1/orders?orderStatus=1
```
