---
jira_key: "COM-251"
aliases: ["COM-251"]
summary: "API - MVP - Review - Generar ingreso -> Diferencia de IVA al finalizar la orden"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2025-11-17 22:19"
updated: "2025-12-05 05:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-251"
---

# COM-251: API - MVP - Review - Generar ingreso -> Diferencia de IVA al finalizar la orden

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2025-11-17 22:19 |
| Actualizado | 2025-12-05 05:31 |
| Etiquetas | ninguna |
| Jira | [COM-251](https://bluinc.atlassian.net/browse/COM-251) |

## Relaciones

- **Padre:** [[COM-109]] Generar INGRESO o pedido (a partir de una orden de compra)
- **relates to:** [[COM-216]] API - MVP - Refactor  - Cada que se haga un ingreso revisar para cambiar el estado de la orden en caso que sean iguales la cantidad ingresadas que las totales para todos los items

## Descripcion

Después de generar el ingreso de una orden, en su totalidad, se visualiza diferente el IVA seleccionado.

Adicional a esto, una pregunta, ¿es correcto que se visualice cada uno de los ingresos?

[adjunto]
```
curl 'https://gamma.api.purchases.lio.red/v1/makeProviderOrderInbound' \
  -X POST \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-MX' \
  -H 'Accept-Encoding: gzip, deflate, br, zstd' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NjM0MzEwMjgsImF1ZCI6IjczYzQzYjc2Yzc5NDNmNWRjMmEyMTdjMjIyOWMzOWI3YjUwMzBkNjciLCJ1c2VyIjp7ImlkIjoiODE0MDciLCJjb2RlRlAiOiI5MjE1NyIsImFnZW50SWQiOiI3MiIsInVzdUlkZW50aWZpY2FjaW9uIjpudWxsLCJjb21wcmFzIjoiMSIsInBtIjoiMSIsImNvbXBhbnlDb2RlIjoiMTEifSwiaWF0IjoxNzYzNDI3NDI4LCJuYmYiOjE3NjM0Mjc0Mjh9.SO-NYG5x4ZaCAH3GoW6fz69rKS3CzdZcGPGHY8u--UA' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://gamma.compras.saftel.com' \
  -H 'Connection: keep-alive' \
  -H 'Referer: https://gamma.compras.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  --data-raw '{"orderNumber":12707,"trackingNumber":"345","arrivalDate":"2025-11-06 22:05","providerId":"001812","providerName":"MC LASER SERVICIOS SRL","observation":"","status":"P","voucherPurchaseId":"","countryId":7,"countryName":"Argentina","warehousesId":3,"buyerName":"Obari Anabel","buyerId":72,"currencyQuote":1310,"currencyFiscalQuote":1,"voucherNumber":"222","dateVoucherNumber":"2025-11-12 22:06","proformaInvoice":"333","distributeTaxes":[],"items":[{"id":124263,"title":"KEYBOARD + MOUSE MSI","sku":"FORGEGK300C-FORGE GK300 COMBO BLUE US","price":{"value":0,"iva":0,"finalPrice":0},"lastCostForSale":null,"warranty":"12 meses","amount":10,"position":"mousenueva","taxPosition":{"iibb":0,"iva":15,"ivaAd":1212,"ganancias":10,"te":0,"aec":11,"dii":0,"die":0},"amountEntered":"4.000","totalItemTax":0,"partial":6,"updateAverageCost":false}]}'
```
