---
jira_key: "NBWEB-113"
summary: "API - CMS - Subir Banner"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-04-12 07:56"
updated: "2022-08-01 12:36"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-113"
---

# NBWEB-113: API - CMS - Subir Banner

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
| Jira | [NBWEB-113](https://bluinc.atlassian.net/browse/NBWEB-113) |

## Descripción

Se debe utilizar el recurso para subir imágenes al servidor y a su vez poder ordenarlas

```
POST {{API_URL}}/v1/cms/banner

Request
{
  image: ''
}
```

Return

```json
{
  success: 'ok',
  image: 'bd470a4653ccf91cb73a09790b14f0f4.jpeg';
}
```



Creación de tablas

```
USE [NB_WEB]
GO

/****** Object:  Table [dbo].[banners]    Script Date: 12/04/2022 08:29:16 a.m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[banners](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[type] [int] NOT NULL,
	[image] [varchar](50) NOT NULL,
	[position] [int] NOT NULL,
	[link] [varchar](250) NULL
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO


```
