---
jira_key: "NBWEB-188"
aliases: ["NBWEB-188"]
summary: "API - Pagos - Procesar pagos con tarjeta"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-05-16 14:48"
updated: "2022-06-26 21:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-188"
---

# NBWEB-188: API - Pagos - Procesar pagos con tarjeta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-16 14:48 |
| Actualizado | 2022-06-26 21:33 |
| Etiquetas | ninguna |
| Jira | [NBWEB-188](https://bluinc.atlassian.net/browse/NBWEB-188) |

## Relaciones

- **Padre:** [[NBWEB-77]] Implementar Pagos
- **blocks:** [[NBWEB-242]] APP - Procesar pago con tarjeta y plata en cuenta de mp

## Descripcion

```
POST {{API_URL}}/v1/carrito/processPayment
```

Recibe del formulario 

`http://omega.nb.com.ar/mercadopago?branch={numeroDeBranch}&orderNumber={numero de orden}`

```json
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

Si `savePaymentMethod` esta en true se guarda el metodo de pago dentro de mercadopago para este cliente.

Retorna:

```
{
  succes: true
}
```
