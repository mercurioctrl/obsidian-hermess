# API - Fix - Corregir doble-descuento de stock por race en MakeSale/RemoveSale

**Proyecto:** [[pedidos|Pedidos]]
**Estado:** Implementado (pendiente verificación en vivo + regularización de datos)
**Fecha:** 2026-06-11
**Repos afectados:** `api-rest-pedidos-laravel` (fix) · `inventario/ms-metadata` (donde se detectó el síntoma)

Una **race condition** en `MakeSaleService` descuenta stock **dos veces** ante requests duplicados/concurrentes del mismo pedido, mientras la baja (`RemoveSaleService`) solo repone una vez. Resultado: stock que desaparece sin documento de venta. Se detectó porque el `stockDelta` del panel de inventario daba valores distintos de cero. Auditoría completa: **138 artículos** con **683 unidades** realmente perdidas.

---

## 1. El síntoma — `stockDelta` incorrecto

El panel de stock de `inventario` (backend `ms-metadata`, `core/controllers/stocks/stocks.py`) calcula por artículo un **`stockDelta`**: una reconciliación entre los **documentos oficiales** del ERP y el **stock físico actual**. Si da ≠ 0, los libros no cuadran (la fila sale en rojo).

### Fórmula (`stocks.py`)

```
stockDelta =  inProviderOrderInbound   (+)  ingresos de proveedor (albprol)
            - aftersalesCreditNote     (-)  NC postventa (ST_RMADETALLE)
            + creditNoteReturn         (+)  devoluciones acreditadas (albclil.ACREDITADO)
            - nstockHide               (-)  stock oculto (stocks.nstock_d1)
            - stock                    (-)  stock real (stocks.nstock)
            - stockLio                 (-)  stock LibreOpción (stocks.nstock_lo)
            - stockCtrl                (-)  stock en control (stocks.nstock_ctrl)
            - stockLoQueue             (-)  stock en cola (stocks.nstock_en_cola)
            - salesReserved            (-)  remitos reservados (albclit.ntipoalb = 1)
            - sales                    (-)  ventas remitadas (albclit.ntipoalb > 1)
            + globalRegularization     (+)  regularización global (stocks.regularizacion_global)
```

> Mezcla **flujos acumulados** (albprol/albclil, históricos) con el **stock vivo** (tabla `stocks`). Cuando una operación toca el stock vivo sin dejar el documento equivalente, aparece un delta fantasma. Ver [[relacion-tablas-articulo-stocks]] y [[relacion-tablas-albprot-albprol]].

### Caso testigo — artículo 119699 (empresa 4)

`MOUSE WIRELESS GENIUS NX-7000X BLACK` — **`stockDelta = 70`**:

| Componente | Signo | Valor |
|---|:---:|---:|
| inProviderOrderInbound | + | 9000 |
| sales | − | 8930 |
| (resto) | | 0 |
| **stock físico actual** | | **0** |

`9000 − 8930 = 70`. Entraron 9000, hay documentos de venta por 8930, stock 0 → **70 unidades "desaparecieron"** sin respaldo.

---

## 2. Diagnóstico — el historial de stock (`registro_stock`)

La tabla `NB_WEB.dbo.registro_stock` es el kardex: cada movimiento con `cantidad`, `sAnterior`/`sPosterior`, `remito` y `fichero` (proceso que lo generó).

Para el 119699, los 70 faltantes salen de **exactamente 2 remitos** con la misma firma:

**R-0002-00610351 — 17/03/2025**

| Hora | cantidad | sAnterior | sPosterior | operación |
|---|---:|---:|---:|---|
| 10:42:58 | −50 | 1997 | 1947 | Generar Pedido (MakeSale) |
| 10:43:24 | −50 | **1997** | 1947 | Generar Pedido (MakeSale) |
| 10:45:12 | +50 | 1897 | 1947 | Eliminar pedido (RemoveSale) |

**R-0002-00613197 — 09/04/2025**: idéntico patrón (−20, −20, +20).

### La firma del bug

Dos movimientos `MakeSale` con el **mismo `sAnterior`** (1997), a segundos de diferencia → **dos requests leyeron el mismo stock inicial en paralelo** (doble-submit / race). Como el `UPDATE` es **relativo** (`SET nstock = nstock - qty`, confirmado: los ingresos usan `nstock = nstock + 3000`), las dos restas **sí se aplicaron** (−100 real), pero la cancelación repuso **una sola vez** (+50). Neto: **−50 perdidas, sin documento**. Lo mismo con −20.

Verificado además: ni la línea `albclil` ni la cabecera `albclit` de esos remitos existen ya (pedido cancelado y borrado), y no hay tablas `pedcli*` en esta base (los pedidos viven en la API Laravel). El `stockDelta = 70` es **correcto** — está detectando una pérdida real, el defecto está en el alta de pedidos.

---

## 3. Detección masiva — todos los casos

Firma precisa en SQL: **≥2 movimientos `MakeSaleService` para el mismo `(cref, remito, sAnterior)`** (imposible sin concurrencia).

```sql
SELECT cref, remito, sAnterior, cantidad, COUNT(*) AS veces
FROM NB_WEB.dbo.registro_stock
WHERE fichero LIKE '%MakeSaleService%'
  AND remito IS NOT NULL AND LTRIM(RTRIM(remito)) <> ''
  AND cantidad < 0
GROUP BY cref, remito, sAnterior, cantidad
HAVING COUNT(*) >= 2
```

