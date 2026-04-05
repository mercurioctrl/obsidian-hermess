---
jira_key: "NBWEB-706"
aliases: ["NBWEB-706"]
summary: "API - Registro de usuario - Email invalido "
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Guillermo Avila"
created: "2024-04-15 00:59"
updated: "2024-04-23 19:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-706"
---

# NBWEB-706: API - Registro de usuario - Email invalido 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Guillermo Avila |
| Creado | 2024-04-15 00:59 |
| Actualizado | 2024-04-23 19:29 |
| Etiquetas | ninguna |
| Jira | [NBWEB-706](https://bluinc.atlassian.net/browse/NBWEB-706) |

## Relaciones

- **Padre:** [[NBWEB-602 - Sitio Web|NBWEB-602]] Sitio Web
- **relates to:** [[NBWEB-676 - API - Agregar agregar direccion, codigo postal y whatsapp en el registro de un|NBWEB-676]] API - Agregar agregar direccion, codigo postal y whatsapp en el registro de un cliente y que se pueda levantar en PED

## Descripcion

- Resultado obtenido: 



```
<br /> <b>Warning</b>: Undefined array key "ACCOUNT_CONFIRMATION_URL" in <b>/var/www/app/src/Support/AccountConfirmation.php</b> on line <b>46</b><br /> <br /> <b>Warning</b>: Undefined array key "ACCOUNT_CONFIRMATION_URL" in <b>/var/www/app/src/Support/AccountConfirmation.php</b> on line <b>48</b><br /> Message could not be sent. Mailer Error: SMTP Error: The following recipients failed: Gprueba_bremer@nb.com.ar: <Gprueba_bremer@nb.com.ar>: Recipient address rejected: User unknown in virtual mailbox table "Ocurri\u00f3 un error en el servidor de e-mails"
```

[adjunto]


- Pasos para replicar error: 



Ingresar un correo inexistente.


- Datos de la prueba: 



```
curl 'https://gamma.api.nb.com.ar/v1/registrationRequest' \
  -X 'PUT' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
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
  --data-raw '{"email":"Gprueba_bremer@nb.com.ar","username":"Gprueba_bremer","password":"Admin123","showName":"Gprueba_bremer","fiscalName":"Bremer Company SA de CV","socialName":"Bremer Comp","formatFiscalId":0,"fiscalId":"12345678","fiscalCategoryId":"3","province":9,"place":416,"address":"Lopez mateos","postalCode":"2024","name":"Bremer","lastName":"A","personId":"87654321","firstPhoneNumber":"0011234567","secondPhoneNumber":"0011234567","whaPhone":"5201123456787","howDidYouMeetUsId":null,"webSite":null}'
```



- Resultado esperado: 



Mensaje de error contenido en un objeto con parámetros previamente definidos.



- Posible solución:

- Verificar que la variable de entorno se encuentre en el archivo `.env` del servidor


- Modificar el mensaje que devuelve como respuesta a un objeto parecido a  `{success: false, message: $mail->ErrorInfo}`





[adjunto]
