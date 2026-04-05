---
jira_key: "LIO-275"
aliases: ["LIO-275"]
summary: "API - Feat - Agregar al catalogo la sección \"Mayores descuentos\" "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-03-17 05:18"
updated: "2025-03-18 01:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-275"
---

# LIO-275: API - Feat - Agregar al catalogo la sección "Mayores descuentos" 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-03-17 05:18 |
| Actualizado | 2025-03-18 01:33 |
| Etiquetas | ninguna |
| Jira | [LIO-275](https://bluinc.atlassian.net/browse/LIO-275) |

## Relaciones

- **Padre:** [[LIO-166 - Catalogos y sincronizaciones|LIO-166]] Catalogos y sincronizaciones
- **has action item:** [[LIO-276 - APP - Refactor - Agregar la seccion mayores descuentos|LIO-276]] APP - Refactor - Agregar la seccion "mayores descuentos"

## Descripcion

Dentro de lo que son las búsquedas de catalogo “normales” es decir, las que traer los filtros, existe un parámetro de orden que ya existe, lo utilizaremos para ordenar todos los productos de una búsqueda (o todos cuando no tengo termino de búsqueda).

Usaremos entonces el parámetro `o=discount`

```
GET {API_URL}/v4/search?search={termino de busqueda}&offset=0&o=discount
```

Y lo que haremos es básicamente orientar nuestra búsqueda a un resultado ordenado por el parámetro `descuento` de la tabla `CS.dbo.prodcutos`
