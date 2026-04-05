---
jira_key: "PED-964"
aliases: ["PED-964"]
summary: "API - Feat - Cerrar ticket "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-03-04 19:19"
updated: "2025-03-07 04:54"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-964"
---

# PED-964: API - Feat - Cerrar ticket 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-04 19:19 |
| Actualizado | 2025-03-07 04:54 |
| Etiquetas | ninguna |
| Jira | [PED-964](https://bluinc.atlassian.net/browse/PED-964) |

## Relaciones

- **Padre:** [[PED-960]] Tickets de pedido
- **has action item:** [[PED-966]] APP - Feat - Agregar modal para visualizar y responder tickets al ejecutar el accionable en el indicador de ticket para una orden

## Descripcion

```
PATCH {API_URL}/v1/orders/{branch-order}/ticket/resolved
```

Este recurso sirve para cuando el usuario ya ve que esta resuelto, puede marcarlo como resuelto y solo cambia en caso de estar abierto `"open": false`

Seguiremos ademas, lo realizado en el refactor [link](https://lioteam.atlassian.net/browse/LIO-244)  de tal forma que cada vez que generamos un comentario marcaremos

`[NewBytes_DBF].[dbo].[pedclitTicket].pending=false`
