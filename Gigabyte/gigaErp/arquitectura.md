# Arquitectura — gigaErp

## Estructura de directorios

```
gigaErp/
├── backend/          ← Laravel 11 (PHP 8.4)
│   ├── app/
│   │   ├── Enums/            ← RolUsuario, EstadoTarea, EstadoVenta, EstadoOrdenVenta, TipoMovimiento
│   │   ├── Http/Controllers/ ← ~25 controllers (incl. ImportacionCatalogoController)
│   │   ├── Http/Resources/   ← 9 API resources
│   │   ├── Models/           ← ~24 Eloquent models
│   │   └── (no Services aún)
│   ├── database/
│   │   ├── migrations/       ← 0001–0040 (numeradas)
│   │   └── seeders/          ← DatabaseSeeder, DemoSeeder, ProductoInvidSeeder,
│   │                            ProductoNewBytesSeeder, CuentaCorrienteSeeder, UsuarioSeeder
│   ├── resources/views/
│   │   ├── ventas/           ← invoice.blade.php, invoice-preview.blade.php
│   │   └── notas-credito/    ← preview.blade.php
│   └── routes/api.php        ← todo dentro de auth:sanctum (excepto previews y login)
├── frontend/         ← Nuxt 3 SPA (ssr: false)
│   ├── components/
│   │   ├── ui/               ← Modal, FormField, DataTable, StatsCard, StatusBadge, Toast
│   │   └── OrdenItems.vue    ← picker de productos para órdenes de venta
│   ├── composables/          ← useApi, useNotification
│   ├── layouts/              ← default (sidebar+topbar), auth
│   ├── middleware/           ← auth.global.ts (NO usar definePageMeta)
│   ├── pages/
│   │   ├── clientes/
│   │   │   ├── index.vue               ← listado con saldo_usd. Click fila → cuenta corriente
│   │   │   └── [id]/
│   │   │       ├── index.vue           ← ficha distribuidor + fondo marketing
│   │   │       └── cuenta-corriente.vue ← movimientos, saldo acumulado, línea de crédito, notas de crédito
│   │   ├── mercaderia/
│   │   │   ├── index.vue               ← redirect a /mercaderia/stock
│   │   │   ├── stock/index.vue         ← tabs + filtros en card blanca
│   │   │   ├── catalogo/index.vue      ← tab Catálogo: editar/crear parámetros de producto
│   │   │   ├── depositos/index.vue     ← tabs
│   │   │   └── importaciones/
│   │   │       ├── index.vue, nueva.vue, [id].vue
│   │   ├── productos/
│   │   │   ├── index.vue               ← APIs Distri (+ toggle stock, botón Cargar catálogo)
│   │   │   └── importar.vue            ← wizard carga masiva de catálogo
│   │   ├── existencias/index.vue       ← Stock Distri
│   │   ├── ordenes-venta/
│   │   │   ├── index.vue               ← listado
│   │   │   ├── nueva.vue               ← crear orden con líneas dinámicas
│   │   │   └── [id].vue                ← detalle, edición, PDF, nota de crédito
│   │   └── configuracion/index.vue     ← config empresa + CRUD usuarios con permisos
│   ├── public/logos/
│   └── stores/               ← auth.ts (Pinia)
└── docker-compose.yml
```

## Sidebar — estructura de navegación

```
Principal:    Dashboard · Distribuidores · Proveedores
Operaciones:  Stock Bodega · Stock Distri · APIs Distri · Resellers · Órdenes de Venta
Marketing:    Fondos · Calendario · Tareas
Admin:        Configuración (solo admin)
```

> Inventario (Stock Bodega) = 4 tabs: **Stock · Catálogo · Depósitos · Subir Masivo** (barra duplicada en cada página).

## Modelos principales y relaciones

