---
jira_key: "STASK-16"
aliases: ["STASK-16"]
summary: "API - Feat – Encolar notificación multicanal (universal)"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2026-01-13 08:43"
updated: "2026-02-24 21:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/STASK-16"
---

# STASK-16: API - Feat – Encolar notificación multicanal (universal)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-13 08:43 |
| Actualizado | 2026-02-24 21:13 |
| Etiquetas | ninguna |
| Jira | [STASK-16](https://bluinc.atlassian.net/browse/STASK-16) |

## Relaciones

- **Padre:** [[STASK-15]] Sistema de Notificaciones Multicanal (Queue + Workers)

## Descripcion

Crear un nuevo endpoint que permita **encolar notificaciones multicanal** a usuarios del sistema.
El endpoint valida el payload, aplica idempotencia opcional mediante `dedupeKey`, registra la solicitud y genera intentos por canal/usuario.
No realiza envíos directos: delega la ejecución a workers desacoplados.
Convive con el recurso legacy existente sin modificarlo.

```
POST /v1/queueNotification
```

**Payload**

```
{
  "channelsRequested": ["push", "email", "sms"],
  "content": {
    "push": {
      "title": "INCENTIVO MSI EXTENDIDO!",
      "body": "No pierdas otra oportunidad..."
    },
    "email": {
      "subject": "INCENTIVO MSI EXTENDIDO!",
      "body": "No pierdas otra oportunidad...",
      "ctaLink": "/dashboard/limitesObjetivos"
    },
    "sms": {
      "body": "INCENTIVO MSI: no pierdas otra oportunidad..."
    }
  },
  "targets": { "type": "users", "ids": [6964, 3564, 6005] },
  "type": "lo",
  "data": { "link": "/dashboard/limitesObjetivos" },
  "dedupeKey": "lo:incentivo-msi:2026-02-25"
}

```

### Respuesta esperada (201)

```
{
  "id": "uuid",
  "status": "queued",
  "channelsRequested": ["push", "email", "sms"],
  "channelsResolved": ["push", "email"],
  "resolution": {
    "excluded": [
      { "channel": "sms", "reason": "CHANNEL_NOT_ENABLED" }
    ]
  }
}

```

### Reglas clave

- `dedupeKey` es **opcional**:

- si viene → se aplica idempotencia


- si no viene → se encola siempre




- `channelsResolved` debe reflejar solo los canales efectivamente encolados


- Canales no implementados deben excluirse explícitamente



### Criterios de aceptación

- El endpoint no envía notificaciones directamente.


- Si `dedupeKey` existe, no se duplican envíos.


- Se registran requests y attempts por canal/usuario.


- El legacy `POST /v1/notifications` no se ve afectado.


- La respuesta explica claramente qué canales se procesan y cuáles no.
