---
jira_key: "NBWEB-233"
summary: "API - Buscar un cliente en mercadopago"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-06-06 16:17"
updated: "2022-06-26 21:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-233"
---

# NBWEB-233: API - Buscar un cliente en mercadopago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-06 16:17 |
| Actualizado | 2022-06-26 21:07 |
| Etiquetas | ninguna |
| Jira | [NBWEB-233](https://bluinc.atlassian.net/browse/NBWEB-233) |

## Descripción

Se busca el cliente guardado en mercado pago, si no existe se debe crear y se guarda en la tabla `client_mercadopago`

```
GET {{API_URL}}/v1/carrito/mpClient/{correo cliente}
```

Retorna

```
{
  "paging": {
    "limit": 10,
    "offset": 0,
    "total": 1
  },
  "results": [
    {
      "address": {
        "id": "1162600213",
        "street_name": "Caetano Poli, 12",
        "zip_code": "05187010"
      },
      "addresses": [
        {}
      ],
      "cards": [
        {}
      ],
      "date_created": "2017-05-05T04:00:00.000Z",
      "date_last_updated": "2017-05-05T13:23:25.021Z",
      "default_address": "1162600213",
      "default_card": 1493990563105,
      "email": "test@test.com",
      "first_name": "Customer",
      "id": "123456789-jxOV430go9fx2e",
      "identification": {
        "number": "19119119100",
        "type": "CPF"
      },
      "last_name": "Tester",
      "live_mode": true,
      "metadata": {},
      "phone": {
        "area_code": "11",
        "number": "987654321"
      }
    }
  ]
}
```
