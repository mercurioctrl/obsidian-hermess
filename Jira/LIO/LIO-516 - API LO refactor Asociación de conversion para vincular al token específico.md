---
jira_key: "LIO-516"
aliases: ["LIO-516"]
summary: "API LO refactor Asociación de conversion para vincular al token específico"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2026-01-16 09:54"
updated: "2026-01-29 13:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-516"
---

# LIO-516: API LO refactor Asociación de conversion para vincular al token específico

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2026-01-16 09:54 |
| Actualizado | 2026-01-29 13:27 |
| Etiquetas | ninguna |
| Jira | [LIO-516](https://bluinc.atlassian.net/browse/LIO-516) |

## Relaciones

- **Padre:** [[LIO-504]] Sección Referidos

## Descripcion

Crear un nuevo endpoint que permita al usuario autenticado obtener un listado de todos sus tokens de referidos activos junto con las estadísticas de conversiones asociadas a cada uno. Actualmente, el sistema solo permite consultar conversiones por token específico mediante `GET /referrals/{token}/conversions`, pero no existe una vista consolidada de todos los tokens del usuario con sus métricas.

**Objetivo**

Implementar el endpoint `GET /referrals/tokens/conversions` que retorne todos los tokens activos del usuario autenticado con las siguientes métricas por token:

- Cantidad total de conversiones


- Suma total de comisiones generadas (fees)


- Suma total del monto de las órdenes


- Fecha de la última conversión


- Información básica del token (id, token, created_at, updated_at)



El endpoint debe incluir paginación y retornar tokens incluso si no tienen conversiones asociadas (valores en 0/null).

**Criterios de Aceptación**

- Endpoint accesible en GET /referrals/tokens/conversions


- Requiere autenticación mediante token JWT


- Soporta parámetros de paginación


- Retorna solo tokens activos (deleted_at IS NULL) del usuario autenticado


- Tokens ordenados por created_at DESC, id DESC (más recientes primero)


- Incluye tokens sin conversiones con valores en 0 o null según corresponda


- Respuesta con estructura estándar: success, message, data, pagination



```
GET /v4/referrals/tokens/conversions
```

```json
{
    "success": true,
    "message": "Tokens con conversiones obtenidos correctamente.",
    "data": [
        {
            "id": 32,
            "token": "eferreyra10",
            "totalFees": 0,
            "conversionsCount": 0,
            "totalAmount": 0,
            "lastConversionDate": null,
            "createdAt": "2026-01-27 17:47:35",
            "updatedAt": "2026-01-27 17:47:35"
        },
        {
            "id": 31,
            "token": "eferreyra2023",
            "totalFees": 0,
            "conversionsCount": 0,
            "totalAmount": 0,
            "lastConversionDate": null,
            "createdAt": "2026-01-27 17:47:18",
            "updatedAt": "2026-01-27 17:47:18"
        },
        {
            "id": 11,
            "token": "eferreyra2025",
            "totalFees": 23623.52,
            "conversionsCount": 3,
            "totalAmount": 47247.05,
            "lastConversionDate": "2025-09-18 14:04:15",
            "createdAt": "2025-09-17 10:30:53",
            "updatedAt": "2025-09-17 10:30:53"
        }
    ],
    "pagination": {
        "currentPage": 1,
        "perPage": 15,
        "total": 3,
        "totalPages": 1
    }
}
```



Nota importante: No se modifica la tabla referral_conversions. La asociación se mantiene mediante el campo referral_token existente, pero se mejora la consulta y la respuesta para mayor claridad.
