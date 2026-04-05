---
jira_key: "COM-133"
aliases: ["COM-133"]
summary: "API - Review - No se guarda si intento quitar una posicion arancelaria para un producto"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-08-06 09:38"
updated: "2024-08-08 04:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-133"
---

# COM-133: API - Review - No se guarda si intento quitar una posicion arancelaria para un producto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-06 09:38 |
| Actualizado | 2024-08-08 04:48 |
| Etiquetas | ninguna |
| Jira | [COM-133](https://bluinc.atlassian.net/browse/COM-133) |

## Relaciones

- **Padre:** [[COM-77]] Editar orden de compra

## Descripcion

```
curl 'https://gamma.api.purchases.lio.red/v1/providerOrder/11200' \
  -X 'PATCH' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MjI5NTAzNTksImF1ZCI6IjVlYjEyMzZlYzQ5ZGRlMWMyZGRhYjA3MDdiNDBlNTM0ZTgwNmQ1NWEiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImFnZW50SWQiOiIxMiIsInVzdUlkZW50aWZpY2FjaW9uIjoiU2ViYSIsImNvbXByYXMiOiIxIiwicG0iOiIxIn0sImlhdCI6MTcyMjk0Njc1OSwibmJmIjoxNzIyOTQ2NzU5fQ.dbXfofPMbDViQjUVP6OMTFFtT3_akAqcfWHWgRpV9rQ' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://gamma.compras.saftel.com' \
  -H 'Referer: https://gamma.compras.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36' \
  -H 'ngrok-skip-browser-warning: true' \
  -H 'sec-ch-ua: "Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '{"id":100682,"position":null,"amount":5,"price":{"value":20,"iva":10.5}}'
```
