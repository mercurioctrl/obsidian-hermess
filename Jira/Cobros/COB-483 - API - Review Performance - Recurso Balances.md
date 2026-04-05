---
jira_key: "COB-483"
aliases: ["COB-483"]
summary: "API - Review Performance - Recurso \"Balances\""
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-02-16 12:30"
updated: "2024-02-16 13:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-483"
---

# COB-483: API - Review Performance - Recurso "Balances"

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-16 12:30 |
| Actualizado | 2024-02-16 13:03 |
| Etiquetas | ninguna |
| Jira | [COB-483](https://bluinc.atlassian.net/browse/COB-483) |

## Relaciones

- **Padre:** [[COB-5 - API - Feat - Obtener cuenta corriente de un cliente|COB-5]] API - Feat - Obtener cuenta corriente de un cliente

## Descripcion

Por alguna razón en producción este recurso demora demasiado y traba los demás recursos.

Caso de prueba

```
curl 'https://api2.cashbox.lio.red/v1/balances/25789' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MDgxODE4NDcsImF1ZCI6IjJmZjdkMzYwN2EzNWNhMWU1MGRjZjY2YWQ1ZTY0MWFmYmNkMDhiYjAiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImNvYnJvIjoiMSIsImNvYnJvQWRtaW4iOiIxIiwiYWdlbnRJZCI6IjEyIiwiYm94IjoiU2ViYSIsIm1hbmFnZW1lbnQiOiIxIiwiZWRpdF9jcmVkaXQiOiIxIiwiY29icm9BZGp1c3RUbyI6IjEifSwiaWF0IjoxNzA4MDk1NDQ3LCJuYmYiOjE3MDgwOTU0NDd9.RNDmQyj78bu-B0COtEdTLw0dPqQ0iH87vuOSc-yAkGs' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://caja.saftel.com' \
  -H 'Referer: https://caja.saftel.com/clients/Miguel_Tamara?currentPage=1&itemsPerPage=15' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --compressed
```
