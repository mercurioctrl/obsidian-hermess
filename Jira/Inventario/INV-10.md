---
jira_key: "INV-10"
summary: "API - Login"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-06-03 14:40"
updated: "2022-06-09 11:48"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-10"
---

# INV-10: API - Login

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-06-03 14:40 |
| Actualizado | 2022-06-09 11:48 |
| Etiquetas | ninguna |
| Jira | [INV-10](https://bluinc.atlassian.net/browse/INV-10) |

## Descripción

Se debe implementar con JWT para implementar un servicio de login y un sistema de roles

En principio crearemos una tabla de usuarios y una de roles según el siguiente esquema

**PRODUCTOS.dbo.users**

- id


- userName


- userEmail


- userPassword


- roleId


- userAgent


- userBrowser


- userOs


- userIp


- userLoginDate





**PRODUCTOS.dbo.userRoles**

- id


- description





En principio solo tendremos  dos perfiles: Administrador, Editor
