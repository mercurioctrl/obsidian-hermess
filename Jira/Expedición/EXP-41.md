---
jira_key: "EXP-41"
summary: "APP - Feat - Detalle seriales por ítem de pedido proveedor"
status: "Gamma"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-11-07 18:37"
updated: "2023-01-11 16:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-41"
---

# EXP-41: APP - Feat - Detalle seriales por ítem de pedido proveedor

| Campo | Valor |
|-------|-------|
| Estado | Gamma (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-07 18:37 |
| Actualizado | 2023-01-11 16:02 |
| Etiquetas | ninguna |
| Jira | [EXP-41](https://bluinc.atlassian.net/browse/EXP-41) |

## Descripción

Al hacer clic en uno de los items de [link](https://lioteam.atlassian.net/browse/EXP-40) que son los detalles de un pedido de compra, se debe abrir un modal con una tablita que contenga la lista de seriales que tiene ese producto para ese pedido.

Desde el recurso [link](https://lioteam.atlassian.net/browse/EXP-39) obtendremos información del siguiente tipo

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

Se debe mostrar la informacion completa de la cabecera y una tablita con los serials que estan dentro del objote, la fecha y una columna mas para un icono de “borar serial”.
