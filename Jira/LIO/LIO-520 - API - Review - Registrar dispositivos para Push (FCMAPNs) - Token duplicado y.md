---
jira_key: "LIO-520"
aliases: ["LIO-520"]
summary: "API - Review - Registrar dispositivos para Push (FCM/APNs) -> Token duplicado y fecha de actualización"
status: "Backlog"
type: "Subtarea"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Guillermo Avila"
created: "2026-01-22 15:59"
updated: "2026-01-22 16:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-520"
---

# LIO-520: API - Review - Registrar dispositivos para Push (FCM/APNs) -> Token duplicado y fecha de actualización

| Campo | Valor |
|-------|-------|
| Estado | Backlog (Por hacer) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Guillermo Avila |
| Creado | 2026-01-22 15:59 |
| Actualizado | 2026-01-22 16:21 |
| Etiquetas | ninguna |
| Jira | [LIO-520](https://bluinc.atlassian.net/browse/LIO-520) |

## Relaciones

- **Padre:** [[LIO-507]] Login y otros aspectos generales
- **clones:** [[LIO-512]] API - Feat - Registrar dispositivos para Push (FCM/APNs)

## Descripcion

Algunas observaciones sobre el recurso:

```
POST /v4/push/devices
```

## 

- Al utilizar un `token` con otro usuario (habiéndose registrado previamente con un usuario), aparece un error 500.



> 409 Conflict: violación de unicidad no resoluble (ej: token duplicado y no se puede reasignar por política) (idealmente lo resolvés por reasignación y evitás este 409).


[adjunto]


- Al momento de ejecutar el recurso de nuevo (nueva visita), con los mismos parámetros, la fecha de `UpdatedAt` se desfasa por cuatro horas. Se toma como referencia la fecha en `LastSeenAt`



[adjunto]


##
