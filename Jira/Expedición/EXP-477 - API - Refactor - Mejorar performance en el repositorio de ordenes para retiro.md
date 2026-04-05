---
jira_key: "EXP-477"
aliases: ["EXP-477"]
summary: "API - Refactor - Mejorar performance en el repositorio de ordenes para retiro"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-02-14 09:30"
updated: "2025-02-19 17:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-477"
---

# EXP-477: API - Refactor - Mejorar performance en el repositorio de ordenes para retiro

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-14 09:30 |
| Actualizado | 2025-02-19 17:51 |
| Etiquetas | ninguna |
| Jira | [EXP-477](https://bluinc.atlassian.net/browse/EXP-477) |

## Relaciones

- **Padre:** [[EXP-7 - Despacho de retiros|EXP-7]] Despacho de retiros
- **has action item:** [[SNB-2779 - Muy lento sector expedicion armado finalizado|SNB-2779]] Muy lento sector expedicion armado finalizado

## Descripcion

Intentaremos cumplir la regla de los 2 segundos para el caso de este repositorio, en producción, con los siguientes filtros,

Si bien el motivo viene por una demora producida por algún problema en los despachos y el aumento en la cantidad de items, es un buen momento para revisar la performance del recurso.

```
GET {API_URL}/v1/pickUp?currentPage=1&itemsPerPage=300&status=2,11,10,4
```

```
curl 'https://api.warehouse.lio.red/v1/pickUp?currentPage=1&itemsPerPage=300&status=2,11,10,4' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3Mzk2MTkyMDksImF1ZCI6IjlkYjc3ZmI1NTkyMTg0YTkxMGFkYTU0NDdhOTZkYzgyMWU4Nzc3OTIiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImFnZW50SWQiOiIxMiIsInVzdUlkZW50aWZpY2FjaW9uIjoiU2ViYSIsImV4cGVkaWNpb24iOiIxIiwiZXhwZWRpY2lvbkFkbWluIjoiMSIsIm1hbmFnZW1lbnQiOiIxIiwiZXhwX3VwbG9hZF9zZXJpYWxzIjoiMSIsImV4cF9pdGVtcyI6IjEiLCJjb21wYW55Q29kZSI6bnVsbH0sImlhdCI6MTczOTUzNjQwOSwibmJmIjoxNzM5NTM2NDA5fQ.kn3YSbL1qYpaZ8U_sveso1SRBsYYwRIDaq1WMkDTv58' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://expedicion.saftel.com' \
  -H 'Referer: https://expedicion.saftel.com/pickUp?currentPage=1&itemsPerPage=300&status=2,11,10,4' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"'
```
