---
jira_key: "NBWEB-836"
aliases: ["NBWEB-836"]
summary: "API - Refactor - Listar / Editar / Agregar Mis Categorias -> Agregar parámetro \"ocultar\""
status: "Finalizada"
type: "Subtarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-08-20 09:49"
updated: "2024-08-25 23:03"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-836"
---

# NBWEB-836: API - Refactor - Listar / Editar / Agregar Mis Categorias -> Agregar parámetro "ocultar"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-08-20 09:49 |
| Actualizado | 2024-08-25 23:03 |
| Etiquetas | ninguna |
| Jira | [NBWEB-836](https://bluinc.atlassian.net/browse/NBWEB-836) |

## Relaciones

- **Padre:** [[NBWEB-610 - API - Refactor - Agregar internalTax a los montos finales de las ordenes dentro|NBWEB-610]] API - Refactor - Agregar internalTax a los montos finales de las ordenes dentro de Mi Cuenta
- **blocks:** [[NBWEB-837 - APP - Refactor - Listar Editar Agregar Mis Categorias - Agregar parámetro|NBWEB-837]] APP - Refactor - Listar / Editar / Agregar Mis Categorias -> Agregar parámetro "ocultar"

## Descripcion

Agregaremos un parámetro al recurso, que sirve para ocultar items específicos. Esto sirve para que no le aparezcan en la integración. (Varias veces consultaron como sacar los categorías o cosas especificas) 

```
GET {API_URL}/v1/miCuenta/misCategorias 
```

```
PATCH {API_URL}/v1/miCuenta/misCategorias
```

```
POST {API_URL}/v1/miCuenta/misCategorias
```

```
{
    "success": true,
    "categories": [
        {
            "categoryId": 2,
            "description": "DISCOS HDD",
            "userId": 7463,
            "categoryUserId": 340,
            "descriptionUser": "Discos Rigidos HDD",
            "utility": 10
            "hide": true/false <--- Nuevo parametro
  }
  ...
]
```
