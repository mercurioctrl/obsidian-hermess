---
jira_key: "PED-912"
aliases: ["PED-912"]
summary: "API - Refactor - Agregar permiso de \"Edicion de costo para una orden\""
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-12-20 08:28"
updated: "2025-01-02 10:56"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-912"
---

# PED-912: API - Refactor - Agregar permiso de "Edicion de costo para una orden"

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-20 08:28 |
| Actualizado | 2025-01-02 10:56 |
| Etiquetas | ninguna |
| Jira | [PED-912](https://bluinc.atlassian.net/browse/PED-912) |

## Relaciones

- **Padre:** [[PED-911]] Permisos, roles, etc
- **has action item:** [[PED-910]] APP - MVP - Refactor - Seleccionar costo para el item de una orden

## Descripcion

```
GET {API_URL}/v1/auth/user
```

```
{
    "user": {
        "id": 7463,
        "codeFP": 19227,
        "username": "catriel",
        "email": "hermess87@gmail.com",
        "codeAgent": 12,
        "showName": "catriel2",
        "usuIdentificacion": "Seba",
        "pedidos": true,
        "pm": true,
        "allComissions": false,
        "roleDescription": "Administrador",
        "discountShipping": true,
        "rebill": true,
        "orderOwner": null,
        "ip": "190.189.118.96",
        "whatsappAgent": null,
        "phoneAgent": null,
        "emailAgent": "soporteweb@nb.com.ar",
        "nameAgent": null,
        "roleAgent": "Administrador",
        "companyCode": null,
        "editCostForSale": 1 <--- Se agrega
    }
}
```

```
[NB_WEB].[dbo].[permisos_agente]
```
