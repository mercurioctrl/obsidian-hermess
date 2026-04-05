---
jira_key: "INV-77"
summary: "APP - Pestaña de marcas - Nombre de parámetro no coincidente"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2024-06-11 16:02"
updated: "2024-06-11 19:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-77"
---

# INV-77: APP - Pestaña de marcas - Nombre de parámetro no coincidente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2024-06-11 16:02 |
| Actualizado | 2024-06-11 19:16 |
| Etiquetas | ninguna |
| Jira | [INV-77](https://bluinc.atlassian.net/browse/INV-77) |

## Descripción

Al crear una marca me aparece un error, platicando con Eze me comenta que puede ser debido a que se está mandando el parámetro `websiteShow` en lugar de `webSiteShow`.

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
