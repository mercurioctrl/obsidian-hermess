---
jira_key: "SNB-3285"
aliases: ["SNB-3285"]
summary: "Whaticket - LO - Orden de los mensajes del ticket"
status: "Resuelta"
type: "Support"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2025-07-29 16:03"
updated: "2025-07-31 11:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-3285"
---

# SNB-3285: Whaticket - LO - Orden de los mensajes del ticket

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2025-07-29 16:03 |
| Actualizado | 2025-07-31 11:49 |
| Etiquetas | ninguna |
| Jira | [SNB-3285](https://bluinc.atlassian.net/browse/SNB-3285) |

## Relaciones

- **relates to:** [[LIO-228]] API - Feat - Mostrar un ticket por id de ticket

## Descripcion

Desde Whaticket nos reportan que no es posible visualizar los mensajes recientes enviados, sin embargo, al ver el caso se pudo observar que es posible que el ordenamiento es el que habría que ajustar

[adjunto]
```
curl ^"https://omega-api4.libreopcion.com.ar/v4/ticket/735534?id=1025^" ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0^" ^
  -H ^"Accept: application/json, text/plain, */*^" ^
  -H ^"Accept-Language: es-MX^" ^
  -H ^"Accept-Encoding: gzip, deflate, br, zstd^" ^
  -H ^"Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NjY3NzQ2NjgsImF1ZCI6ImM0YjIzYmI5ZmE4NTBlY2IwYjA5OWY1NTg1NDFhOTIzNTUyMTYyZmQiLCJ1c2VyIjp7ImlkIjoyODI3NDYsImVtYWlsIjoiZ2Vyb3BpbmNoYTI5MDhAZ21haWwuY29tIiwibm9tYnJlIjoiR2VyXHUwMGYzbmltbyBHYXJjaWEgRGFuaWVsIiwicGVyZmlsIjoidXN1YXJpbyIsImRvY3VtZW50byI6IjQ2OTA4ODEzIiwidGVsZWZvbm8iOiIyMjE2MTYgNTM3NCIsImRpcmVjY2lvbiI6eyJjYWxsZSI6IjUyMSA1IHkgNiIsIm51bWVybyI6IjEwNDgiLCJwaXNvIjoiLiIsImNhc2FBcHRvIjoiY2FzYSJ9LCJjb2RpZ29Qb3N0YWwiOiIxOTAwIiwiYXZhdGFyIjo2MywiY2l1ZGFkIjp7ImlkIjoxMDgyMywibm9tYnJlIjoiTEEgUExBVEEgICAgICAgICAgICAgICAgICAgICAgIiwicHJvdmluY2lhSWQiOjJ9LCJwcm92aW5jaWEiOnsiaWQiOjIsIm5vbWJyZSI6IkJVRU5PUyBBSVJFUyIsInBhaXNJZCI6NywiY2l1ZGFkRGVmZWN0b0lkIjoxMDgyM30sInBhaXMiOnsiaWQiOjcsIm5vbWJyZSI6IkFSR0VOVElOQSJ9LCJ0aWVuZGFJZCI6MCwidmVuZGVkb3JJZCI6MjUxMDE0LCJ0b2tlblYzIjoiZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SjFjM1ZoY21sdklqcDdJbWxrSWpveU9ESTNORFlzSW1WdFlXbHNJam9pWjJWeWIzQnBibU5vWVRJNU1EaEFaMjFoYVd3dVkyOXRJaXdpYm05dFluSmxJam9pUjJWeVhIVXdNR1l6Ym1sdGJ5QkhZWEpqYVdFZ1JHRnVhV1ZzSWl3aWNHVnlabWxzSWpvaVkyOXRjSEpoWkc5eUlpd2laRzlqZFcxbGJuUnZJam9pTkRZNU1EZzRNVE1pTENKMFpXeGxabTl1YnlJNklqSXlNVFl4TmlBMU16YzBJaXdpWkdseVpXTmphVzl1SWpwN0ltTmhiR3hsSWpvaU5USXhJRFVnZVNBMklpd2liblZ0WlhKdklqb2lNVEEwT0NJc0luQnBjMjhpT2lJdUlpd2lZMkZ6WVVGd2RHOGlPaUpqWVhOaEluMHNJbU52WkdsbmIxOXdiM04wWVd3aU9pSXhPVEF3SWl3aVlYWmhkR0Z5SWpvMk15d2lZMmwxWkdGa0lqcDdJbWxrSWpveE1EZ3lNeXdpYm05dFluSmxJam9pVEVFZ1VFeEJWRUVpTENKd2NtOTJhVzVqYVdGZmFXUWlPaklzSW5SdmRHRnNJam93ZlN3aWNISnZkbWx1WTJsaElqcDdJbWxrSWpveUxDSnJaWGtpT2pJc0ltNXZiV0p5WlNJNklrSlZSVTVQVXlCQlNWSkZVeUlzSW5CaGFYTmZhV1FpT2pjc0luUnZkR0ZzSWpvd0xDSmphWFZrWVdSZlpHVm1aV04wYjE5cFpDSTZNSDBzSW5CaGFYTWlPbnNpYVdRaU9qY3NJbTV2YldKeVpTSTZJa0ZTUjBWT1ZFbE9RU0lzSW5SdmRHRnNJam93ZlN3aWRHbGxibVJoWDJsa0lqb3dMQ0oyWlc1a1pXUnZjbDlwWkNJNk1qVXhNREUwTENKMGIydGxibFkwSWpvaVFUZEZNakJGTmtFdE1EbERSQzAwUlRZMExVRkZSVE10TkRrMFJUUXpOa1ZFTjBFMElpd2lZMjlrYVdkdlgzQnZjM1JoYkY5a1pXWmhkV3gwSWpveE9UQXdMQ0poWTNScGRtVlhZV3hzWlhRaU9tWmhiSE5sZlN3aWFYTnpJam9pYkdsaWNtVnZjR05wYjI0dVkyOXRJaXdpWVhWa0lqb2liR2xpY21WdmNHTnBiMjR1WTI5dElpd2lhV0YwSWpveE56VXpPREUwTmpZNExDSnVZbVlpT2pFM05UTTRNVFEyTmpoOS5BbHY1YnNHOTR5VWVTbVlwcngzczhMcVNscVY0c3k2TXNhTy12NDJmNV9nIiwiY29kaWdvUG9zdGFsRGVmYXVsdCI6MTkwMCwiYWN0aXZlV2FsbGV0IjpmYWxzZX0sImlhdCI6MTc1MzgxNDY2OCwibmJmIjoxNzUzODE0NjY4fQ.u8rki8-_JpgfUiHkmySVRvWyGC0nZIWdLZ7IxEZReHk^" ^
  -H ^"Origin: https://libreopcion.com.ar^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Referer: https://libreopcion.com.ar/^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: same-site^" ^
  -H ^"Priority: u=0^"
```
