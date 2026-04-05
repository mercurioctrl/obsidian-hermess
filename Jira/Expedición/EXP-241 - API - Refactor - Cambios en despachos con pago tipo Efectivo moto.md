---
jira_key: "EXP-241"
aliases: ["EXP-241"]
summary: "API - Refactor - Cambios en despachos con pago tipo \"Efectivo moto\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-03-17 09:37"
updated: "2023-04-11 10:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-241"
---

# EXP-241: API - Refactor - Cambios en despachos con pago tipo "Efectivo moto"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-17 09:37 |
| Actualizado | 2023-04-11 10:26 |
| Etiquetas | ninguna |
| Jira | [EXP-241](https://bluinc.atlassian.net/browse/EXP-241) |

## Relaciones

- **Padre:** [[EXP-12 - Feat - Listar pedidos para envio|EXP-12]] Feat - Listar pedidos para envio

## Descripcion

Modificaremos el recurso para “Despachar” [https://lioteam.atlassian.net/browse/EXP-98](https://lioteam.atlassian.net/browse/EXP-98) de tal manera que solo si es “Efectivo Moto”, una vez despachado el estado siguiente sea “Despachado, Pendiente a Cobrar” en lugar de “Finalizado”.

Solo en ese caso, setearemos ese valor en la columna `ID_STATUS` en `[NEW_BYTES].[dbo].[MS_VENTAS_REMITOS]`

 

Los estados posibles se encuentran en: `[NEW_BYTES].[dbo].[MS_STATUS_REMITO] `



Esto se hacer para marcarlos como pendientes de cobro, y luego poder dejarlos aparte hasta que sean cobrados.
