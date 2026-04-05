---
jira_key: "COM-285"
aliases: ["COM-285"]
summary: "APP - Review - Revisar por que no anda correctamente el subtotal de una orden en la edición de la misma"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Marbe Moreno"
created: "2026-03-04 08:56"
updated: "2026-03-05 10:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-285"
---

# COM-285: APP - Review - Revisar por que no anda correctamente el subtotal de una orden en la edición de la misma

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Marbe Moreno |
| Creado | 2026-03-04 08:56 |
| Actualizado | 2026-03-05 10:22 |
| Etiquetas | ninguna |
| Jira | [COM-285](https://bluinc.atlassian.net/browse/COM-285) |

## Relaciones

- **Padre:** [[COM-8]] Ordenes de compra

## Descripcion

no muestra el subtotal final cuando se edita las cantidades de una orden de compra

El front esta esperando que en el objeto de respuesta del patch venga el `finalPrice`

PATCH - [https://api.purchases.lio.red/v1/providerOrder/12576](https://api.purchases.lio.red/v1/providerOrder/12576)



```

{
    "state": "success",
    "response": "Item actualizado correctamente",
    "code": 200,
    "item": {
        "id": 122358,
        "amount": 1,
        "price": {
            "value": 15,
            "iva": 0,
             "finalPrice": 15 //-> falta que lo retorne
        },
        "position": null,
        "taxPosition": null
    }
}
```
