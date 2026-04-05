---
jira_key: "COB-605"
aliases: ["COB-605"]
summary: "API - Review - Se debe hacer la descarga del reporte de balances sensible a los mismos filtros que se aplica al repositorio -> Deuda cheque no coincidente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2026-01-20 11:43"
updated: "2026-01-23 16:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-605"
---

# COB-605: API - Review - Se debe hacer la descarga del reporte de balances sensible a los mismos filtros que se aplica al repositorio -> Deuda cheque no coincidente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2026-01-20 11:43 |
| Actualizado | 2026-01-23 16:01 |
| Etiquetas | ninguna |
| Jira | [COB-605](https://bluinc.atlassian.net/browse/COB-605) |

## Relaciones

- **Padre:** [[COB-573 - Clientes|COB-573]] Clientes
- **clones:** [[COB-602 - API - Refactor - Se debe hacer la descarga del reporte de balances sensible a|COB-602]] API - Refactor - Se debe hacer la descarga del reporte de balances sensible a los mismos filtros que se aplica al repositorio

## Descripcion

Al descargar el reporte de clientes, la deuda en cheque para este caso parece no coincidente.

```
GET {API_URL}/v1/clients/xlsx
```

[adjunto]
```
curl 'https://gamma.api.cashbox.lio.red/v1/clients/xlsx?desactive=false&sellerId=8&balanceState=debt&balanceStateOrder=asc' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:147.0) Gecko/20100101 Firefox/147.0' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-MX' \
  -H 'Accept-Encoding: gzip, deflate, br, zstd' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3Njg5MjI0NTAsImF1ZCI6IjQzYTIxNmJlODhmYzE5ZWU0MTZhNmY1NDJmN2I2YmZkYzYzMTEyMjQiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImNvYnJvIjoiMSIsImNvYnJvQWRtaW4iOiIxIiwiYWdlbnRJZCI6IjEyIiwiYm94IjoiU2ViYSIsIm1hbmFnZW1lbnQiOiIxIiwiZWRpdF9jcmVkaXQiOiIxIiwiY29icm9BZGp1c3RUbyI6IjEifSwiaWF0IjoxNzY4OTE4ODUwLCJuYmYiOjE3Njg5MTg4NTB9.hOytUJ4flU4BhCMcU6iuT9WuG8OlkagL8tXr6JEzUCE' \
  -H 'Origin: https://gamma.caja.saftel.com' \
  -H 'Connection: keep-alive' \
  -H 'Referer: https://gamma.caja.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site'
```
