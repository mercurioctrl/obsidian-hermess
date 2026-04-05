---
jira_key: "COB-396"
aliases: ["COB-396"]
summary: "APi - Refactor - Response Object en Cobros Simultaneos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2023-04-10 12:26"
updated: "2023-04-24 07:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-396"
---

# COB-396: APi - Refactor - Response Object en Cobros Simultaneos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2023-04-10 12:26 |
| Actualizado | 2023-04-24 07:44 |
| Etiquetas | ninguna |
| Jira | [COB-396](https://bluinc.atlassian.net/browse/COB-396) |

## Relaciones

- **Padre:** [[COB-389 - Refactor - Cobros multiples|COB-389]] Refactor - Cobros multiples
- **blocks:** [[COB-391 - APP - Refactor - Cobrar mas de un pedido en el mismo cobro|COB-391]] APP - Refactor - Cobrar mas de un pedido en el mismo "cobro"

## Descripcion

Al utilizar el recurso.

```
/v1/box/Seba?currentPage=1&branch=0002&cnumalb=00543642
```

Retorna el siguiente object según lo conversado en la daily - 10/04/2023.

```
{
    "response": [
        {
            "movementId": 637492,
            "trCode": "42",
            "dateHour": "10-04-2023 10:15",
            "description": "Cobro Efectivo Caja",
            "subtotal": 21000,
            "currency": "PESOS",
            "symbol": "+",
            "userName": "SEBA",
            "comment": "PRUEBA MULTIPLE PAGOS",
            "branch": null,
            "albNumber": null,
            "symbol_F10": "+",
            "clientId": null,
            "clientName": null,
            "documentReference": "-",
            "boxOrigin": "Seba",
            "boxDestiny": null,
            "canceled": false,
            "cotization": 0
        },
        {
            "movementBankId": 151840,
            "dateHour": "10-04-2023 10:04",
            "subtotal": 21000,
            "currency": "PESOS",
            "userName": "Seba",
            "description": "Banco Galicia",
            "accountBank": 2,
            "comment": "Prueba Multiple Pagos Cobro por caja: Seba - Pedidos Simultaneos:X000200543684, X000200543642, X000200543641 - Cliente: 32103",
            "albNumber": null,
            "branch": null,
            "clientId": 32103,
            "clientName": "Libre Opcion Libre Opcion",
            "cotization": 105
        },
        {
            "ctaCteId": 677726,
            "dateHour": "10-04-2023 10:04",
            "subtotal": 100,
            "currency": "DOLAR",
            "userName": "Seba",
            "description": "Cta Cte - Cobrar al Cliente",
            "comment": "Pago simultaneo",
            "albNumber": null,
            "branch": null,
            "clientId": "32103",
            "clientName": "Libre Opcion Libre Opcion",
            "cotization": 140
        }
    ],
    "simultaneous": {
        "X000200543641": [
            {
                "id": 9914,
                "dateHour": "10-04-2023 10:04",
                "subtotal": 7.4499998,
                "description": "CTA CTE CLIENTE"
            },
            {
                "id": 9915,
                "dateHour": "10-04-2023 10:04",
                "subtotal": 1564.5,
                "description": "PESOS"
            },
            {
                "id": 9916,
                "dateHour": "10-04-2023 10:04",
                "subtotal": 1564.5,
                "description": "DEPOSITO BANCARIO EN PESOS"
            }
        ],
        "X000200543642": [
            {
                "id": 9917,
                "dateHour": "10-04-2023 10:04",
                "subtotal": 21.452499,
                "description": "CTA CTE CLIENTE"
            },
            {
                "id": 9918,
                "dateHour": "10-04-2023 10:04",
                "subtotal": 4505.0249,
                "description": "PESOS"
            },
            {
                "id": 9919,
                "dateHour": "10-04-2023 10:04",
                "subtotal": 4505.0249,
                "description": "DEPOSITO BANCARIO EN PESOS"
            }
        ],
        "X000200543684": [
            {
                "id": 9920,
                "dateHour": "10-04-2023 10:04",
                "subtotal": 67.626671,
                "description": "CTA CTE CLIENTE"
            },
            {
                "id": 9921,
                "dateHour": "10-04-2023 10:04",
                "subtotal": 14201.601,
                "description": "PESOS"
            },
            {
                "id": 9922,
                "dateHour": "10-04-2023 10:04",
                "subtotal": 14201.601,
                "description": "DEPOSITO BANCARIO EN PESOS"
            }
        ]
    }
}
```
