---
jira_key: "PED-706"
aliases: ["PED-706"]
summary: "API - Listado de ordenes -> Destino bancario - No coincidente con el liquidado"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-04-30 20:34"
updated: "2024-05-07 17:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-706"
---

# PED-706: API - Listado de ordenes -> Destino bancario - No coincidente con el liquidado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-04-30 20:34 |
| Actualizado | 2024-05-07 17:11 |
| Etiquetas | ninguna |
| Jira | [PED-706](https://bluinc.atlassian.net/browse/PED-706) |

## Relaciones

- **Padre:** [[PED-3]] Ordenes de compra
- **blocks:** [[PED-705]] API - Refactor - agregar campo destino bancario para recurso de comprobante

## Descripcion

Al liquidar seleccione el banco `BANCO SANTANDER RIO S.A.`, sin embargo, me aparece otro banco en el comprobante.

[adjunto]
```
curl 'https://gamma.api.orders.lio.red/v1/orders?currentPage=1&itemsPerPage=15&between=01-01-2023_30-04-2024&orderTypeId=5&search=10332769' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTQ1MjI1MjMsImF1ZCI6IjZjYmM3MTRlZmEzM2YzODBmNDUyMmE4MDUxMWQ2OTI0NzYxNDVlM2IiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjEsImRpc2NvdW50U2hpcHBpbmciOjEsInJlYmlsbCI6MX0sImlhdCI6MTcxNDUxODkyMywibmJmIjoxNzE0NTE4OTIzfQ.17Pz2D163zyfdXgPW6U9Vv7u9oOcwnAaoTGWRUDuZn4' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://gamma.pedidos.saftel.com' \
  -H 'Referer: https://gamma.pedidos.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0' \
  -H 'sec-ch-ua: "Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"'
```
