---
jira_key: "PED-360"
aliases: ["PED-360"]
summary: "API - Review - Error al realizar una liquidacion en produccion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-12-19 09:50"
updated: "2023-12-20 14:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-360"
---

# PED-360: API - Review - Error al realizar una liquidacion en produccion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-19 09:50 |
| Actualizado | 2023-12-20 14:53 |
| Etiquetas | ninguna |
| Jira | [PED-360](https://bluinc.atlassian.net/browse/PED-360) |

## Relaciones

- **Padre:** [[PED-123]] Feat - Liquidar pedido

## Descripcion

```
curl 'https://api.orders.lio.red/v1/closeSale' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MDMwNzM5NjAsImF1ZCI6IjJjNDY0YjE5Yjg1ZDhlOTM1N2E4Yzc2ODFmZDUxMzBhMTE4MzZkYTQiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjB9LCJpYXQiOjE3MDI5ODc1NjAsIm5iZiI6MTcwMjk4NzU2MH0.cTGoNUrQlnrMOkYgTI9Ykd7p8nnWz2r722XgdwfQOb0' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://beta.pedidos.saftel.com' \
  -H 'Referer: https://beta.pedidos.saftel.com/orders?search=00570251&currentPage=1' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '[{"shippingMethod":3999,"paymentMethod":1,"comment":"","order":"00570251","branch":"0002","currencyQuote":1030,"manualCurrencyQuote":false}]' \
  --compressed
```

Recibo

```
{
    "errors": {
        "status": 500,
        "title": "Undefined property: stdClass::$ID_CLIENTE",
        "file": "\/var\/www\/app\/app\/Services\/Liquidate\/CreateOrder.php",
        "line": 284
    }
}
```
