---
jira_key: "LIO-586"
aliases: ["LIO-586"]
summary: "APP - Refactor - Ajustar el match de los resellers segun internalId y title"
status: "Ready for QA"
type: "Tarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Marbe Moreno"
created: "2026-03-30 10:31"
updated: "2026-03-30 11:01"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-586"
---

# LIO-586: APP - Refactor - Ajustar el match de los resellers segun internalId y title

| Campo | Valor |
|-------|-------|
| Estado | Ready for QA (En curso) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Marbe Moreno |
| Creado | 2026-03-30 10:31 |
| Actualizado | 2026-03-30 11:01 |
| Etiquetas | ninguna |
| Jira | [LIO-586](https://bluinc.atlassian.net/browse/LIO-586) |

## Relaciones

- **Padre:** [[LIO-2 - Variedad y Calidad de ProductosCatalogos|LIO-2]] Variedad y Calidad de Productos/Catalogos

## Descripcion

ahora como se duplican los productos al GET `resellerByItemId` en el back se le agreguó el title para poder matchear

```
{
    "internalId": 121159,
    "title": "PENDRIVE NETAC U185 WHITE 64GB USB 3.0",// nuevo parametro
    "resellers": [
        {
            "id": 752967,
            "resellerDescription": "STORE GS",
            "resellerPrice": 8045.75,
            "freeShipping": 0,
            "vendedor": null
        },
        {
            "id": 752961,
            "resellerDescription": "Gears Store",
            "resellerPrice": 8045.75,
            "freeShipping": 0,
            "vendedor": null
        },
        {
            "id": 752985,
            "resellerDescription": "Exxit Computación",
            "resellerPrice": 8045.75,
            "freeShipping": 0,
            "vendedor": null
        }
    ]
}
```

debiendo quedar de manera inversa  a la imagen, es decir, actualmente  si se busca pendriva netac los vendedores aparecen en el item de tienda Hunnox pero deben aparecer en el item de abajo, esto sucede proque comparten el mismo internalId
