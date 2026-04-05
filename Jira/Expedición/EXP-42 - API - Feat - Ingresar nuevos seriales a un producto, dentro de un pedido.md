---
jira_key: "EXP-42"
aliases: ["EXP-42"]
summary: "API - Feat - Ingresar nuevos seriales a un producto, dentro de un pedido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-11-07 18:54"
updated: "2023-06-21 07:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-42"
---

# EXP-42: API - Feat - Ingresar nuevos seriales a un producto, dentro de un pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-07 18:54 |
| Actualizado | 2023-06-21 07:11 |
| Etiquetas | ninguna |
| Jira | [EXP-42](https://bluinc.atlassian.net/browse/EXP-42) |

## Relaciones

- **Padre:** [[EXP-11 - Feat - Serializar entrada de mercadería|EXP-11]] Feat - Serializar entrada de mercadería

## Descripcion

Este recurso se encarga de cargar nuevos seriales a un determinado item y lo hace a partir de una lista de seriales

```
POST {API_URL}/v1/providersOrders/{providerOrderId}/serials/{itemId}
```

Payload: 

```
[
  {
    mode:list, //indica el modo para la lista
    "serials": [
        'FAT43939393933',
        'FAT43939393933',
        'FAT43939393933',
        'FAT43939393933',
        'FAT43939393933',
        'FAT43939393933',
        'FAT43939393933',
    ]
}
]
```

**¿donde se guardan los seriales?**

Se guardan en la tabla `[NEW_BYTES].[dbo].[ST_DETALLE_STOCK]`

Una vez alcanzado el total de seriales, por la cantidad de items, no pueden cargarse mas seriales.
