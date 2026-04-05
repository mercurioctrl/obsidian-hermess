---
jira_key: "EXP-295"
aliases: ["EXP-295"]
summary: "API - Refactor - ordersRefund debe admitir pedidos que aun no fueron despachados"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-05-28 20:00"
updated: "2023-06-08 06:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-295"
---

# EXP-295: API - Refactor - ordersRefund debe admitir pedidos que aun no fueron despachados

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-05-28 20:00 |
| Actualizado | 2023-06-08 06:16 |
| Etiquetas | ninguna |
| Jira | [EXP-295](https://bluinc.atlassian.net/browse/EXP-295) |

## Relaciones

- **Padre:** [[EXP-294]] Refactor - Devoluciones (pre-despacho)

## Descripcion

Haremos un refactor del recurso 

```
POST {{API_URL}}/v1/ordersRefund/{pedido}
```

```
{
  "voucherTypeId": 2,
  "clientId": 45862,
  "pedido":"X000200558281",
  "trade":[
          {
            "units": 1,
            "price": 0.2,
            "ivaTax": 21,
            "internalId": 100502
          }
  ]
}
```

Para que nos permita hacer devoluciones (acreditar) productos dentro de un pedido que aun no fue despachado.

Para esto se deben tener en cuenta al menos dos aspectos:

1- Si el pedido aun no fue factura, entonces el tipo de devolución que hago, es igual al de suc 10 (no hace comprobante).

Para saber si esta facturado puedo usar `NewBytes_DBF.dbo.albclit.lfacturado = true`

2- Lo que estoy acreditando, no necesita tener serial, dado de justamente al no tenerlo disponible físicamente, por mas que tenga que serialzar 10 unidades de un producto para despachar, solo tendré 9 seriales. El que acredito no tiene.

3- Si ya se hicieron créditos anteriores tengo que tener en cuenta la columna `NewBytes_DBF.dbo.albclil.ACREDITADO` para limitar las unidades que se pueden devolver.
