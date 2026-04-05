---
jira_key: "LIO-433"
aliases: ["LIO-433"]
summary: "API - Feat - Listar visitas"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-08-27 08:52"
updated: "2025-09-02 10:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-433"
---

# LIO-433: API - Feat - Listar visitas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-27 08:52 |
| Actualizado | 2025-09-02 10:02 |
| Etiquetas | ninguna |
| Jira | [LIO-433](https://bluinc.atlassian.net/browse/LIO-433) |

## Relaciones

- **Padre:** [[LIO-408 - Referidos|LIO-408]] Referidos

## Descripcion

```
GET {API_URL}/v4/referrals/{token}/visits
```

Basándonos en la tabla `[LO].[dbo].user_referrals` mostraremos informacion de las visitas del token de referido para ese token especifico y de ser necesario haremos join con otra tabla

```
{
  "data": [
    {
      "id": 1001,
      "usuarioID": 5645,
      "userName": "Lisa Simpson",
      "userEmail": "lista@simpsopn.com",
      "attributed_at": "10-11-2025 15:12",
      "valid_until": "10-12-2025 15:12",
    },
    {
      "id": 1002,
      "usuarioID": 5642,
      "userName": "Bart Simpson",
      "userEmail": "lista@simpsopn.com",
      "attributed_at": "09-11-2025 15:12",
      "valid_until": "09-12-2025 15:12",
    }
  ],
  ... paginado etc .... 
}

```

Este recurso se usaría para un esquema similar a este, en la pestaña de visitas del rectángulo rojo

[adjunto]
