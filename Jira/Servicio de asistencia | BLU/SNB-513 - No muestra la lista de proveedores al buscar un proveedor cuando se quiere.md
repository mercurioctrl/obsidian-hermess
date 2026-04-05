---
jira_key: "SNB-513"
aliases: ["SNB-513"]
summary: "No muestra la lista de proveedores al buscar un proveedor cuando se quiere hacer un \"pago a proveedor\""
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Carla Luciana Carpintieri"
created: "2023-01-24 11:33"
updated: "2023-01-24 14:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-513"
---

# SNB-513: No muestra la lista de proveedores al buscar un proveedor cuando se quiere hacer un "pago a proveedor"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Carla Luciana Carpintieri |
| Creado | 2023-01-24 11:33 |
| Actualizado | 2023-01-24 14:08 |
| Etiquetas | ninguna |
| Jira | [SNB-513](https://bluinc.atlassian.net/browse/SNB-513) |

## Relaciones

*Sin relaciones*

## Descripcion

No muestra la lista de proveedores al buscar un proveedor cuando se quiere hacer un "pago a proveedor"

```
curl 'https://api.cashbox.lio.red/v1/providers/new?currentPage=1&itemsPerPage=15' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NzQ1NzU0MjUsImF1ZCI6ImJhNjY5YWZiNGUxOWNiNjRjNjRkODRjN2E1MjdmZjcyZDVhZjdlZjAiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImNvYnJvIjoiMSIsImNvYnJvQWRtaW4iOiIxIiwiYWdlbnRJZCI6IjEyIiwiYm94IjoiU2ViYSJ9LCJpYXQiOjE2NzQ1NjQ2MjUsIm5iZiI6MTY3NDU2NDYyNX0.64s2ek0cbsvSjYbP51mwXzA09c0ssIoa9ltzM_-8Fv8' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://caja.saftel.com' \
  -H 'Referer: https://caja.saftel.com/box/Seba?currentPage=1&itemsPerPage=15' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --compressed
```

El error en cuestion es:

```
"SQLSTATE[42S02]: [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]El nombre de objeto 'NEW_BYTES.dbo.providersBalance' no es v\u00e1lido. SQL: SELECT [ID_PROVEEDOR] as id, [CCODPRO] as providerCode, [cnompro] as name, [NombreComercial] as businessName, RTRIM([Direccion]) as addres, [Id_Pais] as countryId, [Id_Provincia] as provicenId, [Id_Ciudad] as localitieId, [Contacto] as contact, ISNULL((SELECT TOP 1 amount FROM NEW_BYTES.dbo.providersBalance WHERE providerId = F.ID_PROVEEDOR ORDER BY balanceDate DESC),0) + ISNULL(SaldoInicialCTA,0) as totSaldosaFavor, ISNULL(SaldoInicialCTA,0) as saldoInicialCTA, [AgentePercIVA] as agentePercIVA, [Id_CategoriaIVA] as ivaPercepction, [correo] as correo, [alicuotaIbb] as aliquotIbb FROM [NewBytes_DBF].[dbo].[FP_Proveedores] AS F WHERE [cnompro] LIKE '%new%' GROUP BY ID_PROVEEDOR,CCODPRO,cnompro,NombreComercial,Direccion,Id_Pais,Id_Provincia,Id_Ciudad,Contacto,SaldoInicialCTA,AgentePercIVA,Id_CategoriaIVA,correo,alicuotaIbb ORDER BY CCODPRO DESC OFFSET 0 rows FETCH next 15 rows only"
```
