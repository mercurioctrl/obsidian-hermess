---
jira_key: "PED-855"
aliases: ["PED-855"]
summary: "API - Refactor - Agregar el internalTax a la liquidacion o cierre de venta"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2024-10-29 07:40"
updated: "2024-11-19 15:26"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-855"
---

# PED-855: API - Refactor - Agregar el internalTax a la liquidacion o cierre de venta

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2024-10-29 07:40 |
| Actualizado | 2024-11-19 15:26 |
| Etiquetas | ninguna |
| Jira | [PED-855](https://bluinc.atlassian.net/browse/PED-855) |

## Relaciones

- **Padre:** [[PED-4 - Pedidos|PED-4]] Pedidos

## Descripcion

Así como hicimos en el resto del circuito plasmaremos en el final de la venta los datos para poder mostrarlos con facilidad  en el cobro y en los comprobantes

```
POST {API_URL}/v1/{API_URL}/v1/closeSaleLimites
```

Para esto debemos tener varias consideraciones en este punto y podemos repasar la historia original de la liquidación en [link](https://lioteam.atlassian.net/issues/[[PED-124]]?jql=%28summary%20~%20%22liquidacion%2A%22%20OR%20description%20~%20%22liquidacion%2A%22%29%20AND%20project%20IN%20%2810050%29%20ORDER%20BY%20created%20DESC)  y repasaremos cada uno de los pasos de esa funciona

**1 - Verificar cupo disponible para el vendedor**

Debemos incluir dentro de la verificación, nuestro nuevo monto asegurándonos de que forme parte del monto final.

**2 - Creamos la cabecera de la compra:** 

Al insertar la cabecera de la compra en `[NEW_BYTES].[dbo].MS_REMITO_CABECERA` vemos que la tabla contempla los totales para toda la venta. Es necesario que se incluya el impuesto interno dentro del `TOTALREMITO` . Adicionalmente para manejar el mismo criterio que con otros impuestos (tal como se hace con `IMPPERCEP` e `TOTALIVA1` y `TOTALIVA2`) agregando la columna `[NEW_BYTES].[dbo].[MS_REMITO_CABECERA]`.`TOTALINTTAX` para albergar el monto nominal  que es la suma de todos los IMPUESTOS INTERNOS (internalTax) que tienen los items del pedido.

**3 - creamos el detalle, para la cabecera de la compra:**

Al insertar las filas de detalle de los items en `[NEW_BYTES].[dbo].MS_REMITO_DETALLE` agregaremos nuestros parametros para internalTax. Para esto incluiremos el monto dentro de `ART_PRECIOFINAL` como lo venimos haciendo y agregaremos una nueva columna para guardar el dato por separado `[NEW_BYTES].[dbo].MS_REMITO_DETALLE.ART_INTTAX` en terminos porcentuales como lo hacemos para los detalles.

**5 - Nos aseguramos que en el enlace de pago, el monto final contenga el impuesto interno**

Incluiremos el impuesto interno en el monto final que se guarda en `[NEW_BYTES].[dbo].[MC_ENLACE_REMITOS_FORMASPAGO].EVFP_IMPORTE`

**8 - Nos aseguramos que el monto final que incluye el impuesto interno se imputa el cobro en la CC del cliente de modo tal que pueda tener su inverso posteriormente (El cobro)**

Como en otros pasos, debe estar incluido en `[NEW_BYTES].[dbo].MC_CCORRIENTES_MOVIMIENTOS.CC_IMPORTEUSD` que es lo que se le guarda en la cuenta corriente al cliente y se le cobra (paga el impuesto interno ) Ademas, lo guardaremos en una columna `NEW_BYTES].[dbo].MC_CCORRIENTES_MOVIMIENTOS.PORC_INTTAX` (como se hace en `PORC_PERCEPCION`)

**9 - Ultimos paso: Se crean registros sobre el pago **

Nos aseguramos como en otros pasos, que el impuesto interno se incluya en el monto final `[NEW_BYTES].[dbo].MC_ENLACE_CCMOVIMIENTOS_FORMASPAGO.EMFP_IMPORTE`
