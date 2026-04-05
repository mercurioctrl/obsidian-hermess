---
jira_key: "PED-1072"
aliases: ["PED-1072"]
summary: "API - Refactor - Ordernar aceleradores desde el acelerador mas alto, al mas bajo"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-08-01 09:09"
updated: "2025-08-12 10:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1072"
---

# PED-1072: API - Refactor - Ordernar aceleradores desde el acelerador mas alto, al mas bajo

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-01 09:09 |
| Actualizado | 2025-08-12 10:44 |
| Etiquetas | ninguna |
| Jira | [PED-1072](https://bluinc.atlassian.net/browse/PED-1072) |

## Relaciones

- **Padre:** [[PED-753]] Incentivos Clientes

## Descripcion

Ordenaremos el repositorio de modo tal que veamos primero los que tienen mayor aceleracion

```
GET /v1/clientsObjectives/acelerators?expired={expired}
```
