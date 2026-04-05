---
jira_key: "NBWEB-247"
aliases: ["NBWEB-247"]
summary: "Crear Tabla para Registrar Clientes MercadoPago"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Catriel Mercurio"
reporter: "Emanuel Jesus Ferreyra"
created: "2022-06-09 10:26"
updated: "2022-06-26 21:32"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-247"
---

# NBWEB-247: Crear Tabla para Registrar Clientes MercadoPago

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Catriel Mercurio |
| Reportado por | Emanuel Jesus Ferreyra |
| Creado | 2022-06-09 10:26 |
| Actualizado | 2022-06-26 21:32 |
| Etiquetas | ninguna |
| Jira | [NBWEB-247](https://bluinc.atlassian.net/browse/NBWEB-247) |

## Relaciones

- **blocks:** [[NBWEB-223]] API - Vincular el cliente en mercado pago con el interno al procesar un pago de mp

## Descripcion

Se requiere la Creacion de la Tabla client_mercadopago.

```
USE [NEW_BYTES]
GO

/****** Object:  Table [dbo].[client_mercadopago]    Script Date: 6/8/2022 11:49:15 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[client_mercadopago](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[mp_id] [varchar](50) NULL,
	[mp_email] [varchar](50) NULL,
	[client_id] [int] NULL,
	[created_at] [datetime] NULL DEFAULT (getdate())
) ON [PRIMARY]
GO
```
