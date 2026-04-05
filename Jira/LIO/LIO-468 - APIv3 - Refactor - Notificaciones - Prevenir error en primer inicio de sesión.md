---
jira_key: "LIO-468"
aliases: ["LIO-468"]
summary: "APIv3 - Refactor - Notificaciones -> Prevenir error en primer inicio de sesión"
status: "Backlog"
type: "Subtarea"
priority: "Low"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2025-10-30 14:21"
updated: "2025-10-30 14:55"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-468"
---

# LIO-468: APIv3 - Refactor - Notificaciones -> Prevenir error en primer inicio de sesión

| Campo | Valor |
|-------|-------|
| Estado | Backlog (Por hacer) |
| Tipo | Subtarea |
| Prioridad | Low |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2025-10-30 14:21 |
| Actualizado | 2025-10-30 14:55 |
| Etiquetas | ninguna |
| Jira | [LIO-468](https://bluinc.atlassian.net/browse/LIO-468) |

## Relaciones

- **Padre:** [[LIO-313 - Notificaciones|LIO-313]] Notificaciones

## Descripcion

Realizaremos un refactor en el recurso para evitar que, al iniciar sesión por primera vez (inmediatamente después de crear la cuenta), se genere el error adjunto.

Cabe mencionar que esto ocurre al crear una cuenta mediante Google y únicamente durante el primer inicio de sesión.

En caso de no poder generar el token en ese primer intento, no debe producirse un fallo.



```
{{API_URL}}/notifications/tokens/push
```

[adjunto]
```
curl.exe ^"https://omega-api.libreopcion.com.ar/notifications/tokens/push^" ^
-X POST ^
-H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0^" ^
-H ^"Accept: application/json, text/plain, /^" ^
-H ^"Accept-Language: es-MX^" ^
-H ^"Accept-Encoding: gzip, deflate, br, zstd^" ^
-H ^"Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjp7ImlkIjozMTQ0MTgsImVtYWlsIjoiZy5hdmlsYTA4ODBAZ21haWwuY29tIiwibm9tYnJlIjoiR3VpbGxlcm1vIFx1MDBjMXZpbGEiLCJwZXJmaWwiOiJjb21wcmFkb3IiLCJkb2N1bWVudG8iOiIiLCJ0ZWxlZm9ubyI6IiIsImRpcmVjY2lvbiI6eyJjYWxsZSI6IiIsIm51bWVybyI6IiIsInBpc28iOiIiLCJjYXNhQXB0byI6IiJ9LCJjb2RpZ29fcG9zdGFsIjoiIiwiYXZhdGFyIjowLCJjaXVkYWQiOnsiaWQiOm51bGwsIm5vbWJyZSI6bnVsbCwicHJvdmluY2lhX2lkIjpudWxsLCJ0b3RhbCI6bnVsbH0sInByb3ZpbmNpYSI6eyJpZCI6MCwia2V5IjowLCJub21icmUiOiIiLCJwYWlzX2lkIjo3LCJ0b3RhbCI6MCwiY2l1ZGFkX2RlZmVjdG9faWQiOjB9LCJwYWlzIjp7ImlkIjo3LCJub21icmUiOiIiLCJ0b3RhbCI6MH0sInRpZW5kYV9pZCI6MCwidmVuZGVkb3JfaWQiOjAsInRva2VuVjQiOiJEMzY1MTg3Ni1CQjA4LTQ4RTUtODdERC1GRTAzMEM0N0FBRkMiLCJjb2RpZ29fcG9zdGFsX2RlZmF1bHQiOm51bGwsImFjdGl2ZVdhbGxldCI6ZmFsc2V9LCJpc3MiOiJsaWJyZW9wY2lvbi5jb20iLCJhdWQiOiJsaWJyZW9wY2lvbi5jb20iLCJpYXQiOjE3NjE4MzQ3MDgsIm5iZiI6MTc2MTgzNDcwOH0.jEAC2s_7chNqFy_QsW3ePcdkMGsI021xIFQvWf49Am4^" ^
-H ^"Content-Type: application/json^" ^
-H ^"Origin: https://libreopcion.com.ar^" ^
-H ^"Connection: keep-alive^" ^
-H ^"Referer: https://libreopcion.com.ar/^" ^
-H ^"Sec-Fetch-Dest: empty^" ^
-H ^"Sec-Fetch-Mode: cors^" ^
-H ^"Sec-Fetch-Site: same-site^" ^
--data-raw ^"^{^\^"token^\^":^\^"eSo3oRmJ1n7cidEpb03-SX:APA91bGaviG8uekNt6wgWcym62j57B2Jwf794Cb_0Fc_nfMxV-mr5SZq65DyVGe3zzsqD0RADn2ERC8uLqtGaPYYeP3ZX2eDehbRVFeWZDdFyrK-2N5dTb8^\^"^}^"
```
