---
jira_key: "NBWEB-104"
summary: "API - Pre ingreso de postventa"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-04-08 09:05"
updated: "2022-06-26 21:42"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-104"
---

# NBWEB-104: API - Pre ingreso de postventa

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-04-08 09:05 |
| Actualizado | 2022-06-26 21:42 |
| Etiquetas | ninguna |
| Jira | [NBWEB-104](https://bluinc.atlassian.net/browse/NBWEB-104) |

## Descripción

Se trata del recurso que hace posible el pre ingreso de nuevos casos de postventa, con sus detalles

```
POST {{API_URL}}/v1/postventa
```

**Request:**

```json
{
  contactNumber: '+54 9 11 30958675' 
  detail: [
    {
    productId: 2345,
    serialNumber: '423423fds3243fsd',
    failTypeId: 3,
    quantity :2,
    failDescription: 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.',
    invoiceNumber: 'A00030048948',
    img: [ {
        "id": "257659",
        "filename": "eb4fc89a3b443ae8ff7a622d14a3428b.png",
        "url": "http://static.nb.com.ar/img/eb4fc89a3b443ae8ff7a622d14a3428b.png"
    },
    {
        "id": "257671",
        "filename": "eb81cc64c07459ee95474a9f4a4a4a0c.png",
        "url": "http://static.nb.com.ar/img/eb81cc64c07459ee95474a9f4a4a4a0c.png"
    }
    ,
    secondarySerial : [
        {
          serialNumber: 'WE4791013661',
          serialDetail: {
            clientId: '016050',
            saleDate: '2015-12-24 09:16:27.090',
            warranty: 1,
            elapsedMonths: '77',
            referSale: '0002-00296114',
            productId: '1945',
            productDescription: 'TECLADO_GENIUS_06B',
            purchasePrice: '5.71012800000',
            currentWarranty: false,
            buyer: false,
          },
        },
]]
    }

  ]
}
```



Se utilizan las tablas `postsaleInbound` y `postsaleInboundDetail`



**Creación de tablas**

```sql
USE [NB_WEB]
GO

/****** Object:  Table [dbo].[postsaleInbound]    Script Date: 08/04/2022 09:13:07 a.m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[postsaleInbound](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[clientId] [int] NOT NULL,
	[userId] [int] NOT NULL,
	[date] [datetime] NOT NULL,
	[contactNumber] [varchar](25) NULL
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO


```





```sql
USE [NB_WEB]
GO

/****** Object:  Table [dbo].[postsaleInboundDetail]    Script Date: 08/04/2022 09:13:49 a.m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[postsaleInboundDetail](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[productId] [int] NOT NULL,
	[serialNumber] [int] NULL,
	[failType] [int] NOT NULL,
	[quantity] [int] NOT NULL,
	[failDescription] [text] NOT NULL,
	[invoiceNumber] [varchar](23) NULL,
	[productDescription] [varchar](150) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO


```
