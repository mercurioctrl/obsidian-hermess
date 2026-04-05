---
jira_key: "NBWEB-114"
aliases: ["NBWEB-114"]
summary: "API - CMS - Save Banners"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-04-12 07:56"
updated: "2022-08-01 12:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-114"
---

# NBWEB-114: API - CMS - Save Banners

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-12 07:56 |
| Actualizado | 2022-08-01 12:36 |
| Etiquetas | ninguna |
| Jira | [NBWEB-114](https://bluinc.atlassian.net/browse/NBWEB-114) |

## Relaciones

- **Padre:** [[NBWEB-73 - API - CMS - ABMS|NBWEB-73]] API - CMS - ABMS

## Descripcion

Se trata del recurso para posicionar un banner, 

```
PATCH {{API_URL}}/v1/cms/banner


ENVIO EL OBJETO CON LOS CHECKSUMS DE LAS IMAGENES A GUARDAR 


```

Request

```json
{
'type':1,
'img': [ {
"filename": "eb4fc89a3b443ae8ff7a622d14a3428b.png",
"url": "http://wwww.nb.com.ar/algo"
  ''
},
{
"filename": "eb4fc89a3b443ae8ff7a622d14a3428b.png",
"url": "http://wwww.nb.com.ar/algo"
}]
}
```
