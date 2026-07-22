---
jira_key: PEGA-194
status: En curso
assignee: Emanuel Jesus Ferreyra
assignee_email: null
reporter: Emanuel Jesus Ferreyra
priority: Medium
issuetype: Subtarea
project: PEGA
updated: "2025-06-24T10:20:50.531-0300"
created: "2025-05-23T13:23:47.979-0300"
url: "https://bluinc.atlassian.net/browse/PEGA-194"
tags: [jira, PEGA, en-curso]
---

# PEGA-194 · API - Feat -  Login con email y contraseña y Logout

[PEGA-194 en Jira](https://bluinc.atlassian.net/browse/PEGA-194)

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

## Comentarios (2)

### @Guillermo Avila — 2025-06-10 10:58:55

1. Solo me gustaría comentar la adición del parámetro `success`.

```
{
  "success": true,                    // true o false
  "message": "Operación exitosa",     // Descripción opcional
  "data": {}                          // Objeto con datos devueltos o null
}
```

### @Guillermo Avila — 2025-06-24 10:20:42

1. Recomendaciones anteriores:

---
_Sincronizado por jira-sidecar el 2026-06-07 22:27:20 UTC._
