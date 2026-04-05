---
jira_key: "PED-1043"
aliases: ["PED-1043"]
summary: "API - Refactor - Agregar MLA al recurso de las ordenes"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-07-11 13:32"
updated: "2025-07-22 11:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1043"
---

# PED-1043: API - Refactor - Agregar MLA al recurso de las ordenes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-11 13:32 |
| Actualizado | 2025-07-22 11:51 |
| Etiquetas | ninguna |
| Jira | [PED-1043](https://bluinc.atlassian.net/browse/PED-1043) |

## Relaciones

- **Padre:** [[PED-915]] MercadoLibre
- **has action item:** [[PED-1046]] APP - Refactor - Cuando una orden cuenta con el atributo MLA se debe marcar como una compra de mercadolibre

## Descripcion

```
GET {API_URL}/v1/orders
```

```
{
    "response": [
        {
            "date": "2025-07-11 13:29:57",
            "orderNumber": "10418171",
            "branchNumber": "0002",
            "albnumNumber": null,
            "realAlbumNumber": null,
            "clientDescription": "OVERDRIVE S.A",
            "clientId": 9657,
            "orderTypeId": 4,
            "observation": "PEDIDO DE INTERNET",
            "status": "P",
            "statusId": null,
            "statusDescription": "Pendiente",
            "invoice": null,
            "token": null,
            "voucherId": null,
            "sellerId": 5,
            "seller": "Contardi Patricio",
            "totalInPesos": 488854.737,
            "total": 329.112,
            "finalTotal": 383.41548,
            "shippingMethod": 3999,
            "codePostal": 1056,
            "currency": 1275,
            "perception": 19.74672,
            "shippingLabel": false,
            "idLo": null,
            "mpExternalReference": null,
            "mpPaymentId": null,
            "paymentMethodId": 3,
            "paymentMethodDescription": "Dep\u00f3sito en Banco",
            "joinShipping": false,
            "dropShipping": false,
            "paymentVoucher": false,
            "mpPaymentStatus": null,
            "liquidateDestinationBankName": "",
            "delivered": false,
            "internalTax": 0,
            "companyCode": 4,
            "tracking": "",
            "cancelled": 0,
            "ticketStatus": 0
        },
        {
            "date": "2025-07-11 13:29:56",
            "orderNumber": "10418170",
            "branchNumber": "0002",
            "albnumNumber": null,
            "realAlbumNumber": null,
            "clientDescription": "OLAH DAVID",
            "clientId": 18643,
            "orderTypeId": 2,
            "observation": "INTERNO",
            "status": "P",
            "statusId": null,
            "statusDescription": "Pendiente",
            "invoice": null,
            "token": null,
            "voucherId": null,
            "sellerId": 51,
            "seller": "Lautaro Soto",
            "totalInPesos": 263228.85000000003,
            "total": 165.1632,
            "finalTotal": 206.454,
            "shippingMethod": 0,
            "codePostal": 7000,
            "currency": 1275,
            "perception": 6.606528,
            "shippingLabel": false,
            "idLo": null,
            "mpExternalReference": null,
            "mpPaymentId": null,
            "paymentMethodId": null,
            "paymentMethodDescription": null,
            "joinShipping": false,
            "dropShipping": false,
            "paymentVoucher": false,
            "mpPaymentStatus": null,
            "liquidateDestinationBankName": "",
            "delivered": false,
            "internalTax": 0,
            "companyCode": 4,
            "tracking": "",
            "cancelled": 0,
            "ticketStatus": 0
            "mla": 2342343242 <-- SE AGREGA EL MLA DE pedclit, sino viene en null
        },
        {
            "date": "2025-07-11 13:27:55",
```
