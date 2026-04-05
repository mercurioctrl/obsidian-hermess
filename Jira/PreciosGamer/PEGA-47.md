---
jira_key: "PEGA-47"
summary: "API - Feat - Listar zonas de banner"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-01-03 09:44"
updated: "2023-01-09 13:51"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PEGA-47"
---

# PEGA-47: API - Feat - Listar zonas de banner

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-01-03 09:44 |
| Actualizado | 2023-01-09 13:51 |
| Etiquetas | ninguna |
| Jira | [PEGA-47](https://bluinc.atlassian.net/browse/PEGA-47) |

## Descripción

```
GET {{API_URL}}/v1/cms/banners/zones
```

Retorna

```
[
  {
    "id": 3,
    "descroption": "Banner central"
  },
  {
    "id": 3,
    "descroption": "Banner central"
  },
  {
    "id": 3,
    "descroption": "Banner central"
  }
]
```

Se debe crear una tabla para almacenar la información del tipo `PEGA.dbo.bannersZones`

```
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[bannersZones](
    [id] [int] IDENTITY(1,1) NOT NULL,
    [description] [varchar](50) NULL
) ON [PRIMARY]
GO

```
