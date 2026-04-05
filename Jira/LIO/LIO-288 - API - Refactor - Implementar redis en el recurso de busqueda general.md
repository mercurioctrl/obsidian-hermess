---
jira_key: "LIO-288"
aliases: ["LIO-288"]
summary: "API - Refactor - Implementar redis en el recurso de busqueda general"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-03-20 12:53"
updated: "2025-03-26 01:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-288"
---

# LIO-288: API - Refactor - Implementar redis en el recurso de busqueda general

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-20 12:53 |
| Actualizado | 2025-03-26 01:16 |
| Etiquetas | ninguna |
| Jira | [LIO-288](https://bluinc.atlassian.net/browse/LIO-288) |

## Relaciones

- **Padre:** [[LIO-261 - Implementar Redis|LIO-261]] Implementar Redis

## Descripcion

Implementaremos redis para el recurso y todos sus filtros

```
GET {API4_URL}/v4/search?search={terminos de busqueda}&offset=0&freeshipping=1&marcas=gigabyte
```
