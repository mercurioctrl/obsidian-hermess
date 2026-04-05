---
jira_key: "EXP-331"
aliases: ["EXP-331"]
summary: "API - Feat - Eliminar etiqueta de envio"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-07-04 10:27"
updated: "2023-07-24 08:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-331"
---

# EXP-331: API - Feat - Eliminar etiqueta de envio

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-07-04 10:27 |
| Actualizado | 2023-07-24 08:52 |
| Etiquetas | ninguna |
| Jira | [EXP-331](https://bluinc.atlassian.net/browse/EXP-331) |

## Relaciones

- **Padre:** [[EXP-13]] Feat - Etiquetas y seguimiento
- **blocks:** [[EXP-333]] APP - Feat - Eliminar etiqueta de envio

## Descripcion

Se trata de una feat necesaria para evitar el reporte “Necesito que me borre una etiqueta”.

```
DELETE {{API_URL}}/v1/shipments/deleteTrackingOrder/{branch}/{order}
```

Lo que hace es eliminar el tracking de `pedclict` y `trackingNumbers`

Es importante verificar que el pedido ya no este en estado entregado, ni que tenga fecha de dropeado, en ese caso no puede borrarse.
