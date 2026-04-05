---
jira_key: "LIO-467"
aliases: ["LIO-467"]
summary: "API - Refactor - Al crear  o modificar un token de referidos, verificamos si el usuario crador tiene cliente en NB, si no es asi lo creamos y se lo asignamos"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-10-29 16:50"
updated: "2025-10-30 17:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-467"
---

# LIO-467: API - Refactor - Al crear  o modificar un token de referidos, verificamos si el usuario crador tiene cliente en NB, si no es asi lo creamos y se lo asignamos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-10-29 16:50 |
| Actualizado | 2025-10-30 17:07 |
| Etiquetas | ninguna |
| Jira | [LIO-467](https://bluinc.atlassian.net/browse/LIO-467) |

## Relaciones

- **Padre:** [[LIO-408]] Referidos
- **action item from:** [[LIO-409]] API - Feat - Crear un nuevo token de referidos por parte de un usuario

## Descripcion

Segun lo conversado refactorizaremos el recurso 

```
POST {API_URL}/v4/referrals/token
```

Para comprobar si el usuario que esta creando el token tiene cliente dentro de `[NewBytes_DBF].[dbo].[clientes]` y si no es así lo crearemos y vincularemos al usuario de Libre Opción
