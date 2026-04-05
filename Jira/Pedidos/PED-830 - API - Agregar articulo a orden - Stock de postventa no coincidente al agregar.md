---
jira_key: "PED-830"
aliases: ["PED-830"]
summary: "API - Agregar articulo a orden - Stock de postventa no coincidente al agregar articulo "
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-09-25 01:29"
updated: "2025-01-27 13:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-830"
---

# PED-830: API - Agregar articulo a orden - Stock de postventa no coincidente al agregar articulo 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-09-25 01:29 |
| Actualizado | 2025-01-27 13:49 |
| Etiquetas | ninguna |
| Jira | [PED-830](https://bluinc.atlassian.net/browse/PED-830) |

## Relaciones

- **Padre:** [[PED-64]] Productos
- **relates to:** [[PED-826]] API - Refactor - Agregar al repositorio de productos, aquellos productos que tienen stock en postventa y cuanto stock tiene de manera correspondiente

## Descripcion

Después de agregar un artículo a la orden que contaba con existencias en postventa, el nuevo stock de postventa muestra cero, a pesar de que antes de añadir el artículo había tres unidades disponibles.

[adjunto]
[adjunto]
```
curl 'https://gamma.api.orders.lio.red/v1/orders/addItem' -X PATCH -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0' -H 'Accept: application/json, text/plain, */*' -H 'Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3' -H 'Accept-Encoding: gzip, deflate, br, zstd' -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MjcyNDE2ODUsImF1ZCI6ImI0ZTk1YmQ5NDc4ODYxYTgyMjI1NjFmYTEzMWUwYWM2Yzg2OWMzYzIiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicm9sZURlc2NyaXB0aW9uIjoiQWRtaW5pc3RyYWRvciIsInBlZGlkb3MiOjEsInBtIjoxLCJkaXNjb3VudFNoaXBwaW5nIjoxLCJyZWJpbGwiOjF9LCJpYXQiOjE3MjcyMzgwODUsIm5iZiI6MTcyNzIzODA4NX0.4fTYdnggp1ONupkOpm4ASeBO_PODEuZDCvnZHqxhLWw' -H 'Content-Type: application/json' -H 'Origin: https://gamma.pedidos.saftel.com' -H 'Connection: keep-alive' -H 'Referer: https://gamma.pedidos.saftel.com/' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: cross-site' --data-raw '{"order":"10337025","branch":"0000","itemId":118016,"amount":1}'
```
