---
jira_key: "PED-741"
aliases: ["PED-741"]
summary: "API - Review - Filtro por \"ordernar por\" \"ultima compra\" reportan que funciona mal para algunos vendedores (No pagina, solo muestra una pagina)"
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-06-05 17:50"
updated: "2024-06-06 10:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-741"
---

# PED-741: API - Review - Filtro por "ordernar por" "ultima compra" reportan que funciona mal para algunos vendedores (No pagina, solo muestra una pagina)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-05 17:50 |
| Actualizado | 2024-06-06 10:46 |
| Etiquetas | ninguna |
| Jira | [PED-741](https://bluinc.atlassian.net/browse/PED-741) |

## Relaciones

- **Padre:** [[PED-16 - Listar clientes|PED-16]] Listar clientes

## Descripcion

Adjunto un caso donde no pagina, pero hay otros casos donde si, como el de Lautaro por ejemplo.

```
curl 'https://api.orders.lio.red/v1/clients?sellerId=8&currentPage=1&order=lastBuy&direction=desc&itemsPerPage=100' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTc2NzUxODMsImF1ZCI6ImI5MTFiMWVhNmUyNTk4YTU4ZDNmNmE2ZmNkZTJiZmE3YzlkMjlhNTEiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjEsImRpc2NvdW50U2hpcHBpbmciOjEsInJlYmlsbCI6MX0sImlhdCI6MTcxNzU4ODc4MywibmJmIjoxNzE3NTg4NzgzfQ.Ie32tSVDm3FQ5ayjFFnOjx3JOiblO3_LB14CRwLA02g' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://www.pedidos.saftel.com' \
  -H 'Referer: https://www.pedidos.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"'
```
