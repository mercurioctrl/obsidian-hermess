---
jira_key: "PEGA-194"
summary: "API - Feat -  Login con email y contraseña y Logout"
status: "En curso"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Emanuel Jesus Ferreyra"
created: "2025-05-23 13:23"
updated: "2025-06-24 10:20"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-194"
---

# PEGA-194: API - Feat -  Login con email y contraseña y Logout

| Campo | Valor |
|-------|-------|
| Estado | En curso (En curso) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2025-05-23 13:23 |
| Actualizado | 2025-06-24 10:20 |
| Etiquetas | ninguna |
| Jira | [PEGA-194](https://bluinc.atlassian.net/browse/PEGA-194) |

## Descripción

Se debe poder hacer login con email y contraseña

```
POST v1/reseller/login
```



payload:

```json
{
   "email": "katech@Katech.com",
   "password": "Katech1241"
}
```



response: 200 OK

```json
{
   "message": "Login exitoso",
   "data": {
      "id": 4,
      "reseller_code": null,
      "name": "Katech",
      "company_name": "Katech S.A.",
      "email": "katech@Katech.com",
      "created_at": "2025-05-27T22:34:47.000000Z",
      "updated_at": "2025-05-27T22:34:47.000000Z"
   },
   "token": "103|FbLWUGcZKF9U....."
}
```





Tambien su respectivo Logout.

```powershell
POST v1/reseller/logout 
```



response: 200 ok

```json
{
   "message": "Cierre de sesión exitoso"
}
```
