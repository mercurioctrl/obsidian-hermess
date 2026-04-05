---
jira_key: "PEGA-49"
aliases: ["PEGA-49"]
summary: "API - Feat - Guardar banners"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-01-03 10:02"
updated: "2023-01-09 13:50"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-49"
---

# PEGA-49: API - Feat - Guardar banners

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-01-03 10:02 |
| Actualizado | 2023-01-09 13:50 |
| Etiquetas | ninguna |
| Jira | [PEGA-49](https://bluinc.atlassian.net/browse/PEGA-49) |

## Relaciones

- **Padre:** [[PEGA-33 - Feat - Administrar sliders|PEGA-33]] Feat - Administrar sliders
- **blocks:** [[PEGA-35 - APP - Feat - Administrar sliders|PEGA-35]] APP - Feat - Administrar sliders

## Descripcion

Se trata del recurso para posicionar un banner,

```
PATCH {{API_URL}}/v1/cms/banner
```

Request

```
{
'type':1,

'img': [ 
    {
    "filename": "eb4fc89a3b443ae8ff7a622d14a3428b.png",
    "url": "http://wwww.nb.com.ar/algo"
      ''
    },
    {
    "filename": "eb4fc89a3b443ae8ff7a622d14a3428b.png",
    "url": "http://wwww.nb.com.ar/algo"
    }
]
}
```
