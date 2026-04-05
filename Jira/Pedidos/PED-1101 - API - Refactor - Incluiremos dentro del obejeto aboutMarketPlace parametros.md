---
jira_key: "PED-1101"
aliases: ["PED-1101"]
summary: "API - Refactor - Incluiremos dentro del obejeto  aboutMarketPlace parametros relativos al dinero usado en wallet para mostrar como fue la operacion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-09-12 15:11"
updated: "2025-09-24 11:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1101"
---

# PED-1101: API - Refactor - Incluiremos dentro del obejeto  aboutMarketPlace parametros relativos al dinero usado en wallet para mostrar como fue la operacion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-09-12 15:11 |
| Actualizado | 2025-09-24 11:18 |
| Etiquetas | ninguna |
| Jira | [PED-1101](https://bluinc.atlassian.net/browse/PED-1101) |

## Relaciones

- **Padre:** [[PED-54]] Cuenta corriente de clientes
- **has action item:** [[PED-1110]] APP - Refactor - Agrear al modulo de marketplace el importe utilizado para llegar al monto del pedido

## Descripcion

Se debe agregar el paremtro walletUsedHere al siguiente recurso de pedidos

```
GET /v1/aboutMarketPlace/0002-10425224
```

este parametro contiene el importe en pesos utilizado por la wallet en la confirmacion de una compra desde LO.



```json
{
    "success": true,
    "msg": "Pedido encontrado",
    "data": {
        "document": "37892693",
        ....
        "ipOrigin": "181.116.45.185",
        "items": [
            {
                "distributorId": 1,
                "detailIdLo": 787978,
                "productIdLo": 387022,
                "resellerOrderId": 745611,
                "priceLo": 7556,
                "discountLo": 0,
                "walletUsedHere": 1000,-------------> nuevo paremtro en pesos.
                "discount": 0,
                "clientCostLo": 5.06,
                "utilityLo": 2,
                "iva": 10.5,
                "amountLo": 1,
                "descriptionLo": "TECLADO GENIUS RS2 [[KB-116]] SP BLK",
                "itemId": 103788,
                "refundLo": 0
            }
        ]
    }
}
```
