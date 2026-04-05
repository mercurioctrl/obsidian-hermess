---
jira_key: "PED-798"
aliases: ["PED-798"]
summary: "API - Refactor - En la liquiadacion, solo cuando el pedido queda autorizaco (ID_sTATUS > 1), marcaremos la fecha de aturizacion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-08-19 08:20"
updated: "2024-08-27 04:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-798"
---

# PED-798: API - Refactor - En la liquiadacion, solo cuando el pedido queda autorizaco (ID_sTATUS > 1), marcaremos la fecha de aturizacion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-19 08:20 |
| Actualizado | 2024-08-27 04:06 |
| Etiquetas | ninguna |
| Jira | [PED-798](https://bluinc.atlassian.net/browse/PED-798) |

## Relaciones

- **Padre:** [[PED-123 - Feat - Liquidar pedido|PED-123]] Feat - Liquidar pedido
- **is blocked by:** [[PED-806 - API - Al autorizar un pedido almacenar la fecha y hora - Fecha no guardada|PED-806]] API - Al autorizar un pedido almacenar la fecha y hora - Fecha no guardada

## Descripcion

Para esto crearemos la columna `[NEW_BYTES].[dbo].[MS_VENTAS_REMITOS].F_H_AUTORIZADO`

En ella guardaremos fecha y hora del momento en que el pedido paso a estado > 1

Lo que se quiere, es poder tener el momento exacto en que el pedido fue autorizado, ya que estamos usando para ordenaros la fecha y hora del pedido o liquidación, pero no siempre es el ultimo que esta “Autorizado para preparar”
