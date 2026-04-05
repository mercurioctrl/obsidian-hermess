---
jira_key: "POS-268"
aliases: ["POS-268"]
summary: "APP -Feat - Marcar rechazados en enviados a proveedores"
status: "CodeReview"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-09-22 16:37"
updated: "2023-10-19 11:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-268"
---

# POS-268: APP -Feat - Marcar rechazados en enviados a proveedores

| Campo | Valor |
|-------|-------|
| Estado | CodeReview (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-22 16:37 |
| Actualizado | 2023-10-19 11:25 |
| Etiquetas | ninguna |
| Jira | [POS-268](https://bluinc.atlassian.net/browse/POS-268) |

## Relaciones

- **Padre:** [[POS-235]] Postventa Proveedores Recepcion

## Descripcion

Crearemos un recurso que sirve para “marcar como rechazado” basado en 

```
DELETE {{API_URL}}/v1/sendToProvider/reject
```

Payload:

```json
{
    "afterSaleId": [
    "33209",
    "33219"
    ],
    "headerId": 14103
}
```

[adjunto]
Para esto agregaremos en cada fila del item un checkbox, y al seleccionar uno o mas haremos aparecer el botón “Marcar como rechazado” para ejecutar el recurso
