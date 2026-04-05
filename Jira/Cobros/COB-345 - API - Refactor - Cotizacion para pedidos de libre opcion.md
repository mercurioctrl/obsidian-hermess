---
jira_key: "COB-345"
aliases: ["COB-345"]
summary: "API - Refactor - Cotizacion para pedidos de libre opcion"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-03-09 16:22"
updated: "2023-03-10 12:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-345"
---

# COB-345: API - Refactor - Cotizacion para pedidos de libre opcion

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-09 16:22 |
| Actualizado | 2023-03-10 12:48 |
| Etiquetas | ninguna |
| Jira | [COB-345](https://bluinc.atlassian.net/browse/COB-345) |

## Relaciones

- **Padre:** [[COB-329 - Refactor - Auto liquidar si el medio de pago es efectivo y retiro|COB-329]] Refactor - Auto liquidar si el medio de pago es efectivo y retiro

## Descripcion

En la autoliquidacion discriminaremos los pedidos de libre opcion

```
SELECT cobserv
  FROM [NewBytes_DBF].[dbo].[pedclit]
  where cnumped = '10283909'
```

Y de ser uno de estos, mostraremos siempre la cotizacion obtenida de

```
SELECT nvaldiv
  FROM [NewBytes_DBF].[dbo].[pedclit]
  where cnumped = '10283909'
```

De esta forma nos aseguramos que el pedido corresponda al monto en pesos que el CONSUMIDOR FINAL compro (los casos de new bytes no deben tocarse).
