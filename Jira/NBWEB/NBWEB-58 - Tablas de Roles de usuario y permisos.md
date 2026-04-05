---
jira_key: "NBWEB-58"
aliases: ["NBWEB-58"]
summary: "Tablas de Roles de usuario y permisos"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Catriel Mercurio"
created: "2022-03-29 11:30"
updated: "2022-06-26 20:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-58"
---

# NBWEB-58: Tablas de Roles de usuario y permisos

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Catriel Mercurio |
| Creado | 2022-03-29 11:30 |
| Actualizado | 2022-06-26 20:11 |
| Etiquetas | ninguna |
| Jira | [NBWEB-58](https://bluinc.atlassian.net/browse/NBWEB-58) |

## Relaciones

- **Padre:** [[NBWEB-2]] API - Mi cuenta

## Descripcion

Se agregan las tablas para el sistema de roles y permisos

```sql
USE [NB_WEB]
GO

/****** Object:  Table [dbo].[userRoles]    Script Date: 29/03/2022 11:47:53 a.m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[userRoles](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[description] [varchar](50) NOT NULL
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO


```



```sql
USE [NB_WEB]
GO

/****** Object:  Table [dbo].[userPermissions]    Script Date: 29/03/2022 11:48:22 a.m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[userPermissions](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[roleId] [int] NOT NULL,
	[list] [bit] NOT NULL,
	[remove] [bit] NOT NULL,
	[make] [bit] NOT NULL
) ON [PRIMARY]

GO


```
