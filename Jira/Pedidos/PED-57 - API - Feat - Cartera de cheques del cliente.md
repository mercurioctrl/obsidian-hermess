---
jira_key: "PED-57"
aliases: ["PED-57"]
summary: "API - Feat - Cartera de cheques del cliente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-09-07 09:00"
updated: "2023-09-14 09:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-57"
---

# PED-57: API - Feat - Cartera de cheques del cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-07 09:00 |
| Actualizado | 2023-09-14 09:32 |
| Etiquetas | ninguna |
| Jira | [PED-57](https://bluinc.atlassian.net/browse/PED-57) |

## Relaciones

- **Padre:** [[PED-54 - Cuenta corriente de clientes|PED-54]] Cuenta corriente de clientes
- **is blocked by:** [[PED-53 - Migracion a Laravel|PED-53]] Migracion a Laravel
- **blocks:** [[PED-62 - APP - Feat - Mostrar cartera de cheques del cliente|PED-62]] APP - Feat - Mostrar cartera de cheques del cliente

## Descripcion

Este recurso muestra los cheques que tiene recibidos el cliente en la cuenta corriente, es decir aquellos que le restan saldo a su linea de crédito de cheques

```
GET {{API_URL}}/v1/checksReceived/{clientId}
```

**Retorna**

```json
[
    {
        "clientId": "25613 ",
        "clientName": "DREVNIAK PEDRO JOSE",
        "checkNumber": "23990699",
        "bankId": "7",
        "bankName": "BANCO DE GALICIA Y BUENOS AIRES S.A.",
        "bankBranchId": "7              ",
        "amount": "82318.0",
        "emitDate": "16\/08\/2023",
        "dateCharged": "18\/09\/2023",
        "receptionDate": "20230817",
        "status": "Recibido",
        "statusId": "1",
        "branch": "0002",
        "cnumalb": "00564420",
        "clearingTime": "48",
        "boxId": "CAJA1",
        "checkId": "330411",
        "quoteCheck": "472.60000000000002",
        "interest": "18.149999999999999",
        "own": "SI"
    },
    {
        "clientId": "25613 ",
        "clientName": "DREVNIAK PEDRO JOSE",
        "checkNumber": "23919764",
        "bankId": "7",
        "bankName": "BANCO DE GALICIA Y BUENOS AIRES S.A.",
        "bankBranchId": "7              ",
        "amount": "83211.5",
        "emitDate": "02\/08\/2023",
        "dateCharged": "05\/09\/2023",
        "receptionDate": "20230803",
        "status": "Recibido",
        "statusId": "1",
        "branch": "0002",
        "cnumalb": "00563136",
        "clearingTime": "48",
        "boxId": "CAJA1",
        "checkId": "330378",
        "quoteCheck": "363.98000000000002",
        "interest": "16.66",
        "own": "SI"
    },
    {
        "clientId": "25613 ",
        "clientName": "DREVNIAK PEDRO JOSE",
        "checkNumber": "23990698",
        "bankId": "7",
        "bankName": "BANCO DE GALICIA Y BUENOS AIRES S.A.",
        "bankBranchId": "7              ",
        "amount": "82318.0",
        "emitDate": "17\/08\/2023",
        "dateCharged": "21\/09\/2023",
        "receptionDate": "20230817",
        "status": "Recibido",
        "statusId": "1",
        "branch": "0002",
        "cnumalb": "00564420",
        "clearingTime": "48",
        "boxId": "CAJA1",
        "checkId": "330414",
        "quoteCheck": "477.0",
        "interest": "19.25",
        "own": "SI"
    },
    {
        "clientId": "25613 ",
        "clientName": "DREVNIAK PEDRO JOSE",
        "checkNumber": "23919766",
        "bankId": "7",
        "bankName": "BANCO DE GALICIA Y BUENOS AIRES S.A.",
        "bankBranchId": "7              ",
        "amount": "83211.5",
        "emitDate": "02\/08\/2023",
        "dateCharged": "06\/09\/2023",
        "receptionDate": "20230803",
        "status": "Recibido",
        "statusId": "1",
        "branch": "0002",
        "cnumalb": "00563136",
        "clearingTime": "48",
        "boxId": "CAJA1",
        "checkId": "330379",
        "quoteCheck": "365.50999999999999",
        "interest": "17.149999999999999",
        "own": "SI"
    },
```

**Repositorio guía**

```sql
SELECT REC.ID_CLIENTE AS clientId
    , REC.TITULAR_CUENTA AS clientName
    , REC.NRO_CHEQUE AS checkNumber
    , REC.ID_BANCO AS bankId
    , REC.NOMBRE_BANCO AS bankName
    , REC.ID_SUCBANCO AS bankBranchId
    , REC.IMPORTE AS amount
    , CONVERT(VARCHAR(10), CONVERT(DATETIME, REC.FECHA_EMISION), 103) AS emitDate
    , CONVERT(NVARCHAR(10), CONVERT(DATETIME, REC.FECHA_COBRO), 103) AS dateCharged
    , CASE 
        WHEN MOV.ID_ESTADO = 1
            THEN CAST(MOV.FECHA_MOVIMIENTO AS INT)
        ELSE NULL
        END AS receptionDate
    , E.DESCRIPCION AS STATUS
    , E.ID_ESTADOCHEQUE AS statusId
    , REC.ID_SUCURSAL AS branch
    , REC.ID_REMITO AS cnumalb
    , REC.CLEARING AS clearingTime
    , MOV.USU_IDENTIFICACION AS boxId
    , CAST(REC.ID_CHEQUE AS INT) AS checkId
    , REC.quoteCheck
    , REC.interest
    , REC.CHEQ_PROPIO AS own
FROM [NEW_BYTES].[dbo].[MS_CHEQUES_ESTADOACTUAL] AS MOV
LEFT JOIN [NEW_BYTES].[dbo].[MS_CHEQUES_RECIBIDOS_ENLACE] AS REC
    ON MOV.ID_CHEQUE = REC.ID_CHEQUE
LEFT JOIN [NEW_BYTES].[dbo].[MS_CHEQUES_ESTADOS] AS E
    ON MOV.ID_ESTADO = E.ID_ESTADOCHEQUE
WHERE MOV.ID_CHEQUE IN (
        SELECT MS_CHEQUES_RECIBIDOS_ENLACE.ID_CHEQUE
        FROM [NEW_BYTES].[dbo].[MS_CHEQUES_RECIBIDOS_ENLACE]
        INNER JOIN [NEW_BYTES].[dbo].[MS_CHEQUES_ESTADOACTUAL]
            ON [MS_CHEQUES_RECIBIDOS_ENLACE].ID_CHEQUE = [MS_CHEQUES_ESTADOACTUAL].ID_CHEQUE
        WHERE (
                [MS_CHEQUES_ESTADOACTUAL].ID_ESTADO = 1
                OR [MS_CHEQUES_ESTADOACTUAL].ID_ESTADO = 2
                OR [MS_CHEQUES_ESTADOACTUAL].ID_ESTADO = 3
                OR [MS_CHEQUES_ESTADOACTUAL].ID_ESTADO = 6
                OR [MS_CHEQUES_ESTADOACTUAL].ID_ESTADO = 7
                )
            AND [MS_CHEQUES_RECIBIDOS_ENLACE].ID_CLIENTE = ?
        )

```
