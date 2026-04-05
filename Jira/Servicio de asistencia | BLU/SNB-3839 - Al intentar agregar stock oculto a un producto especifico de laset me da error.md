---
jira_key: "SNB-3839"
aliases: ["SNB-3839"]
summary: "Al intentar agregar stock oculto a un producto especifico de laset me da error"
status: "Esperando por el cliente"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-03-31 06:06"
updated: "2026-03-31 17:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-3839"
---

# SNB-3839: Al intentar agregar stock oculto a un producto especifico de laset me da error

| Campo | Valor |
|-------|-------|
| Estado | Esperando por el cliente (En curso) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-03-31 06:06 |
| Actualizado | 2026-03-31 17:10 |
| Etiquetas | ninguna |
| Jira | [SNB-3839](https://bluinc.atlassian.net/browse/SNB-3839) |

## Relaciones

*Sin relaciones*

## Descripcion

```
curl 'https://api.inventory.lio.red/itemsStocks/121769/manualAdjustments' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NzUwMzQwNzgsInVzdWFyaW8iOjc0NjN9.jYa6oqE59mCv3ClmrcoMWsHqFRkqCKvuW63wxEBP7Uo' \
  -H 'Referer: https://inventario.saftel.com/' \
  -H 'sec-ch-ua: "Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Content-Type: application/json' \
  --data-raw '{"amount":10,"reason":"Se agrega para probar con agustin en miami","warehouseStockId":9}'
```
