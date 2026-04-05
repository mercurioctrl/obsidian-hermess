---
jira_key: "SNB-1472"
aliases: ["SNB-1472"]
summary: "Error al intentar realizar una compra en LO"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-01-30 11:24"
updated: "2024-02-07 20:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/SNB-1472"
---

# SNB-1472: Error al intentar realizar una compra en LO

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-01-30 11:24 |
| Actualizado | 2024-02-07 20:41 |
| Etiquetas | ninguna |
| Jira | [SNB-1472](https://bluinc.atlassian.net/browse/SNB-1472) |

## Relaciones

*Sin relaciones*

## Descripcion

```
"Internal Server Error: No se pudo confirmar tu compra, intente nuevamente. Error: No se pudieron generar las multiples ordenes de compra. Error: SQLSTATE[42000]: [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]Sintaxis incorrecta cerca de la palabra clave 'SELECT'. SQL: INSERT INTO [NewBytes_DBF].[dbo].[pedclit] ( cnumped, dfecped, ccodcli, cidendir, ccodalm, cestado, dfecent, csuped, ccondent, cexped, cobserv, ccodpago, nbultos, nportes, ccodage, ncomision, linternet, ccoddiv, nvaldiv, ccodtrans, cnumsuc, lbienuso, lanula, ndtoesp, nmontoesp, ndpp, nmotopp, codigoPedido, ID_VENDEDOR, ID_ALMACEN, ID_CLIENTE, ID_FORMADEPAGO, ID_MONEDA, ID_TRANSPORTISTA, ID_ESTADOPEDIDOCLI, ID_NROPEDCLI_ENC, cdirentrega, ID_Sucursal, ccodage_creador, label, idDirCliNbWeb, orderTypeId, idLo, medioEnvioId ) VALUES ( REPLACE(STR((SELECT MAX(cnumped) + 1 FROM [NewBytes_DBF].[dbo].pedclit), 8), SPACE(1), '0'), GETDATE(), '080585', '0', 'SAF', 'P', GETDATE(), '', '', '', 'PEDIDO LIBRE OPCION', 'CO', 0, 0.000, '100', 0.00, 1, 'DOL', (SELECT cotizacion FROM [LO].[dbo].[pedidosCabecera] WHERE id = 573772), '', '0002', 0, 0, 0.00, 0.000, 0.00, 0.000, NULL, 100, 2, 32103, SELECT (SELECT ID_FORMA FROM NEW_BYTES.dbo.MS_FORMASPAGO_REMITOS_VENDEDORES where medioPagoIdLo = medioPagoElegidoID ) FROM [LO].[dbo].[pedidosCabeceraPaquete] where pedidoCabeceraID = 573772, 1, NULL, 1, (SELECT MAX(cnumped) + 1 FROM [NewBytes_DBF].[dbo].pedclit), NULL, 2, '100', NULL, '26466', 5, 573772, (SELECT medioEnvioElegidoID FROM [LO].[dbo].[pedidosCabeceraPaquete] where pedidoCabeceraID = 573772) );"
```

```
curl 'https://api.gamma.libreopcion.com/pedidos/checkout/confirmar' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjp7ImlkIjoyMzgwNDAsImVtYWlsIjoiZ2F2aWxhQG5iLmNvbS5hciIsIm5vbWJyZSI6Ikd1aWxsZXJtbyIsInBlcmZpbCI6InZlbmRlZG9yIiwiZG9jdW1lbnRvIjoiMDEyMzQ1NjciLCJ0ZWxlZm9ubyI6IjQ0MjYwMjI1OTEiLCJkaXJlY2Npb24iOnsiY2FsbGUiOiJMQSBDQVJBTUJBREEiLCJudW1lcm8iOiJMQSBDQVJBTUJBREEiLCJwaXNvIjoiTEEgQ0FSQU1CQURBIiwiY2FzYUFwdG8iOiJMQSBDQVJBTUJBREEifSwiY29kaWdvX3Bvc3RhbCI6IjEwMDAiLCJhdmF0YXIiOjcsImNpdWRhZCI6eyJpZCI6NCwibm9tYnJlIjoiQUJBU1RPIiwicHJvdmluY2lhX2lkIjoyLCJ0b3RhbCI6MH0sInByb3ZpbmNpYSI6eyJpZCI6Miwia2V5IjoyLCJub21icmUiOiJCVUVOT1MgQUlSRVMiLCJwYWlzX2lkIjo3LCJ0b3RhbCI6MCwiY2l1ZGFkX2RlZmVjdG9faWQiOjB9LCJwYWlzIjp7ImlkIjo3LCJub21icmUiOiJBUkdFTlRJTkEiLCJ0b3RhbCI6MH0sInRpZW5kYV9pZCI6MCwidmVuZGVkb3JfaWQiOjIwNjMxNn0sImlzcyI6ImxpYnJlb3BjaW9uLmNvbSIsImF1ZCI6ImxpYnJlb3BjaW9uLmNvbSIsImlhdCI6MTcwNDgyNTY1NCwibmJmIjoxNzA0ODI1NjU0fQ.-P63TT2OKgbsl25l2uZFs8YS2ts2s_Up5GjatdqR5cg' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://gamma.libreopcion.com' \
  -H 'Referer: https://gamma.libreopcion.com/mi-compra/confirmar?checkout=true&checkoutExpress=false' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0' \
  -H 'sec-ch-ua: "Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw '{"id":573772}' \
  --compressed
```
