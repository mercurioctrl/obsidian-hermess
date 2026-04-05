---
jira_key: "STASK-31"
aliases: ["STASK-31"]
summary: "API - Task - Feat - Implementación Endpoint Legacy Notifications - POST /notifications"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2026-03-05 11:04"
updated: "2026-03-11 10:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/STASK-31"
---

# STASK-31: API - Task - Feat - Implementación Endpoint Legacy Notifications - POST /notifications

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2026-03-05 11:04 |
| Actualizado | 2026-03-11 10:59 |
| Etiquetas | ninguna |
| Jira | [STASK-31](https://bluinc.atlassian.net/browse/STASK-31) |

## Relaciones

- **Padre:** [[STASK-15 - Sistema de Notificaciones Multicanal (Queue + Workers)|STASK-15]] Sistema de Notificaciones Multicanal (Queue + Workers)

## Descripcion

Se debe implementar el endpoint **POST **`/notifications` en `service-task-v3` para mantener compatibilidad con el sistema legacy de notificaciones, el cual aún es consumido por otros microservicios.

El sistema `legacy-notification` fue migrado parcialmente a `service-task-v3`, pero actualmente no se encuentra disponible el endpoint principal **POST **`/notifications`, encargado de crear notificaciones multi-canal.

Otros microservicios continúan dependiendo de este endpoint, por lo que es necesario replicar su comportamiento en el nuevo servicio.



Se debe desarrollar el endpoint **POST **`/notifications/` en `service-task-v3` cumpliendo con los siguientes requerimientos:

#### Requisitos funcionales

- Mantener **compatibilidad 100%** con el payload y response del sistema legacy.


- Soportar los siguientes canales:

- `push`


- `mailing`


- `website`




- Crear automáticamente usuarios con estado `"pending"` si no existen.


- Implementar acortamiento de URLs.


- Generar tokens únicos utilizando algoritmo [[SHA-512]].


- Validar reglas de negocio:

- `users` obligatorio


- `channels` obligatorio


- URL única entre canales




- Garantizar atomicidad mediante transacciones de base de datos.



### Endpoint esperado

#### POST `/api/notifications/`

#### Request esperado

```json
{
  "users": {
    "receiver": 274942,
    "transmitter": 1
  },
  "channels": [
    {
      "service": "push",
      "content": {
        "text": "Nueva notificación",
        "url": "https://example.com/path"
      },
      "priority": 1
    }
  ]
}
```

#### Response esperado (201)

```
"La notificación se creó exitosamente!"
```



### Tablas involucradas

- `LO.dbo.notifications_header`


- `LO.dbo.notifications_push`


- `LO.dbo.notifications_mailing`


- `LO.dbo.notifications_website`


- `LO.dbo.legacy_notification_users`





### Impacto esperado

- Mantener compatibilidad con microservicios existentes.


- No requerir cambios en clientes que actualmente consumen el endpoint legacy.


- Exponer el endpoint como público (sin autenticación), replicando el comportamiento original.


- Permitir completar la migración del sistema legacy a `service-task-v3`.





El endpoint de esta tarea es el -> {{API_URL}}/v1/notification/legacy
