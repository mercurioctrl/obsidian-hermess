---
jira_key: "SNB-2979"
aliases: ["SNB-2979"]
summary: "Libre Opción - Autologin desde pedidos fallido "
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2025-04-09 16:27"
updated: "2025-04-14 11:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-2979"
---

# SNB-2979: Libre Opción - Autologin desde pedidos fallido 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2025-04-09 16:27 |
| Actualizado | 2025-04-14 11:18 |
| Etiquetas | ninguna |
| Jira | [SNB-2979](https://bluinc.atlassian.net/browse/SNB-2979) |

## Relaciones

- **relates to:** [[LIO-85]] API - Feat - AutoLogin desde pedidos
- **action item from:** [[LIO-320]] Cambiar URL a v4 en autologin 

## Descripcion

Al intentar hacer autologin desde el sistema de Pedidos en producción, me aparece el siguiente mensaje 
”El token no es válido.”

```
Gaston Luna Paez
```

```
curl "https://omega-api.libreopcion.com.ar/auth/autologin" -X POST -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0" -H "Accept: application/json, text/plain, */*" -H "Accept-Language: es-MX" -H "Accept-Encoding: gzip, deflate, br, zstd" -H "Content-Type: application/json" -H "Origin: https://libreopcion.com.ar" -H "Connection: keep-alive" -H "Referer: https://libreopcion.com.ar/" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: same-site" --data-raw "{""token"":""d897a5887f4d11980c4cda8ab39d7bc5""}"
```

[adjunto]


```
curl "https://omega-api4.libreopcion.com.ar/v4/auth/user" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0" -H "Accept: application/json, text/plain, */*" -H "Accept-Language: es-MX" -H "Accept-Encoding: gzip, deflate, br, zstd" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjp7ImlkIjoyOTg5MzMsImVtYWlsIjoidG9uZ2FzLnJhbWlyb3UyQGdtYWlsLmNvbSIsIm5vbWJyZSI6Ikdhc3RvbiBMdW5hIFBhZXoiLCJwZXJmaWwiOiJjb21wcmFkb3IiLCJkb2N1bWVudG8iOiIzOTI1Njc1NiIsInRlbGVmb25vIjoiMzQzNTAxODE5MyIsImRpcmVjY2lvbiI6eyJjYWxsZSI6IlNhbnRpYWdvIGRlbCBFc3Rlcm8iLCJudW1lcm8iOiIxMDUiLCJwaXNvIjoiIiwiY2FzYUFwdG8iOiIifSwiY29kaWdvX3Bvc3RhbCI6IjMxMjIiLCJhdmF0YXIiOjIwLCJjaXVkYWQiOnsiaWQiOjM3NzUsIm5vbWJyZSI6IkNFUlJJVE8iLCJwcm92aW5jaWFfaWQiOjUsInRvdGFsIjowfSwicHJvdmluY2lhIjp7ImlkIjo1LCJrZXkiOjUsIm5vbWJyZSI6IkVOVFJFIFJJT1MiLCJwYWlzX2lkIjo3LCJ0b3RhbCI6MCwiY2l1ZGFkX2RlZmVjdG9faWQiOjB9LCJwYWlzIjp7ImlkIjo3LCJub21icmUiOiJBUkdFTlRJTkEiLCJ0b3RhbCI6MH0sInRpZW5kYV9pZCI6MCwidmVuZGVkb3JfaWQiOjI2NjE5MiwidG9rZW5WNCI6IjMyM0U1RjdFLUIyQjktNDkwRC05OEJBLUZBODI3MUU0NUQxNyIsImNvZGlnb19wb3N0YWxfZGVmYXVsdCI6bnVsbH0sImlzcyI6ImxpYnJlb3BjaW9uLmNvbSIsImF1ZCI6ImxpYnJlb3BjaW9uLmNvbSIsImlhdCI6MTc0NDIyNjQ4NCwibmJmIjoxNzQ0MjI2NDg0fQ.pmL4XNrFpM5nNv9VQjQ4XYwpQCNQc8ZhXD3__WuO9xQ" -H "Origin: https://libreopcion.com.ar" -H "Connection: keep-alive" -H "Referer: https://libreopcion.com.ar/" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: same-site"
```

[adjunto]
