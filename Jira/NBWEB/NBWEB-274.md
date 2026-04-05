---
jira_key: "NBWEB-274"
summary: "Crear Tabla distance - para registro de metricas entre 2 puntos."
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Emanuel Jesus Ferreyra"
created: "2022-06-24 10:09"
updated: "2022-06-24 16:11"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-274"
---

# NBWEB-274: Crear Tabla distance - para registro de metricas entre 2 puntos.

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2022-06-24 10:09 |
| Actualizado | 2022-06-24 16:11 |
| Etiquetas | ninguna |
| Jira | [NBWEB-274](https://bluinc.atlassian.net/browse/NBWEB-274) |

## Descripción

Query para crear Tabla distance que se utilizara para registrar los distancia entre 2 puntos proporcionado por google maps.

```
USE [LO]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[distances](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[distanceKm] [int] NOT NULL,
	[cpHost] [int] NOT NULL,
	[cp] [int] NOT NULL,
	[duration] varchar(50) NOT NULL,
	[created_at] [datetime] NULL DEFAULT (getdate())
) ON [PRIMARY]
GO
```
