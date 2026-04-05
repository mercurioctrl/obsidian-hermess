---
jira_key: "EXP-414"
aliases: ["EXP-414"]
summary: "BD - Actualización - Eliminar nombres de despachos incorrectos"
status: "Tareas por hacer"
type: "Subtarea"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Guillermo Avila"
created: "2024-06-04 14:21"
updated: "2024-06-04 14:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-414"
---

# EXP-414: BD - Actualización - Eliminar nombres de despachos incorrectos

| Campo | Valor |
|-------|-------|
| Estado | Tareas por hacer (Por hacer) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Guillermo Avila |
| Creado | 2024-06-04 14:21 |
| Actualizado | 2024-06-04 14:44 |
| Etiquetas | ninguna |
| Jira | [EXP-414](https://bluinc.atlassian.net/browse/EXP-414) |

## Relaciones

- **Padre:** [[EXP-249]] Feat - Vincular despacho / Editar despacho
- **relates to:** [[EXP-251]] API - Feat - Editar / Crear despacho en base a un pedido 

## Descripcion

Debido a que en ocasiones se ingresa erróneamente la ubicación del despacho en lugar del nombre de éste, surge la necesidad de realizar una actualización como `NULL` a todos los nombres de despachos que no coinciden con el formato correcto.



 Ejemplo de algunos nombres de despacho erróneos que pasaron el filtro de número de caracteres.

[adjunto]
