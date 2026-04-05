---
jira_key: "BULLY-14"
summary: "API - Feat - Login"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-06-22 10:25"
updated: "2023-06-28 10:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BULLY-14"
---

# BULLY-14: API - Feat - Login

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-06-22 10:25 |
| Actualizado | 2023-06-28 10:32 |
| Etiquetas | ninguna |
| Jira | [BULLY-14](https://bluinc.atlassian.net/browse/BULLY-14) |

## Descripción

Se agregara el recurso de login con JWT para 

```
POST {API_URL}/v1/login
```

```
username
pass
```

Los mismos deben guardarse en la siguientes columnas de la tabla `users` que crearemos para tal fin

`[bulliTicker].dbo.users.username`

`[bulliTicker].dbo.users.password`

La tabla tendra

id

id autonumerico

username

Nombre de ususario

password

clave encriptada

lastConectionDate

fecha de ultima conexion
