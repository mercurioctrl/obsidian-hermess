---
jira_key: "NBWEB-464"
summary: "DB - Create - Agregar Tabla Nueva trackingNumber"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Emanuel Jesus Ferreyra"
created: "2022-08-18 14:37"
updated: "2022-11-25 10:22"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-464"
---

# NBWEB-464: DB - Create - Agregar Tabla Nueva trackingNumber

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2022-08-18 14:37 |
| Actualizado | 2022-11-25 10:22 |
| Etiquetas | ninguna |
| Jira | [NBWEB-464](https://bluinc.atlassian.net/browse/NBWEB-464) |

## Descripción

```
USE [NewBytes_DBF]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].trackingNumber(
	[id] int IDENTITY(1,1) NOT NULL,
	[branch] int NOT NULL,
	[numOrder] int NOT NULL,
    [tracking] [varchar](100) NULL,
	[packageGrouper] [varchar](100) NULL,
    [medioEnvioId] int NOT NULL,
	[created_at] [datetime] NOT NULL DEFAULT (getdate())
) ON [PRIMARY]
GO
```
