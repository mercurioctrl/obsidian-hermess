---
jira_key: "EXP-373"
aliases: ["EXP-373"]
summary: "APP - Refactor - Cambiar endpoint en listado de seguimientos"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-10-12 09:56"
updated: "2023-10-12 17:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-373"
---

# EXP-373: APP - Refactor - Cambiar endpoint en listado de seguimientos

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-12 09:56 |
| Actualizado | 2023-10-12 17:35 |
| Etiquetas | ninguna |
| Jira | [EXP-373](https://bluinc.atlassian.net/browse/EXP-373) |

## Relaciones

- **Padre:** [[EXP-372 - Refactor - Seguimientos|EXP-372]] Refactor - Seguimientos

## Descripcion

Refactorizaremos la pestaña seguimientos ([/trackingOrders?currentPage=1&itemsPerPage=15](https://expedicion.saftel.com/trackingOrders?currentPage=1&itemsPerPage=15)) para que muestre el recurso

```
GET {{API_URL}}/v1/trackingOrders/drops
```

y el detalle de cada una de esas cabeceras con

```
GET {{API_URL}}/v1/trackingOrders/drops/6
```



Las cabeceras pueden finalizarse usando 

```
PATCH {{API_URL}}/v1/trackingOrders/finalizeDrop/5
```
