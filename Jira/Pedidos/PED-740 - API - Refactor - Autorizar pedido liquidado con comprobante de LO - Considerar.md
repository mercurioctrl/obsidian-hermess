---
jira_key: "PED-740"
aliases: ["PED-740"]
summary: "API - Refactor - Autorizar pedido liquidado con comprobante de LO - Considerar sobrante del monto transferido"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-06-05 16:38"
updated: "2024-06-06 20:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-740"
---

# PED-740: API - Refactor - Autorizar pedido liquidado con comprobante de LO - Considerar sobrante del monto transferido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-06-05 16:38 |
| Actualizado | 2024-06-06 20:35 |
| Etiquetas | ninguna |
| Jira | [PED-740](https://bluinc.atlassian.net/browse/PED-740) |

## Relaciones

- **Padre:** [[PED-3 - Ordenes de compra|PED-3]] Ordenes de compra
- **relates to:** [[PED-691 - API - Autorizar pedido (cobrar) liquidado si tiene el comprobante guardado y si|PED-691]] API - Autorizar pedido (cobrar) liquidado si tiene el comprobante guardado y si es de libre opcion

## Descripcion

Al momento de autorizar un pedido liquidado de Libre Opción con comprobante cargado, considerar cuando el monto ingresado sea mayor al monto total del pedido.

Monto final = $ 127.449,99 → u$s 144,83

Monto ingresado = $ 200.000,22 → u$s 227,27 

[adjunto]
```
curl 'https://gamma.api.orders.lio.red/v1/paymentForBank' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTc2MTgyNzEsImF1ZCI6IjRlNTM0ZGUxMWUwMDcxNjAyNzg2MWY3OWU3NzAzMzEyODlkMzkzOTkiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjEsImRpc2NvdW50U2hpcHBpbmciOjEsInJlYmlsbCI6MX0sImlhdCI6MTcxNzYxNDY3MSwibmJmIjoxNzE3NjE0NjcxfQ._fmYxQIvQHgFryUQVpipTY0Uqys6vm-Yf4oSUZILtBc' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://gamma.pedidos.saftel.com' \
  -H 'Referer: https://gamma.pedidos.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 OPR/110.0.0.0' \
  -H 'sec-ch-ua: "Chromium";v="124", "Opera";v="110", "Not-A.Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw '{"pedido":"X000200569168","transferAmount":"200000.22"}'
```

[adjunto]
