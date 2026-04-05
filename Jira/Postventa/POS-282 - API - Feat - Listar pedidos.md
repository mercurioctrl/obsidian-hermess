---
jira_key: "POS-282"
aliases: ["POS-282"]
summary: "API - Feat - Listar pedidos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-02-21 13:33"
updated: "2024-03-02 18:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-282"
---

# POS-282: API - Feat - Listar pedidos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-02-21 13:33 |
| Actualizado | 2024-03-02 18:23 |
| Etiquetas | ninguna |
| Jira | [POS-282](https://bluinc.atlassian.net/browse/POS-282) |

## Relaciones

- **Padre:** [[POS-281]] Listar pedidos
- **blocks:** [[POS-283]] APP - Feat - Listar pedidos
- **is blocked by:** [[POS-286]] API - Listar pedidos - Observaciones del objeto respuesta

## Descripcion

Crearemos un nuevo repositorio encargado de listar los pedidos para que se puedan buscar desde postventa

```
GET {API_URL}/v1/orders?search={orderNumber|albnumber|clientId|clientName}&&between={intervalo de fechas}&itemId={itemId dentro del pedido}&sku={sku del producto dentro del pedido}
```

```
{
    "response": [
        {
            "date": "2024-02-16 17:53:20",
            "orderNumber": "10336951",
            "branchNumber": "0010",
            "albnumNumber": null,
            "clientDescription": "Altamiranda Dario",
            "clientId": 12621,
            "orderTypeId": 2,
            "observation": "INTERNO",
            "status": "P",
            "statusId": null,
            "statusDescription": "Pendiente",
            "invoice": null,
            "token": null,
            "voucherId": null,
            "sellerId": 12,
            "seller": "Sistema Web",
            "totalInPesos": 101060.69,
            "total": 118.2,
            "finalTotal": 118.2,
            "currency": 855,
            "perception": 0,
            "shippingLabel": false,
            "idLo": null,
        },
        {
            "date": "2024-02-16 17:53:20",
            "orderNumber": "10336951",
            "branchNumber": "0010",
            "albnumNumber": null,
            "clientDescription": "Altamiranda Dario",
            "clientId": 12621,
            "orderTypeId": 2,
            "observation": "INTERNO",
            "status": "P",
            "statusId": null,
            "statusDescription": "Pendiente",
            "invoice": null,
            "token": null,
            "voucherId": null,
            "sellerId": 12,
            "seller": "Sistema Web",
            "totalInPesos": 101060.69,
            "total": 118.2,
            "finalTotal": 118.2,
            "currency": 855,
            "perception": 0,
            "shippingLabel": false,
            "idLo": null,
        },
```

Solo podremos ver en este repositorio aquellos pedidos que cumplan con alblclit.ntipoalb > 1
