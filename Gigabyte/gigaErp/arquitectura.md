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
│   │   ├── migrations/       ← 0001–0044 (numeradas; 0044 = addons_marketing)
│   │   └── seeders/          ← DatabaseSeeder, DemoSeeder, ProductoInvidSeeder,
│   │                            ProductoNewBytesSeeder, CuentaCorrienteSeeder, UsuarioSeeder
│   ├── resources/views/
│   │   ├── ventas/           ← invoice.blade.php, invoice-preview.blade.php
│   │   └── notas-credito/    ← preview.blade.php
│   └── routes/api.php        ← todo dentro de auth:sanctum (excepto previews y login)
├── frontend/         ← Nuxt 3 SPA (ssr: false)
│   ├── components/
│   │   ├── ui/               ← Modal, FormField, DataTable, StatsCard, StatusBadge, Toast
│   │   ├── OrdenItems.vue    ← picker de productos para órdenes de venta
│   │   ├── GlobalSearch.vue  ← buscador del topbar
│   │   ├── NavItem.vue       ← ítem del sidebar (data-guia para el tour)
│   │   └── GuiaTour.vue      ← overlay de la guía interactiva
│   ├── composables/          ← useApi, useNotification, useGuia, useListasPrecio, useExcelExport, useHistoriaLabel, useProyectoLabel
│   ├── utils/                ← guias.ts (contenido del tour de onboarding)
│   ├── layouts/              ← default (sidebar+topbar+botón Ayuda+GuiaTour), auth
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

# Onboarding (asistente de configuración inicial)
GET  /api/onboarding/estado                         autodetecta pasos: usuarios→mercadería→precios→stock→distribuidores

# Precios (importación/exportación masiva por global_part)
POST /api/precios/importar                          body: filas[] (parseadas en navegador con SheetJS)
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

## Guía interactiva (onboarding tour)

