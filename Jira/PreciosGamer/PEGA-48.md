---
jira_key: "PEGA-48"
summary: "API - Feat - Listar banners"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-01-03 09:51"
updated: "2023-01-09 13:49"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-48"
---

# PEGA-48: API - Feat - Listar banners

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-01-03 09:51 |
| Actualizado | 2023-01-09 13:49 |
| Etiquetas | ninguna |
| Jira | [PEGA-48](https://bluinc.atlassian.net/browse/PEGA-48) |

## Descripción

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

Se creara la tabla `PEGA.[dbo].[banners]`

```
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[banners](
    [id] [int] IDENTITY(1,1) NOT NULL,
    [type] [int] NULL,
    [image] [varchar](50) NOT NULL,
    [position] [int] NOT NULL,
    [link] [varchar](250) NULL
) ON [PRIMARY]
GO

```
