---
jira_key: "PED-309"
aliases: ["PED-309"]
summary: "API - Review - Nuevos filtros (sin liquidacion) producen fallo al filtrar"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-12-05 16:15"
updated: "2024-01-18 13:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-309"
---

# PED-309: API - Review - Nuevos filtros (sin liquidacion) producen fallo al filtrar

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-05 16:15 |
| Actualizado | 2024-01-18 13:57 |
| Etiquetas | ninguna |
| Jira | [PED-309](https://bluinc.atlassian.net/browse/PED-309) |

## Relaciones

- **Padre:** [[PED-8 - Listar ordenes de compra|PED-8]] Listar ordenes de compra

## Descripcion

```
curl 'https://gamma.api.orders.lio.red/v1/orders?currentPage=1&itemsPerPage=15&sellerId=12&orderStatus=P' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MDE4MDcyNDUsImF1ZCI6IjJlMThhNDI3MTczNDdjMDFhODdkYTdkN2ExN2FiZWFlNTczMGI1N2QiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjF9LCJpYXQiOjE3MDE4MDM2NDUsIm5iZiI6MTcwMTgwMzY0NX0.cTfo8bbg5e9qu3yZE5DmI2nALaOntFy4rEPzR45oMnY' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://gamma.pedidos.saftel.com' \
  -H 'Referer: https://gamma.pedidos.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --compressed
```
