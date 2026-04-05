---
jira_key: "INV-56"
aliases: ["INV-56"]
summary: "API - Listar productos - Combinación de filtros"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-01-30 04:15"
updated: "2024-01-31 21:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-56"
---

# INV-56: API - Listar productos - Combinación de filtros

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-01-30 04:15 |
| Actualizado | 2024-01-31 21:01 |
| Etiquetas | ninguna |
| Jira | [INV-56](https://bluinc.atlassian.net/browse/INV-56) |

## Relaciones

- **Padre:** [[INV-2 - MS - METADATA - API|INV-2]] MS - METADATA - API
- **relates to:** [[INV-14 - API - Listar productos|INV-14]] API - Listar productos

## Descripcion

Cuando intento combinar los filtros de marca y categoría, no obtengo ningún resultado, a pesar de que hay productos que cumplen con ambos criterios. Un ejemplo específico sería al aplicar el filtro por `categoryId=34` y `brandId=85`, donde, a pesar de que hay productos con esa marca y categoría según la lista, la consulta no arroja resultados.

[adjunto]
