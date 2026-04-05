---
jira_key: "NBWEB-162"
summary: "API - CMS - Listar Marcas"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-05-02 09:45"
updated: "2022-07-21 10:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-162"
---

# NBWEB-162: API - CMS - Listar Marcas

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-05-02 09:45 |
| Actualizado | 2022-07-21 10:42 |
| Etiquetas | ninguna |
| Jira | [NBWEB-162](https://bluinc.atlassian.net/browse/NBWEB-162) |

## Descripción

Se trata del recurso para listar los banners disponibles, para ser cambiado de orden, o editados

```
GET {{API_URL}}/v1/cms/brands
```

Retorna

```
[{
'brandId':1,
'img': "eb4fc89a3b443ae8ff7a622d14a3428b.png"
'description' : 'AMD',
'show': true
},
{
'brandId':1,
'img': "eb4fc89a3b443ae8ff7a622d14a3428b.png"
'description' : 'AMD',
'show': true
}]
```
