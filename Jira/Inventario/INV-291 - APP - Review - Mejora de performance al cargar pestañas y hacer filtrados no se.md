---
jira_key: "INV-291"
aliases: ["INV-291"]
summary: "APP - Review - Mejora de performance al cargar pestañas y hacer filtrados no se debe hacer mas de 1 vez la solicitud "
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Marbe Moreno"
created: "2025-12-18 17:04"
updated: "2025-12-23 19:04"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-291"
---

# INV-291: APP - Review - Mejora de performance al cargar pestañas y hacer filtrados no se debe hacer mas de 1 vez la solicitud 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Marbe Moreno |
| Creado | 2025-12-18 17:04 |
| Actualizado | 2025-12-23 19:04 |
| Etiquetas | ninguna |
| Jira | [INV-291](https://bluinc.atlassian.net/browse/INV-291) |

## Relaciones

- **Padre:** [[INV-23]] Aplicacion de inventario

## Descripcion

En todas las pestañás ocurria que se llamaba mas de una vez algun recurso, sea marcas categorias o incluso itemsStock se llamaba 3 veces

[adjunto]
si no hay mas que un cambio no se debe disparar 3 veces debe ser una sola

**Criterios de aceptación**

- Revisar que todos los filtrados funcionen bien de todas las pestañás que el recurso solo se llame una vez sea por recarga de pagina, por cambio en el algún selector o input de busqueda


- La pestaña de *ItemsStock* debe mostrar un mensaje en caso que se ingrese con una cuenta q no tiene companycode asociado o este el filtro general (tuerquita) en ***Todos***: que se debe seleccionar ‘empresa’ para poder filtrar ya que sino es muy larga la cantidad de opciones y realentiza la petición


- Hacer que todos los selectores de marca y categoría al no estar filtrado por empresa tenga el span segun empresa 


- Revisar por qué si no hay `companyCode` seleccionado y se entra a una ruta.. no se obtienen las marcas


- Al cambiar empresa desde el settings general (la tuerquita del lado superior derecho).. debe limpiar brands y categories  seleccionadas en selectores y obtenerlas nuevamente segun el companyCode nuevo


- Al iniciar sesion, o con sesion que no tiene companycode debo setear TODOS en el setting general de empresa y sub selectores
