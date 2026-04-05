---
jira_key: "PEGA-146"
aliases: ["PEGA-146"]
summary: "API - Refactor - Incorporar consulta a Redis en los paginados de las búsquedas tambien"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-11-20 06:52"
updated: "2024-11-25 00:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-146"
---

# PEGA-146: API - Refactor - Incorporar consulta a Redis en los paginados de las búsquedas tambien

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-20 06:52 |
| Actualizado | 2024-11-25 00:43 |
| Etiquetas | ninguna |
| Jira | [PEGA-146](https://bluinc.atlassian.net/browse/PEGA-146) |

## Relaciones

- **Padre:** [[PEGA-2]] Catalogos y Buscador

## Descripcion

Incorporaremos consultas a Redis para el recurso

```
GET {API_URL}/v1/items?order=asc_price&rate=down&search=amd&offset=30

```
