---
jira_key: "STASK-28"
aliases: ["STASK-28"]
summary: "API - feat: Limpieza automática de tokens push inválidos (FCM/APNS)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2026-02-19 17:05"
updated: "2026-02-26 17:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/STASK-28"
---

# STASK-28: API - feat: Limpieza automática de tokens push inválidos (FCM/APNS)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2026-02-19 17:05 |
| Actualizado | 2026-02-26 17:02 |
| Etiquetas | ninguna |
| Jira | [STASK-28](https://bluinc.atlassian.net/browse/STASK-28) |

## Relaciones

- **Padre:** [[STASK-15 - Sistema de Notificaciones Multicanal (Queue + Workers)|STASK-15]] Sistema de Notificaciones Multicanal (Queue + Workers)

## Descripcion

Cuando `FCM` o `APNS` rechazan una notificación porque el token del dispositivo es inválido o expirado, el attempt queda marcado
 como failed en la base de datos, pero el token sigue activo en LO.dbo.UserPushDevices. Esto provoca que cada nuevo llamado a
 `POST /v1/queueNotification` vuelva a generar jobs para ese token, consumiendo recursos de cola y llamadas a APIs externas pagas
 (FCM, APNS) de forma innecesaria.

 **Solución a implementar**
 Se adoptar estrategia híbrida:

- Invalidación inmediata (en el job): cuando ProcessPushNotification falla definitivamente con un error INVALID_TOKEN,
desactiva el token específico en el mismo momento, antes de que pueda generar nuevos attempts.


- Limpieza batch nocturna (safety net): un comando Artisan programado diariamente a las 03:00 desactiva en lote todos los
tokens que acumularon 3 o más fallos por token inválido.





** Criterios de aceptación**

- Un token FCM reportado como UNREGISTERED queda desactivado en` LO.dbo.UserPushDevices` tras el primer fallo definitivo del job


- Un token APNS con respuesta HTTP 410 queda desactivado de la misma forma


- php artisan notifications:invalidate-failed-devices ejecuta sin errores e imprime cuántos tokens desactivó


- php artisan schedule:list muestra el comando programado a las 03:00


- El resto de rutas y canales (email, SMS, WhatsApp) no se ven afectados
