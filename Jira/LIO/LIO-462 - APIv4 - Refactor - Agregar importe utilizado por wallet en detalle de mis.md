---
jira_key: "LIO-462"
aliases: ["LIO-462"]
summary: "APIv4 - Refactor - Agregar importe utilizado por wallet en detalle de mis compras"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-09-24 14:36"
updated: "2025-10-01 10:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-462"
---

# LIO-462: APIv4 - Refactor - Agregar importe utilizado por wallet en detalle de mis compras

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-09-24 14:36 |
| Actualizado | 2025-10-01 10:40 |
| Etiquetas | ninguna |
| Jira | [LIO-462](https://bluinc.atlassian.net/browse/LIO-462) |

## Relaciones

- **Padre:** [[LIO-281]] Compras
- **action item from:** [[LIO-463]] APP - Refactor - Agregar importe utilizado por wallet en detalle de mis compras

## Descripcion

Se debe agregar al recurso 

```
GET /v4/purchase/{ID  de pedido cabecear}
```



los campos  `walletUsedHere`  y `walletUsedHereTolta` permtiendo ver en el detalle de una compra cuanto se utilizo con la wallet. y tambien ver el total utilizado en el pedido completo.

Ejemplo:

```
{
    "id": 747025,
    "fechaCreacion": "2025-09-16 10:17:34",
    "envio": {
       ...
    },
    "retiro": {
        
    },
    "pago": {
       ...
    },
    "descuentoLO": 0,
    "walletUsedHereTotal": 1000, --> campo utilizado para el total del pedido.
    "orderNb": "10425758",
    "subtotal": 7631,
    "productos": [
        {
            "id": 695592,
            "enNB": true,
            "titulo": "MOUSE GENIUS [[NX-7000]] BLACK WIRELESS NEW G5",
            "img": "519fea729a921c5da7417f8545cd6c78.jpg",
            "cantidad": 1,
            "precio": 7631,
            "descuento": 0,
            "descuentoLO": 0,
            "walletUsedHere": 1000, --> campo con el importe utilizado para el items
            "interesPago": 0,
            ...
        }
    ],
    "cliente": {
        "id": 274942,
        ...
    },
    "resumenVendedor": {
		...
    }
}
```
