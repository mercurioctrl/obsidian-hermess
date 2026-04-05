---
jira_key: "COB-518"
aliases: ["COB-518"]
summary: "API - Refactor - Agrupar por concepto las Entradas / Salidas para graficar"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-08 10:23"
updated: "2025-02-04 14:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-518"
---

# COB-518: API - Refactor - Agrupar por concepto las Entradas / Salidas para graficar

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-08 10:23 |
| Actualizado | 2025-02-04 14:12 |
| Etiquetas | ninguna |
| Jira | [COB-518](https://bluinc.atlassian.net/browse/COB-518) |

## Relaciones

- **Padre:** [[COB-507 - Entrada Salida Cajas|COB-507]] Entrada / Salida Cajas
- **is blocked by:** [[COB-532 - API - Agrupar las entradas y salidas para graficar - Filtro por fechas no|COB-532]] API - Agrupar las entradas y salidas para graficar - Filtro por fechas no coincidente
- **is blocked by:** [[COB-533 - API - Agrupar por concepto las Entradas Salidas para graficar - Pases visibles|COB-533]] API - Agrupar por concepto las Entradas / Salidas para graficar - Pases visibles
- **relates to:** [[COB-519 - APP - Refactor - Graficar Entradas Salidas de caja|COB-519]] APP - Refactor - Graficar Entradas / Salidas de caja

## Descripcion

Crearemos un recurso que nos traiga ingresos y egreso de caja para poder gratificarlos según los siguientes filtros

- Caja (Usuario)


- Concepto (tr)


- Divisa (dolar/peso/cheque/etc)


- Fechas


- Subconcepto (`transactionTypeDescriptionComplement`) 



```
GET {API_URL}/v1/statistics/boxes?between=24-07-2024_24-07-2024&paymentMethod=2&transactionType=2&agentId=66

```

Devuelve

```

  {
    "transactionTypeId": "22",
    "transactionTypeDescription": "Pases Egresos",
    "amount": -1.0,
    "paymentMethodId": 1,
    "LOG_ID_ENTRADASALIDA": null,
    "paymentMethodDescription": "DOLARES",
    "transactionTypeDescriptionComplement": null,
    "concatenatedDescription": "Pases Egresos - "
  },
  {
    "transactionTypeId": "8",
    "transactionTypeDescription": "Salidas Varias",
    "amount": -12.0,
    "paymentMethodId": 1,
    "LOG_ID_ENTRADASALIDA": 29,
    "paymentMethodDescription": "DOLARES",
    "transactionTypeDescriptionComplement": "Banco Galicia",
    "concatenatedDescription": "Salidas Varias - Banco Galicia"
  },
  {
    "transactionTypeId": "8",
    "transactionTypeDescription": "Salidas Varias",
    "amount": -50.0,
    "paymentMethodId": 1,
    "LOG_ID_ENTRADASALIDA": 37,
    "paymentMethodDescription": "DOLARES",
    "transactionTypeDescriptionComplement": "Gastos Operativos",
    "concatenatedDescription": "Salidas Varias - Gastos Operativos"
  },
  ....
```

```
WITH CTE AS (
    SELECT 
        LOG.TR_CODIGO as transactionTypeId,
        TR.TR_NOMBRE as transactionTypeDescription,
        SUM(CASE 
                WHEN TR.TR_INDICADOR_SIGNO_F10 = '-'
                    THEN LOG_IMPORTE * - 1
                ELSE LOG_IMPORTE
            END) AS amount,
        LOG.ID_FORMAPAGO as paymentMethodId,
        LOG_ID_ENTRADASALIDA,
        FP.FP_DESCRIPCION as paymentMethodDescription,
        IIF(
            LOG.TR_CODIGO = 8,
            (SELECT Descripcion
             FROM NEW_BYTES.dbo.BA_BP_DESTINOS_SALIDAS
             WHERE ID_Destino_Salida = LOG.LOG_ID_ENTRADASALIDA),
            (SELECT OE_Descripcion
             FROM NEW_BYTES.dbo.BA_BP_ORIGENES_ENTRADAS
             WHERE ID_Origen_Entrada = LOG.LOG_ID_ENTRADASALIDA)
        ) as transactionTypeDescriptionComplement
    FROM [NEW_BYTES].[dbo].MC_LOG_OPERACIONES LOG
    LEFT JOIN [NEW_BYTES].[dbo].GL_TRANSACCIONES TR
        ON LOG.TR_CODIGO = TR.TR_CODIGO
    LEFT JOIN NEW_BYTES.dbo.MC_CCORRIENTES_MOVIMIENTOS MCV
        ON MCV.ID_CCMOVIMIENTO = ID_REFERENCIA
    LEFT JOIN NEW_BYTES.dbo.MC_FORMAS_PAGO FP
        ON FP.ID_FORMAPAGO = LOG.ID_FORMAPAGO
    WHERE LOG_FECHAMOVIMIENTO >= '20010101'
        AND LOG.LOG_FECHAMOVIMIENTO BETWEEN '20240701' AND '20240725'
        AND (
            CC_ANULADO = 'NO'
            OR CC_ANULADO IS NULL
        )
    GROUP BY LOG.TR_CODIGO,
        TR.TR_NOMBRE,
        LOG.ID_FORMAPAGO,
        FP.FP_DESCRIPCION,
        LOG_ID_ENTRADASALIDA
)
SELECT 
    transactionTypeId,
    transactionTypeDescription,
    amount,
    paymentMethodId,
    LOG_ID_ENTRADASALIDA,
    paymentMethodDescription,
    transactionTypeDescriptionComplement,
    CONCAT(transactionTypeDescription, ' - ', transactionTypeDescriptionComplement) as concatenatedDescription
FROM CTE
GROUP BY 
    transactionTypeId,
    transactionTypeDescription,
    amount,
    paymentMethodId,
    LOG_ID_ENTRADASALIDA,
    paymentMethodDescription,
    transactionTypeDescriptionComplement,
    CONCAT(transactionTypeDescription, ' - ', transactionTypeDescriptionComplement)

```
