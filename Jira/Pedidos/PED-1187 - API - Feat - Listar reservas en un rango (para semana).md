---
jira_key: "PED-1187"
aliases: ["PED-1187"]
summary: "API - Feat - Listar reservas en un rango (para semana)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2025-12-14 21:31"
updated: "2026-01-07 12:10"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1187"
---

# PED-1187: API - Feat - Listar reservas en un rango (para semana)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-14 21:31 |
| Actualizado | 2026-01-07 12:10 |
| Etiquetas | ninguna |
| Jira | [PED-1187](https://bluinc.atlassian.net/browse/PED-1187) |

## Relaciones

- **Padre:** [[PED-1186]] Sistema de reservas de salas de reuniones (vista semanal)
- **is cloned by:** [[PED-1199]] API - Review - Listar reservas en un rango (para semana) - QA Observaciones
- **has action item:** [[PED-1203]] APP - Feat - Reservas de salas de reunion
- **relates to:** [[PED-1225]] API - Refactor - Listar/Crear reservas en un rango -> Agregar 'notes' al listar las reservas y al crearla
- **relates to:** [[PED-1226]] API - Refactor - Listar reservas en un rango (para semana) -> Agregar nombre de usuario

## Descripcion

Devuelve todas las reservas **activas** de la sala que intersectan el rango de fechas solicitado.
El front lo usa para pintar la **vista semanal**, mostrando bloques ocupados y calculando los espacios libres.
Siempre responde ordenado por hora de inicio.

```
GET /v1/rooms/{roomId}/reservations?from={iso}&to={iso}
```

- `from` y `to`  **0** (ej: `2025-12-15`)


- Devuelve reservas **active** que intersecten el rango (`startAt < to` AND `endAt > from`).



**Response 200**

```
{
  "data": [
    {
      "id": 123,
      "roomId": 1,
      "title": "Sync",
      "startAt": "2025-12-16T10:00:00-03:00",
      "endAt": "2025-12-16T11:00:00-03:00",
      "status": "active",
      "createdByUserId": 55,
      "createdAt": "2025-12-14T20:10:00-03:00"
    }
  ]
}

```

**Reglas**

- Siempre ordenar por `startAt ASC`.


- No devolver canceladas.



**SQL orientativo**

```
SELECT id, room_id, created_by_user_id, title, start_at, end_at, status, created_at
FROM dbo.room_reservations
WHERE room_id = @roomId
  AND status = 'active'
  AND start_at < @to
  AND end_at > @from
ORDER BY start_at ASC;
```

## Tablas (SQL Server)

### `dbo.rooms`

- `id` BIGINT IDENTITY PK


- `name` NVARCHAR(120)


- `location` NVARCHAR(120) NULL


- `capacity` INT NULL


- `is_active` BIT DEFAULT 1


- `created_at` DATETIME2


- `updated_at` DATETIME2



### `dbo.room_reservations`

 

- `id` BIGINT IDENTITY PK


- `room_id` BIGINT FK


- `created_by_user_id` BIGINT FK (a tu tabla users)


- `title` NVARCHAR(160)


- `notes` NVARCHAR(MAX) NULL


- `start_at` DATETIME(0)


- `end_at` DATETIME(0)


- `status` VARCHAR(20) DEFAULT 'active' (`active|cancelled`)


- `cancelled_at` DATETIME(0) NULL


- `created_at` DATETIME(0) DEFAULT SYSDATETIMEOFFSET()


- `updated_at` DATETIME(0) DEFAULT SYSDATETIMEOFFSET()



**Índices**

- `IX_rr_room_status_start (room_id, status, start_at)`


- `IX_rr_room_end (room_id, end_at)`


- `IX_rr_user_start (created_by_user_id, start_at)`
