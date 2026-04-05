---
jira_key: "NBWEB-25"
aliases: ["NBWEB-25"]
summary: "Detalle Mis pedidos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-25 10:34"
updated: "2022-06-26 20:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-25"
---

# NBWEB-25: Detalle Mis pedidos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-25 10:34 |
| Actualizado | 2022-06-26 20:10 |
| Etiquetas | ninguna |
| Jira | [NBWEB-25](https://bluinc.atlassian.net/browse/NBWEB-25) |

## Relaciones

- **Padre:** [[NBWEB-2]] API - Mi cuenta

## Descripcion

Se trata del recurso para obtener del detalle de un pedido

```
GET {{API_URL}}/v1/miCuenta/pedidos/{branch}/{albNumber}
```

Retorna un array de objetos con los productos que contiene la orden de compra



```json
[
    {
        "branch": "0002",
        "albNumber": "00529823",
        "clientId": 45658,
        "productId": 7656,
        "description": "MOUSE GENIUS [[DX-110]] G5 BLACK PS2",
        "amount": 1.000,
        "iva": 10.50,
        "Price":{
          "value":53.56365,
          "iva":10.5,
          "finalPrice":59.187833250000004
        },
        "currencyQuote": 115.75,
        "percepcion": 0
    },
    {
    "branch": "0002",
    "albNumber": "00529823",
    "clientId": 45658,
    "productId": 7656,
    "description": "MOUSE GENIUS [[DX-110]] G5 BLACK PS2",
    "amount": 1.000,
    "iva": 10.50,
    "Price":{
      "value":53.56365,
      "iva":10.5,
      "finalPrice":59.187833250000004
    },
    "currencyQuote": 115.75,
    "perception": 0
  }
    ]
```



Las tablas para contruir la vista completa del pedido es `[NewBytes_DBF].[dbo].[albclit]` y `[NewBytes_DBF].[dbo].[albclil]`

Las tablas para obtener la percepcion es `[NEW_BYTES].[dbo].[MS_REMITO_CABECERA]` mediante el vinculo

`albclit.cnumscu = MS_REMITO_CABECERA and albclit.cnumalb = MS_REMITO_CABECERA.remito_fp`
