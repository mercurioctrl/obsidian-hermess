---
jira_key: "INV-163"
aliases: ["INV-163"]
summary: "API - Refactor - Agregar los parametros \"notSerializable\" Y \"national\""
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-10-18 09:42"
updated: "2024-10-21 23:02"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-163"
---

# INV-163: API - Refactor - Agregar los parametros "notSerializable" Y "national"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-10-18 09:42 |
| Actualizado | 2024-10-21 23:02 |
| Etiquetas | ninguna |
| Jira | [INV-163](https://bluinc.atlassian.net/browse/INV-163) |

## Relaciones

- **Padre:** [[INV-23 - Aplicacion de inventario|INV-23]] Aplicacion de inventario
- **has action item:** [[INV-164 - APP - Refactor - Agregar los parametros notSerializable y national a la carga|INV-164]] APP - Refactor - Agregar los parametros "notSerializable" y "national" a la carga masiva
- **has action item:** [[SNB-2417 - Agregar a las altas masivas de producto la posibilidad de poner nacional y que|SNB-2417]] Agregar a las altas masivas de producto la posibilidad de poner nacional y que no sea serializable

## Descripcion

```
POST {API_URL}/import/xlsx
```

```
{
  "file": "undefined",
  "currency": "1",
  "companyCode": "04",
  "distribuitor": "1",
  "preview": "0",
  "notSerializable" : true/false  <-- NUEVO
  "national" : true / false <--- NUEVO
  "mapping": {
    "A": "mainImage",
    "B": "sku",
    "C": "title",
    "D": "brand",
    "E": "category",
    "F": "price",
    "G": "stock",
    "H": "iva",
    "I": "officialSiteUrl"
  }
}
```



Para marcar si es nacional se usa `[NewBytes_DBF].[dbo].[articulo].national`
