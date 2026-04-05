---
jira_key: "LIO-29"
aliases: ["LIO-29"]
summary: "API - Refactor - Al cancelar un pedido desde libre opcion, debe cambiar bien el estado \"cancelado\" y marcarlo como \"eliminado\" en \"Capa 1\""
status: "Finalizada"
type: "Subtarea"
priority: "Highest"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-06-04 10:16"
updated: "2024-06-19 12:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-29"
---

# LIO-29: API - Refactor - Al cancelar un pedido desde libre opcion, debe cambiar bien el estado "cancelado" y marcarlo como "eliminado" en "Capa 1"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Highest |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-06-04 10:16 |
| Actualizado | 2024-06-19 12:26 |
| Etiquetas | ninguna |
| Jira | [LIO-29](https://bluinc.atlassian.net/browse/LIO-29) |

## Relaciones

- **Padre:** [[LIO-28 - El sitio debe funcionar correctamente, sin puntos grises o cosas que no se|LIO-28]] El sitio debe funcionar correctamente, sin puntos grises o cosas que no se entienden
- **is blocked by:** [[LIO-53 - API - Al cancelar un pedido desde libre opción, cambiar estado a cancelado y|LIO-53]] API - Al cancelar un pedido desde libre opción, cambiar estado a "cancelado" y marcarlo como "eliminado" en "Capa 1" - Orden no anulada

## Descripcion

Modificaremos en la api legacy le recurso, para que ademas de cancelar el pedido desde el punto de vista de libre opción, lo haga tambien en capa 1

```
DELETE {API_URL}/pedidos/compras/{idcompra}
```

Osea que ademas de hacer eso, se debe marcar el pedido como cancelado, para el punto de vista de capa 1.

Es decir:

`[NewBytes_DBF].[dbo].[pedclit].lanula = 1`

Esto solo puede hacerse cuando aun no paso a remito (no tiene cnumalb en albclit)
