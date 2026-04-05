---
jira_key: "SNB-1805"
aliases: ["SNB-1805"]
summary: "Al intentar cambiar un cliente, me devuelve un error de NIVA"
status: "Resuelta"
type: "Support"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-04-19 13:46"
updated: "2024-04-19 14:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-1805"
---

# SNB-1805: Al intentar cambiar un cliente, me devuelve un error de NIVA

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-19 13:46 |
| Actualizado | 2024-04-19 14:01 |
| Etiquetas | ninguna |
| Jira | [SNB-1805](https://bluinc.atlassian.net/browse/SNB-1805) |

## Relaciones

*Sin relaciones*

## Descripcion

Adjunto ejemplo del CURL en PRODUCCION

```
curl 'https://api.orders.lio.red/v1/orders/changeClient' \
  -X 'PATCH' \
  -H 'Accept: application/json, text/plain, /' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTM2MjQ1MTIsImF1ZCI6ImQ3NDUwNDVmNmFiZDFhMjljNWQ0YWQ1ZWRkNzk5NzgzMDVkOWM5NjEiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjEsImRpc2NvdW50U2hpcHBpbmciOjEsInJlYmlsbCI6MX0sImlhdCI6MTcxMzUzODExMiwibmJmIjoxNzEzNTM4MTEyfQ.3V52rmJXE7Z0BxsoIHmHqlR0Aat3i9nR7LjUeKxQ8N4' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://www.pedidos.saftel.com' \
  -H 'Referer: https://www.pedidos.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '{"newClientId":9456,"order":"10344834","branch":"0002"}'
```
