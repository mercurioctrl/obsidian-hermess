---
jira_key: "PED-83"
aliases: ["PED-83"]
summary: "APP - Feat - Ver detalle de una orden de compra"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-09-20 10:17"
updated: "2024-01-26 18:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-83"
---

# PED-83: APP - Feat - Ver detalle de una orden de compra

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-20 10:17 |
| Actualizado | 2024-01-26 18:05 |
| Etiquetas | ninguna |
| Jira | [PED-83](https://bluinc.atlassian.net/browse/PED-83) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra
- **is blocked by:** [[PED-82]] API - Feat - Ver detalle de una orden de compra
- **relates to:** [[PED-367]] APP - Ver detalle de una orden de compra - Incidencias varias
- **relates to:** [[PED-453]]   APP - Ver detalle de una orden de compra - IVA vacío
- **relates to:** [[PED-518]] APP - Refactor - Ver detalle de una orden de compra - Actualizar subtotales

## Descripcion

Usando el recurso [https://lioteam.atlassian.net/browse/PED-82](https://lioteam.atlassian.net/browse/PED-82) 
Mostraremos un modal similar a este para ver el contenido del producto 

Se deben mostrar adicionalmente los nuevos paramtros

- Vendedor


- Creador


- Pedido


- Invoice



[adjunto]
[adjunto]


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
