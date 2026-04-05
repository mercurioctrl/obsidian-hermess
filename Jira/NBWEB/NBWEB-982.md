---
jira_key: "NBWEB-982"
summary: "API - Refactor - Agregar lista E de precios para los clientes que la tienen seleccionadas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-07-17 09:23"
updated: "2025-07-17 15:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-982"
---

# NBWEB-982: API - Refactor - Agregar lista E de precios para los clientes que la tienen seleccionadas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-17 09:23 |
| Actualizado | 2025-07-17 15:23 |
| Etiquetas | ninguna |
| Jira | [NBWEB-982](https://bluinc.atlassian.net/browse/NBWEB-982) |

## Descripción

Agregaremos un nuevo precio para la lista E, que se obtiene utilizando `[NewBytes_DBF].[dbo].[articulo].[npvp6]`

Esta lista sera para los clientes que estén marcados como `[NewBytes_DBF].[dbo].[clientes].ntarifapp=6`

Esto impactara tanto en la lista de precios, como en las ordenes generadas y listas descargadas para los clientes que estén alcanzados por `ntarifapp=6`
