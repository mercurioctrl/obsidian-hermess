---
jira_key: "NBWEB-116"
summary: "API - CMS - Login"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-04-12 08:44"
updated: "2022-06-26 21:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-116"
---

# NBWEB-116: API - CMS - Login

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-12 08:44 |
| Actualizado | 2022-06-26 21:09 |
| Etiquetas | ninguna |
| Jira | [NBWEB-116](https://bluinc.atlassian.net/browse/NBWEB-116) |

## Descripción

```
{{API_URL}}/v1/cms/auth/login
```

Utilizando la tabla `[NB_WEB].[dbo].[usuariosAdmin]` se debe generar un login especifico usando JWT para el cms, con este token y solo con este, deben autorizarse o no los recursos que están en
