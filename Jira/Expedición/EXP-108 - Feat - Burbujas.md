---
jira_key: "EXP-108"
aliases: ["EXP-108"]
summary: "Feat - Burbujas"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Guillermo Avila"
reporter: "Catriel Mercurio"
created: "2022-12-19 12:21"
updated: "2023-02-06 15:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-108"
---

# EXP-108: Feat - Burbujas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Guillermo Avila |
| Reportado por | Catriel Mercurio |
| Creado | 2022-12-19 12:21 |
| Actualizado | 2023-02-06 15:52 |
| Etiquetas | ninguna |
| Jira | [EXP-108](https://bluinc.atlassian.net/browse/EXP-108) |

## Relaciones

- **Padre:** [[EXP-1 - Base y Repositorios|EXP-1]] Base y Repositorios
- **Subtarea:** [[EXP-109 - API - Feat - Burbujas de pendientes según cada pestaña|EXP-109]] API - Feat - Burbujas de pendientes según cada pestaña
- **Subtarea:** [[EXP-110 - APP - Feat - Burbujas de pendientes según cada pestaña|EXP-110]] APP - Feat - Burbujas de pendientes según cada pestaña
- **Subtarea:** [[EXP-531 - API - Refactor - Agregar companyCode y las burbujas pendings y controlar que|EXP-531]] API - Refactor - Agregar companyCode y las burbujas pendings y controlar que quede alineado con las cantidades de las pestañas
- **Subtarea:** [[EXP-532 - APP - Refactor - Agregar companyCode y las burbujas pendings y controlar que|EXP-532]] APP - Refactor - Agregar companyCode y las burbujas pendings y controlar que quede alineado con las cantidades de las pestañas
- **Subtarea:** [[EXP-536 - API - Review - Agregar companyCode y las burbujas pendings - Diferencias entre|EXP-536]] API - Review - Agregar companyCode y las burbujas pendings -> Diferencias entre los pendientes y listados
- **is blocked by:** [[EXP-133 - Ingresos - Cantidad de pendientes no coincidentes|EXP-133]] Ingresos - Cantidad de pendientes no coincidentes
- **is blocked by:** [[EXP-194 - Envíos - Cantidad de pendientes no coincidentes|EXP-194]] Envíos - Cantidad de pendientes no coincidentes
- **is blocked by:** [[EXP-195 - Pases de mercadería - Error al cargar datos|EXP-195]] Pases de mercadería - Error al cargar datos
- **is blocked by:** [[EXP-136 - Cantidad de pendientes no coincidentes en pases de mercadería|EXP-136]] Cantidad de pendientes no coincidentes en pases de mercadería
- **is blocked by:** [[EXP-134 - Retiros - Cantidad de pendientes no coincidentes|EXP-134]] Retiros - Cantidad de pendientes no coincidentes

## Descripcion

Estas burbujas buscan dar cuenta del la cantidad de pendientes que hay en cada uno de las pestañas a ser procesadas. Son tareas que es necesario hacer para remover de la lista y dejar en cero el numero de pendiente de cada pestaña.

Se trata del recurso que hacemos para estas aplicaciones que datan de cuantas acciones tenemos pendientes en cada pestaña.

- Ingresos: Mostraremos la cantidad de los que aun figuran como “no serializados”


- Retiros: Mostramos la cantidad de los RETIROS aun no despachados con el boton “despachar”


- Envíos: Mostramos la cantidad de los ENVIOS aun no despachados con el boton “despachar”


- Pases de mercadería: Mostramos la cantidad de paseas que aun no fueron “aceptados” y están pendientes.


- Inventario: Muestro la cantidad de productos que aun están pendientes de conteo.





- Al ingresar a cada pestaña en la aplicación la cantidad que debo ver inicialmente, es la que se indica en la burbuja de la pestaña.
