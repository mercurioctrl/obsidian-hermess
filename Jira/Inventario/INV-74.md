---
jira_key: "INV-74"
summary: "API - Refactor - Editar / Crear marcas - Guardar datos adicionales"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-06-07 20:08"
updated: "2024-06-11 19:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-74"
---

# INV-74: API - Refactor - Editar / Crear marcas - Guardar datos adicionales

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-06-07 20:08 |
| Actualizado | 2024-06-11 19:21 |
| Etiquetas | ninguna |
| Jira | [INV-74](https://bluinc.atlassian.net/browse/INV-74) |

## Descripción

1. Al crear una marca vamos a guardar los siguientes parámetros:

- `imagen`


- `hide`


- `websiteShow`



[attachment]
[attachment]
```
curl 'https://gamma.api.inventory.lio.red/brands' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTc4MDI5MzEsInVzdWFyaW8iOjUzfQ.ODVAsnOJEJv4xLoZvS3IEHbU8u-Yu1TIPZzSjVt5YYk' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://gamma.inventario.saftel.com' \
  -H 'Referer: https://gamma.inventario.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 OPR/110.0.0.0' \
  -H 'sec-ch-ua: "Chromium";v="124", "Opera";v="110", "Not-A.Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw '{"description":"Gprueba0803","imagen":"http://static.nb.com.ar/img/731da603219cb848041e35bb9b43806f.png","hide":true,"websiteShow":false}'
```



Aquí van algunas sugerencias

- Actualizar peticiones en Postman


- Quitar los espacios adicionales en la descripción al obtener el listado de marcas



---

Actualización 11/06/24

2. Al intentar crear una marca me regresa un código de estado http 200 y no me especifica el error.

[attachment]
```
curl "https://gamma.api.inventory.lio.red/brands" ^
  -H "Accept: application/json, text/plain, */*" ^
  -H "Accept-Language: es-419,es;q=0.9" ^
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTgxMzI0NDEsInVzdWFyaW8iOjUzfQ.0fHxC5ZyeVbv9OZLa8whKeMkrp6yP4J_N6BRtgTCKLk" ^
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
  --data-raw ^"^{^\^"description^\^":^\^"Gprueba300^\^",^\^"imagen^\^":^\^"http://static.nb.com.ar/img/ea96799d896309ad8d24aa181428bf35.jpg^\^",^\^"hide^\^":true,^\^"websiteShow^\^":true^}^"
```
