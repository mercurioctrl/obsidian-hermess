---
jira_key: "NBWEB-55"
aliases: ["NBWEB-55"]
summary: "Categorías / Marcas -  Barra Lateral"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-03-29 07:59"
updated: "2022-06-21 21:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-55"
---

# NBWEB-55: Categorías / Marcas -  Barra Lateral

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-29 07:59 |
| Actualizado | 2022-06-21 21:52 |
| Etiquetas | ninguna |
| Jira | [NBWEB-55](https://bluinc.atlassian.net/browse/NBWEB-55) |

## Relaciones

- **Padre:** [[NBWEB-52]] APP - Maquetado y Desarrollo - Home
- **relates to:** [[NBWEB-37]] Listar Categorias
- **relates to:** [[NBWEB-38]] Listar Marcas

## Descripcion

Para construir este elemento se utiliza el recurso 



```
GET {{API_URL}}/v1/categories
```

y

```
GET {{API_URL}}/v1/brands
```

que retornan un array de objetos del siguiente tipo:

Categorías:

```json
[
    {
        "description": "MEMORIAS",
        "id": "1",
        "initialB": "5",
        "initialC": "10        "
    },
    {
        "description": "DISCOS HDD",
        "id": "2",
        "initialB": "3",
        "initialC": "5         "
    }
]
```

Marcas:



```json
[
    {
        "description": "PIONNER",
        "id": "1",
        "imagen": "1.jpeg"
    },
    {
        "description": "THERMALTAKE",
        "id": "2",
        "imagen": "22thermaltake_medidas_nomanual.png"
    }
]
```



**Otras consideraciones: **

Según lo conversado en la reunión sobre el sitio, en la home deben estar los enlaces a todas las categorías y marcas, en todo momento.

Es decir que aunque los mismos enlaces estén ocultos a la vista según el diseño, deben estar en el HTML.

---

Los enlaces de las categorías deben ir según los siguientes ejemplos:

[https://www.nb.com.ar/brand/thermaltake](https://www.nb.com.ar/brand/thermaltake)

[https://www.nb.com.ar/categories/discos-hdd](https://www.nb.com.ar/categories/discos-hdd)
