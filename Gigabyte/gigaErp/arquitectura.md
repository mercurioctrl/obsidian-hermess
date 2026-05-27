# Arquitectura — gigaErp

## Estructura de directorios

```
gigaErp/
├── backend/          ← Laravel 11 (PHP 8.4)
│   ├── app/
│   │   ├── Enums/            ← RolUsuario, EstadoTarea, PrioridadTarea, EstadoVenta, EstadoOrdenVenta, TipoMovimiento
│   │   ├── Http/Controllers/ ← 22 resource controllers + CuentaCorrienteController
│   │   ├── Http/Resources/   ← 9 API resources
│   │   ├── Models/           ← 21 Eloquent models (+ MovimientoCuenta)
│   │   └── Services/
│   ├── database/
│   │   ├── migrations/       ← 0001–0030
│   │   └── seeders/          ← DatabaseSeeder + DemoSeeder + ProductoInvidSeeder + ProductoNewBytesSeeder + CuentaCorrienteSeeder
│   └── routes/api.php        ← todo dentro de auth:sanctum
├── frontend/         ← Nuxt 3 SPA (ssr: false)
│   ├── components/
│   │   ├── ui/               ← Modal, FormField, DataTable, StatsCard, StatusBadge, Toast
│   │   └── OrdenItems.vue
│   ├── composables/          ← useApi, useNotification
│   ├── layouts/              ← default (sidebar+topbar), auth
│   ├── middleware/           ← auth.global.ts (NO usar definePageMeta)
│   ├── pages/
│   │   ├── clientes/
│   │   │   ├── index.vue               ← listado con saldo_usd + botones de acción
│   │   │   └── [id]/
│   │   │       ├── index.vue           ← ficha distribuidor + fondo marketing
│   │   │       └── cuenta-corriente.vue ← movimientos, saldo acumulado
│   │   ├── mercaderia/
│   │   │   ├── index.vue               ← redirect a /mercaderia/stock
│   │   │   ├── stock/index.vue         ← tabs + buscador + filtro con/sin stock
│   │   │   ├── depositos/index.vue     ← tabs
│   │   │   └── importaciones/
│   │   │       ├── index.vue           ← tabs (tab "Subir Masivo" activo)
│   │   │       ├── nueva.vue
│   │   │       └── [id].vue
│   │   ├── productos/index.vue         ← APIs Distri
│   │   ├── existencias/index.vue       ← Stock Distri
│   │   ├── ordenes-venta/index.vue     ← listado de órdenes
│   │   ├── ordenes-venta/nueva.vue     ← crear orden con líneas dinámicas
│   │   └── ordenes-venta/[id].vue      ← detalle, edición y descarga de PDF
│   ├── public/logos/
│   └── stores/               ← auth.ts (Pinia)
├── nginx/default.conf
└── docker-compose.yml
```

## Sidebar — estructura de navegación

```
Principal:    Dashboard · Distribuidores · Proveedores
Operaciones:  Stock Bodega · Stock Distri · APIs Distri · Órdenes de Venta
Marketing:    Fondo · Calendario · Tareas
Admin:        Configuración (solo admin)
```

## Módulo Cuenta Corriente — `GET /api/clientes/{cliente}/cuenta-corriente`

```
Tabla: movimientos_cuenta
Campos: id, cliente_id, tipo (TipoMovimiento enum), referencia, concepto,
        fecha, debe_usd, haber_usd, venta_id (nullable FK → ventas)
```

**Enum TipoMovimiento:** `FACTURA`, `PAGO`, `NOTA_CREDITO`, `AJUSTE`

**Response:**
```json
{
  "movimientos": [
    {
      "id": 1, "fecha": "2025-08-10", "tipo": "FACTURA", "tipo_label": "Factura",
      "referencia": "VTA-H001", "concepto": "...",
      "debe_usd": 15800, "haber_usd": 0, "saldo_usd": 15800,
      "venta_id": null, "venta_numero": null
    }
  ],
  "resumen": { "debe_usd": 104660, "haber_usd": 96350, "saldo_usd": 8310 }
}
```

**Saldo acumulado corriente:** se calcula en el controller con closure sobre `$saldoAcumulado`.

