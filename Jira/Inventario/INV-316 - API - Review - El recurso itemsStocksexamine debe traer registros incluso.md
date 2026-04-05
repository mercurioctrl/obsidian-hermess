---
jira_key: "INV-316"
aliases: ["INV-316"]
summary: "API - Review - El recurso itemsStocks/examine debe traer  registros incluso cuando no se filtra el ID_ALMACEN de manera explicita -> Error de sintaxis"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2026-01-07 10:15"
updated: "2026-01-21 19:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-316"
---

# INV-316: API - Review - El recurso itemsStocks/examine debe traer  registros incluso cuando no se filtra el ID_ALMACEN de manera explicita -> Error de sintaxis

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2026-01-07 10:15 |
| Actualizado | 2026-01-21 19:01 |
| Etiquetas | ninguna |
| Jira | [INV-316](https://bluinc.atlassian.net/browse/INV-316) |

## Relaciones

- **Padre:** [[INV-199 - Control de Stock Stock en general Control de Precios|INV-199]] Control de Stock / Stock en general  / Control de Precios
- **clones:** [[INV-304 - API - Review - El recurso itemsStocksexamine debe traer registros incluso|INV-304]] API - Review - El recurso itemsStocks/examine debe traer  registros incluso cuando no se filtra el ID_ALMACEN de manera explicita

## Descripcion

Al consumir el recurso aparece el siguiente error de SQL:

[adjunto]
```
curl.exe ^"https://gamma.api.inventory.lio.red/itemsStocks/examine?itemId=118357^&type=salesReserved^&between=08-12-2025_07-01-2026^&currentPage=1^&itemsPerPage=20^" ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0^" ^
  -H ^"Accept: application/json, text/plain, */*^" ^
  -H ^"Accept-Language: es-MX^" ^
  -H ^"Accept-Encoding: gzip, deflate, br, zstd^" ^
  -H ^"Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3Njc4NzUyMzAsInVzdWFyaW8iOjc0NjN9.Vy_1foSkj7C2WuB-HE6yVnJJDT9UtNeLxAvvk7DslTY^" ^
  -H ^"Origin: https://gamma.inventario.saftel.com^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Referer: https://gamma.inventario.saftel.com/^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: cross-site^" ^
  -H ^"Priority: u=0^"
```
