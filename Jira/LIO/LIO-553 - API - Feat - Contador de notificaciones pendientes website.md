---
jira_key: "LIO-553"
aliases: ["LIO-553"]
summary: "API - Feat - Contador de notificaciones pendientes website"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2026-02-23 17:36"
updated: "2026-03-09 16:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-553"
---

# LIO-553: API - Feat - Contador de notificaciones pendientes website

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2026-02-23 17:36 |
| Actualizado | 2026-03-09 16:59 |
| Etiquetas | ninguna |
| Jira | [LIO-553](https://bluinc.atlassian.net/browse/LIO-553) |

## Relaciones

- **Padre:** [[LIO-550 - Migración de notificaciones LO Legacy → V4|LIO-550]] Migración de notificaciones LO Legacy → V4

## Descripcion

Endpoint contador de pendientes website



```
GET  /notifications/website/number/pending
```

Descripción: Retorna total de notificaciones pendientes (no vistas) para un usuario LO.



Este recurso devuelve el conteo de todas las notificaciones, es decir, incluye las pendientes y no pendientes.
