---
jira_key: "LIO-54"
aliases: ["LIO-54"]
summary: "API - PED - Refactor - Al eliminar un pedido de libre opción en el sistema de pedidos, se debe marcar como \"cancelado\" en la plataforma libre opción - Orden no cancelada"
status: "Finalizada"
type: "Error"
priority: "Highest"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-06-19 03:17"
updated: "2024-06-19 12:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-54"
---

# LIO-54: API - PED - Refactor - Al eliminar un pedido de libre opción en el sistema de pedidos, se debe marcar como "cancelado" en la plataforma libre opción - Orden no cancelada

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Highest |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-06-19 03:17 |
| Actualizado | 2024-06-19 12:23 |
| Etiquetas | ninguna |
| Jira | [LIO-54](https://bluinc.atlassian.net/browse/LIO-54) |

## Relaciones

- **blocks:** [[LIO-30]] API - PED - Refactor - Al eliminar un pedido de libre opcion en el sistema de pedidos, se debe marcar como "cancelado" en la plataforma libre opcion

## Descripcion

Al eliminar la orden desde pedidos, esta no se cancela para Libre Opción.

`0002-10332857`

`580729`

[adjunto]
[adjunto]
```
curl "https://gamma.api.orders.lio.red/v1/orders/0002-10332857" ^
  -X "DELETE" ^
  -H "Accept: application/json, text/plain, */*" ^
  -H "Accept-Language: es-419,es;q=0.9" ^
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTg3Nzc3MjYsImF1ZCI6Ijg4NDkzYjE5YmI5MmQ0NzdjMDhhOTU5NDk2NmJhZTFjMTI3YTEyZTEiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjEsImRpc2NvdW50U2hpcHBpbmciOjEsInJlYmlsbCI6MX0sImlhdCI6MTcxODc3NDEyNiwibmJmIjoxNzE4Nzc0MTI2fQ.VahvSp8jIJRDD9cUreE5Ot8tGiIO7Jc6tZEIDFKJC_8" ^
  -H "Connection: keep-alive" ^
  -H "Origin: https://gamma.pedidos.saftel.com" ^
  -H "Referer: https://gamma.pedidos.saftel.com/" ^
  -H "Sec-Fetch-Dest: empty" ^
  -H "Sec-Fetch-Mode: cors" ^
  -H "Sec-Fetch-Site: cross-site" ^
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 OPR/110.0.0.0" ^
  -H ^"sec-ch-ua: ^\^"Chromium^\^";v=^\^"124^\^", ^\^"Opera^\^";v=^\^"110^\^", ^\^"Not-A.Brand^\^";v=^\^"99^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^"
```
