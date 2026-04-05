---
jira_key: "PED-126"
aliases: ["PED-126"]
summary: "API - Feat - Liquidar pedido 2 parte -> Autorizacion"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2023-10-06 09:07"
updated: "2023-10-19 16:47"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-126"
---

# PED-126: API - Feat - Liquidar pedido 2 parte -> Autorizacion

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2023-10-06 09:07 |
| Actualizado | 2023-10-19 16:47 |
| Etiquetas | ninguna |
| Jira | [PED-126](https://bluinc.atlassian.net/browse/PED-126) |

## Relaciones

- **Padre:** [[PED-123 - Feat - Liquidar pedido|PED-123]] Feat - Liquidar pedido

## Descripcion

Una parte importante de la liquidación es el estado final en el que queda el pedido. Existen 2 estados posibles, el estado “2 - autorizado” y el estado “1 - Pendiente de autorización” según la tabla `[NEW_BYTES].[dbo].[MS_STATUS_REMITO]`

El estado final, dependerá de la combinación de algunos parámetros y saldos. 

Según la tabla `[NEW_BYTES].[dbo].[MS_FORMASPAGO_REMITOS_VENDEDORES]` diremos entonces que 

- **Condición Principal**:
Para cualquier caso donde `[NEW_BYTES].[dbo].[MS_FORMASPAGO_REMITOS_VENDEDORES].SALIDA_AUTORIZADA = SI`

```
if ($this->id_forma == 2 || $this->id_forma == 4) {
    $this->set_id_status(1);
}else...
```



Si el valor de `id_forma` es 2 o 4` 2- Efectivo Motomami `o `4 - Efectivo Camioneta ` se establece el `id_status` a `1 - Pendientes a Autorizar`


- **Segunda Condición**:

```
if ($this->id_forma == 16) {
    $this->set_id_status(2);
}

```

Si el valor de `id_forma` es `16 - Pago diferido` , se establece el `id_status` a 2.


- **Tercera Condición**:

```
if ($this->id_forma == 6) {
    $amount = $this->getCChequeAmount();
    if ($amount < $this->totalremito) {
        exit('No se puede liquidar con CHEQUE, el monto es mayor al saldo disponible para CHEQUE. ' . $amount . '<' . $this->totalremito);
    } else {
        $this->set_id_status(1);
    }
}

```

Si el valor de `id_forma` es 6 (que parece representar un cheque), entonces:

- Se obtiene el monto disponible del cheque con `getCChequeAmount()`.


- Si este monto es menor que `totalremito`, se detiene la ejecución y muestra un mensaje indicando que el monto del cheque no es suficiente.


- Si el monto es suficiente, se establece el `id_status` a 1.





**¿como calculamos getCChequeAmount?**

**1 - obtenemos el saldo de cheque**

```
SELECT (
        CLI_SALDOCHEQUE - isNULL((
                SELECT sum(TOTALREMITO * COTIZACION)
                FROM NEW_BYTES.DBO.MS_REMITO_CABECERA
                LEFT JOIN NEW_BYTES.dbo.MS_VENTAS_REMITOS
                    ON MS_VENTAS_REMITOS.REMITO_FP = MS_REMITO_CABECERA.REMITO_FP
                        AND MS_REMITO_CABECERA.SUCURSAL_REMITO = MS_VENTAS_REMITOS.SUCURSAL_REMITO
                WHERE ID_FORMA = 6
                    AND ID_STATUS = 1
                    AND ID_CLIENTE = MS_CTACTE_CLIENTES.ID_CLIENTE
                ), 0) - (
            (
                SELECT ISNULL(SUM(IMPORTE), 0) AS TOTAL
                FROM [NEW_BYTES].[dbo].[MS_CHEQUES_RECIBIDOS_ENLACE]
                INNER JOIN [NEW_BYTES].[dbo].[MS_CHEQUES_ESTADOACTUAL]
                    ON [MS_CHEQUES_RECIBIDOS_ENLACE].ID_CHEQUE = [MS_CHEQUES_ESTADOACTUAL].ID_CHEQUE
                WHERE (
                        [MS_CHEQUES_ESTADOACTUAL].ID_ESTADO = 1
                        OR [MS_CHEQUES_ESTADOACTUAL].ID_ESTADO = 2
                        OR [MS_CHEQUES_ESTADOACTUAL].ID_ESTADO = 3
                        OR [MS_CHEQUES_ESTADOACTUAL].ID_ESTADO = 6
                        OR [MS_CHEQUES_ESTADOACTUAL].ID_ESTADO = 7
                        )
                    AND [MS_CHEQUES_RECIBIDOS_ENLACE].ID_CLIENTE = MS_CTACTE_CLIENTES.ID_CLIENTE
                )
            )
        ) AS CLI_SALDO_CHEQUE_T
FROM NEW_BYTES.dbo.MS_CTACTE_CLIENTES
WHERE ID_CLIENTE = ?

```

**2 - Con ese valor, lo pasaremos a pesos y ese es mi saldo.**

```php
return $obj_prod2[0]->CLI_SALDO_CHEQUE_T != 0 ? 
       (float) ($obj_prod2[0]->CLI_SALDO_CHEQUE_T / $this->cotizacion) : 
       (float) 0;

```

- **Condición por Defecto para **id_forma:

```

if ($this->id_forma == 1) {
    $amount = $this->getCCAmount();
    $this->set_id_status($amount < $this->totalremito ? 1 : 2);
}
```

Si ninguna de las condiciones anteriores se cumple:

- Y si `id_forma` es 1:

- Se obtiene un monto con `getCCAmount()`.


- Si este monto es menor que `totalremito`, se establece el `id_status` a 1.


- Si no, se establece el `id_status` a 2.



**¿como calculamos getCCAmount?**

```
  SELECT
    sum(CASE [MC_CCORRIENTES_MOVIMIENTOS].TR_CODIGO
    WHEN 4 THEN
    CC_IMPORTEUSD*-1
    WHEN 24 THEN
    CC_IMPORTEUSD*-1
    WHEN 125 THEN
    CC_IMPORTEUSD*-1
    WHEN 14 THEN
    CC_IMPORTEUSD*-1
    WHEN 34 THEN
    CC_IMPORTEUSD*-1
    WHEN 32 THEN
    CC_IMPORTEUSD*-1
    WHEN 41 THEN
    CC_IMPORTEUSD*-1
    ELSE CC_IMPORTEUSD
    END ) AS TOTAL
    FROM [NEW_BYTES].[dbo].[MC_CCORRIENTES_MOVIMIENTOS]
    INNER JOIN [NEW_BYTES].[dbo].GL_TRANSACCIONES
    ON MC_CCORRIENTES_MOVIMIENTOS.TR_CODIGO = GL_TRANSACCIONES.TR_CODIGO
    INNER JOIN NewBytes_DBF.dbo.clientes
    ON MC_CCORRIENTES_MOVIMIENTOS.ID_CLIENTE = clientes.ID_CLIENTE
    WHERE CC_ANULADO = 'NO'
    AND MC_CCORRIENTES_MOVIMIENTOS.ID_CLIENTE = ?
    GROUP BY  [MC_CCORRIENTES_MOVIMIENTOS].ID_CLIENTE, clientes.cnomcli
    ORDER BY  TOTAL ASC
```





**Resumen**: El código verifica diferentes formas de pago (`id_forma`) y, según la forma de pago y ciertas condiciones (como montos disponibles), establece un estado (`id_status`). Las formas de pago parecen ser números (2, 4, 16, 6, 1) y los estados son 1 o 2.

## ¿Que debemos retornar?

Retornaremos un `succes:true` u un statusDescription: Para el estado final definido, según la descripción de la tabla `[NEW_BYTES].[dbo].[MS_STATUS_REMITO]`
