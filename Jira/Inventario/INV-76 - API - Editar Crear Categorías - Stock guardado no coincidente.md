---
jira_key: "INV-76"
aliases: ["INV-76"]
summary: "API - Editar / Crear Categorías - Stock guardado no coincidente "
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-06-11 14:06"
updated: "2024-06-11 19:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-76"
---

# INV-76: API - Editar / Crear Categorías - Stock guardado no coincidente 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-06-11 14:06 |
| Actualizado | 2024-06-11 19:40 |
| Etiquetas | ninguna |
| Jira | [INV-76](https://bluinc.atlassian.net/browse/INV-76) |

## Relaciones

- **Padre:** [[INV-23 - Aplicacion de inventario|INV-23]] Aplicacion de inventario
- **blocks:** [[INV-72 - API - Feat - Editar Crear Categorias|INV-72]] API - Feat - Editar / Crear Categorias

## Descripcion

1. Al editar el stock de una categoría estos se guardan en otra categoría.

[adjunto]
[adjunto]
```
curl "https://gamma.api.inventory.lio.red/categories" ^
  -X "PATCH" ^
  -H "Accept: application/json, text/plain, */*" ^
  -H "Accept-Language: es-419,es;q=0.9" ^
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTgxMjYwMzgsInVzdWFyaW8iOjUzfQ.jUoo21PQW9P-nBkXjw1CfQFDvBcTXuJRgqnBGE000Qo" ^
  -H "Connection: keep-alive" ^
  -H "Content-Type: application/json" ^
  -H "Origin: https://gamma.inventario.saftel.com" ^
  -H "Referer: https://gamma.inventario.saftel.com/" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: cross-site" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 OPR/110.0.0.0" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Opera^\^";v=^\^"110^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" ^
  --data-raw ^"^{^\^"id^\^":83,^\^"description^\^":^\^"Audifonozz^\^",^\^"webShow^\^":1,^\^"alphaCode^\^":^\^"83^\^",^\^"highAverage^\^":^\^"301^\^",^\^"widthAverage^\^":^\^"300^\^",^\^"lengthAverage^\^":^\^"299^\^",^\^"weightAverage^\^":^\^"298^\^",^\^"initStockMedium^\^":^\^"297^\^",^\^"initStockLarge^\^":^\^"296^\^"^}^"
```
