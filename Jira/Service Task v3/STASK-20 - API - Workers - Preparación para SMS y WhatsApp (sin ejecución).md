---
jira_key: "STASK-20"
aliases: ["STASK-20"]
summary: "API - Workers - Preparación para SMS y WhatsApp (sin ejecución)"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-01-13 08:50"
updated: "2026-02-25 13:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/STASK-20"
---

# STASK-20: API - Workers - Preparación para SMS y WhatsApp (sin ejecución)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-13 08:50 |
| Actualizado | 2026-02-25 13:01 |
| Etiquetas | ninguna |
| Jira | [STASK-20](https://bluinc.atlassian.net/browse/STASK-20) |

## Relaciones

- **Padre:** [[STASK-15 - Sistema de Notificaciones Multicanal (Queue + Workers)|STASK-15]] Sistema de Notificaciones Multicanal (Queue + Workers)
- **Subtarea:** [[STASK-23 - API - Feat - Implementar Twilio configuracion e implemetancion de sms queue|STASK-23]] API - Feat - Implementar Twilio configuracion e implemetancion de sms queue works.
- **Subtarea:** [[STASK-24 - API - Feat - Implementar Twilio configuracion e implemetancion de whatsapp|STASK-24]] API - Feat - Implementar Twilio configuracion e implemetancion de whatsapp queue works.
- **Subtarea:** [[STASK-25 - API - Refactor - implementar Rate Limiting, Throttling y Middleware en POST|STASK-25]] API - Refactor - implementar Rate Limiting, Throttling y Middleware en POST queueNotification
- **Subtarea:** [[STASK-26 - API - DB - Migración y normalización de números telefónicos legacy a|STASK-26]] API - DB - Migración y normalización de números telefónicos legacy a repositorio unificado de usuarios
- **Subtarea:** [[STASK-27 - API - DB - Migración y depuración de tokens FCMAPNs legacy a UserPushDevices|STASK-27]] API - DB - Migración y depuración de tokens FCM/APNs legacy a UserPushDevices
- **Subtarea:** [[STASK-32 - API-TASK-V3 feat Integrar Infobip como proveedor SMS por defecto con|STASK-32]] API-TASK-V3 feat Integrar Infobip como proveedor SMS por defecto con arquitectura desacoplada

## Descripcion

Dejar preparado el sistema para aceptar SMS y WhatsApp **sin habilitar envíos reales**.
El contrato, validaciones y base de datos deben soportar estos canales.
Los canales no implementados se excluyen explícitamente.

### Tareas

- Permitir `channelsRequested` = sms / whatsapp


- Validar contenido mínimo (`content.sms.body`, etc.)


- Resolver como `excluded: CHANNEL_NOT_ENABLED`


- Documentar puntos de extensión para futuros workers



### Criterios de aceptación

- El payload acepta sms/whatsapp sin romper.


- No se crean attempts activos para canales no implementados.


- La respuesta explica claramente la exclusión.


- No se requieren cambios cuando se agreguen los workers.
