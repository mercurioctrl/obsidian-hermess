---
jira_key: "PED-1248"
aliases: ["PED-1248"]
summary: "API - Refactor - Listar marcas con fondos (totales disponibles) - Eliminar espacios vacíos en marcas"
status: "Finalizada"
type: "Tarea"
priority: "High"
assignee: "Franco Callipo"
reporter: "Guillermo Avila"
created: "2026-01-09 10:24"
updated: "2026-01-12 16:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1248"
---

# PED-1248: API - Refactor - Listar marcas con fondos (totales disponibles) - Eliminar espacios vacíos en marcas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | High |
| Asignado | Franco Callipo |
| Reportado por | Guillermo Avila |
| Creado | 2026-01-09 10:24 |
| Actualizado | 2026-01-12 16:23 |
| Etiquetas | ninguna |
| Jira | [PED-1248](https://bluinc.atlassian.net/browse/PED-1248) |

## Relaciones

- **Padre:** [[PED-1208]] Gestión de Aportes y Gastos de Marketing
- **clones:** [[PED-1216]] API - Feat - Listar marcas con fondos (totales disponibles)

## Descripcion

Realizaremos un refactor en el nombre de la marca para eliminar los espacios vacíos innecesarios. De esta forma, mejoraremos su visualización en la interfaz.

```
GET /v1/marketing/brands
```

[adjunto]
