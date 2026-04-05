---
jira_key: "PED-990"
aliases: ["PED-990"]
summary: "APP - Refactor - Cambiar parámetro averageCost	por costForSale"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2025-04-24 23:25"
updated: "2025-05-02 23:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-990"
---

# PED-990: APP - Refactor - Cambiar parámetro averageCost	por costForSale

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2025-04-24 23:25 |
| Actualizado | 2025-05-02 23:36 |
| Etiquetas | ninguna |
| Jira | [PED-990](https://bluinc.atlassian.net/browse/PED-990) |

## Relaciones

- **Padre:** [[PED-34]] Generar / Editar ordenes
- **relates to:** [[PED-989]] API - Review - Probar actualización de renta al cambiar el costo
- **duplicates:** [[PED-925]] APP - MVP - Refactor - Guardar costo para el item de una orden

## Descripcion

Platicando con Eze, comenta que el nombre para el costo es `costForSale`.

```
curl "https://gamma.api.orders.lio.red/v1/orders/addItem" -X PATCH -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0" -H "Accept: application/json, text/plain, */*" -H "Accept-Language: es-MX" -H "Accept-Encoding: gzip, deflate, br, zstd" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDU1NTAzNDAsImF1ZCI6IjFmYThlZjBhYjljYzYzODBkODUwY2MwYTNkODkyOTc4NTQzNGU4ZTUiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicm9sZURlc2NyaXB0aW9uIjoiUHJvZHVjdCBNYW5hZ2VyIiwicGVkaWRvcyI6MSwicG0iOjEsImRpc2NvdW50U2hpcHBpbmciOjEsInJlYmlsbCI6MSwiaXNQbSI6MCwiaXNHZXJlbmNpYSI6MCwiZWRpdENvc3RGb3JTYWxlIjoxLCJwZWRfZnVsbF9iZW5lZml0cyI6MCwiZGVzbGlxdWlkYXIiOjEsInVubGltaXRlZFJlcG9ydHMiOjB9LCJpYXQiOjE3NDU1NDY3NDAsIm5iZiI6MTc0NTU0Njc0MH0.0dN9asyiPHjnA4iLKyH124Yh0PNhtP_p_lfwwp1_fKg" -H "Content-Type: application/json" -H "Origin: https://gamma.pedidos.saftel.com" -H "Connection: keep-alive" -H "Referer: https://gamma.pedidos.saftel.com/" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: cross-site" -H "Priority: u=0" --data-raw "{""order"":""10356460"",""branch"":""0002"",""itemId"":111598,""amount"":1,""selectedPrice"":14.84798,""averageCost"":7.48}"
```

[adjunto]
