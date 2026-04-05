---
jira_key: "EXP-322"
aliases: ["EXP-322"]
summary: "API - Refactor - Devolución, excepciones de cambio de estado"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-06-26 20:23"
updated: "2023-06-28 12:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-322"
---

# EXP-322: API - Refactor - Devolución, excepciones de cambio de estado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-06-26 20:23 |
| Actualizado | 2023-06-28 12:46 |
| Etiquetas | ninguna |
| Jira | [EXP-322](https://bluinc.atlassian.net/browse/EXP-322) |

## Relaciones

- **Padre:** [[EXP-294]] Refactor - Devoluciones (pre-despacho)
- **blocks:** [[SNB-877]] Autorizacion pedido

## Descripcion

Cuando el pedido se encuentra en 

`[NEW_BYTES].[dbo].[MS_VENTAS_REMITOS].[ID_STATUS]` = 1 

`[NEW_BYTES].[dbo].[MS_VENTAS_REMITOS].[ID_STATUS]` = 2

Entonces no se hace el cambio de estado por mas que haga una devolución
