---
jira_key: "POS-297"
aliases: ["POS-297"]
summary: "API - Créditos pendientes - Error al acreditar"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Guillermo Avila"
created: "2024-04-25 16:07"
updated: "2024-07-07 22:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-297"
---

# POS-297: API - Créditos pendientes - Error al acreditar

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Guillermo Avila |
| Creado | 2024-04-25 16:07 |
| Actualizado | 2024-07-07 22:02 |
| Etiquetas | ninguna |
| Jira | [POS-297](https://bluinc.atlassian.net/browse/POS-297) |

## Relaciones

- **Padre:** [[POS-24]] Creditos
- **blocks:** [[POS-291]] API - Refactor - en logica al realizar nota de credito según sucursal asignada al pedido

## Descripcion

Al intentar acreditar en créditos pendientes me aparece el siguiente error.

[adjunto]
```
curl 'https://gamma.api.aftersale.lio.red/v1/makeAftersalesCredits' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTQ0MTYyMTYsImF1ZCI6IjFhNGJiODQ0MjE3MDNmNmQxOTdhNzQ5Nzk0MTUxZDNhOTliYTM0OWQiLCJ1c2VyIjp7ImlkIjoiNjI4MTEiLCJjb2RlRlAiOiIwNDc5NzAiLCJwb3N0dmVudGEiOiIxIiwicG9zdHZlbnRhX2NyZWRpdG9zIjoiMSIsImFnZW50SWQiOiI1OCIsInBvc3R2ZW50YV9zb2x1Y2lvbiI6IjEiLCJwb3N0dmVudGFfYWRtaW4iOiIxIiwidXN1SWRlbnRpZmljYWNpb24iOm51bGwsIm1hbmFnZW1lbnQiOiIxIn0sImlhdCI6MTcxNDA3MTc1NiwibmJmIjoxNzE0MDcxNzU2fQ.xfd_vdPokzP8L2GwDV56JNXwWFCRIPAO5a2uF01o1GU' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://gamma.postventa.saftel.com' \
  -H 'Referer: https://gamma.postventa.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0' \
  -H 'sec-ch-ua: "Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw '{"afterSaleId":34663,"itemId":111454,"afterSaleDetailId":58456,"voucherTypeId":2,"clientId":44087,"trade":[{"units":1,"price":373.52,"ivaTax":10.5,"internalId":111454}]}'
```

---

Actualización 07/05/24
Intenté realizar la acreditación y me apareció lo siguiente. 

[adjunto]
Además de poder realizar la acreditación quizás estaría bueno identificar el porque no se está devolviendo el mensaje de error.
