---
jira_key: "LIO-227"
aliases: ["LIO-227"]
summary: "API - Refactor - Cerrar ticket"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-02-17 18:07"
updated: "2025-03-04 19:19"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-227"
---

# LIO-227: API - Refactor - Cerrar ticket

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-17 18:07 |
| Actualizado | 2025-03-04 19:19 |
| Etiquetas | ninguna |
| Jira | [LIO-227](https://bluinc.atlassian.net/browse/LIO-227) |

## Relaciones

- **Padre:** [[LIO-21]] Migrar sistema de tickets para usar el de capa 1 (NB)

## Descripcion

Este recurso sirve para cuando el usuario ya ve que esta resuelto, puede marcarlo como resuelto y solo cambia en caso de estar abierto `"open": false`

```
PATCH {APIv4_URL}/v4/ticket/680312/resolved
```
