---
jira_key: "PED-1153"
aliases: ["PED-1153"]
summary: "APP - Review - Agregar/quitar item a una orden -> Error al editar un articulo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2025-10-09 15:48"
updated: "2025-11-12 10:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1153"
---

# PED-1153: APP - Review - Agregar/quitar item a una orden -> Error al editar un articulo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2025-10-09 15:48 |
| Actualizado | 2025-11-12 10:41 |
| Etiquetas | ninguna |
| Jira | [PED-1153](https://bluinc.atlassian.net/browse/PED-1153) |

## Relaciones

- **Padre:** [[PED-34 - Generar Editar ordenes|PED-34]] Generar / Editar ordenes
- **relates to:** [[PED-39 - API - Feat - Agregarquitar item a una orden|PED-39]] API - Feat - Agregar/quitar item a una orden
- **relates to:** [[PED-1150 - API - MVP - Refactor - Incluir stockWarehouseCode junto a stockWarehouseId y|PED-1150]] API - MVP - Refactor - Incluir stockWarehouseCode junto a stockWarehouseId y stockWarehouseDescription
- **action item from:** [[PED-1149 - APP - MVP - Refacotor - Mostrar almacén en detalle de órdenes|PED-1149]] APP - MVP - Refacotor - Mostrar almacén en detalle de órdenes

## Descripcion

Al intentar modificar el costo de un articulo en el detalle de la orden, me aparece el siguiente error:

[adjunto]
```
curl.exe ^"https://gamma.api.orders.lio.red/v1/orders/addItem^" ^
  -X PATCH ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:143.0) Gecko/20100101 Firefox/143.0^" ^
  -H ^"Accept: application/json, text/plain, */*^" ^
  -H ^"Accept-Language: es-MX^" ^
  -H ^"Accept-Encoding: gzip, deflate, br, zstd^" ^
  -H ^"Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NjAwMzg1NjEsImF1ZCI6IjA3NjU1NjFkZWNlODg0ODdiNzE2OTRlMzA4ZTQwMTAxYTRmNjI3MmEiLCJ1c2VyIjp7ImlkIjo4MTQwNywiY29kZUZQIjoiOTIxNTciLCJhZ2VudElkIjo3MiwidXN1SWRlbnRpZmljYWNpb24iOm51bGwsInJvbGVEZXNjcmlwdGlvbiI6IlByb2R1Y3QgTWFuYWdlciIsInBlZGlkb3MiOjEsInBtIjoxLCJkaXNjb3VudFNoaXBwaW5nIjoxLCJyZWJpbGwiOjAsImlzUG0iOjEsImlzR2VyZW5jaWEiOjAsImVkaXRDb3N0Rm9yU2FsZSI6MSwicGVkX2Z1bGxfYmVuZWZpdHMiOjEsImRlc2xpcXVpZGFyIjowLCJ1bmxpbWl0ZWRSZXBvcnRzIjpudWxsLCJjcmVhdGVNYW51YWxWb3VjaGVyIjowLCJiYW5MaXN0UHJpY2UiOm51bGx9LCJpYXQiOjE3NjAwMzQ5NjEsIm5iZiI6MTc2MDAzNDk2MX0.3zTyqa7QqNzFF79r87fHhLGZvrlzLVBRYUom1ilTNDY^" ^
  -H ^"Content-Type: application/json^" ^
  -H ^"Origin: https://gamma.pedidos.saftel.com^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Referer: https://gamma.pedidos.saftel.com/^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: cross-site^" ^
  --data-raw ^"^{^\^"order^\^":^\^"10425805^\^",^\^"branch^\^":^\^"0002^\^",^\^"itemId^\^":115876,^\^"amount^\^":3,^\^"selectedPrice^\^":8.47,^\^"costForSale^\^":7^}^"
```
