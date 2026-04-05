---
jira_key: "NBWEB-681"
summary: "API - Refactor - Agregar el nombre de medio de envio al objeto de las ordenes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-04-03 16:52"
updated: "2024-04-16 18:00"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-681"
---

# NBWEB-681: API - Refactor - Agregar el nombre de medio de envio al objeto de las ordenes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-03 16:52 |
| Actualizado | 2024-04-16 18:00 |
| Etiquetas | ninguna |
| Jira | [NBWEB-681](https://bluinc.atlassian.net/browse/NBWEB-681) |

## Descripción

Refactorizaremos el objeto para agregar `deliveryMethodDescription` y `deliveryMethodId`

```
GET v1/miCuenta/ordenesDeCompra
```

```
[
    {
        "status": 2,
        "branch": "0002",
        "orderNumber": "10343407",
        "clientName": "DEMARIA JAVIER ALBERTO",
        "userName": "",
        "clientId": 19494,
        "subtotal": {
            "currencyQuote": 880,
            "subtotalDollar": 544.25804,
            "subtotalDollarFinal": 601.875236,
            "subTotalPesosAr": 478947.0752,
            "subTotalPesosArFinal": 529650.20768
        },
        "date": "27-03-2024",
        "trackingNumber": "360001066217310",
        "deliveryMethodDescription": 'Andreani', <-- NUEVO PARAMETRO
        "deliveryMethodId": 2, <-- NUEVO PARAMETRO
        "secretKey": null,
        "paymentVoucher": false,
        "paymentMethodId": "3"
    },
    {
        "status": 1,
        "branch": "0002",
        "orderNumber": "10343312",
        "clientName": "DEMARIA JAVIER ALBERTO",
        "userName": "jdemaria",
        "clientId": 19494,
        "subtotal": {
            "currencyQuote": 880,
            "subtotalDollar": 544.21471,
            "subtotalDollarFinal": 601.8228067,
            "subTotalPesosAr": 478908.9448,
            "subTotalPesosArFinal": 529604.069896
        },
        "date": "26-03-2024",
        "trackingNumber": null,
        "secretKey": "oveja",
        "paymentVoucher": false,
        "paymentMethodId": "3"
    }
]
```
