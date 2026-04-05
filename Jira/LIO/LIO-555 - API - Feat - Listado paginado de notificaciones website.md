---
jira_key: "LIO-555"
aliases: ["LIO-555"]
summary: "API - Feat -  Listado paginado de notificaciones website"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2026-02-23 17:37"
updated: "2026-03-09 18:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-555"
---

# LIO-555: API - Feat -  Listado paginado de notificaciones website

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2026-02-23 17:37 |
| Actualizado | 2026-03-09 18:41 |
| Etiquetas | ninguna |
| Jira | [LIO-555](https://bluinc.atlassian.net/browse/LIO-555) |

## Relaciones

- **Padre:** [[LIO-550]] Migración de notificaciones LO Legacy → V4

## Descripcion

Endpoint paginado de notificaciones website

```
GET /notifications/website/paginate
```


Descripción: Retorna notificaciones website paginadas (offset fijo de 20).
