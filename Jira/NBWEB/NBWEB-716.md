---
jira_key: "NBWEB-716"
summary: "APP - Seguimiento de envíos - Sin datos de seguimiento"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2024-04-17 20:13"
updated: "2024-04-23 23:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-716"
---

# NBWEB-716: APP - Seguimiento de envíos - Sin datos de seguimiento

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2024-04-17 20:13 |
| Actualizado | 2024-04-23 23:07 |
| Etiquetas | ninguna |
| Jira | [NBWEB-716](https://bluinc.atlassian.net/browse/NBWEB-716) |

## Descripción

Al no obtener datos de seguimiento se queda cargando.

[attachment]
Datos de la prueba:

```
curl 'https://gamma.api.nb.com.ar/v1/miCuenta/ordenesDeCompra/0002/10332671/tracking' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTM0MDM4MzIsImF1ZCI6ImY0YTVjMmY5N2M5MzI2ZDRhNDQ3OTlhN2MzODkxNjU2N2Q1YzZhNmIiLCJ1c2VyIjp7ImlkIjo2NjM2OSwiY29kaWdvRlAiOiI3NTk4MCIsInJvbGUiOjEsImNvcnJlb0NvbmZpcm1hZG8iOjEsImNhcnJpdG9BY3Rpdm8iOjgxOTYxMTMsImJsYWNrVXNlciI6MCwibW9kZSI6IndlYiJ9LCJpYXQiOjE3MTMzOTMwMzIsIm5iZiI6MTcxMzM5MzAzMn0.Hs2IKV2QuhKTRK8F2b9jem9_xOu75bhB7KdwCssOd0s' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://gamma.nb.com.ar' \
  -H 'Referer: https://gamma.nb.com.ar/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0' \
  -H 'sec-ch-ua: "Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"'
```
