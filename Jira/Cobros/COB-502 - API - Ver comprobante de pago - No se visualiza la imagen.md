---
jira_key: "COB-502"
aliases: ["COB-502"]
summary: "API - Ver comprobante de pago - No se visualiza la imagen"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-03-26 11:23"
updated: "2024-04-29 17:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-502"
---

# COB-502: API - Ver comprobante de pago - No se visualiza la imagen

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-03-26 11:23 |
| Actualizado | 2024-04-29 17:07 |
| Etiquetas | ninguna |
| Jira | [COB-502](https://bluinc.atlassian.net/browse/COB-502) |

## Relaciones

- **Padre:** [[COB-33 - Cobrar|COB-33]] Cobrar
- **blocks:** [[COB-498 - API - Refactor - Ver comprobante de pago - Apuntar a NB|COB-498]] API - Refactor - Ver comprobante de pago - Apuntar a NB

## Descripcion

- Agregaremos la ruta completa para poder acceder a la imagen.



[adjunto]
---

Actualización 23/04/24

- Al abrir el comprobante, me encuentro con una advertencia que impide la apertura del modal correspondiente.



[adjunto]
```
curl 'https://gamma.api.cashbox.lio.red/v1/paymentVoucher/0002-10332596' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTM5MDk3MDcsImF1ZCI6Ijc0YmFiZWJkMTJkZTJlMmIzZGU0ZjM3OTk3YTkzYzNiODgzYjFkYTciLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImNvYnJvIjoiMSIsImNvYnJvQWRtaW4iOiIxIiwiYWdlbnRJZCI6IjEyIiwiYm94IjoiU2ViYSIsIm1hbmFnZW1lbnQiOiIxIiwiZWRpdF9jcmVkaXQiOiIxIiwiY29icm9BZGp1c3RUbyI6IjEifSwiaWF0IjoxNzEzOTA2MTA3LCJuYmYiOjE3MTM5MDYxMDd9.bFAKEL_Z-EcPyNQMFLXmodxij9SQ8RVkL4p8RDPnKMs' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://gamma.caja.saftel.com' \
  -H 'Referer: https://gamma.caja.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0' \
  -H 'sec-ch-ua: "Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"'
```
