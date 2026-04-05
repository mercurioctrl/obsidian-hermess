---
jira_key: "COB-337"
aliases: ["COB-337"]
summary: "API - Refactor - Tipo de cambio especifico para pedidos de libre opcion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-03-03 12:43"
updated: "2023-03-13 16:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-337"
---

# COB-337: API - Refactor - Tipo de cambio especifico para pedidos de libre opcion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-03 12:43 |
| Actualizado | 2023-03-13 16:06 |
| Etiquetas | ninguna |
| Jira | [COB-337](https://bluinc.atlassian.net/browse/COB-337) |

## Relaciones

- **Padre:** [[COB-329 - Refactor - Auto liquidar si el medio de pago es efectivo y retiro|COB-329]] Refactor - Auto liquidar si el medio de pago es efectivo y retiro

## Descripcion

En el caso que se realizara un auto liquidación de un pedido de libre opción, la cotización a utilizarse sera la que devuelve

```
SELECT COTIZACION
FROM [NEW_BYTES].[dbo].[MS_COTIZACIONES]
WHERE id = 3
```
