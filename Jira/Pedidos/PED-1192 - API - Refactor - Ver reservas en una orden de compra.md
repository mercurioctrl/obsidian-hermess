---
jira_key: "PED-1192"
aliases: ["PED-1192"]
summary: "API - Refactor - Ver reservas en una orden de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Marbe Moreno"
created: "2025-12-15 12:23"
updated: "2025-12-18 14:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1192"
---

# PED-1192: API - Refactor - Ver reservas en una orden de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Marbe Moreno |
| Creado | 2025-12-15 12:23 |
| Actualizado | 2025-12-18 14:35 |
| Etiquetas | ninguna |
| Jira | [PED-1192](https://bluinc.atlassian.net/browse/PED-1192) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra
- **has action item:** [[PED-86]] APP - Feat - Ver reservas de una orden de compra
- **has action item:** [[PED-85]] API - Feat - Ver reservas en una orden de compra
- **has action item:** [[PED-1193]] APP - Refactor - Ver reservas en una orden de compra

## Descripcion

Este recurso debe poder recibir `stockWarehouseId` y filtrar correctamente

```
GET {API_URL}/v1/itemReservations/{itemId}?stockWarehouseId=1
```
