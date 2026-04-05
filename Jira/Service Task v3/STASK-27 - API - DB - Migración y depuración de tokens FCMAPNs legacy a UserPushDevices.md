---
jira_key: "STASK-27"
aliases: ["STASK-27"]
summary: "API - DB - Migración y depuración de tokens FCM/APNs legacy a UserPushDevices"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2026-02-13 17:48"
updated: "2026-02-26 17:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/STASK-27"
---

# STASK-27: API - DB - Migración y depuración de tokens FCM/APNs legacy a UserPushDevices

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2026-02-13 17:48 |
| Actualizado | 2026-02-26 17:35 |
| Etiquetas | ninguna |
| Jira | [STASK-27](https://bluinc.atlassian.net/browse/STASK-27) |

## Relaciones

- **Padre:** [[STASK-20]] API - Workers - Preparación para SMS y WhatsApp (sin ejecución)

## Descripcion

Se requiere migrar tokens push legacy hacia `UserPushDevices`, asegurando consistencia con el modelo actual de notificaciones push (Android, iOS, Browser).

La migración debe:

- Importar solo el **token más reciente por usuario** desde tablas legacy. 

- `LO.dbo.legacy_notification_tokens`  → la tabla proviene de la migracion de ms-notificaciones legacy - mysql




- Evitar duplicados respetando el índice único `(Provider, PushToken)`.


- Asignar correctamente `Platform`, `Provider` y metadatos mínimos para dispositivos web legacy.


- Garantizar idempotencia.


- Dejar el sistema preparado para coexistir con registros móviles actuales.



El objetivo es consolidar tokens activos y eliminar ruido histórico que impacta la entrega de notificaciones push.





Tabla actualmente:

```sql
create table LO.dbo.UserPushDevices
(
    Id             bigint identity
        constraint PK_UserPushDevices
            primary key,
    UserId         int                                not null,
    DeviceId       nvarchar(64)                       not null,
    Platform       varchar(16)                        not null
        constraint CK_UserPushDevices_Platform
            check ([Platform] = 'browser' OR [Platform] = 'ios' OR [Platform] = 'android'),
    Provider       varchar(16)                        not null
        constraint CK_UserPushDevices_Provider
            check ([Provider] = 'apns' OR [Provider] = 'fcm'),
    PushToken      nvarchar(512),
    Environment    varchar(16)
        constraint CK_UserPushDevices_Environment
            check ([Environment] IS NULL OR ([Environment] = 'sandbox' OR [Environment] = 'production')),
    AppVersion     nvarchar(32),
    BuildNumber    nvarchar(32),
    OsVersion      nvarchar(32),
    DeviceModel    nvarchar(64),
    Locale         nvarchar(16),
    Timezone       nvarchar(64),
    IsActive       bit       default 1                not null,
    RevokedAt      datetime2,
    LastSeenAt     datetime2,
    CreatedAt      datetime2 default sysutcdatetime() not null,
    UpdatedAt      datetime2 default sysutcdatetime() not null,
    UserAgent      nvarchar(512),
    BrowserName    nvarchar(64),
    BrowserVersion nvarchar(32),
    DeviceType     varchar(16)
)
go

create unique index IX_UserPushDevices_UserId_DeviceId
    on dbo.UserPushDevices (UserId, DeviceId)
go

create unique index IX_UserPushDevices_Provider_PushToken
    on dbo.UserPushDevices (Provider, PushToken)
    where [PushToken] IS NOT NULL
go

create index IX_UserPushDevices_UserId_IsActive
    on dbo.UserPushDevices (UserId, IsActive) include (Provider, PushToken, Platform, Environment, LastSeenAt)
g
```
