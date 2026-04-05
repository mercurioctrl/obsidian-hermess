---
jira_key: "NBWEB-799"
summary: "API - Refactor - Agregar utilidad extra por categoría al cliente (al precio que paga el reseller)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-31 12:56"
updated: "2024-08-07 01:30"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-799"
---

# NBWEB-799: API - Refactor - Agregar utilidad extra por categoría al cliente (al precio que paga el reseller)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-31 12:56 |
| Actualizado | 2024-08-07 01:30 |
| Etiquetas | ninguna |
| Jira | [NBWEB-799](https://bluinc.atlassian.net/browse/NBWEB-799) |

## Descripción

Agregaremos la tabla `[NewBytes_DBF].[dbo].[userCategories]`

Crearemos una tabla con 4 columnas

- id (auto)


- userId (int)


- categoryId (int)


- utility



Se debe verificar que los cambios no generen retrasos a los recursos cuando listas todo el catalogo o muchos items
