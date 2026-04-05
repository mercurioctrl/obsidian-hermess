---
jira_key: "PED-949"
aliases: ["PED-949"]
summary: "API - Refactor - Agregar el parametro \"cancelled\" en el recurso \"orders\""
status: "Finalizada"
type: "Subtarea"
priority: "Low"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-02-12 14:55"
updated: "2025-02-25 21:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-949"
---

# PED-949: API - Refactor - Agregar el parametro "cancelled" en el recurso "orders"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Low |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-12 14:55 |
| Actualizado | 2025-02-25 21:50 |
| Etiquetas | ninguna |
| Jira | [PED-949](https://bluinc.atlassian.net/browse/PED-949) |

## Relaciones

- **Padre:** [[PED-948]] Ordenes canceladas/eliminadas
- **has action item:** [[PED-950]] APP - Refactor - Agregar cancelacion visual (estado , tachado, opaciodad o algo)

## Descripcion

Agregaremos el parámetro `cancelled` para poder mostrar visualmente mas fácilmente los que están cancelados que a simple vista parecen pedidos normales (no cancelados)

```
GET {API_URL}/v1/orders?orderStatus=cancelled
```

```
{
    "response": [
        {
            "date": "2025-02-24 14:43:06",
            "orderNumber": "10393312",
            "branchNumber": "0002",
            "albnumNumber": null,
            "realAlbumNumber": null,
            "clientDescription": "DA SILVA NICOLAS EZEQUIEL",
            "clientId": 40795,
            "orderTypeId": 1,
            "observation": "DESCARGADO",
            "status": "P",
            "statusId": null,
            "statusDescription": "Pendiente",
            "invoice": null,
            "token": null,
            "voucherId": null,
            "sellerId": 30,
            "seller": "Albarracin Julian",
            "totalInPesos": 451320.61119850003,
            "total": 378.0055,
            "finalTotal": 417.696077,
            "shippingMethod": 3999,
            "codePostal": 1678,
            "currency": 1080.5,
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
            "companyCode": 4,
            "tracking": "",
            "cancelled": 0, <-- SE AGREGA
        },
        {
            "date": "2025-02-24 14:34:57",
            "orderNumber": "10393311",
            "branchNumber": "0002",
            "albnumNumber": null,
            "realAlbumNumber": null,
            "clientDescription": "BORTOLOT FABIANA ANDREA",
            "clientId": 87334,
            "orderTypeId": 5,
            "observation": "PEDIDO LIBRE OPCION",
            "status": "P",
            "statusId": null,
            "statusDescription": "Pendiente",
            "invoice": null,
            "token": null,
            "voucherId": null,
            "sellerId": 100,
            "seller": "Opcion Libre",
            "totalInPesos": 128131.27745,
            "total": 106.57489,
            "finalTotal": 119.191886,
            "shippingMethod": 4069,
            "codePostal": 1878,
            "currency": 1075,
            "perception": 0,
            "shippingLabel": false,
            "idLo": 682460,
            "mpExternalReference": "87ddb30c458c81d0e24f74008f79f055  ",
            "paymentMethodId": null,
            "paymentMethodDescription": null,
            "joinShipping": false,
```