**Saldo en listado:** `ClienteController@index` usa `withSum('movimientosCuenta as debe_total_usd', 'debe_usd')` + `withSum(... 'haber_usd')`. Luego `ClienteResource` computa `saldo_usd = debe_total_usd - haber_total_usd`.

## Routing Nuxt — gotcha crítico

**Problema:** Si existe `pages/foo/[id].vue` Y el directorio `pages/foo/[id]/`, Nuxt trata el `.vue` como layout padre de todas las rutas hijas. El contenido de las rutas hijas no reemplaza al padre.

**Solución:** Mover `[id].vue` a `[id]/index.vue`. Así son rutas hermanas independientes.

```
pages/clientes/
  [id]/
    index.vue           → /clientes/:id   (ficha)
    cuenta-corriente.vue → /clientes/:id/cuenta-corriente
```

## Patrones de backend

- Resource controllers: `index / store / show / update / destroy`
- Respuestas con Resource: wrap `{ data: {} }` automático para recursos individuales
- Colecciones paginadas: `{ data: [], meta: { total, per_page, current_page, last_page } }`
- **En frontend siempre:** `c?.data ?? c` para recursos individuales, `res.data ?? res` para listas

## Módulo Productos — `GET /api/productos`

```
Filtros: ?search=X &distribuidor_id=N &stock=con_stock|sin_stock &activo=1
Pagina: 50 por página
Eager loads: distribuidor, stocks.deposito
```

## Módulo Existencias — `GET /api/existencias`

```json
{ "distribuidores": [...], "items": [{ "sku", "stock": {dist_id: N|0|null} }] }
```

## Módulo Órdenes de Venta

Pipeline: OrdenVenta (BORRADOR) → `POST /ordenes-venta/{id}/invoice` → Venta (PENDIENTE) → PAGADA/CANCELADA

Cada `ItemOrdenVenta` tiene `deposito_id` nullable (de qué depósito se toma el stock).

## Rutas estáticas — orden crítico

Las rutas estáticas van **antes** del `apiResource`. Ejemplos:
```php
Route::get('/clientes/export', ...);           // antes de apiResource
Route::get('/clientes/{cliente}/fondo', ...);  // antes de apiResource
Route::get('/clientes/{cliente}/cuenta-corriente', ...); // antes de apiResource
Route::apiResource('clientes', ...);           // DESPUÉS
```

## apiResource — pluralización española (BUG CONOCIDO)

| apiResource | Parámetro generado | Fix |
|------------|-------------------|-----|
| `acciones` | `{accione}` ❌ | `.parameters(['acciones' => 'accion'])` |
| `proveedores` | `{proveedore}` ❌ | `.parameters(['proveedores' => 'proveedor'])` |
| `ordenes-venta` | `{orden_venta}` ✅ | `.parameters(['ordenes-venta' => 'orden_venta'])` |

## Paginación vs colección por módulo

| Módulo | Backend | Frontend — leer con |
|--------|---------|---------------------|
| Clientes, Ventas, Acciones, Productos, Órdenes de Venta | `paginate(20/50)` | `res.data` + `res.meta` |
| Tareas, Etiquetas, Tipos, Estados, Depósitos | `get()` | `res.data ?? res` |
| Existencias | `get()` agrupado | `res.distribuidores` + `res.items` (sin wrapper) |
| Cuenta corriente | custom | `cc.movimientos` + `cc.resumen` |

## Modelos y relaciones principales

```
Cliente (=Distribuidor)
  ├── acciones_marketing · campanas · asignaciones_fondo
  ├── ventas · ordenes_venta · tareas
  ├── productos (via distribuidor_id)
  └── movimientos_cuenta  ← NUEVO

MovimientoCuenta
  ├── belongsTo: Cliente
  └── belongsTo: Venta (nullable)

Producto
  ├── stocks_deposito (StockDeposito)
  └── items_orden_venta · items_venta

OrdenVenta → ItemOrdenVenta → [Deposito]
Venta → ItemVenta
```

## Enum en colecciones — bug keyBy

`->get()->keyBy('estado')` falla con enum cast. **Fix:** `->keyBy(fn($v) => $v->estado->value)`

