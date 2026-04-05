---
jira_key: "PED-751"
aliases: ["PED-751"]
summary: "API - Refactor  ajustar parametros al actualizar estado de orden en acción autorizar"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Sin asignar"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-06-24 16:18"
updated: "2024-06-28 20:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-751"
---

# PED-751: API - Refactor  ajustar parametros al actualizar estado de orden en acción autorizar

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Sin asignar |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-06-24 16:18 |
| Actualizado | 2024-06-28 20:17 |
| Etiquetas | ninguna |
| Jira | [PED-751](https://bluinc.atlassian.net/browse/PED-751) |

## Relaciones

- **Padre:** [[PED-3 - Ordenes de compra|PED-3]] Ordenes de compra

## Descripcion

Esta corresponde a una mejora en el metodo   

`updateOrderStatusFinalized($remitFp, $sucRemit, $newStatus): bool {}` 

de la clase `BoxTradeRepository`
