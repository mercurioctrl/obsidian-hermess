---
jira_key: "INV-252"
aliases: ["INV-252"]
summary: "API - MVP - Sync up - Modificacion de costos por sellIn sellOut ( Se encarga de ajustar los costosy guardar los valores anteriores segun el criterio de fecha o cantidad de corte)"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Marbe Moreno"
created: "2025-10-17 11:24"
updated: "2025-12-05 02:35"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/INV-252"
---

# INV-252: API - MVP - Sync up - Modificacion de costos por sellIn sellOut ( Se encarga de ajustar los costosy guardar los valores anteriores segun el criterio de fecha o cantidad de corte)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Marbe Moreno |
| Creado | 2025-10-17 11:24 |
| Actualizado | 2025-12-05 02:35 |
| Etiquetas | ninguna |
| Jira | [INV-252](https://bluinc.atlassian.net/browse/INV-252) |

## Relaciones

- **Padre:** [[INV-250]] Repositorio de Sell In Sell Out
- **relates to:** [[INV-273]] API - MVP Refactor - Syncup  Sell In/ Sell Out -> Agregar almacén al historial

## Descripcion

Crear un recurso de sincronización que recorra las acciones de descuento registradas en
`[NewBytes_DBF].[dbo].[articulo].sellDiscount` y se encargue de:

- Iniciar acciones vigentes que todavía no hayan aplicado el descuento sobre el costo.


- Reaplicar el descuento cuando una acción fue despausada y sigue vigente.


- Expirar acciones que hayan alcanzado el máximo de unidades vendidas (`maxStockQty`) o cuya fecha de finalización (`endDate`) haya pasado.


- Restaurar siempre el costo original (`ncosteprom`) cuando una acción finaliza o está pausada.



En todos los casos debe preservarse el costo original y registrarse cada cambio de costo en
`[NB_WEB].[dbo].[historial_costos]`.

### Nuevo recurso

**Endpoint propuesto**

```
POST {API_URL}/sellDiscount/syncUp

```

Sin body (se ejecuta la sincronización global de todas las acciones vigentes / pausadas según reglas).

**Respuesta (ejemplo)**

```
{
  "success": true,
  "startedActions": 3,
  "expiredActions": 2,
  "reactivatedActions": 1
}

```

- `startedActions`: cantidad de acciones que comenzaron a aplicar su descuento en esta ejecución.


- `expiredActions`: cantidad de acciones que terminaron (por fecha o por stock vendido).


- `reactivatedActions`: cantidad de acciones que volvieron a aplicar el descuento luego de estar pausadas (si corresponde).



---

### Alcance y comportamiento del syncUp

El recurso deberá recorrer los registros de `[NewBytes_DBF].[dbo].[articulo].sellDiscount` y, para cada acción, aplicar la siguiente lógica:

#### 1. Datos de referencia

Cada acción de la tabla `sellDiscount` se asume al menos con estos campos (ya definidos en historias anteriores):

- `itemId`


- `stockWarehouseId`


- `originalCost` (costo original del artículo, snapshot de `[NewBytes_DBF].[dbo].[articulo].ncosteprom`)


- `percentageDiscount` **o** `amountDiscount` (solo uno activo por acción)


- `startDate`


- `endDate` (opcional)


- `maxStockQty` (opcional)


- `paused` (boolean)


- Cualquier otro flag que indique estado (ej: `started`, `expired`, etc., si ya existe o se define en esta historia).



El costo actual del producto se toma de:
`[NewBytes_DBF].[dbo].[articulo].ncosteprom`

#### 2. Cálculo de unidades vendidas

Para cada acción con `maxStockQty`, el syncUp debe calcular cuántas unidades se vendieron desde `startDate` hasta el momento actual, usando una consulta equivalente a:

```
SELECT SUM(albclil.ncanent) AS VENTAS
FROM NewBytes_DBF.dbo.albclil
LEFT OUTER JOIN NewBytes_DBF.dbo.albclit
    ON albclil.ID_NROREMCLI_ENC = albclit.ID_NROREMCLI_ENC
WHERE albclil.ID_Articulo = @itemId
  AND albclit.ntipoalb > 1
  AND {between_startDate_y_fecha_actual}

```

> La implementación exacta del filtro `{between}` se ajustará según las reglas de fechas de la acción (`startDate`, `endDate`).


#### 3. Condiciones para **expirar** una acción

Una acción debe expirar cuando:

- La cantidad de ventas acumuladas (`VENTAS`) desde `startDate` es **mayor o igual** a `maxStockQty` (si `maxStockQty` está definido), **o**


- La fecha actual es **posterior** a `endDate` (si `endDate` está definido).



En ese caso, el syncUp debe:

- Restaurar `[NewBytes_DBF].[dbo].[articulo].ncosteprom` al valor `originalCost` guardado en `sellDiscount`.


- Marcar la acción como expirada (campo de estado correspondiente en `sellDiscount`).


- Registrar el cambio de costo en `[NB_WEB].[dbo].[historial_costos]`.



Además, si la acción está **pausada** y por definición de negocio una acción pausada no debe impactar el costo, el syncUp también debe verificar que el costo actual sea el `originalCost` y, de no ser así, restaurarlo y registrar el cambio en `historial_costos`.

#### 4. Condiciones para **iniciar** una acción

Una acción se considera **no iniciada** cuando está dentro de su ventana de vigencia (fechas y stock) y aún no se aplicó el descuento sobre `ncosteprom` (por ejemplo, `originalCost` vacío/null o flag `started = false`).

Si:

- Fecha actual >= `startDate`


- (No hay `endDate` o fecha actual <= `endDate`)


- (No hay `maxStockQty` o `VENTAS` < `maxStockQty`)


- `paused = false`


- El costo actual aún no refleja el descuento



Entonces el syncUp debe:

- Guardar, si todavía no está guardado, el costo original de `[NewBytes_DBF].[dbo].[articulo].ncosteprom` en `sellDiscount.originalCost`.


- Calcular el nuevo costo aplicando el descuento:

- Si hay `percentageDiscount`: `newCost = originalCost * (1 - percentageDiscount / 100)`


- Si hay `amountDiscount`: `newCost = originalCost - amountDiscount`




- Actualizar `[NewBytes_DBF].[dbo].[articulo].ncosteprom` con ese nuevo costo.


- Marcar la acción como iniciada (flag de estado).


- Registrar el cambio en `[NB_WEB].[dbo].[historial_costos]` (incluyendo costo anterior, costo nuevo, itemId, stockWarehouseId, referencia a la acción de `sellDiscount`, motivo “sellDiscountSyncUp”, etc.).



#### 5. Condiciones para **reanudar** una acción despausada

Si una acción estaba marcada como `paused = true` y en algún momento pasa a `paused = false`, el syncUp debe:

- Verificar que la acción siga vigente por fecha y stock (mismas reglas que en el punto anterior).


- Verificar que el costo actual (`ncosteprom`) **ya refleje** el descuento.

- Si **no** lo refleja, repetir la lógica de inicio:

- Asegurarse de tener `originalCost` correcto.


- Aplicar el descuento y actualizar `ncosteprom`.


- Registrar el cambio en `historial_costos`.







Esto evita que una acción despausada quede “vigente” conceptualmente pero sin impacto en el costo.

#### 6. Acciones pausadas

Para acciones con `paused = true`, el comportamiento esperado es:

- No deben tener el costo con descuento activo.


- El syncUp debe asegurar que:

- `ncosteprom` sea igual a `originalCost`.


- Si encuentra un costo descontado mientras la acción está pausada, debe restaurar el costo original y registrar el cambio en `historial_costos`.





---

### Reglas de integridad y seguridad

- **No aplicar dos veces el mismo descuento**

- Antes de modificar `ncosteprom`, el syncUp debe determinar si el costo actual ya refleja la acción de descuento en curso (por ejemplo, comparando contra el cálculo esperado según `originalCost` + descuento).


- Si el costo ya coincide con el valor descontado, no debe volver a aplicar el descuento ni repetir el registro en `historial_costos`.




- **Preservar siempre el **`originalCost`

- Antes de cualquier modificación de `ncosteprom`, se debe asegurar que `originalCost` esté correctamente cargado en `sellDiscount`.


- El `originalCost` es la única fuente de verdad para restaurar el costo original cuando la acción termina, se pausa o expira.




- **Acciones no superpuestas**

- El sistema **no debe permitir** tener dos acciones de `sellDiscount` que se solapen en el tiempo para el mismo `itemId` + `stockWarehouseId` (se asume que esa validación se hace al crear/editar la acción, pero esta historia debe mencionarlo como requisito de integridad).


- El syncUp debe trabajar bajo el supuesto de una sola acción vigente/activa por item y depósito, evitando casos donde múltiples acciones intenten modificar el mismo `ncosteprom` al mismo tiempo.




- **Registro en **`historial_costos`** obligatorio**

- Cada vez que se modifica el valor de `[NewBytes_DBF].[dbo].[articulo].ncosteprom`, se debe insertar un registro en `[NB_WEB].[dbo].[historial_costos]` con:

- `itemId`


- `stockWarehouseId`


- costo anterior


- costo nuevo


- fecha y hora


- origen de la operación (por ejemplo: `sellDiscountSyncUp`)


- identificador de la acción en `sellDiscount`
