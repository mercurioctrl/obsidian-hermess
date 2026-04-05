---
jira_key: "NBWEB-242"
summary: "APP - Procesar pago con tarjeta y plata en cuenta de mp"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-06-08 13:53"
updated: "2022-06-26 21:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-242"
---

# NBWEB-242: APP - Procesar pago con tarjeta y plata en cuenta de mp

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-08 13:53 |
| Actualizado | 2022-06-26 21:08 |
| Etiquetas | ninguna |
| Jira | [NBWEB-242](https://bluinc.atlassian.net/browse/NBWEB-242) |

## Descripción

Devuelve `"savePaymentMethod": true`

si acepto guardar las tarjetas


```
POST {{API_URL}}/v1/carrito/processPayment
```



```
{
    "token": "30eff525a87ffe8901c281f72deff905",
    "issuer_id": "3",
    "payment_method_id": "master",
    "transaction_amount": 1962.2146109999996,
    "installments": 1,
    "description": "Descripción del producto",
    "payer": {
        "email": "soporteweb2@nb.com.ar",
        "identification": {
            "type": "DNI",
            "number": "37892693"
        },
        "clientId": 27613,
        "orderId": "10217331",
        "branch": "0002"
    },
    "savePaymentMethod": true
}
```