## Decisiones de diseño

### `config:cache` obligatorio (PHP-FPM)
`env()` devuelve null en PHP-FPM. Fix: `docker exec gigaerp-backend php artisan config:cache`

### Distribuidores = Clientes con `tipo='distribuidor'`
No hay tabla separada para distribuidores. Campo `tipo` en `clientes`.

### Dos tablas de stock coexisten
- `stock` directo en `productos`: Productos y Existencias
- `stock_deposito` (via `StockDeposito`): Stock Bodega
- Son independientes — no se sincronizan automáticamente

### Nomenclatura UI vs URL
| URL | Nombre UI |
|-----|-----------|
| `/mercaderia/stock` | Stock Bodega |
| `/existencias` | Stock Distri |
| `/productos` | APIs Distri |
| `/mercaderia/importaciones` | Subir Masivo |
| `/marketing` | Fondo |

## Ver también

- [[gigaErp]] · [[stack]] · [[changelog]] · [[contexto]] · [[memoria]]
- [[modulos/productos]] · [[modulos/ordenes-venta]] · [[modulos/invoice-preview]]

## Módulo Importaciones de Stock (XLSX)

Flujo de 3 pasos para ingresar stock al depósito desde un archivo Excel.

### Endpoints

- `POST /api/mercaderia/importaciones/parsear` — Recibe archivo xlsx/xls/csv, lo guarda en storage con UUID, devuelve headers de la primera fila + muestra de filas para mapeo
- `POST /api/mercaderia/importaciones/procesar` — Recibe `staged_id`, `deposito_id` y mapeo (`col_codigo`, `col_cantidad`), ejecuta upsert en `stock_deposito`

### Modelos

- `ImportacionMercaderia` — Registro de cada carga (fecha, depósito, archivo)
- `ItemImportacionMercaderia` — Líneas de trazabilidad por producto

### Frontend (`frontend/pages/mercaderia/importaciones/`)

- `index.vue` — listado de importaciones con tab "Subir Masivo"
- `nueva.vue` — paso 1: upload archivo → paso 2: mapeo de columnas → paso 3: confirmar
- `[id].vue` — detalle de una importación

**Dependencia backend:** `phpoffice/phpspreadsheet` (ya instalado en el container)

## Ver también

- [[contexto]] · [[modulos/productos]] · [[stack]]

## Sistema de permisos — `permisos` JSON en `usuarios`

```php
// Modelo Usuario
public function tienePermiso(string $permiso): bool
{
    if ($this->esAdmin()) return true;
    return in_array($permiso, $this->permisos ?? []);
}
```

**Permisos actuales:**
| Clave | Descripción | Dónde se verifica |
|-------|-------------|------------------|
| `aprobaciones` | Aprobar órdenes de venta (BORRADOR → APROBADA) | `OrdenVentaController::aprobar()` |
| `VER_MONTOS` | Ver montos en el sistema | `authStore.verMontos` |

**Agregar permiso nuevo:** string en `PERMISOS_DISPONIBLES` (configuracion/index.vue) + verificar en backend con `tienePermiso()`.

## Flujo de estados — Órdenes de Venta

```
BORRADOR ──(aprobaciones)──► APROBADA ──(cualquiera)──► FACTURADA
   │                              │
   └──────────────────────────────┴──────────────────► ANULADA
```

**Endpoints de transición (antes del apiResource en routes/api.php):**
```php
Route::post(/ordenes-venta/{orden_venta}/invoice, ...)   // APROBADA → FACTURADA
Route::patch(/ordenes-venta/{orden_venta}/aprobar, ...)  // BORRADOR → APROBADA (requiere permiso)
Route::patch(/ordenes-venta/{orden_venta}/anular, ...)   // → ANULADA
Route::apiResource(ordenes-venta, ...)
```

## Gestión de usuarios desde UI

`Configuración → Usuarios` — tab completo con:
- Listado: nombre, email, rol, activo, badges de permisos
- Modal crear/editar: nombre, email, password, rol, activo, checkboxes de permisos
- Solo visible para ADMIN (`if (!authStore.isAdmin) navigateTo("/")`)
