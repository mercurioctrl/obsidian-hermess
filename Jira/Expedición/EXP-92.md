---
jira_key: "EXP-92"
summary: "API - Refactor - No dejar serializar un item que no tiene cargado al menos uno de los codigos unicos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-11-22 13:37"
updated: "2024-09-18 09:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-92"
---

# EXP-92: API - Refactor - No dejar serializar un item que no tiene cargado al menos uno de los codigos unicos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-22 13:37 |
| Actualizado | 2024-09-18 09:01 |
| Etiquetas | ninguna |
| Jira | [EXP-92](https://bluinc.atlassian.net/browse/EXP-92) |

## Descripción

Dentro de la tabla `NewBytes_DBF.dbo.articulos` deben (o deberían) estar las columnas para guardar

- upc


- ean


- gtin


- isbn



Los mismos tienen una extensión determinada y especificación ([https://liniocapacitaciones.files.wordpress.com/2016/04/codigos_barras_liniope.pdf](https://liniocapacitaciones.files.wordpress.com/2016/04/codigos_barras_liniope.pdf))

Para comenzar a tomar un serial se debe validar que al menos uno de estos valores este cargado en el formato correcto.
