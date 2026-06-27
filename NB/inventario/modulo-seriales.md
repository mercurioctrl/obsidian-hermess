# Módulo Seriales — modal de detalle por artículo

Modal que lista los seriales de un artículo desde la grilla de Stock, con estado,
documentos asociados, cambios de RMA y compra de origen. Click en las celdas de
Seriales (Us/Tot, Disp., Δ ser.) lo abre.

- **Front**: `components/Modal/ItemStock/SerialsById.vue`, `plugins/api.js` (`getSerialsById`).
- **Back**: `get_item_serials` en `ms-metadata/core/controllers/stocks/stocks.py`;
  endpoint `GET /serials/{itemId}?stockWarehouseId=`; modelo `ItemSerial`.

## Columnas
Serial · Estado (En stock / Despachado) · Devuelto (tag + fecha) · **Cambio RMA** ·
Fecha de ingreso · **Compra** · Fecha de despacho · Orden · Factura · NC · Pedido · Depósito.

## Estado del serial
`present` = sigue en stock = `ST_DETALLE_STOCK.FECHA_EGRESO` NULL/0; el resto está
despachado. RMA (cliente/proveedor) se marca con tag aparte (`ID_RMACLIENTE` /
`ID_RMAPROVEEDOR`).

> **Bug resuelto**: el endpoint serializaba solo 6 campos a mano → el front nunca
> recibía `present` y todo aparecía como "despachado". Fix: serializar el objeto
> completo. Además los LEFT JOIN multiplicaban filas → `OUTER APPLY ... TOP 1` (última
> salida) deja **1 fila por serial** (item 118151: 1945→1943, en stock 0→217).

## Cadena documental (serial → comprobante)
`serial → ST_REMITOS_VENTA_DETALLE_SALIDA (RVD, por SERIAL) → albclit (cabecera de
remito cliente: REMITO_FP=cnumalb + SUCURSAL_REMITO=cnumsuc)`. De `albclit`: `cnumped`
= **pedido**, `cfactura` = comprobante; el tipo (1=Factura / 2=NC) sale de
`FP_FactWebCliEncabezado.NTIPODOCU` por `CFACTURA`. **Gotcha de índice**: mantener
`CNUMALB` bare en el join (no `LTRIM(RTRIM(...))`, mata `IX_FP_FactWebCliEncabezado_1`).

> **Gap conocido**: las NC de **devolución física** son un documento aparte no
> alcanzable por el remito de despacho; solo aparecen las NC de punto de venta.

## Cambio RMA (serial reemplazado ↔ reemplazo)
El RMA tipo "Cambio" (`ST_RMADETALLE.ID_ACCION = 2`) deja dos rastros:
- `ST_RMADETALLE.SERIAL` = unidad que el **cliente devolvió**.
- `ST_DETALLE_STOCK.ID_RMACLIENTE` = el RMA por el que **salió el reemplazo**.

Cruzándolos por `ID_RMACLIENTE` se marca, en ambas direcciones: "reemplazó a X"
(`rmaReplacedSerial`) y "reemplazado por Y" (`rmaReplacementSerial`). Ej. real:
`9LW1332O30370 → 9LX6010R30164 → 9MJ8169X40044`. Se resuelve con **UNA query chica
sobre `ST_RMADETALLE` (acotada al CREF) + dicts en Python** — la versión con subqueries
correlacionadas contra `ST_DETALLE_STOCK` (5.4M) tardaba 12.6s → 1.1s.

## Compra de origen
`ST_DETALLE_STOCK.ID_COMPRA` formateado a 8 dígitos (legacy): 13191 → `00013191`.

## UX del modal
- Filtros **en vivo** (sin botón): estado (Todos/En stock/Despachados/RMA), depósito
  (**"Todos" por defecto** — clave: si filtra por el depósito de la fila esconde los
  disponibles), búsqueda (matchea serial, seriales de cambio y nº de compra).
- Chips de conteo: Total / En stock / Despachados / RMA.
- Paginación configurable (50/100/200/500) + switch **"Ver todos"**.
- Export **CSV** (BOM + `;`) y **XLSX** (`import('xlsx')` dinámico) respetando los
  filtros visibles; archivo `seriales_<itemId>_<fecha>`.
- Header con `scroll.x` numérico (suma de anchos) para que la cabecera acompañe el
  scroll horizontal — ver gotcha antd 1.x en [[contexto]].

## Ver también
- [[arquitectura#Modal de seriales — documentos, RMA y compra]]
- [[performance-indices]] — los índices P2/P3 aceleran los conteos y el OUTER APPLY
- [[modulo-regularizacion]] — el Δ ser. y el ledger de seriales
- [[changelog]] · [[memoria]] · [[inventario]]
