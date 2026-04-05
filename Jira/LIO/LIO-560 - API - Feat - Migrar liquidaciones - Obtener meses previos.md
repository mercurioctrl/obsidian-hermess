---
jira_key: "LIO-560"
aliases: ["LIO-560"]
summary: "API - Feat - Migrar liquidaciones -> Obtener meses previos "
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2026-02-26 09:16"
updated: "2026-03-31 15:58"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-560"
---

# LIO-560: API - Feat - Migrar liquidaciones -> Obtener meses previos 

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-26 09:16 |
| Actualizado | 2026-03-31 15:58 |
| Etiquetas | ninguna |
| Jira | [LIO-560](https://bluinc.atlassian.net/browse/LIO-560) |

## Relaciones

- **Padre:** [[LIO-537 - Migración de repositorios previa deprecación de la api legacy|LIO-537]] Migración de repositorios previa deprecación de la api legacy
- **has action item:** [[LIO-594 - APP - Feat - Migrar liquidaciones - Obtener meses previos|LIO-594]] APP - Feat - Migrar liquidaciones -> Obtener meses previos 

## Descripcion

## Contexto

En la sección "Mis Cobros", debajo del resumen del mes actual, hay una línea de tiempo o listado que muestra **todos los meses pasados** en los que el vendedor tuvo actividad (o debería haberla tenido). Cada entrada indica cuántas ventas ocurrieron ese mes. El frontend usa este listado para renderizar el historial navegable de liquidaciones.

La API actual vive en `api.gamma.libreopcion.com`. Hay que migrar este recurso a la nueva API conservando exactamente el mismo contrato de respuesta.

[adjunto]
Se recomienda probar la funcionalidad con el vendedorID 447 y meses anteriores harcodeados, ya que en desarrollo es probable que meses recientes no tengan movimiento por ser un entorno tipo sandbox

---

## Recurso a migrar

| Campo | Valor |
| --- | --- |
| **Verbo** | `GET` |
| **Path** | `/liquidaciones/meses-previos` |
| **Autenticación** | Bearer JWT (token del vendedor en el header `Authorization`) |
| **Body / Payload** | Ninguno. Es un GET sin cuerpo. |
| **Query params** | Ninguno. |

---

## Cómo funciona conceptualmente

Este endpoint **no devuelve solo los meses con ventas**. Devuelve una lista continua y completa desde el primer mes en que el vendedor tuvo al menos una venta liquidada hasta el mes inmediatamente anterior al actual, sin saltos, rellenando los meses vacíos.

El proceso tiene tres etapas:

### 1. Consulta a la base de datos

Se buscan todos los pedidos de productos nativos **de meses anteriores al actual** que cumplan las condiciones de liquidación (ver filtros más abajo). Se agrupan por mes/año y se cuenta cuántos hay en cada uno.

Solo se consideran **productos nativos** (del catálogo propio de LibreOpción). Los filtros son:

- El pedido **no está cancelado** (ni por el usuario, ni por el vendedor, ni por LO, ni automáticamente).


- El pedido está marcado como **cobrado** (`cobrado = 1`).


- El estado del cliente externo (`pedclit.cestado`) es **distinto de **`'P'`.


- La fecha de creación del pedido es de un **mes distinto al actual** (`DATEPART(mm, ...) <> DATEPART(mm, GETDATE())`).



### 2. Relleno de meses sin ventas

Una vez obtenidos los meses con ventas, el sistema calcula el rango completo entre el **primer mes liquidado** y el **mes anterior al actual**, e inserta entradas con `ventas: 0` para todos los meses intermedios que no aparecieron en la query.

### 3. Caso especial: primeros 10 días del mes

Si hoy es **antes del día 10**, el mes anterior se considera aún en procesamiento. En ese caso, el mes anterior al actual recibe `ventas: -1` en lugar de su valor real o `0`. El frontend debe interpretar `-1` como "en proceso, aún no disponible".

> **Nota:** el mes actual **nunca aparece** en esta respuesta. Es responsabilidad del endpoint `resumen-actual`.


---

## Tablas y bases de datos involucradas

| Base de datos | Tabla | Rol |
| --- | --- | --- |
| `LO` | `pedidosDetalle` | Ítems de los pedidos |
| `LO` | `pedidosCabeceraVendedor` | Relación entre el ítem y el vendedor (incluye `vendedorID`) |
| `LO` | `pedidosCabecera` | Cabecera del pedido (fechas, estados de cancelación, cobrado) |
| `NewBytes_DBF` | `pedclit` | Estado del cliente en sistema externo (se filtra `cestado <> 'P'`) |

**Join clave para el filtro por vendedor:** `pedidosCabeceraVendedor.vendedorID = :vendedor_id` El `vendedor_id` se extrae del JWT del request, **no viene como parámetro en la URL**.

---

## Query SQL (referencia)

Esta query obtiene los meses con ventas reales. El relleno de meses vacíos se hace en la **capa de aplicación**, no en SQL.

```
SELECT
    COUNT(*) AS ventas,
    DATENAME(MONTH, fechaCreacion) AS mes,
    DATENAME(YEAR, fechaCreacion) AS año,
    RIGHT('0' + CAST(DATEPART(MONTH, fechaCreacion) AS VARCHAR), 2) AS keyMes,
    DATEPART(YEAR, fechaCreacion) AS keyAño
FROM (
    SELECT [PC].fechaCreacion
    FROM [LO].[dbo].[pedidosDetalle] PD
    LEFT JOIN [LO].[dbo].[pedidosCabeceraVendedor] PCV ON [PCV].id = [PD].pedidoCabeceraResellerID
    LEFT JOIN [LO].[dbo].[pedidosCabecera] PC ON [PC].id = [PCV].pedidoCabeceraID
    LEFT JOIN [NewBytes_DBF].[dbo].[pedclit] PED ON [PED].cnumped = [PCV].pedclitid
    WHERE
        ([PC].canceladoUsuario <> 1 AND [PC].canceladoVendedor <> 1
         AND [PC].canceladoLibreOpcion <> 1 AND [PC].canceladoAutomaticamente IS NULL)
        AND [PC].cobrado = 1
        AND [PED].cestado <> 'P'
        AND DATEPART(mm, [PC].fechaCreacion) <> DATEPART(mm, GETDATE())
        AND [PCV].vendedorID = :vendedor_id
) AS ventas
GROUP BY
    DATEADD(MONTH, DATEDIFF(MONTH, 0, fechaCreacion), 0),
    DATENAME(MONTH, fechaCreacion),
    DATENAME(YEAR, fechaCreacion),
    DATEPART(MONTH, fechaCreacion),
    DATEPART(YEAR, fechaCreacion)
ORDER BY
    DATEPART(YEAR, fechaCreacion) DESC,
    DATEPART(MONTH, fechaCreacion) DESC
```

> `keyMes` y `keyAño` son columnas auxiliares usadas en la capa de aplicación para construir la clave `YYYY-MM` que permite detectar y rellenar los meses faltantes. **No se devuelven al cliente.**


---

## Lógica de relleno en aplicación (pseudocódigo)

```
primerMes = último elemento del resultado SQL (el más antiguo)
fechaDesde = primerMes.año + '-' + primerMes.mes
fechaHasta = hoy
​
para cada mes entre fechaDesde y fechaHasta (exclusive mes actual):
    si mes existe en el resultado SQL:
        agregar con su conteo real
    si no existe:
        si hoy < día 10 Y mes == mes anterior:
            agregar con ventas = -1  (en proceso)
        si no:
            agregar con ventas = 0  (sin ventas)
```

El array resultante se entrega **del más antiguo al más reciente** (orden cronológico ascendente), tal como lo muestra la respuesta real.

---

## Respuestas posibles

### 200 OK — Respuesta exitosa

Devuelve un **array de objetos**, uno por cada mes desde el primer mes liquidado hasta el mes anterior al actual. Puede ser un array vacío si el vendedor nunca tuvo ventas.

```
[
    {
        "ventas": 3,
        "mes": "Enero",
        "año": "2019"
    },
    {
        "ventas": 0,
        "mes": "Febrero",
        "año": "2019"
    },
    {
        "ventas": 12,
        "mes": "Junio",
        "año": "2020"
    }
]
```

**Descripción de cada campo:**

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `ventas` | `int` | Cantidad de pedidos liquidados en ese mes. `0` = sin ventas. `-1` = mes aún en procesamiento (solo aplica al mes anterior cuando hoy < día 10). |
| `mes` | `string` | Nombre del mes en español (ej: `"Enero"`). Viene de `DATENAME(MONTH, ...)`. |
| `año` | `string` | Año como string (ej: `"2026"`). Viene de `DATENAME(YEAR, ...)`. |

**Valores especiales del campo **`ventas`**:**

| Valor | Significado |
| --- | --- |
| `> 0` | El vendedor tuvo N ventas liquidadas ese mes. |
| `0` | El vendedor no tuvo ventas ese mes (mes relleno por la aplicación). |
| `-1` | El mes aún está en procesamiento (solo aparece en el mes anterior al actual durante los primeros 9 días del mes). |

**Fragmento real de respuesta capturado de gamma** (enero 2019 → enero 2026):

```
[
    { "ventas": 3,  "mes": "Enero",   "año": "2019" },
    { "ventas": 0,  "mes": "Febrero", "año": "2019" },
    { "ventas": 1,  "mes": "Mayo",    "año": "2019" },
    { "ventas": 62, "mes": "Abril",   "año": "2023" },
    { "ventas": 0,  "mes": "Enero",   "año": "2026" }
]
```

### 400 Bad Request

Se devuelve si el token JWT no contiene un usuario válido o el `vendedor_id` no puede resolverse.

```
{
    "error": {
        "code": 400,
        "message": "Falta definir el usuario"
    }
}
```

### 500 Internal Server Error

Se devuelve si la query falla o hay un problema de conexión con la base de datos.

```
{
    "error": {
        "code": 500,
        "message": "Hubo un problema al intentar obtener el resumen actual de liquidación."
    }
}
```

---

## Reglas de negocio importantes

- **El **`vendedor_id`** viene del JWT**, no de la URL. El endpoint no recibe parámetros.


- **Solo accesible para perfil **`vendedor`.


- **El mes actual nunca aparece** en el array. Para el mes en curso existe el endpoint `resumen-actual`.


- **El relleno de meses vacíos ocurre en la capa de aplicación**, no en SQL. La query solo retorna meses con ventas reales; el código construye la secuencia completa.


- **Si el vendedor nunca tuvo ventas**, la query no retorna filas. En ese caso el array de respuesta puede ser vacío `[]`, o solo contener el mes anterior con `-1` si aplica la regla del día 10.


- **El orden es cronológico ascendente** (del más antiguo al más reciente).


- **Los nombres de mes y año son strings en español** tal como los devuelve SQL Server con `DATENAME`. Verificar configuración regional del servidor o traducir en código.



---

## Criterios de aceptación

- `GET /liquidaciones/meses-previos` responde `200` con un array para un vendedor con historial.


- El array incluye todos los meses entre el primero liquidado y el mes anterior al actual, sin saltos.


- Los meses sin ventas aparecen con `ventas: 0`.


- El mes actual **no aparece** en el array.


- Si hoy es anterior al día 10, el mes anterior aparece con `ventas: -1`.


- El array está ordenado cronológicamente ascendente.


- El request sin token o con token inválido responde `401` / `400`.


- Solo se incluyen pedidos con `cobrado = 1` y estado externo distinto de `'P'`.
