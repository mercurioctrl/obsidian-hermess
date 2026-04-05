---
jira_key: "INV-226"
aliases: ["INV-226"]
summary: "API - MVP - Refactor - Agregar paginacion al repositorio de stock, permitiendo elegir cantidad por pagina"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-11-06 09:31"
updated: "2025-12-05 04:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-226"
---

# INV-226: API - MVP - Refactor - Agregar paginacion al repositorio de stock, permitiendo elegir cantidad por pagina

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-06 09:31 |
| Actualizado | 2025-12-05 04:25 |
| Etiquetas | ninguna |
| Jira | [INV-226](https://bluinc.atlassian.net/browse/INV-226) |

## Relaciones

- **Padre:** [[INV-199 - Control de Stock Stock en general Control de Precios|INV-199]] Control de Stock / Stock en general  / Control de Precios
- **has action item:** [[INV-227 - APP - MVP - Refactor - Agregar paginacion al repositorio de stock, permitiendo|INV-227]] APP - MVP - Refactor - Agregar paginacion al repositorio de stock, permitiendo elegir cantidad por pagina

## Descripcion

Agreagermos la posiblidad de paginar eligiendo `itemsPerPage`, si `itemsPerPage` no viene por defecto es 100

```
GET {API_URL}/itemsStocks?currentPage=1&itemsPerPage=100&companyCode=4
```
