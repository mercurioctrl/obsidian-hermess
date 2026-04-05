---
jira_key: "EXP-484"
aliases: ["EXP-484"]
summary: "API - Refactor - Agregar internalTax en el objeto de la orden para que el front sepa que debe enviarlo al acreditar"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-04-03 12:33"
updated: "2025-04-08 10:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-484"
---

# EXP-484: API - Refactor - Agregar internalTax en el objeto de la orden para que el front sepa que debe enviarlo al acreditar

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-04-03 12:33 |
| Actualizado | 2025-04-08 10:23 |
| Etiquetas | ninguna |
| Jira | [EXP-484](https://bluinc.atlassian.net/browse/EXP-484) |

## Relaciones

- **Padre:** [[EXP-116]] Devoluciones
- **blocks:** [[EXP-483]] APP - Refactor - Agregar internalTax en los casos que corresponda
- **has action item:** [[SNB-2914]] ERROR EN NC CON ART. CON IMP. INTERNO

## Descripcion

```
GET {API_URL}/v1/orders/X000200612288
```

```
[
...
    {
        "title": "MONITOR BENQ LED 27 GW2780 TPR BLACK",
        "id": 116291,
        "sku": "9H.LGELA.TPR",
        "category": "MONITORES        ",
        "idCategory": 7,
        "idBrand": 40,
        "brand": "BENQ",
        "mainImage": "158d3f0c8c97944e9e52b2eda4363b7e.jpeg",
        "notSerializable": 0,
        "incomingQuantity": 1,
        "serializedQuantity": 0,
        "fullSerialized": false,
        "acreditado": 0,
        "conIva": 258.910476,
        "ivaTax": 21,
        "sinIva": 213.9756,
        "cotizacion": 1094.5,
        "iibbPerceptions": 0,
        "internalTax": 23.46 <--- Se agrega
    }
  ...
]
```
