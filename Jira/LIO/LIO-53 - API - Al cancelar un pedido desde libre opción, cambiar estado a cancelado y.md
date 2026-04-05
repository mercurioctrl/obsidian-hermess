---
jira_key: "LIO-53"
aliases: ["LIO-53"]
summary: "API - Al cancelar un pedido desde libre opción, cambiar estado a \"cancelado\" y marcarlo como \"eliminado\" en \"Capa 1\" - Orden no anulada"
status: "Finalizada"
type: "Error"
priority: "Highest"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-06-19 02:20"
updated: "2024-06-19 12:18"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-53"
---

# LIO-53: API - Al cancelar un pedido desde libre opción, cambiar estado a "cancelado" y marcarlo como "eliminado" en "Capa 1" - Orden no anulada

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Highest |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-06-19 02:20 |
| Actualizado | 2024-06-19 12:18 |
| Etiquetas | ninguna |
| Jira | [LIO-53](https://bluinc.atlassian.net/browse/LIO-53) |

## Relaciones

- **blocks:** [[LIO-29]] API - Refactor - Al cancelar un pedido desde libre opcion, debe cambiar bien el estado "cancelado" y marcarlo como "eliminado" en "Capa 1"

## Descripcion

Al intentar cancelar un pedido recién creado me devuelve un array vacío, adicional a esto la orden no se marca como anulada.
`580728`
`0002-10332856`

[adjunto]
[adjunto]
