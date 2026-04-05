---
jira_key: "LIO-290"
aliases: ["LIO-290"]
summary: "API - Refactor - Implementar redis en el recurso de busqueda por categoria"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-03-20 12:56"
updated: "2025-03-25 10:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-290"
---

# LIO-290: API - Refactor - Implementar redis en el recurso de busqueda por categoria

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-20 12:56 |
| Actualizado | 2025-03-25 10:52 |
| Etiquetas | ninguna |
| Jira | [LIO-290](https://bluinc.atlassian.net/browse/LIO-290) |

## Relaciones

- **Padre:** [[LIO-261]] Implementar Redis

## Descripcion

Implementaremos redis para el recurso y todos sus filtros

```
GET {API4_URL}/v4/category?search={terminos de busqueda} 
```
