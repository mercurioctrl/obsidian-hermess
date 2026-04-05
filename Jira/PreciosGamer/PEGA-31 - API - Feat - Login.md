---
jira_key: "PEGA-31"
aliases: ["PEGA-31"]
summary: "API - Feat - Login"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-11-15 17:33"
updated: "2022-11-24 17:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-31"
---

# PEGA-31: API - Feat - Login

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-11-15 17:33 |
| Actualizado | 2022-11-24 17:16 |
| Etiquetas | ninguna |
| Jira | [PEGA-31](https://bluinc.atlassian.net/browse/PEGA-31) |

## Relaciones

- **Padre:** [[PEGA-30]] Feat - Login

## Descripcion

```
POST {{API_URL}}/v1/cms/auth/login
```

**Form-data:**

- User 


- Password



Para esto crearemos una tabla en `PEGA` llamada `cmsUsers`

Y crearemos un usuarios `master` con clave `npm8956`

La tabla debe tener al menos los siguientes campos

- Correo


- user name


- password


- roleId //inicializado en 1 


- lastDateLogin // la fecha e ultimo login
