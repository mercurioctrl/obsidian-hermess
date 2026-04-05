---
jira_key: "NBWEB-153"
summary: "API - CMS - Listar banners"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-04-29 10:49"
updated: "2022-08-01 12:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-153"
---

# NBWEB-153: API - CMS - Listar banners

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-29 10:49 |
| Actualizado | 2022-08-01 12:36 |
| Etiquetas | ninguna |
| Jira | [NBWEB-153](https://bluinc.atlassian.net/browse/NBWEB-153) |

## Descripción

Se trata del recurso para listar los banners disponibles, para ser cambiado de orden, o editados

```
GET {{API_URL}}/v1/cms/banner
```

Retorna

```
{
'type':1,
'img': "eb4fc89a3b443ae8ff7a622d14a3428b.png"
'url' : 'www.urldeejemplo.com',
'position': 3
},
```
