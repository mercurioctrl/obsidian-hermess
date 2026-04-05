---
jira_key: "PED-1195"
aliases: ["PED-1195"]
summary: "API - Feat - Salas de reunión: Alta y listado"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2025-12-19 12:51"
updated: "2025-12-26 08:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1195"
---

# PED-1195: API - Feat - Salas de reunión: Alta y listado

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2025-12-19 12:51 |
| Actualizado | 2025-12-26 08:48 |
| Etiquetas | ninguna |
| Jira | [PED-1195](https://bluinc.atlassian.net/browse/PED-1195) |

## Relaciones

- **Padre:** [[PED-1186]] Sistema de reservas de salas de reuniones (vista semanal)
- **has action item:** [[PED-1203]] APP - Feat - Reservas de salas de reunion

## Descripcion

Implementar endpoints para **crear** y **listar** salas de reunión, de forma que el sistema pueda administrar múltiples salas y el front pueda mostrarlas para seleccionar cuál reservar.

**Objetivo**
Permitir que un usuario autorizado registre nuevas salas con sus datos básicos (nombre, ubicación, capacidad) y consultar el listado de salas disponibles.

---

## Alcance

- Crear tabla `rooms` (si no existe) y exponer:

- `GET /v1/rooms` (listar)


- `POST /v1/rooms` (crear)





---

## Endpoints

### 1) Listar salas

```
GET /v1/rooms
```

**Comportamiento**

- Devuelve salas **activas** (`isActive=true`) por defecto.


- Ordenar por `name ASC`.



**Response 200**

```
{
  "data": [
    { "id": 1, "name": "Sala Reuniones", "location": "Piso 2", "capacity": 8, "isActive": true }
  ]
}
```

**Query params (opcionales)**

- `includeInactive=true` → incluye salas inactivas.



---

### 2) Crear sala

```
POST /v1/rooms
```

**Payload**

```
{
  "name": "Sala Reuniones",
  "location": "Piso 2",
  "capacity": 8,
  "isActive": true
}

```

**Reglas**

- `name` obligatorio, trim, mínimo 3 caracteres.


- `name` debe ser **único** (si ya existe ⇒ 409).


- `capacity` opcional; si viene, debe ser `>= 1`.


- `isActive` default `true` si no se envía.



**Response 201**

```
{
  "data": {
    "id": 10,
    "name": "Sala Reuniones",
    "location": "Piso 2",
    "capacity": 8,
    "isActive": true
  }
}

```

**Error 409 (nombre duplicado)**

```
{
  "error": "ROOM_NAME_ALREADY_EXISTS",
  "message": "Ya existe una sala con ese nombre."
}

```

---

## Base de datos (SQL Server)

### Tabla `dbo.rooms`

- `id` BIGINT IDENTITY(1,1) PK


- `name` NVARCHAR(120) NOT NULL


- `location` NVARCHAR(120) NULL


- `capacity` INT NULL


- `is_active` BIT NOT NULL DEFAULT 1


- `created_at` DATETIME2(0) NOT NULL DEFAULT SYSDATETIME()


- `updated_at` DATETIME2(0) NOT NULL DEFAULT SYSDATETIME()



**Índices**

- `UX_rooms_name` UNIQUE (`name`)



---

## Criterios de aceptación

- `POST /v1/rooms` crea una sala y devuelve `201` con su `id`.


- Si el `name` ya existe, devuelve `409 ROOM_NAME_ALREADY_EXISTS`.


- `GET /v1/rooms` devuelve únicamente salas activas por defecto y ordenadas por nombre.


- Con `includeInactive=true`, `GET /v1/rooms` incluye también salas inactivas.


- Validaciones: `name` requerido y `capacity` (si viene) debe ser `>= 1`.
