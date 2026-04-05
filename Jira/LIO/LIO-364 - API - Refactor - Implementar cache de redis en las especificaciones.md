---
jira_key: "LIO-364"
aliases: ["LIO-364"]
summary: "API - Refactor - Implementar cache de redis en las especificaciones"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-05-27 08:46"
updated: "2025-06-12 10:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-364"
---

# LIO-364: API - Refactor - Implementar cache de redis en las especificaciones

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-27 08:46 |
| Actualizado | 2025-06-12 10:21 |
| Etiquetas | ninguna |
| Jira | [LIO-364](https://bluinc.atlassian.net/browse/LIO-364) |

## Relaciones

- **Padre:** [[LIO-261]] Implementar Redis
- **relates to:** [[LIO-365]] Cambiar Ruta de Especificaciones.

## Descripcion

Se migró el recurso a v4



{{API_URL}}/v4/item/691009/specs





devuelve

```json
[
    {
        "id": 3102297,
        "nombre": "Brand",
        "valor": "Ducky",
        "total": 1
    },
    {
        "id": 3100671,
        "nombre": "Cord Length\t",
        "valor": "60 inches",
        "total": 1
    },
    {
        "id": 3102765,
        "nombre": "Frame Bottom Material\t",
        "valor": "Plastic",
        "total": 1
    }
]
```

y se le implemetno REDIS
