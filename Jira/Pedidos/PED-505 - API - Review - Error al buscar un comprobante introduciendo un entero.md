---
jira_key: "PED-505"
aliases: ["PED-505"]
summary: "API - Review - Error al buscar un comprobante introduciendo un entero"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-01-19 09:57"
updated: "2024-01-26 03:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-505"
---

# PED-505: API - Review - Error al buscar un comprobante introduciendo un entero

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-19 09:57 |
| Actualizado | 2024-01-26 03:21 |
| Etiquetas | ninguna |
| Jira | [PED-505](https://bluinc.atlassian.net/browse/PED-505) |

## Relaciones

- **Padre:** [[PED-98 - Feat - Listar comprobantes|PED-98]] Feat - Listar comprobantes

## Descripcion

```
curl 'https://gamma.api.orders.lio.red/v1/vouchers?currentPage=1&itemsPerPage=15&search=312323' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MDU2NzI1OTksImF1ZCI6IjlkMTcwM2FmNzk2NDBhMmQ5ZDNjMGY2ZDBhZTA0ZmJhODI4YzBiM2YiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjF9LCJpYXQiOjE3MDU2Njg5OTksIm5iZiI6MTcwNTY2ODk5OX0.uFFT0-i8sCvwnr8KAfysGdUo9bxg3ZpHQuCN6y7Wpac' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://gamma.pedidos.saftel.com' \
  -H 'Referer: https://gamma.pedidos.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --compressed
```
