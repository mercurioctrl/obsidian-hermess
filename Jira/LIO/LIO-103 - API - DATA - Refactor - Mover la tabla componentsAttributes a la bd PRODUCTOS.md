---
jira_key: "LIO-103"
aliases: ["LIO-103"]
summary: "API - DATA - Refactor -> Mover la tabla componentsAttributes a la bd PRODUCTOS"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-10-04 06:48"
updated: "2024-10-09 22:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-103"
---

# LIO-103: API - DATA - Refactor -> Mover la tabla componentsAttributes a la bd PRODUCTOS

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-10-04 06:48 |
| Actualizado | 2024-10-09 22:23 |
| Etiquetas | ninguna |
| Jira | [LIO-103](https://bluinc.atlassian.net/browse/LIO-103) |

## Relaciones

- **Padre:** [[LIO-71]] Armador de equipos
- **has action item:** [[INV-147]] API - Refactor - Filtrar productos que no cuentan con todos sus atributos obligatorios
- **action item from:** [[LIO-72]] API - Research - Crearemos una tabla con los atributos que son obligatorios para cada cateogria

## Descripcion

La moveremos para utilizar con mayor facilidad en armadores y sistemas de inventario

Adicionalmente le agregaremos el ID DE CATEGORIA DE CAPA 1, que se puede mapear usando la columna `[LO].[dbo].[categorias].id_nb` para cada categoría porque fue concebida desde el punto de vista de libre opcion
