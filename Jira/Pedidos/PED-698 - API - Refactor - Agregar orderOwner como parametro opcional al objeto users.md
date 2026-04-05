---
jira_key: "PED-698"
aliases: ["PED-698"]
summary: "API - Refactor - Agregar orderOwner como parametro opcional al objeto users"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2024-04-25 15:52"
updated: "2024-04-29 02:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-698"
---

# PED-698: API - Refactor - Agregar orderOwner como parametro opcional al objeto users

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2024-04-25 15:52 |
| Actualizado | 2024-04-29 02:27 |
| Etiquetas | ninguna |
| Jira | [PED-698](https://bluinc.atlassian.net/browse/PED-698) |

## Relaciones

- **Padre:** [[PED-10 - Login y credenciales|PED-10]] Login y credenciales 
- **blocks:** [[PED-699 - APP - Feat - Si tengo el parametro orderOwner en el objeto user mostrare esos|PED-699]] APP - Feat - Si tengo el parametro orderOwner en el objeto user mostrare esos pedidos/filtros del vendedor
- **blocks:** [[SNB-1826 - NUMERO DE VENTA|SNB-1826]] NUMERO DE VENTA

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
        "orderOwner": 8, <---
        "showName": "catriel2",
        "usuIdentificacion": "Seba",
        "pedidos": true,
        "pm": false,
        "roleDescription": "Ejecutivo De Cuentas" <--- se agrega el parametro
    }
}
```

El parametro estara guardado en la tabla `[NewBytes_DBF].[dbo].agentes`
