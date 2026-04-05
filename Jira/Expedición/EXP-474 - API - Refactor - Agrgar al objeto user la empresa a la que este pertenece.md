---
jira_key: "EXP-474"
aliases: ["EXP-474"]
summary: "API - Refactor - Agrgar al objeto \"user\" la empresa a la que este pertenece"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-12-16 09:19"
updated: "2024-12-17 10:46"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/EXP-474"
---

# EXP-474: API - Refactor - Agrgar al objeto "user" la empresa a la que este pertenece

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-12-16 09:19 |
| Actualizado | 2024-12-17 10:46 |
| Etiquetas | ninguna |
| Jira | [EXP-474](https://bluinc.atlassian.net/browse/EXP-474) |

## Relaciones

- **Padre:** [[EXP-1 - Base y Repositorios|EXP-1]] Base y Repositorios

## Descripcion

Agregaremos el parámetro de empresa a

```
GET {API_URL}/v1/auth/user
```

El mismo proviene de la tabla `[NewBytes_DBF].[dbo].[agentes]` en un parámetro nuevo que agregaremos llamado “`companyCode`”

```
{
    "user": {
        "id": "7463",
        "codeFP": "19227",
        "username": "catriel",
        "email": "hermess87@gmail.com",
        "codeAgent": 12,
        "showName": "catriel2",
        "usuIdentificacion": "Seba",
        "expedicion": 1,
        "expedicionAdmin": 1,
        "management": 1,
        "exp_upload_serials": 1,
        "exp_items": 1,
        "companyCode": 4, <--- AGREGAR
    }
}
```
