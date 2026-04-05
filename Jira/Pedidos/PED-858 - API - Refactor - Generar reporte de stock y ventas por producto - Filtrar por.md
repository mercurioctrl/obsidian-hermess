---
jira_key: "PED-858"
aliases: ["PED-858"]
summary: "API - Refactor - Generar reporte de stock y ventas por producto -> Filtrar por string"
status: "Finalizada"
type: "Subtarea"
priority: "Lowest"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-10-30 02:41"
updated: "2024-11-30 03:04"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-858"
---

# PED-858: API - Refactor - Generar reporte de stock y ventas por producto -> Filtrar por string

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Lowest |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-10-30 02:41 |
| Actualizado | 2024-11-30 03:04 |
| Etiquetas | ninguna |
| Jira | [PED-858](https://bluinc.atlassian.net/browse/PED-858) |

## Relaciones

- **Padre:** [[PED-213]] Reportes de ventas

## Descripcion

Vamos a llevar a cabo un refactor en el reporte de Stock para permitir el filtrado por cadenas de texto.

```
GET {API_URL}/v1/reports/stocks?between=01-01-2024_31-01-2024&search={string}
```
