---
jira_key: "LIO-566"
aliases: ["LIO-566"]
summary: "API - Feat - LO - v3 -Migración NotificationService a Task-v3"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2026-03-05 16:19"
updated: "2026-03-16 13:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-566"
---

# LIO-566: API - Feat - LO - v3 -Migración NotificationService a Task-v3

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2026-03-05 16:19 |
| Actualizado | 2026-03-16 13:50 |
| Etiquetas | ninguna |
| Jira | [LIO-566](https://bluinc.atlassian.net/browse/LIO-566) |

## Relaciones

- **Padre:** [[LIO-507]] Login y otros aspectos generales

## Descripcion

Refactorización de `NotificationService` para migrar desde el servicio legacy de notificaciones hacia los nuevos microservicios laravel-v4 y task-v3.



**Importante aclaración**

Si bien los servicios apuntan a v4 no se utilizaran mas desde LO-V3 aun asi se mantiene para evitar romper con alguna acomplamiento.

El que realmente es importante es el de task-v3 el cual es utilizado en todas las partes del legacy LO-V3 : verificacion, compras, chats → por el momento se seguira utilizando hasta ser totalmente deprecado. 



### Mapeo de Endpoints

| Método | Servicio Anterior | Servicio Nuevo |
| --- | --- | --- |
| `addTokenForPush()` | legacy-notification | laravel-v4 `/push/devices` |
| `getNumberPendings()` | legacy-notification | laravel-v4 `/notification/number/pending` |
| `getLastPendings()` | legacy-notification | laravel-v4 `/notification/last/pending` |
| `getPaginate()` | legacy-notification | laravel-v4 `/notification/paginate` |
| `create()` | legacy-notification | task-v3 `/notification` |

#### Variables de Entorno Requeridas

Agregar en `.env` de todos los ambientes:

```bash
URL_LARAVEL_V4=https://api-laravel-v4.libreopcion.com
URL_TASK_V3=https://api-task-v3.libreopcion.com
```
