---
jira_key: "COB-543"
aliases: ["COB-543"]
summary: "API - Refactor - En el Cobro, solo cuando el pedido queda autorizado (ID_STATUS > 1), marcaremos la fecha de autorizacion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-08-19 08:22"
updated: "2024-08-25 23:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-543"
---

# COB-543: API - Refactor - En el Cobro, solo cuando el pedido queda autorizado (ID_STATUS > 1), marcaremos la fecha de autorizacion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-19 08:22 |
| Actualizado | 2024-08-25 23:11 |
| Etiquetas | ninguna |
| Jira | [COB-543](https://bluinc.atlassian.net/browse/COB-543) |

## Relaciones

- **Padre:** [[COB-389]] Refactor - Cobros multiples

## Descripcion

Similar a [link](https://lioteam.atlassian.net/browse/PED-798) 

pero desde cuando se hace un cobro.

Básicamente una vez cobrado (osea ID_STATUS > 1) debemos registar el momento en la columna `[NEW_BYTES].[dbo].[MS_VENTAS_REMITOS].F_H_AUTORIZADO`
