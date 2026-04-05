---
jira_key: "LIO-517"
aliases: ["LIO-517"]
summary: "APP MOBILE - Feat - Registrar token FCM post login al ingresar al dashboard inicial"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-01-19 16:14"
updated: "2026-01-22 15:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-517"
---

# LIO-517: APP MOBILE - Feat - Registrar token FCM post login al ingresar al dashboard inicial

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-19 16:14 |
| Actualizado | 2026-01-22 15:50 |
| Etiquetas | ninguna |
| Jira | [LIO-517](https://bluinc.atlassian.net/browse/LIO-517) |

## Relaciones

- **Padre:** [[LIO-507]] Login y otros aspectos generales
- **action item from:** [[LIO-512]] API - Feat - Registrar dispositivos para Push (FCM/APNs)

## Descripcion

Implementar un endpoint idempotente que permita registrar y mantener actualizados los dispositivos móviles del usuario autenticado y sus tokens de notificación (FCM/APNs), quedando preparado para el envío de push notifications sin necesidad de relogin.

---

### Alcance funcional

- Registro de dispositivos móviles post‑login (al ingresar al dashboard inicial).


- Soporte multi‑dispositivo por usuario.


- Reasignación segura de tokens cuando estos aparecen asociados a otro usuario.


- Actualización de metadata y `lastSeenAt` en cada invocación.


- Compatibilidad futura con iOS y Android vía FCM/APNs.



```
POST /v4/push/devices
```

**Autenticación:** JWT obligatorio.

### Payload

```
{
  "deviceId": "9b6b2f7e-6b6c-4c2d-8e8e-43bb2c8a3a10",
  "platform": "ios",
  "provider": "fcm",
  "token": "xxxxxx",
  "environment": "production",
  "appVersion": "1.0.12",
  "buildNumber": "1012",
  "osVersion": "17.2",
  "deviceModel": "iPhone15,3",
  "locale": "es-AR",
  "timezone": "America/Argentina/Buenos_Aires"
}

```

- No debe requerirse relogin para que el nuevo token quede activo.



---

### Respuestas

**200 OK – registro existente actualizado**

```
{
  "success": true,
  "status": "updated",
  "device": {
    "id": 12345,
    "deviceId": "9b6b2f7e-6b6c-4c2d-8e8e-43bb2c8a3a10",
    "platform": "ios",
    "provider": "fcm",
    "isActive": true,
    "lastSeenAt": "2026-01-13T12:34:56Z"
  }
}

```

**201 Created – nuevo registro**

```
{
  "success": true,
  "status": "created",
  "device": {
    "id": 12345,
    "deviceId": "9b6b2f7e-6b6c-4c2d-8e8e-43bb2c8a3a10",
    "platform": "ios",
    "provider": "fcm",
    "isActive": true,
    "lastSeenAt": "2026-01-13T12:34:56Z"
  }
}

```

### Criterios de aceptación

- Idempotencia garantizada (no se generan duplicados).


- Un token no queda asociado a más de un usuario simultáneamente.


- Un usuario puede tener múltiples dispositivos activos.


- Validaciones correctas con códigos HTTP coherentes.


- Auditoría mínima persistida (`CreatedAt`, `UpdatedAt`, `LastSeenAt`, `IsActive`).
