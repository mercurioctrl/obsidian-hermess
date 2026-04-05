---
jira_key: "COB-43"
aliases: ["COB-43"]
summary: "API - Feat - Listar comprobantes de pago"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-08-02 08:01"
updated: "2024-02-16 11:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-43"
---

# COB-43: API - Feat - Listar comprobantes de pago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-02 08:01 |
| Actualizado | 2024-02-16 11:17 |
| Etiquetas | ninguna |
| Jira | [COB-43](https://bluinc.atlassian.net/browse/COB-43) |

## Relaciones

- **Padre:** [[COB-48]] Comprobantes fiscales
- **Subtarea:** [[COB-49]] API - Feat - Filtrar comprobantes
- **Subtarea:** [[COB-50]] API - Feat - Paginar
- **Subtarea:** [[COB-118]] API - Refactor - Se hacen algunos cambios en el objeto final
- **Subtarea:** [[COB-333]] API - Review - Problema al hacer una busqueda de comprobantes
- **relates to:** [[COB-482]] API - Listar comprobantes de pago - Error al visualizar/descargar comprobantes

## Descripcion

Se trata del recurso principal para listar los comprobantes fiscales (facturas, nota de crédito y nota de débito)

```
GET {{API_URL}}/v1/vouchers
```

Retorna

```json
[
  {
    "voucherId": 482313,
    "pedido": "00542498",
    "businessName": "NB DISTRIBUIDORA MAYORISTA SRL",
    "voucherType": "A",
    "branch": "0003",
    "voucherNumber": "00109798",
    "date": "2022-08-09 15:09:01",
    "clientName": "GALASCHI DARIO JOSE",
    "clientId": "019447",
    "UserEmail": null,
    "voucherType": 1,
    "voucherTypeDescription": "FACTURA",
    "ID_NROREMCLI_ENC": "X000200542498",
    "iibbPercepctions": 0.0,
    "totalFinal": 569.19,
    "total": 515.1,
    "totalIva": 54.09,
    "relatedVoucherId": null,
    "relatedVoucher": null,
    "currency": "DOL",
    "taxOnly": null,
    "relatedVoucherType": null
  },
  {
    "voucherId": 482312,
    "pedido": "00542560",
    "businessName": "NB DISTRIBUIDORA MAYORISTA SRL",
    "voucherTypeTax": "A",
    "branch": "0003",
    "voucherNumber": "00109797",
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
  {
    "voucherId": 482311,
    "pedido": "00542604",
    "businessName": "NB DISTRIBUIDORA MAYORISTA SRL",
    "voucherTypeTax": "B",
    "branch": "0003",
    "voucherNumber": "00035567",
    "date": "2022-08-09 15:07:17",
    "clientName": "PASTUCH DIEGO MIGUEL",
    "clientId": "011508",
    "UserEmail": "aru@hotmail.com",
    "voucherTypeId": 1,
    "voucherTypeDescription": "FACTURA",
    "ID_NROREMCLI_ENC": "X000200542604",
    "iibbPercepctions": 0.0,
    "totalFinal": 53.2,
    "total": 47.36,
    "totalIva": 5.84,
    "relatedVoucherId": null,
    "relatedVoucher": null,
    "currency": "DOL",
    "taxOnly": null,
    "relatedVoucherType": null
  }
  ]
```

```sql
SELECT TOP(300)
    ID_NROFACCLI_ENC as voucherId,
    ID_NROREMCLI_ENC as pedido,
    FP_Empresas.CNOMBRE as businessName,
    CSERIE as voucherTypeTax,
    CNUMSUC as branch,
    CNUMFAC as voucherNumber ,
    CONVERT(VARCHAR, DFECFAC, 20)  as date,
    cnomcli as clientName,
    clientes.ccodcli as clientId,


    UserEmail,
    NTIPODOCU as voucherType,
    FP_TiposDocumentosCobro.Descripcion,
    ID_NROREMCLI_ENC,
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
WHERE LANULADA = 'false' AND CAE IS NOT NULL

    AND NCNOTOCASALDONISTOCK IS NULL

ORDER BY DFECFAC DESC
```
