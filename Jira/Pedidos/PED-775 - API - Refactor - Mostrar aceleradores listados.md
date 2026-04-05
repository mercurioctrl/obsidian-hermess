---
jira_key: "PED-775"
aliases: ["PED-775"]
summary: "API - Refactor - Mostrar aceleradores listados"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-22 13:34"
updated: "2024-07-23 18:25"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-775"
---

# PED-775: API - Refactor - Mostrar aceleradores listados

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-22 13:34 |
| Actualizado | 2024-07-23 18:25 |
| Etiquetas | ninguna |
| Jira | [PED-775](https://bluinc.atlassian.net/browse/PED-775) |

## Relaciones

- **Padre:** [[PED-753 - Incentivos Clientes|PED-753]] Incentivos Clientes
- **blocks:** [[PED-776 - APP - Refactor - Mostrar los aceleradores que estan disponibles|PED-776]] APP - Refactor - Mostrar los aceleradores que estan disponibles

## Descripcion

Crearemos un recurso para listar todos los aceleradores de forma tal que los vendedores puedan conocerlos todo el tiempo

```
GET /v1/clientsObjectives/acelerators?expired=false
```

```
[
  {
    "id": 1,
    "txtMatch": " ",
    "acelerator": 1.0,
    "startDate": "2024-07-01T00:00:00",
    "endDate": "2024-07-31T00:00:00"
  },
  {
    "id": 2,
    "txtMatch": "notebook",
    "acelerator": 1.5,
    "startDate": "2024-07-03T00:00:00",
    "endDate": "2024-07-05T18:00:00"
  },
  {
    "id": 4,
    "txtMatch": "trust",
    "acelerator": 2.0,
    "startDate": "2024-07-15T00:00:00",
    "endDate": "2024-07-31T00:00:00"
  },
  {
    "id": 5,
    "txtMatch": "PRIME B650M-A II",
    "acelerator": 2.0,
    "startDate": "2024-07-15T00:00:00",
    "endDate": "2024-07-31T00:00:00"
  }

...
]
```

Tiene un filtro llamado `expired`

Si `expired`= true entonces muestro solos los expirados

Si `expired`= false entonces muestro solo los que no expiraron

Si `expired` es NULL entonces muestro todo
