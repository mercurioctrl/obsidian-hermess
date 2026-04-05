---
jira_key: "PED-725"
aliases: ["PED-725"]
summary: "API - Feat - Recurso para obtener la informacion completa tal como se genero en el market place (LO)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-05-24 12:58"
updated: "2024-05-30 18:28"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-725"
---

# PED-725: API - Feat - Recurso para obtener la informacion completa tal como se genero en el market place (LO)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-05-24 12:58 |
| Actualizado | 2024-05-30 18:28 |
| Etiquetas | ninguna |
| Jira | [PED-725](https://bluinc.atlassian.net/browse/PED-725) |

## Relaciones

- **Padre:** [[PED-724 - Modal Venta Market Place LO|PED-724]] Modal "Venta Market Place LO"
- **relates to:** [[PED-621 - API - Obtener información de como se genero una orden en Marketplace (LO) -|PED-621]] API - Obtener información de como se genero una orden en Marketplace (LO) - Sugerencias de mejora en el objeto
- **relates to:** [[PED-732 - API - Obtener información de como se genero una orden en Marketplace (LO) -|PED-732]] API - Obtener información de como se genero una orden en Marketplace (LO) - Agregar resellerPhone

## Descripcion

Crearemos un recurso para poder ver la informacion completa de como se genero una venta en su marketplace de origen, en este caso libre opción, mas allá de como impacto en las ordenes de nb.

```
GET {API_URL}/v1/aboutMarketPlace/branch-order
```

```
[
  {
    "document": "40603664",
    "idLo": 644928,
    "creationDate": "20/05/2024",
    "currencyQuote": 903.0,
    "idResellerOrderId": 638077,
    "resellerName": "BitBayres",
    "resellerPhone": "6828-4000",
    "order": "10350855",
    "cnumalb": "00580698",
    "branch": "0002",
    "deliveryInfoLo": "{\"Nombre del que recibe\":\"Nahuel Santiago Beltran Navarro\",\"Direcci\\u00f3n\":\"Barrio Juramento, Calle 20 de Junio 169,  ,  CP: 4200, SANTIAGO DEL ESTERO           , SANTIAGO DEL ESTERO\",\"C\\u00f3digo Postal\":\"4200\"}",
    "clientNameLo": "Nahuel Santiago Beltran Navarro",
    "mailClientLo": "nsbn97@gmail.com",
    "clientPhoneLo": "3854757240",
    "deliveryNameLo": "Entregar                                          ",
    "paymentNameLo": "Transferencia                                     ",
    "placeIdLo": 18166,
    "provinceIdLo": 18,
    "deliveryDescriptionLo": "A domicilio por Entregar",
    "specialDiscountLo": 0.0,
    "costoEnvio": 0.0,
    "intterestRate": 0.0,
    "items":[
  {
    "idDistributir": 1,
    "detailIdLo": 661027,
    "productoIDLo": 712531,
    "orderResellerID": 638077,
    "priceLo": 328590,
    "discountLo": 0.0,
    "clientCostLo": 32931.0,
    "utilityLo": 0.0,
    "iva": 1050.0,
    "amountLo": 1,
    "descriptionLo": "PROCESADOR AMD (AM4) RYZEN 7 5700X3D S/COOLER",
    "itemId": 118838,
    "refundLo": 0
  },
  {
    "idDistributir": 1,
    "detailIdLo": 661027,
    "productoIDLo": 712531,
    "orderResellerID": 638077,
    "priceLo": 328590,
    "discountLo": 0.0,
    "clientCostLo": 32931.0,
    "utilityLo": 0.0,
    "iva": 1050.0,
    "amountLo": 1,
    "descriptionLo": "PROCESADOR AMD (AM4) RYZEN 7 5700X3D S/COOLER",
    "itemId": 118838,
    "refundLo": 0
  }
]
  }
]
```

Consulta orientadora:

```
SELECT
    TOP(1)
    usuarios.documento as document,
    [pedidosCabecera].id as idLo,
    CONVERT(VARCHAR, [pedidosCabecera].fechaCreacion, 103) AS creationDate,
    [cotizacion] as currencyQuote,
    pedidosCabeceraVendedor.ID AS idResellerOrderId,
    vendedores.nombre AS resellerName,
    vendedores.telefono AS resellerPhone,
    pedclit.cnumped AS 'order',
    albclit.cnumalb AS 'cnumalb',
    albclit.cnumsuc AS branch,
    [pedidosCabeceraVendedor].[medioDeEnvioDatos] as deliveryInfoLo,
    [usuarios].nombre as clientNameLo,
    [usuarios].[correo] as mailClientLo,
    [usuarios].[telefono] as clientPhoneLo,
    [mediosEnvio].nombre as deliveryNameLo,
    [mediosPago].nombre as paymentNameLo,
    usuarios.ciudadID as placeIdLo
    , usuarios.provinciaID as provinceIdLo,
    mediosEnvio.descripcion as deliveryDescriptionLo,
    ( SELECT SUM(pedidosDetalle.descuentoLO)
    FROM [LO].[dbo].[pedidosDetalle]
        INNER JOIN [LO].[dbo].pedidosCabeceraVendedor ON pedidosCabeceraVendedor.ID = [pedidosDetalle].pedidoCabeceraResellerID
        LEFT JOIN LO.dbo.pedidosCabecera F ON F.id = pedidosCabeceraVendedor.pedidoCabeceraID
    WHERE F.id =pedidosCabecera.id AND pedidosDetalle.devuelto <> 1 ) AS specialDiscountLo
 
    ,(SELECT SUM(medioenviocosto)
    FROM LO.dbo.pedidosCabeceraPaquete
    WHERE pedidoCabeceraID = pedidosCabecera.id) as costoEnvio,
    (     SELECT
        SUM((cantidad*(precio - (precio*[pedidosDetalle].descuento/100)) * medioDePagoInteres / 100))
    FROM
        [LO].[dbo].[pedidosDetalle]
        INNER JOIN
        [LO].[dbo].pedidosCabeceraVendedor ON pedidosCabeceraVendedor.ID = [pedidosDetalle].pedidoCabeceraResellerID
        LEFT JOIN LO.dbo.pedidosCabecera F ON F.id = pedidosCabeceraVendedor.pedidoCabeceraID
    WHERE F.id =pedidosCabecera.id AND pedidosDetalle.devuelto <> 1) AS intterestRate
FROM [LO].[dbo].pedidosCabeceraVendedor
    INNER JOIN
    [LO].[dbo].[pedidosCabecera] ON pedidosCabecera.id = pedidosCabeceraVendedor.pedidoCabeceraID
    LEFT JOIN
    NewBytes_DBF.dbo.pedclit ON pedidosCabeceraVendedor.pedclitID = pedclit.cnumped
    --LEFT JOIN LO.dbo.pedidosCabeceraPaquete ON pedidosCabecera.id = pedidosCabeceraPaquete.pedidoCabeceraID
    LEFT JOIN [LO].[dbo].[vendedores] ON vendedores.id = [pedidosCabeceraVendedor].vendedorID
    LEFT JOIN [LO].[dbo].[usuarios] ON usuarios.id = [pedidosCabecera].[usuarioID]
    LEFT JOIN [LO].[dbo].[mediosEnvio] ON mediosEnvio.id = [pedidosCabeceraVendedor].[medioDeEnvioID]
    LEFT JOIN [LO].[dbo].[mediosPago] ON mediosPago.id = [pedidosCabeceraVendedor].[medioDePagoID]
    LEFT JOIN NewBytes_DBF.dbo.albclit ON albclit.cnumped = pedclit.cnumped
    LEFT JOIN NewBytes_DBF.dbo.agentes ON agentes.ccodage = pedclit.ccodage
WHERE pedidosCabecera.id = ?
```

Consulta orientadora para los items:

```

SELECT 
articulo.id_distribuidora as idDistributir, 
[pedidosDetalle].[id] as detailIdLo, 
[pedidosDetalle].[productoID] as productoIDLo, 
[pedidosDetalle].[pedidoCabeceraResellerID] as orderResellerID , 
[pedidosDetalle].[precio] as priceLo, 
[pedidosDetalle].[descuento] as discountLo, 
[pedidosDetalle].[costo_cliente] as clientCostLo, 
[pedidosDetalle].[utilidad] as utilityLo, 
[pedidosDetalle].[iva] as iva, 
[pedidosDetalle].[cantidad] as amountLo, 
productos.titulo as descriptionLo, 
productos.id_interno as itemId
,pedidosDetalle.devuelto as refundLo
FROM [LO].[dbo].[pedidosDetalle]
INNER JOIN CS.DBO.productos ON [pedidosDetalle].productoID = productos.id
LEFT JOIN LO.dbo.pedidosCabeceraPaquete ON pedidosCabeceraPaquete.id = pedidosDetalle.pedidoCabeceraPaqueteID
LEFT JOIN NewBytes_DBF.dbo.articulo ON productos.id_interno = articulo.ID_ARTICULO
WHERE pedidosCabeceraPaquete.pedidoCabeceraID = ?
```
