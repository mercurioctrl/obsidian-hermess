---
jira_key: "EXP-510"
aliases: ["EXP-510"]
summary: "API - Obtener seriales en xlsx -> Propuesta de mejora al visualizar ingreso sin artículos "
status: "Finalizada"
type: "Subtarea"
priority: "Lowest"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2025-09-15 20:47"
updated: "2025-12-05 05:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-510"
---

# EXP-510: API - Obtener seriales en xlsx -> Propuesta de mejora al visualizar ingreso sin artículos 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Lowest |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2025-09-15 20:47 |
| Actualizado | 2025-12-05 05:53 |
| Etiquetas | ninguna |
| Jira | [EXP-510](https://bluinc.atlassian.net/browse/EXP-510) |

## Relaciones

- **Padre:** [[EXP-486 - Ver ingreso|EXP-486]] Ver ingreso

## Descripcion

Me gustaría proponer como mejora que la respuesta del backend, en caso de no existir elementos en el ingreso, se envíe contenida en un objeto JSON. Esto permitirá que el frontend pueda interpretarla correctamente.

```
{
  "success": true,                    // true o false
  "message": "Operación exitosa",     // Descripción opcional
  "data": {}                          // Objeto con datos devueltos o null
}
```

[adjunto]
```
curl.exe ^"https://gamma.api.warehouse.lio.red/v1/providersOrders/00012227/xlsx^" ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:142.0) Gecko/20100101 Firefox/142.0^" ^
  -H ^"Accept: application/json, text/plain, */*^" ^
  -H ^"Accept-Language: es-MX^" ^
  -H ^"Accept-Encoding: gzip, deflate, br, zstd^" ^
  -H ^"Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NTgwMTU1NjQsImF1ZCI6ImQzNTllM2I2ZTU0NTBkZmI3ZTJlMTMyZDkyZTY3YzVjNDc2NTE1Y2IiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImFnZW50SWQiOiIxMiIsInVzdUlkZW50aWZpY2FjaW9uIjoiU2ViYSIsImV4cGVkaWNpb24iOiIxIiwiZXhwZWRpY2lvbkFkbWluIjoiMSIsIm1hbmFnZW1lbnQiOiIxIiwiZXhwX3VwbG9hZF9zZXJpYWxzIjoiMSIsImV4cF9pdGVtcyI6IjEiLCJjb21wYW55Q29kZSI6bnVsbH0sImlhdCI6MTc1Nzk3OTI2NCwibmJmIjoxNzU3OTc5MjY0fQ.8oI4Mw7yi1ANQt9pSL_okfIZOvU-2Y5WWY2h51kmroE^" ^
  -H ^"Origin: https://gamma.expedicion.saftel.com^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Referer: https://gamma.expedicion.saftel.com/^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: cross-site^"
```
