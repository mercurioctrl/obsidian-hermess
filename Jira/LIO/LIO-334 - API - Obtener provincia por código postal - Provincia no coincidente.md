---
jira_key: "LIO-334"
aliases: ["LIO-334"]
summary: "API - Obtener provincia por código postal - Provincia no coincidente"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2025-04-24 11:22"
updated: "2025-04-24 15:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-334"
---

# LIO-334: API - Obtener provincia por código postal - Provincia no coincidente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2025-04-24 11:22 |
| Actualizado | 2025-04-24 15:34 |
| Etiquetas | ninguna |
| Jira | [LIO-334](https://bluinc.atlassian.net/browse/LIO-334) |

## Relaciones

- **relates to:** [[LIO-186]] API - Feat - implementar recurso para obtener provincia por codigo postal

## Descripcion

Al agregar el código postal 3300 me devuelve la provincia de Corrientes, tengo entendido que es de Misiones.

```
curl 'https://gamma.api4.libreopcion.com/v4/users/postalCode' -X POST -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0' -H 'Accept: application/json, text/plain, */*' -H 'Accept-Language: es-MX' -H 'Accept-Encoding: gzip, deflate, br, zstd' -H 'Referer: https://gamma.libreopcion.com/' -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NTg0MzIzODgsImF1ZCI6ImQ2OTAxOGUzMGUxZjg2MWRlODNmNDUwNTA0NjYyOGI3ZGEwNzQyMmYiLCJ1c2VyIjp7ImlkIjoyMzkzNzgsImVtYWlsIjoiZ2F2aWxhQG5iLmNvbS5hciIsIm5vbWJyZSI6IkdwcnVlYmEgTE8iLCJwZXJmaWwiOiJ2ZW5kZWRvciIsImRvY3VtZW50byI6Ijc2NTQzMjEwIiwidGVsZWZvbm8iOiI0LTYzNi0zNDA3IiwiZGlyZWNjaW9uIjp7ImNhbGxlIjoiQy4gRXN0YWRvIFBsdXJpbmFjaW9uYWwgZGUgQm9saXZpYSIsIm51bWVybyI6IjU2MSIsInBpc28iOiIyIiwiY2FzYUFwdG8iOiJIb3RlbCBMYSBQYXoifSwiY29kaWdvUG9zdGFsIjoiMTQwNiIsImF2YXRhciI6MjAsImNpdWRhZCI6eyJpZCI6MjA4MzIsIm5vbWJyZSI6IkNBQkEiLCJwcm92aW5jaWFJZCI6MX0sInByb3ZpbmNpYSI6eyJpZCI6MSwibm9tYnJlIjoiQ0FCQSIsInBhaXNJZCI6MCwiY2l1ZGFkRGVmZWN0b0lkIjoyMDgzMn0sInBhaXMiOnsiaWQiOjAsIm5vbWJyZSI6IkFSR0VOVElOQSJ9LCJ0aWVuZGFJZCI6MCwidmVuZGVkb3JJZCI6MjA3NjU0LCJ0b2tlblYzIjoiZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SjFjM1ZoY21sdklqcDdJbWxrSWpveU16a3pOemdzSW1WdFlXbHNJam9pWjJGMmFXeGhRRzVpTG1OdmJTNWhjaUlzSW01dmJXSnlaU0k2SWtkd2NuVmxZbUVnVEU4aUxDSndaWEptYVd3aU9pSjJaVzVrWldSdmNpSXNJbVJ2WTNWdFpXNTBieUk2SWpjMk5UUXpNakV3SWl3aWRHVnNaV1p2Ym04aU9pSTBMVFl6Tmkwek5EQTNJaXdpWkdseVpXTmphVzl1SWpwN0ltTmhiR3hsSWpvaVF5NGdSWE4wWVdSdklGQnNkWEpwYm1GamFXOXVZV3dnWkdVZ1FtOXNhWFpwWVNJc0ltNTFiV1Z5YnlJNklqVTJNU0lzSW5CcGMyOGlPaUl5SWl3aVkyRnpZVUZ3ZEc4aU9pSkliM1JsYkNCTVlTQlFZWG9pZlN3aVkyOWthV2R2WDNCdmMzUmhiQ0k2SWpFME1EWWlMQ0poZG1GMFlYSWlPakl3TENKamFYVmtZV1FpT25zaWFXUWlPakl3T0RNeUxDSnViMjFpY21VaU9pSkRRVUpCSWl3aWNISnZkbWx1WTJsaFgybGtJam94TENKMGIzUmhiQ0k2TUgwc0luQnliM1pwYm1OcFlTSTZleUpwWkNJNk1Td2lhMlY1SWpveExDSnViMjFpY21VaU9pSkRRVUpCSWl3aWNHRnBjMTlwWkNJNk1Dd2lkRzkwWVd3aU9qQXNJbU5wZFdSaFpGOWtaV1psWTNSdlgybGtJam93ZlN3aWNHRnBjeUk2ZXlKcFpDSTZiblZzYkN3aWJtOXRZbkpsSWpwdWRXeHNMQ0owYjNSaGJDSTZiblZzYkgwc0luUnBaVzVrWVY5cFpDSTZNQ3dpZG1WdVpHVmtiM0pmYVdRaU9qSXdOelkxTkN3aWRHOXJaVzVXTkNJNklqWXpOVEEzUkRJNUxUY3hOVGN0TkRRNVFpMUJRME00TFRZNE9VTXdRVVF5TWpkRU1pSXNJbU52WkdsbmIxOXdiM04wWVd4ZlpHVm1ZWFZzZENJNk1USXlPWDBzSW1semN5STZJbXhwWW5KbGIzQmphVzl1TG1OdmJTSXNJbUYxWkNJNklteHBZbkpsYjNCamFXOXVMbU52YlNJc0ltbGhkQ0k2TVRjME5UUTNNak00T0N3aWJtSm1Jam94TnpRMU5EY3lNemc0ZlEuaFlHRkk4eldCT0RFMjlLcE13VVU5TVpXSTBla0FQUkY3QU1EOW13ajhlRSIsImNvZGlnb1Bvc3RhbERlZmF1bHQiOjEyMjl9LCJpYXQiOjE3NDU0NzIzODgsIm5iZiI6MTc0NTQ3MjM4OH0.h_i68WVaG_zkjlMaNJ6M9PMMyEj_O465XiY1LXeWul0' -H 'Content-Type: application/json' -H 'Origin: https://gamma.libreopcion.com' -H 'Connection: keep-alive' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-site' -H 'Priority: u=0' --data-raw '{"postalCode":3300}'
```

[adjunto]
Considerar las distintas tablas en las que se tuviera que hacer la corrección.
