---
jira_key: "NBWEB-707"
aliases: ["NBWEB-707"]
summary: "API - Enviar correo al adjuntar comprobante de pago - Error al enviar correo"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Guillermo Avila"
created: "2024-04-15 01:34"
updated: "2024-04-17 19:55"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-707"
---

# NBWEB-707: API - Enviar correo al adjuntar comprobante de pago - Error al enviar correo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Guillermo Avila |
| Creado | 2024-04-15 01:34 |
| Actualizado | 2024-04-17 19:55 |
| Etiquetas | ninguna |
| Jira | [NBWEB-707](https://bluinc.atlassian.net/browse/NBWEB-707) |

## Relaciones

- **Padre:** [[NBWEB-602 - Sitio Web|NBWEB-602]] Sitio Web
- **blocks:** [[NBWEB-690 - Enviar correo de comporbante adjutnado|NBWEB-690]] Enviar correo de comporbante adjutnado

## Descripcion

- Resultado obtenido: 



```
Message could not be sent.Mailer Error: SMTP Error: The following recipients failed: testing@nb.com.ar: <testing@nb.com.ar>: Recipient address rejected: User unknown in virtual mailbox table
```

[adjunto]


- Pasos para replicar error: 



Guardar comprobante en una orden de “MIS ORDENES DE COMPRA“.



- Datos de la prueba: 



```
curl 'https://gamma.api.nb.com.ar/v1/paymentVoucher' \
  -X 'PATCH' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTMxNzE5NjgsImF1ZCI6IjY5NzI5YjA1ZTBkMjc2ODA2YzEwMzk4ODMyYjUxYTU0YTYzMjBlYzQiLCJ1c2VyIjp7ImlkIjo2NjM2OSwiY29kaWdvRlAiOiI3NTk4MCIsInJvbGUiOjEsImNvcnJlb0NvbmZpcm1hZG8iOjEsImNhcnJpdG9BY3Rpdm8iOjgxOTUwNTQsImJsYWNrVXNlciI6MCwibW9kZSI6IndlYiJ9LCJpYXQiOjE3MTMxNjExNjgsIm5iZiI6MTcxMzE2MTE2OH0.kSOeboKMzp4-owWO9JlbFdKcI8y5K6XIsIX1vemAd3I' \
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
  --data-raw '[{"branch":"0002","order":"10332671","fileImg":"731da603219cb848041e35bb9b43806f.png","cbu":"1033267112343221122222","nroOperacion":"10332671","nameOwner":"Gprueba0310","internalOperationNumber":"031011"}]'
```



- Resultado esperado: 



A pesar de que no se envío el correo devolver mensaje satisfactorio de que el comprobante se ha guardado sin la advertencia.



- Posible solución:

- Verificar que el correo `testing@nb.com.ar` esté activo


- Contener el error y registrar si se envío o no el correo
