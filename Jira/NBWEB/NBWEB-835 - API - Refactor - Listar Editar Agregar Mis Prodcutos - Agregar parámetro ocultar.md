---
jira_key: "NBWEB-835"
aliases: ["NBWEB-835"]
summary: "API - Refactor - Listar / Editar / Agregar Mis Prodcutos -> Agregar parámetro \"ocultar\""
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-08-20 09:37"
updated: "2024-08-25 23:04"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-835"
---

# NBWEB-835: API - Refactor - Listar / Editar / Agregar Mis Prodcutos -> Agregar parámetro "ocultar"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-20 09:37 |
| Actualizado | 2024-08-25 23:04 |
| Etiquetas | ninguna |
| Jira | [NBWEB-835](https://bluinc.atlassian.net/browse/NBWEB-835) |

## Relaciones

- **Padre:** [[NBWEB-610 - API - Refactor - Agregar internalTax a los montos finales de las ordenes dentro|NBWEB-610]] API - Refactor - Agregar internalTax a los montos finales de las ordenes dentro de Mi Cuenta
- **blocks:** [[NBWEB-838 - APP - Refactor - Listar Editar Agregar Mis Prodcutos - Agregar parámetro ocultar|NBWEB-838]] APP - Refactor - Listar / Editar / Agregar Mis Prodcutos -> Agregar parámetro "ocultar"

## Descripcion

Agregaremos un parámetro al recurso, que sirve para ocultar items específicos. Esto sirve para que no le aparezcan en la integración. (Varias veces consultaron como sacar los outlet o cosas especificas) 

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
    "description": "Procesador AMD blablabla",
    "hide": true/false <--- Nuevo parametro
  }
]
```
