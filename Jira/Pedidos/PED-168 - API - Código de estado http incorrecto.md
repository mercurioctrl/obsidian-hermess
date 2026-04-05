---
jira_key: "PED-168"
aliases: ["PED-168"]
summary: "API - Código de estado http incorrecto"
status: "Finalizada"
type: "Error"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Guillermo Avila"
created: "2023-10-25 23:24"
updated: "2023-10-26 14:21"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-168"
---

# PED-168: API - Código de estado http incorrecto

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Error |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Guillermo Avila |
| Creado | 2023-10-25 23:24 |
| Actualizado | 2023-10-26 14:21 |
| Etiquetas | ninguna |
| Jira | [PED-168](https://bluinc.atlassian.net/browse/PED-168) |

## Relaciones

- **blocks:** [[PED-10 - Login y credenciales|PED-10]] Login y credenciales 

## Descripcion

Al intentar iniciar sesión con credenciales incorrectas me devuelve un código de estado http 200 lo cual el FrontEnd no detecta que hubo un error y por consecuencia no muestra al usuario que algo salió mal.

Aparte de notificarle al usuario que las credenciales son incorrectas, como lo hemos manejado ya, habrá que informarle específicamente si cuál de los datos (usuario o contraseña) es el incorrecto.

[adjunto]
[adjunto]
