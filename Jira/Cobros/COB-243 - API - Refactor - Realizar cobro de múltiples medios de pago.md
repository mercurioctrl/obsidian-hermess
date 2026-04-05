---
jira_key: "COB-243"
aliases: ["COB-243"]
summary: "API - Refactor - Realizar cobro de múltiples medios de pago"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-11-29 11:37"
updated: "2023-01-26 08:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-243"
---

# COB-243: API - Refactor - Realizar cobro de múltiples medios de pago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-29 11:37 |
| Actualizado | 2023-01-26 08:42 |
| Etiquetas | ninguna |
| Jira | [COB-243](https://bluinc.atlassian.net/browse/COB-243) |

## Relaciones

- **Padre:** [[COB-242 - Refactor - Modal de cobros para mezclar medios de pago diferentes|COB-242]] Refactor - Modal de cobros para mezclar medios de pago diferentes
- **is blocked by:** [[COB-126 - API - Feat - Realizar cobro|COB-126]] API - Feat - Realizar cobro
- **blocks:** [[COB-244 - APP - Refactor - Hacer dinámica la grilla de pago en el modal de cobro|COB-244]] APP - Refactor - Hacer dinámica la grilla de pago en el modal de cobro

## Descripcion

Haremos un refactor sobre el recurso de [link](https://lioteam.atlassian.net/browse/COB-126). El objeto es poder iterar cualquier combinación de pago que pretenda realizar un cliente.

Recibiremos un payload del siguiente tipo

```
[
    {
        "clientId": 25757,
        "pedido": "X000200420517",
        "finalAmount": 1144.74,
        "comment": "Algun comentario opcional",
        "payments": [
            {
                "paymentMethodId": 1,
                "amountPaid": "1000"
                "currenciId: 1,
                "bankAccountId": null
            },
            {
                "paymentMethodId": 2,
                "amountPaid": "34"
                "currenciId: 2,
                "bankAccountId": 3
            },
            {
                "paymentMethodId": 1,
                "amountPaid": "1000"
                "currenciId: 1,
                "bankAccountId": null
            }
        ]
    }
]
```
