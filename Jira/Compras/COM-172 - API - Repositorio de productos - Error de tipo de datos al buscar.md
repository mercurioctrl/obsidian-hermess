---
jira_key: "COM-172"
aliases: ["COM-172"]
summary: "API - Repositorio de productos - Error de tipo de datos al buscar"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2025-02-19 00:44"
updated: "2025-02-20 20:06"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-172"
---

# COM-172: API - Repositorio de productos - Error de tipo de datos al buscar

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2025-02-19 00:44 |
| Actualizado | 2025-02-20 20:06 |
| Etiquetas | ninguna |
| Jira | [COM-172](https://bluinc.atlassian.net/browse/COM-172) |

## Relaciones

- **Padre:** [[COM-1 - Bases y repositorios|COM-1]] Bases y repositorios
- **action item from:** [[COM-82 - API - Feat - Repositorio de productos|COM-82]] API - Feat - Repositorio de productos

## Descripcion

Al intentar buscar un articulo me aparece el siguiente error:

```
trim(): Argument #1 ($string) must be of type string, null given
```

```
curl 'https://gamma.api.purchases.lio.red/v1/items?search=gabinete' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0' -H 'Accept: application/json, text/plain, */*' -H 'Accept-Language: es-MX' -H 'Accept-Encoding: gzip, deflate, br, zstd' -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3Mzk5Mzk2NDEsImF1ZCI6IjNlYTRlYTI0ZThhMTFlN2ZjMDI1MjVjYWQzMWQwNzljNjhjNjcxMzkiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImFnZW50SWQiOiIxMiIsInVzdUlkZW50aWZpY2FjaW9uIjoiU2ViYSIsImNvbXByYXMiOiIxIiwicG0iOiIxIiwiY29tcGFueUNvZGUiOiI0In0sImlhdCI6MTczOTkzNjA0MSwibmJmIjoxNzM5OTM2MDQxfQ.1N5ppeGqFMyAIO2K5gDgC7eSwSvgWS4-riqdOsZnSq4' -H 'Origin: https://gamma.compras.saftel.com' -H 'Connection: keep-alive' -H 'Referer: https://gamma.compras.saftel.com/' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: cross-site'
```

```
GET {{API_URL}}/v1/items?search={articulo descripcion}
```

[adjunto]
