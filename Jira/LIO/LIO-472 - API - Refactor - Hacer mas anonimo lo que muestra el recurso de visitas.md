---
jira_key: "LIO-472"
aliases: ["LIO-472"]
summary: "API - Refactor - Hacer mas \"anonimo\" lo que muestra el recurso de visitas"
status: "Finalizada"
type: "Tarea"
priority: "Highest"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-10-31 13:44"
updated: "2025-11-06 11:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-472"
---

# LIO-472: API - Refactor - Hacer mas "anonimo" lo que muestra el recurso de visitas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Highest |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-31 13:44 |
| Actualizado | 2025-11-06 11:03 |
| Etiquetas | ninguna |
| Jira | [LIO-472](https://bluinc.atlassian.net/browse/LIO-472) |

## Relaciones

- **Padre:** [[LIO-408 - Referidos|LIO-408]] Referidos

## Descripcion

Lo que haremos es retirar el parámetro `userEmail` del objeto y recortar solo a la primera palabra el `userName` si es una dejar esa

```
GET {API_URL}/v4/referrals/{token}/visits?per_page=10&page=1
```

```
{
    "success": true,
    "message": "Visitas obtenidas correctamente.",
    "data": [
        {
            "id": 17,
            "usuarioID": 2,
            "userName": "Catriel",
            "attributed_at": "15-09-2025 14:26",
            "valid_until": null
        }
    ],
    "pagination": {
        "current_page": 1,
        "per_page": 10,
        "total": 1,
        "total_pages": 1
    }
}
```
