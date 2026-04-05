---
jira_key: "PED-1166"
aliases: ["PED-1166"]
summary: "API - MVP - Refactor - Agregar companyCode al objeto que devuelve el repositorio de comprobantes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-10-30 12:54"
updated: "2025-12-05 04:08"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1166"
---

# PED-1166: API - MVP - Refactor - Agregar companyCode al objeto que devuelve el repositorio de comprobantes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-30 12:54 |
| Actualizado | 2025-12-05 04:08 |
| Etiquetas | ninguna |
| Jira | [PED-1166](https://bluinc.atlassian.net/browse/PED-1166) |

## Relaciones

- **Padre:** [[PED-98 - Feat - Listar comprobantes|PED-98]] Feat - Listar comprobantes
- **action item from:** [[PED-99 - API - Feat - Listar comprobantes|PED-99]] API - Feat - Listar comprobantes
- **has action item:** [[PED-1167 - APP - MVP - Refactor - Cambiar la ruta para mostrar el comprobante según|PED-1167]] APP - MVP - Refactor - Cambiar la ruta para mostrar el comprobante según companyCode

## Descripcion

Refactorizaremos el recurso para agregarle el parámetro `companyCode` 

```
GET {API_URL}/v1/vouchers
```

```
{
    "vouchers": [
        {
            "voucherId": 591291,
            "pedido": "X000200635532",
            "businessName": "NB DISTRIBUIDORA MAYORISTA SRL",
            "voucherTypeTax": "A",
            "voucherBranch": "0003",
            "voucherNumber": "00165780",
            "order": "10435419",
            "branch": "0002",
            "companyCode": 11, <-- SE AGREGA
            "DFECFAC": "2025-10-30 12:53:28",
            "date": "30-10-2025 12:53",
            "clientName": "CLIX SA",
            "clientId": "023461",
            "UserEmail": "clixelectronical@hotmail.com",
            "voucherTypeId": 1,
            "voucherTypeDescription": "FACTURA",
            "idNroremcliEnc": "X000200635532",
            "iibbPercepctions": 0,
            "totalFinal": 6662.14,
            "total": 6029.08,
            "totalIva": 633.05,
            "relatedVoucherId": null,
            "relatedVoucher": null,
            "currency": "DOL",
            "taxOnly": null,
            "relatedVoucherType": null,
            "token": "9dcc9372f50df3ab83f69fe47985ac",
            "thirdVoucher": 0
        },
        {
            "voucherId": 591290,
            "pedido": "X000200635535",
            "businessName": "NB DISTRIBUIDORA MAYORISTA SRL",
            "voucherTypeTax": "A",
            "voucherBranch": "0003",
```
