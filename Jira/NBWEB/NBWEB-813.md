---
jira_key: "NBWEB-813"
summary: "APP - Listar/Editar/Agregar Mis Productos - Filtro por categoría no coincidente "
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Guillermo Avila"
created: "2024-08-07 02:34"
updated: "2024-08-08 05:23"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-813"
---

# NBWEB-813: APP - Listar/Editar/Agregar Mis Productos - Filtro por categoría no coincidente 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Guillermo Avila |
| Creado | 2024-08-07 02:34 |
| Actualizado | 2024-08-08 05:23 |
| Etiquetas | ninguna |
| Jira | [NBWEB-813](https://bluinc.atlassian.net/browse/NBWEB-813) |

## Descripción

Al seleccionar algún filtro por categoría no me devuelve los resultados esperados (objeto vacío). Esto puede ser debido a como se está formulando la petición.

```
GET	https://gamma.api.nb.com.ar/v1/miCuenta/misProductos?query={"category":"44"}
```

[attachment]
