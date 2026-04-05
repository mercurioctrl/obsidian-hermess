---
jira_key: "PED-551"
aliases: ["PED-551"]
summary: "APP - Refactor - Ver detalle de orden de compra -> Marcar faltantes en caso de existir (casillero rojo)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-02-09 10:28"
updated: "2024-02-14 17:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-551"
---

# PED-551: APP - Refactor - Ver detalle de orden de compra -> Marcar faltantes en caso de existir (casillero rojo)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-09 10:28 |
| Actualizado | 2024-02-14 17:45 |
| Etiquetas | ninguna |
| Jira | [PED-551](https://bluinc.atlassian.net/browse/PED-551) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra
- **is blocked by:** [[PED-550]] API - Refactor - Ver detalle de orden de compra -> Agregar stocks

## Descripcion

Basándonos en los parámetros agregados en [link](https://lioteam.atlassian.net/browse/PED-550)  utilizaremos los campos `stock`, `stockLio`, `stockInOrders`, `availableStock` para determinar si el producto esta disponible de la misma forma  que lo hacemos en el listrado de producto.

Caso contrario lo marcaremos en rojo.

Esto solo se hace cuando el pedido aun esta en status = 'P'
