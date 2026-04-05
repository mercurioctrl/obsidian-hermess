---
jira_key: "PED-1156"
aliases: ["PED-1156"]
summary: "APP - MVP - Trabar filtro asignado por vendedor (no se puede deseleccionar el vendedor)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Marbe Moreno"
created: "2025-10-17 10:47"
updated: "2025-11-20 16:13"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1156"
---

# PED-1156: APP - MVP - Trabar filtro asignado por vendedor (no se puede deseleccionar el vendedor)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Marbe Moreno |
| Creado | 2025-10-17 10:47 |
| Actualizado | 2025-11-20 16:13 |
| Etiquetas | ninguna |
| Jira | [PED-1156](https://bluinc.atlassian.net/browse/PED-1156) |

## Relaciones

- **Padre:** [[PED-8]] Listar ordenes de compra
- **has action item:** [[PED-1168]] API - MVP - Feat - Agregar permiso para bloquear el cambio de vendedor en los filtros al objeto user

## Descripcion

Solo dejaremos cambiar el filtro vendedor a quienes tengan el permiso `unlockedSellerFilter=True`

```
GET {API_URL}/v1/auth/user
```

```
{
    "user": {
        ...
        "unlockedSellerFilter": true <<-- Se agrega
        ...
    }
}
```
