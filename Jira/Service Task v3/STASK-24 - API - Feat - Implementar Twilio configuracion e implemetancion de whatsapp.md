---
jira_key: "STASK-24"
aliases: ["STASK-24"]
summary: "API - Feat - Implementar Twilio configuracion e implemetancion de whatsapp queue works."
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2026-02-13 17:35"
updated: "2026-03-19 19:39"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/STASK-24"
---

# STASK-24: API - Feat - Implementar Twilio configuracion e implemetancion de whatsapp queue works.

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2026-02-13 17:35 |
| Actualizado | 2026-03-19 19:39 |
| Etiquetas | ninguna |
| Jira | [STASK-24](https://bluinc.atlassian.net/browse/STASK-24) |

## Relaciones

- **Padre:** [[STASK-20 - API - Workers - Preparación para SMS y WhatsApp (sin ejecución)|STASK-20]] API - Workers - Preparación para SMS y WhatsApp (sin ejecución)

## Descripcion

El sistema deberá incorporar soporte para envío de notificaciones **WhatsApp** utilizando **Twilio Content Templates**, con procesamiento asíncrono mediante **Laravel Queue**.

Se deberá implementar:

- Un **WhatsAppNotificationService** como worker encargado de enviar mensajes de WhatsApp utilizando templates aprobados en Twilio, con soporte para variables dinámicas.


- Un **ProcessWhatsAppNotification** como Job de Laravel Queue, con hasta 3 intentos y backoff exponencial (1, 5 y 15 minutos).


- Extensión del **TwilioService** con un método `sendWhatsApp()` que permita enviar mensajes mediante `contentSid` y `contentVariables`.


- Actualización de servicios existentes para habilitar y validar el canal `whatsapp`.



**Flujo esperado**:

- El endpoint `/queueNotification` recibe un payload solicitando el canal `whatsapp`, incluyendo `contentSid` y `contentVariables`.


- Se crean los registros `notification_request` y `notification_attempt`.


- El job se encola en la queue `whatsapp`.


- El worker resuelve y normaliza el teléfono del usuario y envía el mensaje vía Twilio Content API.


- Se actualiza el estado del attempt y del request según el resultado del envío.



**Se requiere.**

- Habilitar el canal `whatsapp` en `ChannelResolverService`.


- Encolar el job correspondiente desde `QueueNotificationService`.


- Validar `contentSid` (obligatorio) y `contentVariables` (opcional) en `QueueNotificationValidator`.



**Comando de ejecución del worker**:

```
php artisan queue:work --queue=whatsapp --tries=3 --timeout=90
```
