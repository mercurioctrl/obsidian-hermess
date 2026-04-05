---
jira_key: "PED-1188"
aliases: ["PED-1188"]
summary: "API - Feat - Crear reserva (con control anti-solape)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2025-12-14 21:33"
updated: "2025-12-26 08:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1188"
---

# PED-1188: API - Feat - Crear reserva (con control anti-solape)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-14 21:33 |
| Actualizado | 2025-12-26 08:48 |
| Etiquetas | ninguna |
| Jira | [PED-1188](https://bluinc.atlassian.net/browse/PED-1188) |

## Relaciones

- **Padre:** [[PED-1186]] Sistema de reservas de salas de reuniones (vista semanal)
- **has action item:** [[PED-1203]] APP - Feat - Reservas de salas de reunion

## Descripcion

Crea una nueva reserva para la sala en un rango horario específico.
Valida que `endAt > startAt` y **rechaza la operación si hay solapamiento** con otra reserva existente.
La creación es transaccional para evitar conflictos por requests simultáneos.

```
POST /v1/rooms/{roomId}/reservations
```

**Payload**

```
{
  "title": "Reunión producto",
  "startAt": "2025-12-16T10:30:00-03:00",
  "endAt": "2025-12-16T11:15:00-03:00",
  "notes": "Roadmap"
}

```

**Response 201**

```
{
  "data": {
    "id": 124,
    "roomId": 1,
    "title": "Reunión producto",
    "startAt": "2025-12-16T10:30:00-03:00",
    "endAt": "2025-12-16T11:15:00-03:00",
    "status": "active",
    "createdByUserId": 55
  }
}

```

**409 si solapa**

```
{
  "error": "ROOM_ALREADY_BOOKED",
  "message": "La sala ya está reservada en ese rango.",
  "conflicts": [
    { "id": 120, "startAt": "2025-12-16T10:00:00-03:00", "endAt": "2025-12-16T11:00:00-03:00" }
  ]
}

```

**Reglas**

- `endAt > startAt` (si no, 422).


- Solape si existe reserva `active` con:

- `existing.startAt < newEndAt AND existing.endAt > newStartAt`




- Debe ser **race-safe** (dos POST simultáneos no pueden colarse).



**Sql Orientativo**

```
SET XACT_ABORT ON;
SET NOCOUNT ON;
BEGIN TRAN;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

IF EXISTS (
  SELECT 1
  FROM dbo.room_reservations WITH (UPDLOCK, HOLDLOCK, INDEX(IX_rr_room_status_start))
  WHERE room_id = @roomId
    AND status = 'active'
    AND start_at < @newEnd
    AND end_at   > @newStart
)
BEGIN
  ROLLBACK;
  -- el backend traduce esto a 409
  THROW 50001, 'ROOM_ALREADY_BOOKED', 1;
END

INSERT INTO dbo.room_reservations (room_id, created_by_user_id, title, notes, start_at, end_at)
VALUES (@roomId, @userId, @title, @notes, @newStart, @newEnd);

COMMIT;
```
