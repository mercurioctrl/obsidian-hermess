---
jira_key: "NBWEB-61"
summary: "Buscador"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-03-29 16:41"
updated: "2022-06-21 21:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-61"
---

# NBWEB-61: Buscador

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-29 16:41 |
| Actualizado | 2022-06-21 21:34 |
| Etiquetas | ninguna |
| Jira | [NBWEB-61](https://bluinc.atlassian.net/browse/NBWEB-61) |

## Descripción

Se debe maquetar, conectar y construir las herramientas de filtrado y visualización para el buscador de productos

Para las busquedas se usa el recurso



```
GET [URL_PUNTERO]/terminos_de_busqueda
```

Retorna:



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
