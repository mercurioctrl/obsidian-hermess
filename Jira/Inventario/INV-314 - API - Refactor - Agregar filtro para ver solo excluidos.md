---
jira_key: "INV-314"
aliases: ["INV-314"]
summary: "API - Refactor - Agregar filtro para ver solo excluidos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-01-06 14:38"
updated: "2026-01-20 18:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-314"
---

# INV-314: API - Refactor - Agregar filtro para ver solo excluidos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-06 14:38 |
| Actualizado | 2026-01-20 18:10 |
| Etiquetas | ninguna |
| Jira | [INV-314](https://bluinc.atlassian.net/browse/INV-314) |

## Relaciones

- **Padre:** [[INV-27]] Productos
- **has action item:** [[INV-315]] APP - Refactor - Incluir filtro Excluidos 

## Descripcion

Cuando viene el filtro `excluded=true` solo mostraremos los productos que cumplan `[NewBytes_DBF].[dbo].[articulo].EXCLUIR = 1` caso contrario, o si no viene el filtro mostraremos como lo hacemos hoy, es decir `[NewBytes_DBF].[dbo].[articulo].EXCLUIR = 0`

```
GET {API_URL}/items?currentPage=1&itemsPerPage=300&search={palabra}&excluded=true
```
