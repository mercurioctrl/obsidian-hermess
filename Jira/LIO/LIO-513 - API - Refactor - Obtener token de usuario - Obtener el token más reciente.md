---
jira_key: "LIO-513"
aliases: ["LIO-513"]
summary: "API - Refactor - Obtener token de usuario - Obtener el token más reciente"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2026-01-15 11:13"
updated: "2026-01-22 13:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-513"
---

# LIO-513: API - Refactor - Obtener token de usuario - Obtener el token más reciente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2026-01-15 11:13 |
| Actualizado | 2026-01-22 13:05 |
| Etiquetas | ninguna |
| Jira | [LIO-513](https://bluinc.atlassian.net/browse/LIO-513) |

## Relaciones

- **Padre:** [[LIO-408 - Referidos|LIO-408]] Referidos
- **relates to:** [[LIO-409 - API - Feat - Crear un nuevo token de referidos por parte de un usuario|LIO-409]] API - Feat - Crear un nuevo token de referidos por parte de un usuario

## Descripcion

Realizaremos un refactor sobre el recurso para traer el token creado más reciente.

`LO.dbo.referrals`

```
GET {{API_URL}}/v4/referrals/token
```

[adjunto]
