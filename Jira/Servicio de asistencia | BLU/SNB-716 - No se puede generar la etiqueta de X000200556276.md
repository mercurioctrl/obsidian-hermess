---
jira_key: "SNB-716"
aliases: ["SNB-716"]
summary: "No se puede generar la etiqueta de X000200556276"
status: "Resuelta"
type: "Support"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-04-27 12:28"
updated: "2023-04-27 13:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-716"
---

# SNB-716: No se puede generar la etiqueta de X000200556276

| Campo | Valor |
|-------|-------|
| Estado | Resuelta (Listo) |
| Tipo | Support |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-04-27 12:28 |
| Actualizado | 2023-04-27 13:15 |
| Etiquetas | ninguna |
| Jira | [SNB-716](https://bluinc.atlassian.net/browse/SNB-716) |

## Relaciones

*Sin relaciones*

## Descripcion

Se obtiene 

```
{"Andreani":{"state":"Error de validaci\u00f3n","message":"No se encuentran sucursales para los filtros ingresados"}}

```

Al hacer

```
curl 'https://api.warehouse.lio.red/v1/shipments/addTrackingOrder' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODI2MTk4NjMsImF1ZCI6ImI3NWU2MTk2ZTZiM2UwMmQwMWQ5ZWU2YjFlMzkxZDAzN2IxZDcxM2MiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImFnZW50SWQiOiIxMiIsInVzdUlkZW50aWZpY2FjaW9uIjoiU2ViYSIsImV4cGVkaWNpb24iOiIxIiwiZXhwZWRpY2lvbkFkbWluIjoiMSIsIm1hbmFnZW1lbnQiOiIxIn0sImlhdCI6MTY4MjYwOTA2MywibmJmIjoxNjgyNjA5MDYzfQ.f95ztOeX40oRm7seGMV5MYlNJX-Sem5xbfj-65IcWDQ' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://expedicion.saftel.com' \
  -H 'Referer: https://expedicion.saftel.com/shipments/00556276?currentPage=1&itemsPerPage=300' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '{"branch":"0002","order":"10311358","packageGroup":1,"idDirCliNbWeb":20736}' \
  --compressed
```

[adjunto]
