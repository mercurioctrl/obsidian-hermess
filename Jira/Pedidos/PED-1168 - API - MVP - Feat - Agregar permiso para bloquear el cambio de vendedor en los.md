---
jira_key: "PED-1168"
aliases: ["PED-1168"]
summary: "API - MVP - Feat - Agregar permiso para bloquear el cambio de vendedor en los filtros al objeto user"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-11-07 17:52"
updated: "2025-11-20 16:14"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-1168"
---

# PED-1168: API - MVP - Feat - Agregar permiso para bloquear el cambio de vendedor en los filtros al objeto user

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-11-07 17:52 |
| Actualizado | 2025-11-20 16:14 |
| Etiquetas | ninguna |
| Jira | [PED-1168](https://bluinc.atlassian.net/browse/PED-1168) |

## Relaciones

- **Padre:** [[PED-8 - Listar ordenes de compra|PED-8]] Listar ordenes de compra
- **action item from:** [[PED-1156 - APP - MVP - Trabar filtro asignado por vendedor (no se puede deseleccionar el|PED-1156]] APP - MVP - Trabar filtro asignado por vendedor (no se puede deseleccionar el vendedor)

## Descripcion

Agregaremos en la tabla de permisos el parámetro `[NB_WEB].[dbo].[permisos_agente].unlockedSellerFilter` 

Adicionalmente agregaremos al objeto `user` el mismo permiso para que el front pueda disponer de el 

```
GET {API_URL}/v1/auth/user
```

```
{
    "user": {
        "id": 7463,
        "codeFP": 19227,
        "username": "Catriel",
        "email": "hermess87@gmail.com",
        "codeAgent": 12,
        "showName": "catriel2",
        "usuIdentificacion": "Seba",
        "pedidos": true,
        "pm": true,
        "allComissions": true,
        "roleDescription": "Administrador",
        "discountShipping": true,
        "rebill": true,
        "orderOwner": null,
        "ip": "181.87.118.6",
        "whatsappAgent": null,
        "phoneAgent": null,
        "emailAgent": "soporteweb@nb.com.ar",
        "nameAgent": null,
        "roleAgent": "Administrador",
        "companyCode": null,
        "editCostForSale": null,
        "unlimitedReports": null,
        "createManualVoucher": 1,
        "banListPrice": null,
        "unlockedSellerFilter": true <<-- Se agrega
    }
}
```
