---
jira_key: "PED-526"
aliases: ["PED-526"]
summary: "API - Refactor - Agregar comisiones de sucursal 10, que no se ven"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-02-02 08:47"
updated: "2024-02-08 14:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-526"
---

# PED-526: API - Refactor - Agregar comisiones de sucursal 10, que no se ven

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-02 08:47 |
| Actualizado | 2024-02-08 14:15 |
| Etiquetas | ninguna |
| Jira | [PED-526](https://bluinc.atlassian.net/browse/PED-526) |

## Relaciones

- **Padre:** [[PED-174 - Listar comisiones|PED-174]] Listar comisiones
- **is blocked by:** [[PED-175 - API - Feat - Listar comisiones|PED-175]] API - Feat - Listar comisiones

## Descripcion

En términos generales parece andar bien, pero no veo ningún pedido sucursal 10

```
GET {API_URL}/v1/comissions
```

[adjunto]
```
curl 'https://api.orders.lio.red/v1/comissions?sellerId=8&currentPage=1&between=01-01-2024_31-01-2024' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MDY5MDYyNTYsImF1ZCI6IjgyMGE2YTM0NjZhYjY2NWVlMDJlMzhlYTQzNDk2OTIzN2NkNWU0YTciLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjF9LCJpYXQiOjE3MDY4MTk4NTYsIm5iZiI6MTcwNjgxOTg1Nn0.IFF6uXtO1L1_0MfOX-p0oMUab15XhHgvUrv69_AYOMU' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://www.pedidos.saftel.com' \
  -H 'Referer: https://www.pedidos.saftel.com/comissions?sellerId=8&currentPage=1&between=01-01-2024_31-01-2024' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --compressed
```
