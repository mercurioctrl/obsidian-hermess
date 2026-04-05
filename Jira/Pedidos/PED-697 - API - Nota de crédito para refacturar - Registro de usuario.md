---
jira_key: "PED-697"
aliases: ["PED-697"]
summary: "API - Nota de crédito para refacturar - Registro de usuario"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-04-25 13:33"
updated: "2024-04-30 13:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-697"
---

# PED-697: API - Nota de crédito para refacturar - Registro de usuario

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-04-25 13:33 |
| Actualizado | 2024-04-30 13:50 |
| Etiquetas | ninguna |
| Jira | [PED-697](https://bluinc.atlassian.net/browse/PED-697) |

## Relaciones

- **Padre:** [[PED-5 - Comprobantes|PED-5]] Comprobantes
- **blocks:** [[PED-653 - API - Feat - Hacer NC y Desvincular para refacturar un comprobante|PED-653]] API - Feat - Hacer NC y Desvincular para refacturar un comprobante

## Descripcion

Solo faltaría marcar en la cabecera de las facturas que usuario realiza la acción.

[adjunto]
```
curl 'https://gamma.api.orders.lio.red/v1/creditToRebill' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTQwNzI5MzYsImF1ZCI6IjZjYmM3MTRlZmEzM2YzODBmNDUyMmE4MDUxMWQ2OTI0NzYxNDVlM2IiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjEsImRpc2NvdW50U2hpcHBpbmciOjEsInJlYmlsbCI6MX0sImlhdCI6MTcxNDA2OTMzNiwibmJmIjoxNzE0MDY5MzM2fQ.MxagWft00UkleJX225xtDk3D6UIXTvN8-PpDnYmOhB0' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://gamma.pedidos.saftel.com' \
  -H 'Referer: https://gamma.pedidos.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0' \
  -H 'sec-ch-ua: "Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw '{"clientId":"037811","pedido":"X000200568930","iibbPerception":14385}'
```
