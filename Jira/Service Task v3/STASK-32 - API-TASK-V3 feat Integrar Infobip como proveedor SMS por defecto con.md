---
jira_key: "STASK-32"
aliases: ["STASK-32"]
summary: "API-TASK-V3 feat Integrar Infobip como proveedor SMS por defecto con arquitectura desacoplada"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2026-03-25 16:37"
updated: "2026-03-30 16:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/STASK-32"
---

# STASK-32: API-TASK-V3 feat Integrar Infobip como proveedor SMS por defecto con arquitectura desacoplada

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2026-03-25 16:37 |
| Actualizado | 2026-03-30 16:15 |
| Etiquetas | ninguna |
| Jira | [STASK-32](https://bluinc.atlassian.net/browse/STASK-32) |

## Relaciones

- **Padre:** [[STASK-20 - API - Workers - Preparación para SMS y WhatsApp (sin ejecución)|STASK-20]] API - Workers - Preparación para SMS y WhatsApp (sin ejecución)
- **has action item:** [[LIO-578 - APIAPP - Feat - Validar numero de telefono|LIO-578]] API/APP - Feat - Validar numero de telefono

## Descripcion

```
POST /v1/queueNotification
```



Reemplazar el uso directo de Twilio para SMS por una abstracción basada en interfaz (SmsProviderInterface) que permita intercambiar proveedores mediante configuración. 

Implementar InfobipService usando la SMS API v3 de Infobip como proveedor por defecto, manteniendo Twilio disponible como
alternativa. 

El proveedor activo debe controlarse desde la variable de entorno `SMS_DEFAULT_PROVIDER`.



```
# SMS Provider (infobip | twilio)
SMS_DEFAULT_PROVIDER=infobip

# Infobip Configuration
INFOBIP_BASE_URL=
INFOBIP_API_KEY=
INFOBIP_SMS_FROM=

```
