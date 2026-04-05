---
jira_key: "EXP-398"
aliases: ["EXP-398"]
summary: "API - Review - Pedido que aparece en la grilla de envios, cuando en realidad es un retiro"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-02-01 15:20"
updated: "2024-02-07 13:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-398"
---

# EXP-398: API - Review - Pedido que aparece en la grilla de envios, cuando en realidad es un retiro

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-01 15:20 |
| Actualizado | 2024-02-07 13:50 |
| Etiquetas | ninguna |
| Jira | [EXP-398](https://bluinc.atlassian.net/browse/EXP-398) |

## Relaciones

- **Padre:** [[EXP-6]] Despacho de envios

## Descripcion

En ámbito de  se visualiza una venta que esta liquidado como un retiro, pero por alguna razon aparece en la grilla de envios

```
curl 'https://api.warehouse.lio.red/v1/shipments/00572125?currentPage=1&itemsPerPage=300&status=2,11,10,4' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MDY4MTIxNTksImF1ZCI6IjBlY2Q0ZThhNGE0NDdlNjY2MjdjODkzYzA4NTUzYzkyY2RlYTlmYjciLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImFnZW50SWQiOiIxMiIsInVzdUlkZW50aWZpY2FjaW9uIjoiU2ViYSIsImV4cGVkaWNpb24iOiIxIiwiZXhwZWRpY2lvbkFkbWluIjoiMSIsIm1hbmFnZW1lbnQiOiIxIiwiZXhwX3VwbG9hZF9zZXJpYWxzIjoiMSJ9LCJpYXQiOjE3MDY3MjkzNTksIm5iZiI6MTcwNjcyOTM1OX0.59OmYg4SED7aspvBy_SA472oKufciGprOpJxNRZGw2M' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://expedicion.saftel.com' \
  -H 'Referer: https://expedicion.saftel.com/shipments/00572125?currentPage=1&itemsPerPage=300&status=2,11,10,4' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --compressed
```
