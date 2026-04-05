---
jira_key: "COM-144"
aliases: ["COM-144"]
summary: "APP - Refactor - Agregar item junto con su posición arancelaría "
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2024-09-18 02:35"
updated: "2024-09-22 20:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-144"
---

# COM-144: APP - Refactor - Agregar item junto con su posición arancelaría 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2024-09-18 02:35 |
| Actualizado | 2024-09-22 20:40 |
| Etiquetas | ninguna |
| Jira | [COM-144](https://bluinc.atlassian.net/browse/COM-144) |

## Relaciones

- **Padre:** [[COM-8 - Ordenes de compra|COM-8]] Ordenes de compra
- **relates to:** [[COM-70 - APP - Refactor - Agregar a el objeto del detalle de la orden la posicion|COM-70]] APP - Refactor - Agregar a el objeto del detalle de la orden la posicion arancelaria y sus impuestos 
- **relates to:** [[COM-143 - APP - Review - Problema al obtener posición arancelaria|COM-143]] APP - Review - Problema al obtener posición arancelaria

## Descripcion

Realizaremos un refactor para que al agregar un articulo a una orden de compra, esta se agregue junto con su posición arancelaria. 

Para esto, tomaremos la posición arancelaria que obtenemos al momento de buscar el articulo

```
https://gamma.api.purchases.lio.red/v1/items?search={termino de búsqueda}
```

[adjunto]
La cual incluiremos en la carga útil al momento de agregar el articulo a la orden y de esta manera el mensaje de respuesta del back contendrá su posición y en la interfaz poder visualizarla. 

```
https://gamma.api.purchases.lio.red/v1/providerOrder/{itemId}
```

[adjunto]
