---
jira_key: "INV-307"
aliases: ["INV-307"]
summary: "API - Review - Al marcar o crear un nuevo kit, se debe verificar que el item sea \"nuevo\" (no tenga aun costo promedio), ni tenga ventas (albclil) - QA observaciones"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2025-12-26 11:35"
updated: "2025-12-29 12:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-307"
---

# INV-307: API - Review - Al marcar o crear un nuevo kit, se debe verificar que el item sea "nuevo" (no tenga aun costo promedio), ni tenga ventas (albclil) - QA observaciones

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2025-12-26 11:35 |
| Actualizado | 2025-12-29 12:09 |
| Etiquetas | ninguna |
| Jira | [INV-307](https://bluinc.atlassian.net/browse/INV-307) |

## Relaciones

- **Padre:** [[INV-253]] Crear y modificar Kits
- **clones:** [[INV-292]] API - Refactor - Al marcar o crear un nuevo kit, se debe verificar que el item sea "nuevo" (no tenga aun costo promedio), ni tenga ventas (albclil)

## Descripcion

Al intentar marcar un articulo, recién creado, como kit, me aparece el siguiente mensaje.

[adjunto]
[adjunto]
```
curl.exe ^"https://gamma.api.inventory.lio.red/itemsKits^" ^
  -X POST ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0^" ^
  -H ^"Accept: application/json, text/plain, */*^" ^
  -H ^"Accept-Language: es-MX^" ^
  -H ^"Accept-Encoding: gzip, deflate, br, zstd^" ^
  -H ^"Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NjY4NDMzMTcsInVzdWFyaW8iOjY2MzY5fQ.A30cNi0rkwF5Fxk0gqsXnF-Jfwf99B0WszPdOqYoURE^" ^
  -H ^"Content-Type: application/json^" ^
  -H ^"Origin: https://gamma.inventario.saftel.com^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Referer: https://gamma.inventario.saftel.com/^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: cross-site^" ^
  -H ^"Priority: u=0^" ^
  --data-raw ^"^{^\^"itemId^\^":125122^}^"
```
