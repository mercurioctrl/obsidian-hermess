---
jira_key: "EXP-405"
aliases: ["EXP-405"]
summary: "API - Feat - Agregar parametro dropShipping al listado de despacho de envios"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-03-27 13:07"
updated: "2024-04-21 21:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-405"
---

# EXP-405: API - Feat - Agregar parametro dropShipping al listado de despacho de envios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-03-27 13:07 |
| Actualizado | 2024-04-21 21:07 |
| Etiquetas | ninguna |
| Jira | [EXP-405](https://bluinc.atlassian.net/browse/EXP-405) |

## Relaciones

- **Padre:** [[EXP-404]] DropShipping
- **is blocked by:** [[EXP-49]] API - Feat - Listar pedidos para envío
- **blocks:** [[EXP-406]] APP - Feat - Agregar parametro dropShipping al listado de despacho de envios

## Descripcion

```
GET {API_URL}/v1/shipments
```

Agregar al objeto el parámetro dropShipping en caso de que lo tenga el pedido
