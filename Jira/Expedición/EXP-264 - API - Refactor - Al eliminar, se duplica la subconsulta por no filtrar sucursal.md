---
jira_key: "EXP-264"
aliases: ["EXP-264"]
summary: "API - Refactor - Al eliminar, se duplica la subconsulta por no filtrar sucursal"
status: "Gamma"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-03-30 08:24"
updated: "2023-03-30 10:37"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-264"
---

# EXP-264: API - Refactor - Al eliminar, se duplica la subconsulta por no filtrar sucursal

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-30 08:24 |
| Actualizado | 2023-03-30 10:37 |
| Etiquetas | ninguna |
| Jira | [EXP-264](https://bluinc.atlassian.net/browse/EXP-264) |

## Relaciones

- **Padre:** [[EXP-15]] Feat - Serializar salida

## Descripcion

Al realizar 

```
curl 'https://api.warehouse.lio.red/v1/orders/X001000021234/serials/117841' \
  -X 'DELETE' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-US,es-419;q=0.9,es;q=0.8,gl;q=0.7,en;q=0.6' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODAxODQ2OTcsImF1ZCI6IjY3MTdjYmI5ZDIyOGNiNThkNjY5YTQ1MDAwZjExNmM4ZTZkOGE4NjgiLCJ1c2VyIjp7ImlkIjoiNzQ2MyIsImNvZGVGUCI6IjAxOTIyNyIsImFnZW50SWQiOiIxMiIsInVzdUlkZW50aWZpY2FjaW9uIjoiU2ViYSIsImV4cGVkaWNpb24iOiIxIiwiZXhwZWRpY2lvbkFkbWluIjoiMSIsIm1hbmFnZW1lbnQiOiIxIn0sImlhdCI6MTY4MDE3Mzg5NywibmJmIjoxNjgwMTczODk3fQ.IP-JkYqX0FZLxox2RBqCxpkJwIPPmeuz9ZJlWw2SCqQ' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://expedicion.saftel.com' \
  -H 'Referer: https://expedicion.saftel.com/shipments/00021234?currentPage=1&itemsPerPage=300' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw '[{"serials":["1178411612220038"]}]' \
  --compressed
```

Se obtiene el mensaje

```
"SQLSTATE[21000]: [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]La subconsulta ha devuelto m\u00e1s de un valor, lo que no es correcto cuando va a continuaci\u00f3n de =, !=, <, <=, >, >= o cuando se utiliza como expresi\u00f3n. SQL: SELECT SERIAL as serial, D_SALIDA.HORA_EXACTA as admissionDate, ( SELECT authorizedDate FROM NEW_BYTES.dbo.ST_REMITOS_VENTA_CABECERA_SALIDA C_SALIDA WHERE C_SALIDA.REMITO_FP = D_SALIDA.REMITO_FP ) as dispatchDate FROM [NEW_BYTES].[dbo].ST_REMITOS_VENTA_DETALLE_SALIDA D_SALIDA WHERE D_SALIDA.REMITO_FP = '00021234' AND D_SALIDA.CREF = (SELECT cRef FROM NewBytes_DBF.dbo.articulo WHERE ID_ARTICULO = '117841' )"
```

Al hacer 

```
SELECT * FROM NEW_BYTES.dbo.ST_REMITOS_VENTA_CABECERA_SALIDA C_SALIDA
WHERE C_SALIDA.REMITO_FP = '00021234'
```

se observan dos registros, por lo cual, la subconsulta que se encuentra en el select para dispatcht date debneria filtrar sucursal para solucionar el problema.
