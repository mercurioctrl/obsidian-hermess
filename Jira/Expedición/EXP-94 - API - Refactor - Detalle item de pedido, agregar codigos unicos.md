---
jira_key: "EXP-94"
aliases: ["EXP-94"]
summary: "API - Refactor - Detalle item de pedido, agregar codigos unicos"
status: "Gamma"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-11-22 13:51"
updated: "2022-12-15 09:53"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-94"
---

# EXP-94: API - Refactor - Detalle item de pedido, agregar codigos unicos

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-22 13:51 |
| Actualizado | 2022-12-15 09:53 |
| Etiquetas | ninguna |
| Jira | [EXP-94](https://bluinc.atlassian.net/browse/EXP-94) |

## Relaciones

- **Padre:** [[EXP-10 - Feat - Listar pedidos (despachos) proveedores|EXP-10]] Feat - Listar pedidos (despachos) proveedores

## Descripcion

Se debe hacer un reactor de [link](https://lioteam.atlassian.net/browse/EXP-38) para uncluir los `codigos unicos `

- upc


- ean


- gtin


- isb



Esto nos servirá desde el front para determinar si debo pedirlos, ademas de para identificar mejor los productos

```
GET {API_URL}/v1/providersOrders/{providerOrderId}
```

Retorna

```
[
    {
    "Title": "FUENTE GAMER GIGABYTE 550W 80 PLUS",
    "Id": "104964",
    "Sku": "GP-P550B",
    "Category": "FUENTES ",
    "IdCategory": "38",
    "IdBrand": "4",
    "Brand": "GIGABYTE ",
    "imagen_principal": "https://static.nb.com.ar/i/nb_nombre-del-producto_ver_b65cd71de19e10c27d8c357cd99cded9.png",
    "fullSerialized": true, //este parametro aun no lo tenes, lo desarrollaremos mas adelante
    "incomingQuantity": 25,
    "serializedQuantity": 25,
    "notSerializable": false,
    gtin:null,
    ean:0012345678905,
    isbn: null,
    upc:012345678905
   }
]
```
