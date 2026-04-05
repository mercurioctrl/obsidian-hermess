---
jira_key: "SNB-3819"
aliases: ["SNB-3819"]
summary: "Revisar en INV si hay algun problema con el servidor de imagen al subir una imagen principal"
status: "Esperando por ayuda"
type: "Error"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Marbe Moreno"
created: "2026-03-18 14:28"
updated: "2026-03-18 15:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-3819"
---

# SNB-3819: Revisar en INV si hay algun problema con el servidor de imagen al subir una imagen principal

| Campo | Valor |
|-------|-------|
| Estado | Esperando por ayuda (En curso) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Marbe Moreno |
| Creado | 2026-03-18 14:28 |
| Actualizado | 2026-03-18 15:51 |
| Etiquetas | ninguna |
| Jira | [SNB-3819](https://bluinc.atlassian.net/browse/SNB-3819) |

## Relaciones

*Sin relaciones*

## Descripcion

[adjunto]
Adjunto video para ver como replicar el problema, 
1- seleccionar img principal ,

2-elegir la imagen 

3- Muestra success

4- recargar → muestra sin imagen



y si se hizo el

 curl '[https://api.inventory.lio.red/item/122495'](https://api.inventory.lio.red/item/122495') \
  -X 'PATCH' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: en-US,en;q=0.9,es-ES;q=0.8,es;q=0.7' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NzM5MjMwOTcsInVzdWFyaW8iOjYyNjI2fQ.5Vtdg99cSJlRF8uMeCXMM1U9_vkwNfiDGHy6ly-1V7c' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: [https://inventario.saftel.com'](https://inventario.saftel.com') \
  -H 'Referer: [https://inventario.saftel.com/'](https://inventario.saftel.com/') \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '{"mainImage":"[http://static.nb.com.ar/img/dc84db1eaea0b1bd6f3851aa3dbc7468.jpg](http://static.nb.com.ar/img/dc84db1eaea0b1bd6f3851aa3dbc7468.jpg)"}'



pero despues q recargo y no viene si realizo de nuevo ese curl si queda asignado (lo hago desde el radiobutton)
