---
jira_key: "INV-273"
aliases: ["INV-273"]
summary: "API - MVP Refactor - Syncup  Sell In/ Sell Out -> Agregar almacén al historial"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2025-12-05 02:35"
updated: "2025-12-08 15:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-273"
---

# INV-273: API - MVP Refactor - Syncup  Sell In/ Sell Out -> Agregar almacén al historial

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2025-12-05 02:35 |
| Actualizado | 2025-12-08 15:03 |
| Etiquetas | ninguna |
| Jira | [INV-273](https://bluinc.atlassian.net/browse/INV-273) |

## Relaciones

- **Padre:** [[INV-250]] Repositorio de Sell In Sell Out
- **relates to:** [[INV-252]] API - MVP - Sync up - Modificacion de costos por sellIn sellOut ( Se encarga de ajustar los costosy guardar los valores anteriores segun el criterio de fecha o cantidad de corte)

## Descripcion

Haremos un refactor para que, al ejecutar el syncup, también se guarde el `stockWarehouseId`, con el fin de identificar a qué artículo y en qué depósito se le aplicó el descuento.

```
POST {{API_URL}}/sellDiscount/syncUp
```

[adjunto]
