---
jira_key: "PED-702"
aliases: ["PED-702"]
summary: "API - Autorizar pedido liquidado con comprobante y de LO - Datos del comprobante completos"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-04-29 00:42"
updated: "2024-04-30 14:04"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-702"
---

# PED-702: API - Autorizar pedido liquidado con comprobante y de LO - Datos del comprobante completos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-04-29 00:42 |
| Actualizado | 2024-04-30 14:04 |
| Etiquetas | ninguna |
| Jira | [PED-702](https://bluinc.atlassian.net/browse/PED-702) |

## Relaciones

- **Padre:** [[PED-3]] Ordenes de compra
- **blocks:** [[PED-691]] API - Autorizar pedido (cobrar) liquidado si tiene el comprobante guardado y si es de libre opcion

## Descripcion

Al intentar autorizar el pedido me aparece la siguiente advertencia, sin embargo, se puede visualizar que los datos del comprobante están completos.

[adjunto]
```
curl 'https://gamma.api.orders.lio.red/v1/paymentForBank' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTQzNjQ3NTQsImF1ZCI6IjFlOWI2MGQ5NmM0YTRlOWFhMmEyODgyZWEwZDFhZWQ0YmEzOTA1ZWEiLCJ1c2VyIjp7ImlkIjo3NDYzLCJjb2RlRlAiOiIwMTkyMjciLCJhZ2VudElkIjoxMiwidXN1SWRlbnRpZmljYWNpb24iOiJTZWJhIiwicGVkaWRvcyI6MSwicG0iOjEsImRpc2NvdW50U2hpcHBpbmciOjEsInJlYmlsbCI6MX0sImlhdCI6MTcxNDM2MTE1NCwibmJmIjoxNzE0MzYxMTU0fQ.KuRU5EHUiDFaOC7VIpJq0S2TYd3auyipwuEWWCZQLAk' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://gamma.pedidos.saftel.com' \
  -H 'Referer: https://gamma.pedidos.saftel.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0' \
  -H 'sec-ch-ua: "Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw '{"pedido":"X000200569125","transferAmount":"45833.84"}'
```


Dato extra:
Dándole un vistazo más a profundidad este error devuelto, me parece que es debido a que no se encuentra el dato `documento` en la tabla `NB_WEB.dbo.pedidosCabeceraComprobantePago`

[adjunto]
Nota:

Agregaré el dato `documento` al pedido manualmente para seguir con la prueba.
