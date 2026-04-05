---
jira_key: "PED-694"
aliases: ["PED-694"]
summary: "API - Feat - Eliminacion logica de solicitud"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-04-24 09:47"
updated: "2024-04-24 19:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-694"
---

# PED-694: API - Feat - Eliminacion logica de solicitud

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-24 09:47 |
| Actualizado | 2024-04-24 19:42 |
| Etiquetas | ninguna |
| Jira | [PED-694](https://bluinc.atlassian.net/browse/PED-694) |

## Relaciones

- **Padre:** [[PED-201]] Solicitudes de Alta
- **blocks:** [[PED-695]] APP - Feat - Eliminar solocitud

## Descripcion

Agregaremos el recurso

```
DELETE /v1/clientsRequests/{requestId}
```

para realizar una eliminación lógica sobre las solicitudes y de esta forma poder limpiar y ver las que realmente son importantes y están pendientes
