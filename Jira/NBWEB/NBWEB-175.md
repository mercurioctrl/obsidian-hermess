---
jira_key: "NBWEB-175"
summary: "APP - Mi cuenta - Pedidos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Marbe Moreno"
created: "2022-05-12 09:56"
updated: "2023-02-02 15:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-175"
---

# NBWEB-175: APP - Mi cuenta - Pedidos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Marbe Moreno |
| Creado | 2022-05-12 09:56 |
| Actualizado | 2023-02-02 15:10 |
| Etiquetas | ninguna |
| Jira | [NBWEB-175](https://bluinc.atlassian.net/browse/NBWEB-175) |

## Descripción

### Pedidos 

```
GET {{API_URL}}/v1/miCuenta/pedidos?limit=10&offset=10
```



```json
[
 {
        "status": 1,
        "branch": "0002",
        "albNumber": "00495427",
        "clientName": "KWIK-E-MART",
        "clientId": 00001,
        "subtotal": {
            "currencyQuote": 105,
            "subtotalDollar": 1059.9822,
            "subtotalDollarFinal": 1282.578462,
            "subTotalPesosAr": 111298.131,
            "subTotalPesosArFinal": 134670.73851
        }
    },
]


```

### 

### Detalle del pedido

```
GET {{API_URL}}/v1/miCuenta/pedidos/0002/00495427
```



```json
[
    {
        "branch": "0002",
        "albNumber": "00495427",
        "clientId": 25433,
        "productId": "104835",
        "description": "AURICULAR GAMER RAZER BLACKSHARK V2 X WIRED/7.1",
        "amount": "27.000",
        "price": {
            "value": 39.2586,
            "iva": 21,
            "finalPrice": 47.502906
        },
        "currencyQuote": 105,
        "perception": 0
    }
]


```
