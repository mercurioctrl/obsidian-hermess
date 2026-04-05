---
jira_key: "SNB-3073"
aliases: ["SNB-3073"]
summary: "Al intentar abrir el detalle de un pedido en particular me devuelve \"server error\""
status: "Cerrada"
type: "Support"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-05-12 15:54"
updated: "2025-05-12 17:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-3073"
---

# SNB-3073: Al intentar abrir el detalle de un pedido en particular me devuelve "server error"

| Campo | Valor |
|-------|-------|
| Estado | Cerrada (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-12 15:54 |
| Actualizado | 2025-05-12 17:34 |
| Etiquetas | ninguna |
| Jira | [SNB-3073](https://bluinc.atlassian.net/browse/SNB-3073) |

## Relaciones

*Sin relaciones*

## Descripcion

```
curl 'https://api.orders.lio.red/v1/orders/0002-10406401' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDcxMDAyMjcsImF1ZCI6IjIxNTJiYzNmMjIwMzhmYTU0N2FjYWU1YjFkNTFiNTZlNjk3NWNlZGQiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicm9sZURlc2NyaXB0aW9uIjoiQWRtaW5pc3RyYWRvciIsInBlZGlkb3MiOjEsInBtIjoxLCJkaXNjb3VudFNoaXBwaW5nIjoxLCJyZWJpbGwiOjEsImlzUG0iOjEsImlzR2VyZW5jaWEiOjEsImVkaXRDb3N0Rm9yU2FsZSI6bnVsbCwicGVkX2Z1bGxfYmVuZWZpdHMiOjEsImRlc2xpcXVpZGFyIjoxLCJ1bmxpbWl0ZWRSZXBvcnRzIjpudWxsfSwiaWF0IjoxNzQ3MDEzODI3LCJuYmYiOjE3NDcwMTM4Mjd9.9Lye_Wu5pvvY4vanYk4M3sXTgT86sdRA2FYbDkzkwNY' \
  -H 'Referer: https://www.pedidos.saftel.com/' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'sec-ch-ua: "Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0'
```
