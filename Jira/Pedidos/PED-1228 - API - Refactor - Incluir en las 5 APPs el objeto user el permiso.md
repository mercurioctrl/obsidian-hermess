---
jira_key: "PED-1228"
aliases: ["PED-1228"]
summary: "API - Refactor - Incluir en las 5 APPs el objeto user el permiso unlockedCompanyFilter"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-01-05 11:36"
updated: "2026-01-12 11:05"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1228"
---

# PED-1228: API - Refactor - Incluir en las 5 APPs el objeto user el permiso unlockedCompanyFilter

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-01-05 11:36 |
| Actualizado | 2026-01-12 11:05 |
| Etiquetas | ninguna |
| Jira | [PED-1228](https://bluinc.atlassian.net/browse/PED-1228) |

## Relaciones

- **Padre:** [[PED-1227 - Permiso de cambio de empresa para las 5 APPs|PED-1227]] Permiso de cambio de empresa para las 5 APPs
- **has action item:** [[PED-1229 - APP - Refactor - Incluir en las 5 APPs, el bloqueo del selector de empresa|PED-1229]] APP - Refactor - Incluir en las 5 APPs, el bloqueo del selector de empresa segun unlockedCompanyFilter

## Descripcion

Incluiremos el parámetro `unlockedCompanyFilter` proveniente de la tabla `NB_WEB.dbo.permisos_agente.unlockedCompanyFilter`

El funcionamiento es el mismo que `unlockedSellerFilter` 

```
GET /v1/auth/user
```

```
{
    "user": {
        "id": 81408,
        ...
        "unlockedSellerFilter": 1,
        "useStockIncoming": true,
        unlockedCompanyFilter: 1|0
    }
}
```

Esto se llevara a cabo para todas las aplicaciones listadas, segun cada objeto `user` en ellas

PedidosComprasInventarioPostventaExpedición
