---
jira_key: "COB-111"
aliases: ["COB-111"]
summary: "API - Feat - Listar Metodos de Pago Remitos Vendedores"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2022-09-22 11:38"
updated: "2022-10-25 09:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-111"
---

# COB-111: API - Feat - Listar Metodos de Pago Remitos Vendedores

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2022-09-22 11:38 |
| Actualizado | 2022-10-25 09:02 |
| Etiquetas | ninguna |
| Jira | [COB-111](https://bluinc.atlassian.net/browse/COB-111) |

## Relaciones

- **Padre:** [[COB-41]] APP - Feat -  Listar cobrables

## Descripcion

```
GET {{API_URL}}/v1/tradablePaymentMethod
```

Recurso que lista todos los metodos de pago proveniente de la tabla  `[NEW_BYTES].[dbo].[MS_FORMASPAGO_REMITOS_VENDEDORES]`

[
    {
        "paymentMethodId": 1,
        "description": "Cta. Cte Cliente",
        "show": false,
        "interest": 0
    },
    {
        "paymentMethodId": 2,
        "description": "Efectivo Moto",
        "show": false,
        "interest": 0
    },
    {
        "paymentMethodId": 3,
        "description": "Depósito en Banco",
        "show": true,
        "interest": 0
    },
    {
        "paymentMethodId": 4,
        "description": "Efectivo Camioneta",
        "show": false,
        "interest": 0
    },
    {
        "paymentMethodId": 5,
        "description": "Efectivo Caja",
        "show": true,
        "interest": 0
    },
    {
        "paymentMethodId": 6,
        "description": "Cheque Cliente",
        "show": true,
        "interest": 0
    },
    {
        "paymentMethodId": 7,
        "description": "Mpago NB",
        "show": false,
        "interest": 0
    },
    {
        "paymentMethodId": 8,
        "description": "Mpago LO",
        "show": false,
        "interest": 0
    },
    {
        "paymentMethodId": 9,
        "description": "Efectivo LO Cons. Final",
        "show": false,
        "interest": 0
    },
    {
        "paymentMethodId": 10,
        "description": "Efectivo LO GREEN CASH",
        "show": false,
        "interest": 0
    },
    {
        "paymentMethodId": 11,
        "description": "Tarjeta Credito",
        "show": false,
        "interest": 50
    },
    {
        "paymentMethodId": 12,
        "description": "Tarjeta AHORA 12",
        "show": false,
        "interest": 0
    },
    {
        "paymentMethodId": 13,
        "description": "Tarjeta AHORA 18",
        "show": false,
        "interest": 0
    },
    {
        "paymentMethodId": 14,
        "description": "Tarjeta Debito",
        "show": false,
        "interest": 0
    },
    {
        "paymentMethodId": 15,
        "description": "Dinero en mercadopago",
        "show": false,
        "interest": 0
    }
]
