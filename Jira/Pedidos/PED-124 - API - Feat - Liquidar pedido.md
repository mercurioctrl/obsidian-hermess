---
jira_key: "PED-124"
aliases: ["PED-124"]
summary: "API - Feat - Liquidar pedido"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-10-06 08:11"
updated: "2025-12-19 15:16"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-124"
---

# PED-124: API - Feat - Liquidar pedido

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-06 08:11 |
| Actualizado | 2025-12-19 15:16 |
| Etiquetas | ninguna |
| Jira | [PED-124](https://bluinc.atlassian.net/browse/PED-124) |

## Relaciones

- **Padre:** [[PED-123]] Feat - Liquidar pedido
- **blocks:** [[PED-125]] APP - Feat - Modal de liquidacion
- **relates to:** [[SNB-3569]] PED - API - Liquidar pedido - Error al liquidar y duplicación de la orden

## Descripcion

Leela tranqui y en u ratito la charlamos si queres

```
POST {API_URL}/v1/closeSale
```

**Payload**

```
deliveyMethod
paymentMethod
comment
order
branch
comment
```

1 - Verificar cupo disponible para el vendedor

Según lo que estuvimos trabajando, existe un limite que le permite a un vendedor, seguir o no liquidando (o cerrando pedidos). Para poder verificarlo tendremos los montos para cada vendedor, separados en 2 sucursales (`0010` y  `0002`).

Para eso en principio haremos algo como esto, que nos permite obtener los datos necesarios:

```
SELECT agentes.nominalDailyLimit{sucursal} - (
        SUM(ncanent * npreunit - ncanent * npreunit * albclil.ndto / 100) + (
            SELECT SUM(ncanent * npreunit - ncanent * npreunit * albclil.ndto / 100)
            FROM NewBytes_DBF.DBO.albclil
            WHERE ID_NROREMCLI_ENC = {pedido}
            )
        ) AS limite
    , (
        SELECT SUM(ncanent * npreunit - ncanent * npreunit * albclil.ndto / 100)
        FROM NewBytes_DBF.DBO.albclil
        WHERE ID_NROREMCLI_ENC = {pedido}
        ) esteRemito
    , (agentes.nominalDailyLimit{sucursal} - (SUM(ncanent * npreunit - ncanent * npreunit * albclil.ndto / 100))) AS limiteReal
FROM [NewBytes_DBF].[dbo].[albclit]
LEFT JOIN NewBytes_DBF.DBO.albclil
    ON albclil.ID_NROREMCLI_ENC = albclit.ID_NROREMCLI_ENC
LEFT JOIN NEW_BYTES.dbo.MS_REMITO_CABECERA A
    ON A.REMITO_FP = albclit.cnumalb
        AND albclil.cnumsuc = A.SUCURSAL_REMITO
LEFT JOIN NewBytes_DBF.dbo.agentes
    ON agentes.ID_VENDEDOR = {vendedor}
WHERE (ID_VENDEDOR_LIQ = {vendedor})
    AND CONVERT(DATE, FECHA_LIQUIDACION, 112) = CONVERT(DATE, GETDATE(), 112)
    AND albclit.cnumsuc = '".$sucursalString."'
GROUP BY agentes.nominalDailyLimit{sucursal}

```

Una vez que obtenemos ese dato, podemos decir que

```
if ($limiteDisponible->limite <= 0)
    
    //mostramos un mensaje como este y terminamos la ejecucion
   "Ya no dispones de cupo para el dia de hoy. Tu cupo disponible es: usd  " . ($limiteDisponible->limiteReal) . "";


```

De otra forma avanzamos normalmente



**2 - Creamos la cabecera de la compra:**

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

**3 -  creamos el detalle, para la cabecera de la compra:**

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

**4 - creamos el anexo para la cabecera que identifica parámetros de pago y envío:**

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

[LA INFO DE ESTA TABLA PROVIENE DE NUESTRA REQUEST]

**5 - Creamos el enlace con el pago para que sae comptabile con todos los sistemas**

```
        INSERT INTO [NEW_BYTES].[dbo].MC_ENLACE_REMITOS_FORMASPAGO (
            [SUCURSAL_REMITO]
            ,[REMITO_FP]
            ,[ID_FORMAPAGO]
            ,[EVFP_IMPORTE]
        ) VALUES (?, ?, ?, ?);
```

**6 - Registramos ganancias y otros detalles, para cada item**

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

**7- Registramos ganancias y otras informaciones como ya lo hicimos en la liquidacion de efectivo**

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

**8 - Se imputa el cobro en la CC del cliente de modo tal que pueda tener su inverso posteriormente (El cobro)**

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

**9 - Se crean registros sobre el pago **

```
    INSERT INTO [NEW_BYTES].[dbo].MC_ENLACE_CCMOVIMIENTOS_FORMASPAGO (
         [ID_CCMOVIMIENTO]
        ,[ID_FORMAPAGO]
        ,[EMFP_IMPORTE]
        ,[EMFP_COTIZACION]
        ,[EMFP_CHEQUES]) VALUES (  ?, ?, ?, ?, ?)
```
