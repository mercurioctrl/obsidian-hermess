---
jira_key: "LOCAPP-24"
summary: "API - Refactor - Guardar el modo de pago al generar un comprobante"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-02-07 16:17"
updated: "2024-06-05 17:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-24"
---

# LOCAPP-24: API - Refactor - Guardar el modo de pago al generar un comprobante

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-07 16:17 |
| Actualizado | 2024-06-05 17:42 |
| Etiquetas | ninguna |
| Jira | [LOCAPP-24](https://bluinc.atlassian.net/browse/LOCAPP-24) |

## Descripción

Por lo que pude ver, venimos guardando el dato `[NewBytes_DBF].[dbo].[FP_FactWebCliEncabezado].ID_FORMADEPAGO` siempre en 1.

El mismo corresponde a la forma en que esta emitido el pago de un pedido y corresponde a los valores obtenidos en la tabla `[NewBytes_DBF].[dbo].[FP_FormasPagos]`

El problema que veo, es que no encuentro una forma de enlazarlo con la tabla `[NEW_BYTES].[dbo].[MS_FORMASPAGO_REMITOS_VENDEDORES]` que es donde realmente veo como se pago…

En caso de no haber un indice comuno una equivalencia deberemos agregarla.
