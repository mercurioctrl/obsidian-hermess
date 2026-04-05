---
jira_key: "SNB-3161"
aliases: ["SNB-3161"]
summary: "API - Postventa - Postventas finalizadas -> Error al intentar generar orden de envío "
status: "Resuelta"
type: "Support"
priority: "Low"
assignee: "Catriel Mercurio"
reporter: "Guillermo Avila"
created: "2025-06-12 14:32"
updated: "2025-09-04 09:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-3161"
---

# SNB-3161: API - Postventa - Postventas finalizadas -> Error al intentar generar orden de envío 

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Low |
| Asignado | Catriel Mercurio |
| Reportado por | Guillermo Avila |
| Creado | 2025-06-12 14:32 |
| Actualizado | 2025-09-04 09:51 |
| Etiquetas | ninguna |
| Jira | [SNB-3161](https://bluinc.atlassian.net/browse/SNB-3161) |

## Relaciones

- **relates to:** [[POS-335 - API - Crear endpoint para generar orden de envio desde postventa - Error al|POS-335]] API - Crear endpoint para generar orden de envio desde postventa -> Error al intentar generar orden

## Descripcion

Al intentar generar la orden de envío desde el sistema de Postventa, se visualiza el siguiente error. 
Ema me comenta que esto puede ocurrir debido al servicio de correo en gamma.

```
curl "https://gamma.api.aftersale.lio.red/v1/afterSales/35055/finalized/createReturnOrder" -X POST -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0" -H "Accept: application/json, text/plain, */*" -H "Accept-Language: es-MX" -H "Accept-Encoding: gzip, deflate, br, zstd" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDkxNzgwMjMsImF1ZCI6IjIzMWFjMGFiOWYxN2M2MjlkMzgxZWQ2MzBkYjI3ZDA4ZmEyNjhmZDkiLCJ1c2VyIjp7ImlkIjoiNjI4MTEiLCJ1c2VybmFtZSI6ImVtYW56YW5vIiwiY29kZUZQIjoiMDQ3OTcwIiwicG9zdHZlbnRhIjoiMSIsInBvc3R2ZW50YV9jcmVkaXRvcyI6IjEiLCJhZ2VudElkIjoiNTgiLCJwb3N0dmVudGFfc29sdWNpb24iOiIxIiwicG9zdHZlbnRhX2FkbWluIjoiMSIsInVzdUlkZW50aWZpY2FjaW9uIjpudWxsLCJtYW5hZ2VtZW50IjoiMSJ9LCJpYXQiOjE3NDg4MzM1NjMsIm5iZiI6MTc0ODgzMzU2M30.tVNSfecHSwW5v9335d0LYfCq2aoHZLeBdd7k1kIYzBE" -H "Origin: https://gamma.postventa.saftel.com" -H "Connection: keep-alive" -H "Referer: https://gamma.postventa.saftel.com/" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: cross-site" -H "Priority: u=0" -H "Content-Length: 0"
```

[adjunto]
