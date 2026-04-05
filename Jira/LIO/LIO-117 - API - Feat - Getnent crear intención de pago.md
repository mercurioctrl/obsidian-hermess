---
jira_key: "LIO-117"
aliases: ["LIO-117"]
summary: "API - Feat - Getnent crear intención de pago"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-10-29 09:03"
updated: "2024-11-06 00:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-117"
---

# LIO-117: API - Feat - Getnent crear intención de pago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-10-29 09:03 |
| Actualizado | 2024-11-06 00:33 |
| Etiquetas | ninguna |
| Jira | [LIO-117](https://bluinc.atlassian.net/browse/LIO-117) |

## Relaciones

- **Padre:** [[LIO-8 - Proceso pago sencillo y competitiva a nivel financiamiento|LIO-8]] Proceso pago sencillo y competitiva a nivel financiamiento
- **has action item:** [[LIO-116 - APP - Refactor - Agregaremos al checkout la pasarela o iframe de pago para|LIO-116]] APP - Refactor - Agregaremos al checkout la pasarela o iframe de pago para GETNET

## Descripcion

```
POST {{API_URL}}/v4/intentionToPayGetnet
```

```
{
   "customer": {
      "customer_id": "123",
      "first_name": "EmaDev",
      "last_name": "DevF",
      "name": "Jou00e3o da Silva",
      "email": "ema@gmail.com",
      "document_type": "dni",
      "document_number": "37888999",
      "billing_address": {
         "street": "Av. Colon",
         "number": "1000",
         "country": "AR",
         "postal_code": "7600"
      }
   },
   "shipping": {
      "first_name": "EmaDev",
      "last_name": "DevNB",
      "address": {
         "street": "Av. Colon",
         "number": "1000",
         "postal_code": "7600",
         "country": "AR"
      }
   },
   "product": [
      {
         "title": "Monitor Benq",
         "value": 1000,
         "quantity": 1
      }
   ],
   "payment": {
      "currency": "ARS",
      "amount": 100000
   }
}
```
