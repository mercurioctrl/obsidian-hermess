---
jira_key: "NBWEB-234"
summary: "API - Obtener medios de pago mp"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-06-06 16:19"
updated: "2022-06-26 21:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-234"
---

# NBWEB-234: API - Obtener medios de pago mp

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-06 16:19 |
| Actualizado | 2022-06-26 21:08 |
| Etiquetas | ninguna |
| Jira | [NBWEB-234](https://bluinc.atlassian.net/browse/NBWEB-234) |

## Descripción

```
GET {{API_URL}}/v1/carrito/mpPaymentMethods
```

```
{
  "id": "8987269652",
  "date_created": "2021-03-16T16:08:20.592-04:00",
  "date_last_updated": "2021-03-16T16:08:20.592-04:00",
  "customer_id": "470183340-cpunOI7UsIHlHr",
  "expiration_month": 6,
  "expiration_year": 2023,
  "first_six_digits": "503143",
  "last_four_digits": "6351",
  "payment_method": {
    "id": "master",
    "name": "Mastercard",
    "payment_type_id": "credit_card",
    "thumbnail": "http://img.mlstatic.com/org-img/MP3/API/logos/master.gif",
    "secure_thumbnail": "https://www.mercadopago.com/org-img/MP3/API/logos/master.gif"
  },
  "security_code": {
    "length": 3,
    "card_location": "back"
  },
  "issuer": {
    "id": 24,
    "name": "Mastercard"
  },
  "cardholder": {
    "name": "APRO",
    "identification": {
      "number": "19119119100",
      "type": "CPF"
    }
  },
  "user_id": "470183340",
  "live_mode": true
}
```

`Recusro en mp: https://api.mercadopago.com/v1/customers/{customer_id}`

El `customer_id` se obtiene vinculando el cliente interno de nb con el customer_id (client_mercadopago)
