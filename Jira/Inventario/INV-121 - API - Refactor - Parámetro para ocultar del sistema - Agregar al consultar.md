---
jira_key: "INV-121"
aliases: ["INV-121"]
summary: "API - Refactor - Parámetro para ocultar del sistema - Agregar al consultar"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-09-11 05:14"
updated: "2024-09-13 03:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-121"
---

# INV-121: API - Refactor - Parámetro para ocultar del sistema - Agregar al consultar

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-09-11 05:14 |
| Actualizado | 2024-09-13 03:23 |
| Etiquetas | ninguna |
| Jira | [INV-121](https://bluinc.atlassian.net/browse/INV-121) |

## Relaciones

- **relates to:** [[INV-115]] API - Refactor - Agregar parametro para ocultar del sistema

## Descripcion

Agregaremos el parámetro así como se hizo en los demás recursos pero ahora al consultar. Esto es necesario para que la interfaz pueda mostrar los ocultos del sistema.

`hide`

```
GET {{API_URL}}/v1/categories
```

```
    {
        "id": 20,
        "description": "ACCESORIOS",
        "webShow": 1,
        "hide": <----------------------------- Se agrega
        "alphaCode": "0020",
        "highAverage": 145.0,
        "widthAverage": 243.0,
        "lengthAverage": 140.0,
        "weightAverage": 500.0,
        "initStockMedium": 5,
        "initStockLarge": 325,
        "companyCode": null
    },
```
