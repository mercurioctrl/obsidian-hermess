---
jira_key: "STASK-19"
aliases: ["STASK-19"]
summary: "API - Workers - Worker de Emails"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-01-13 08:50"
updated: "2026-03-04 10:29"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/STASK-19"
---

# STASK-19: API - Workers - Worker de Emails

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-13 08:50 |
| Actualizado | 2026-03-04 10:29 |
| Etiquetas | ninguna |
| Jira | [STASK-19](https://bluinc.atlassian.net/browse/STASK-19) |

## Relaciones

- **Padre:** [[STASK-15 - Sistema de Notificaciones Multicanal (Queue + Workers)|STASK-15]] Sistema de Notificaciones Multicanal (Queue + Workers)

## Descripcion

Implementar el worker responsable del envío de correos electrónicos.
Consume attempts del canal email y utiliza un proveedor de correo transaccional.
Registra estado, errores y `provider_message_id`.

### Tareas

- Crear cola `queue:email`


- Implementar `EmailNotificationWorker`


- Integrar proveedor (phpmailer)


- Renderizar subject/body/cta


- Manejar retries y fallos definitivos



### Criterios de aceptación

- Email funciona independientemente del push.


- Los errores quedan registrados por attempt.


- El worker no procesa otros canales.


- El envío es completamente asíncrono.
