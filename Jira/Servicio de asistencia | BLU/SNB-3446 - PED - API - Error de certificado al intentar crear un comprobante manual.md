---
jira_key: "SNB-3446"
aliases: ["SNB-3446"]
summary: "PED - API - Error de certificado al intentar crear un comprobante manual"
status: "Resuelta"
type: "Support"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Guillermo Avila"
created: "2025-10-02 10:32"
updated: "2025-10-16 11:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-3446"
---

# SNB-3446: PED - API - Error de certificado al intentar crear un comprobante manual

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Guillermo Avila |
| Creado | 2025-10-02 10:32 |
| Actualizado | 2025-10-16 11:31 |
| Etiquetas | ninguna |
| Jira | [SNB-3446](https://bluinc.atlassian.net/browse/SNB-3446) |

## Relaciones

- **blocks:** [[PED-1104 - API - Refactor - Uso del parámetro cotización al generar comprobantes manuales|PED-1104]] API - Refactor - Uso del parámetro cotización al generar comprobantes manuales

## Descripcion

En Pedidos, al intentar crear un voucher manual aparece el siguiente error:

[adjunto]


```
curl 'https://gamma.api.orders.lio.red/v1/makeVoucherManual' \
  -X POST \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:143.0) Gecko/20100101 Firefox/143.0' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-MX' \
  -H 'Accept-Encoding: gzip, deflate, br, zstd' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NTk0MTUyNjUsImF1ZCI6IjYyYzVjYzAxNWZkMGNmZTU4ZjQzNjdiNmU2Y2Y1ZmQ3OThjM2JiZTYiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicm9sZURlc2NyaXB0aW9uIjoiQWRtaW5pc3RyYWRvciIsInBlZGlkb3MiOjEsInBtIjoxLCJkaXNjb3VudFNoaXBwaW5nIjoxLCJyZWJpbGwiOjEsImlzUG0iOjEsImlzR2VyZW5jaWEiOjEsImVkaXRDb3N0Rm9yU2FsZSI6MSwicGVkX2Z1bGxfYmVuZWZpdHMiOjEsImRlc2xpcXVpZGFyIjoxLCJ1bmxpbWl0ZWRSZXBvcnRzIjpudWxsLCJjcmVhdGVNYW51YWxWb3VjaGVyIjoxLCJiYW5MaXN0UHJpY2UiOiJDIn0sImlhdCI6MTc1OTQxMTY2NSwibmJmIjoxNzU5NDExNjY1fQ.STRJ2mhzxTqz7OARzxvGMl-amL1bchjWUUXzixpLh18' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://gamma.pedidos.saftel.com' \
  -H 'Connection: keep-alive' \
  -H 'Referer: https://gamma.pedidos.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  --data-raw '{"clientId":86322,"voucherType":"FACTURA","cotizacion":"100","trade":[{"internalId":5425,"units":1,"price":"300","ivaTax":10.5,"internalTax":200,"description":"NINGUN PRODUCTO"}],"impactCurrentAccount":true}'
```
