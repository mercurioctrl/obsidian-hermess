---
jira_key: "NBWEB-711"
summary: "API - Seguimiento de envíos - Sin datos de seguimiento"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-04-15 18:05"
updated: "2024-04-17 20:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-711"
---

# NBWEB-711: API - Seguimiento de envíos - Sin datos de seguimiento

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-04-15 18:05 |
| Actualizado | 2024-04-17 20:18 |
| Etiquetas | ninguna |
| Jira | [NBWEB-711](https://bluinc.atlassian.net/browse/NBWEB-711) |

## Descripción

- Resultado obtenido: 



[attachment]
- Pasos para replicar error: 

- Agregar a una orden un tracking sin movimientos.




- Datos de la prueba: 



```
curl 'https://gamma.api.nb.com.ar/v1/miCuenta/ordenesDeCompra/0002/10332671/tracking' \
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

- Resultado esperado: 

- 1. Código de estado de la respuesta HTTP coincidente con el objeto devuelto


- 2. Objeto con estructura definida 





Esto con la finalidad de darle herramientas al Front para identificar la respuesta de la petición 

- Posible solución:

- 1. Cambiar código de estado devuelto


- 2. Modificar el objeto de respuesta





```
{ "success": false, "message": "No se encontraron datos para el tracking" }
```
