---
jira_key: "NBWEB-103"
summary: "API - Recursos tipo de falla para formulario de postventa"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-04-08 08:47"
updated: "2022-06-26 21:24"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-103"
---

# NBWEB-103: API - Recursos tipo de falla para formulario de postventa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-08 08:47 |
| Actualizado | 2022-06-26 21:24 |
| Etiquetas | ninguna |
| Jira | [NBWEB-103](https://bluinc.atlassian.net/browse/NBWEB-103) |

## Descripción

Se trata del recurso que muestra los tipos de falla y sus parámetros. Sirve para componer el formulario, entre otras cosas.

```
GET {{API_URL}}/v1/postventa/failTypes
```

Retorna:



```json
[
    {
        "description": "No enciende",
        "id": 1,
        "requiredImg" :false //corresponde a la obligatoriedad de poner la imagen
    },
        {
        "description": "Faño Fisico",
        "id": 2,
        "requiredImg" :true //corresponde a la obligatoriedad de poner la imagen
    }
]
```



Creación de tablas nuevas

```sql
USE [NB_WEB]
GO

/****** Object:  Table [dbo].[postventaFailTypes]    Script Date: 08/04/2022 08:50:47 a.m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[postventaFailTypes](
	[id] [int] NOT NULL,
	[description] [varchar](25) NOT NULL,
	[requiredImg] [bit] NOT NULL
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO

ALTER TABLE [dbo].[postventaFailTypes] ADD  CONSTRAINT [DF_postventaFailTypes_requiredImg]  DEFAULT ((0)) FOR [requiredImg]
GO


```



Se debe cargar la tabla con los casos iniciales según lo conversado

```
Daño Fisico
  |-Imagen obligatoria
No enciende
No da imagen
No detecta
```
