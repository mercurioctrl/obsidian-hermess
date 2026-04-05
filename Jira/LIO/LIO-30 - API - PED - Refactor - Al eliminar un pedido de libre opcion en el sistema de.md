---
jira_key: "LIO-30"
aliases: ["LIO-30"]
summary: "API - PED - Refactor - Al eliminar un pedido de libre opcion en el sistema de pedidos, se debe marcar como \"cancelado\" en la plataforma libre opcion"
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-06-04 10:20"
updated: "2024-06-19 12:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-30"
---

# LIO-30: API - PED - Refactor - Al eliminar un pedido de libre opcion en el sistema de pedidos, se debe marcar como "cancelado" en la plataforma libre opcion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-04 10:20 |
| Actualizado | 2024-06-19 12:26 |
| Etiquetas | ninguna |
| Jira | [LIO-30](https://bluinc.atlassian.net/browse/LIO-30) |

## Relaciones

- **Padre:** [[LIO-28 - El sitio debe funcionar correctamente, sin puntos grises o cosas que no se|LIO-28]] El sitio debe funcionar correctamente, sin puntos grises o cosas que no se entienden
- **is blocked by:** [[LIO-54 - API - PED - Refactor - Al eliminar un pedido de libre opción en el sistema de|LIO-54]] API - PED - Refactor - Al eliminar un pedido de libre opción en el sistema de pedidos, se debe marcar como "cancelado" en la plataforma libre opción - Orden no cancelada

## Descripcion

Alreves de como se hace en [link](https://lioteam.atlassian.net/browse/LIO-29) 

Desde el punto de vista de pedidos, se debe poder cancelar los mismos en libre opción, cuando se los elimina en capa uno.

```
DELETE /v1/orders/{branch-order}
```

En caso de que el pedido que estamos eliminando (`lanulado=1`) lo marcaremos como cancelado en libre opción.

`[LO].[dbo].[pedidosCabecera].[canceladoLibreOpcion]` =1
