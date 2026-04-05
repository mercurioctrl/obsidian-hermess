---
jira_key: "PEGA-164"
aliases: ["PEGA-164"]
summary: "API - Refactor - Modificar SyncUp para guardar la fecha del ultimo cambio de precios"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-01-07 10:06"
updated: "2025-01-27 17:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-164"
---

# PEGA-164: API - Refactor - Modificar SyncUp para guardar la fecha del ultimo cambio de precios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-07 10:06 |
| Actualizado | 2025-01-27 17:32 |
| Etiquetas | ninguna |
| Jira | [PEGA-164](https://bluinc.atlassian.net/browse/PEGA-164) |

## Relaciones

- **Padre:** [[PEGA-3]] Scraping y procesamientos
- **has action item:** [[PEGA-165]] API - Refactor - Nuevo parámetro para filtrar limite de días desde la ultima modificación de precio

## Descripcion

Agregaremos la columna `priceChangeDate` en la tabla `[PEGA].[dbo].[items]`

Lo que buscaremos sera poder capturar la fecha exacta, donde el ítem cambio de precio por ultima vez

```
GET {{API_URL}}/v1/sync/items/{token}?importerId={importerId}
```
