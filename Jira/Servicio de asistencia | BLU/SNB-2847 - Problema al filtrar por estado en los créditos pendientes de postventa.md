---
jira_key: "SNB-2847"
aliases: ["SNB-2847"]
summary: "Problema al filtrar por estado en los créditos pendientes de postventa"
status: "Resuelta"
type: "Support"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Catriel Mercurio"
created: "2025-03-05 16:42"
updated: "2025-09-04 10:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-2847"
---

# SNB-2847: Problema al filtrar por estado en los créditos pendientes de postventa

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-05 16:42 |
| Actualizado | 2025-09-04 10:16 |
| Etiquetas | ninguna |
| Jira | [SNB-2847](https://bluinc.atlassian.net/browse/SNB-2847) |

## Relaciones

*Sin relaciones*

## Descripcion

```
curl 'https://api.aftersale.lio.red/v1/afterSalesCredits/find/coradir?currentPage=1&itemsPerPage=50&testStatus=2' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDEyNzk1MDIsImF1ZCI6ImM3MDU1MWU5ZjQxOTJjMGY0ZDg5ZWFiYWRjNDk5MjYyMmUyZGYwZjkiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsInBvc3R2ZW50YSI6IjEiLCJwb3N0dmVudGFfY3JlZGl0b3MiOiIxIiwiYWdlbnRJZCI6IjEyIiwicG9zdHZlbnRhX3NvbHVjaW9uIjoiMSIsInBvc3R2ZW50YV9hZG1pbiI6IjEiLCJ1c3VJZGVudGlmaWNhY2lvbiI6IlNlYmEiLCJtYW5hZ2VtZW50IjoiMSJ9LCJpYXQiOjE3NDExOTMxMDIsIm5iZiI6MTc0MTE5MzEwMn0._MM197LMkN65ynxIj2H5Rc7nn6eZ1qBhrvbW4Fl50SU' \
  -H 'Referer: https://postventa.saftel.com/afterSalesCredits/coradir?currentPage=1&itemsPerPage=50&testStatus=2' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'sec-ch-ua: "Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"' \
  -H 'sec-ch-ua-mobile: ?0'
```
