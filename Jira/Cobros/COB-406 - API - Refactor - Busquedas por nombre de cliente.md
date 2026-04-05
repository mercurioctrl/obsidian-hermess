---
jira_key: "COB-406"
aliases: ["COB-406"]
summary: "API - Refactor - Busquedas por nombre de cliente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-04-20 10:15"
updated: "2023-04-26 09:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-406"
---

# COB-406: API - Refactor - Busquedas por nombre de cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-04-20 10:15 |
| Actualizado | 2023-04-26 09:14 |
| Etiquetas | ninguna |
| Jira | [COB-406](https://bluinc.atlassian.net/browse/COB-406) |

## Relaciones

- **Padre:** [[COB-183 - Feat - Listar cheques|COB-183]] Feat - Listar cheques

## Descripcion

Al listar cheques buscando por nombre (Por ej: Maximus) recibo el mensaje de:

```
SQLSTATE[42000]: [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]Error al convertir el tipo de datos nvarchar a float. SQL: SELECT REC.ID_CLIENTE as clientId, REC.TITULAR_CUENTA as clientName, REC.NRO_CHEQUE as checkNumber, REC.ID_BANCO as bankId, REC.NOMBRE_BANCO as bankName, REC.ID_SUCBANCO as bankBranchId, REC.IMPORTE as amount, CONVERT(varchar(10),CONVERT(datetime, REC.FECHA_EMISION),103) as emitDate, CONVERT(nvarchar(10),CONVERT(datetime, REC.FECHA_COBRO),103) as dateCharged, CASE WHEN MOV.ID_ESTADO = 1 THEN CAST(MOV.FECHA_MOVIMIENTO as INT) ELSE NULL END as receptionDate, E.DESCRIPCION as status, E.ID_ESTADOCHEQUE as statusId, REC.ID_SUCURSAL as branch, REC.ID_REMITO as cnumalb, REC.CLEARING as clearingTime, MOV.USU_IDENTIFICACION as boxId, CAST(REC.ID_CHEQUE as INT) as checkId, REC.quoteCheck, REC.interest FROM [NEW_BYTES].[dbo].[MS_CHEQUES_ESTADOACTUAL] as MOV LEFT JOIN [NEW_BYTES].[dbo].[MS_CHEQUES_RECIBIDOS_ENLACE] AS REC ON MOV.ID_CHEQUE = REC.ID_CHEQUE LEFT JOIN [NEW_BYTES].[dbo].[MS_CHEQUES_ESTADOS] AS E ON MOV.ID_ESTADO = E.ID_ESTADOCHEQUE WHERE 1=1 AND ( REC.TITULAR_CUENTA LIKE '%maximus%' OR REC.NRO_CHEQUE LIKE '%maximus%' OR REC.ID_CHEQUE = 'maximus' ) ORDER BY MOV.ID_CHEQUE DESC OFFSET 0 rows FETCH next 15 rows only
```
