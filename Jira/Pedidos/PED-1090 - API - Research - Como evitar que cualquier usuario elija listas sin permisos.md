---
jira_key: "PED-1090"
aliases: ["PED-1090"]
summary: "API - Research - Como evitar que cualquier usuario elija listas sin permisos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-08-28 10:01"
updated: "2025-09-02 16:52"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1090"
---

# PED-1090: API - Research - Como evitar que cualquier usuario elija listas sin permisos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-28 10:01 |
| Actualizado | 2025-09-02 16:52 |
| Etiquetas | ninguna |
| Jira | [PED-1090](https://bluinc.atlassian.net/browse/PED-1090) |

## Relaciones

- **Padre:** [[PED-237 - Precios|PED-237]] Precios

## Descripcion

Dado que no todos los vendedores tienen permitido usar cualquier lista (en este caso se da para la lista E pero en Laset suele ser común según para cada vendedor asignar listas puntuales)

Se buscara la mejor forma de poder limitar el acceso a las mismas, para cada vendedor.

Lo mas conveniente es poder hacerlo por omisión, es decir marcar aquellas listas a las que queremos que ciertas personas de la tabla  `[NewBytes_DBF].[dbo].[agentes]` no tengan acceso, aunque podemos escuchar diferentes propuestas de como hacerlo mejor.

Se debe tener en cuenta un esquema claro, que permita que cada agenta pueda ver o no ver ciertas listas de precios y que sea lo mas performativo posible.

Podría aplicar al recurso 

```
GET {API_URL}/v1/orders/{branch-order}
```

O directamente al cambiar el item como una restricción

```
PATCH {API_URL}/v1/orders/addItem
```

[adjunto]
Si queres revisa los recursos y lo charlamos !
