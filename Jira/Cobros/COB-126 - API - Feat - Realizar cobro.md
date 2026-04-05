---
jira_key: "COB-126"
aliases: ["COB-126"]
summary: "API - Feat - Realizar cobro"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-09-28 22:09"
updated: "2022-11-29 11:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COB-126"
---

# COB-126: API - Feat - Realizar cobro

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-09-28 22:09 |
| Actualizado | 2022-11-29 11:47 |
| Etiquetas | ninguna |
| Jira | [COB-126](https://bluinc.atlassian.net/browse/COB-126) |

## Relaciones

- **Padre:** [[COB-115 - Feat - Realizar un cobro|COB-115]] Feat - Realizar un cobro
- **is blocked by:** [[COB-125 - APP - Feat - Modal de cobro|COB-125]] APP - Feat - Modal de cobro
- **is blocked by:** [[COB-127 - API - Feat - Crear recibo|COB-127]] API - Feat - Crear recibo
- **blocks:** [[COB-243 - API - Refactor - Realizar cobro de múltiples medios de pago|COB-243]] API - Refactor - Realizar cobro de múltiples medios de pago

## Descripcion

Acá se pueden tomar dos posibles recursos

```
POST {API_URL}/v1/box/{boxId}
```

```
POST {API_URL}/v1/trade
```

En el primer caso se hace referencia al objeto **box** en referencia a [link](https://lioteam.atlassian.net/browse/COB-3) 

En el segundo se especifica un acción especifica en la ruta. Usa el enfoque que crees que mas te sirve.

El recurso recibe una carga útil basada en la informacion que nos provee un formulario de este tipo:

[adjunto]
Payload:

```
[{
"clientId":4543, 
"pedido": 'X000234234324', //opcional
"finalAmount": 1214,
"comment":"Algun comentario opcional"
  "payments":[
 {
   "paymentMethodsId": 1,
   "amountPaid": "300",
 },
 {
  "paymentMethodsId": 2,
   "amountPaid": "5000",
 },
 {
  "paymentMethodsId": 3,
   "amountPaid": "150",
 },
 {
 "paymentMethodsId": 4,
   "amountPaid": "50000",
 }
]
}]
```

`payments` Es la informacion necesaria para construir la tabla de pagos del otro lado. El resto de los datos que se ven en la tabla, los obtendremos del otro lado.



Si no existe `pedido` voy a decir que **Monto a pagar** = `finalAmount`

Si existe `pedido`, obtenemos todos los totales directamente de  la tabla `MS_REMITO_CABECERA`

Luego sumo todos los valores del objeto `payments` y si el total en dolares de los mismos NO es mayor o igual al **Monto a pagar** entonces termino el proceso. aviso que no se puede continuar.

Usamos la logica que vimos en la daily, de como funciona la tabla del modal. Multiplicando los saldos.

Las cotizaciones pueden sacarse de la columna cotización en `[NEW_BYTES].[dbo].[MS_COTIZACIONES]`

Con esa informacion información ya podes iterar `payments` para convertir todo a dolares y ver si lo que cobraste es mayor o igual a Monto a pagar.

Si puedo continuar

**Imputa el saldo en la cuenta del cliente**, usando una sola fila sobre la tabla `MC_CCORRIENTES_MOVIMIENTOS` ver [link](https://lioteam.atlassian.net/browse/COB-5)

**Imputa los valores recibidos en la caja que realizo el cobro **Usando una linea para cada `paymentMethodsId` utilizado en la transacción `MC_LOG_OPERACIONES` usando uno de los siguientes códigos según corresponda 

```
SELECT *
FROM [NEW_BYTES].[dbo].[GL_TRANSACCIONES]
where TR_CODIGO IN (16,12,28,42,44,126,51,53)
```

Recordar que debes dejar las referencias entre los movimientos tal cual se especifica en [link](https://lioteam.atlassian.net/browse/COB-3)

```sql
... FROM [NEW_BYTES].[dbo].MC_LOG_OPERACIONES LOG
LEFT JOIN NEW_BYTES.dbo.MC_CCORRIENTES_MOVIMIENTOS MCV
ON MCV.ID_CCMOVIMIENTO = ID_REFERENCIA
LEFT JOIN NEW_BYTES.dbo.MS_REMITO_CABECERA AS REMITO
ON REMITO.REMITO_FP = LOG.LOG_REMITO_FP AND REMITO.SUCURSAL_REMITO = LOG.LOG_SUCURSAL_REMITO
LEFT JOIN NEW_BYTES.dbo.MS_REMITO_CABECERA AS REMITO
ON REMITO.REMITO_FP = LOG.LOG_REMITO_FP AND REMITO.SUCURSAL_REMITO = LOG.LOG_SUCURSAL_REMITO...
```

Ya casi terminamos

Finalmente solo si `pedido` en el payload lo uso tambien para marcar el pedido como cobrado

Lo marco en la tabla `[NEW_BYTES].[dbo].[MS_VENTAS_REMITOS]` como `ID_STATUS = 2` en referencia a los estados que podemos ver en

```
SELECT * FROM [NEW_BYTES].[dbo].[MS_STATUS_REMITO]
```

y agrego el [link](https://lioteam.atlassian.net/browse/COB-127)



Miralo y lo charlamos
