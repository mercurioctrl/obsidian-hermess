---
jira_key: "LIO-434"
aliases: ["LIO-434"]
summary: "API - Feat - Actividad reciente del token para este usuario"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-08-27 09:39"
updated: "2025-09-02 16:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-434"
---

# LIO-434: API - Feat - Actividad reciente del token para este usuario

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-27 09:39 |
| Actualizado | 2025-09-02 16:41 |
| Etiquetas | ninguna |
| Jira | [LIO-434](https://bluinc.atlassian.net/browse/LIO-434) |

## Relaciones

- **Padre:** [[LIO-408]] Referidos

## Descripcion

```
GET {API_URL}/v4/referrals/{token}/stats
```

Basándonos en la tabla `LO.dbo.referral_conversions`  y `[LO].[dbo].user_referrals` mostraremos informacion de la actividad reciente para dar un resumen rapido del token al usuario que es propietario del mismo

```
{
  "data": {
    "referral_id": 4234,
    "token": "tokenDelUsuario",
    "counters": {
      "visits": 95,
      "conversions": 11,
      "conversion_rate": 0.116
    },
    "recent_activity": [
      {
        "type": "conversion",
        "occurred_at": "2025-08-27 15:23",
        "pedidoCabeceraId": 42343,
        "amount": 15000.00,
        "fee": 750.00
      },
      {
        "type": "visit",
        "occurred_at": "2025-08-27 18:19",
        "city": "Buenos Aires, AR",
      }
    ]
  }
}

```

Este repositorio sirve para construir algo similar al apartado de actividad reciente enmarcado en el rectangulo rojo

[adjunto]
