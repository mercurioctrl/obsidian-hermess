---
jira_key: "EXP-479"
aliases: ["EXP-479"]
summary: "API - Listar pedidos para retiro - Error al buscar por cadena de texto"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2025-02-18 22:34"
updated: "2025-02-20 20:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-479"
---

# EXP-479: API - Listar pedidos para retiro - Error al buscar por cadena de texto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2025-02-18 22:34 |
| Actualizado | 2025-02-20 20:03 |
| Etiquetas | ninguna |
| Jira | [EXP-479](https://bluinc.atlassian.net/browse/EXP-479) |

## Relaciones

- **Padre:** [[EXP-6]] Despacho de envios
- **action item from:** [[EXP-55]] API - Feat - Listar pedidos para retiro

## Descripcion

Al momento de buscar alguna orden, me aparece el siguiente error:

[adjunto]


```
"App\\Service\\PickUp\\PickUpService::allPickUp(): Argument #2 ($stringFilter) must be of type ?array, string given, called in \/var\/www\/app\/src\/Controller\/PickUp\/PickUp.php on line 36"
```

```
curl 'https://gamma.api.warehouse.lio.red/v1/pickUp/10356028?currentPage=1&itemsPerPage=300&status=2,11,10' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0' -H 'Accept: application/json, text/plain, */*' -H 'Accept-Language: es-MX' -H 'Accept-Encoding: gzip, deflate, br, zstd' -H 'Referer: https://gamma.expedicion.saftel.com/' -H 'Origin: https://gamma.expedicion.saftel.com' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: cross-site' -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3Mzk5NjQ2MjQsImF1ZCI6IjFlZmQ5YzlmNWNhMTdhZDZkOTZmYmMwNTQ2OGUzZmE3ZmFkNmY3YmUiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImFnZW50SWQiOiIxMiIsInVzdUlkZW50aWZpY2FjaW9uIjoiU2ViYSIsImV4cGVkaWNpb24iOiIxIiwiZXhwZWRpY2lvbkFkbWluIjoiMSIsIm1hbmFnZW1lbnQiOiIxIiwiZXhwX3VwbG9hZF9zZXJpYWxzIjoiMSIsImV4cF9pdGVtcyI6IjEiLCJjb21wYW55Q29kZSI6IjQifSwiaWF0IjoxNzM5OTI4MzI0LCJuYmYiOjE3Mzk5MjgzMjR9.cX6T09OrBecrL0D_arKm8CXiv81czBzM5R0GTcBHPRM' -H 'Connection: keep-alive'
```

```
GET https://gamma.api.warehouse.lio.red/v1/pickUp/10356028?currentPage=1&itemsPerPage=300&status=2,11,10
```
