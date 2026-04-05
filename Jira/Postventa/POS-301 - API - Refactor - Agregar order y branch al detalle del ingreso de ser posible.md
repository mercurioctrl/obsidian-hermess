---
jira_key: "POS-301"
aliases: ["POS-301"]
summary: "API - Refactor - Agregar \"order\" y \"branch\" al detalle del ingreso de ser posible"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-04 15:49"
updated: "2024-07-08 11:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-301"
---

# POS-301: API - Refactor - Agregar "order" y "branch" al detalle del ingreso de ser posible

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-04 15:49 |
| Actualizado | 2024-07-08 11:07 |
| Etiquetas | ninguna |
| Jira | [POS-301](https://bluinc.atlassian.net/browse/POS-301) |

## Relaciones

- **Padre:** [[POS-19]] Ingresos
- **is blocked by:** [[POS-304]] API- Agregar order y branch al detalle del ingreso - Remito no visible

## Descripcion

```
GET {API_URL}/v1/afterSales/{ingreso}
```

```
[
    {
        "afterSaleId": 35109,
        "remito" : "X0020123123"
        "detailId": 58936,
        "serial": "103805000493",
        "quantity": 1,
        "productId": 103805,
        "productDescription": "JOYSTICK TRUST YULA PC PS3 GXT 540",
        "description": "no funciona el anal\u00f3gico derecho",
        "testStatus": "",
        "report": "",
        "testProductStatus": "",
        "testProductStatusId": 0,
        "comment": "",
        "productUrl": "https:\/\/www.nb.com.ar\/fromPostventa_-_103805",
        "stock": 30,
        "stockLio": 1,
        "isReady": false,
        "voucherNumber": null,
        "token": null,
        "passId": null,
        "passItemDescription": null,
        "passItemStatus": null,
        "passItemId": null,
        "passSerial": null,
        "isRecovery": false
    }
]
```