| Métrica | Valor |
|---|---:|
| Grupos con la firma del race (bruto) | 5.748 |
| Artículos tocados (bruto) | 1.771 |
| Remitos afectados | 5.747 |
| Unidades descontadas de más (bruto) | 35.231 |
| **Artículos con PÉRDIDA NETA real** | **138** |
| **Unidades perdidas (neto, tras reversas y ventas legítimas)** | **683** |

La pérdida neta se obtuvo cruzando, por remito afectado, lo descontado del stock contra lo documentado en `albclil` (mismo método que el 119699, validado: da 70 exacto). Top: 117542 (75), 119699 (70), 115239 (30), 106820 (20), 7658 (20), 102048 (19)…

> Listado completo de los 138: archivo `casos_doble_descuento.csv` (generado en el análisis).

---

## 4. La solución implementada

Todo en `api-rest-pedidos-laravel`. El fix correcto va en la **API de pedidos**, no en `ms-metadata` (que solo reporta el síntoma).

### 4.1 Lock de pedido reutilizable — `MakeSaleRepository`

```php
public function lockOrderForProcessing($branch, $order)
{
    $sql = " SELECT cestado FROM [NewBytes_DBF].[dbo].[pedclit] WITH (UPDLOCK, HOLDLOCK)
             WHERE cnumped = :cnumped AND cnumsuc = :cnumsuc ";
    return DB::selectOne($sql, ['cnumped' => $order, 'cnumsuc' => $branch]);
}
```

Toma un lock de actualización exclusivo sobre la fila del pedido, **retenido hasta el commit** (por estar dentro de `DB::transaction`).

### 4.2 Guard en `MakeSaleService::executeOrder()`

Al inicio de la transacción, antes de tocar nada:

```php
$lockedOrder = $this->repository->lockOrderForProcessing($params['branch'], $params['order']);
if ($lockedOrder && $lockedOrder->cestado !== 'P') {
    throw new \Exception('El pedido ya fue facturado o está siendo procesado');
}
```

Dos requests del mismo pedido: el primero lockea y avanza; el segundo **bloquea**, despierta cuando el primero commitea, lee `cestado = 'S'` y corta. **Un solo descuento.**

### 4.3 `RemoveSaleService::revertSale()` — transacción + guard

`revertSale` **no estaba envuelto en transacción** (sin atomicidad ni aislamiento). Se envolvió en `DB::transaction` y se agregó el mismo guard (estado esperado `'s'` = remitido):

```php
return DB::transaction(function () use ($params) {
    $lockedOrder = $this->repository->lockOrderForProcessing($params['branch'], $params['order']);
    if ($lockedOrder && strtolower($lockedOrder->cestado) !== 's') {
        throw new \Exception('El pedido ya fue revertido o no se encuentra Remitido');
    }
    // ... resto del revert ...
});
```

Evita doble reposición de stock y, de yapa, la baja ahora es atómica.

### 4.4 Numeración de `CNUMALB` — `MakeSaleRepository::createHeader()`

`createHeader` calculaba el próximo remito con `MAX(CNUMALB)+1` **sin lock** → dos pedidos concurrentes de la misma sucursal podían colisionar. Se agregó hint a los dos subqueries:

```sql
FROM [NewBytes_DBF].[dbo].albclit WITH (UPDLOCK, HOLDLOCK) WHERE cnumsuc = '...'
```

Serializa la numeración por sucursal entre pedidos distintos.

Ver el flujo completo en [[modulo-makesale]] y [[modulo-removesale]].

---

## 5. Caveats y verificación

- **OPcache:** la API está corriendo. Si `opcache.validate_timestamps=0`, hay que recargar PHP-FPM para que tome el cambio. Confirmar.
- **`CNUMALB` (4.4) — trade-off:** el `HOLDLOCK` evita remitos duplicados pero, con alta concurrencia en la misma sucursal, puede provocar deadlocks esporádicos (SQL Server aborta una → reintento). Alternativa más limpia: `SEQUENCE`/tabla contador dedicada.
- **Índice `pedclit(cnumped, cnumsuc)`:** verificar que exista para que el lock 4.1 sea de fila y no de rango.
- **Verificación:** facturar y revertir un pedido normal (debe andar igual). Caso de carrera: dos requests casi simultáneos del mismo pedido → uno OK, el otro rechazado, **un solo** movimiento en `registro_stock`.

---

## 6. Pendientes

- [ ] **Regularizar datos:** +683 unidades en los 138 artículos perdidos. Script listo (dry-run validado, **sin aplicar**): [[API - Fix - Script de regularización stock doble-descuento|Script de regularización]].
- [ ] **Front:** debounce / deshabilitar el botón Facturar al primer click (defensa en profundidad).
- [ ] **Evaluar** `SEQUENCE` para `CNUMALB` en vez del `MAX+1` con lock.
- [ ] Confirmar recarga de OPcache en el server.

## Ver también

- [[modulo-makesale|MakeSale — ejecución de pedidos]]
- [[modulo-removesale|RemoveSale — reversión de remitos]]
- [[relacion-tablas-articulo-stocks|Artículo y stocks]]
- [[relacion-tablas-albprot-albprol|Remitos de compra (albprot/albprol)]]
- [[relacion-tablas-ped-alb|Ventas: pedclit / pedclil / albclit / albclil]]
- [[contexto|Reglas de negocio y gotchas]]
