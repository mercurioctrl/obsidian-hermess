---
jira_key: "NBWEB-783"
summary: "API - falla la busqueda por marcas"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Marbe Moreno"
created: "2024-07-24 10:47"
updated: "2024-07-24 16:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-783"
---

# NBWEB-783: API - falla la busqueda por marcas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Marbe Moreno |
| Creado | 2024-07-24 10:47 |
| Actualizado | 2024-07-24 16:06 |
| Etiquetas | ninguna |
| Jira | [NBWEB-783](https://bluinc.atlassian.net/browse/NBWEB-783) |

## Descripción

al filtrar por marca si no encuentra productos trae todos los productos en lugar de no traer nada
[https://api.nb.com.ar/v1/brand/alcatel?available_stock=0](https://api.nb.com.ar/v1/brand/alcatel?available_stock=0)

[attachment]
