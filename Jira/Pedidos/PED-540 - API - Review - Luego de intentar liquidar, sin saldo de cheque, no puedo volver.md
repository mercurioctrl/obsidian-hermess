---
jira_key: "PED-540"
aliases: ["PED-540"]
summary: "API - Review - Luego de intentar liquidar, sin saldo de cheque, no puedo volver a liquidar"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-02-07 15:29"
updated: "2024-02-10 20:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-540"
---

# PED-540: API - Review - Luego de intentar liquidar, sin saldo de cheque, no puedo volver a liquidar

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-07 15:29 |
| Actualizado | 2024-02-10 20:34 |
| Etiquetas | ninguna |
| Jira | [PED-540](https://bluinc.atlassian.net/browse/PED-540) |

## Relaciones

- **Padre:** [[PED-123]] Feat - Liquidar pedido
- **is blocked by:** [[PED-549]] API - Liquidar orden - Error saldo insuficiente al liquidar con cheque

## Descripcion

Cuando recibo este mensaje

[adjunto]
E intento volver a liquidar una vez agregado el saldo, me devuelve

[adjunto]
Seguro porque deben quedar creadas filas en tablas que deberian ser eliminadas si fallo.

Te dejo el curl para probar en gamma

```
curl 'https://gamma.api.orders.lio.red/v1/closeSale' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es;q=0.9' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MDczMzMxODUsImF1ZCI6ImYxZTE4ZWQwNmM1YzlkNTUyODNiN2ExNGJjNTVhNDQ5OWRiZThlYjMiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjF9LCJpYXQiOjE3MDczMjk1ODUsIm5iZiI6MTcwNzMyOTU4NX0.JIH9K0Ivd9IVdVWP6aepSxA9A51Hk3wCcpQvOznCZx8' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://gamma.pedidos.saftel.com' \
  -H 'Referer: https://gamma.pedidos.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '[{"shippingMethod":3999,"paymentMethod":6,"comment":"","order":"00568988","branch":"0002","currencyQuote":800,"bankId":null,"manualCurrencyQuote":false}]' \
  --compressed
```
