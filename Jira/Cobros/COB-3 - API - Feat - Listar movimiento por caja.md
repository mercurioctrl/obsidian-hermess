---
jira_key: "COB-3"
aliases: ["COB-3"]
summary: "API - Feat - Listar movimiento por caja"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-07-13 13:46"
updated: "2024-04-29 17:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-3"
---

# COB-3: API - Feat - Listar movimiento por caja

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-13 13:46 |
| Actualizado | 2024-04-29 17:52 |
| Etiquetas | ninguna |
| Jira | [COB-3](https://bluinc.atlassian.net/browse/COB-3) |

## Relaciones

- **Padre:** [[COB-15]] Cajas
- **Subtarea:** [[COB-27]] (deprecado) API - Feat - Filtrar entre fechas
- **Subtarea:** [[COB-37]] API - Feat - Agregar paginado
- **Subtarea:** [[COB-39]] API - Feat - Agregar Filtros
- **Subtarea:** [[COB-72]] API - Feat - Filtrar por tipo de transaccion
- **Subtarea:** [[COB-81]] API - Review - Filtros de "formas de pago" con comportamiento extraño
- **Subtarea:** [[COB-82]] API - Review - Filtros de "transactionType" con comportamiento extraño
- **Subtarea:** [[COB-84]] API - Refactor - Si el movimiento es un pase, agregar un parametro para la fecha en que fue aceptado
- **Subtarea:** [[COB-86]] API - Refactor - Se debe agregar un parametro llamado docuemtReference
- **Subtarea:** [[COB-90]] API - Review - Medio de pago/Divisa indefinido
- **Subtarea:** [[COB-98]] API - Feat - Editar comentario en movimiento de caja
- **Subtarea:** [[COB-138]] API - Refactor - Agregar permiso administrativo para ver movimientos de caja ajena
- **Subtarea:** [[COB-169]] API - Refactor - Agregar filtros necesarios para comprobantes
- **Subtarea:** [[COB-217]] API - Refactor - Cuando estoy viendo un pase en los movimientos de caja, estan invertidos origen y destinatario
- **is caused by:** [[COB-30]] APP - Feat - Ver movimientos de caja
- **blocks:** [[COB-169]] API - Refactor - Agregar filtros necesarios para comprobantes
- **blocks:** [[COB-166]] MS - Feat - Ms comprobantes, recurso de recibo de dinero
- **relates to:** [[COB-504]] API - Listar movimiento por caja - No se visualiza el cliente

## Descripcion

Este recurso se utiliza para obtener el detalle de los movimiento de una caja especifica.

```
GET {API_URL}/v1/box/{boxId}
```

Retorna:

```json
[
  {
  
    "date": "20050331",
    "hour": "154230",
    "Description": "Salidas Varias",
    "subtotal": 14142.0,
    "currency": "DOLARES",
    "symbol": "-",
    "caption": null,
    "userName": "SEBA",
    "comment": "MILLENIUM AD",
    "branch": null,
    "albNumber": null,
    "symbol_F10": "-",
    "currencyQuote": null,
    "clientId": null,
    "clientName": null
  },
  {
    
    "date": "20050415",
    "hour": "101107",
    "Description": "Remitos",
    "subtotal": 79.0,
    "currency": null,
    "symbol": "+",
    "caption": "SALIDA SI AUTORIZADA",
    "userName": "ADRIAN",
    "comment": null,
    "branch": "0002",
    "albNumber": "00006893",
    "symbol_F10": "+",
    "currencyQuote": 2.96,
    "clientId": 3243,
    "clientName": "Berdasco Enrique y Cía"
  }
  ]
```

Para obtener estos datos se debe utilizar 

```sql
SELECT
top(100)
LOG.LOG_SECUENCIA,
LOG.LOG_FECHAPROCESO  ,
LOG.LOG_HORAPROCESO  ,
TR.TR_NOMBRE ,
LOG.LOG_IMPORTE  ,
FP.FP_DESCRIPCION  ,
TR.TR_INDICADOR_SIGNO_F10  ,
UPPER(LOG.LOG_LEYENDA)  ,
UPPER(LOG.USU_IDENTIFICACION)  e,
UPPER(LOG.LOG_REFERENCIA)  ,
UPPER(LOG.LOG_SUCURSAL_REMITO)  ,
LOG.LOG_REMITO_FP  ,
TR_INDICADOR_SIGNO_F10  ,
REMITO.COTIZACION  ,
REMITO.ID_CLIENTE ,
REMITO.CLI_NOMBRE  
FROM [NEW_BYTES].[dbo].MC_LOG_OPERACIONES LOG
LEFT JOIN [NEW_BYTES].[dbo].GL_TRANSACCIONES TR
ON LOG.TR_CODIGO = TR.TR_CODIGO
LEFT JOIN NEW_BYTES.dbo.MC_CCORRIENTES_MOVIMIENTOS MCV
ON MCV.ID_CCMOVIMIENTO = ID_REFERENCIA
LEFT JOIN NEW_BYTES.dbo.MC_FORMAS_PAGO FP
ON FP.ID_FORMAPAGO = LOG.ID_FORMAPAGO
LEFT JOIN NEW_BYTES.dbo.MS_REMITO_CABECERA AS REMITO
ON REMITO.REMITO_FP = LOG.LOG_REMITO_FP AND REMITO.SUCURSAL_REMITO = LOG.LOG_SUCURSAL_REMITO
WHERE LOG.LOG_FECHAPROCESO IS NOT NULL
AND (LOG.USU_IDENTIFICACION = ?)
GROUP BY LOG.LOG_SECUENCIA,
LOG.LOG_FECHAPROCESO,
LOG.LOG_HORAPROCESO,
TR.TR_NOMBRE,
LOG.LOG_IMPORTE,
FP.FP_DESCRIPCION,
TR.TR_INDICADOR_SIGNO_F10,
LOG.LOG_LEYENDA,
LOG.USU_IDENTIFICACION,
LOG.LOG_REFERENCIA,
LOG.LOG_SUCURSAL_REMITO,
LOG.LOG_REMITO_FP,
TR_INDICADOR_SIGNO_F10,
REMITO.COTIZACION,
REMITO.ID_CLIENTE,
REMITO.CLI_NOMBRE
ORDER BY LOG.LOG_SECUENCIA ASC
```
