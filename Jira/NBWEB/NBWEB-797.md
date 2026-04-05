---
jira_key: "NBWEB-797"
summary: "API - Refactor - Agregar utilidad extra por producto y cliente (al precio que paga el reseller)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-31 12:55"
updated: "2024-08-01 10:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-797"
---

# NBWEB-797: API - Refactor - Agregar utilidad extra por producto y cliente (al precio que paga el reseller)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-31 12:55 |
| Actualizado | 2024-08-01 10:53 |
| Etiquetas | ninguna |
| Jira | [NBWEB-797](https://bluinc.atlassian.net/browse/NBWEB-797) |

## Descripción

Agregaremos la tabla `[NewBytes_DBF].[dbo].[userItems]`

Crearemos una tabla con 4 columnas

- id (auto)


- clientId (int)


- itemId (int)


- utility



Se debe verificar que los cambios no generen retrasos a los recursos cuando listas todo el catalogo o muchos items
