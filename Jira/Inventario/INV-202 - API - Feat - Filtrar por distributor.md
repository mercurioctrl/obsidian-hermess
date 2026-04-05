---
jira_key: "INV-202"
aliases: ["INV-202"]
summary: "API - Feat - Filtrar por \"distributor\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-09-03 13:33"
updated: "2025-09-03 19:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-202"
---

# INV-202: API - Feat - Filtrar por "distributor"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-09-03 13:33 |
| Actualizado | 2025-09-03 19:08 |
| Etiquetas | ninguna |
| Jira | [INV-202](https://bluinc.atlassian.net/browse/INV-202) |

## Relaciones

- **Padre:** [[INV-27 - Productos|INV-27]] Productos
- **has action item:** [[INV-200 - APP - Feat - Cambiar atributo distributor y poder filtrarlo en el repositorio|INV-200]] APP - Feat - Cambiar atributo "distributor" y poder filtrarlo en el repositorio "items"

## Descripcion

Filtraremos los productos por distribuidor, recibe un entero, si es `NULL` trae todas

```
GET {API_URL}/items?distributor={int/null}
```
