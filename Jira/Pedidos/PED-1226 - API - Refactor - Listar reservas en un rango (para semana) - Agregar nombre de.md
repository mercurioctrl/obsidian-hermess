---
jira_key: "PED-1226"
aliases: ["PED-1226"]
summary: "API - Refactor - Listar reservas en un rango (para semana) -> Agregar nombre de usuario"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Guillermo Avila"
created: "2026-01-05 11:19"
updated: "2026-01-26 12:28"
labels: ["esperandoDependencia"]
jira_url: "https://bluinc.atlassian.net/browse/PED-1226"
---

# PED-1226: API - Refactor - Listar reservas en un rango (para semana) -> Agregar nombre de usuario

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Guillermo Avila |
| Creado | 2026-01-05 11:19 |
| Actualizado | 2026-01-26 12:28 |
| Etiquetas | esperandoDependencia |
| Jira | [PED-1226](https://bluinc.atlassian.net/browse/PED-1226) |

## Relaciones

- **Padre:** [[PED-1186 - Sistema de reservas de salas de reuniones (vista semanal)|PED-1186]] Sistema de reservas de salas de reuniones (vista semanal)
- **relates to:** [[PED-1187 - API - Feat - Listar reservas en un rango (para semana)|PED-1187]] API - Feat - Listar reservas en un rango (para semana)
- **is cloned by:** [[PED-1270 - API - Review - Listar reservas en un rango (para semana) - Agregar nombre de|PED-1270]] API - Review - Listar reservas en un rango (para semana) - Agregar nombre de usuario -> Usuario guardado no coincidente

## Descripcion

Realizaremos un refactor en las respuestas de los recursos de reservas (GET y POST) para agregar `createdByUserName`.



```
GET/POST {{API_URL}}/v1/rooms/{roomId}/reservations
```

```
{
  "data": [
    {
      "id": 38,
      "roomId": 5,
      "title": "Greserva",
      "notes": "Gnotas",
      "startAt": "2026-01-07 09:00:00",
      "endAt": "2026-01-07 18:45:00",
      "status": "active",
      "createdByUserId": 23,
      "createdByUserName": andi <----------------------- SE AGREGA
      "createdAt": "2026-01-07 11:45:01"
    }
  ]
}

```



Query orientativa:

```
SELECT	
	created_by_user_id,
	UserName
FROM NB_WEB.dbo.room_reservations
LEFT JOIN NB_WEB.dbo.usuarios_nb
	ON room_reservations.created_by_user_id = NB_WEB.dbo.usuarios_nb.UserId
```



Al crear la reserva, el usuario almacenado debe coincidir con el usuario que la creó.
