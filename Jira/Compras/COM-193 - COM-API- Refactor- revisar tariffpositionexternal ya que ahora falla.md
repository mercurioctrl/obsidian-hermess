---
jira_key: "COM-193"
aliases: ["COM-193"]
summary: "COM-API- Refactor- revisar  tariffpositionexternal ya que ahora falla"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Marbe Moreno"
created: "2025-06-13 10:49"
updated: "2025-06-13 17:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-193"
---

# COM-193: COM-API- Refactor- revisar  tariffpositionexternal ya que ahora falla

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Marbe Moreno |
| Creado | 2025-06-13 10:49 |
| Actualizado | 2025-06-13 17:01 |
| Etiquetas | ninguna |
| Jira | [COM-193](https://bluinc.atlassian.net/browse/COM-193) |

## Relaciones

- **Padre:** [[COM-8]] Ordenes de compra
- **action item from:** [[COM-192]] APP - MVP - Refactor - Permitir agregar posición arancelaria de manera mas sencilla 

## Descripcion

Curl para probar error

```
curl 'https://gamma.api.purchases.lio.red/v1/tariffPositionExternal?search=3929.40.00.000N' \   -H 'Accept: application/json, text/plain, */*' \   -H 'Accept-Language: en-US,en;q=0.9,es-ES;q=0.8,es;q=0.7' \   -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDk3NjQ1ODksImF1ZCI6IjY2YzQzMGRhOWFiODY2NDYzMTI1YmVmZjIyOGI2MmY5NDExMGZmN2EiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImFnZW50SWQiOiIxMiIsInVzdUlkZW50aWZpY2FjaW9uIjoiU2ViYSIsImNvbXByYXMiOiIxIiwicG0iOiIxIiwiY29tcGFueUNvZGUiOiI0In0sImlhdCI6MTc0OTc2MDk4OSwibmJmIjoxNzQ5NzYwOTg5fQ.8bmocf07uQBgJ2TbYo0YswlqxyBAtkyseR86nMJ5YoY' \   -H 'Cache-Control: no-cache' \   -H 'Connection: keep-alive' \   -H 'Origin: http://localhost:3003' \   -H 'Pragma: no-cache' \   -H 'Referer: http://localhost:3003/' \   -H 'Sec-Fetch-Dest: empty' \   -H 'Sec-Fetch-Mode: cors' \   -H 'Sec-Fetch-Site: cross-site' \   -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36' \   -H 'sec-ch-ua: "Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"' \   -H 'sec-ch-ua-mobile: ?0' \   -H 'sec-ch-ua-platform: "Linux"'
```

Segun lo hablado:
La busqueda la hace de forma externa, y ahora esa manera de buscar pide que haga login y genere un token es necesario hacer un refactor y ver si se puede obtener las tarifas de impuestos
