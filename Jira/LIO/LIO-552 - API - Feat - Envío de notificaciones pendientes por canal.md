---
jira_key: "LIO-552"
aliases: ["LIO-552"]
summary: "API - Feat -  Envío de notificaciones pendientes por canal"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2026-02-23 17:36"
updated: "2026-03-09 13:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-552"
---

# LIO-552: API - Feat -  Envío de notificaciones pendientes por canal

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2026-02-23 17:36 |
| Actualizado | 2026-03-09 13:19 |
| Etiquetas | ninguna |
| Jira | [LIO-552](https://bluinc.atlassian.net/browse/LIO-552) |

## Relaciones

- **Padre:** [[LIO-550]] Migración de notificaciones LO Legacy → V4

## Descripcion

**Movido**: Este endpoint fue movido a task v3. para centralizar todas las acciones que disparan notificaciones en ese microservicio.

por lo que esta tarea no tiene implementacion en LO-V4. adjunto tarea relacionada.

[link](https://bluinc.atlassian.net/browse/STASK-29) 



Endpoint de envío de pendientes por canal

```
POST /notifications/send/pendings/{channel}
```



Descripción: Ejecuta envío de pendientes para el canal recibido por path param.
