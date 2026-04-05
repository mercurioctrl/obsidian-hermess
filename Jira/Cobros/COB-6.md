---
jira_key: "COB-6"
summary: "API - Feat -  Obtener saldos de un cliente"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-07-14 14:05"
updated: "2022-10-20 17:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-6"
---

# COB-6: API - Feat -  Obtener saldos de un cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-14 14:05 |
| Actualizado | 2022-10-20 17:09 |
| Etiquetas | ninguna |
| Jira | [COB-6](https://bluinc.atlassian.net/browse/COB-6) |

## Descripción

Este recurso sirve para leer los limtes, usados y no usados de la cuenta corriente del cliente. Es decir el monto disponible en descubierto y el utilizado. Tambien el de cheques,

```
GET {API_RUL}/v1/balances/{clientId}
```

Retorna

```
[
  {
    "limitCheckBalanceAmount": 2004252.04,
    "usedCheckBalanceAmount": 2004252.04,
    "limitBalanceAmount": 2000.0,
    "usedBalanceAmount": 122.06
  }
]
```



Usando

```
SELECT  
TOP(1)
-------------------------------------------
(SELECT
ISNULL(SUM(IMPORTE), 0) AS TOTAL
FROM [NEW_BYTES].[dbo].[MS_CHEQUES_RECIBIDOS_ENLACE]
INNER JOIN [NEW_BYTES].[dbo].[MS_CHEQUES_ESTADOACTUAL]
ON [MS_CHEQUES_RECIBIDOS_ENLACE].ID_CHEQUE = [MS_CHEQUES_ESTADOACTUAL].ID_CHEQUE
WHERE ([MS_CHEQUES_ESTADOACTUAL].ID_ESTADO = 1
OR [MS_CHEQUES_ESTADOACTUAL].ID_ESTADO = 2
OR [MS_CHEQUES_ESTADOACTUAL].ID_ESTADO = 3
OR [MS_CHEQUES_ESTADOACTUAL].ID_ESTADO = 6
OR [MS_CHEQUES_ESTADOACTUAL].ID_ESTADO = 7)
AND [MS_CHEQUES_RECIBIDOS_ENLACE].ID_CLIENTE = MC_CCORRIENTES_MOVIMIENTOS.ID_CLIENTE)
AS SALDO_CHEQUE_CLI,
-------------------------------------------
(SELECT
CLI_SALDODOLAR
FROM NEW_BYTES.dbo.MS_CTACTE_CLIENTES
WHERE ID_CLIENTE = MC_CCORRIENTES_MOVIMIENTOS.ID_CLIENTE)
AS CLI_SALDODOLAR,
-------------------------------------------
(SELECT
SUM(CASE f.TR_CODIGO
WHEN 4 THEN CC_IMPORTEUSD * -1
WHEN 24 THEN CC_IMPORTEUSD * -1
WHEN 125 THEN CC_IMPORTEUSD * -1
WHEN 14 THEN CC_IMPORTEUSD * -1
WHEN 34 THEN CC_IMPORTEUSD * -1
WHEN 32 THEN CC_IMPORTEUSD * -1
WHEN 41 THEN CC_IMPORTEUSD * -1
ELSE CC_IMPORTEUSD
END)
FROM [NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS] f
INNER JOIN [NEW_BYTES].[dbo].GL_TRANSACCIONES
ON f.TR_CODIGO = GL_TRANSACCIONES.TR_CODIGO
WHERE CC_ANULADO = 'NO'
AND CC_FECHAMOVIMIENTO >= '20010101'
AND f.ID_CLIENTE = MC_CCORRIENTES_MOVIMIENTOS.ID_CLIENTE
GROUP BY f.ID_CLIENTE)
AS TOTAL_CC
FROM [NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS]
INNER JOIN [NEW_BYTES].[dbo].GL_TRANSACCIONES
ON MC_CCORRIENTES_MOVIMIENTOS.TR_CODIGO = GL_TRANSACCIONES.TR_CODIGO
INNER JOIN NewBytes_DBF.dbo.clientes
ON MC_CCORRIENTES_MOVIMIENTOS.ID_CLIENTE = clientes.ID_CLIENTE
WHERE CC_ANULADO = 'NO'
AND CC_FECHAMOVIMIENTO >= '20010101'
AND MC_CCORRIENTES_MOVIMIENTOS.ID_CLIENTE = ?
```
