---
jira_key: "COB-5"
aliases: ["COB-5"]
summary: "API - Feat - Obtener cuenta corriente de un cliente"
status: "CodeReview"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-07-14 14:04"
updated: "2023-02-02 09:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-5"
---

# COB-5: API - Feat - Obtener cuenta corriente de un cliente

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-14 14:04 |
| Actualizado | 2023-02-02 09:29 |
| Etiquetas | ninguna |
| Jira | [COB-5](https://bluinc.atlassian.net/browse/COB-5) |

## Relaciones

- **Padre:** [[COB-20 - Cuentas Corrientes|COB-20]] Cuentas Corrientes
- **Subtarea:** [[COB-57 - API - Refactor - Nuevos parametros|COB-57]] API - Refactor - Nuevos parametros
- **Subtarea:** [[COB-59 - API - Feat - Paginar|COB-59]] API - Feat - Paginar
- **Subtarea:** [[COB-60 - API - Feat - Agregar saldo en cuenta a un cliente|COB-60]] API - Feat - Agregar saldo en cuenta a un cliente
- **Subtarea:** [[COB-61 - API - Feat - Anular un movimiento|COB-61]] API - Feat - Anular un movimiento
- **Subtarea:** [[COB-62 - API - Feat - Editar un movimiento|COB-62]] API - Feat - Editar un movimiento
- **Subtarea:** [[COB-63 - API - Feat - Agregar un memo|COB-63]] API - Feat - Agregar un memo
- **Subtarea:** [[COB-76 - API - Refactor - Refactor subtotales en pesos de las cuentas corrientes|COB-76]] API - Refactor - Refactor subtotales en pesos de las cuentas corrientes
- **Subtarea:** [[COB-87 - API - Review - Paginar|COB-87]] API - Review - Paginar
- **Subtarea:** [[COB-93 - API - Feat - Filtrar lista clientes|COB-93]] API - Feat - Filtrar lista clientes
- **Subtarea:** [[COB-256 - API - Refactor - Anular movimiento|COB-256]] API - Refactor - Anular movimiento
- **Subtarea:** [[COB-279 - API - Refactor - Agregar al objeto de la cuenta corriente la branch|COB-279]] API - Refactor - Agregar al objeto de la cuenta corriente la branch
- **Subtarea:** [[COB-378 - API - Feat - Mover saldo entre clientes|COB-378]] API - Feat - Mover saldo entre clientes
- **Subtarea:** [[COB-379 - API - O. Mejora - Mejorar rendimiento de la consulta|COB-379]] API - O. Mejora - Mejorar rendimiento de la consulta 
- **Subtarea:** [[COB-467 - API - Feat - Obtener pedido completo para que el que lee la cuenta corriente lo|COB-467]] API - Feat - Obtener pedido completo para que el que lee la cuenta corriente lo pueda visualizar
- **Subtarea:** [[COB-468 - APP - Feat - Obtener pedido completo para que el que lee la cuenta corriente|COB-468]] APP - Feat - Obtener pedido completo para que el que lee la cuenta corriente pueda visualizarlo
- **Subtarea:** [[COB-472 - API - Refactor - Cotización en cero|COB-472]] API - Refactor - Cotización en cero
- **Subtarea:** [[COB-483 - API - Review Performance - Recurso Balances|COB-483]] API - Review Performance - Recurso "Balances"
- **blocks:** [[COB-322 - Refactor - Agregar nombre real a los movimientos de cc|COB-322]] Refactor - Agregar nombre real a los movimientos de cc
- **blocks:** [[COB-325 - API - Refactor - Enlace a documentación de postventa (Notas de credito) a los|COB-325]] API - Refactor - Enlace a documentación de postventa (Notas de credito) a los movimientos de CC
- **blocks:** [[COB-326 - APP - Refactor - Enlace a documentación de postventa (Notas de credito) a los|COB-326]] APP - Refactor - Enlace a documentación de postventa (Notas de credito) a los movimientos de CC

## Descripcion

```
GET {API_RUL}/v1/currentAccount/{clientId}
```

```
 [
        {
            "date": "20170315",
            "albNumber": "00326440",
            "total": -921.25999999999999,
            "currencyQuote": 15.81,
            "agent": "VENTAS3",
            "comment": "Aca un texto o comentario",
            "currentBalance": 2.0800000000001546,
            "currencyQuoteDay": 136.0,
            "currencyQuoteDayCheck": 146.06,
            "subTotal": "-63146,01",
            "id": 300399   
        },
    {
            "date": "20170315",
            "albNumber": "00326440",
            "total": -921.25999999999999,
            "currencyQuote": 15.81,
            "agent": "VENTAS3",
            "comment": "Aca un texto o comentario",
            "currentBalance": 2.0800000000001546,
            "currencyQuoteDay": 136.0,
            "currencyQuoteDayCheck": 146.06,
            "subTotal": "-63162,45",
            "id": 300399
        },
]
```



Toda la informacion para conseguir le objeto se logra de la siguiente manera

```
SELECT (SELECT
COTIZACION
FROM NEW_BYTES.dbo.MS_COTIZACIONES
WHERE NOMBRE = 'PESOS')
AS COTIZACION_HOY,

(SELECT
COTIZACION
FROM NEW_BYTES.dbo.MS_COTIZACIONES
WHERE NOMBRE = 'CHEQUES')
AS COTIZACION_HOY_CHEQUE,

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
(SELECT
CLI_SALDODOLAR
FROM NEW_BYTES.dbo.MS_CTACTE_CLIENTES
WHERE ID_CLIENTE = MC_CCORRIENTES_MOVIMIENTOS.ID_CLIENTE)
AS CLI_SALDODOLAR,
MC_CCORRIENTES_MOVIMIENTOS.CC_FECHAMOVIMIENTO,
MC_CCORRIENTES_MOVIMIENTOS.REMITO_FP,
MC_CCORRIENTES_MOVIMIENTOS.COTIZACION,
MC_CCORRIENTES_MOVIMIENTOS.USU_IDENTIFICACION,
MC_CCORRIENTES_MOVIMIENTOS.CC_OBSERVACIONES,
CASE [MC_CCORRIENTES_MOVIMIENTOS].TR_CODIGO
WHEN 4 THEN CC_IMPORTEUSD * -1
WHEN 24 THEN CC_IMPORTEUSD * -1
WHEN 125 THEN CC_IMPORTEUSD * -1
WHEN 14 THEN CC_IMPORTEUSD * -1
WHEN 34 THEN CC_IMPORTEUSD * -1
WHEN 32 THEN CC_IMPORTEUSD * -1
WHEN 41 THEN CC_IMPORTEUSD * -1
ELSE CC_IMPORTEUSD
END AS TOTAL,
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
AS TOTAL_CC,
ROW_NUMBER() OVER (ORDER BY MC_CCORRIENTES_MOVIMIENTOS.ID_CCMOVIMIENTO DESC) AS Rownr,
MC_CCORRIENTES_MOVIMIENTOS.ID_CCMOVIMIENTO
FROM [NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS]
INNER JOIN [NEW_BYTES].[dbo].GL_TRANSACCIONES
ON MC_CCORRIENTES_MOVIMIENTOS.TR_CODIGO = GL_TRANSACCIONES.TR_CODIGO
INNER JOIN NewBytes_DBF.dbo.clientes
ON MC_CCORRIENTES_MOVIMIENTOS.ID_CLIENTE = clientes.ID_CLIENTE
WHERE CC_ANULADO = 'NO'
AND CC_FECHAMOVIMIENTO >= '20010101'
AND MC_CCORRIENTES_MOVIMIENTOS.ID_CLIENTE =
```
