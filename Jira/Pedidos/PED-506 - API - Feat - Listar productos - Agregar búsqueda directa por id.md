---
jira_key: "PED-506"
aliases: ["PED-506"]
summary: "API - Feat - Listar productos -> Agregar búsqueda directa por id"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-01-19 09:58"
updated: "2024-01-26 03:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-506"
---

# PED-506: API - Feat - Listar productos -> Agregar búsqueda directa por id

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-01-19 09:58 |
| Actualizado | 2024-01-26 03:26 |
| Etiquetas | ninguna |
| Jira | [PED-506](https://bluinc.atlassian.net/browse/PED-506) |

## Relaciones

- **Padre:** [[PED-65 - Listado de productos|PED-65]] Listado de productos

## Descripcion

```
GET {API_URL}/v1/items?search=12343
```

Si detectamos que `search` solo tiene un id, seguiremos buscando en el titulo, porque puede ser parte de un nombre, pero ademas ingresaremos un filtro para buscar tambien por id, en caso de que le este mandando el id concreto del producto.

Esto matchea contra `[NewBytes_DBF].[dbo].[articulo].ID_ARTICULO` y produce un solo resultado en el caso de matchear exacto
