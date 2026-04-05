---
jira_key: "SNB-2319"
aliases: ["SNB-2319"]
summary: "Problema de formateo de fechas (?) o de carga de datos (?)"
status: "Resuelta"
type: "Support"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-09-17 10:20"
updated: "2024-09-17 11:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-2319"
---

# SNB-2319: Problema de formateo de fechas (?) o de carga de datos (?)

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-17 10:20 |
| Actualizado | 2024-09-17 11:27 |
| Etiquetas | ninguna |
| Jira | [SNB-2319](https://bluinc.atlassian.net/browse/SNB-2319) |

## Relaciones

*Sin relaciones*

## Descripcion

```
curl 'https://api.warehouse.lio.red/v1/items?currentPage=1&itemsPerPage=15&counted=false' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MjY2NTY5ODEsImF1ZCI6IjE5YWY3NDE0ZWI0YjlmYjJiMDZhMDI0ODZiMGNhODczMTkzYjUzZjQiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImFnZW50SWQiOiIxMiIsInVzdUlkZW50aWZpY2FjaW9uIjoiU2ViYSIsImV4cGVkaWNpb24iOiIxIiwiZXhwZWRpY2lvbkFkbWluIjoiMSIsIm1hbmFnZW1lbnQiOiIxIiwiZXhwX3VwbG9hZF9zZXJpYWxzIjoiMSIsImV4cF9pdGVtcyI6IjEifSwiaWF0IjoxNzI2NTc0MTgxLCJuYmYiOjE3MjY1NzQxODF9.wbVp8Zjbx1KZySFNbtK5Mtn_4E8yHld3KQrU7xB2u_0' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://expedicion.saftel.com' \
  -H 'Referer: https://expedicion.saftel.com/stock?currentPage=1&itemsPerPage=15&counted=false' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36' \
  -H 'ngrok-skip-browser-warning: true' \
  -H 'sec-ch-ua: "Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"'
```
