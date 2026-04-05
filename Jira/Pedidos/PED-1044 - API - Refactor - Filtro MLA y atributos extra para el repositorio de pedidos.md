---
jira_key: "PED-1044"
aliases: ["PED-1044"]
summary: "API - Refactor - Filtro MLA y atributos extra para el repositorio de pedidos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-07-11 13:36"
updated: "2025-07-15 10:30"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1044"
---

# PED-1044: API - Refactor - Filtro MLA y atributos extra para el repositorio de pedidos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-07-11 13:36 |
| Actualizado | 2025-07-15 10:30 |
| Etiquetas | ninguna |
| Jira | [PED-1044](https://bluinc.atlassian.net/browse/PED-1044) |

## Relaciones

- **Padre:** [[PED-915 - MercadoLibre|PED-915]] MercadoLibre
- **has action item:** [[PED-1047 - APP - Refactor - Filtrar pedidos de mercadolibre|PED-1047]] APP - Refactor - Filtrar pedidos de mercadolibre

## Descripcion

Según lo conversado, la idea es introducir un nuevo filtro para ver solamente los de mercadolibre, y en ese caso agregaremos la informacion anexa que tenemos.

```
GET {API_URL}/v1/orders?ml=true
```

Cuando recibo el parámetro en `true` debo anexar la tabla `[NewBytes_DBF].[dbo].[pedcliML]`

y agregar los nuevos parámetros

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
            "ticketStatus": 0,
            "mla": "2000008461027217",
            "created_at": "2025-10-07T11:00:01", <-- SE AGREGA
            "closed_at": "2025-10-07T11:00:05",  <-- SE AGREGA
            "status": "paid",  <-- SE AGREGA
            "total_amount": 54218.0,  <-- SE AGREGA
            "amount_paid": 54218.0,  <-- SE AGREGA
            "seller": "DD20240923144352", <--  SE AGREGA
            "buyer": "GENAGUS", , <-- SE AGREGA
            "payment_method": "credit_card", <-- SE AGREGA
            "billed": null  <-- SE AGREGA
            }
      ....
```
