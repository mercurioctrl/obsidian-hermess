---
jira_key: "PED-211"
aliases: ["PED-211"]
summary: "API - Review - Generar pedido de una orden de libre opcion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-11-02 11:48"
updated: "2024-01-18 20:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-211"
---

# PED-211: API - Review - Generar pedido de una orden de libre opcion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-11-02 11:48 |
| Actualizado | 2024-01-18 20:08 |
| Etiquetas | ninguna |
| Jira | [PED-211](https://bluinc.atlassian.net/browse/PED-211) |

## Relaciones

- **Padre:** [[PED-91 - APP - Feat - Generar pedido|PED-91]] APP - Feat - Generar pedido

## Descripcion

Al intentar generar un pedido a partir de una orden emitida por libre opcion recibo un error

```
curl 'https://gamma.api.orders.lio.red/v1/makeSale' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2OTg5Mzg0ODksImF1ZCI6IjVmYzFkODMyMzJhMjEzNGE4MGE1OTUxOTg0NTMzZjY5MzJmNjhkNGIiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MX0sImlhdCI6MTY5ODkzNDg4OSwibmJmIjoxNjk4OTM0ODg5fQ.YbRjXINaFFMpcMqMsr5nuwX8ms7fZdlKaKG_FKNQ4JE' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://gamma.pedidos.saftel.com' \
  -H 'Referer: https://gamma.pedidos.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '{"branch":"0002","order":"10314844"}' \
  --compressed
```
