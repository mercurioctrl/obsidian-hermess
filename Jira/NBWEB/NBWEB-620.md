---
jira_key: "NBWEB-620"
summary: "API - Feat - Setear medio de pago, asi como seteamos cuando tiene un envio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-01-24 08:55"
updated: "2024-01-31 00:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-620"
---

# NBWEB-620: API - Feat - Setear medio de pago, asi como seteamos cuando tiene un envio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-24 08:55 |
| Actualizado | 2024-01-31 00:25 |
| Etiquetas | ninguna |
| Jira | [NBWEB-620](https://bluinc.atlassian.net/browse/NBWEB-620) |

## Descripción

Al procesar un carrito y crear una orden en `[NewBytes_DBF].[dbo].[pedclit]`

Agregaremos la columna paymentMethodId de modo tal que podamos setearlo 

`[NewBytes_DBF].[dbo].[pedclit].paymentMethodId` segun la eleccion del cliente, porque aparentemente al dia de hoy se esta perdiendo el dato.

Coméntame si lo estamos guardando en algún lugar diferente.
