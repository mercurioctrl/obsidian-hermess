---
jira_key: "PED-90"
aliases: ["PED-90"]
summary: "API - Feat- Generar pedido (albclit) desde una orden de compra (pedclit)"
status: "Finalizada"
type: "Historia"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-09-26 13:26"
updated: "2025-12-16 10:27"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-90"
---

# PED-90: API - Feat- Generar pedido (albclit) desde una orden de compra (pedclit)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Historia |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-09-26 13:26 |
| Actualizado | 2025-12-16 10:27 |
| Etiquetas | ninguna |
| Jira | [PED-90](https://bluinc.atlassian.net/browse/PED-90) |

## Relaciones

- **Padre:** [[PED-4 - Pedidos|PED-4]] Pedidos
- **Subtarea:** [[PED-113 - API - Review - No permite generar pedido|PED-113]] API - Review - No permite generar pedido
- **Subtarea:** [[PED-129 - API - Refactor - Generar pedido para Libre Opción|PED-129]] API - Refactor - Generar pedido para Libre Opción 
- **Subtarea:** [[PED-158 - API - Review - Problemas al generar un pedido (albclit)|PED-158]] API - Review - Problemas al generar un pedido (albclit)
- **blocks:** [[PED-91 - APP - Feat - Generar pedido|PED-91]] APP - Feat - Generar pedido
- **has action item:** [[PED-1151 - API - MVP - Implementar almacenes al generar pedido (albclit) desde una orden|PED-1151]] API - MVP - Implementar almacenes al generar pedido (albclit) desde una orden de compra (pedclit)
- **relates to:** [[PED-1178 - API - Refactor - Generar pedido - Evitar creación y duplicación de pedidos ante|PED-1178]] API - Refactor - Generar pedido -> Evitar creación y duplicación de pedidos ante errores en el proceso

## Descripcion

```
POST {API_URL}/v1/makeSale
```

```
{
order:10329359
branch:0002
}
```

Al momento de generar un pedido se hacen varios pasos. La finalidad de esto es realizar las acciones de manera 

- Verificar estado del pedido y Verificar pedidos pendientes


- Generar cabecera


- Generar detalle (Control de stock, log de stock, guardado de detalle)


- Traer comentarios


- Actualizar Stocks





### Verificar estado del pedido

Lo principal es que el estado aun este en `cestado = 'P'`

Adicionalmente se hace una verificación sobre los pedidos de ese ‘vendedor’ para saber si tiene alguno ‘pendiente’ (`cestado = 'P'`) mas viejo de X días. De ser así, lanzamos una excepción que explique esta situación.

La cantidad de días se configura por vendedor y esta en `[NewBytes_DBF].[dbo].agentes.xRemitoVto`

Ejemplo para obtener pedidos viejos

```sql
SELECT count(cnumped) as cantidad
FROM [NewBytes_DBF].[dbo].[pedclit]
LEFT JOIN NewBytes_DBF.DBO.agentes ON agentes.ccodage = pedclit.ccodage
WHERE DATEDIFF(DAY,dfecped, getdate()) > agentes.xRemitoVto 
AND (cobserv = 'INTERNO' OR  cobserv = 'DESCARGADO') 
AND cestado ='P' AND pedclit.ccodage = ?
```

Si ambas condiciones se cumplen, entonces pasmos al siguiente paso.

### Generar cabecera

Lo primero es tomar una cabecera, para ya aparcar un numero de ‘albclit’ que vamos a utilizar en el proceso. Cualquier fallo o excepción antes de completar el proceso de ‘generar pedido’ elimina esta cabecera si es que ya se creo.

Usaremos una ‘query’ similar a esta, para lo cual debemos tener de antemano los datos.

```sql
INSERT INTO [NewBytes_DBF].[dbo].[albclit]
(
CNUMALB
,DFECALB
,CCODCLI
,CCODALM
,CCODAGE
,CNUMPED
,CNUMSUC
,ID_VENDEDOR
,ID_ALMACEN
,ID_CLIENTE
,ID_ESTADOREMITOCLI
,ID_NROREMCLI_ENC
,ID_Sucursal
,ID_FORMADEPAGO
,ID_MONEDA
,NTIPOALB
,lfacturado
) VALUES
(
REPLACE(STR((SELECT MAX(CNUMALB)+1 FROM [NewBytes_DBF].[dbo].albclit WHERE cnumsuc = '" . $cabecera->cnumsuc . "'), 8), SPACE(1), '0')
,GETDATE()
,'" . $cabecera->ccodcli . "'
,'SAF'
,'" . $cabecera->ccodage . "'
,'" . $cabecera->cnumped . "'
,'" . $cabecera->cnumsuc . "'
," . $cabecera->ccodage . "
,2
," . $cabecera->ccodcli . "
,1
,'X" . $cabecera->cnumsuc . "'+REPLACE(STR((SELECT MAX(CNUMALB)+1 FROM [NewBytes_DBF].[dbo].albclit WHERE cnumsuc = '" . $cabecera->cnumsuc . "'), 8), SPACE(1), '0')
," . $id_sucursal . "
,0
,1
,1
,0
)
```

### Generar Detalle

Este paso a su vez, consta de varios pasos que detallaremos mas abajo **y que se ejecutan al iterar item por item**

1 - Obtener stock y validar que alcance. Por definición el stock que sale de `[NewBytes_DBF].[dbo].stock`.nstock entra en `[NewBytes_DBF].[dbo].[albclil].ncantent` y se debe impedir cualquier discordancia en este punto.

¿Como se hace la comparación? 

`[NewBytes_DBF].[dbo].[pedclil].ncanped <= [NewBytes_DBF].[dbo].stock.nstock`

Es decir, que comparamos que el `ncanped` que traemos del pedido, sea menor o igual al stock disponible. Si es así podemos proceder con algo como lo siguiente **PERO SIN EJECUTARLA, SINO QUE LA ACUMULAREMOS**

**Query acumulativa de stock**

```sql
UPDATE [NewBytes_DBF].[dbo].stocks SET nstock = nstock - {cantidad} 
WHERE id_Articulo = {itemId}
```

**Query acumulativa para el historial**

```sql
INSERT INTO [NB_WEB].[dbo].[registro_stock] (
                fecha,
                codigo,
                cref,
                cantidad,
                remito,
                agente,
                exito,
                fichero,
                sAnterior,
                query
            ) VALUES (
                GETDATE(),
                {itemId}
                {cerf}
                {cantidad operdada mas signo} <- ej: -3
               'R-' . {branch} . '-' . {cnumalb} . ',
                {agentId},
                1,
                'pedidos.nb',
                (
                SELECT
                    (nstock + nstock_lo + nstock_en_cola)
                FROM
                    [NewBytes_DBF].[dbo].[stocks]
                WHERE
                (cref =  {itemId})
                ),
               {esto se usa para guardar informacion adicional}
            );
```

**Query acumulativa de marcar stock posterior**

```sql
UPDATE
[NB_WEB].[dbo].[registro_stock]
SET sPosterior = (
SELECT
    (nstock + nstock_lo + nstock_en_cola)
FROM
    [NewBytes_DBF].[dbo].[stocks]
WHERE
    (ID_ARTICULO = {itemId})
)
WHERE
id =
(
SELECT TOP(1) id
FROM [NB_WEB].[dbo].[registro_stock]
WHERE
codigo = {itemId} <- ojo el formato
AND cref =  {itemId} <- ojo el formato
AND remito = 'R-' . {branch} . '-' . {cnumalb} . ',
AND agente = {agentId}
AND fichero = pedidos.nb
AND cantidad =    {cantidad operdada mas signo} <- ej: -3
ORDER BY fecha DESC
);
```

**Query acumulativa de detalle de pedido**

```sql
INSERT INTO [NewBytes_DBF].[dbo].[albclil]
(
                CNUMALB,
                CREF,
                CDETALLE,
                NPREUNIT,
                NDTO,
                NIVA,
                NCANENT,
                CNUMSUC,
                ID_ARTICULO,
                ID_NROREMCLI_ENC,
                Id_Sucursal
            ) VALUES
            (
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?
            )
```

En cada iterecion de cada producto, acumularemos estas 4 query, y al mismo tiempo haremos la pregunta

`[NewBytes_DBF].[dbo].[pedclil].ncanped <= [NewBytes_DBF].[dbo].stock.nstock` ?

Si en cualquiera de las veces que itero para construir estas query, la respuesta es NO, es decir no tengo stock

entonces elimino mi cabecera y termino el proceso indicando de que producto no tengo stock.

```
DELETE FROM [NewBytes_DBF].[dbo].albclit WHERE CNUMALB = ? AND  CNUMSUC = ?
```

Si fue `true` para todos los casos entonces ejecuto mis querys acumuladas para los siguientes casos

- **Query acumulativa para el historial**


- **Query acumulativa de detalle de pedido**


- **Query acumulativa de stock**


- **Query acumulativa de marcar stock posterior**



Si todos los pasos anteriores son correctos entonces

```
UPDATE [NewBytes_DBF].[dbo].[pedclit] SET cestado = 's'
WHERE cnumped = ?
```



[Se que es muy largo y seguro te genera dudas, así que avísame y lo vemos]
