# Arquitectura — gigaErp

## Estructura de directorios

```
gigaErp/
├── backend/          ← Laravel 11 (PHP 8.4)
│   ├── app/
│   │   ├── Enums/            ← RolUsuario, EstadoTarea, EstadoVenta, EstadoOrdenVenta, TipoMovimiento
│   │   ├── Http/Controllers/ ← ~24 controllers
│   │   ├── Http/Resources/   ← 9 API resources
│   │   ├── Models/           ← ~24 Eloquent models
│   │   └── (no Services aún)
│   ├── database/
│   │   ├── migrations/       ← 0001–0033 (numeradas)
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
│   │   │   ├── depositos/index.vue     ← tabs
│   │   │   └── importaciones/
│   │   │       ├── index.vue, nueva.vue, [id].vue
│   │   ├── productos/index.vue         ← APIs Distri
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
Operaciones:  Stock Bodega · Stock Distri · APIs Distri · Órdenes de Venta
Marketing:    Fondos · Calendario · Tareas
Admin:        Configuración (solo admin)
```

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
  └── (precio_lista_1..4, codigo_distribuidor, sku)
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

# Importaciones
POST /api/importaciones-mercaderia/parsear          multipart: file
POST /api/importaciones-mercaderia/chequear-skus
POST /api/importaciones-mercaderia                  body: staged_id, deposito_id, mapeo
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

## Ver también

- [[gigaErp]] — índice del proyecto
- [[contexto]] — reglas de negocio, usuarios, distribuidores
- [[changelog]] — historial de cambios
- [[memoria]] — gotchas y patrones recurrentes
- [[troubleshooting]] — errores conocidos y fixes
- [[modulos/ordenes-venta]] — pipeline Orden → Aprobación → Invoice → Nota de Crédito