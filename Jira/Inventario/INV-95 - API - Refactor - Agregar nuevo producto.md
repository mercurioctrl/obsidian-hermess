---
jira_key: "INV-95"
aliases: ["INV-95"]
summary: "API - Refactor - Agregar nuevo producto"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-08-15 15:47"
updated: "2024-09-24 03:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-95"
---

# INV-95: API - Refactor - Agregar nuevo producto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-15 15:47 |
| Actualizado | 2024-09-24 03:12 |
| Etiquetas | ninguna |
| Jira | [INV-95](https://bluinc.atlassian.net/browse/INV-95) |

## Relaciones

- **Padre:** [[INV-27 - Productos|INV-27]] Productos
- **blocks:** [[INV-102 - APP - Refactor - Agregare nuevo producto|INV-102]] APP - Refactor - Agregare nuevo producto
- **relates to:** [[INV-104 - API - Agregar nuevo producto - Sugerencia de mejora en el llenado de columnas|INV-104]] API - Agregar nuevo producto - Sugerencia de mejora en el llenado de columnas
- **relates to:** [[PED-831 - APP - Refactor - Agregar stock de Postventa - Agregar sucursal|PED-831]] APP - Refactor - Agregar stock de Postventa -> Agregar sucursal

## Descripcion

Agregaremos el recurso necesario para crear un producto de cero, para eso debemos crear como minimo dos registros fundamentales en dos tablas

`[NewBytes_DBF].[dbo].[articulo]` y `[NewBytes_DBF].[dbo].[stocks]`

```
POST {API_URL}/item
```

```
    {
            "title": "OUTLET GABINETE SFX RACKEABLE A4U450 ",
            "sku": "OA4U450",
            "id": 104393,
            "categoryId": 60,
            "brandId": 18,
            "stock": 0.0,
            "warranty": "3 meses ",
            "ean": null,
            "upc": "000000104393",
}
```

En el caso de `[NewBytes_DBF].[dbo].[stocks]` incializaremos todos los stock en cero

Tener en cuenta que los parametros

```
,[cref]
,[codigo]
,[ID_ARTICULO]

```

siempre valen lo mismo, porque son producto de la implementaicon de distintos sistemas en el tiempo. Hoy en dia logramos tener claves numericas (ID_ARTICULO) por lo tanto los demas toman su valor
