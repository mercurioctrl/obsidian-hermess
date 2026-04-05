---
jira_key: "PED-759"
aliases: ["PED-759"]
summary: "API - Refactor - En el filtro de Trust, cuando no filtro por vendedor tarda bastante, pero ademas suele no traer nada, cuando hay vendedors que si cumplieron el objetivo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-06-30 18:12"
updated: "2024-07-24 11:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-759"
---

# PED-759: API - Refactor - En el filtro de Trust, cuando no filtro por vendedor tarda bastante, pero ademas suele no traer nada, cuando hay vendedors que si cumplieron el objetivo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-30 18:12 |
| Actualizado | 2024-07-24 11:18 |
| Etiquetas | ninguna |
| Jira | [PED-759](https://bluinc.atlassian.net/browse/PED-759) |

## Relaciones

- **Padre:** [[PED-299]] Objetivos y Desafios
- **is blocked by:** [[PED-768]] API - Limites y Objetivos - Tiempo de espera excedido

## Descripcion

```
curl 'https://api.orders.lio.red/v1/objectives/capillarityIncentive?currentPage=1&sellerId=8&itemFilter=trust' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTk4Njc3NjgsImF1ZCI6IjIwNDU5NDA3NTk5YmU4OGQ5NWNhOWViNWM3NjRiYjhjN2VmNGZiZDkiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjEsImRpc2NvdW50U2hpcHBpbmciOjEsInJlYmlsbCI6MX0sImlhdCI6MTcxOTc4MTM2OCwibmJmIjoxNzE5NzgxMzY4fQ.x54wNULg5jLxq2Z57N4Ap4_uW0s4CFLeUdRE7r_sORU' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://www.pedidos.saftel.com' \
  -H 'Referer: https://www.pedidos.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"'
```
