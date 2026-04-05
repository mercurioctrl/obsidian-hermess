---
jira_key: "NBWEB-712"
aliases: ["NBWEB-712"]
summary: "API - Agregar medio de envío al objeto de ordenes - Medio de envío vacío"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-04-15 19:15"
updated: "2024-04-16 17:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-712"
---

# NBWEB-712: API - Agregar medio de envío al objeto de ordenes - Medio de envío vacío

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-04-15 19:15 |
| Actualizado | 2024-04-16 17:59 |
| Etiquetas | ninguna |
| Jira | [NBWEB-712](https://bluinc.atlassian.net/browse/NBWEB-712) |

## Relaciones

- **Padre:** [[NBWEB-602]] Sitio Web
- **blocks:** [[NBWEB-681]] API - Refactor - Agregar el nombre de medio de envio al objeto de las ordenes

## Descripcion

- Resultado obtenido: 



[adjunto]
- Pasos para replicar error: 

- Crear una orden en el sitio de NB con medio de envío




- Datos de la prueba: 



```
curl 'https://gamma.api.nb.com.ar/v1/miCuenta/ordenesDeCompra?limit=10&offset=0' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTMyMjEyMTgsImF1ZCI6ImY0YTVjMmY5N2M5MzI2ZDRhNDQ3OTlhN2MzODkxNjU2N2Q1YzZhNmIiLCJ1c2VyIjp7ImlkIjo2NjM2OSwiY29kaWdvRlAiOiI3NTk4MCIsInJvbGUiOjEsImNvcnJlb0NvbmZpcm1hZG8iOjEsImNhcnJpdG9BY3Rpdm8iOjgxOTYwNTgsImJsYWNrVXNlciI6MCwibW9kZSI6IndlYiJ9LCJpYXQiOjE3MTMyMTA0MTgsIm5iZiI6MTcxMzIxMDQxOH0.jCzotoK6-ZM2Ddu0N6njxdIxq8f06KyFqq4t18cI8Ac' \
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

[adjunto]
- Resultado esperado: 

- Visualizar el id del medio de envío de la orden y su descripción




- Posible solución:

- Podría ser que se está haciendo relación con el remito, sin embargo, hasta este punto solo se ha creado la orden





[adjunto]
