---
jira_key: "PED-1143"
aliases: ["PED-1143"]
summary: "API - MVP - Refactor - Filtro de deposito para el recurso items"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-10-06 14:09"
updated: "2025-10-28 10:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1143"
---

# PED-1143: API - MVP - Refactor - Filtro de deposito para el recurso items

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-06 14:09 |
| Actualizado | 2025-10-28 10:50 |
| Etiquetas | ninguna |
| Jira | [PED-1143](https://bluinc.atlassian.net/browse/PED-1143) |

## Relaciones

- **Padre:** [[PED-1107]] Almacenes Multiples
- **action item from:** [[PED-1108]] API - MVP - Refactor - Mostrar items con almacenes multiples, cuando existan, y agregar el parametro stockWarehouseId
- **has action item:** [[PED-1144]] APP - MVP - Feat - Filtro de deposito para el recurso items

## Descripcion

Agregaremos un filtro para el recurso `items` que nos permita ver solo el stock de un “almacén” determinado

```
GET {API_URL}/v1/items?stockWarehouseId={stockWarehouseId}
```
