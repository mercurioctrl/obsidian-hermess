---
jira_key: "LIO-219"
aliases: ["LIO-219"]
summary: "API - Feat - Crear un ticket vinculado a el ítem de un una orden"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-02-12 14:02"
updated: "2025-02-20 16:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-219"
---

# LIO-219: API - Feat - Crear un ticket vinculado a el ítem de un una orden

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-02-12 14:02 |
| Actualizado | 2025-02-20 16:26 |
| Etiquetas | ninguna |
| Jira | [LIO-219](https://bluinc.atlassian.net/browse/LIO-219) |

## Relaciones

- **Padre:** [[LIO-21]] Migrar sistema de tickets para usar el de capa 1 (NB)
- **has action item:** [[LIO-226]] APP - Refactor - Conectar sistema de envio de ticket a v4

## Descripcion

Crearemos un recurso que nos permita crear un ticket para un pedido especifico (Si ya existe un ticket abierto para el pedido se nos debe informar que no puede abrirse uno nuevo hasta cerrar el anterior)

```
POST {APIv4_URL}/v4/ticket/680312
```

**Carga Util:**

```
{
"idLo":680312, (ex idPedido)
"idItemLo":0, (ex idPedidoDetalle)
"idType":2, (ex idTipo)
"idIssue":20, (ex idMotivo)
"description":"esto es una prueba"
}
```

**Retorna:**

```
{
    "id": 85695,
    "open": true,
    "description":"esto es una prueba",
    "startDate": "2025-02-12 14:26:36.360",
    "endDate": "",
    "type": {
        "id": 2,
        "description": "Tengo un problema"
    },
    "issue": {
        "id": 8,
        "description": "Con el vendedor"
    },
    "thread": [] <-- aca mas adelante vendra el hilo de comentarios si existe
}
```

## ¿Donde se guarda?

Crearemos una tabla `[NewBytes_DBF].[dbo].[pedclitTicket]` relacionándolo a la orden creada

```
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[pedclitTicket](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[idTicketType] [int] NULL,
	[idTicketIssue] [int] NULL,
	[open] [tinyint] NOT NULL,
	[description] [varchar](250) NULL,
	[startDate] [datetime] NULL,
	[endDate] [datetime] NULL,
	[description] [text] NULL,
	[idLo] [int] NULL,
	[cnumped] [varchar](8) NULL,
	[cnumsuc] [varchar](4) NULL,
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[pedclitTicket] ADD  CONSTRAINT [DF_ticketOpen]  DEFAULT ((0)) FOR [open]
GO

```
