---
jira_key: "PED-322"
aliases: ["PED-322"]
summary: "API - Ver detalle de una orden de compra -> Cotización incorrecta - Incidencias varias"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2023-12-11 08:35"
updated: "2023-12-12 21:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-322"
---

# PED-322: API - Ver detalle de una orden de compra -> Cotización incorrecta - Incidencias varias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2023-12-11 08:35 |
| Actualizado | 2023-12-12 21:11 |
| Etiquetas | ninguna |
| Jira | [PED-322](https://bluinc.atlassian.net/browse/PED-322) |

## Relaciones

- **blocks:** [[PED-305]] API - Refactor - Ver detalle de una orden de compra -> Se obtiene (en algunos casos) la cotizacion de manera incorrecta

## Descripcion

Al ver el flujo del recurso `OrderController::class, 'getDetail'` no encuentro la parte en la que se considera obtener la cotización en el caso de que la orden está liquidada, proveniente de `[NEW_BYTES].[dbo].[MS_REMITO_CABECERA].COTIZACION`, o la cotización del día, proveniente de `[NEW_BYTES].[dbo].[MS_COTIZACIONES]`

[adjunto]
Considerar dar un vistazo a esta otra incidencia en la que comento algunos detalles que encontré en las cotizaciones.

[[PED-320] API - Mostrar cotización correspondiente en pedidos cerrados - Incidencias varias](https://lioteam.atlassian.net/browse/PED-320)
