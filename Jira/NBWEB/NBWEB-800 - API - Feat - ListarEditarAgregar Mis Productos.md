---
jira_key: "NBWEB-800"
aliases: ["NBWEB-800"]
summary: "API - Feat - Listar/Editar/Agregar Mis Productos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-07-31 13:26"
updated: "2024-08-02 01:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-800"
---

# NBWEB-800: API - Feat - Listar/Editar/Agregar Mis Productos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-07-31 13:26 |
| Actualizado | 2024-08-02 01:14 |
| Etiquetas | ninguna |
| Jira | [NBWEB-800](https://bluinc.atlassian.net/browse/NBWEB-800) |

## Relaciones

- **Padre:** [[NBWEB-610]] API - Refactor - Agregar internalTax a los montos finales de las ordenes dentro de Mi Cuenta
- **blocks:** [[NBWEB-801]] APP - Feat - Listar/Editar/Agregar Mis Productos

## Descripcion

Con el mismo criterio que trabajamos en [link](https://lioteam.atlassian.net/browse/NBWEB-644)  para permitirle a los clientes que desde la sección Mi cuenta > Mis categorías marquen nombre y utildad, haremos lo propio para el caso de los productos.

```
GET {API_URL}/v1/miCuenta/misProductos?categoryId=4
```

```
PATCH {API_URL}/v1/miCuenta/misProductos
```

```
POST {API_URL}/v1/miCuenta/misProductos
```

```
[
  {
    "id": 1,
    "userId": 7463,
    "itemId": 64,
    "utility": 23.0,
    "description": "Procesador AMD blablabla"
  }
]
```

Notese que el recurso para el metodo GET tiene un filtro categoryId que sirve para el caso de tener muchos items, igual que estén filtrados por categoría
