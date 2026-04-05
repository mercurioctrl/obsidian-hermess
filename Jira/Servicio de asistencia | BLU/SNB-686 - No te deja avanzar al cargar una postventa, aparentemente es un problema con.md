---
jira_key: "SNB-686"
aliases: ["SNB-686"]
summary: "No te deja avanzar al cargar una postventa, aparentemente es un problema con una query y un tipo"
status: "Resuelta"
type: "Support"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "jtamagnone@nb.com.ar"
created: "2023-04-14 15:19"
updated: "2023-04-18 09:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-686"
---

# SNB-686: No te deja avanzar al cargar una postventa, aparentemente es un problema con una query y un tipo

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | jtamagnone@nb.com.ar |
| Creado | 2023-04-14 15:19 |
| Actualizado | 2023-04-18 09:35 |
| Etiquetas | ninguna |
| Jira | [SNB-686](https://bluinc.atlassian.net/browse/SNB-686) |

## Relaciones

*Sin relaciones*

## Descripcion

Por alguna razon no te deja avanzar cuando haces esto desde el front:



```
curl 'https://api.aftersale.lio.red/v1/createPreAfterSale' \
  -H 'Accept: application/json, text/plain, /' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODE1NjUyNTcsImF1ZCI6IjhhZDkyODM3MzA5YTg0M2QwOGNiZGYzN2VmYjg5ZDI4Y2NmN2M0YWUiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsInBvc3R2ZW50YSI6IjEiLCJwb3N0dmVudGFfY3JlZGl0b3MiOiIxIiwiYWdlbnRJZCI6IjEyIiwicG9zdHZlbnRhX3NvbHVjaW9uIjoiMSIsInBvc3R2ZW50YV9hZG1pbiI6IjEiLCJ1c3VJZGVudGlmaWNhY2lvbiI6IlNlYmEiLCJtYW5hZ2VtZW50IjoiMSJ9LCJpYXQiOjE2ODE0Nzg4NTcsIm5iZiI6MTY4MTQ3ODg1N30.wk0gTYVQKpNLc4ILa7BfViv6Wx78OgTyK4Llvi-45Vs' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://postventa.saftel.com' \
  -H 'Referer: https://postventa.saftel.com/preAfterSales?currentPage=1&itemsPerPage=50' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '{"clientId":"009456","userId":"66626","contactNumber":"01153694527","email":"mganzinelli@parquedelacosta.com.ar","details":{"productId":"116741","failTypeId":"5","failDescription":"se tilda. se reinicia 1153694527 mganzinelli@parquedelacosta.com.ar","quantity":1,"serialNumber":"sn2204060077","invoiceNumber":"0002454545"}}' \
  --compressed
```
