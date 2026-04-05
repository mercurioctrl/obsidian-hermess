---
jira_key: "PED-1302"
aliases: ["PED-1302"]
summary: "Crear repositorio de Paises."
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Ezequiel manzano"
created: "2026-02-04 12:38"
updated: "2026-02-13 10:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1302"
---

# PED-1302: Crear repositorio de Paises.

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Ezequiel manzano |
| Creado | 2026-02-04 12:38 |
| Actualizado | 2026-02-13 10:52 |
| Etiquetas | ninguna |
| Jira | [PED-1302](https://bluinc.atlassian.net/browse/PED-1302) |

## Relaciones

- **Padre:** [[PED-2 - Bases y repositorios|PED-2]] Bases y repositorios
- **has action item:** [[PED-1304 - APP - Refactor - Editar Clientes, cambios en casos internacionales|PED-1304]] APP - Refactor - Editar Clientes, cambios en casos internacionales

## Descripcion

```
GET {{API_URL}}/v1/countries
```

Devuelve 

```
{
    "id": 1,
    "description": "Argentina",
    "flag": "🇦🇷",
    "default": 1,
    "prefixFlag": "AR"
  },
```
