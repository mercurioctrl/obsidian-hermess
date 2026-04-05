---
jira_key: "PED-1321"
aliases: ["PED-1321"]
summary: "API - Feat - Ver detalle pedido -> Agregar nro proforma (ver/editar)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Marbe Moreno"
created: "2026-03-03 11:58"
updated: "2026-03-05 07:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1321"
---

# PED-1321: API - Feat - Ver detalle pedido -> Agregar nro proforma (ver/editar)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Marbe Moreno |
| Creado | 2026-03-03 11:58 |
| Actualizado | 2026-03-05 07:40 |
| Etiquetas | ninguna |
| Jira | [PED-1321](https://bluinc.atlassian.net/browse/PED-1321) |

## Relaciones

- **Padre:** [[PED-8 - Listar ordenes de compra|PED-8]] Listar ordenes de compra
- **blocks:** [[LOCAPP-84 - API - MVP - Servicio de facturación - Feat - implementar packing List|LOCAPP-84]] API - MVP - Servicio de facturación - Feat - implementar packing List
- **has action item:** [[PED-1320 - APP - Feat - Ver detalle pedido - Agregar nro proforma (vereditar)|PED-1320]] APP - Feat - Ver detalle pedido -> Agregar nro proforma (ver/editar)
- **has action item:** [[PED-1325 - API - Refactor - Nro proforma de una orden|PED-1325]] API - Refactor - Nro proforma de una orden

## Descripcion

Debe poder verse:

GET [https://gamma.api.orders.lio.red/v1/orders/0000-10337677](https://gamma.api.orders.lio.red/v1/orders/0000-10337677)

```
{
    "date": "2026-03-02 12:13:00",
    "makeSaleDate": null,
    "orderNumber": "10337677",
    "branchNumber": "0000",
    "incotermId": null,
    "incotermCode": null,
    "albnumNumber": null,
    "realAlbumNumber": null,
    "clientEmail": null,
    "clientName": "VISAO VIP SRL",
    "clientId": 92434,
    "userId": 0,
    "observation": null,
    "status": "P",
    "invoice": null,
    "token": null,
    "voucherId": null,
    "seller": "Anabel",
    "sellerId": "72",
    "sellerCreator": "Florencia Mansilla",
    "sellerIdCreator": "73",
    "items": [],
    "currencyQuote": 1325,
    "shippingMethodId": null,
    "shippingMethodName": null,
    "tracking": null,
    "packageGrouper": null,
    "localityId": null,
    "localityName": null,
    "provinceId": null,
    "provinceName": null,
    "alphaCode": null,
    "phoneNumber": null,
    "postalCode": null,
    "customerAddressId": null,
    "address": null,
    "niva": 5,
    "percepcion": 0,
    "percepcionArba": 0,
    "whoBuild": null,
    "whoAuthorized": null,
    "addressFinal": null,
    "postalCodeFinal": null,
    "provinceNameFinal": null,
    "localityNameFinal": null,
    "statusId": null,
    "statusDescription": "Pendiente",
    "cancelled": 0,
    "delivered": null,
    "kits": [],
    "paymentTerms": 12,
    "forwarderId": 6,
    "forwarderName": "dhl ejemplo",
    "proformaInvoice":"[[ABC-123456]]" -> nuevo campo
}
```





Debe poder editarse

```
curl 'https://gamma.api.orders.lio.red/v1/orders/0000-10337677' \
  -X 'PATCH' \
  -H 'Accept: application/json, text/plain, /' \
  -H 'Accept-Language: en-US,en;q=0.9,es-ES;q=0.8,es;q=0.7' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NzI1NTM1MzMsImF1ZCI6ImIyYmRjOGJhZDliYzhmN2QyMDdjZDU3MTJlNTMzYTIxODUxNTRiNjUiLCJ1c2VyIjp7ImlkIjo4MTQwOCwiY29kZUZQIjpudWxsLCJhZ2VudElkIjo3MywidXN1SWRlbnRpZmljYWNpb24iOm51bGwsInJvbGVEZXNjcmlwdGlvbiI6IlByb2R1Y3QgTWFuYWdlciIsInBlZGlkb3MiOjEsInBtIjoxLCJkaXNjb3VudFNoaXBwaW5nIjoxLCJyZWJpbGwiOjAsImlzUG0iOjEsImlzR2VyZW5jaWEiOjAsImVkaXRDb3N0Rm9yU2FsZSI6MCwicGVkX2Z1bGxfYmVuZWZpdHMiOjEsImRlc2xpcXVpZGFyIjoxLCJ1bmxpbWl0ZWRSZXBvcnRzIjpudWxsLCJjcmVhdGVNYW51YWxWb3VjaGVyIjowLCJiYW5MaXN0UHJpY2UiOm51bGwsInVubG9ja2VkU2VsbGVyRmlsdGVyIjoxLCJ1c2VTdG9ja0luY29taW5nIjoxLCJ1bmxvY2tlZENvbXBhbnlGaWx0ZXIiOjEsIm1hcmtldGluZ0Z1bmRzIjowLCJjb21wYW55Q29kZSI6MTF9LCJpYXQiOjE3NzI1NDk5MzMsIm5iZiI6MTc3MjU0OTkzM30.P6rylYtfIaXs0wvBILz9fLXgxXHsL-eu5AQRb4LQ8cQ' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://gamma.pedidos.saftel.com' \
  -H 'Pragma: no-cache' \
  -H 'Referer: https://gamma.pedidos.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '{"proformaInvoice":”abc-123”}'
```
