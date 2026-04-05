---
jira_key: "SNB-3553"
aliases: ["SNB-3553"]
summary: "PED - API - Productos -> Error al buscar productos"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2025-12-09 14:20"
updated: "2025-12-09 14:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-3553"
---

# SNB-3553: PED - API - Productos -> Error al buscar productos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2025-12-09 14:20 |
| Actualizado | 2025-12-09 14:48 |
| Etiquetas | ninguna |
| Jira | [SNB-3553](https://bluinc.atlassian.net/browse/SNB-3553) |

## Relaciones

*Sin relaciones*

## Descripcion

[adjunto]
```
curl.exe ^"https://gamma.api.orders.lio.red/v1/items?between=24-11-2025_09-12-2025^&stock=1^&search=teclado^" ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0^" ^
  -H ^"Accept: application/json, text/plain, */*^" ^
  -H ^"Accept-Language: es-MX^" ^
  -H ^"Accept-Encoding: gzip, deflate, br, zstd^" ^
  -H ^"Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NjUzMDM3NDIsImF1ZCI6ImJmOTY1YmJiMjhjYjc5ZTllMjM2YWMyZDg1ODZhNTg3ZjQ0ZWE1M2EiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicm9sZURlc2NyaXB0aW9uIjoiQWRtaW5pc3RyYWRvciIsInBlZGlkb3MiOjEsInBtIjoxLCJkaXNjb3VudFNoaXBwaW5nIjoxLCJyZWJpbGwiOjEsImlzUG0iOjEsImlzR2VyZW5jaWEiOjEsImVkaXRDb3N0Rm9yU2FsZSI6MSwicGVkX2Z1bGxfYmVuZWZpdHMiOjEsImRlc2xpcXVpZGFyIjoxLCJ1bmxpbWl0ZWRSZXBvcnRzIjpudWxsLCJjcmVhdGVNYW51YWxWb3VjaGVyIjoxLCJiYW5MaXN0UHJpY2UiOiJDIiwidW5sb2NrZWRTZWxsZXJGaWx0ZXIiOjEsInVzZVN0b2NrSW5jb21pbmciOjF9LCJpYXQiOjE3NjUzMDAxNDIsIm5iZiI6MTc2NTMwMDE0Mn0.446d67jBMg8uy-ekZUFozPpSS4yIIS4-avknbLdROFA^" ^
  -H ^"Origin: https://gamma.pedidos.saftel.com^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Referer: https://gamma.pedidos.saftel.com/^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: cross-site^"
```
