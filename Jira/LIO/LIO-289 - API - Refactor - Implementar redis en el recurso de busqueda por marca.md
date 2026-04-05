---
jira_key: "LIO-289"
aliases: ["LIO-289"]
summary: "API - Refactor - Implementar redis en el recurso de busqueda por marca"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-03-20 12:55"
updated: "2025-03-25 10:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-289"
---

# LIO-289: API - Refactor - Implementar redis en el recurso de busqueda por marca

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-20 12:55 |
| Actualizado | 2025-03-25 10:50 |
| Etiquetas | ninguna |
| Jira | [LIO-289](https://bluinc.atlassian.net/browse/LIO-289) |

## Relaciones

- **Padre:** [[LIO-261]] Implementar Redis

## Descripcion

Implementaremos redis para el recurso y todos sus filtros

```
GET {API4_URL}/v4/brands?search={terminos de busqueda} 
```
