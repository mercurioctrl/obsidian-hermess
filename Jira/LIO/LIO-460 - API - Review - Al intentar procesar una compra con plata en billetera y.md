---
jira_key: "LIO-460"
aliases: ["LIO-460"]
summary: "API - Review - Al intentar procesar una compra con plata en billetera y transferencia, no me deja hacerlo por un error de query (parece faltar alguna columna o haber un corrimiento)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-09-23 09:44"
updated: "2025-09-26 10:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-460"
---

# LIO-460: API - Review - Al intentar procesar una compra con plata en billetera y transferencia, no me deja hacerlo por un error de query (parece faltar alguna columna o haber un corrimiento)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-09-23 09:44 |
| Actualizado | 2025-09-26 10:27 |
| Etiquetas | ninguna |
| Jira | [LIO-460](https://bluinc.atlassian.net/browse/LIO-460) |

## Relaciones

- **Padre:** [[LIO-419]] Mejoras de pagos

## Descripcion

[adjunto]


```
curl 'https://api.gamma.libreopcion.com/pedidos/checkout/confirmar' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjp7ImlkIjoyLCJlbWFpbCI6Imhlcm1lc3M4N0BnbWFpbC5jb20iLCJub21icmUiOiJDYXRyaWVsIE1lcmN1cmlvbyIsInBlcmZpbCI6InZlbmRlZG9yIiwiZG9jdW1lbnRvIjoiMzM0NTc5NjIiLCJ0ZWxlZm9ubyI6IjQtNjM2LTM0MDYiLCJkaXJlY2Npb24iOnsiY2FsbGUiOiJNZWRpbmEiLCJudW1lcm8iOiIzNTEiLCJwaXNvIjoiMSIsImNhc2FBcHRvIjoiMyJ9LCJjb2RpZ29fcG9zdGFsIjoiMTQwOCIsImF2YXRhciI6MTIsImNpdWRhZCI6eyJpZCI6MjA4MzIsIm5vbWJyZSI6IkNBQkEiLCJwcm92aW5jaWFfaWQiOjEsInRvdGFsIjowfSwicHJvdmluY2lhIjp7ImlkIjoxLCJrZXkiOjEsIm5vbWJyZSI6IkNBQkEiLCJwYWlzX2lkIjo3LCJ0b3RhbCI6MCwiY2l1ZGFkX2RlZmVjdG9faWQiOjB9LCJwYWlzIjp7ImlkIjo3LCJub21icmUiOiJBUkdFTlRJTkEiLCJ0b3RhbCI6MH0sInRpZW5kYV9pZCI6MjY4MDYsInZlbmRlZG9yX2lkIjoyMiwidG9rZW5WNCI6IkZGRDMxNEZDLTJCMDQtNEVBMS04NTQ1LTk2QjZGNjZFNEEzQSIsImNvZGlnb19wb3N0YWxfZGVmYXVsdCI6MTQwNywiYWN0aXZlV2FsbGV0Ijp0cnVlfSwiaXNzIjoibGlicmVvcGNpb24uY29tIiwiYXVkIjoibGlicmVvcGNpb24uY29tIiwiaWF0IjoxNzU4NjMxMDEwLCJuYmYiOjE3NTg2MzEwMTB9.3h4j23sOL8549z-ywLm-FzmRyJ2k_1Fpz57qj4mGdz8' \
  -H 'Referer: https://gamma.libreopcion.com/mi-compra/confirmar?checkout=true&checkoutExpress=true' \
  -H 'sec-ch-ua: "Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Content-Type: application/json' \
  --data-raw '{"id":747096,"bulk":null,"quotes":{"deliveryTimeRange":"entre el lunes 22 y el viernes 26","deliveryDays":3}}'
```

```
{
    "error": {
        "code": 500,
        "message": "Internal Server Error: No se pudo confirmar tu compra, intente nuevamente. Error: Error insertando movimiento: SQLSTATE[42000]: [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]Error al convertir el tipo de datos nvarchar a float. SQL: INSERT INTO NEW_BYTES.dbo.MC_CCORRIENTES_MOVIMIENTOS ( ID_CCMOVIMIENTO, ID_CLIENTE, TR_CODIGO, CC_FECHAMOVIMIENTO, USU_IDENTIFICACION, REMITO_FP, SUCURSAL_REMITO, CC_IMPORTEUSD, CC_ANULADO, CC_OBSERVACIONES, CC_HORAMOVIMIENTO, CC_OBSERVACIONES2, COTIZACION, NROFACTURA, IMPORTE_PERCEPCION, PORC_PERCEPCION, fechaMovimiento, ID_PROCEDENCIA, PORC_INTTAX, HMAC, pending, idLo, showWallet ) VALUES ( '918286.0', '91245', 32, convert(varchar(10),getdate(),112), 'WALLETLO', NULL, NULL, 1.16, 'NO', 'Uso de dinero en compras', convert(varchar(8), getdate(), 108), NULL, 'Uso de dinero en compras', NULL, NULL, NULL, GETDATE(), NULL, 1325, 0, NULL, 'ddc52dc72d1c437bca85fc7affbd5e32fc88c1e84790b582d3c67ae4cdda1149', 747096 )"
    },
    "debug": {
        "source": "Pedidos.php:149 at call stage",
        "stages": {
            "success": [
                "get",
                "route",
                "negotiate",
                "validate"
            ],
            "failure": [
                "call",
                "message"
            ]
        }
    }
}
```
