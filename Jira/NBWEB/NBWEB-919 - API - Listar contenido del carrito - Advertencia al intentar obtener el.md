---
jira_key: "NBWEB-919"
aliases: ["NBWEB-919"]
summary: "API - Listar contenido del carrito - Advertencia al intentar obtener el contenido"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-11-06 02:52"
updated: "2024-11-08 10:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-919"
---

# NBWEB-919: API - Listar contenido del carrito - Advertencia al intentar obtener el contenido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-11-06 02:52 |
| Actualizado | 2024-11-08 10:41 |
| Etiquetas | ninguna |
| Jira | [NBWEB-919](https://bluinc.atlassian.net/browse/NBWEB-919) |

## Relaciones

- **Padre:** [[NBWEB-602 - Sitio Web|NBWEB-602]] Sitio Web
- **relates to:** [[NBWEB-47 - Listar contenido del carrito|NBWEB-47]] Listar contenido del carrito

## Descripcion

Me aparece la siguiente advertencia al intentar obtener el contenido de mi carrito, la cual pareciera que impide se visualicen los artículos.

```
TECLADO AUREOX BATTLETAG GAMING GK400
```

```
curl "https://gamma.api.nb.com.ar/v1/carrito" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0" -H "Accept: application/json, text/plain, /" -H "Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3" -H "Accept-Encoding: gzip, deflate, br, zstd" -H "Referer: https://gamma.nb.com.ar/" -H "Origin: https://gamma.nb.com.ar" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: same-site" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MzA4ODIzNTcsImF1ZCI6ImQ2ODFkM2VmOTI4ZWJlOWMxOTIzMDNiNTliMzRhZDFhMWM5OWVmMGQiLCJ1c2VyIjp7ImlkIjo2NjM2OSwiY29kaWdvRlAiOiI3NTk4MCIsInJvbGUiOjEsImNvcnJlb0NvbmZpcm1hZG8iOjEsImNhcnJpdG9BY3Rpdm8iOjgyMTI2MDksImJsYWNrVXNlciI6MCwibW9kZSI6IndlYiIsImRvbWFpbiI6bnVsbH0sImlhdCI6MTczMDg3MTU1NywibmJmIjoxNzMwODcxNTU3fQ.TU8V9w6F_VpGgt_RLKfd_zmuAnfqhSZbZ0ye7hZJ7dE" -H "Connection: keep-alive"
```

[adjunto]
