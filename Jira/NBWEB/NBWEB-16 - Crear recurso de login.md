---
jira_key: "NBWEB-16"
aliases: ["NBWEB-16"]
summary: "Crear recurso de login"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-03-17 09:06"
updated: "2024-01-29 17:07"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-16"
---

# NBWEB-16: Crear recurso de login

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-17 09:06 |
| Actualizado | 2024-01-29 17:07 |
| Etiquetas | ninguna |
| Jira | [NBWEB-16](https://bluinc.atlassian.net/browse/NBWEB-16) |

## Relaciones

- **Padre:** [[NBWEB-6 - Login|NBWEB-6]] Login
- **relates to:** [[NBWEB-622 - API - Refactor - Crear recurso de login - Validar credenciales|NBWEB-622]] API - Refactor - Crear recurso de login - Validar credenciales

## Descripcion

La tabla que se utiliza para obtener los datos es 

```
[NB_WEB].[dbo].[usuarios_nb]
```



Debe estar en 

```
{{API_URL}}/auth/login
```



y debe devolver un objeto del siguiente tipo



```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NDc1MjIyMjcsImF1ZCI6Ijk0ZDhkMWYwMDRkZWE4NjQ4OGU0ODBkNWI2ZDUxZGRlZjUzNDA4ZTkiLCJ1c2VyIjp7ImlkIjoxLCJuYW1lIjoiRHVja3kiLCJlbWFpbCI6ImR1Y2t5QGxpYnJlb3BjaW9uLmNvbSIsInN0b3JlSWQiOjF9LCJpYXQiOjE2NDc1MTg2MjcsIm5iZiI6MTY0NzUxODYyN30.zYOaawI0ZJx7F3o_Jk65YFFlYJu2xc0hnP0WmdFDqro",
    "user": {
        "id": 23,
        "name": "nombreDeUsuario",
        "email": "correo@delusuario.com",
        "shoppingCartId": 3242,
        "codeFP": 343,
        "showName": "Nombre para mostrar",    
        "blackUser": 1,    
        "internalAgent": 343        
    }
}
```



Cuando se hace el login, deben guardarse las siguientes columnas, con los datos del usuario que corresponden a la informacion de su terminal y conexion



```
 [ssid_update]
 ,[ip]
 ,[os]
 ,[browser]
 ,[version]
 ,[user_agent]
```
