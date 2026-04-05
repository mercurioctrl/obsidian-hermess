---
jira_key: "COB-244"
aliases: ["COB-244"]
summary: "APP - Refactor - Hacer dinámica la grilla de pago en el modal de cobro"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-11-30 09:06"
updated: "2024-02-14 15:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-244"
---

# COB-244: APP - Refactor - Hacer dinámica la grilla de pago en el modal de cobro

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-30 09:06 |
| Actualizado | 2024-02-14 15:47 |
| Etiquetas | ninguna |
| Jira | [COB-244](https://bluinc.atlassian.net/browse/COB-244) |

## Relaciones

- **Padre:** [[COB-242 - Refactor - Modal de cobros para mezclar medios de pago diferentes|COB-242]] Refactor - Modal de cobros para mezclar medios de pago diferentes
- **is blocked by:** [[COB-243 - API - Refactor - Realizar cobro de múltiples medios de pago|COB-243]] API - Refactor - Realizar cobro de múltiples medios de pago

## Descripcion

Basandonos en el recurso de [link](https://lioteam.atlassian.net/browse/COB-243) vamos a modificar el modal de cobro para poder agregar combinaciones de pago posibles de manera personalizada.

Inicialmente entonces, solo cargaremos el medio de pago especificado en la liquidación, cuando tengo seleccionado un pedido.

En caso contrario no mostraremos nada y el primero, sera el que agreguemos.

[adjunto]
Al hacer clic en agregar

Debo poder seleccionar el medio de pago del repositorio de medios de pago [link](https://lioteam.atlassian.net/browse/COB-31) y en caso de estar interactuando con un banco, tambien debo selecionarlo [link](https://lioteam.atlassian.net/browse/COB-165)

Armaremos un payload del siguiente tipo

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
