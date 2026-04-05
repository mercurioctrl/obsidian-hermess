---
jira_key: "NBWEB-210"
summary: "Crear Tablas para MercadoPago"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Emanuel Jesus Ferreyra"
created: "2022-05-27 18:43"
updated: "2022-06-26 21:09"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-210"
---

# NBWEB-210: Crear Tablas para MercadoPago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2022-05-27 18:43 |
| Actualizado | 2022-06-26 21:09 |
| Etiquetas | ninguna |
| Jira | [NBWEB-210](https://bluinc.atlassian.net/browse/NBWEB-210) |

## Descripción

`response_mercadopago`

```
USE [NEW_BYTES]
GO

/****** Object:  Table [dbo].[response_mercadopago]    Script Date: 5/27/2022 6:40:12 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[response_mercadopago](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[data_id] [int] NOT NULL,
	[client_id] [int] NOT NULL,
	[branch] [int] NOT NULL,
	[order_id] [int] NOT NULL,
	[status] [varchar](50) NULL,
	[status_detail] [varchar](50) NULL,
	[date_approved] [varchar](50) NULL,
	[payment_method_id] [varchar](50) NULL,
	[payment_type_id] [varchar](50) NULL,
	[error_message] [varchar](50) NULL,
	[created_at] [datetime] NOT NULL,
 CONSTRAINT [PK_response_mercadopago] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[response_mercadopago] ADD  DEFAULT (getdate()) FOR [created_at]
GO

```





`notification_mercadopago`

```
USE [NEW_BYTES]
GO

/****** Object:  Table [dbo].[notification_mercadopago]    Script Date: 6/2/2022 9:41:32 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[notification_mercadopago](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[id_webhook] [bigint] NOT NULL,
	[live_mode] [varchar](10) NOT NULL,
	[type] [varchar](25) NOT NULL,
	[date_created] [varchar](25) NOT NULL,
	[user_id_mercadopago] [int] NOT NULL,
	[api_version] [varchar](20) NOT NULL,
	[action] [varchar](25) NOT NULL,
	[data_id] [int] NOT NULL,
	[created_at] [datetime] NOT NULL,
 CONSTRAINT [PK_notification_mercadopago] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[notification_mercadopago] ADD  CONSTRAINT [DF_notification_mercadopago_created_at]  DEFAULT (getdate()) FOR [created_at]
GO


```