```
Cliente (distribuidores)
  ├── hasMany MovimientoCuenta   ← cuenta corriente
  ├── hasMany HistorialLineaCredito ← historial de cambios de línea de crédito
  ├── hasMany NotaCredito        ← notas de crédito emitidas
  ├── hasMany AsignacionFondo
  ├── hasMany AccionMarketing
  └── hasMany OrdenVenta

NotaCredito
  ├── belongsTo Cliente
  ├── belongsTo Usuario
  └── hasMany NotaCreditoItem    ← ítems de texto libre (sin FK a productos)

MovimientoCuenta
  ├── belongsTo Cliente
  ├── belongsTo Venta (nullable)
  └── belongsTo NotaCredito (nullable)

OrdenVenta
  ├── belongsTo Cliente
  ├── belongsTo Usuario
  ├── belongsTo Venta (nullable, cuando está FACTURADA)
  └── hasMany ItemOrdenVenta
        └── belongsTo Deposito (nullable)

Venta
  ├── belongsTo Cliente
  └── hasMany ItemVenta
        └── belongsTo Producto

Producto
  ├── hasMany StockDeposito
  ├── (precio_lista_1..4, codigo_distribuidor, sku)
  └── (catálogo GIGABYTE: item_no, bu_code, chipset, global_part, link, ean, carton_*)
```

## Enums

| Enum | Valores |
|------|---------|
| `RolUsuario` | ADMIN, OPERATIVO |
| `EstadoOrdenVenta` | BORRADOR, APROBADA, FACTURADA, ANULADA |
| `EstadoVenta` | PENDIENTE, PAGADA, CANCELADA |
| `TipoMovimiento` | FACTURA, PAGO, NOTA_CREDITO, AJUSTE |

## Rutas API destacadas

```
# Públicas (validación por token en controller)
GET  /api/ventas/{venta}/preview?token=...
GET  /api/notas-credito/{nota}/preview?token=...

# Clientes / cuenta corriente
GET  /api/clientes/{cliente}/cuenta-corriente
GET  /api/clientes/{cliente}/historial-credito
PATCH /api/clientes/{cliente}/linea-credito         body: { monto_usd, notas }

# Notas de crédito
GET  /api/clientes/{cliente}/notas-credito
POST /api/clientes/{cliente}/notas-credito          body: { fecha, concepto, items[] }

# Órdenes de venta
PATCH /api/ordenes-venta/{id}/aprobar
PATCH /api/ordenes-venta/{id}/anular
POST  /api/ordenes-venta/{id}/invoice

# Importaciones de stock (mercadería)
POST /api/importaciones-mercaderia/parsear          multipart: file
POST /api/importaciones-mercaderia/chequear-skus
POST /api/importaciones-mercaderia                  body: staged_id, deposito_id, mapeo

# Carga masiva de catálogo (productos, no stock)
POST /api/importaciones-catalogo/parsear            multipart: archivo
POST /api/importaciones-catalogo                    body: staged_id, mapping{item_no...}, marca, categoria
```

## Módulo Nota de Crédito — flujo

```
1. Usuario abre NC desde cuenta corriente o desde orden FACTURADA
2. Modal con ítems (texto libre) + concepto + fecha
   — Desde orden: pre-llenado con productos, editable para parciales
3. POST /api/clientes/{cliente}/notas-credito
4. Backend: crea NotaCredito + NotaCreditoItems + MovimientoCuenta (NOTA_CREDITO haber)
5. Frontend: refresca movimientos + abre preview en nueva tab
6. Preview: GET /api/notas-credito/{id}/preview?token=...
   — Blade verde, mismo estilo que invoice, descarga PDF client-side
```

## Módulo Línea de Crédito — flujo

```
1. Admin hace click en lápiz en cuenta-corriente.vue
2. Modal con monto + motivo/notas
3. PATCH /api/clientes/{cliente}/linea-credito
4. Backend: actualiza clientes.linea_credito_usd + crea historial_linea_credito
5. Frontend: actualiza cliente, refresca historial
6. Barra de utilización: saldo_usd / linea_credito_usd (roja >90%)
```

## Módulo Carga de Catálogo — flujo

```
1. /productos/importar o pestaña Catálogo → subir xlsx/csv
2. POST /api/importaciones-catalogo/parsear → guarda staged + devuelve headers/rows/campos
3. Frontend auto-mapea columnas por regex (item_no, bu_code, ean, carton_*...)
4. POST /api/importaciones-catalogo → upsert Producto por item_no
   - sku = codigo_distribuidor = item_no · nombre/modelo = global_part · marca=GIGABYTE
5. Devuelve { creados, actualizados, omitidos, errores }
```

## Patrones Frontend

### Desempaquetar respuestas API

