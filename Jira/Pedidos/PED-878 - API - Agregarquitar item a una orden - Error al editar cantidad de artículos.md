---
jira_key: "PED-878"
aliases: ["PED-878"]
summary: "API - Agregar/quitar item a una orden - Error al editar cantidad de artículos "
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-11-20 22:05"
updated: "2024-11-25 00:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-878"
---

# PED-878: API - Agregar/quitar item a una orden - Error al editar cantidad de artículos 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-11-20 22:05 |
| Actualizado | 2024-11-25 00:41 |
| Etiquetas | ninguna |
| Jira | [PED-878](https://bluinc.atlassian.net/browse/PED-878) |

## Relaciones

- **Padre:** [[PED-3 - Ordenes de compra|PED-3]] Ordenes de compra
- **relates to:** [[PED-39 - API - Feat - Agregarquitar item a una orden|PED-39]] API - Feat - Agregar/quitar item a una orden

## Descripcion

Al intentar modificar la cantidad de items en una orden de Postventa, me aparece el siguiente error

```
curl "https://gamma.api.orders.lio.red/v1/orders/addItem" -X PATCH -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0" -H "Accept: application/json, text/plain, */*" -H "Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3" -H "Accept-Encoding: gzip, deflate, br, zstd" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MzIxNTQyOTIsImF1ZCI6IjQxYmY4MWQyZjQ2YzZkZmYxNWEwZTk1NTRmODk0Y2QzODgwZmYxZWEiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicm9sZURlc2NyaXB0aW9uIjoiRGVwYXJ0YW1lbnRvIFJNQSIsInBlZGlkb3MiOjEsInBtIjoxLCJkaXNjb3VudFNoaXBwaW5nIjoxLCJyZWJpbGwiOjF9LCJpYXQiOjE3MzIxNTA2OTIsIm5iZiI6MTczMjE1MDY5Mn0.Odx2GULV7lhh_gmWVMWq1n6m2JE8KfE92AVdMBubYJg" -H "Content-Type: application/json" -H "Origin: https://gamma.pedidos.saftel.com" -H "Connection: keep-alive" -H "Referer: https://gamma.pedidos.saftel.com/" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: cross-site" -H "Priority: u=0" --data-raw "{""order"":""00000004"",""branch"":""0003"",""itemId"":111598,""amount"":""1"",""selectedPrice"":14.84798}"
```

[adjunto]
