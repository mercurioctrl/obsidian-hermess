---
jira_key: "BLUWEB-24"
summary: "API - Faet - Login de usuarios"
status: "LISTO"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-05-14 10:11"
updated: "2025-05-16 17:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-24"
---

# BLUWEB-24: API - Faet - Login de usuarios

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-14 10:11 |
| Actualizado | 2025-05-16 17:11 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-24](https://bluinc.atlassian.net/browse/BLUWEB-24) |

## Descripción

```
POST {API_URL}/login
```

```
{
  "email": "usuario@example.com",
  "password": "secret123"
}
```

Response 200 – Login exitoso (devuelve el objeto users)

```
{
  "token": "jwt_token",
  "user": {
    "id": 1,
    "first_name": "Juan",
    "last_name": "Pérez",
    "email": "usuario@example.com",
    "role": "client",
    "job_title": "Comprador",
    "phone": "1123456789",
    "whatsapp": "1123456789",
    "cbu": "2850590940090412345671",
    "alias": "juan.cuenta.banco",
    "status": "active"
  }
}

```

Response 401 – Credenciales inválidas

```
{
  "error": "Invalid credentials"
}
```

Response 403 – Usuario inactivo

```
{
  "error": "User is inactive"
}
```

Response 422 – Campos faltantes

```
{
  "errors": {
    "email": ["The email field is required."],
    "password": ["The password field is required."]
  }
}
```

### Comportamiento esperado

- Valida que el **email exista** y la contraseña coincida usando `Hash::check()`


- El usuario debe tener `status = 'active'`


- Devuelve token JWT firmado


- Devuelve objeto `user` con todos los campos definidos:

- `first_name`


- `last_name`


- `email`


- `role` (desde `users.role` o relacionada con tabla `roles`)


- `job_title`


- `phone`


- `whatsapp`


- `cbu`


- `alias`


- `status`





---

###  Criterios de aceptación

- Si el usuario está inactivo, no se permite el login (código 403)


- La contraseña es validada con `Hash::check()`


- El token es generado y devuelto con `JWT` (proponer otro metodo si existe algo mas conveniente)


- Se loguea el evento de login exitoso o fallido si corresponde (opcional)
