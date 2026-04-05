---
jira_key: "NBWEB-858"
aliases: ["NBWEB-858"]
summary: "MS Envios - Refactor - Agregar medidas y peso principales para los productos (segunda jerarquia por categoria)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-08-30 14:53"
updated: "2024-09-05 10:54"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-858"
---

# NBWEB-858: MS Envios - Refactor - Agregar medidas y peso principales para los productos (segunda jerarquia por categoria)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-30 14:53 |
| Actualizado | 2024-09-05 10:54 |
| Etiquetas | ninguna |
| Jira | [NBWEB-858](https://bluinc.atlassian.net/browse/NBWEB-858) |

## Relaciones

- **Padre:** [[NBWEB-507]] Refactor cotizacion de envios en el sitio

## Descripcion

Segun lo conversado y lo realizado en la API en [link](https://lioteam.atlassian.net/browse/NBWEB-768)  aplicaremos la misma logica para calcular los envíos del lado del microservicio

**Modificaremos el recurso de cotización y generaciones de etiquetas **para agregar estos parámetros `highAverage`,`widthAverage`,`lengthAverage`,`weightAverage` teniendo en cuenta que de no encontrarse en `[NewBytes_DBF].[dbo].[articulo]` lo traeremos de `[NewBytes_DBF].[dbo].[familias]`

Es decir que tomaremos como primeras medidas las que aparecen en el producto y en caso de que no existan, recién ahí el promedio por categoria.
