---
jira_key: "LIO-514"
aliases: ["LIO-514"]
summary: "API LO V4 refactor: Listar todos los tokens de un cliente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2026-01-16 09:52"
updated: "2026-01-29 10:30"
labels: ["esperandoDependencia"]
jira_url: "https://bluinc.atlassian.net/browse/LIO-514"
---

# LIO-514: API LO V4 refactor: Listar todos los tokens de un cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2026-01-16 09:52 |
| Actualizado | 2026-01-29 10:30 |
| Etiquetas | esperandoDependencia |
| Jira | [LIO-514](https://bluinc.atlassian.net/browse/LIO-514) |

## Relaciones

- **Padre:** [[LIO-504]] Sección Referidos
- **is cloned by:** [[LIO-522]] API LO V4 - Review - Listar todos los tokens de un cliente -> Tokens no visibles

## Descripcion

Actualmente, el endpoint GET /referrals/token retorna un único token del usuario autenticado mediante el método getUserReferralToken() en ReferralRepository, que ejecuta un SELECT sin ORDER BY ni límite.

Objetivo: Modificar el endpoint para que retorne todos los tokens activos del usuario (donde deleted_at IS NULL), manteniendo la retrocompatibilidad con la respuesta actual.



```php
GET /referrals/token
```



```json
{
    "hasToken": true,
    "token": "eferreyra10",
    "created_at": "2026-01-27 17:47:35",
    "updated_at": "2026-01-27 17:47:35",
    "tokens": [
        {
            "id": 32,
            "token": "eferreyra10",
            "created_at": "2026-01-27 17:47:35",
            "updated_at": "2026-01-27 17:47:35",
            "is_current": true
        },
        {
            "id": 31,
            "token": "eferreyra2023",
            "created_at": "2026-01-27 17:47:18",
            "updated_at": "2026-01-27 17:47:18",
            "is_current": false
        },
        {
            "id": 11,
            "token": "eferreyra2025",
            "created_at": "2025-09-17 10:30:53",
            "updated_at": "2025-09-17 10:30:53",
            "is_current": false
        }
    ],
    "message": "Token de referidos obtenido correctamente."
}
```
