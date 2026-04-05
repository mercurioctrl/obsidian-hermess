---
jira_key: "PED-783"
aliases: ["PED-783"]
summary: "API - Refactor - Agregar utilidad extra por categoría al cliente (al precio que paga el reseller)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-31 12:49"
updated: "2024-08-19 08:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-783"
---

# PED-783: API - Refactor - Agregar utilidad extra por categoría al cliente (al precio que paga el reseller)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-31 12:49 |
| Actualizado | 2024-08-19 08:57 |
| Etiquetas | ninguna |
| Jira | [PED-783](https://bluinc.atlassian.net/browse/PED-783) |

## Relaciones

- **Padre:** [[PED-65]] Listado de productos

## Descripcion

Agregaremos la tabla `[NewBytes_DBF].[dbo].[userCategories]`

Crearemos una tabla con 4 columnas

- id (auto)


- userId (int)


- categoryId (int)


- utility



Se debe verificar que los cambios no generen retrasos a los recursos cuando listas todo el catalogo o muchos items
