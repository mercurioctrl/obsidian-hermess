---
jira_key: "COB-118"
aliases: ["COB-118"]
summary: "API - Refactor - Se hacen algunos cambios en el objeto final"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-09-28 14:09"
updated: "2022-10-27 08:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-118"
---

# COB-118: API - Refactor - Se hacen algunos cambios en el objeto final

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-28 14:09 |
| Actualizado | 2022-10-27 08:14 |
| Etiquetas | ninguna |
| Jira | [COB-118](https://bluinc.atlassian.net/browse/COB-118) |

## Relaciones

- **Padre:** [[COB-43]] API - Feat - Listar comprobantes de pago

## Descripcion

```json
 {
   "voucherId": 486098,
    "pedido": "X000200546381", //verificar el campo, porque debe tener este formato (ver query)
    "businessName": "NB DISTRIBUIDORA MAYORISTA SRL",
    "voucherTypeTax": "A",
    "voucherBranch": "0003", // cambia de nombre 
    "voucherNumber": "00109797",
    "order": "10294832", // se agrega
    "branch": "0002", // se agrega
    "date": "2022-08-09 15:08:58",
    "clientName": "GALASCHI DARIO JOSE",
    "clientId": "019447",
    "UserEmail": null,
    "voucherTypeId": 1,
    "voucherTypeDescription": "FACTURA",
    "ID_NROREMCLI_ENC": "X000200542560",
    "iibbPercepctions": 0.0,
    "totalFinal": 3100.61,
    "total": 2805.98,
    "totalIva": 294.63,
    "relatedVoucherId": null,
    "relatedVoucher": null,
    "currency": "DOL",
    "taxOnly": null,
    "relatedVoucherType": null
  },
```



Consulta SQL orientativa por si hay faltantes:

```
SELECT TOP(300)
    A.ID_NROFACCLI_ENC as voucherId,
    A.ID_NROREMCLI_ENC as pedido,
    FP_Empresas.CNOMBRE as businessName,
    A.CSERIE as voucherTypeTax,
    A.CNUMSUC as voucherBranch,
    CNUMFAC as voucherNumber ,
    CONVERT(VARCHAR, DFECFAC, 20)  as date,
    cnomcli as clientName,
    clientes.ccodcli as clientId,
    albclit.cnumped as 'order',
    albclit.cnumsuc as branch,
    UserEmail,
    NTIPODOCU as voucherType,
    FP_TiposDocumentosCobro.Descripcion,
    A.ID_NROREMCLI_ENC,
    ImportePercepCLi as iibbPercepctions,
    TOTIMP_EnviadoAFIP as totalFinal,
    TOTNETO_EnvidoAFIP as total,
    TOTIVAS_EnviadoAFIP as totalIva,

    ID_FACRELACIONADA as relatedVoucherId,
    CASE NTIPODOCU
WHEN 2 THEN
(SELECT top(1)
        'FA '+CFACTURA AS CFACTURA
    FROM NewBytes_DBF.dbo.FP_FactWebCliEncabezado
    WHERE ID_NROFACCLI_ENC =A.ID_FACRELACIONADA )
WHEN 9 THEN
(SELECT top(1)
        'FA '+CFACTURA AS CFACTURA
    FROM NewBytes_DBF.dbo.FP_FactWebCliEncabezado
    WHERE ID_FACRELACIONADA = A.ID_NROFACCLI_ENC AND NTIPODOCU = 8)
WHEN 8 THEN
(SELECT top(1)
        'FA '+CFACTURA AS CFACTURA
    FROM NewBytes_DBF.dbo.FP_FactWebCliEncabezado
    WHERE  ID_FACRELACIONADA = A.ID_NROFACCLI_ENC AND NTIPODOCU =9 )
ELSE
(SELECT top(1)
        'NC '+CFACTURA AS CFACTURA
    FROM NewBytes_DBF.dbo.FP_FactWebCliEncabezado
    WHERE ID_FACRELACIONADA = A.ID_NROFACCLI_ENC )
END as relatedVoucher,
    A.CCODDIV as currency,

    (
SELECT top(1)
        NCNOTOCASALDONISTOCK
    FROM NewBytes_DBF.dbo.FP_FactWebCliEncabezado
    WHERE ID_NROREMCLI_ENC = A.ID_NROREMCLI_ENC and NCNOTOCASALDONISTOCK IS NOT NULL AND NTIPODOCU = 2
        AND CAE IS NOT NULL AND ID_NROREMCLI_ENC IS NOT NULL AND ID_NROREMCLI_ENC <> '0' AND A.ID_NROREMCLI_ENC <> '0'
) as taxOnly ,

    CASE NTIPODOCU
WHEN 2 THEN
(
SELECT top(1)
        NTIPODOCU
    FROM NewBytes_DBF.dbo.FP_FactWebCliEncabezado
    WHERE ID_NROFACCLI_ENC =A.ID_FACRELACIONADA
)
WHEN 9 THEN
(SELECT top(1)
        NTIPODOCU
    FROM NewBytes_DBF.dbo.FP_FactWebCliEncabezado
    WHERE FP_FactWebCliEncabezado.ID_NROREMCLI_ENC = A.ID_NROREMCLI_ENC AND NTIPODOCU = 8)
WHEN 8 THEN
(SELECT top(1)
        NTIPODOCU
    FROM NewBytes_DBF.dbo.FP_FactWebCliEncabezado
    WHERE  FP_FactWebCliEncabezado.ID_NROREMCLI_ENC = A.ID_NROREMCLI_ENC AND NTIPODOCU =9 )
ELSE
(
SELECT top(1)
        NTIPODOCU
    FROM NewBytes_DBF.dbo.FP_FactWebCliEncabezado
    WHERE ID_FACRELACIONADA = A.ID_NROFACCLI_ENC
)
END as relatedVoucherType
FROM
    NewBytes_DBF.dbo.FP_FactWebCliEncabezado A
    LEFT JOIN
    NewBytes_DBF.dbo.clientes
    ON
A.ccodcli = clientes.ccodcli
    LEFT JOIN
    NB_WEB.dbo.usuarios_nb
    ON clientes.ccodcli = usuarios_nb.codigoFP
    LEFT JOIN
    NewBytes_DBF.dbo.FP_TiposDocumentosCobro
    ON FP_TiposDocumentosCobro.Id_TipoDocCobro = A.ntipodocu
    LEFT JOIN NewBytes_DBF.dbo.FP_PuntosVenta ON FP_PuntosVenta.ID_PUNTOVENTA = A.ID_PUNTOVENTA AND FP_PuntosVenta.TipoFacturacion = 3
    LEFT JOIN NewBytes_DBF.dbo.FP_Sucursales ON  FP_PuntosVenta.ID_Sucursal = FP_Sucursales.Id_sucursal AND FP_PuntosVenta.TipoFacturacion = 3
    LEFT JOIN [NewBytes_DBF].[dbo].[FP_Empresas] ON FP_Empresas.SUCFacturaPlus = A.CNUMSUC
    LEFT JOIN NewBytes_DBF.dbo.albclit ON albclit.ID_NROREMCLI_ENC = A.ID_NROREMCLI_ENC
WHERE LANULADA = 'false' AND CAE IS NOT NULL

    AND NCNOTOCASALDONISTOCK IS NULL

ORDER BY DFECFAC DESC
```
