---
jira_key: "INV-209"
aliases: ["INV-209"]
summary: "API - MVP - Review - Al editar un item si se manda iva 0 dice success pero al abrir de nuevo el producto conserva el anterior"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Marbe Moreno"
created: "2025-10-15 18:18"
updated: "2025-11-12 16:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-209"
---

# INV-209: API - MVP - Review - Al editar un item si se manda iva 0 dice success pero al abrir de nuevo el producto conserva el anterior

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Marbe Moreno |
| Creado | 2025-10-15 18:18 |
| Actualizado | 2025-11-12 16:35 |
| Etiquetas | ninguna |
| Jira | [INV-209](https://bluinc.atlassian.net/browse/INV-209) |

## Relaciones

- **Padre:** [[INV-11 - API - Detalle de producto|INV-11]] API - Detalle de producto

## Descripcion

Realice este patch

```
curl 'https://gamma.api.inventory.lio.red/item/123838' \
  -X 'PATCH' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: en-US,en;q=0.9,es-ES;q=0.8,es;q=0.7' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NjA2Mzg1NzgsInVzdWFyaW8iOjgxNDA3fQ.kVz9hoQ6Ycpf8L7vx1Jo55IYMAq8UqvvarK9keJnSSQ' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://gamma.inventario.saftel.com' \
  -H 'Pragma: no-cache' \
  -H 'Referer: https://gamma.inventario.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '{"iva":0}'
```

y al hacer el get sigue estando en 10.5


```
curl 'https://gamma.api.inventory.lio.red/items?currentPage=1&itemsPerPage=300&companyCode=11&search=camioncito' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: en-US,en;q=0.9,es-ES;q=0.8,es;q=0.7' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NjA2Mzg1NzgsInVzdWFyaW8iOjgxNDA3fQ.kVz9hoQ6Ycpf8L7vx1Jo55IYMAq8UqvvarK9keJnSSQ' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://gamma.inventario.saftel.com' \
  -H 'Pragma: no-cache' \
  -H 'Referer: https://gamma.inventario.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"'
```
