---
jira_key: "STASK-4"
aliases: ["STASK-4"]
summary: "PED - Feat - Crear notificaciones en firebase"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-09-04 08:49"
updated: "2025-02-18 14:28"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/STASK-4"
---

# STASK-4: PED - Feat - Crear notificaciones en firebase

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-04 08:49 |
| Actualizado | 2025-02-18 14:28 |
| Etiquetas | ninguna |
| Jira | [STASK-4](https://bluinc.atlassian.net/browse/STASK-4) |

## Relaciones

- **Padre:** [[STASK-3 - Crear notificaciones|STASK-3]] Crear notificaciones

## Descripcion

Esta tarea se ejecuta para crear notificaciones en Firebase con el siguiente contenido, vinculando el token con un usuariode nb

```
POST /v3/notifications
```

```
{
  "type":"nb", <-- Este parametro lo usamos para saber para que usuarios consideraremos los userId
  "title": "Notificación importante",
  "body": "Esta es la descripción de la notificación",
  "data": {
    "link": "https://enlace-del-recurso.com"
  },
  "userIds": [123, 456, 789] 
}
```

- `title`: El título de la notificación.


- `body`: La descripción de la notificación.


- `data.link`: El enlace asociado a la notificación.
