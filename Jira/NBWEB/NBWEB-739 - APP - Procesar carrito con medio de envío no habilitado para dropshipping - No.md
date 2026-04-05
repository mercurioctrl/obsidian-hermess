---
jira_key: "NBWEB-739"
aliases: ["NBWEB-739"]
summary: "APP - Procesar carrito con medio de envío no habilitado para dropshipping - No se visualiza mensaje de respuesta"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2024-05-22 18:58"
updated: "2024-05-27 23:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-739"
---

# NBWEB-739: APP - Procesar carrito con medio de envío no habilitado para dropshipping - No se visualiza mensaje de respuesta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2024-05-22 18:58 |
| Actualizado | 2024-05-27 23:24 |
| Etiquetas | ninguna |
| Jira | [NBWEB-739](https://bluinc.atlassian.net/browse/NBWEB-739) |

## Relaciones

- **Padre:** [[NBWEB-602]] Sitio Web
- **blocks:** [[NBWEB-737]] APP - Refactor: Al procesar el carrito y recibir el error debe ser posible mostrar el mensaje con el nuevo objeto entregado por la api

## Descripcion

Al procesar el carrito con un medio de envío no disponible para hacer dropshipping, no se muestra el mensaje de respuesta.

[adjunto]
```
curl 'https://gamma.api.nb.com.ar/v1/carrito/process' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTY0MjU2NzIsImF1ZCI6ImI2MGE1Njg2NGUwYTg5MzVjODY0MDcxMTBkY2RlZTY3ODAzMmQxODMiLCJ1c2VyIjp7ImlkIjo2NjM2OSwiY29kaWdvRlAiOiI3NTk4MCIsInJvbGUiOjEsImNvcnJlb0NvbmZpcm1hZG8iOjEsImNhcnJpdG9BY3Rpdm8iOjgxOTcxNzMsImJsYWNrVXNlciI6MCwibW9kZSI6IndlYiJ9LCJpYXQiOjE3MTY0MTQ4NzIsIm5iZiI6MTcxNjQxNDg3Mn0.a0Bm-HG25MB5TSgrQlpkI6DR1mJpcRRD2MdtKdQqa-g' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://gamma.nb.com.ar' \
  -H 'Referer: https://gamma.nb.com.ar/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0' \
  -H 'sec-ch-ua: "Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw '{"note":"Gprueba0655","medioDePagoId":3,"dropShipping":true,"codigoPostalFavorito":"1000","mediodeEnvioId":3030,"idDirCli":"27466","datosBultos":{"weightKg":0.28,"sizeCm":"7.37x7.37x7.37","amount":1},"dpPayload":{"clientName":"Gprueba_Dropshipping","clientEmail":"gavila@nb.com.ar"}}'
```
