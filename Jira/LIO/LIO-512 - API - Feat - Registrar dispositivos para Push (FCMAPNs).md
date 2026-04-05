---
jira_key: "LIO-512"
aliases: ["LIO-512"]
summary: "API - Feat - Registrar dispositivos para Push (FCM/APNs)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-01-13 09:14"
updated: "2026-02-18 16:59"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-512"
---

# LIO-512: API - Feat - Registrar dispositivos para Push (FCM/APNs)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-13 09:14 |
| Actualizado | 2026-02-18 16:59 |
| Etiquetas | ninguna |
| Jira | [LIO-512](https://bluinc.atlassian.net/browse/LIO-512) |

## Relaciones

- **Padre:** [[LIO-507 - Login y otros aspectos generales|LIO-507]] Login y otros aspectos generales
- **has action item:** [[LIO-517 - APP MOBILE - Feat - Registrar token FCM post login al ingresar al dashboard|LIO-517]] APP MOBILE - Feat - Registrar token FCM post login al ingresar al dashboard inicial
- **is cloned by:** [[LIO-520 - API - Review - Registrar dispositivos para Push (FCMAPNs) - Token duplicado y|LIO-520]] API - Review - Registrar dispositivos para Push (FCM/APNs) -> Token duplicado y fecha de actualización
- **action item from:** [[LIO-541 - API - Feat - Registrar dispositivos Web para Push (FCM Web)|LIO-541]] API - Feat - Registrar dispositivos Web para Push (FCM Web)

## Descripcion

Crear un recurso dedicado para registrar dispositivos y sus tokens de push, desacoplado del login.
Debe soportar múltiples dispositivos por usuario, y evitar que un token quede asignado a más de un usuario/dispositivo.


El endpoint debe ser idempotente (upsert) y permitir actualizar token/metadata cuando rota o cambia.
Queda preparado para enviar notificaciones luego a iOS/Android (FCM/APNs), sin requerir relogin.

```
POST /v4/push/devices
```

**Payload**

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

## Respuesta esperada

### 200 OK (update / ya existía)

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

### 201 Created (nuevo registro)

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

## Errores y códigos HTTP

- **400 Bad Request**: payload inválido (faltan campos, platform/provider inválidos, token vacío si se requiere).


- **401 Unauthorized**: JWT faltante/expirado/incorrecto.


- **409 Conflict**: violación de unicidad no resoluble (ej: token duplicado y no se puede reasignar por política) *(idealmente lo resolvés por reasignación y evitás este 409)*.


- **422 Unprocessable Entity**: `environment` inválido, `deviceId` formato inválido, provider incompatible.


- **500 Internal Server Error**: falla inesperada DB/infra.



> Recomendación operativa: **no usar 409** si van a permitir reasignación del token al usuario actual (lo más práctico). En ese caso, se devuelve 200/201.


## Descripción de parámetros

- `deviceId` *(string, requerido)*: UUID persistente por instalación de app. No debe cambiar entre sesiones.


- `platform` *(enum: ios|android, requerido)*: plataforma del dispositivo.


- `provider` *(enum: fcm|apns, requerido)*: proveedor del token entregado.


- `token` *(string, requerido para activar push)*: token actual. Puede admitirse `null` si quieren “registrar el device” aunque no haya permisos aún (definir política).


- `environment` *(enum: production|sandbox, opcional)*: solo relevante para APNs directo; si usan FCM para iOS, puede omitirse.


- `appVersion/buildNumber/osVersion/deviceModel/locale/timezone` *(opcionales)*: metadata para diagnóstico y segmentación futura.



## Tablas de base de datos necesarias 

### `LO.dbo.UserPushDevices`

**Campos mínimos recomendados**

- `Id BIGINT IDENTITY PK`


- `UserId INT NOT NULL`


- `DeviceId NVARCHAR(64) NOT NULL`


- `Platform VARCHAR(16) NOT NULL`


- `Provider VARCHAR(16) NOT NULL`


- `PushToken NVARCHAR(512) NULL`


- `Environment VARCHAR(16) NULL`


- `IsActive BIT NOT NULL DEFAULT 1`


- `RevokedAt DATETIME2 NULL`


- `LastSeenAt DATETIME2 NULL`


- `CreatedAt DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME()`


- `UpdatedAt DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME()`



**Índices/uniques**

- `UNIQUE (UserId, DeviceId)`


- `UNIQUE (Provider, PushToken) WHERE PushToken IS NOT NULL`


- `INDEX (UserId, IsActive) INCLUDE (Provider, PushToken, Platform, Environment, LastSeenAt)`



## Criterios de aceptación

- **Idempotencia**: repetir el mismo request no crea duplicados; actualiza `LastSeenAt/UpdatedAt`.


- **No pisado entre usuarios**: un mismo `(provider, token)` nunca queda asociado a dos usuarios a la vez; si aparece con otro usuario, se reasigna al actual.


- **Multi-dispositivo**: un usuario puede registrar múltiples `deviceId` distintos y todos quedan activos.


- **Validaciones**: `deviceId/platform/provider` requeridos y con enum correcto; errores devuelven 400/422 según corresponda.


- **Auditoría mínima**: se persisten `CreatedAt/UpdatedAt/LastSeenAt` y `IsActive` correctamente.
