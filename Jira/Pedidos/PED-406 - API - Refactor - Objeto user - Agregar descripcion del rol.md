---
jira_key: "PED-406"
aliases: ["PED-406"]
summary: "API - Refactor - Objeto user -> Agregar descripcion del rol"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-12-28 08:47"
updated: "2023-12-28 18:12"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-406"
---

# PED-406: API - Refactor - Objeto user -> Agregar descripcion del rol

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-12-28 08:47 |
| Actualizado | 2023-12-28 18:12 |
| Etiquetas | ninguna |
| Jira | [PED-406](https://bluinc.atlassian.net/browse/PED-406) |

## Relaciones

- **Padre:** [[PED-10]] Login y credenciales 

## Descripcion

```
GET {API_URL}/v1/auth/user
```

```
{
    "user": {
        "id": 7463,
        "codeFP": 19227,
        "username": "master",
        "email": "hermess87@gmail.com",
        "codeAgent": 12,
        "showName": "catriel2",
        "usuIdentificacion": "Seba",
        "pedidos": true,
        "pm": false,
        "roleDescription": "Ejecutivo De Cuentas" <--- se agrega el parametro
    }
}
```

El nuevo parámetro podemos encontrarlo en `[NewBytes_DBF].[dbo].[agentes].firma_puesto`
