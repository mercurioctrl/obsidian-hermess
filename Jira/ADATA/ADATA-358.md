---
jira_key: "ADATA-358"
summary: "API - Feat - Autenticación (Login, Autoregistro, Recuperación de clave)"
status: "Listo"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2026-02-19 11:17"
updated: "2026-02-23 12:40"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/ADATA-358"
---

# ADATA-358: API - Feat - Autenticación (Login, Autoregistro, Recuperación de clave)

| Campo | Valor |
|-------|-------|
| Estado | Listo (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-19 11:17 |
| Actualizado | 2026-02-23 12:40 |
| Etiquetas | ninguna |
| Jira | [ADATA-358](https://bluinc.atlassian.net/browse/ADATA-358) |

## Descripción

Implementar:

- Login con correo + password


- Autoregistro de usuario


- Recuperación de clave (token expirable)



Endpoints sugeridos

- `POST /auth/register`


- `POST /auth/login`


- `POST /auth/forgot-password`


- `POST /auth/reset-password`


- `GET /me`



### Acceptance Criteria

AC

Criterio

AC1

Register crea usuario y permite login.

AC2

Login retorna sesión/token y permite acceder a /me.

AC3

Forgot/reset password funciona con token de un solo uso y expiración.

AC4

Errores son explícitos (credenciales inválidas, token vencido, etc.).
