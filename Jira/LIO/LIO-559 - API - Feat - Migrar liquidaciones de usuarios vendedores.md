---
jira_key: "LIO-559"
aliases: ["LIO-559"]
summary: "API - Feat - Migrar liquidaciones de usuarios vendedores"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Franco Callipo"
reporter: "Catriel Mercurio"
created: "2026-02-26 08:52"
updated: "2026-03-31 15:57"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-559"
---

# LIO-559: API - Feat - Migrar liquidaciones de usuarios vendedores

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Franco Callipo |
| Reportado por | Catriel Mercurio |
| Creado | 2026-02-26 08:52 |
| Actualizado | 2026-03-31 15:57 |
| Etiquetas | ninguna |
| Jira | [LIO-559](https://bluinc.atlassian.net/browse/LIO-559) |

## Relaciones

- **Padre:** [[LIO-537 - Migración de repositorios previa deprecación de la api legacy|LIO-537]] Migración de repositorios previa deprecación de la api legacy
- **has action item:** [[LIO-593 - APP - Feat - Migrar liquidaciones de usuarios vendedores|LIO-593]] APP - Feat - Migrar liquidaciones de usuarios vendedores

## Descripcion

# Contexto

En la sección "Mis Cobros" del panel del vendedor, hay un widget que muestra el **resumen financiero del mes en curso**: cuánto ganó el vendedor, qué comisión le corresponde, sobre qué volumen de ventas se calcularon esos valores, y cuál es el neto final. Este endpoint es el que alimenta ese widget en tiempo real.

La API actual vive en `api.gamma.libreopcion.com`. Hay que migrar este recurso a la nueva API conservando exactamente el mismo contrato de respuesta.

[adjunto]
Se recomienda probar la funcionalidad con el vendedorID 447 y meses anteriores harcodeados, ya que en desarrollo es probable que meses recientes no tengan movimiento por ser un entorno tipo sandbox

---

## Recurso a migrar

| Campo | Valor |
| --- | --- |
| **Verbo** | `GET` |
| **Path** | `/liquidaciones/resumen-actual` |
| **Autenticación** | Bearer JWT (token del vendedor en el header `Authorization`) |
| **Body / Payload** | Ninguno. Es un GET sin cuerpo. |
| **Query params** | Ninguno. |

---

## Cómo funciona conceptualmente

Cuando el vendedor entra a "Mis Cobros", quiere saber cuánto lleva ganado **en el mes actual**. El sistema calcula ese resumen en tiempo real consultando todos los pedidos del mes vigente que le pertenecen.

Solo se consideran **productos nativos** (del catálogo propio de LibreOpción). Para contabilizar un pedido se exige:

- El pedido **no está cancelado** (ni por el usuario, ni por el vendedor, ni por LO, ni automáticamente).


- El pedido está marcado como **cobrado** (`cobrado = 1`).


- El estado del cliente externo (`pedclit.cestado`) es **distinto de **`'P'` (es decir, no está pendiente en el sistema externo NewBytes).


- La ganancia neta (`ganancia - gastos`) es **mayor o igual a cero**.


- La fecha de creación del pedido cae en el **mes y año actuales**.



La ganancia se calcula como `ganancia - gastos` (se descuentan los gastos al margen bruto). La columna `ventasGanancia` acumula el volumen de ventas (`cantidad * precioVenta`). El campo `total` se calcula como `ganancia - comision`. El mes y el año se obtienen con `DATENAME` sobre `GETDATE()`, por lo que siempre reflejan el período actual del servidor.

---

## Tablas y bases de datos involucradas

| Base de datos | Tabla | Rol |
| --- | --- | --- |
| `LO` | `pedidosDetalle` | Ítems de los pedidos |
| `LO` | `pedidosDetalleLiquidacion` | Datos de liquidación por ítem (ganancia, comisión, gastos, cantidad, precioVenta) |
| `LO` | `pedidosCabeceraVendedor` | Relación entre el ítem y el vendedor (incluye `vendedorID`) |
| `LO` | `pedidosCabecera` | Cabecera del pedido (fechas, estados de cancelación, cobrado) |
| `NewBytes_DBF` | `pedclit` | Estado del cliente en sistema externo (se filtra `cestado <> 'P'`) |

**Join clave para el filtro por vendedor:** `pedidosCabeceraVendedor.vendedorID = :vendedor_id` El `vendedor_id` se extrae del JWT del request, **no viene como parámetro en la URL**.

---

## Query SQL (referencia)

```
SELECT
    DATENAME(MONTH, GETDATE()) AS mes,
    DATENAME(YEAR, GETDATE()) AS año,
    CAST(SUM([PDL].ganancia - [PDL].gastos) AS DECIMAL(14, 2)) AS ganancia,
    CAST(SUM([PDL].comision) AS DECIMAL(14, 2)) AS comision,
    CAST(SUM([PDL].cantidad * [PDL].precioVenta) AS DECIMAL(14, 2)) AS ventasGanancia
FROM [LO].[dbo].[pedidosDetalle] PD
LEFT JOIN [LO].[dbo].[pedidosDetalleLiquidacion] PDL ON [PD].id = [PDL].pedidoDetalleId
LEFT JOIN [LO].[dbo].[pedidosCabeceraVendedor] PCV ON [PCV].id = [PD].pedidoCabeceraResellerID
LEFT JOIN [LO].[dbo].[pedidosCabecera] PC ON [PC].id = [PCV].pedidoCabeceraID
LEFT JOIN [NewBytes_DBF].[dbo].[pedclit] PED ON [PED].cnumped = [PCV].pedclitid
WHERE
    ([PC].canceladoUsuario <> 1 AND [PC].canceladoVendedor <> 1
     AND [PC].canceladoLibreOpcion <> 1 AND [PC].canceladoAutomaticamente IS NULL)
    AND [PC].cobrado = 1
    AND [PED].cestado <> 'P'
    AND DATEPART(mm, [PC].fechaCreacion) = DATEPART(mm, GETDATE())
    AND DATEPART(yy, [PC].fechaCreacion) = DATEPART(yy, GETDATE())
    AND ([PDL].ganancia - [PDL].gastos) >= 0
    AND [PCV].vendedorID = :vendedor_id
```

---

## Respuestas posibles

### 200 OK — Respuesta exitosa

El único caso de éxito. Devuelve un único objeto JSON (no un array).

```
{
    "ganancia": 1250.50,
    "comision": 312.62,
    "ventasGanancia": 8400.00,
    "ventasComision": 3100.00,
    "total": 937.88,
    "mes": "Febrero",
    "año": "2026"
}
```

**Descripción de cada campo:**

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `ganancia` | `float` | Suma de ganancias netas del mes (`ganancia - gastos` por ítem). |
| `comision` | `float` | Suma de comisiones que LO retiene al vendedor en el mes. |
| `ventasGanancia` | `float` | Volumen de ventas del mes (`cantidad × precioVenta`). |
| `ventasComision` | `float` | No aplica para productos nativos. Siempre `0`. |
| `total` | `float` | Neto que le corresponde al vendedor: `ganancia - comision`. **Este campo se calcula en la capa de aplicación, no en la query.** |
| `mes` | `string` | Nombre del mes actual en español (ej: `"Febrero"`). Viene de `DATENAME(MONTH, GETDATE())`. |
| `año` | `string` | Año actual como string (ej: `"2026"`). Viene de `DATENAME(YEAR, GETDATE())`. |

> **Atención:** Cuando el vendedor no tiene ventas en el mes, todos los valores numéricos llegan como `0` (o `-0`, que es equivalente). La respuesta sigue siendo 200 OK; no es un error.


**Ejemplo real de respuesta con cero ventas (capturado de gamma):**

```
{
    "ganancia": -0,
    "comision": -0,
    "ventasGanancia": -0,
    "ventasComision": -0,
    "total": 0,
    "mes": "Febrero",
    "año": "2026"
}
```

> El frontend debe tratar `-0` y `0` como equivalentes.


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

- **El **`vendedor_id`** viene del JWT**, no de la URL. El endpoint no recibe parámetros. Hay que extraerlo del token autenticado.


- **Solo accesible para perfil **`vendedor`. Si el perfil del token es otro (admin, usuario, etc.), el endpoint no debe responder datos (retornar vacío o 403, a definir por la nueva API).


- **Siempre devuelve un único objeto**, nunca un array. Aunque no haya ventas, devuelve el objeto con todos los valores en `0`.


- **El **`total`** se calcula en código**, no en la query: `total = ganancia - comision`.


- **Los floats se normalizan** antes de enviarlos. La función actual usa `Utils::normalizarFlotante()` para evitar precisiones raras. Asegurarse de redondear correctamente (máximo 2 decimales en la query con `DECIMAL(14,2)`).


- **El mes y el año son strings en español** tal como los devuelve SQL Server con `DATENAME` en la configuración regional del servidor. Verificar que la nueva base de datos esté configurada igual o traducir en código.



---

## Criterios de aceptación

- `GET /liquidaciones/resumen-actual` responde `200` con el objeto correcto para un vendedor con ventas en el mes.


- El mismo endpoint responde `200` con todos los valores en `0` para un vendedor sin ventas.


- El request sin token o con token inválido responde `401` / `400`.


- El campo `total` es siempre igual a `ganancia - comision`.


- Los campos `mes` y `año` reflejan el período en curso del servidor.


- El endpoint ignora pedidos cancelados (cualquier tipo de cancelación).


- Solo se incluyen pedidos con `cobrado = 1` y estado externo distinto de `'P'`.
