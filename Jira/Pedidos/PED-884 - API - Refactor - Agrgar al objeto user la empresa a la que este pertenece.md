---
jira_key: "PED-884"
aliases: ["PED-884"]
summary: "API - Refactor - Agrgar al objeto \"user\" la empresa a la que este pertenece"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-11-25 08:07"
updated: "2024-11-29 03:34"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-884"
---

# PED-884: API - Refactor - Agrgar al objeto "user" la empresa a la que este pertenece

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-11-25 08:07 |
| Actualizado | 2024-11-29 03:34 |
| Etiquetas | ninguna |
| Jira | [PED-884](https://bluinc.atlassian.net/browse/PED-884) |

## Relaciones

- **Padre:** [[PED-132]] Feat - Login / Re Login
- **has action item:** [[PED-883]] APP - Refactor - Agregar filtro empresa global

## Descripcion

Agregaremos el parámetro de empresa a

```
GET {API_URL}/v1/auth/user
```

El mismo proviene de la tabla `[NewBytes_DBF].[dbo].[agentes]` en un parametro nuevo que agregaremos llamado “`companyCode`”

```
{
    "user": {
        "id": 7463,
        "codeFP": 19227,
        "username": "catriel",
        "email": "hermess87@gmail.com",
        "codeAgent": 12,
        "companyCode": 4 <--SE AGREGA
        "showName": "catriel2",
        "usuIdentificacion": "Seba",
        "pedidos": true,
        "pm": true,
        "allComissions": false,
        "roleDescription": "Administrador",
        "discountShipping": true,
        "rebill": true,
        "orderOwner": null,
        "ip": "181.230.69.201",
        "whatsappAgent": null,
        "phoneAgent": null,
        "emailAgent": "soporteweb@nb.com.ar",
        "nameAgent": null,
        "roleAgent": "Administrador"
    }
}
```
