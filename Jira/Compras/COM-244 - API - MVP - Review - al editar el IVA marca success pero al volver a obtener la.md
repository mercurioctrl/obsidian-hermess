---
jira_key: "COM-244"
aliases: ["COM-244"]
summary: "API - MVP - Review - al editar el IVA marca success pero al volver a obtener la orden no se modificó"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Marbe Moreno"
created: "2025-10-21 14:10"
updated: "2025-11-25 12:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-244"
---

# COM-244: API - MVP - Review - al editar el IVA marca success pero al volver a obtener la orden no se modificó

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Marbe Moreno |
| Creado | 2025-10-21 14:10 |
| Actualizado | 2025-11-25 12:59 |
| Etiquetas | ninguna |
| Jira | [COM-244](https://bluinc.atlassian.net/browse/COM-244) |

## Relaciones

- **Padre:** [[COM-38 - Ver orden de compra|COM-38]] Ver orden de compra

## Descripcion

```
curl 'https://gamma.api.purchases.lio.red/v1/providerOrder/12304' \
  -X 'PATCH' \
  -H 'Accept: application/json, text/plain, /' \
  -H 'Accept-Language: en-US,en;q=0.9,es-ES;q=0.8,es;q=0.7' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NjEwNzAxMzIsImF1ZCI6IjUxY2M3NDliN2VmMWMzZTNhMjJhMmVhYTdkOWIwODQ4ZTUwMDNmZTUiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImFnZW50SWQiOiIxMiIsInVzdUlkZW50aWZpY2FjaW9uIjoiU2ViYSIsImNvbXByYXMiOiIxIiwicG0iOiIxIiwiY29tcGFueUNvZGUiOiI0In0sImlhdCI6MTc2MTA2NjUzMiwibmJmIjoxNzYxMDY2NTMyfQ.R9_A_zM0SYqGj00Xeh8Tg43TFTvxD2qUU2-SpH3Flgc' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://gamma.compras.saftel.com' \
  -H 'Pragma: no-cache' \
  -H 'Referer: https://gamma.compras.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '{"id":115876,"amount":1,"price":{"value":0,"iva":"15"},"position":null}'
```

y al obtenerlo vuelvo a tener el marcado por default


[adjunto]
