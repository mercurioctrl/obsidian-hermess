---
jira_key: "PED-82"
aliases: ["PED-82"]
summary: "API - Feat - Ver detalle de una orden de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-09-20 10:17"
updated: "2024-04-15 20:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-82"
---

# PED-82: API - Feat - Ver detalle de una orden de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-20 10:17 |
| Actualizado | 2024-04-15 20:10 |
| Etiquetas | ninguna |
| Jira | [PED-82](https://bluinc.atlassian.net/browse/PED-82) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra
- **blocks:** [[PED-83]] APP - Feat - Ver detalle de una orden de compra
- **blocks:** [[PED-101]] API - Feat - Ver detalle de una orden de compra -> Agregar cotizacion
- **relates to:** [[PED-476]] API - Ver detalle de una orden de compra - Creador de la orden vacío
- **relates to:** [[PED-671]] API - Ver detalle de una orden de compra - Vendedor vacío

## Descripcion

Agregaremos un recurso que sirve para mostrar el detalle de una orden, es decir su contenido.

```
GET {API_URL}/v1/orders/{branch-order}
```

Devuelve

```json
{
"agentDescription": "Andrea Altamiranda",
"agentId": 45,
"createdBy": "Andrea Altamiranda",
"albNumber": "10328179",
"invoiceBranch": "0003",
  "invoiceNumber": "00005433",
  "invoiceType": "B",
  "voucherId": 510381,
  "voucherUrl": "https:\/\/omega.comprobantes.lio.red\/voucher\/F\/510381\/6af1b94f4d21a2738ca76c44391d56?show=1"
"items": 
    [
        {
            "orderId": "10281918",
            "branch": "0002",
            "clientId": "019227",
            "description": "ACCESORIOS PHILIPS HUE CABLE 2M RGB LIGHTSTRIP PLUS V4",
            "itemId": "113234",
            "amount": "1.000",
            "status": "P",
            "value": "56.79523",
            "iva": "21.00",
            "price": {
                "value": 56.79523,
                "iva": 21,
                "finalPrice": 68.7222283
            }
        },
        {
            "orderId": "10281918",
            "branch": "0002",
            "clientId": "019227",
            "description": "ACCESORIOS GENERICO CABLE MONITOR VGA",
            "itemId": "111770",
            "amount": "1.000",
            "status": "P",
            "value": "18.72000",
            "iva": "21.00",
            "price": {
                "value": 18.72,
                "iva": 21,
                "finalPrice": 22.6512
            }
        },
        {
            "orderId": "10281918",
            "branch": "0002",
            "clientId": "019227",
            "description": "SSD SATA 480GB 2.5 PNY",
            "itemId": "109455",
            "amount": "1.000",
            "status": "P",
            "value": "74.36000",
            "iva": "21.00",
            "price": {
                "value": 74.36,
                "iva": 21,
                "finalPrice": 89.9756
            }
        }
    ]
}
```
