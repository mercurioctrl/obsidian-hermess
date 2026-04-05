---
jira_key: "NBWEB-654"
aliases: ["NBWEB-654"]
summary: "API - Refactor -Mis Categorías -> \"Mi categoría\" - Actualizar utilidad de usuario "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2024-03-18 15:03"
updated: "2024-03-20 14:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-654"
---

# NBWEB-654: API - Refactor -Mis Categorías -> "Mi categoría" - Actualizar utilidad de usuario 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2024-03-18 15:03 |
| Actualizado | 2024-03-20 14:44 |
| Etiquetas | ninguna |
| Jira | [NBWEB-654](https://bluinc.atlassian.net/browse/NBWEB-654) |

## Relaciones

- **Padre:** [[NBWEB-641 - Listas de precio|NBWEB-641]] Listas de precio

## Descripcion

Cuando se crean o eliminan categorías en "Mis Categorías", se debe activar/desactivar el campo `NewBytes_DBF.dbo.clientes.userUtility`. Este proceso tiene la intención de asegurar que, al crear una nueva categoría, el usuario pueda ver automáticamente la utilidad actualizada en los productos. De igual manera, al eliminar una categoría, se verifica que, en caso de no existir más categorías, se desactive el campo.

```
POST {API_URL}/v1/miCuenta/misCategorias
```

```
DELETE {{API_URL}}/v1/miCuenta/misCategorias/{categoryUserId}
```
