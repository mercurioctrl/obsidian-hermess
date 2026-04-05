---
jira_key: "EXP-39"
summary: "API - Feat - Detalle seriales por ítem de pedido proveedor"
status: "Gamma"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-11-04 09:44"
updated: "2023-01-11 16:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-39"
---

# EXP-39: API - Feat - Detalle seriales por ítem de pedido proveedor

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-04 09:44 |
| Actualizado | 2023-01-11 16:02 |
| Etiquetas | ninguna |
| Jira | [EXP-39](https://bluinc.atlassian.net/browse/EXP-39) |

## Descripción

Este recurso se encarga de traer informacion sobre los seriales de un pedido de entrada

```
GET {API_URL}/v1/providersOrders/{providerOrderId}/serials/{itemId}
```

Retorna un array de objetos

```
[
  {
    "Title": "FUENTE GAMER GIGABYTE 550W 80 PLUS",
    "Id": "104964",
    "Sku": "GP-P550B",
    "imagen_principal": "https://static.nb.com.ar/i/nb_nombre-del-producto_ver_b65cd71de19e10c27d8c357cd99cded9.png",
    incomingQuantity: 25,
    "serials": [
      {
        admissionDate: 12-01-2022,
        serial: FAT43939393933
      },
      {
        admissionDate: 12-01-2022,
        serial: FAT43939393933
      },
      {
        admissionDate: 12-01-2022,
        serial: FAT43939393933
      }
    ]
}
]
```

**Las tablas que pueden intervenir son**

`SELECT * FROM [NewBytes_DBF].[dbo].[FP_Proveedores]`
`[NewBytes_DBF].[dbo].[PedProT]`

`[NewBytes_DBF].[dbo].[PedProl]`

`[NEW_BYTES].[dbo].[ST_DETALLE_STOCK]`

`[NewBytes_DBF].[dbo].[articulo]`

`[NEW_BYTES].[dbo].[ST_DESPACHOS_ENTRADAS_CABECERA]`
`[NEW_BYTES].[dbo].[ST_ENL_DESPACHOS_ENTRADAS_REMITOS]`
`[NEW_BYTES].[dbo].[ST_DESPACHOS_ENTRADAS_CABECERA]`
