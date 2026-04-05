---
jira_key: "COB-450"
aliases: ["COB-450"]
summary: "API - Review - Listado de cobros pendientes algunos problemas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-07-07 08:21"
updated: "2023-07-09 20:54"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-450"
---

# COB-450: API - Review - Listado de cobros pendientes algunos problemas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-07-07 08:21 |
| Actualizado | 2023-07-09 20:54 |
| Etiquetas | ninguna |
| Jira | [COB-450](https://bluinc.atlassian.net/browse/COB-450) |

## Relaciones

- **Padre:** [[COB-357]] Feat - Listar Despachados, pendientes a cobrar
- **blocks:** [[SNB-944]] se cambió de columna un pedido jajajaj

## Descripcion

De un tiempo a estar parte observamos que en el listado de cobros pendientes existen algunos issues que listo a continuacion

### 1 - El numero de la pestaña y los pedidos que se muestran no coinciden 

[adjunto]
## 2- Existe algun problema con las busqyedas, ya que la misma parece no funcionar y tampoco su paginado ver ejemplo aca abajo:



```
curl 'https://api.cashbox.lio.red/v1/pendingCharges/cabrera?currentPage=1&itemsPerPage=100' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODg3Mzk0MTUsImF1ZCI6ImYxOTYwMDdjOTc3NDg4YjQyZGI3OThlMzFkNmZkNmFhMjZkMDMyNzIiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImNvYnJvIjoiMSIsImNvYnJvQWRtaW4iOiIxIiwiYWdlbnRJZCI6IjEyIiwiYm94IjoiU2ViYSIsIm1hbmFnZW1lbnQiOiIxIiwiZWRpdF9jcmVkaXQiOiIxIn0sImlhdCI6MTY4ODcyODYxNSwibmJmIjoxNjg4NzI4NjE1fQ.MSv840tq4up23mL9YPYGY186w2uPRbfxp0O9J8wcGnc' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://caja.saftel.com' \
  -H 'Referer: https://caja.saftel.com/pendingCharges/cabrera?currentPage=1&itemsPerPage=100' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --compressed
```
