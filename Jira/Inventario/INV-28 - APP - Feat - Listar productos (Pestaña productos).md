---
jira_key: "INV-28"
aliases: ["INV-28"]
summary: "APP - Feat - Listar productos (Pestaña productos)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2023-03-16 14:25"
updated: "2025-02-25 20:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-28"
---

# INV-28: APP - Feat - Listar productos (Pestaña productos)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2023-03-16 14:25 |
| Actualizado | 2025-02-25 20:42 |
| Etiquetas | ninguna |
| Jira | [INV-28](https://bluinc.atlassian.net/browse/INV-28) |

## Relaciones

- **Padre:** [[INV-27 - Productos|INV-27]] Productos
- **is blocked by:** [[INV-14 - API - Listar productos|INV-14]] API - Listar productos
- **is blocked by:** [[INV-20 - API - Editar detalle de producto|INV-20]] API - Editar detalle de producto
- **relates to:** [[INV-180 - APP - Refactor - Listar productos (Pestaña productos) - Portada no visible tras|INV-180]] APP - Refactor - Listar productos (Pestaña productos) - Portada no visible tras selección

## Descripcion

Basándonos en el recurso [link](https://lioteam.atlassian.net/browse/MSMET-14)  confeccionaremos un listado de productos con las siguientes columnas.

La idea del listado es que se use para poder ir cargando la informacion de los productos y por lo tanto, algunos datos son editables en el mismo contexto sin tener que abrir modales ni nada.

Para poder editar los atributos, usaremos el recurso [link](https://lioteam.atlassian.net/browse/MSMET-20) 

- Titulo (editable)


- Sku (editable)


- id


- Categoria decripcion (editable)


- Marca descripcion (editable)


- Imagen principal


- Garantia (editable)


- Decripcion (si viene true, mostrar algun simbolito como que esta completa)


- Cantidad de atributos


- Cantidad de imagenes


- ean (editable)


- upc (editable)


- gtin (editable)



#### Se debe poder filtrar por

- Categoria (desde el repo)


- Marca (desde el repo)


- Termino de busqueda (es un string)
