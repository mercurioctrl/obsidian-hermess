---
jira_key: "LIO-101"
aliases: ["LIO-101"]
summary: "APP - Refactor - Cambios de precio y utilidad en el inventario"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2024-09-25 15:56"
updated: "2026-02-13 10:20"
labels: ["waiting"]
jira_url: "https://bluinc.atlassian.net/browse/LIO-101"
---

# LIO-101: APP - Refactor - Cambios de precio y utilidad en el inventario

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2024-09-25 15:56 |
| Actualizado | 2026-02-13 10:20 |
| Etiquetas | waiting |
| Jira | [LIO-101](https://bluinc.atlassian.net/browse/LIO-101) |

## Relaciones

- **Padre:** [[LIO-98]] Inventario resellers
- **action item from:** [[LIO-100]] API - Refactor - Permitir hacer el cambio de utilidad lineal sin restringir a minUtility
- **has action item:** [[LIO-536]] APP - Refactor - Cambiar la posibilidad de cambiar el precio de un item en el listado de inventario

## Descripcion

Se debe desconectar el recurso de la API LEGACY, para utilizar el recurso nuevo en APIv4

```
PATCH {{API_URL}}/v4/inventories/products/{id}/list
```

```
{
    "price" : 4983297
}
```

```
{
  "utility" : 2.51
}
```
