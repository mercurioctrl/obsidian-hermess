---
jira_key: "SNB-1523"
aliases: ["SNB-1523"]
summary: "Falla siempre que quiero obtener la informacion del usuario (el usuario existe)"
status: "Resuelta"
type: "Support"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-02-21 15:54"
updated: "2024-02-22 09:45"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-1523"
---

# SNB-1523: Falla siempre que quiero obtener la informacion del usuario (el usuario existe)

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-21 15:54 |
| Actualizado | 2024-02-22 09:45 |
| Etiquetas | ninguna |
| Jira | [SNB-1523](https://bluinc.atlassian.net/browse/SNB-1523) |

## Relaciones

*Sin relaciones*

## Descripcion

```
curl 'https://api.orders.lio.red/v1/user/46686' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MDg2MTk0OTUsImF1ZCI6IjhlM2JjNjk4NzRkMGQyYzRkMWE0NDAxMGM5Y2UyOWM2ODFjODg2ZTEiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjF9LCJpYXQiOjE3MDg1MzMwOTUsIm5iZiI6MTcwODUzMzA5NX0.hWRCF7A99bH8MsPgCM14VJfaGNF4sTKeOvI-OdE4SVc' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://pedidos.saftel.com' \
  -H 'Referer: https://pedidos.saftel.com/clients?currentPage=1&itemsPerPage=15&search=MRT_GLOBAL_TRADE_SRL' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --compressed
```
