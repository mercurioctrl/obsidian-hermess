---
jira_key: "PED-377"
aliases: ["PED-377"]
summary: "API - Guardar condiciones de liquidación (Sin liquidar) - Incidencias varias"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2023-12-21 19:25"
updated: "2023-12-28 16:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-377"
---

# PED-377: API - Guardar condiciones de liquidación (Sin liquidar) - Incidencias varias

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2023-12-21 19:25 |
| Actualizado | 2023-12-28 16:16 |
| Etiquetas | ninguna |
| Jira | [PED-377](https://bluinc.atlassian.net/browse/PED-377) |

## Relaciones

- **blocks:** [[PED-371]] API - Feat - Guardar condiciones de liquidación (Sin liquidar)
- **blocks:** [[PED-372]] APP - Feat - Guardar condiciones de liquidación (Sin liquidar)

## Descripcion

1. Al intentar guardar una liquidación me aparece el siguiente mensaje, sin embargo, el pago no será por medio bancario.

[adjunto]
```
curl "https://gamma.api.orders.lio.red/v1/makeSaleConditions" ^
  -H "Accept: application/json, text/plain, */*" ^
  -H "Accept-Language: es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5" ^
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MDM2MTcwMjMsImF1ZCI6ImZlMmEzYjliNWU5MWMzMzA0NjMyMWIxOWI3MDcwNmEyNjM2OTI5NjMiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjB9LCJpYXQiOjE3MDM2MTM0MjMsIm5iZiI6MTcwMzYxMzQyM30.N8XMxlp8gd5AVWlqzZBsvUUP5PyVK9sf3XS2lTgy0zU" ^
  -H "Connection: keep-alive" ^
  -H "Content-Type: application/json" ^
  -H "Origin: https://gamma.pedidos.saftel.com" ^
  -H "Referer: https://gamma.pedidos.saftel.com/" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: cross-site" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0" ^
  -H "sec-ch-ua: ^\^"Not_A Brand^\^";v=^\^"8^\^", ^\^"Chromium^\^";v=^\^"120^\^", ^\^"Microsoft Edge^\^";v=^\^"120^\^"" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H "sec-ch-ua-platform: ^\^"Windows^\^"" ^
  --data-raw "^[^{^\^"order^\^":^\^"00568900^\^",^\^"branch^\^":^\^"0002^\^",^\^"paymentMethod^\^":4,^\^"shippingMethod^\^":3031,^\^"bankId^\^":null,^\^"manualCurrencyQuote^\^":410,^\^"comment^\^":^\^"Gprueba1502^\^"^}^]" ^
  --compressed
```
