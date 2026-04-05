---
jira_key: "LIO-62"
aliases: ["LIO-62"]
summary: "API - Review - Hacer que funcione como antes el perfil para ver los productos del vendedor"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-08 09:41"
updated: "2024-07-22 11:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-62"
---

# LIO-62: API - Review - Hacer que funcione como antes el perfil para ver los productos del vendedor

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-08 09:41 |
| Actualizado | 2024-07-22 11:48 |
| Etiquetas | ninguna |
| Jira | [LIO-62](https://bluinc.atlassian.net/browse/LIO-62) |

## Relaciones

- **Padre:** [[LIO-28 - El sitio debe funcionar correctamente, sin puntos grises o cosas que no se|LIO-28]] El sitio debe funcionar correctamente, sin puntos grises o cosas que no se entienden
- **relates to:** [[LIO-73 - API - Refactor - Ver productos del vendedor - Añadir atributos|LIO-73]] API - Refactor - Ver productos del vendedor - Añadir atributos

## Descripcion

En el pasado cuando buscabas por el nombre de un reseller, te permitía ver todos sus productos, de la siguiente mantera

[link](https://libreopcion.com/exxit-computacion) 

Para esto las búsquedas 
[https://api4.libreopcion.com/v4/search?search=exxit-computacion&offset=0](https://api4.libreopcion.com/v4/search?search=exxit-computacion&offset=0)
[https://api4.libreopcion.com/v4/onlyResellers?search=exxit-computacion](https://api4.libreopcion.com/v4/onlyResellers?search=exxit-computacion)
[https://api4.libreopcion.com/v4/intervalPrices?search=exxit-computacion](https://api4.libreopcion.com/v4/intervalPrices?search=exxit-computacion)
[https://api4.libreopcion.com/v4/attributes?search=exxit-computacion](https://api4.libreopcion.com/v4/attributes?search=exxit-computacion)
[https://api4.libreopcion.com/v4/category?search=exxit-computacion](https://api4.libreopcion.com/v4/category?search=exxit-computacion)
[https://api4.libreopcion.com/v4/brands?search=exxit-computacion](https://api4.libreopcion.com/v4/brands?search=exxit-computacion)



Deben ser reactivas a mostrar los elementos para ese reseller