Sistema de ayuda paso a paso por sección. Motor propio, sin librerías. Ver [[changelog#2026-06-17 — Guía interactiva]] y [[contexto#Guía interactiva — reglas|contexto]].

```
utils/guias.ts            ← contenido: guias[] por clave de ruta, pasos { titulo, texto, target?, posicion? }
composables/useGuia.ts    ← estado global (singleton módulo, patrón useNotification)
                            match de ruta por clave-prefijo más larga · localStorage de vistas
components/GuiaTour.vue    ← overlay (Teleport a body): spotlight + tooltip + navegación
layouts/default.vue       ← botón Ayuda (topbar) + auto-inicio 1ª vez + <GuiaTour/>
components/NavItem.vue     ← :data-guia="'nav-'+to" para anclar pasos al menú
```

- **Resaltado**: el paso con `target` (selector CSS) hace `scrollIntoView` + spotlight con `box-shadow: 0 0 0 9999px rgba(...)`. Sin `target`, el paso va centrado con overlay completo.
- **Persistencia**: `localStorage['gigaerp_guias_vistas']` = array de claves ya vistas. `iniciarSiPrimeraVez(path)` solo arranca si no está vista.
- **Anclajes disponibles**: `data-guia="nav-<ruta>"` (sidebar), `topbar-search`, `topbar-ayuda`.
- **Para extender**: editar solo `utils/guias.ts`; para anclar a botones de una página, agregar `data-guia` al elemento y referenciarlo en el paso (hoy los pasos de página son centrados).

## Onboarding — vaciado + asistente de configuración inicial (2026-06-23, commit `2c45e61`)

Distinto de la [[#Guía interactiva (onboarding tour)|guía interactiva]] (que es solo UI). Esto prepara el ERP para un cliente nuevo:

- **`php artisan erp:vaciar`** (`Console/Commands/VaciarErp.php`): borra datos transaccionales **conservando admin, depósitos y configuración**; evita el re-seed de boot. `/backups/` está en `.gitignore`.
- **Asistente** (`frontend/components/AsistenteInicial.vue` + `utils/onboarding.ts`, montado en `pages/index.vue`): guía el camino **usuarios → mercadería → precios → stock → distribuidores**, autodetectando cada paso vía `GET /api/onboarding/estado` (`OnboardingController`).
- **Autor de productos** (`created_by`, migración `0044`): alta manual e importación masiva graban el usuario; `ProductoResource` lo expone y el catálogo lo muestra.

## Permisos de visualización por sección (2026-06-29)

Permisos `VER_SECCION_*` por sección del sidebar, **opt-in** (admin ve todo). Reglas en [[contexto#Permisos por sección — reglas|contexto]].

- **Backend: sin cambios.** Las keys se guardan en `usuario.permisos` (array JSON ya existente, validado `nullable|array`). No hay enum ni migración.
- **`utils/secciones.ts`** (fuente única de verdad): `SECCIONES[]` con `{ key, label, to, icon, grupo, exact? }` + `permisoDeRuta(path)` (Dashboard matchea `/` exacto; el resto por prefijo del primer segmento).
- **`layouts/default.vue`**: renderiza el sidebar desde `SECCIONES` filtrando por `authStore.tienePermiso(s.key)`; agrupa por `grupo` y **oculta el encabezado de grupo si no hay ítems visibles**.
- **`middleware/secciones.global.ts`**: route guard global. Corre después de `auth.global.ts` (orden alfabético), llama `authStore.init()` defensivo, deja pasar admin / rutas públicas, y si el no-admin entra a una sección sin permiso lo manda a `primeraRutaPermitida()` (1ª de `SECCIONES` que tenga, o `/sin-acceso`). Blinda además `/configuracion` (solo admin).
- **`pages/configuracion/index.vue`**: checkboxes "Secciones visibles" reusando `togglePermiso` (las keys conviven en `permisos`), atajo "Marcar/Desmarcar todas", badges con `labelPermiso()`.
- ⚠️ **Solo frontend**: no hay enforcement de API. Para seguridad real falta middleware/policies por endpoint en el backend.

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
>
> ⚠️ Hoy el `docker compose build backend` **falla** (skeleton Laravel no resuelve), así que el backend **solo** se puede actualizar en caliente vía `docker cp` + `docker restart`. Ver [[troubleshooting#10. Rebuild limpio del backend falla (composer create-project)|troubleshooting #10]].

## Backup/restore completo (ZIP)

`BackupController` (rutas admin `GET /api/backup/generate`, `POST /api/backup/restore`). Objetivo de diseño: **un solo artefacto autosuficiente** para levantar el dataset entero en otra instancia (clonar repo → `docker compose up` → restaurar ZIP).

- **Formato:** ZIP con `ZipArchive` = `database.json` (volcado de las ~27 tablas en orden FK padres→hijos, igual que antes) + `files/…` con **todo** `storage/app/public` recursivo (adjuntos de marketing + imágenes del editor Markdown). Versión de payload `2.0`.
- **Restore idempotente y retrocompatible:** detecta ZIP (por extensión o firma `PK\x03\x04`) vs JSON viejo. DB → `SET FOREIGN_KEY_CHECKS=0` + truncate en orden inverso + insert por chunks de 500. Archivos → extrae `files/*` a `storage/app/public` con merge/overwrite y guardia anti path-traversal (`..`).
- **Storage persistente:** `storage/app/public` es un named volume (`uploads_storage`), sobrevive a rebuilds; el symlink `public/storage → storage/app/public` sirve los archivos.
- **Límites subidos para archivos pesados:** PHP `upload_max_filesize/post_max_size/memory_limit=512M` (`conf.d/uploads.ini` en el Dockerfile) y nginx `client_max_body_size 512M` + timeouts 600s en `/api/`. Los defaults (2M/8M/20M) rompían cualquier ZIP con imágenes.

Detalle de reglas en [[contexto#Backup/restore — reglas|contexto]] · registro en [[changelog#2026-07-02 — Backup/restore completo en ZIP (datos + archivos)|changelog]].

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

