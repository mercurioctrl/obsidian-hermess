---
jira_key: "INV-169"
aliases: ["INV-169"]
summary: "API - Refactor - Agregar cuantos items vienen por caja para lectura / edición"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-11-25 14:54"
updated: "2024-11-30 05:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-169"
---

# INV-169: API - Refactor - Agregar cuantos items vienen por caja para lectura / edición

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-25 14:54 |
| Actualizado | 2024-11-30 05:40 |
| Etiquetas | ninguna |
| Jira | [INV-169](https://bluinc.atlassian.net/browse/INV-169) |

## Relaciones

- **Padre:** [[INV-69 - Categorias|INV-69]] Categorias
- **has action item:** [[INV-170 - APP - Refactor - Agregar cuantos items vienen por caja para lectura edición|INV-170]] APP - Refactor - Agregar cuantos items vienen por caja para lectura / edición

## Descripcion

Agregaremos el parámetro `[NewBytes_DBF].[dbo].[familias].packagePerUnit` al recurso

```
GET {API_URL}/categories
```

```
[
    {
        "id": 20,
        "description": "ACCESORIOS",
        "webShow": 1,
        "alphaCode": "0020",
        "highAverage": 145.0,
        "widthAverage": 243.0,
        "lengthAverage": 140.0,
        "weightAverage": 500.0,
        "initStockMedium": 5,
        "initStockLarge": 325,
        "companyCode": null,
        "hide": 1,
        "packagePerUnit": 0.4 <-- SE AGREGA
        
    },
    {
        "id": 47,
        "description": "AIRE ACONDICIONADO",
        "webShow": 0,
        "alphaCode": "0047",
        "highAverage": null,
        "widthAverage": null,
...
```

---

```
PATCH {API_URL}/categories
```

```
{
    "id": 20,
    "description": "ACCESORIOS",
    "webShow": 1,
    "alphaCode": "0020",
    "highAverage": 145,
    "widthAverage": "242",
    "lengthAverage": 140,
    "weightAverage": 500,
    "initStockMedium": 5,
    "initStockLarge": 325,
    "packagePerUnit": 0.5, <--- Se agrega
    "companyCode": null,
    "hide": 1
}
```
