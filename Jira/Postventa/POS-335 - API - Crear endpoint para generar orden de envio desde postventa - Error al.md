---
jira_key: "POS-335"
aliases: ["POS-335"]
summary: "API - Crear endpoint para generar orden de envio desde postventa -> Error al intentar generar orden"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2025-06-02 00:12"
updated: "2025-06-22 19:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-335"
---

# POS-335: API - Crear endpoint para generar orden de envio desde postventa -> Error al intentar generar orden

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2025-06-02 00:12 |
| Actualizado | 2025-06-22 19:22 |
| Etiquetas | ninguna |
| Jira | [POS-335](https://bluinc.atlassian.net/browse/POS-335) |

## Relaciones

- **relates to:** [[POS-329 - API - Feat - Crear endpoint para generar orden de envio desde postventa|POS-329]] API - Feat - Crear endpoint para generar orden de envio desde postventa
- **relates to:** [[SNB-3161 - API - Postventa - Postventas finalizadas - Error al intentar generar orden de|SNB-3161]] API - Postventa - Postventas finalizadas -> Error al intentar generar orden de envío 

## Descripcion

Al intentar generar una orden de envío desde postventa me aparece el siguiente error:

```
curl "https://gamma.api.aftersale.lio.red/v1/afterSales/35055/finalized/createReturnOrder" -X POST -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0" -H "Accept: application/json, text/plain, */*" -H "Accept-Language: es-MX" -H "Accept-Encoding: gzip, deflate, br, zstd" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDkxNzgwMjMsImF1ZCI6IjIzMWFjMGFiOWYxN2M2MjlkMzgxZWQ2MzBkYjI3ZDA4ZmEyNjhmZDkiLCJ1c2VyIjp7ImlkIjoiNjI4MTEiLCJ1c2VybmFtZSI6ImVtYW56YW5vIiwiY29kZUZQIjoiMDQ3OTcwIiwicG9zdHZlbnRhIjoiMSIsInBvc3R2ZW50YV9jcmVkaXRvcyI6IjEiLCJhZ2VudElkIjoiNTgiLCJwb3N0dmVudGFfc29sdWNpb24iOiIxIiwicG9zdHZlbnRhX2FkbWluIjoiMSIsInVzdUlkZW50aWZpY2FjaW9uIjpudWxsLCJtYW5hZ2VtZW50IjoiMSJ9LCJpYXQiOjE3NDg4MzM1NjMsIm5iZiI6MTc0ODgzMzU2M30.tVNSfecHSwW5v9335d0LYfCq2aoHZLeBdd7k1kIYzBE" -H "Origin: https://gamma.postventa.saftel.com" -H "Connection: keep-alive" -H "Referer: https://gamma.postventa.saftel.com/" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: cross-site" -H "Priority: u=0" -H "Content-Length: 0"
```

[adjunto]
Podríamos ayudar al usuario con mensajes más detallados que expliquen qué ocurre y por qué. Quizás podríamos agregar que nos referimos al tipo de postventa “No fallo“ o “Cambio“.

[adjunto]
