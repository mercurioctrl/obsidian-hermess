---
jira_key: "PED-459"
aliases: ["PED-459"]
summary: "APP - Información del cliente al listado - Ultima compra vacía"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2024-01-08 12:43"
updated: "2024-01-16 03:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-459"
---

# PED-459: APP - Información del cliente al listado - Ultima compra vacía

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2024-01-08 12:43 |
| Actualizado | 2024-01-16 03:13 |
| Etiquetas | ninguna |
| Jira | [PED-459](https://bluinc.atlassian.net/browse/PED-459) |

## Relaciones

- **relates to:** [[PED-387]] APP - Refactor - Agregaremos informacion del cliente al listado

## Descripcion

Cuando el número de días desde la última compra es de cero, es decir, que la compra se realizó ese mismo día, aparece vacío el campo de ultima compra en lugar de decir “hoy“.

[adjunto]
