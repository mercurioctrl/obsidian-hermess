---
jira_key: "SNB-1675"
aliases: ["SNB-1675"]
summary: "[NBWEB] Configuración del servicio de correo"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Guillermo Avila"
created: "2024-03-25 13:37"
updated: "2024-03-28 10:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-1675"
---

# SNB-1675: [NBWEB] Configuración del servicio de correo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Guillermo Avila |
| Creado | 2024-03-25 13:37 |
| Actualizado | 2024-03-28 10:22 |
| Etiquetas | ninguna |
| Jira | [SNB-1675](https://bluinc.atlassian.net/browse/SNB-1675) |

## Relaciones

*Sin relaciones*

## Descripcion

Al intentar registrar un usuario con un correo que no existe, se muestra el siguiente mensaje de error

[adjunto]
```
curl 'https://gamma.api.nb.com.ar/v1/registrationRequest' \
-X 'PUT' \
-H 'Accept: application/json, text/plain, /' \
-H 'Accept-Language: es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,es-MX;q=0.4' \
-H 'Connection: keep-alive' \
-H 'Content-Type: application/json' \
-H 'Origin: https://gamma.nb.com.ar' \
-H 'Referer: https://gamma.nb.com.ar/' \
-H 'Sec-Fetch-Dest: empty' \
-H 'Sec-Fetch-Mode: cors' \
-H 'Sec-Fetch-Site: same-site' \
-H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0' \
-H 'sec-ch-ua: "Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"' \
-H 'sec-ch-ua-mobile: ?0' \
-H 'sec-ch-ua-platform: "Windows"' \
--data-raw '{"email":"anterior@gmail.com","username":"Anterior","password":"Anterior++13a","showName":"Anterior","name":"Anterior","lastName":"Anterior","fiscalName":"Anterior","socialName":"Anterior","formatFiscalId":0,"personId":"12345678","fiscalId":"12345678","fiscalCategoryId":"1","firstPhoneNumber":"131312321","secondPhoneNumber":"12121312","province":2,"place":7,"howDidYouMeetUsId":"Haciendo gpruebas_2","webSite":"https://www.gavilaricardo.com.ar/"}'
```
