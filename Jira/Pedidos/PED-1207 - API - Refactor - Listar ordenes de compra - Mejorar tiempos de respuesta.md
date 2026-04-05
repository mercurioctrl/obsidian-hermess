---
jira_key: "PED-1207"
aliases: ["PED-1207"]
summary: "API - Refactor - Listar ordenes de compra - Mejorar tiempos de respuesta"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2025-12-29 15:46"
updated: "2026-01-09 18:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1207"
---

# PED-1207: API - Refactor - Listar ordenes de compra - Mejorar tiempos de respuesta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2025-12-29 15:46 |
| Actualizado | 2026-01-09 18:49 |
| Etiquetas | ninguna |
| Jira | [PED-1207](https://bluinc.atlassian.net/browse/PED-1207) |

## Relaciones

- **Padre:** [[PED-8 - Listar ordenes de compra|PED-8]] Listar ordenes de compra

## Descripcion

Debido a los cambios recientes, sería conveniente implementar una mejora para optimizar el recurso de listado de órdenes. Por ello, se buscará que el tiempo máximo de espera sea de los dos segundos ya definidos.



Producción

[adjunto]
```
curl.exe ^"https://api.orders.lio.red/v1/orders?between=14-12-2025_29-12-2025^&companyCode=4^&currentPage=1^" ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0^" ^
  -H ^"Accept: application/json, text/plain, */*^" ^
  -H ^"Accept-Language: es-MX^" ^
  -H ^"Accept-Encoding: gzip, deflate, br, zstd^" ^
  -H ^"Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NjcxMTk4MjgsImF1ZCI6IjQ0NmQwNDlmODM4NjIxYjk5Y2IzYWNhMTNhNzRlNmJhMzAxZGM5MjMiLCJ1c2VyIjp7ImlkIjo2MzY2OCwiY29kZUZQIjoiNTU1NTQiLCJhZ2VudElkIjo1OSwidXN1SWRlbnRpZmljYWNpb24iOm51bGwsInJvbGVEZXNjcmlwdGlvbiI6IkFkbWluaXN0cmFkb3IiLCJwZWRpZG9zIjoxLCJwbSI6MCwiZGlzY291bnRTaGlwcGluZyI6MSwicmViaWxsIjowLCJpc1BtIjowLCJpc0dlcmVuY2lhIjoxLCJlZGl0Q29zdEZvclNhbGUiOm51bGwsInBlZF9mdWxsX2JlbmVmaXRzIjowLCJkZXNsaXF1aWRhciI6MCwidW5saW1pdGVkUmVwb3J0cyI6bnVsbCwiY3JlYXRlTWFudWFsVm91Y2hlciI6MCwiYmFuTGlzdFByaWNlIjpudWxsfSwiaWF0IjoxNzY3MDMzNDI4LCJuYmYiOjE3NjcwMzM0Mjh9.Yfa0hM4w_1Zhy827MW-MO7Ynml3kHXygCTMsEheiHVU^" ^
  -H ^"Origin: https://pedidos.saftel.com^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Referer: https://pedidos.saftel.com/^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: cross-site^"
```



Gamma

[adjunto]
```
curl.exe ^"https://gamma.api.orders.lio.red/v1/orders?between=14-12-2024_29-12-2024^&companyCode=4^&currentPage=1^" ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0^" ^
  -H ^"Accept: application/json, text/plain, */*^" ^
  -H ^"Accept-Language: es-MX^" ^
  -H ^"Accept-Encoding: gzip, deflate, br, zstd^" ^
  -H ^"Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NjcwMzY5NjksImF1ZCI6ImIyZjRiNjY3Y2Q0OWVmMWFkMmIwYTMzMDUzNmQ5YTZkNWUxN2U5NzAiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicm9sZURlc2NyaXB0aW9uIjoiQWRtaW5pc3RyYWRvciIsInBlZGlkb3MiOjEsInBtIjoxLCJkaXNjb3VudFNoaXBwaW5nIjoxLCJyZWJpbGwiOjEsImlzUG0iOjEsImlzR2VyZW5jaWEiOjEsImVkaXRDb3N0Rm9yU2FsZSI6MSwicGVkX2Z1bGxfYmVuZWZpdHMiOjEsImRlc2xpcXVpZGFyIjoxLCJ1bmxpbWl0ZWRSZXBvcnRzIjpudWxsLCJjcmVhdGVNYW51YWxWb3VjaGVyIjoxLCJiYW5MaXN0UHJpY2UiOiJDIiwidW5sb2NrZWRTZWxsZXJGaWx0ZXIiOjEsInVzZVN0b2NrSW5jb21pbmciOjF9LCJpYXQiOjE3NjcwMzMzNjksIm5iZiI6MTc2NzAzMzM2OX0.uNXPkVjTKtA4_RT27soAPnRO4rrCoJ4ixrj6juGsW6g^" ^
  -H ^"Origin: https://gamma.pedidos.saftel.com^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Referer: https://gamma.pedidos.saftel.com/^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: cross-site^"
```
