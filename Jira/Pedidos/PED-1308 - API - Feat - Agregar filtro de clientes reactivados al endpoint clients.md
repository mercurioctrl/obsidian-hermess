---
jira_key: "PED-1308"
aliases: ["PED-1308"]
summary: "API - Feat - Agregar filtro de clientes reactivados al endpoint clients"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2026-02-06 15:40"
updated: "2026-02-24 14:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1308"
---

# PED-1308: API - Feat - Agregar filtro de clientes reactivados al endpoint clients

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2026-02-06 15:40 |
| Actualizado | 2026-02-24 14:26 |
| Etiquetas | ninguna |
| Jira | [PED-1308](https://bluinc.atlassian.net/browse/PED-1308) |

## Relaciones

- **Padre:** [[PED-299 - Objetivos y Desafios|PED-299]] Objetivos y Desafios

## Descripcion

Se agregó la funcionalidad para filtrar clientes reactivados en el endpoint de listado de clientes.                               

**Parámetros nuevos:**                                                                                                                

- reactivatedClients (boolean): Activa el filtro de clientes reactivados                                                          


- reactivatedMonths (int, default: 3): Período en meses para considerar la reactivación                                           



**Uso**:                                                                                                                              
*Con este params es mas que suficiente para mostrar los clientes reactivados*

```
GET /clients?sellerId=51&reactivatedClients=true 
```

                                                                                

```
GET /clients?sellerId=51&reactivatedClients=true&reactivatedMonths=6  
```

                                                                                                 

**Lógica aplicada:**                                                                                                                  

- Cliente reactivado: tuvo más de 3 meses de inactividad entre compras                                                            


- Excluye clientes nuevos (sin compra anterior)                                                                                   


- Filtra por período de reactivación (últimos 3 meses por defecto)                                                                





Query actual funcional.

```

select ccodcli,
       clientes.clientLo,
       cnomcli,
       cnomcom,
       cdircli,
       FECHA_ALTA,
       ID_CLIENTE,
       cdnicif,
       email,
       ctfo1cli,
       ctfo2cli,
       cnbrage,
       capeage,
       clientes.ID_PAIS                                                       as countryId,
       FP_Provincias.Descripcion,
       FP_Provincias.ID_PROVINCIA,
       clientes.ccodage,
       average_purchase_value,
       purchase_frequency,
       relationship_duration_month,
       ltv,
       ULTIMA_COMPRA                                                          as lastBuy,
       DATEDIFF(DAY, ULTIMA_COMPRA, GETDATE())                                as sinceLastPurchase,
       whaPhone,
       specialPrice,
       CODEMP,
       voucherCompanyCode,
       perfil,
       (SELECT ROUND(CLI_SALDOCHEQUE, 2)
        FROM NEW_BYTES.dbo.MS_CTACTE_CLIENTES
        WHERE ID_CLIENTE = clientes.ID_CLIENTE)                               as limitCheckBalanceAmount,
       (SELECT ROUND(ISNULL(SUM(IMPORTE), 0), 2) AS TOTAL
        FROM [NEW_BYTES].[dbo].[MS_CHEQUES_RECIBIDOS_ENLACE]
                 INNER JOIN [NEW_BYTES].[dbo].[MS_CHEQUES_ESTADOACTUAL]
                            ON [MS_CHEQUES_RECIBIDOS_ENLACE].ID_CHEQUE = [MS_CHEQUES_ESTADOACTUAL].ID_CHEQUE
        WHERE ([MS_CHEQUES_ESTADOACTUAL].ID_ESTADO = 1
            OR [MS_CHEQUES_ESTADOACTUAL].ID_ESTADO = 2
            OR [MS_CHEQUES_ESTADOACTUAL].ID_ESTADO = 3
            OR [MS_CHEQUES_ESTADOACTUAL].ID_ESTADO = 6
            OR [MS_CHEQUES_ESTADOACTUAL].ID_ESTADO = 7)
          AND [MS_CHEQUES_RECIBIDOS_ENLACE].ID_CLIENTE = clientes.ID_CLIENTE) AS usedCheckBalanceAmount,
       (SELECT TOP 1 ROUND(CLI_SALDODOLAR, 2)
        FROM NEW_BYTES.dbo.MS_CTACTE_CLIENTES
        WHERE MS_CTACTE_CLIENTES.ID_CLIENTE = clientes.ID_CLIENTE)            as limitBalanceAmount,
       (SELECT ROUND(ISNULL(SUM(CASE f.TR_CODIGO
                                    WHEN 4 THEN CC_IMPORTEUSD * -1
                                    WHEN 24 THEN CC_IMPORTEUSD * -1
                                    WHEN 125 THEN CC_IMPORTEUSD * -1
                                    WHEN 14 THEN CC_IMPORTEUSD * -1
                                    WHEN 34 THEN CC_IMPORTEUSD * -1
                                    WHEN 32 THEN CC_IMPORTEUSD * -1
                                    WHEN 41 THEN CC_IMPORTEUSD * -1
                                    ELSE CC_IMPORTEUSD
           END), 0), 2)
        FROM [NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS] f
                 INNER JOIN [NEW_BYTES].[dbo].GL_TRANSACCIONES ON f.TR_CODIGO = GL_TRANSACCIONES.TR_CODIGO
        WHERE CC_ANULADO = 'NO'
          AND CC_FECHAMOVIMIENTO >= '20010101'
          AND f.ID_CLIENTE = clientes.ID_CLIENTE
        GROUP BY f.ID_CLIENTE)                                                AS currentBalance,
       null                                                                   as mode
from [NewBytes_DBF].[dbo].[clientes]
         left join [NewBytes_DBF].[dbo].[agentes] on [clientes].[ID_VENDEDOR] = [agentes].[ID_VENDEDOR]
         left join [NewBytes_DBF].[dbo].[FP_Provincias] on [clientes].[ID_PROVINCIA] = [FP_Provincias].[Id_Provincia]
         left join [NewBytes_DBF].[dbo].[clientesLtv] on [clientes].[ID_CLIENTE] = [clientesLtv].[client_id] and
                                                         [clientesLtv].[create_at] = (select MAX(create_at)
                                                                                      FROM NewBytes_DBF.dbo.clientesLtv
                                                                                      WHERE client_id = clientes.ID_CLIENTE)
where (CAST(agentes.ccodage AS INT) = 51)
  and exists (select 1
              from (SELECT alb.ID_CLIENTE,
                           alb.dfecalb as fecha_compra_actual,
                           LAG(alb.dfecalb) OVER (
                               PARTITION BY alb.ID_CLIENTE
                               ORDER BY alb.dfecalb
                               )       as fecha_compra_anterior
                    FROM [NewBytes_DBF].[dbo].[albclit] alb
                    WHERE alb.dfecalb >= DATEADD(MONTH, -12, CAST(GETDATE() AS DATE))) cph
              where [cph].[ID_CLIENTE] = [clientes].[ID_CLIENTE]
                and [cph].[fecha_compra_anterior] is not null
                and DATEDIFF(month, cph.fecha_compra_anterior, cph.fecha_compra_actual) > 3
                and cph.fecha_compra_actual >= DATEADD(MONTH, -3, CAST(GETDATE() AS DATE))
                and cph.fecha_compra_actual <= CAST(GETDATE() AS DATE))
order by [ID_CLIENTE] desc
offset 0 rows fetch next 15 rows only
```
