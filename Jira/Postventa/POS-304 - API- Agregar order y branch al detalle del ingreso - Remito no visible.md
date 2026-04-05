---
jira_key: "POS-304"
aliases: ["POS-304"]
summary: "API- Agregar order y branch al detalle del ingreso - Remito no visible"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-07-07 22:23"
updated: "2024-07-08 11:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-304"
---

# POS-304: API- Agregar order y branch al detalle del ingreso - Remito no visible

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-07-07 22:23 |
| Actualizado | 2024-07-08 11:07 |
| Etiquetas | ninguna |
| Jira | [POS-304](https://bluinc.atlassian.net/browse/POS-304) |

## Relaciones

- **Padre:** [[POS-24]] Creditos
- **blocks:** [[POS-301]] API - Refactor - Agregar "order" y "branch" al detalle del ingreso de ser posible

## Descripcion

Por alguna razón, el remito no aparece en el detalle del ingreso. Esto podría deberse a que, al realizar el nuevo ingreso, no ingresé el número de serie. Lo hice a través del cliente y el producto.

[adjunto]
[adjunto]
```
curl 'https://gamma.api.aftersale.lio.red/v1/afterSales/35056' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MjA2MzU5NTQsImF1ZCI6ImQ2ZThjYmE5MDBiODk1OGZiZGIxNmM1NGQwNjcyYjVmYzAwZTdkMTciLCJ1c2VyIjp7ImlkIjoiNjI4MTEiLCJjb2RlRlAiOiIwNDc5NzAiLCJwb3N0dmVudGEiOiIxIiwicG9zdHZlbnRhX2NyZWRpdG9zIjoiMSIsImFnZW50SWQiOiI1OCIsInBvc3R2ZW50YV9zb2x1Y2lvbiI6IjEiLCJwb3N0dmVudGFfYWRtaW4iOiIxIiwidXN1SWRlbnRpZmljYWNpb24iOm51bGwsIm1hbmFnZW1lbnQiOiIxIn0sImlhdCI6MTcyMDI5MTQ5NCwibmJmIjoxNzIwMjkxNDk0fQ.wuCpCInH0Ut0KzDLkJhCMQ8f3KQFDD2diy8oPvgs3cs' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://gamma.postventa.saftel.com' \
  -H 'Referer: https://gamma.postventa.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OPR/111.0.0.0' \
  -H 'sec-ch-ua: "Opera";v="111", "Chromium";v="125", "Not.A/Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"'
```
