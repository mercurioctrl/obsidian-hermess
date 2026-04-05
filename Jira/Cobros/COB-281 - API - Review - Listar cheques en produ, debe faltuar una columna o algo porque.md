---
jira_key: "COB-281"
aliases: ["COB-281"]
summary: "API - Review - Listar cheques en produ, debe faltuar una columna o algo porque da error"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-12-29 15:10"
updated: "2023-01-27 17:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-281"
---

# COB-281: API - Review - Listar cheques en produ, debe faltuar una columna o algo porque da error

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-12-29 15:10 |
| Actualizado | 2023-01-27 17:01 |
| Etiquetas | ninguna |
| Jira | [COB-281](https://bluinc.atlassian.net/browse/COB-281) |

## Relaciones

- **Padre:** [[COB-183]] Feat - Listar cheques

## Descripcion

SQLSTATE[42S22]: [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]El nombre de columna 'quoteCheck' no es válido. SQL: SELECT REC.ID_CLIENTE as clientId, REC.TITULAR_CUENTA as clientName, REC.NRO_CHEQUE as checkNumber, REC.ID_BANCO as bankId, REC.NOMBRE_BANCO as bankName, REC.ID_SUCBANCO as bankBranchId, REC.IMPORTE as amount, CONVERT(varchar(10),CONVERT(datetime, REC.FECHA_EMISION),103) as emitDate, CONVERT(nvarchar(10),CONVERT(datetime, REC.FECHA_COBRO),103) as dateCharged, CASE WHEN MOV.ID_ESTADO = 1 THEN CAST(MOV.FECHA_MOVIMIENTO as INT) ELSE NULL END as receptionDate, E.DESCRIPCION as status, E.ID_ESTADOCHEQUE as statusId, REC.ID_SUCURSAL as branch, REC.ID_REMITO as cnumalb, REC.CLEARING as clearingTime, MOV.USU_IDENTIFICACION as boxId, CAST(REC.ID_CHEQUE as INT) as checkId, REC.quoteCheck, REC.interest FROM [NEW_BYTES].[dbo].[MS_CHEQUES_ESTADOACTUAL] as MOV LEFT JOIN [NEW_BYTES].[dbo].[MS_CHEQUES_RECIBIDOS_ENLACE] AS REC ON MOV.ID_CHEQUE = REC.ID_CHEQUE LEFT JOIN [NEW_BYTES].[dbo].[MS_CHEQUES_ESTADOS] AS E ON MOV.ID_ESTADO = E.ID_ESTADOCHEQUE WHERE 1=1 ORDER BY MOV.ID_CHEQUE DESC OFFSET 0 rows FETCH next 15 rows only



[adjunto]
