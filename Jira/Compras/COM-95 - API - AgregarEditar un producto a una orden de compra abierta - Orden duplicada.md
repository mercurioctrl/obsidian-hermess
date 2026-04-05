---
jira_key: "COM-95"
aliases: ["COM-95"]
summary: "API - Agregar/Editar un producto a una orden de compra abierta - Orden duplicada"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-05-15 17:03"
updated: "2024-05-22 04:54"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-95"
---

# COM-95: API - Agregar/Editar un producto a una orden de compra abierta - Orden duplicada

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-05-15 17:03 |
| Actualizado | 2024-05-22 04:54 |
| Etiquetas | ninguna |
| Jira | [COM-95](https://bluinc.atlassian.net/browse/COM-95) |

## Relaciones

- **Padre:** [[COM-8 - Ordenes de compra|COM-8]] Ordenes de compra
- **blocks:** [[COM-90 - API - Refactor - PATCH provider Order add item|COM-90]] API - Refactor  - PATCH provider Order add item

## Descripcion

Note que después de agregar un articulo a la orden, ésta se duplicaba.

[adjunto]
[adjunto]
```
curl 'https://gamma.api.purchases.lio.red/v1/providerOrder/11080' \
  -X 'PATCH' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTU4MDM2NDAsImF1ZCI6ImRjMGI2OTgxNWI1MmQ1NzVjNjZkMWFkMGViYmZlZTc1NjIyMjkzOWUiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImFnZW50SWQiOiIxMiIsInVzdUlkZW50aWZpY2FjaW9uIjoiU2ViYSIsInBlZGlkb3MiOiIxIiwicG0iOiIxIn0sImlhdCI6MTcxNTgwMDA0MCwibmJmIjoxNzE1ODAwMDQwfQ.QABItPyYpayw5q7KrxoRBSJV0NrVZd2gpfC_NyoVMTI' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://gamma.compras.saftel.com' \
  -H 'Referer: https://gamma.compras.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0' \
  -H 'sec-ch-ua: "Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw '{"id":103831,"price":{"value":0,"iva":0},"amount":1,"position":null}'
```
