---
jira_key: "POS-97"
aliases: ["POS-97"]
summary: "API - Feat - Procesar pase de mercadería (Deposito)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2022-09-05 15:10"
updated: "2022-11-17 13:33"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/POS-97"
---

# POS-97: API - Feat - Procesar pase de mercadería (Deposito)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-05 15:10 |
| Actualizado | 2022-11-17 13:33 |
| Etiquetas | ninguna |
| Jira | [POS-97](https://bluinc.atlassian.net/browse/POS-97) |

## Relaciones

- **Padre:** [[POS-95 - API - Feat - Pedir un pase de mercaderia|POS-95]] API - Feat - Pedir un pase de mercaderia
- **blocks:** [[POS-98 - API - Feat - Aceptar pase de mercadería (Postventa)|POS-98]] API - Feat - Aceptar pase de mercadería (Postventa)
- **blocks:** [[POS-156 - APP - Feat - Aplicativo para responder pase desde el deposito|POS-156]] APP - Feat - Aplicativo para responder pase desde el deposito
- **blocks:** [[EXP-82 - API - Feat - Procesar pase|EXP-82]] API - Feat - Procesar pase 

## Descripcion

Esta historia trata sobre el momento donde expedición recibe la petición del pase y lo corresponde introduciendo el serial del producto


```
PATCH {{API_URL}}/v1/passes
```

```
{
       "statusId":1,
        "passId":11,
        "items": [
        {
            "productId": 100,
            "productDescription": "Placa de video",
            "serial": "sn8907433987"
        },
        {
            "productId": 100,
            "productDescription": "Placa de video",
            "serial": "sn8907433988"
        }
        ]
}
```

Para poder hacer el movimiento propiamente dicho, se debe hacer 3 pasos sobre el stock y uno sobre lo seriales.

**Sobre el stock**

- 1 - Verificar si el stock disponible es suficiente para hacer el movimiento


- 2 - Si es posible, registro el movimiento en el log de movimientos de stock


- 3 - Una vez que verifique la escritura en el log, lo descuento del stock y lo muevo de deposito



- Vamos a verificar el stock, para esto usamos la tabla `[NewBytes_DBF].[dbo].[stocks]` usando la formula `nstock - nstock_reserva_pedidos > cantidadDeseada`


- Usando la tabla `[NB_WEB].[dbo].[registro_stock]` registro el movimiento sumando la mayor cantidad posible de información al respecto del movimiento.


- Una vez que hice el movimiento descuento la cantidad de la columna `nstock` de la tabla `[NewBytes_DBF].[dbo].[stocks]` y lo agrego en la columna `nstock_postventa` (esta no existe, la vamos a crear)



**Sobre los seriales **

Los seriales implicados en la transacción deben marcarse correctamente en la tabla de seriales para que no puedan ser tomados en una venta ni otro tipo de acción.

Para esto utilizaremos la tabla `[NEW_BYTES].[dbo].[ST_DETALLE_STOCK]` .

Para ver como deben marcarse basta ver la siguiente query 

```
SELECT TOP (1000) [ID_STOCK]
      ,[ID_COMPRA]
      ,[CREF]
      ,[SERIAL]
      ,[FECHA_INGRESO]
      ,[FECHA_EGRESO]
      ,[ID_MOVIMIENTO]
      ,[PRECIO_COSTO]
      ,[PRECIO_FOB]
      ,[PRECIO_VENTA]
      ,[ID_VENTA]
      ,[GARANTIA_CLIENTE]
      ,[GARANTIA_PROVEEDOR]
      ,[ID_RMACLIENTE]
      ,[ID_RMAPROVEEDOR]
      ,[ID_DEPOSITO]
      ,[ID_STOCKVENTA]
      ,[GTOS_ADIC]
      ,[ID_PARTE]
      ,[ORIGENINGRESO]
      ,[auto]
  FROM [NEW_BYTES].[dbo].[ST_DETALLE_STOCK]
  where ID_RMACLIENTE is not null order by ID_RMACLIENTE desc
```

Como ultimo paso, en este punto se cambia el estado de en `[NB_WEB].[dbo].[passesHeader]` de la columna `statusId` a Aceptado
