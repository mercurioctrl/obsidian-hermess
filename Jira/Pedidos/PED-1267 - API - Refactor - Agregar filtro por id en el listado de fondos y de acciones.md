---
jira_key: "PED-1267"
aliases: ["PED-1267"]
summary: "API - Refactor - Agregar filtro por id en el listado de fondos y de acciones"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Franco Callipo"
reporter: "Marbe Moreno"
created: "2026-01-15 10:12"
updated: "2026-01-16 09:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1267"
---

# PED-1267: API - Refactor - Agregar filtro por id en el listado de fondos y de acciones

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Franco Callipo |
| Reportado por | Marbe Moreno |
| Creado | 2026-01-15 10:12 |
| Actualizado | 2026-01-16 09:43 |
| Etiquetas | ninguna |
| Jira | [PED-1267](https://bluinc.atlassian.net/browse/PED-1267) |

## Relaciones

- **Padre:** [[PED-1208 - Gestión de Aportes y Gastos de Marketing|PED-1208]] Gestión de Aportes y Gastos de Marketing

## Descripcion

- Agregar filtro por `fundId` en listado de fondos ej:



```
https://gamma.api.orders.lio.red/v1/marketing/funds?fundId=3
```



- Agregar filtro por `actionId` en listado de acciones ej:



```
https://gamma.api.orders.lio.red/v1/marketing/actions?actionId=2
```



- Agregar el filtro search para buscar una acción ej


```
https://gamma.api.orders.lio.red/v1/marketing/actions?currentPage=1&itemsPerPage=15&activeOnly=1&search=neuva
```
