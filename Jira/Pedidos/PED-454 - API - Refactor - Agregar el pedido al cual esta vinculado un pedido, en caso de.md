---
jira_key: "PED-454"
aliases: ["PED-454"]
summary: "API - Refactor - Agregar el pedido al cual esta vinculado un pedido, en caso de que exista a las condiciones"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-01-07 21:23"
updated: "2024-01-11 18:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-454"
---

# PED-454: API - Refactor - Agregar el pedido al cual esta vinculado un pedido, en caso de que exista a las condiciones

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-07 21:23 |
| Actualizado | 2024-01-11 18:15 |
| Etiquetas | ninguna |
| Jira | [PED-454](https://bluinc.atlassian.net/browse/PED-454) |

## Relaciones

- **Padre:** [[PED-123]] Feat - Liquidar pedido
- **blocks:** [[PED-455]] APP - Feat - Desunir pedido de otro envio ()

## Descripcion

Agregaremos un parámetro nuevo para indicar el host al cual esta vinculado un pedido en la lectura de los datos guardados para elpedidos.

```
GET {API_URL}/v1/makeSaleConditions/{pedido}
```

```
[
  {
    "id": 93644,
    "pedido": "X000200570446",
    "paymentMethodId": 3,
    "shippingMethod": 20,
    "bankId": 13,
    "manualCurrencyQuote": 10500000000.0,
    "comment": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem",
    "joinShippingHost": "X000200570436" <--- NUEVO PARAMETRO
    
  }
]
```
