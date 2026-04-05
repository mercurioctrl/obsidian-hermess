---
jira_key: "NBWEB-4"
aliases: ["NBWEB-4"]
summary: "API - Catalogos de productos"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-15 15:10"
updated: "2024-04-30 15:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-4"
---

# NBWEB-4: API - Catalogos de productos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-15 15:10 |
| Actualizado | 2024-04-30 15:35 |
| Etiquetas | ninguna |
| Jira | [NBWEB-4](https://bluinc.atlassian.net/browse/NBWEB-4) |

## Relaciones

- **Subtarea:** [[NBWEB-36]] Clase para generar el objeto precio
- **Subtarea:** [[NBWEB-67]] Permitir ordenar el recurso, segun el planteo original
- **Subtarea:** [[NBWEB-69]] Cambio de url de la imagen por checkshum correcto y url completa
- **Subtarea:** [[NBWEB-232]] API - No se deben ver los productos ocultos, ni lo que son de distribucion externa
- **Subtarea:** [[NBWEB-251]] TASK - Deprecar campo ocultar de webartcomplement
- **Subtarea:** [[NBWEB-486]] API - Refactor - Agregar incremento por cliente
- **Subtarea:** [[NBWEB-628]] API - Refactor - Catálogos de productos - Visibilidad de precios
- **Subtarea:** [[NBWEB-753]] API - Catálogos de productos - Sugerencia de mejora al filtrar por categoría errónea
- **Subtarea:** [[NBWEB-760]] API - Refactor - Catálogos de productos - Filtrado por id de producto no coincidente
- **Subtarea:** [[NBWEB-1004]] API - Refactor - Recurso para leer precios -> Actualizar objeto de respuesta
- **relates to:** [[NBWEB-727]] API - Catálogos de productos - Oportunidad de mejora en el buscador del sitio

## Descripcion

```
GET [URL_PUNTERO]/terminos_de_busqueda
```

Los catálogos son todos los recursos que entregan listados de productos.

El recurso devuelve básicamente un array de objetos, donde cada objeto es un producto determinado con los siguientes atributos.

Se debe poder filtrar los resultados por

- Marca


- Categoría


- Id del producto


- Búsqueda mediante un Like dentro del campo titulo


- 10 mas vendidos


- 10 mas visitados



Se debe poder ordenar por precio ASC y DESC

```json
[{
"Title":"FUENTE GAMER GIGABYTE 550W 80 PLUS",
"Id":"104964",
"Sku":"GP-P550B",
"Category":"FUENTES ",
"IdCategory":"38",
"IdBrand":"4",
"Brand":"GIGABYTE ",
"initialB":null,
"initialC":null,
"Stock":"Alto",
"Price":{
    "value":"53.56365",
    "iva":10.5,
    "finalPrice":59.187833250000004
},
"imagen_principal":"https://static.nb.com.ar/i/nb_nombre-del-producto_ver_b65cd71de19e10c27d8c357cd99cded9.png"
},

{
"Title":"FUENTE GAMER GIGABYTE 550W 80 PLUS",
"Id":"104964",
"Sku":"GP-P550B",
"Category":"FUENTES ",
"IdCategory":"38",
"IdBrand":"4",
"Brand":"GIGABYTE ",
"initialB":null,
"initialC":null,
"Stock":"Alto",
"Price":{
    "value":"53.56365",
    "iva":10.5,
    "finalPrice":59.187833250000004
},
"imagen_principal":"https://static.nb.com.ar/i/nb_nombre-del-producto_ver_b65cd71de19e10c27d8c357cd99cded9.png"
}
]
```
