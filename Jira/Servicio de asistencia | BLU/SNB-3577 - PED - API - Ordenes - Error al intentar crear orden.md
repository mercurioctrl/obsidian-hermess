---
jira_key: "SNB-3577"
aliases: ["SNB-3577"]
summary: "PED - API - Ordenes - Error al intentar crear orden "
status: "Esperando por ayuda"
type: "Support"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2025-12-26 12:47"
updated: "2025-12-26 15:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-3577"
---

# SNB-3577: PED - API - Ordenes - Error al intentar crear orden 

| Campo | Valor |
|-------|-------|
| Estado | Esperando por ayuda (En curso) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2025-12-26 12:47 |
| Actualizado | 2025-12-26 15:32 |
| Etiquetas | ninguna |
| Jira | [SNB-3577](https://bluinc.atlassian.net/browse/SNB-3577) |

## Relaciones

*Sin relaciones*

## Descripcion

[adjunto]


```
curl.exe ^"https://gamma.api.orders.lio.red/v1/orders^" ^
  -X POST ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0^" ^
  -H ^"Accept: application/json, text/plain, */*^" ^
  -H ^"Accept-Language: es-MX^" ^
  -H ^"Accept-Encoding: gzip, deflate, br, zstd^" ^
  -H ^"Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NjY3NjUxMzIsImF1ZCI6IjI2MzE0NGExOThmNzk4YzFkMTNjMTQyNWFmYmEwM2Q2ZDc0NzhlOWIiLCJ1c2VyIjp7ImlkIjo2NjM2OSwiY29kZUZQIjoiNzU5ODAiLCJhZ2VudElkIjo2MSwidXN1SWRlbnRpZmljYWNpb24iOm51bGwsInJvbGVEZXNjcmlwdGlvbiI6bnVsbCwicGVkaWRvcyI6MSwicG0iOjEsImRpc2NvdW50U2hpcHBpbmciOjEsInJlYmlsbCI6MSwiaXNQbSI6MSwiaXNHZXJlbmNpYSI6MSwiZWRpdENvc3RGb3JTYWxlIjoxLCJwZWRfZnVsbF9iZW5lZml0cyI6MSwiZGVzbGlxdWlkYXIiOjEsInVubGltaXRlZFJlcG9ydHMiOjEsImNyZWF0ZU1hbnVhbFZvdWNoZXIiOjEsImJhbkxpc3RQcmljZSI6IjEiLCJ1bmxvY2tlZFNlbGxlckZpbHRlciI6MSwidXNlU3RvY2tJbmNvbWluZyI6MX0sImlhdCI6MTc2Njc2MTUzMiwibmJmIjoxNzY2NzYxNTMyfQ.-u8mH_QeTjq656IXis_IoyQZ04SNjmUcYGYjRi9X43k^" ^
  -H ^"Content-Type: application/json^" ^
  -H ^"Origin: https://gamma.pedidos.saftel.com^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Referer: https://gamma.pedidos.saftel.com/^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: cross-site^" ^
  --data-raw ^"^{^\^"clientId^\^":91845,^\^"branch^\^":^\^"0002^\^"^}^"
```
