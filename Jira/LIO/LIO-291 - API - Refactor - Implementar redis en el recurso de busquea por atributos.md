---
jira_key: "LIO-291"
aliases: ["LIO-291"]
summary: "API - Refactor - Implementar redis en el recurso de busquea por atributos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-03-20 12:58"
updated: "2025-03-25 10:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-291"
---

# LIO-291: API - Refactor - Implementar redis en el recurso de busquea por atributos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-20 12:58 |
| Actualizado | 2025-03-25 10:53 |
| Etiquetas | ninguna |
| Jira | [LIO-291](https://bluinc.atlassian.net/browse/LIO-291) |

## Relaciones

- **Padre:** [[LIO-261 - Implementar Redis|LIO-261]] Implementar Redis

## Descripcion

Implementaremos redis para el recurso y todos sus filtros

```
GET {API4_URL}/v4/attributes?search={terminos de busqueda} 
```
