---
jira_key: "PED-781"
aliases: ["PED-781"]
summary: "API - Refactor - Agregar utilidad extra por producto y cliente (al precio que paga el reseller)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-31 12:28"
updated: "2024-08-04 15:38"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-781"
---

# PED-781: API - Refactor - Agregar utilidad extra por producto y cliente (al precio que paga el reseller)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-31 12:28 |
| Actualizado | 2024-08-04 15:38 |
| Etiquetas | ninguna |
| Jira | [PED-781](https://bluinc.atlassian.net/browse/PED-781) |

## Relaciones

- **Padre:** [[PED-65 - Listado de productos|PED-65]] Listado de productos

## Descripcion

Agregaremos la tabla `[NewBytes_DBF].[dbo].[userItems]`

Crearemos una tabla con 4 columnas

- id (auto)


- clientId (int)


- itemId (int)


- utility



Se debe verificar que los cambios no generen retrasos a los recursos cuando listas todo el catalogo o muchos items
