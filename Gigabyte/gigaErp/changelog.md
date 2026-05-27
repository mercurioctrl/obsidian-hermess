## 2026-05-27 — Línea de crédito + Notas de crédito + fixes UI

### Línea de crédito por distribuidor

- Nuevo campo `linea_credito_usd` (decimal nullable) en tabla `clientes` — migración `0031`
- Endpoint `PATCH /api/clientes/{cliente}/linea-credito` con validación `monto_usd` + `notas`
- Endpoint `GET /api/clientes/{cliente}/historial-credito` — devuelve historial con usuario y timestamps
- Tabla `historial_linea_credito` — migración `0032`: `cliente_id`, `usuario_id`, `monto_anterior_usd`, `monto_nuevo_usd`, `notas`
- Modelo `HistorialLineaCredito` con relaciones a `Cliente` y `Usuario`
- **Frontend** `cuenta-corriente.vue`: 4ª card con monto, barra de utilización (roja >90%), botón lápiz (solo admin)
- Modal de edición con campo "Motivo / notas" — cada cambio queda registrado en historial
- Tabla de historial debajo de movimientos: fecha, usuario, anterior, nuevo, notas
- **Demo data**: 2 entradas de historial por distribuidor (asignación inicial + ampliación por Carolina Lagos)

Archivos: `backend/database/migrations/0031_*`, `backend/app/Models/HistorialLineaCredito.php`, `backend/app/Http/Controllers/ClienteController.php` (asignarCredito + historialCredito), `backend/routes/api.php`, `frontend/pages/clientes/[id]/cuenta-corriente.vue`

### Módulo Nota de Crédito

Entidad nueva completa: **nota de crédito** emitida a un distribuidor con ítems libres (texto, no productos del catálogo).

**Backend:**
- Migración `0033`: tablas `notas_credito` y `notas_credito_items` + columna `nota_credito_id` nullable en `movimientos_cuenta`
- Modelo `NotaCredito`: `numero` (NC-0001), `cliente_id`, `usuario_id`, `fecha`, `concepto`, `total_usd`, `estado` (EMITIDA/ANULADA)
- Modelo `NotaCreditoItem`: `descripcion`, `cantidad`, `precio_usd`, `subtotal_usd` — texto libre, sin FK a productos
- `NotaCreditoController`:
  - `GET /clientes/{cliente}/notas-credito` — lista con ítems
  - `POST /clientes/{cliente}/notas-credito` — crea NC + ítems + asienta `MovimientoCuenta` NOTA_CREDITO (haber)
  - `GET /notas-credito/{notaCredito}/preview` — vista HTML pública con `?token=...`
- Vista blade `resources/views/notas-credito/preview.blade.php`: mismo estilo que invoice pero con acento verde, header "Nota de Crédito", total "Total a acreditar", descarga PDF via html2pdf.js

**Frontend — desde cuenta corriente:**
- Botón "Nota de crédito" en header de `/clientes/{id}/cuenta-corriente`
- Modal con: fecha, concepto/obs, tabla de ítems (descripción, cantidad, precio) editables, total en tiempo real
- Al emitir: refresca movimientos, abre preview en nueva tab
- En tabla de movimientos: referencia NC-XXXX es clickeable → abre preview

**Frontend — desde órdenes de venta:**
- Botón "Nota de crédito" (lila) en banner de invoice generada, visible solo cuando estado = FACTURADA
- Modal pre-llenado con ítems de la orden (nombre + SKU como descripción, cantidad y precio originales)
- Ítems editables: bajar cantidad o precio → nota de crédito **parcial**; dejar todo → nota **total**
- Al emitir: acredita al distribuidor de la orden y abre preview

Archivos: `backend/database/migrations/0033_create_notas_credito_tables.php`, `backend/app/Models/{NotaCredito,NotaCreditoItem}.php`, `backend/app/Http/Controllers/NotaCreditoController.php`, `backend/resources/views/notas-credito/preview.blade.php`, `backend/routes/api.php`, `frontend/pages/clientes/[id]/cuenta-corriente.vue`, `frontend/pages/ordenes-venta/[id].vue`

### Navegación: click en distribuidor → cuenta corriente

Antes: click en fila del listado de distribuidores → `/clientes/{id}` (ficha con fondos de marketing).
Ahora: click en fila → `/clientes/{id}/cuenta-corriente` directamente.

Archivo: `frontend/pages/clientes/index.vue`

### Fixes UI

- **Sidebar**: "Fondo" → "Fondos" (`frontend/layouts/default.vue`)
- **Stock Bodega**: barra de filtros ahora usa card `bg-white rounded-xl border border-[#E8E8E3] p-4` consistente con el resto de páginas (`frontend/pages/mercaderia/stock/index.vue`)
- **Importaciones XLSX**: fallback a `codigo_distribuidor` si no hay match por `sku` (`ImportacionMercaderiaController`)

## 2026-05-27 — Datos demo: órdenes de venta para todos los distribuidores

Se crearon 20 órdenes de venta FACTURADAS (5 por distribuidor) via tinker, con sus ventas, ítems y movimientos de cuenta corriente correspondientes.

**Volumen creado:**

| Distribuidor | Órdenes | Facturado |
|---|---|---|
| Elit | 5 | USD 54,540 |
| New Bytes | 5 | USD 40,240 |
| Invid | 5 | USD 52,345 |
| Air | 5 | USD 28,790 |

**Criterio de productos por distribuidor:**
- Elit (BA): high-end — AERO 16, M27U, RTX 4070, SSD, Cooler AIO
- New Bytes (Córdoba): gaming — G5 KF, G27Q, RX 7600, K85, M4000, H500
- Invid (Mendoza): workstation + componentes — AERO 16, M27U, fuentes, coolers, SSD
- Air (Rosario): periféricos litoral — K85, M4000, H500, G27Q, fuentes, SSD

Cada orden: estado FACTURADA, venta asociada (VTA-0015 a VTA-0034), movimiento DEBE en cuenta corriente.
Las órdenes originales del DemoSeeder (OV-0001, OV-0002) se conservan. Total OV: 22, total ventas: 34.

**Commit:** `8162e3c` — incluye todo el módulo de notas de crédito + línea de crédito + este seeding.
