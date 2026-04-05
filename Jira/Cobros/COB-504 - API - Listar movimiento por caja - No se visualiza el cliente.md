---
jira_key: "COB-504"
aliases: ["COB-504"]
summary: "API - Listar movimiento por caja - No se visualiza el cliente"
status: "Finalizada"
type: "Error"
priority: "High"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-04-29 17:51"
updated: "2024-04-30 13:31"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-504"
---

# COB-504: API - Listar movimiento por caja - No se visualiza el cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | High |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-04-29 17:51 |
| Actualizado | 2024-04-30 13:31 |
| Etiquetas | ninguna |
| Jira | [COB-504](https://bluinc.atlassian.net/browse/COB-504) |

## Relaciones

- **Padre:** [[COB-15 - Cajas|COB-15]] Cajas
- **relates to:** [[COB-3 - API - Feat - Listar movimiento por caja|COB-3]] API - Feat - Listar movimiento por caja
- **blocks:** [[SNB-1844 - no se visualiza el nobre del cliente en arqueo|SNB-1844]] no se visualiza el nobre del cliente en arqueo

## Descripcion

Se reporto que no se está visualizando el nombre del cliente en el arqueo de caja. 
Dejo relacionada la incidencia y curl de la prueba.

[adjunto]
```
curl 'https://api.cashbox.lio.red/v1/box/CAJA4?currentPage=1&itemsPerPage=15' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTQ1MDkzNDAsImF1ZCI6ImNlNGQyZmE2ZGViYmExN2NiOWM4YjA2NWNmYWVlOTczMzBmY2EyOTEiLCJ1c2VyIjp7ImlkIjoiNjM2NjgiLCJjb2RlRlAiOiI1NTU1NCIsImNvYnJvIjoiMSIsImNvYnJvQWRtaW4iOiIxIiwiYWdlbnRJZCI6IjU5IiwiYm94IjpudWxsLCJtYW5hZ2VtZW50IjoiMSIsImVkaXRfY3JlZGl0IjoiMCIsImNvYnJvQWRqdXN0VG8iOiIwIn0sImlhdCI6MTcxNDQyMjk0MCwibmJmIjoxNzE0NDIyOTQwfQ.EvXKYUF3MMjIvPdKLiULGRgknFOh_gHB371RU56Hj4U' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://caja.saftel.com' \
  -H 'Referer: https://caja.saftel.com/box/CAJA4?currentPage=1&itemsPerPage=15' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0' \
  -H 'sec-ch-ua: "Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"'
```
