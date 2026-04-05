---
jira_key: "COB-8"
summary: "API - Feat - Listar pases"
status: "Gamma"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-07-15 08:50"
updated: "2022-11-30 12:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-8"
---

# COB-8: API - Feat - Listar pases

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-15 08:50 |
| Actualizado | 2022-11-30 12:10 |
| Etiquetas | ninguna |
| Jira | [COB-8](https://bluinc.atlassian.net/browse/COB-8) |

## Descripción

Se trata del recurso encargado de listar los pases de manera general.

**¿que es un pase?**

Es la operación encargada de mover saldos o valores existentes de una caja a otra. 

**¿que muestra este recurso?**

Muestra todos los pases entrantes y salientes de todas las cajas. (Mas adelante agregaremos filtros en un refactor)

```
GET {{API_URL}}/v1/passes/
```

Devuelve

```
[
  {
    agentName: 'Carla Carpintieri',
    agentId: 3,
    description: 'Pases egresos',
    ammount: 2343.34,
    currency: 'Pesos',
    comment: 'Un comentario cualquiera',
    origin: 'Caja1',
    destiny: 'Dario',
    dateOrigin: '20-12-2021 00:000',
    dateDestiny: '20-12-2021 00:000',
    status: 'Abierto'
  },
  {
    agentName: 'Carla Carpintieri',
    agentId: 3,
    description: 'Pases egresos',
    ammount: 2343.34,
    currency: 'Pesos',
    comment: 'Un comentario cualquiera',
    origin: 'Caja1',
    destiny: 'Dario',
    dateOrigin: '20-12-2021 00:000',
    dateDestiny: '20-12-2021 00:000',
    status: 'Abierto'
  }
]
```



Una query que ilustra el origen de algunos datos

```
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
REMITO.CLI_NOMBRE, 
TR.TR_CODIGO
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
AND TR.TR_CODIGO IN (20,22)
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
REMITO.CLI_NOMBRE,
TR.TR_CODIGO
ORDER BY LOG.LOG_SECUENCIA ASC

```
