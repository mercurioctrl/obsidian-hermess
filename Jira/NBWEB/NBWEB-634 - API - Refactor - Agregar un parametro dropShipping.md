---
jira_key: "NBWEB-634"
aliases: ["NBWEB-634"]
summary: "API - Refactor - Agregar un parametro dropShipping"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-03-04 09:13"
updated: "2024-03-12 16:41"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-634"
---

# NBWEB-634: API - Refactor - Agregar un parametro dropShipping

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-03-04 09:13 |
| Actualizado | 2024-03-12 16:41 |
| Etiquetas | ninguna |
| Jira | [NBWEB-634](https://bluinc.atlassian.net/browse/NBWEB-634) |

## Relaciones

- **Padre:** [[NBWEB-619 - Generar ordenes|NBWEB-619]] Generar ordenes
- **blocks:** [[NBWEB-635 - APP - Refactor - Agregar un parametro dropShipping|NBWEB-635]] APP - Refactor - Agregar un parametro dropShipping

## Descripcion

Agregaremos un parámetro al procesar los carritos llamado `dropShipping` que si es `true` dara cuenta de que el envio va directamente al cliente.

Para esto marcaremos ese pedido en `pedclit` tambien con la columna `dropShipping` en true
