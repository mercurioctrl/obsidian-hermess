---
jira_key: "SNB-2275"
aliases: ["SNB-2275"]
summary: "EXP - No deja despachar por serial faltantos cuando hubo devoluciones"
status: "Resuelta"
type: "Support"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-08-30 12:30"
updated: "2024-08-30 15:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-2275"
---

# SNB-2275: EXP - No deja despachar por serial faltantos cuando hubo devoluciones

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-30 12:30 |
| Actualizado | 2024-08-30 15:02 |
| Etiquetas | ninguna |
| Jira | [SNB-2275](https://bluinc.atlassian.net/browse/SNB-2275) |

## Relaciones

*Sin relaciones*

## Descripcion

Creo que en algun momento esto se andaba correctamente.

Parece ser que al intentar marcar “entregar” verifica y toma que le hace un serial (el que en realidad ya se devolvio).

Dejo el curl que da el error

```
curl 'https://api.warehouse.lio.red/v1/orders/X000200591434/hand' \
  -X 'PATCH' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MjUxMDQzMzQsImF1ZCI6ImNhMmFkM2JjMzYzYWIxYTBkNTQ4YzI2M2Y2MmM3MmIxZjQ0ZjUxZDEiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImFnZW50SWQiOiIxMiIsInVzdUlkZW50aWZpY2FjaW9uIjoiU2ViYSIsImV4cGVkaWNpb24iOiIxIiwiZXhwZWRpY2lvbkFkbWluIjoiMSIsIm1hbmFnZW1lbnQiOiIxIiwiZXhwX3VwbG9hZF9zZXJpYWxzIjoiMSJ9LCJpYXQiOjE3MjUwMjE1MzQsIm5iZiI6MTcyNTAyMTUzNH0.kngUOUHB8b0gFjg5-3olRTzXVJb3fXg1NcxbbKwwmyE' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://expedicion.saftel.com' \
  -H 'Referer: https://expedicion.saftel.com/shipments/591434?currentPage=1&itemsPerPage=300&status=2,11,10,4' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36' \
  -H 'ngrok-skip-browser-warning: true' \
  -H 'sec-ch-ua: "Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '{"authorizeUser":"FE5BA42E32632445","secretKey":false}'
```

[adjunto]
