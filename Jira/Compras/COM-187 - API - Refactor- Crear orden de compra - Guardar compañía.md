---
jira_key: "COM-187"
aliases: ["COM-187"]
summary: "API - Refactor- Crear orden de compra -> Guardar compañía "
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2025-05-13 14:45"
updated: "2025-06-02 18:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-187"
---

# COM-187: API - Refactor- Crear orden de compra -> Guardar compañía 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2025-05-13 14:45 |
| Actualizado | 2025-06-02 18:42 |
| Etiquetas | ninguna |
| Jira | [COM-187](https://bluinc.atlassian.net/browse/COM-187) |

## Relaciones

- **relates to:** [[COM-111 - API - Feat - Crear orden de compra|COM-111]] API - Feat - Crear orden de compra

## Descripcion

Al crear una orden, por alguna razón no se guarda el `companyCode`. Es probable que al introducir este nuevo parámetro solo se haya utilizado para obtenerlo, pero no para almacenarlo.

```
curl 'https://gamma.api.purchases.lio.red/v1/providerOrder' -X POST -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0' -H 'Accept: application/json, text/plain, */*' -H 'Accept-Language: es-MX' -H 'Accept-Encoding: gzip, deflate, br, zstd' -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDcxNjE3MDAsImF1ZCI6IjMyNzE2MWNjOTRkMjczMTMzYmJiYjcxNTJkMGQ2OWU2OWJlYTQ4MzQiLCJ1c2VyIjp7ImlkIjoiNzY2MzEiLCJjb2RlRlAiOiI4Mzc2NCIsImFnZW50SWQiOiI2NyIsInVzdUlkZW50aWZpY2FjaW9uIjpudWxsLCJjb21wcmFzIjoiMSIsInBtIjoiMSIsImNvbXBhbnlDb2RlIjoiMTEifSwiaWF0IjoxNzQ3MTU4MTAwLCJuYmYiOjE3NDcxNTgxMDB9.31z_XTw5tr9iqk0Z1qJC6BncO_WOqQspWBqEpu4jsZo' -H 'Content-Type: application/json' -H 'Origin: https://gamma.compras.saftel.com' -H 'Connection: keep-alive' -H 'Referer: https://gamma.compras.saftel.com/' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: cross-site' -H 'Priority: u=0' --data-raw '{"provider":476,"primaryProvider":null}'
```

[adjunto]
```
SELECT
	ccodage_creador,
    companyCode,
	'',
	*
FROM NewBytes_DBF.dbo.pedprot
WHERE nNumPed = 11246
```

[adjunto]
