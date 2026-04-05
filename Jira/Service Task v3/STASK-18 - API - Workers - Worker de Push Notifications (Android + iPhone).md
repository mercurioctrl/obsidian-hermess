---
jira_key: "STASK-18"
aliases: ["STASK-18"]
summary: "API - Workers - Worker de Push Notifications (Android + iPhone)"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-01-13 08:49"
updated: "2026-02-24 21:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/STASK-18"
---

# STASK-18: API - Workers - Worker de Push Notifications (Android + iPhone)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-13 08:49 |
| Actualizado | 2026-02-24 21:23 |
| Etiquetas | ninguna |
| Jira | [STASK-18](https://bluinc.atlassian.net/browse/STASK-18) |

## Relaciones

- **Padre:** [[STASK-15]] Sistema de Notificaciones Multicanal (Queue + Workers)

## Descripcion

Implementar el worker responsable de procesar attempts del canal **push**.
Debe soportar:

- **Android** mediante Firebase Cloud Messaging (FCM)


- **iPhone** mediante Apple Push Notification Service (APNs)
El worker toma attempts encolados, envía la notificación y actualiza el estado.



### Tareas

- Crear cola `queue:push`


- Implementar `PushNotificationWorker`


- Resolver tokens por usuario (Android/iOS)


- Enviar a FCM/APNs según token


- Manejar errores y retries



### Criterios de aceptación

- Un failure en push no afecta email ni otros canales.


- El worker respeta cancelaciones del request.


- El estado del attempt se actualiza correctamente.


- El envío a iPhone se realiza vía APNs (directo o vía Firebase).





La tarea fue completada en :
