---
jira_key: "PED-99"
summary: "API - Feat - Listar comprobantes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-09-28 09:18"
updated: "2025-10-30 12:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-99"
---

# PED-99: API - Feat - Listar comprobantes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-28 09:18 |
| Actualizado | 2025-10-30 12:59 |
| Etiquetas | ninguna |
| Jira | [PED-99](https://bluinc.atlassian.net/browse/PED-99) |

## Descripción

Similar a lo que hicimos en caja y expedición, haremos una pestaña de comprobantes

```
GET {API_URL}/v1/v1/vouchers
```

```json
{
    "response": [
        {
            "voucherId": 514376,
            "pedido": "X000200566782",
            "businessName": "NB DISTRIBUIDORA MAYORISTA SRL",
            "voucherTypeTax": "B",
            "voucherBranch": "0003",
            "voucherNumber": "00039509",
            "order": "10329239",
            "branch": "0002",
            "date": "28-09-2023 09:08",
            "clientName": "ROBUTTI HORACIO DAVID",
            "clientId": "025995",
            "UserEmail": "horacio.robutti@gmail.com",
            "voucherTypeId": 1,
            "voucherTypeDescription": "FACTURA",
            "idNroremcliEnc": "X000200566782",
            "iibbPercepctions": 0,
            "totalFinal": 165.86,
            "total": 145.7,
            "totalIva": 20.16,
            "relatedVoucherId": null,
            "relatedVoucher": null,
            "currency": "DOL",
            "taxOnly": null,
            "relatedVoucherType": null,
            "token": "d74c4b69756a44e82a9f8c1b96c515"
        },
        {
            "voucherId": 514375,
            "pedido": "X000200566917",
            "businessName": "NB DISTRIBUIDORA MAYORISTA SRL",
            "voucherTypeTax": "A",
            "voucherBranch": "0003",
            "voucherNumber": "00123043",
            "order": "10329500",
            "branch": "0002",
            "date": "28-09-2023 09:07",
            "clientName": "ESPECTRO GRAFICO SRL",
            "clientId": "079840",
            "UserEmail": "",
            "voucherTypeId": 1,
            "voucherTypeDescription": "FACTURA",
            "idNroremcliEnc": "X000200566917",
            "iibbPercepctions": 0,
            "totalFinal": 218.49,
            "total": 197.72,
            "totalIva": 20.76,
            "relatedVoucherId": null,
            "relatedVoucher": null,
            "currency": "DOL",
            "taxOnly": null,
            "relatedVoucherType": null,
            "token": "89fdb2a9c6c40c94353faeba0568a9"
        }
  ]
}
```

```sql
SELECT TOP(300)
ID_NROREMCLI_ENC,
FP_Empresas.CNOMBRE,
CSERIE,
CNUMSUC,
CNUMFAC,
CONVERT(VARCHAR, DFECFAC, 20) AS DFECFAC,
cnomcli,
clientes.ccodcli,
TOTIMP_EnviadoAFIP,
ID_NROFACCLI_ENC,
UserEmail,
NTIPODOCU,
FP_TiposDocumentosCobro.Descripcion,
ID_NROREMCLI_ENC,
ImportePercepCLi,
TOTIMP_EnviadoAFIP,
TOTNETO_EnvidoAFIP,
TOTIVAS_EnviadoAFIP,
CFACTURA,
CNUMALB,
ID_FACRELACIONADA,

CASE NTIPODOCU
WHEN 2 THEN
                  (SELECT top(1) 'FA '+CFACTURA AS CFACTURA
                   FROM NewBytes_DBF.dbo.FP_FactWebCliEncabezado
                   WHERE ID_NROFACCLI_ENC =A.ID_FACRELACIONADA )
           WHEN 9 THEN
                  (SELECT top(1) 'FA '+CFACTURA AS CFACTURA
                   FROM NewBytes_DBF.dbo.FP_FactWebCliEncabezado
                   WHERE ID_FACRELACIONADA = A.ID_NROFACCLI_ENC AND NTIPODOCU = 8)
            WHEN 8 THEN
                (SELECT top(1) 'FA '+CFACTURA AS CFACTURA
                FROM NewBytes_DBF.dbo.FP_FactWebCliEncabezado
                WHERE  ID_FACRELACIONADA = A.ID_NROFACCLI_ENC  AND NTIPODOCU =9 )
           ELSE
                  (SELECT top(1) 'NC '+CFACTURA AS CFACTURA
                   FROM NewBytes_DBF.dbo.FP_FactWebCliEncabezado
                   WHERE ID_FACRELACIONADA = A.ID_NROFACCLI_ENC )
END as DOCU_RELACIONADO,
A.CCODDIV,

(
SELECT top(1)  NCNOTOCASALDONISTOCK FROM NewBytes_DBF.dbo.FP_FactWebCliEncabezado WHERE ID_NROREMCLI_ENC = A.ID_NROREMCLI_ENC and NCNOTOCASALDONISTOCK IS NOT NULL AND NTIPODOCU = 2
AND CAE IS NOT NULL AND ID_NROREMCLI_ENC IS NOT NULL AND ID_NROREMCLI_ENC <> '0' AND A.ID_NROREMCLI_ENC <> '0'
) as NCNOTOCASALDONISTOCK2,

CASE NTIPODOCU
WHEN 2 THEN
(
SELECT top(1) NTIPODOCU FROM NewBytes_DBF.dbo.FP_FactWebCliEncabezado WHERE ID_NROFACCLI_ENC =A.ID_FACRELACIONADA
)
WHEN 9 THEN
                  (SELECT top(1) NTIPODOCU
                   FROM NewBytes_DBF.dbo.FP_FactWebCliEncabezado
                   WHERE FP_FactWebCliEncabezado.ID_NROREMCLI_ENC = A.ID_NROREMCLI_ENC AND NTIPODOCU = 8)
            WHEN 8 THEN
                (SELECT top(1) NTIPODOCU
                FROM NewBytes_DBF.dbo.FP_FactWebCliEncabezado
                WHERE  FP_FactWebCliEncabezado.ID_NROREMCLI_ENC = A.ID_NROREMCLI_ENC  AND NTIPODOCU =9 )
ELSE
(
SELECT top(1) NTIPODOCU FROM NewBytes_DBF.dbo.FP_FactWebCliEncabezado WHERE ID_FACRELACIONADA = A.ID_NROFACCLI_ENC
)
END as DOCU_RELACIONADO_TIPO
,NVALDIV AS COT

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
LEFT JOIN NewBytes_DBF.dbo.FP_PuntosVenta ON FP_PuntosVenta.ID_PUNTOVENTA = A.ID_PUNTOVENTA  AND FP_PuntosVenta.TipoFacturacion = 3
LEFT JOIN NewBytes_DBF.dbo.FP_Sucursales ON  FP_PuntosVenta.ID_Sucursal = FP_Sucursales.Id_sucursal AND FP_PuntosVenta.TipoFacturacion = 3
LEFT JOIN  [NewBytes_DBF].[dbo].[FP_Empresas] ON FP_Empresas.SUCFacturaPlus = A.CNUMSUC
WHERE LANULADA = 'false' AND CAE IS NOT NULL AND
ID_NROFACCLI_ENC IS NOT NULL  AND DFECFAC BETWEEN '28-09-2023 00:01' AND '28-09-2023 23:59'   AND usuarios_nb.subCuenta is null
AND NCNOTOCASALDONISTOCK IS NULL
ORDER BY DFECFAC DESC
```
