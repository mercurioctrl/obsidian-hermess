---
jira_key: "INV-304"
aliases: ["INV-304"]
summary: "API - Review - El recurso itemsStocks/examine debe traer  registros incluso cuando no se filtra el ID_ALMACEN de manera explicita"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-12-25 20:38"
updated: "2026-01-08 10:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-304"
---

# INV-304: API - Review - El recurso itemsStocks/examine debe traer  registros incluso cuando no se filtra el ID_ALMACEN de manera explicita

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-25 20:38 |
| Actualizado | 2026-01-08 10:37 |
| Etiquetas | ninguna |
| Jira | [INV-304](https://bluinc.atlassian.net/browse/INV-304) |

## Relaciones

- **Padre:** [[INV-199 - Control de Stock Stock en general Control de Precios|INV-199]] Control de Stock / Stock en general  / Control de Precios
- **is cloned by:** [[INV-316 - API - Review - El recurso itemsStocksexamine debe traer registros incluso|INV-316]] API - Review - El recurso itemsStocks/examine debe traer  registros incluso cuando no se filtra el ID_ALMACEN de manera explicita -> Error de sintaxis

## Descripcion

En la linea de lo que venimos viendo se debe refactorizar el recurso para que en caso de no contar con el filtro explícito, los muestre todos incluso aquellos que están en NULL

```
GET {API_URL}/itemsStocks/examine?itemId=118357&type=salesReserved&between=01-11-2020_25-12-2025&currentPage=1&itemsPerPage=20&warehouseId=2
```
