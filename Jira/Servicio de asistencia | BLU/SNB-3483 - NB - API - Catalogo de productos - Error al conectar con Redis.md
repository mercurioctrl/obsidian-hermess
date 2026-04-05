---
jira_key: "SNB-3483"
aliases: ["SNB-3483"]
summary: "NB - API - Catalogo de productos - Error al conectar con Redis"
status: "Resuelta"
type: "Support"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Guillermo Avila"
created: "2025-10-17 14:38"
updated: "2025-11-07 17:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-3483"
---

# SNB-3483: NB - API - Catalogo de productos - Error al conectar con Redis

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Guillermo Avila |
| Creado | 2025-10-17 14:38 |
| Actualizado | 2025-11-07 17:07 |
| Etiquetas | ninguna |
| Jira | [SNB-3483](https://bluinc.atlassian.net/browse/SNB-3483) |

## Relaciones

- **relates to:** [[NBWEB-958 - API - Feat - Implementación de Redis en API NB con control vía .env de|NBWEB-958]] API - Feat -  Implementación de Redis en API NB con control vía .env de activacion y TTL

## Descripcion

Me aparece el siguiente error al consultar el recurso:

```
https://gamma.api.nb.com.ar/v1/teclado
```

[adjunto]
```
curl.exe ^"https://gamma.api.nb.com.ar/v1/teclado?currency=1^&iva=1^&available_stock=1^" ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0^" ^
  -H ^"Accept: application/json, text/plain, */*^" ^
  -H ^"Accept-Language: es-MX^" ^
  -H ^"Accept-Encoding: gzip, deflate, br, zstd^" ^
  -H ^"Referer: https://gamma.nb.com.ar/^" ^
  -H ^"Origin: https://gamma.nb.com.ar^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: same-site^" ^
  -H ^"Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NjA3MzMzNTAsImF1ZCI6IjBhNDM2ZGUwN2Y3NjI5ZjM3MWFiMGVlNDE2NWIyOTk3OGU1YjRiMDAiLCJ1c2VyIjp7ImlkIjo4MTIyMiwiY29kaWdvRlAiOiI5MTY5NSIsInJvbGUiOjEsImNvcnJlb0NvbmZpcm1hZG8iOjEsImNhcnJpdG9BY3Rpdm8iOjAsImJsYWNrVXNlciI6MCwic2hvd05hbWUiOm51bGwsIm1vZGUiOiJhcGkiLCJkb21haW4iOm51bGx9LCJpYXQiOjE3NjA3MjI1NTAsIm5iZiI6MTc2MDcyMjU1MH0.Gc7MoxH47odg9trmh_g3nFLLZx8NERoQoQiQ9EoxHwg^" ^
  -H ^"Connection: keep-alive^"
```
