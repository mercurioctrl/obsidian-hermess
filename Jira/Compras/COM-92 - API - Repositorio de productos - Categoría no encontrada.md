---
jira_key: "COM-92"
aliases: ["COM-92"]
summary: "API - Repositorio de productos - Categoría no encontrada"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-05-15 16:43"
updated: "2024-05-16 13:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-92"
---

# COM-92: API - Repositorio de productos - Categoría no encontrada

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-05-15 16:43 |
| Actualizado | 2024-05-16 13:25 |
| Etiquetas | ninguna |
| Jira | [COM-92](https://bluinc.atlassian.net/browse/COM-92) |

## Relaciones

- **relates to:** [[COM-82]] API - Feat - Repositorio de productos

## Descripcion

Al buscar por categoría no me devuelve resultados.

[adjunto]
```
curl 'https://gamma.api.purchases.lio.red/v1/items?search=teclados' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTU4MDM2NDAsImF1ZCI6ImRjMGI2OTgxNWI1MmQ1NzVjNjZkMWFkMGViYmZlZTc1NjIyMjkzOWUiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImFnZW50SWQiOiIxMiIsInVzdUlkZW50aWZpY2FjaW9uIjoiU2ViYSIsInBlZGlkb3MiOiIxIiwicG0iOiIxIn0sImlhdCI6MTcxNTgwMDA0MCwibmJmIjoxNzE1ODAwMDQwfQ.QABItPyYpayw5q7KrxoRBSJV0NrVZd2gpfC_NyoVMTI' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://gamma.compras.saftel.com' \
  -H 'Referer: https://gamma.compras.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0' \
  -H 'sec-ch-ua: "Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"'
```
