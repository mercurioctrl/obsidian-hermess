---
jira_key: "PED-575"
aliases: ["PED-575"]
summary: "API - Feat - Agregar hash de mercadopago para mostrar comprobante"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2024-02-29 09:43"
updated: "2024-03-04 13:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-575"
---

# PED-575: API - Feat - Agregar hash de mercadopago para mostrar comprobante

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2024-02-29 09:43 |
| Actualizado | 2024-03-04 13:18 |
| Etiquetas | ninguna |
| Jira | [PED-575](https://bluinc.atlassian.net/browse/PED-575) |

## Relaciones

- **Padre:** [[PED-329 - Listado de ordenes|PED-329]] Listado de ordenes

## Descripcion

Se debe agrerga campo `mpExternalReference` en listado de ordenes para casos de LO.

con el fin de mostrar desde MercadoPago el comprobante.

```
GET {{API_URL}}/v1/orders?currentPage=1&itemsPerPage=15&sellerId=100
```

```
[{
            "date": "2024-02-29 02:11:25",
            "orderNumber": "10340203",
            "branchNumber": "0002",
            "albnumNumber": "X000200573786",
            "realAlbumNumber": "00573786",
            "clientDescription": "Mariano Merhy",
            "clientId": 81670,
            "orderTypeId": 5,
            "observation": "PEDIDO LIBRE OPCION",
            "status": "s",
            "statusId": 2,
            "statusDescription": "Autorizados. Pendiente a despachar",
            "invoice": null,
            "token": null,
            "voucherId": null,
            "sellerId": 100,
            "seller": "Libre Opcion",
            "totalInPesos": 215286.57,
            "total": 224.96,
            "finalTotal": 250.33,
            "shippingMethod": 3030,
            "codePostal": "",
            "currency": 860,
            "perception": 0,
            "shippingLabel": false,
            "idLo": 629789,
            "mpExternalReference": "23259b721401eedd29a12cee6ed41263",
            "paymentMethodId": 8,
            "paymentMethodDescription": "Mpago LO",
            "joinShipping": false
        }]
```
