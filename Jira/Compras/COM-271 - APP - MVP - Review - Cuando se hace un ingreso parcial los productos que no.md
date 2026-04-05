---
jira_key: "COM-271"
aliases: ["COM-271"]
summary: "APP - MVP - Review - Cuando se hace un ingreso parcial los productos que no tienen cantidad o carga, no hay que agregarlos al objeto, caso contrario da error si el mismo esta completo"
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2026-01-16 09:23"
updated: "2026-01-16 14:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-271"
---

# COM-271: APP - MVP - Review - Cuando se hace un ingreso parcial los productos que no tienen cantidad o carga, no hay que agregarlos al objeto, caso contrario da error si el mismo esta completo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-16 09:23 |
| Actualizado | 2026-01-16 14:33 |
| Etiquetas | ninguna |
| Jira | [COM-271](https://bluinc.atlassian.net/browse/COM-271) |

## Relaciones

- **Padre:** [[COM-109]] Generar INGRESO o pedido (a partir de una orden de compra)

## Descripcion

```
curl 'https://gamma.api.purchases.lio.red/v1/makeProviderOrderInbound' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3Njg1Njc4OTIsImF1ZCI6IjBmYmVlNGI2NTRhNTIwMjgwMDRkZGZhNDQ5MjE5MTA2NzEzYjY1YTIiLCJ1c2VyIjp7ImlkIjoiODE0MDgiLCJjb2RlRlAiOm51bGwsImFnZW50SWQiOiI3MyIsInVzdUlkZW50aWZpY2FjaW9uIjpudWxsLCJjb21wcmFzIjoiMSIsInBtIjoiMSIsImNvbXBhbnlDb2RlIjoiMTEifSwiaWF0IjoxNzY4NTY0MjkyLCJuYmYiOjE3Njg1NjQyOTJ9.TGPIlqNLrsZJIEfrxnNovGmCIDO_b__hCv_pQJxkDF0' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://gamma.compras.saftel.com' \
  -H 'Referer: https://gamma.compras.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '{"orderNumber":12732,"trackingNumber":"252352352353","arrivalDate":"2026-01-31 08:52","providerId":"002337","providerName":"Allplus","observation":"","status":"P","voucherPurchaseId":"","countryId":15,"countryName":"URUGUAY","warehousesId":19,"buyerName":"Mansilla Florencia","buyerId":73,"currencyQuote":1310,"currencyFiscalQuote":1,"voucherNumber":"324324","dateVoucherNumber":"2026-01-16 08:52","proformaInvoice":"324324","distributeTaxes":[],"items":[{"id":125129,"title":"DISCO SSD ADATA SU650 2.5 1TB","sku":"ASU650SS-1TT-R","price":{"value":10,"iva":0,"finalPrice":10},"warranty":"Life Warranty","amount":100,"position":null,"taxPosition":null,"amountEntered":"50.000","updateAverageCost":false,"suggestedCost":null,"totalItemTax":0,"partial":50},{"id":125123,"title":"ENVIO PERSONALIZADO","sku":"LST-ENVIO","price":{"value":34,"iva":0,"finalPrice":34},"warranty":"Life Warranty","amount":1,"position":null,"taxPosition":null,"amountEntered":"1.000","updateAverageCost":false,"suggestedCost":null,"totalItemTax":0,"partial":0}]}'
```
