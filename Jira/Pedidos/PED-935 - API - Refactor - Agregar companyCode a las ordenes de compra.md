---
jira_key: "PED-935"
aliases: ["PED-935"]
summary: "API - Refactor - Agregar \"companyCode\" a las ordenes de compra"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-01-23 07:17"
updated: "2025-01-24 16:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-935"
---

# PED-935: API - Refactor - Agregar "companyCode" a las ordenes de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-01-23 07:17 |
| Actualizado | 2025-01-24 16:27 |
| Etiquetas | ninguna |
| Jira | [PED-935](https://bluinc.atlassian.net/browse/PED-935) |

## Relaciones

- **Padre:** [[PED-3]] Ordenes de compra

## Descripcion

```
GET {API_URL}/v1/orders
```

```
{
    "response": [
        {
            "date": "2025-01-23 01:32:33",
            "orderNumber": "10388403",
            "branchNumber": "0002",
            "albnumNumber": null,
            "realAlbumNumber": null,
            "clientDescription": "SEGAL GABRIEL ALEJANDRO",
            "clientId": 32702,
            "orderTypeId": 4,
            "observation": "PEDIDO DE INTERNET",
            "status": "P",
            "statusId": null,
            "statusDescription": "Pendiente",
            "invoice": null,
            "token": null,
            "voucherId": null,
            "sellerId": 8,
            "seller": "Altamiranda Andrea",
            "totalInPesos": 2675789.5550925,
            "total": 2268.41125,
            "finalTotal": 2506.594431,
            "shippingMethod": 3999,
            "codePostal": null,
            "currency": 1067.5,
            "perception": 0,
            "shippingLabel": false,
            "idLo": null,
            "mpExternalReference": null,
            "paymentMethodId": 3,
            "paymentMethodDescription": "Dep\u00f3sito en Banco",
            "joinShipping": false,
            "dropShipping": false,
            "paymentVoucher": false,
            "mpPaymentStatus": null,
            "liquidateDestinationBankName": "",
            "delivered": false,
            "internalTax": 0,
            "companyCode": "4"
        },
        {
      ...
```
