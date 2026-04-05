---
jira_key: "NBWEB-408"
aliases: ["NBWEB-408"]
summary: "API - Feat - Listar banners"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-07-18 12:31"
updated: "2022-08-01 12:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-408"
---

# NBWEB-408: API - Feat - Listar banners

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-18 12:31 |
| Actualizado | 2022-08-01 12:36 |
| Etiquetas | ninguna |
| Jira | [NBWEB-408](https://bluinc.atlassian.net/browse/NBWEB-408) |

## Relaciones

- **Padre:** [[NBWEB-50]] Sitio Web
- **Subtarea:** [[NBWEB-410]] API - Feat - Agregar esquema de zonas a los banners

## Descripcion

Este recurso es para listar banners en distintas ‘zonas’ del sitio

```
GET {{API_URL}}/v1/banners/{zoneId}
```

Retorna

```
[{
  "image":"https://static.nb.com.ar/img/add70ebedb1a41811649e2e0d0ba158e.jpg",
  "link" : "https://nb.com.ar/genius"  
},
{
  "image":"https://static.nb.com.ar/img/add70ebedb1a41811649e2e0d0ba158e.jpg",
  "link" : "https://nb.com.ar/genius"  
},
{
  "image":"https://static.nb.com.ar/img/add70ebedb1a41811649e2e0d0ba158e.jpg",
  "link" : "https://nb.com.ar/genius"  
}
]
```
