---
jira_key: "COM-101"
aliases: ["COM-101"]
summary: "API - Agregar/editar posiciones arancelarias - Valores no coincidentes"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-05-24 18:54"
updated: "2024-06-05 18:00"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-101"
---

# COM-101: API - Agregar/editar posiciones arancelarias - Valores no coincidentes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-05-24 18:54 |
| Actualizado | 2024-06-05 18:00 |
| Etiquetas | ninguna |
| Jira | [COM-101](https://bluinc.atlassian.net/browse/COM-101) |

## Relaciones

- **relates to:** [[COM-88 - API - Feat - Patch para agregar posiciones arancelarias externas a las locales|COM-88]] API - Feat - Patch para agregar posiciones arancelarias externas a las locales o en su defecto agregar la descripcion de las posiciones arancelarias a la orden

## Descripcion

1. Después de actualizar una posición arancelaria y hacer la solicitud para obtener el detalle de la orden, los valores retornados no coinciden con los guardados.

[adjunto]
[adjunto]
```
curl 'https://gamma.api.purchases.lio.red/v1/providerOrder/11082' \
  -X 'PATCH' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTY1OTMxNTcsImF1ZCI6ImQ3MmUxZDQ2OWUwMGM0ZTlhNjc2MGIxYTZkNmYxY2IwNTZhYjY4ZmUiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImFnZW50SWQiOiIxMiIsInVzdUlkZW50aWZpY2FjaW9uIjoiU2ViYSIsInBlZGlkb3MiOiIxIiwicG0iOiIxIn0sImlhdCI6MTcxNjU4OTU1NywibmJmIjoxNzE2NTg5NTU3fQ.sIzYStYdzbiNQd2KCcAKytvUbJqtGFdlLlf6uwkryPU' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://gamma.compras.saftel.com' \
  -H 'Referer: https://gamma.compras.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0' \
  -H 'sec-ch-ua: "Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw '{"id":102141,"position":"0709.70.00.000L","amount":18,"price":{"value":25,"iva":10.5}}'
```



2. Al buscar una posición arancelaria en especifico me devuelve dos, sin embargo, es la misma

[adjunto]


3. Al editar una posición arancelaria, la selección de la categoría (descripción) no coincide con la almacenada.

[adjunto]
[adjunto]
```
curl 'https://gamma.api.purchases.lio.red/v1/tariffPosition' \
  -X 'PATCH' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTY1OTMxNTcsImF1ZCI6ImQ3MmUxZDQ2OWUwMGM0ZTlhNjc2MGIxYTZkNmYxY2IwNTZhYjY4ZmUiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImFnZW50SWQiOiIxMiIsInVzdUlkZW50aWZpY2FjaW9uIjoiU2ViYSIsInBlZGlkb3MiOiIxIiwicG0iOiIxIn0sImlhdCI6MTcxNjU4OTU1NywibmJmIjoxNzE2NTg5NTU3fQ.sIzYStYdzbiNQd2KCcAKytvUbJqtGFdlLlf6uwkryPU' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://gamma.compras.saftel.com' \
  -H 'Referer: https://gamma.compras.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0' \
  -H 'sec-ch-ua: "Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw '{"position":"0709.70.00.000L","description":"-Espinacas (incluida la de Nueva Zelanda) y  armuelles","categoryId":19,"taxPosition":[{"description":"AEC","value":"22"},{"description":"IIBB","value":"87"},{"description":"IVA","value":"96"},{"description":"IVA AD","value":"92"},{"description":"Ganancias","value":"46"},{"description":"TE","value":"98"},{"description":"DII","value":"16"},{"description":"DIE","value":"55"}]}'
```
