---
jira_key: "PED-1266"
aliases: ["PED-1266"]
summary: "API - Review - Crear Acción de Marketing - CreatedByUserId nulo"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Guillermo Avila"
created: "2026-01-14 10:50"
updated: "2026-01-16 09:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1266"
---

# PED-1266: API - Review - Crear Acción de Marketing - CreatedByUserId nulo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Guillermo Avila |
| Creado | 2026-01-14 10:50 |
| Actualizado | 2026-01-16 09:57 |
| Etiquetas | ninguna |
| Jira | [PED-1266](https://bluinc.atlassian.net/browse/PED-1266) |

## Relaciones

- **Padre:** [[PED-1208]] Gestión de Aportes y Gastos de Marketing
- **clones:** [[PED-1211]] API - Feat - Crear Acción de Marketing

## Descripcion

No parece guardarse el `createdByUserId`

```
POST /v1/marketing/actions
```

[adjunto]
