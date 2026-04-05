---
jira_key: "POS-62"
summary: "API - Refactor - Agregar enlace para los productos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-08-09 10:16"
updated: "2022-10-11 10:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-62"
---

# POS-62: API - Refactor - Agregar enlace para los productos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-08-09 10:16 |
| Actualizado | 2022-10-11 10:21 |
| Etiquetas | ninguna |
| Jira | [POS-62](https://bluinc.atlassian.net/browse/POS-62) |

## Descripción

Para todos los listados que muestren productos, se debe agregar el parametro `productUrl`

Este parámetro simplemente es para poder enlazar al sitio web con la ficha del producto.

Para esto se va a crear un parametro nuevo en el .env con la base de la url a la que posteriormente se le agregara el Id del producto para poder enlazarlo.

[https://www.nb.com.ar/fromPostventa_-_113281](https://www.nb.com.ar/liliana-turbo-ventilador-gris-3-aspas-reclinable_-_113281)
