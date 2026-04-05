---
jira_key: "COB-229"
aliases: ["COB-229"]
summary: "No se ve un movimiento en la cuenta de banco"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-11-07 09:03"
updated: "2022-11-07 11:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-229"
---

# COB-229: No se ve un movimiento en la cuenta de banco

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-07 09:03 |
| Actualizado | 2022-11-07 11:58 |
| Etiquetas | ninguna |
| Jira | [COB-229](https://bluinc.atlassian.net/browse/COB-229) |

## Relaciones

*Sin relaciones*

## Descripcion

```
SELECT TOP (1000) [ID_Movimiento_Entrada]
      ,[Id_Operacion_Entrada]
      ,[ME_Fecha_Movimiento]
      ,[ME_Fecha_Efec]
      ,[ME_Cl_Identificacion]
      ,[Id_Origen_Entrada]
      ,[Id_Caja_Cuenta]
      ,[ME_Banco_Cheque]
      ,[ME_Numero_Cheque]
      ,[ME_Cuenta_Cheque]
      ,[ME_Titular_Cheque]
      ,[ME_Importe]
      ,[ID_Moneda]
      ,[ME_Cotizacion]
      ,[ME_Importe_Original]
      ,[ME_Moneda_Original]
      ,[ME_Observaciones]
      ,[ME_Periodo]
      ,[ME_Anulado]
      ,[ME_Cheque_En_Caja]
      ,[ME_Fecha]
      ,[ME_Hora]
      ,[USU_Identificacion]
      ,[Id_Pago_Cliente_Relacionado]
      ,[ME_ComprobanteDolar]
      ,[ME_ComprobantePesos]
      ,[ID_BancoPesos]
      ,[ID_BancoDolar]
  FROM [NEW_BYTES].[dbo].[BA_BP_MOVIMIENTOS_ENTRADAS]
    WHERE ID_Movimiento_Entrada = 154002
  order by ME_Fecha_Movimiento desc
```
