---
jira_key: "LOCAPP-43"
aliases: ["LOCAPP-43"]
summary: "API - Comprobante a tercero - Oportunidad de mejora "
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-04-29 16:02"
updated: "2024-05-01 13:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LOCAPP-43"
---

# LOCAPP-43: API - Comprobante a tercero - Oportunidad de mejora 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-04-29 16:02 |
| Actualizado | 2024-05-01 13:27 |
| Etiquetas | ninguna |
| Jira | [LOCAPP-43](https://bluinc.atlassian.net/browse/LOCAPP-43) |

## Relaciones

- **relates to:** [[LOCAPP-40 - API - Faet - Generar comprobante (fc,nc,db) a un tercero, para un cliente|LOCAPP-40]] API - Faet - Generar comprobante (fc,nc,db) a un tercero, para un cliente determinado

## Descripcion

Mi sugerencias como mejora son:

- Eliminar las advertencias; esto me parece que se puede hacer verificando que las variables estén definidas antes de utilizarlas


- Respuesta un poco más explicita del por qué “No se pudo crear el comprobante“



[adjunto]
```
curl 'https://gamma.api.warehouse.lio.red/v1/makeVoucher' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTQ0NTE4MzcsImF1ZCI6IjhhNDYyZWE1NzJlMGIyYzQ3ZGVkMWI2ZTE5YjhiMDNlNzhlNGJhMDYiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImFnZW50SWQiOiIxMiIsInVzdUlkZW50aWZpY2FjaW9uIjoiU2ViYSIsImV4cGVkaWNpb24iOiIxIiwiZXhwZWRpY2lvbkFkbWluIjoiMSIsIm1hbmFnZW1lbnQiOiIxIiwiZXhwX3VwbG9hZF9zZXJpYWxzIjoiMSJ9LCJpYXQiOjE3MTQ0MTU1MzcsIm5iZiI6MTcxNDQxNTUzN30.9KCApj2ZqCqoDVONhMPslbmXbIYcxFjAFECTUTKI-f0' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://gamma.expedicion.saftel.com' \
  -H 'Referer: https://gamma.expedicion.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0' \
  -H 'sec-ch-ua: "Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw '{"voucherTypeId":"1","clientId":80628,"pedido":"X000200569115","iibbPerception":"0.00","thirdVoucher":{"dniOrCuit":"5491123456789","socialName":"Gprueba Razon Social","niva":2,"address":"Gprueba dirección","province":22,"city":170,"docType":96}}'
```