```js
// Colección — Resource::collection devuelve { data: [], meta: {} }
const res = await api.get("/clientes")
clientes.value = res.data ?? res
paginacion.value = res.meta ?? null

// Recurso individual — Resource devuelve { data: {} }
const res = await api.get("/clientes/1")
cliente.value = res?.data ?? res
```

### authStore en script setup (no dentro de funciones)

```js
// ✓ Correcto
const authStore = useAuthStore()   // nivel de <script setup>
const puedeAprobar = computed(() => authStore.tienePermiso("aprobaciones"))
```

### Abrir preview en nueva tab

```js
window.open(`/api/ventas/${id}/preview?token=${encodeURIComponent(authStore.token)}`, "_blank")
window.open(`/api/notas-credito/${id}/preview?token=${encodeURIComponent(authStore.token)}`, "_blank")
```

### Subir archivo (FormData con token) — patrón importadores

```js
const fd = new FormData(); fd.append("archivo", file)
await $fetch(`${config.public.apiBase}/importaciones-catalogo/parsear`, {
  method: "POST", body: fd, headers: { Authorization: `Bearer ${authStore.token}` },
})
```

### Patrón de filtros — todas las páginas usan card

```html
<div class="bg-white rounded-xl border border-[#E8E8E3] p-4 flex flex-wrap gap-3 items-center">
  <!-- buscador + selects + pills -->
</div>
```

## Deploy — sin rebuild de container

```bash
# Backend
docker cp backend/app/... gigaerp-backend:/var/www/html/app/...
docker cp backend/routes/api.php gigaerp-backend:/var/www/html/routes/
docker cp backend/database/migrations/XXXX.php gigaerp-backend:/var/www/html/database/migrations/
docker exec gigaerp-backend php artisan migrate --force
docker exec gigaerp-backend php artisan route:clear
docker exec gigaerp-backend php artisan config:cache   # SIEMPRE obligatorio

# Frontend — siempre rebuild completo
docker compose build --no-cache frontend && docker compose up -d frontend
docker restart gigaerp-nginx   # SIEMPRE después de rebuild
```

> ⚠️ El `docker cp` NO instala dependencias. Si el código usa una lib nueva (ej. PhpSpreadsheet vía `maatwebsite/excel`), hay que `docker compose build backend`. Ver [[troubleshooting#8. PhpSpreadsheet no instalado en el container|troubleshooting #8]].

## Ver también

- [[gigaErp]] — índice del proyecto
- [[contexto]] — reglas de negocio, usuarios, distribuidores
- [[changelog]] — historial de cambios
- [[memoria]] — gotchas y patrones recurrentes
- [[troubleshooting]] — errores conocidos y fixes
- [[modulos/productos]] — sync partpicker + carga de catálogo GIGABYTE
- [[modulos/ordenes-venta]] — pipeline Orden → Aprobación → Invoice → Nota de Crédito

## Integración API externa — patrón proxy backend

Para APIs externas públicas (ej. partpicker), el backend actúa como proxy:
- Nunca llamar desde frontend directo (CORS, lógica expuesta)
- `Http::timeout(N)->get(URL, $params)` en el controller
- Timeouts: 15s metadata, 30-60s listados grandes
- Filtrar/validar antes de devolver al frontend

### Sincronización mayoristas

- `GET /api/sincronizar/fuentes` — mayoristas de partpicker (sin `preciosgamer_`)
- `POST /api/sincronizar/vincular-skus` — asigna `sku = strtoupper(nro_parte)` en chunk de 500
- `POST /api/sincronizar/{source}` — upsert masivo paginando 500 items; crea `Cliente` si no existe

**⚠️ Orden de rutas:** `vincular-skus` debe declararse ANTES del wildcard `{source}`.

### Resellers

- `GET /api/resellers/fuentes` — resellers con prefijo `preciosgamer_`
- `GET /api/resellers/items` — proxy con max 200 items, filtros: source, fabricante, isinstock, q

### Gotchas partpicker

- `stock` puede ser negativo (Air): `max(0, (int)$item["stock"])`
- `precio_sin_iva`, `precio_final`, `pct_iva` pueden ser null → defaults 0, 0, 21
- Resellers: precio real en `precio_convertido`, no en `precio_ars` (siempre null)
- `fabricante` = exact match case-insensitive; para LIKE usar `q`
