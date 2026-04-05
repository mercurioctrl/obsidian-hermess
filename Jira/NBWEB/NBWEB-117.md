---
jira_key: "NBWEB-117"
summary: "APP - CMS - Login"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2022-04-12 09:11"
updated: "2022-07-21 10:43"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-117"
---

# NBWEB-117: APP - CMS - Login

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-12 09:11 |
| Actualizado | 2022-07-21 10:43 |
| Etiquetas | ninguna |
| Jira | [NBWEB-117](https://bluinc.atlassian.net/browse/NBWEB-117) |

## Descripción

Formulario de login para backoffice

Source:

```
POST {{API_URL}}/v1/cms/auth/login
```

Se debe generar un login desde un formulario, este es especifico del sitio y no es el mismo que utilizan los usuarios del sitio.
