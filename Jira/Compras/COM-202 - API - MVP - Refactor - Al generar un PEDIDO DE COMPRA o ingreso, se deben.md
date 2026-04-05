---
jira_key: "COM-202"
aliases: ["COM-202"]
summary: "API - MVP - Refactor - Al generar un PEDIDO DE COMPRA o ingreso, se deben enviar las cosas al deposito corresponiente warehousesId (ID_ALMACEN)"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2025-09-30 11:49"
updated: "2025-11-10 10:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/COM-202"
---

# COM-202: API - MVP - Refactor - Al generar un PEDIDO DE COMPRA o ingreso, se deben enviar las cosas al deposito corresponiente warehousesId (ID_ALMACEN)

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2025-09-30 11:49 |
| Actualizado | 2025-11-10 10:15 |
| Etiquetas | ninguna |
| Jira | [COM-202](https://bluinc.atlassian.net/browse/COM-202) |

## Relaciones

- **Padre:** [[COM-109 - Generar INGRESO o pedido (a partir de una orden de compra)|COM-109]] Generar INGRESO o pedido (a partir de una orden de compra)

## Descripcion

Según el requerimiento y lo que venimos trabajando, a partir de la existencia de los nuevos depósitos de stock, debemos decirle al ingresar stock en una orden, debemos marcar cual sera su almacén de destino de manera obligatoria.

Para esto refactorizaremos el recurso 

```
POST {API_URL}/v1/makeProviderOrderInbound
```

**Cambios funcionales:**

- El parámetro `warehousesId` deberá ser **obligatorio**.


- El valor de `warehousesId` determinará en qué depósito se registrará el stock dentro de la tabla `[NewBytes_DBF].[dbo].[stocks]`, específicamente en el campo `ID_ALMACEN`.


- Si no existe una fila para la combinación `(itemId, warehousesId)` en `[NewBytes_DBF].[dbo].[stocks]`, se deberá **crear un nuevo registro** antes de realizar la suma de stock.


- Toda operación de ingreso de stock deberá generar su correspondiente registro en `[NB_WEB].[dbo].[registro_stock]`.



### Consideraciones técnicas

**Consulta de referencia (sistema anterior):**

```
SELECT TOP (1000) *
  FROM [NB_WEB].[dbo].[registro_stock]
  where fichero = 'generarRemitoTipo-pro.php'
  order by id desc
```

#### **Estructura conceptual esperada en **`registro_stock`**:**

| Campo | Descripción |
| --- | --- |
| `warehouseId` | Depósito de destino (almacén donde ingresa el stock) |
| `itemId` | Identificador del artículo |
| `cantidad` | Cantidad ingresada (valor positivo, por ejemplo `10`) |
| `sAnterior` | Stock en el depósito antes del movimiento |
| `sPosterior` | Stock en el depósito después del movimiento |
| `agente` | Usuario o proceso que ejecuta el movimiento |

**Snapshot adicional al momento del cambio:**

- `nstock_lo`


- `nstock`


- `nstock_en_cola`


- `nstock_d1`


- `nstock_reserva_pedidos`


- `nstock_lo_reserva_pedidos`


- `nstock_postventa`
