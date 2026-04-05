---
jira_key: "PED-1105"
aliases: ["PED-1105"]
summary: "API - Review - Generar pedido -> Ordenes de NBE parecieran duplicarse"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2025-09-19 10:55"
updated: "2025-09-26 11:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1105"
---

# PED-1105: API - Review - Generar pedido -> Ordenes de NBE parecieran duplicarse

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2025-09-19 10:55 |
| Actualizado | 2025-09-26 11:03 |
| Etiquetas | ninguna |
| Jira | [PED-1105](https://bluinc.atlassian.net/browse/PED-1105) |

## Relaciones

- **Padre:** [[PED-4 - Pedidos|PED-4]] Pedidos
- **relates to:** [[PED-91 - APP - Feat - Generar pedido|PED-91]] APP - Feat - Generar pedido

## Descripcion

Al generar el pedido de una orden de mercado libre, pareciera duplicarse la orden.

[adjunto]
```
curl 'https://gamma.api.orders.lio.red/v1/orders?between=01-09-2025_16-09-2025&ml=true&currentPage=1' \
-H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:142.0) Gecko/20100101 Firefox/142.0' \
-H 'Accept: application/json, text/plain, /' \
-H 'Accept-Language: es-MX' \
-H 'Accept-Encoding: gzip, deflate, br, zstd' \
-H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NTgwNjQ5ODYsImF1ZCI6ImJhNDE1ODEyZjQ1ZDY3NmQyZjFhN2ZmODJhNWU0MWY3ZGI1NjFiNzIiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicm9sZURlc2NyaXB0aW9uIjoiQWRtaW5pc3RyYWRvciIsInBlZGlkb3MiOjEsInBtIjoxLCJkaXNjb3VudFNoaXBwaW5nIjoxLCJyZWJpbGwiOjEsImlzUG0iOjEsImlzR2VyZW5jaWEiOjEsImVkaXRDb3N0Rm9yU2FsZSI6bnVsbCwicGVkX2Z1bGxfYmVuZWZpdHMiOjEsImRlc2xpcXVpZGFyIjoxLCJ1bmxpbWl0ZWRSZXBvcnRzIjpudWxsLCJjcmVhdGVNYW51YWxWb3VjaGVyIjoxLCJiYW5MaXN0UHJpY2UiOiJDIn0sImlhdCI6MTc1ODA2MTM4NiwibmJmIjoxNzU4MDYxMzg2fQ.Fz46u9jmcj0FWiHs2irXw3rdmSJj13lgSQvc56mwSnc' \
-H 'Origin: https://gamma.pedidos.saftel.com' \
-H 'Connection: keep-alive' \
-H 'Referer: https://gamma.pedidos.saftel.com/' \
-H 'Sec-Fetch-Dest: empty' \
-H 'Sec-Fetch-Mode: cors' \
-H 'Sec-Fetch-Site: cross-site'
```
