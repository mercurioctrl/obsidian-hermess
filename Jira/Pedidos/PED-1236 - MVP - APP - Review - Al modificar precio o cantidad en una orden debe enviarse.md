---
jira_key: "PED-1236"
aliases: ["PED-1236"]
summary: "MVP - APP - Review - Al modificar precio o cantidad en una orden debe enviarse tambien el costForSale en caso de tenerlo asi no se pierde"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Marbe Moreno"
created: "2026-01-06 17:53"
updated: "2026-03-05 09:30"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1236"
---

# PED-1236: MVP - APP - Review - Al modificar precio o cantidad en una orden debe enviarse tambien el costForSale en caso de tenerlo asi no se pierde

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Marbe Moreno |
| Creado | 2026-01-06 17:53 |
| Actualizado | 2026-03-05 09:30 |
| Etiquetas | ninguna |
| Jira | [PED-1236](https://bluinc.atlassian.net/browse/PED-1236) |

## Relaciones

- **Padre:** [[PED-3]] Ordenes de compra

## Descripcion

Cuando se edita una orden solo se envia el `costForSale` al editar el selector, pero se debe enviar cuando se editan el resto de parametros, para evitar errores como obtener `costForSale=null`
