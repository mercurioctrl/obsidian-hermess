---
jira_key: "LIO-409"
aliases: ["LIO-409"]
summary: "API - Feat - Crear un nuevo token de referidos por parte de un usuario"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-08-06 12:55"
updated: "2026-01-16 10:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-409"
---

# LIO-409: API - Feat - Crear un nuevo token de referidos por parte de un usuario

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-06 12:55 |
| Actualizado | 2026-01-16 10:48 |
| Etiquetas | ninguna |
| Jira | [LIO-409](https://bluinc.atlassian.net/browse/LIO-409) |

## Relaciones

- **Padre:** [[LIO-408 - Referidos|LIO-408]] Referidos
- **has action item:** [[LIO-467 - API - Refactor - Al crear o modificar un token de referidos, verificamos si el|LIO-467]] API - Refactor - Al crear  o modificar un token de referidos, verificamos si el usuario crador tiene cliente en NB, si no es asi lo creamos y se lo asignamos
- **relates to:** [[LIO-513 - API - Refactor - Obtener token de usuario - Obtener el token más reciente|LIO-513]] API - Refactor - Obtener token de usuario - Obtener el token más reciente

## Descripcion

El usuario logueado puede crear su propio token personalizado para compartir

```
POST {API_URL}/v4/referrals/token
```

**Carga útil:**

```
{
  "token": "miTokenPersonalizado"
}
```

**Respuestas posibles:**

```
{
  "success": true,
  "message": "Token de referido creado correctamente.",
  "data": {
    "token": "miTokenPersonalizado"
  }
}
```

```
{
  "success": false,
  "message": "El token elegido ya está en uso. Por favor, selecciona otro."
}
```

Tablas orientadoras `LO.dbo.referrals`

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `id` | auto | Identificador único del token creado |
| `referrer_id` | BIGINT (FK users) | El id de la tabla `[LO].[dbo].[usuarios]` |
| `token` | VARCHAR(50) UNIQUE | Token personalizado único |
| `created_at` | TIMESTAMP | Fecha creación |
| `updated_at` | TIMESTAMP | Fecha actualización |

**Eliminar un referral token (Soft)**

```
DELETE {API_URL}/v4/referrals/token
```
