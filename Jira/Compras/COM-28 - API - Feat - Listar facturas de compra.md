---
jira_key: "COM-28"
aliases: ["COM-28"]
summary: "API - Feat - Listar facturas de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-02-15 13:44"
updated: "2024-02-16 15:55"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-28"
---

# COM-28: API - Feat - Listar facturas de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-15 13:44 |
| Actualizado | 2024-02-16 15:55 |
| Etiquetas | ninguna |
| Jira | [COM-28](https://bluinc.atlassian.net/browse/COM-28) |

## Relaciones

- **Padre:** [[COM-27 - Listar facturas de compras|COM-27]] Listar facturas de compras 

## Descripcion

Generaremos un recurso para poder ver las facturas de nuestros proveedores

```
GET {API_URL}/v1/providerVoucher?status={status}&search={voucherCode o providerid, providername}
```

```
[
  {
    "voucherCode": 8260,
    "voucherNumber": "A-0003-00012097",
    "providerId": "000098",
    "providerName": "Novatech Solutions SA              ",
    "vouicherDataDate": "2013-03-07 12:18:52",
    "voucherDate": "2013-02-26 00:00:00",
    "currencyPrefix": "PSO",
    "currencyAmount": 1.0,
    "fob": null,
    "providerOrderInbound": null,
    "statusId": 1,
    "id": 1
  },
  {
    "voucherCode": 8261,
    "voucherNumber": "A-0002-00080642",
    "providerId": "000275",
    "providerName": "ANTONIO FIORENTINO Y MARIO FIOR.   ",
    "vouicherDataDate": "2013-03-08 11:24:02",
    "voucherDate": "2013-03-06 00:00:00",
    "currencyPrefix": "PSO",
    "currencyAmount": 0.0,
    "fob": null,
    "providerOrderInbound": null,
    "statusId": 1,
    "id": 2
  },
  {
    "voucherCode": 8263,
    "voucherNumber": "A-0032-00014045",
    "providerId": "000019",
    "providerName": "PCARTS Argentina SA                ",
    "vouicherDataDate": "2013-03-14 14:04:19",
    "voucherDate": "2013-01-18 00:00:00",
    "currencyPrefix": "PSO",
    "currencyAmount": 1.0,
    "fob": null,
    "providerOrderInbound": null,
    "statusId": 1,
    "id": 3
  },
  {
    "voucherCode": 8264,
    "voucherNumber": "a-0002-00002729",
    "providerId": "000285",
    "providerName": "Ashir Technology Corp Srl          ",
    "vouicherDataDate": "2013-03-15 09:28:52",
    "voucherDate": "2013-02-19 00:00:00",
    "currencyPrefix": "PSO",
    "currencyAmount": 1.0,
    "fob": null,
    "providerOrderInbound": "10612",
    "statusId": 1,
    "id": 4
  }
  ]
```

```
SELECT TOP (1000) CNUMFAC
    , CSUFAC
    , FACPROT.CCODPRO
    , cnompro
    , CONVERT(VARCHAR, DFECFAC, 20) AS DFECFACf
    , CONVERT(VARCHAR, DFECCONT, 20) AS DFECCONTf
    , FACPROT.CCODDIV
    , FACPROT.NVALDIV
    , FACPROT.FOB
    , FACPROT.CNUMALB
    , FACPROT.IDESTADOFAC
    , IDFACPROT
FROM newbytes_dbf.dbo.FACPROT
LEFT JOIN newbytes_dbf.dbo.FP_Proveedores
    ON FACPROT.CCODPRO = FP_Proveedores.CCODPRO

```
