---
jira_key: "PED-1193"
aliases: ["PED-1193"]
summary: "APP - Refactor - Ver reservas en una orden de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Marbe Moreno"
created: "2025-12-15 12:24"
updated: "2025-12-19 12:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1193"
---

# PED-1193: APP - Refactor - Ver reservas en una orden de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Marbe Moreno |
| Creado | 2025-12-15 12:24 |
| Actualizado | 2025-12-19 12:07 |
| Etiquetas | ninguna |
| Jira | [PED-1193](https://bluinc.atlassian.net/browse/PED-1193) |

## Relaciones

- **Padre:** [[PED-8 - Listar ordenes de compra|PED-8]] Listar ordenes de compra
- **has action item:** [[PED-86 - APP - Feat - Ver reservas de una orden de compra|PED-86]] APP - Feat - Ver reservas de una orden de compra
- **action item from:** [[PED-1192 - API - Refactor - Ver reservas en una orden de compra|PED-1192]] API - Refactor - Ver reservas en una orden de compra

## Descripcion

Este recurso debe poder envair `stockWarehouseId` y filtrar correctamente

```
GET {API_URL}/v1/itemReservations/{itemId}?stockWarehouseId=1
```

[adjunto]
