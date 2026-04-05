---
jira_key: "PED-989"
aliases: ["PED-989"]
summary: "API - Review - Probar actualización de renta al cambiar el costo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2025-04-23 11:05"
updated: "2025-04-24 23:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-989"
---

# PED-989: API - Review - Probar actualización de renta al cambiar el costo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2025-04-23 11:05 |
| Actualizado | 2025-04-24 23:39 |
| Etiquetas | ninguna |
| Jira | [PED-989](https://bluinc.atlassian.net/browse/PED-989) |

## Relaciones

- **Padre:** [[PED-34 - Generar Editar ordenes|PED-34]] Generar / Editar ordenes
- **relates to:** [[PED-39 - API - Feat - Agregarquitar item a una orden|PED-39]] API - Feat - Agregar/quitar item a una orden
- **relates to:** [[PED-990 - APP - Refactor - Cambiar parámetro averageCost por costForSale|PED-990]] APP - Refactor - Cambiar parámetro averageCost	por costForSale

## Descripcion

Noté que al cambiar el costo, no se actualiza la renta. Esta solo se actualiza al cambiar el precio.

```
curl 'https://gamma.api.orders.lio.red/v1/orders/addItem' -X PATCH -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0' -H 'Accept: application/json, text/plain, */*' -H 'Accept-Language: es-MX' -H 'Accept-Encoding: gzip, deflate, br, zstd' -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDU0NzQ4NjMsImF1ZCI6IjFmYThlZjBhYjljYzYzODBkODUwY2MwYTNkODkyOTc4NTQzNGU4ZTUiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicm9sZURlc2NyaXB0aW9uIjoiUHJvZHVjdCBNYW5hZ2VyIiwicGVkaWRvcyI6MSwicG0iOjEsImRpc2NvdW50U2hpcHBpbmciOjEsInJlYmlsbCI6MSwiaXNQbSI6MCwiaXNHZXJlbmNpYSI6MCwiZWRpdENvc3RGb3JTYWxlIjoxLCJwZWRfZnVsbF9iZW5lZml0cyI6MCwiZGVzbGlxdWlkYXIiOjEsInVubGltaXRlZFJlcG9ydHMiOjB9LCJpYXQiOjE3NDU0NzEyNjMsIm5iZiI6MTc0NTQ3MTI2M30.Ip5na9kEdEMNaJrcIbJIOl7ZGuXBS_6mzE9t7uiXWvk' -H 'Content-Type: application/json' -H 'Origin: https://gamma.pedidos.saftel.com' -H 'Connection: keep-alive' -H 'Referer: https://gamma.pedidos.saftel.com/' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: cross-site' -H 'Priority: u=0' --data-raw '{"order":"10356457","branch":"0002","itemId":104636,"amount":2,"selectedPrice":100,"averageCost":100}'
```

[adjunto]
