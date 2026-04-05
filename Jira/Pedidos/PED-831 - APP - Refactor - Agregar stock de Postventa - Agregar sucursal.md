---
jira_key: "PED-831"
aliases: ["PED-831"]
summary: "APP - Refactor - Agregar stock de Postventa -> Agregar sucursal"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2024-09-24 03:12"
updated: "2024-11-19 15:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-831"
---

# PED-831: APP - Refactor - Agregar stock de Postventa -> Agregar sucursal

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2024-09-24 03:12 |
| Actualizado | 2024-11-19 15:05 |
| Etiquetas | ninguna |
| Jira | [PED-831](https://bluinc.atlassian.net/browse/PED-831) |

## Relaciones

- **Padre:** [[PED-4 - Pedidos|PED-4]] Pedidos
- **relates to:** [[INV-95 - API - Refactor - Agregar nuevo producto|INV-95]] API - Refactor - Agregar nuevo producto
- **relates to:** [[PED-827 - APP - Refactor - Agregar stock de postventa|PED-827]] APP - Refactor - Agregar stock de postventa
- **has action item:** [[SNB-2535 - no podemos generar pedido para uso internos|SNB-2535]] no podemos generar pedido para uso internos

## Descripcion

Con el fin de poder crear ordenes para postventa agregaremos la sucursal 0003, solo usuarios con el rol de `Jefe de servicio post venta` y `Departamento RMA` pueden agregar este tipo de orden.

[adjunto]
