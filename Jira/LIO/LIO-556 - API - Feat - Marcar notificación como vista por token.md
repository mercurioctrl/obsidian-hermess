---
jira_key: "LIO-556"
aliases: ["LIO-556"]
summary: "API - Feat - Marcar notificación como vista por token"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2026-02-23 17:37"
updated: "2026-03-16 13:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-556"
---

# LIO-556: API - Feat - Marcar notificación como vista por token

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2026-02-23 17:37 |
| Actualizado | 2026-03-16 13:27 |
| Etiquetas | ninguna |
| Jira | [LIO-556](https://bluinc.atlassian.net/browse/LIO-556) |

## Relaciones

- **Padre:** [[LIO-550]] Migración de notificaciones LO Legacy → V4

## Descripcion

Endpoint marcar notificación como vista por token

```
POST /notifications/{token}/mark-view
```


Descripción: Marca view_at de la cabecera de notificación usando el token en URL.
