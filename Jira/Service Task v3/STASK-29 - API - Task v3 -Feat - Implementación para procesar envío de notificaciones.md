---
jira_key: "STASK-29"
aliases: ["STASK-29"]
summary: "API - Task v3 -Feat - Implementación para procesar envío de notificaciones pendientes"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2026-03-02 10:31"
updated: "2026-03-11 10:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/STASK-29"
---

# STASK-29: API - Task v3 -Feat - Implementación para procesar envío de notificaciones pendientes

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2026-03-02 10:31 |
| Actualizado | 2026-03-11 10:32 |
| Etiquetas | ninguna |
| Jira | [STASK-29](https://bluinc.atlassian.net/browse/STASK-29) |

## Relaciones

- **Padre:** [[STASK-15]] Sistema de Notificaciones Multicanal (Queue + Workers)

## Descripcion

El microservicio task-v3 es el encargado del sistema de notificaciones. El microservicio v4 debe poder dispararlo para
procesar notificaciones pendientes.

**Flujo:**

- v4 llama a `POST /internal/notifications/send/pending/{channel} `en task-v3


- task-v3 procesa las notificaciones pendientes y las envía



**Endpoint a implementar/ajustar:**


```
POST /internal/notifications/send/pending/{channel}
```

- **Canales:** push, mailing


- **Consumidor:** microservicio v4



**Comportamiento esperado:**

- Lock distribuido por canal (evita doble procesamiento)


- Retornar métricas: { channel, success, failed, message }
