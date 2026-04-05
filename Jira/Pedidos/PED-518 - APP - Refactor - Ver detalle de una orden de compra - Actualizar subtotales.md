---
jira_key: "PED-518"
aliases: ["PED-518"]
summary: "APP - Refactor - Ver detalle de una orden de compra - Actualizar subtotales"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2024-01-26 18:04"
updated: "2024-01-31 22:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-518"
---

# PED-518: APP - Refactor - Ver detalle de una orden de compra - Actualizar subtotales

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2024-01-26 18:04 |
| Actualizado | 2024-01-31 22:13 |
| Etiquetas | ninguna |
| Jira | [PED-518](https://bluinc.atlassian.net/browse/PED-518) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra
- **relates to:** [[PED-83]] APP - Feat - Ver detalle de una orden de compra
- **relates to:** [[SNB-1466]] SALDOS TOTALES ERRONEOS
- **relates to:** [[PED-519]] API - Review - Revisar respuesta del recurso /orders/addItem

## Descripcion

Al momento de modificar los precios de los productos, en una orden, no se actualizan automáticamente los subtotales sino hasta que cierro el modal y vuelvo a abrirlo.

[adjunto]
[adjunto]


Dato extra:

Esto puede suceder debido a que los subtotales solo se calculan al abrir el detalle de la orden.
