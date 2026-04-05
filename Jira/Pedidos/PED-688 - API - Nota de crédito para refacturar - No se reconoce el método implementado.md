---
jira_key: "PED-688"
aliases: ["PED-688"]
summary: "API - Nota de crédito para refacturar - No se reconoce el método implementado"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-04-21 17:12"
updated: "2024-04-25 13:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-688"
---

# PED-688: API - Nota de crédito para refacturar - No se reconoce el método implementado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-04-21 17:12 |
| Actualizado | 2024-04-25 13:32 |
| Etiquetas | ninguna |
| Jira | [PED-688](https://bluinc.atlassian.net/browse/PED-688) |

## Relaciones

- **Padre:** [[PED-5]] Comprobantes
- **blocks:** [[PED-653]] API - Feat - Hacer NC y Desvincular para refacturar un comprobante

## Descripcion

Al intentar acreditar para refacturar me aparece el siguiente error, esto también me sucede al intentar generar una factura en ordenes. 

[adjunto]
```
curl "https://gamma.api.orders.lio.red/v1/creditToRebill" ^
  -H "Accept: application/json, text/plain, */*" ^
  -H "Accept-Language: es-419,es;q=0.9" ^
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTM3MzMwNDcsImF1ZCI6IjFlOWI2MGQ5NmM0YTRlOWFhMmEyODgyZWEwZDFhZWQ0YmEzOTA1ZWEiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjEsImRpc2NvdW50U2hpcHBpbmciOjEsInJlYmlsbCI6MX0sImlhdCI6MTcxMzcyOTQ0NywibmJmIjoxNzEzNzI5NDQ3fQ._IsitCNpt-_tH6INNo6iIkREhUWu5_Vrj0zjh1afQtI" ^
  -H "Connection: keep-alive" ^
  -H "Content-Type: application/json" ^
  -H "Origin: https://gamma.pedidos.saftel.com" ^
  -H "Referer: https://gamma.pedidos.saftel.com/" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: cross-site" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0" ^
  -H ^"sec-ch-ua: ^\^"Opera^\^";v=^\^"109^\^", ^\^"Not:A-Brand^\^";v=^\^"8^\^", ^\^"Chromium^\^";v=^\^"123^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" ^
  --data-raw ^"^{^\^"clientId^\^":^\^"080592^\^",^\^"pedido^\^":^\^"X000200569033^\^",^\^"iibbPerception^\^":0^}^"
```
