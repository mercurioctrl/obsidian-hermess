---
jira_key: "EXP-507"
aliases: ["EXP-507"]
summary: "API - nuevo recurso para obtener seriales en xlsx"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Ezequiel manzano"
created: "2025-09-04 13:26"
updated: "2025-09-08 20:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-507"
---

# EXP-507: API - nuevo recurso para obtener seriales en xlsx

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Ezequiel manzano |
| Creado | 2025-09-04 13:26 |
| Actualizado | 2025-09-08 20:02 |
| Etiquetas | ninguna |
| Jira | [EXP-507](https://bluinc.atlassian.net/browse/EXP-507) |

## Relaciones

- **relates to:** [[SNB-3304]] agregar al sistema
- **has action item:** [[EXP-508]] APP - Nuevo boton para obtener seriales en xlsx en Ingresos 

## Descripcion

```powershell
curl --location 'https://gamma.api.warehouse.lio.red//v1/providersOrders/00010477/xlsx' \
--header 'Authorization: ••••••'
```

El recurso devolvera un xlsx, se puede obtener tmb solo del item con el param ?itemId=1123223
