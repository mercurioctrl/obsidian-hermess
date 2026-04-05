---
jira_key: "EXP-359"
aliases: ["EXP-359"]
summary: "API - Refactor - Agregar percepciones a las ordenes"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-08-07 08:41"
updated: "2023-08-07 09:54"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-359"
---

# EXP-359: API - Refactor - Agregar percepciones a las ordenes

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-07 08:41 |
| Actualizado | 2023-08-07 09:54 |
| Etiquetas | ninguna |
| Jira | [EXP-359](https://bluinc.atlassian.net/browse/EXP-359) |

## Relaciones

- **Padre:** [[EXP-355 - Emision de facturas|EXP-355]] Emision de facturas

## Descripcion

En principio, aunque no lo agregaremos ahora. Agregaremos el parámetro `iibbPerception` al recurso 

```
GET /v1/orders/X000200562697
```

Que se obtiene de la siguiente columna

`[NEW_BYTES].[dbo].[MS_REMITO_CABECERA].IMPPERCEP`

El fin de esto, es poder construir el objeto necesario para construir la factura mediante el recurso `/v2/CreateVoucher` del servicio de comprobantes.
