---
jira_key: "NBWEB-232"
aliases: ["NBWEB-232"]
summary: "API - No se deben ver los productos ocultos, ni lo que son de distribucion externa"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-06-05 21:29"
updated: "2022-06-25 17:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-232"
---

# NBWEB-232: API - No se deben ver los productos ocultos, ni lo que son de distribucion externa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-05 21:29 |
| Actualizado | 2022-06-25 17:20 |
| Etiquetas | ninguna |
| Jira | [NBWEB-232](https://bluinc.atlassian.net/browse/NBWEB-232) |

## Relaciones

- **Padre:** [[NBWEB-4 - API - Catalogos de productos|NBWEB-4]] API - Catalogos de productos

## Descripcion

En ningun catalogo se deben mostrar los productos que en la tabla `newbytes_dbf.dbo.articulos `

esten marcadas las columnas

- ocultarDeNb


- EXCLUIR


-  id_distribuidora (solo deben mostrarse los que el valor este en 1)
