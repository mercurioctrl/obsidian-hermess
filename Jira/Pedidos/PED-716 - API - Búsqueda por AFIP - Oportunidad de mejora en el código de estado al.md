---
jira_key: "PED-716"
aliases: ["PED-716"]
summary: "API - Búsqueda por AFIP - Oportunidad de mejora en el código de estado al mandar formato incorrecto"
status: "Finalizada"
type: "Tarea"
priority: "Lowest"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-05-13 14:56"
updated: "2024-05-14 11:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-716"
---

# PED-716: API - Búsqueda por AFIP - Oportunidad de mejora en el código de estado al mandar formato incorrecto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Lowest |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-05-13 14:56 |
| Actualizado | 2024-05-14 11:38 |
| Etiquetas | ninguna |
| Jira | [PED-716](https://bluinc.atlassian.net/browse/PED-716) |

## Relaciones

- **Padre:** [[PED-3 - Ordenes de compra|PED-3]] Ordenes de compra
- **relates to:** [[PED-715 - APP - Búsqueda por AFIP - Oportunidad de mejora al mostrar resultados no|PED-715]] APP - Búsqueda por AFIP - Oportunidad de mejora al mostrar resultados no encontrados

## Descripcion

Al mandarse la clave de identificación con el formato incorrecto, devuelve un código de estado 401 (Unauthorized) lo que provoca que se despliegue el modal de login en el front.
Como sugerencia lo cambiaría por el código de estado 400 (Bad Request).

[adjunto]
```
curl 'https://api.orders.lio.red/v1/clients/afip/40.122.663' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTU3MDU4OTQsImF1ZCI6ImMxMWRhYjU1ODk2ZGQwM2Q1ZTM5NDhhYWUzMjlhYzllYmE1MDllOGUiLCJ1c2VyIjp7ImlkIjo2MzY2OCwiY29kZUZQIjoiNTU1NTQiLCJhZ2VudElkIjo1OSwidXN1SWRlbnRpZmljYWNpb24iOm51bGwsInBlZGlkb3MiOjEsInBtIjowLCJkaXNjb3VudFNoaXBwaW5nIjoxLCJyZWJpbGwiOjB9LCJpYXQiOjE3MTU2MTk0OTQsIm5iZiI6MTcxNTYxOTQ5NH0.4wlueEfddWnkVqybtlnlMsqnvzpt07S0t2DrZKEmfmY' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://pedidos.saftel.com' \
  -H 'Referer: https://pedidos.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0' \
  -H 'sec-ch-ua: "Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"'
```
