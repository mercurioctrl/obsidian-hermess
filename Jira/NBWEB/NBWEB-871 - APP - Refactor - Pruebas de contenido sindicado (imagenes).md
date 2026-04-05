---
jira_key: "NBWEB-871"
aliases: ["NBWEB-871"]
summary: "APP - Refactor - Pruebas de contenido sindicado (imagenes)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-09-09 11:22"
updated: "2024-09-11 11:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-871"
---

# NBWEB-871: APP - Refactor - Pruebas de contenido sindicado (imagenes)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-09 11:22 |
| Actualizado | 2024-09-11 11:22 |
| Etiquetas | ninguna |
| Jira | [NBWEB-871](https://bluinc.atlassian.net/browse/NBWEB-871) |

## Relaciones

- **Padre:** [[NBWEB-682 - Productos|NBWEB-682]] Productos

## Descripcion

Segun lo conversado, haremos una prueba para incluir el contenido sindicado por las marcas en la fichas de los productos.

En este caso iniciaremos las pruebas cuando el contenido es solo una imagen (que próximamente podremos cargar desde inventario como contenido sindicado específicamente).

Pero existe la posibilidad de que el material sea tambien código html o similares.

Al ser contenido a veces externo, otras imágenes grandes que pueden ser pesadas, se buscara alguna metodología para que la carga de este contenido no interfiera con la carga de la ficha.

Por esto usaremos algún mecanismo que nos permita cargar el material ultimo, una vez que el sitio y la ficha fueron cargados en su totalidad.

Las imágenes puede estar en nuestro servidor de imágenes o en uno externo y se llaman con una URL, no están en la compilación. 





[adjunto]
