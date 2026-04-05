---
jira_key: "LIO-541"
aliases: ["LIO-541"]
summary: "API - Feat - Registrar dispositivos Web para Push (FCM Web)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2026-02-18 13:14"
updated: "2026-02-26 16:54"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-541"
---

# LIO-541: API - Feat - Registrar dispositivos Web para Push (FCM Web)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2026-02-18 13:14 |
| Actualizado | 2026-02-26 16:54 |
| Etiquetas | ninguna |
| Jira | [LIO-541](https://bluinc.atlassian.net/browse/LIO-541) |

## Relaciones

- **Padre:** [[LIO-507]] Login y otros aspectos generales
- **has action item:** [[LIO-542]] APP - Feat - Registrar dispositivo web para Push Notifications (FCM)
- **has action item:** [[LIO-512]] API - Feat - Registrar dispositivos para Push (FCM/APNs)

## Descripcion

Igual que la versión móvil pero adaptada para navegadores. Soporta múltiples navegadores por usuario (Chrome en PC, Firefox en laptop, Chrome en otro dispositivo, etc.). El `deviceId` se genera y persiste en `localStorage`/`IndexedDB` del navegador, ya que no existe identificador nativo de instalación.

`POST /v4/push/devices`

```
{
  "deviceId": "9b6b2f7e-6b6c-4c2d-8e8e-43bb2c8a3a10",
  "platform": "browser",
  "provider": "fcm",
  "token": "xxxxxx",
  "environment": "production",
  "appVersion": "3.14.0",
  "buildNumber": null,
  "osVersion": null,
  "deviceModel": null,
  "locale": "es-AR",
  "timezone": "America/Argentina/Buenos_Aires",
  "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
  "browserName": "Chrome",
  "browserVersion": "121.0.0",
  "deviceType": "desktop"
}
```



#### Base de datos — Cambios requeridos

#### Columnas adicionales para web

```
ALTER TABLE LO.dbo.UserPushDevices
ADD UserAgent       NVARCHAR(512) NULL,
    BrowserName     NVARCHAR(64)  NULL,
    BrowserVersion  NVARCHAR(32)  NULL,
    DeviceType      VARCHAR(16)   NULL; -- desktop|mobile|tablet
```



## Criterios de aceptación específicos para web

- `platform: browser` + `provider: fcm` → se acepta y procesa normalmente.


- `platform: browser` + `provider: apns` → **422** — combinación inválida.


- Múltiples browsers del mismo usuario quedan todos con `IsActive = 1`.


- Si FCM rota el token, el upsert por `(UserId, DeviceId)` actualiza `PushToken` sin duplicar.
