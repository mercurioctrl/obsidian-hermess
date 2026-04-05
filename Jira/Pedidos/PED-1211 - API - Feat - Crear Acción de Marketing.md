---
jira_key: "PED-1211"
aliases: ["PED-1211"]
summary: "API - Feat - Crear Acción de Marketing"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2026-01-05 07:15"
updated: "2026-01-16 09:57"
labels: ["esperandoDependencia"]
jira_url: "https://bluinc.atlassian.net/browse/PED-1211"
---

# PED-1211: API - Feat - Crear Acción de Marketing

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-05 07:15 |
| Actualizado | 2026-01-16 09:57 |
| Etiquetas | esperandoDependencia |
| Jira | [PED-1211](https://bluinc.atlassian.net/browse/PED-1211) |

## Relaciones

- **Padre:** [[PED-1208]] Gestión de Aportes y Gastos de Marketing
- **has action item:** [[PED-1221]] APP - Feat - Form Crear Acción
- **is cloned by:** [[PED-1266]] API - Review - Crear Acción de Marketing - CreatedByUserId nulo

## Descripcion

**Qué hay que hacer**

- Crear una acción con nombre, descripción y rango de fechas opcional.



**Endpoint**

```
POST /v1/marketing/actions
```

**Ejemplo request (payload)**

```
{
  "name": "Hot Sale 2026",
  "description": "Campaña multiproducto durante Hot Sale",
  "startAt": "2026-05-11T00:00:00-03:00",
  "endAt": "2026-05-13T23:59:59-03:00"
}

```

**Ejemplo response (201)**

```
{
  "id": 501,
  "name": "Hot Sale 2026",
  "description": "Campaña multiproducto durante Hot Sale",
  "startAt": "2026-05-11T00:00:00-03:00",
  "endAt": "2026-05-13T23:59:59-03:00",
  "createdAt": "2026-01-05T06:15:00-03:00"
}

```

**SQL Server**

- `NB_WEB.dbo.Marketing_Actions`



**SQL Server (tabla) — **`Marketing_Actions`

- `Id` (int, identity, PK)


- `Name` (varchar(120), NOT NULL) *(ej. Hot Sale)*


- `Description` (varchar(600), NULL)


- `StartAt` (datetime2, NULL)


- `EndAt` (datetime2, NULL)


- `CreatedAt` (datetime2, NOT NULL, default sysdatetime())


- `CreatedByUserId` (int, NULL)


- Índice:

- `IX_Marketing_Actions_Name` (`Name`)





**Criterios de aceptación**

- `Name` requerido.


- Si vienen fechas, valida `StartAt <= EndAt`.


- Responde `201` con acción creada.


- Permite acción sin fechas.


- No crea asignaciones ni movimientos automáticamente.
