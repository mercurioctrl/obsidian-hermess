---
jira_key: "COB-330"
aliases: ["COB-330"]
summary: "API - Refactor - Autoliquidar si el medio de pago es efectivo y retiro"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-02-17 10:08"
updated: "2024-02-13 04:28"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-330"
---

# COB-330: API - Refactor - Autoliquidar si el medio de pago es efectivo y retiro

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-02-17 10:08 |
| Actualizado | 2024-02-13 04:28 |
| Etiquetas | ninguna |
| Jira | [COB-330](https://bluinc.atlassian.net/browse/COB-330) |

## Relaciones

- **Padre:** [[COB-329 - Refactor - Auto liquidar si el medio de pago es efectivo y retiro|COB-329]] Refactor - Auto liquidar si el medio de pago es efectivo y retiro

## Descripcion

En los casos donde el cliente paga y retira en el momento, no se necesita nada especial al momento del cobro. Por esto podemos generar toda la informacion de liquidación de manera automatica para poder realizar la operación sin mas intervención del vendedor.

Para realizar esto, son necesarios varios pasos. En cada paso se realizara una inserción en la base de datos, a partir de la cual se genera la compra efectiva del producto.

**Primero paso, creamos la cabecera de la compra:**

```
INSERT INTO [NEW_BYTES].[dbo].MS_REMITO_CABECERA (
         [SUCURSAL_REMITO]
        ,[REMITO_FP]
        ,[ANULADO]
        ,[ID_CLIENTE]
        ,[CLI_NOMBRE]
        ,[PESO]
        ,[TOTALSINIVA]
        ,[DESCUENTOS]
        ,[IVA1]
        ,[TOTALIVA1]
        ,[IVA2]
        ,[TOTALIVA2]
        ,[TOTALREMITO]
        ,[SALIDA_AUTORIZADA]
        ,[COTIZACION]
        ,[USU_IDENTIFICACION]
        ,[VENDEDOR]
        ,[OBSERVACIONES_FP]
        ,[USUARIO_FP]
        ,[ID_PROCEDENCIA]
        ,[ID_DIRCLI]
        ,[IMPPERCEP]
        ,[FECHA_REMITO]
        ,[FECHA_LIQUIDACION]
        ,[FE_HO_MODIFICACION]
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
```

Para obtener los datos necesarios haremos la siguiente consulta

```sql
SELECT
        albclit.cnumsuc as SUCURSAL_REMITO,
        albclit.cnumalb as REMITO_FP,
        albclit.ntipoalb as ntipoalb,
        clientes.ID_CLIENTE,
        clientes.cnomcli as CLI_NOMBRE,
        albclit.dfecalb as FECHA_REMITO,
        agentes.capeage as VENDEDOR,
        albclit.ccodage_creador as USUARIO_FP,
        albclil.niva as IVA,
        SUM( ((albclil.npreunit*albclil.ndto/100)) *ncanent) AS DESCUENTO,
        SUM( ((albclil.npreunit*albclil.ndto/100)+((albclil.npreunit*albclil.ndto/100)*albclil.niva/100)) *ncanent) AS DESCUENTO_IVA,
        SUM( (albclil.npreunit - (albclil.npreunit*albclil.ndto/100)) *ncanent) AS TOTAL_SINIVA,
        SUM( ((albclil.npreunit - (albclil.npreunit*albclil.ndto/100)) *ncanent)*albclil.niva /100) AS TOTAL_IVA,
        CASE
        WHEN albclit.cnumsuc = '0010' OR excluirPercepcion = 1
        THEN 0
        ELSE (SUM((ncanent*npreunit-ncanent*npreunit*albclil.ndto/100)*clientes.percepcion)/100)
        END AS percepcionmonto,
        CASE
        WHEN albclit.cnumsuc = '0010' OR excluirPercepcion = 1
        THEN
        (SUM((ncanent*npreunit-ncanent*npreunit*albclil.ndto/100)+(ncanent*npreunit-ncanent*npreunit*albclil.ndto/100)*albclil.niva/100))
        ELSE
        (SUM((ncanent*npreunit-ncanent*npreunit*albclil.ndto/100)+(ncanent*npreunit-ncanent*npreunit*albclil.ndto/100)*albclil.niva/100)+ISNULL((SUM((ncanent*npreunit-ncanent*npreunit*albclil.ndto/100)*clientes.percepcion)/100), 0 ))
        END AS totalFinal,
        SUM(ncanent*npreunit-ncanent*npreunit*albclil.ndto/100) AS totalSinIva,
        MS_COTIZACIONES.COTIZACION,
        clientes.percepcion as PERCEPCION,
        clientes.CODEMP,
        (SELECT  TASAANUAL FROM NEW_BYTES.dbo.PV_PARAMETROS_VARIOS) AS TASAANUAL,
        VARIACOTIZA,
        ST_Autorizaciones.Estado,
        excluirPercepcion
        FROM [NewBytes_DBF].[dbo].[albclit]
        INNER JOIN NewBytes_DBF.dbo.clientes ON clientes.ID_CLIENTE = albclit.ID_CLIENTE
        INNER JOIN NewBytes_DBF.dbo.agentes ON clientes.ID_VENDEDOR = agentes.ID_VENDEDOR
        INNER JOIN NewBytes_DBF.dbo.albclil ON albclit.cnumalb = albclil.cnumalb AND albclit.cnumsuc = albclil.cnumsuc
        INNER JOIN NEW_BYTES.dbo.MS_COTIZACIONES ON MS_COTIZACIONES.NOMBRE = 'PESOS'
        LEFT JOIN NEW_BYTES.dbo.PV_PARAMETROS_VARIOS ON VARIACOTIZA IS NOT NULL
        LEFT JOIN [NEW_BYTES].[dbo].[ST_Autorizaciones] ON 'X'+albclit.cnumalb = ST_Autorizaciones.Remito AND estado =2
        WHERE albclit.ID_NROREMCLI_ENC = ?
        GROUP BY
        albclil.niva,
        albclit.cnumsuc,
        albclit.cnumalb,
        albclit.ntipoalb,
        clientes.ID_CLIENTE,
        clientes.cnomcli,
        albclit.dfecalb,
        agentes.capeage,
        albclit.ccodage_creador,
        MS_COTIZACIONES.COTIZACION,
        clientes.percepcion,
        clientes.CODEMP,
        VARIACOTIZA,
        ST_Autorizaciones.Estado,
        excluirPercepcion
```

**Segundo paso, creamos el detalle, para la cabecera de la compra:**

```
INSERT INTO [NEW_BYTES].[dbo].MS_REMITO_DETALLE (
         [SUCURSAL_REMITO]
        ,[REMITO_FP]
        ,[ID_ARTICULO]
        ,[ART_DESCRIPCION]
        ,[ART_CANTIDAD]
        ,[ART_PRECIOSINIVA]
        ,[ART_DESCUENTO]
        ,[ART_IVA]
        ,[ART_PRECIOFINAL]
        ,[ART_ORDEN]
        ,[FINALIZADO]
       ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
```

Podemos obtener los datos haciendo algo como esto

```sql
SELECT
  albclil.cnumsuc AS SUCURSAL_REMITO,
  albclil.cnumalb AS REMITO_FP,
  albclil.cref AS ID_ARTICULO,
  albclil.cdetalle AS ART_DESCRIPCION,
  albclil.ncanent AS ART_CANTIDAD,
  albclil.npreunit AS ART_PRECIOSINIVA,
  albclil.ndto AS ART_DESCUENTO,
  albclil.niva AS ART_IVA,
  ((npreunit-npreunit*ndto/100) + ((npreunit-npreunit*ndto/100) * niva/100)) AS ART_PRECIOFINAL,
  (npreunit - (npreunit*ndto/100)) AS P_VENTA,
  (ncosteprom) AS COSTO
  FROM [NewBytes_DBF].[dbo].[albclil]
  INNER JOIN [NewBytes_DBF].[dbo].[albclit] ON albclil.cnumalb = albclit.cnumalb AND albclit.cnumsuc = albclil.cnumsuc
  INNER JOIN NewBytes_DBF.dbo.articulo ON articulo.cRef = albclil.cref
  WHERE albclit.ID_NROREMCLI_ENC = ? AND albclit.ntipoalb < 3
```

**Tercer paso, creamos el anexo para la cabecera que identifica parámetros de pago y envío:**

```
       INSERT INTO [NEW_BYTES].[dbo].MS_VENTAS_REMITOS (
         [SUCURSAL_REMITO]
        ,[REMITO_FP]
        ,[OBSERVACIONES_VENTAS]
        ,[TRANSPORTE_FP]
        ,[ID_FORMA]
        ,[ID_STATUS]
        ,[ID_CAJA_CUENTA]
        ,[ANULADO]
        ,[ORIGENLIQ]
        ,[GASTOS_BANCARIOS]
        ,[GASTOS_TRANSPORTE]
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?);
```

La informacion para componer esta tabla proviene de las tablas donde están los estados, las formas de pago, etc. Y ya los conocemos porque siempre van a ser EFECTIVO CAJA y RETIRO.

**Cuarto paso, creamos el anexo para la identificar el pago en sistemas viejos:**

```
        INSERT INTO [NEW_BYTES].[dbo].MC_ENLACE_REMITOS_FORMASPAGO (
            [SUCURSAL_REMITO]
            ,[REMITO_FP]
            ,[ID_FORMAPAGO]
            ,[EVFP_IMPORTE]
        ) VALUES (?, ?, ?, ?);
```

**Quinto paso, creamos registros sobre la ganancia del producto:**

```
        INSERT INTO [NEW_BYTES].[dbo].MS_REMITO_DETALLE_GANANCIA_ENLACE (
         [SUCURSAL_REMITO]
        ,[REMITO_FP]
        ,[ID_ARTICULO]
        ,[ART_DESCRIPCION]
        ,[GANANCIA_ART]
        ,[PORC_GAN]
        ,[CANTIDAD]
        ,[COSTO]
        ,[P_VENTA]
        ,[TIPO_R_NOTA]) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
```

Rellenamos con los datos que ya tenemos y provienen del repositorio de detalles o del de la cabecera y calculamos la ganancia haciendo una operación como esta

iteramos el detalle del producto para obtener cada fila

```
PORC_GAN = (($producto->P_VENTA - $producto->COSTO) / $producto->COSTO) * 100;
```

**Sexto paso, creamos registros sobre la ganancia del pedido pero general:**

```
        INSERT INTO [NEW_BYTES].[dbo].MS_ENLACE_REMITOS_GANANCIAS (
         [SUCURSAL_REMITO]
        ,[REMITO_FP]
        ,[TIPO_R_NOTA]
        ,[FECHA]
        ,[FECHA_PROCESADO]
        ,[GANANCIA]
        ,[USU_IDENTIFICACION]
        ,[COTIZACION]
        ,[SUCURSAL_FACTURACION]
        ,[revisado]
        ,[FECHA_D]) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
```

iteramos el detalle del producto para obtener cada fila, pero esta vez sumamos todo para guardar la ganancia general

```
GANANCIA = $GANANCIA + (($producto->P_VENTA - $producto->COSTO) * $producto->ART_CANTIDAD);
```

**Séptimo paso, imputamos el pago negativo del pedido (esto ya lo conoces, pero siempre lo haces positivo al cobrar):**

```
        INSERT INTO [NEW_BYTES].[dbo].MC_CCORRIENTES_MOVIMIENTOS (
         [ID_CCMOVIMIENTO]
        ,[ID_CLIENTE]
        ,[TR_CODIGO]
        ,[CC_FECHAMOVIMIENTO]
        ,[USU_IDENTIFICACION]
        ,[REMITO_FP]
        ,[SUCURSAL_REMITO]
        ,[CC_IMPORTEUSD]
        ,[CC_ANULADO]
        ,[CC_OBSERVACIONES]
        ,[CC_HORAMOVIMIENTO]
        ,[COTIZACION]
        ,[IMPORTE_PERCEPCION]
        ,[PORC_PERCEPCION]
        ,[fechaMovimiento]) VALUES ( (SELECT MAX([ID_CCMOVIMIENTO] + 1)
    FROM [NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS]), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
```

**Octavo paso, creamos registros sobre el pago que son enlaces con los sistemas viejos:**

```
    INSERT INTO [NEW_BYTES].[dbo].MC_ENLACE_CCMOVIMIENTOS_FORMASPAGO (
         [ID_CCMOVIMIENTO]
        ,[ID_FORMAPAGO]
        ,[EMFP_IMPORTE]
        ,[EMFP_COTIZACION]
        ,[EMFP_CHEQUES]) VALUES (  ?, ?, ?, ?, ?)
```

Esto es muy simple, no creo que te falte nada pero cualquier cosa lo vemos.

**¿COMO SIGUE?**

Lo que sigue a continuación es cobrar normalmente como un cobro en efectivo donde el cajero esta recibiendo la plata, con toda esta base que creamos en nuestra liquidación automatica
