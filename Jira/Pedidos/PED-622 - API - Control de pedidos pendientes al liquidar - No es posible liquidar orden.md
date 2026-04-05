---
jira_key: "PED-622"
aliases: ["PED-622"]
summary: "API - Control de pedidos pendientes al liquidar - No es posible liquidar orden pendiente"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Guillermo Avila"
created: "2024-03-20 12:07"
updated: "2024-03-21 16:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-622"
---

# PED-622: API - Control de pedidos pendientes al liquidar - No es posible liquidar orden pendiente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Guillermo Avila |
| Creado | 2024-03-20 12:07 |
| Actualizado | 2024-03-21 16:16 |
| Etiquetas | ninguna |
| Jira | [PED-622](https://bluinc.atlassian.net/browse/PED-622) |

## Relaciones

- **Padre:** [[PED-4 - Pedidos|PED-4]] Pedidos
- **blocks:** [[PED-617 - API - Refactor - Control de pedidos pendientes al liquidar|PED-617]] API - Refactor - Control de "pedidos pendientes" al liquidar

## Descripcion

1. No me permite liquidar una orden pendiente.

[adjunto]
Dato extra:
Sugeriría que la restricción de liquidación se aplicará solo para ordenes con cantidad de días menores a `xRemitoVto`
