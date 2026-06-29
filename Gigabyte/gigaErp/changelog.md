## 2026-06-29 — Permisos de visualización por sección (sidebar + bloqueo de ruta)

Cada sección del ERP pasa a tener su permiso `VER_SECCION_*`. **Semántica opt-in**: un no-admin solo ve una sección si tiene su permiso; **el admin ve todo**. Detalle en [[arquitectura#Permisos de visualización por sección|arquitectura]] y [[contexto#Permisos por sección — reglas|contexto]].

### Backend — sin cambios
El array `permisos` (`usuarios.permisos`, cast `array`) ya aceptaba strings arbitrarios y `UsuarioController@{store,update}` lo valida como `nullable|array`. Las keys `VER_SECCION_*` se guardan ahí mismo junto a `aprobaciones`/`VER_MONTOS`. **Sin enum ni migración.**

### Frontend
- **`utils/secciones.ts`** (nuevo) — fuente única de verdad: `SECCIONES[]` (key, label, ruta, ícono, grupo) + `permisoDeRuta(path)`. Las 13 secciones: Dashboard, Distribuidores, Proveedores, Stock Bodega, Stock Distri, APIs Distri, Resellers, Órdenes de Venta, Notas de Crédito, Fondos, Calendario, Proyectos, Tareas.
- **`middleware/secciones.global.ts`** (nuevo) — bloquea el acceso directo por URL; si falta el permiso redirige a la primera sección permitida (o `/sin-acceso`). Blinda también `/configuracion` (solo admin). Corre después de `auth.global.ts`.
- **`pages/sin-acceso.vue`** (nuevo) — landing para usuarios sin ninguna sección.
- **`layouts/default.vue`** — sidebar generado desde `SECCIONES`, agrupado, oculta encabezados de grupo vacíos (reemplaza los `v-if puedeVer()` parciales anteriores).
- **`pages/configuracion/index.vue`** — checkboxes "Secciones visibles" por usuario (reusa `togglePermiso`, las keys viven en el mismo array `permisos`), atajo "Marcar/Desmarcar todas", badges legibles.
- **Seeders** (`UsuarioSeeder`, `DemoSeeder`) — operativos demo con secciones para no romper la demo bajo opt-in; se corrigieron claves viejas (`VER_SECCION_ACCIONES`→`CALENDARIO`, `VER_SECCION_VENTAS`→`ORDENES`).

⚠️ **El bloqueo es solo de frontend** (sidebar + route guard). Los endpoints siguen abiertos a cualquier usuario autenticado — para rechazo real falta agregar policies por endpoint en el backend.

**Archivos:** `frontend/utils/secciones.ts` (nuevo), `frontend/middleware/secciones.global.ts` (nuevo), `frontend/pages/sin-acceso.vue` (nuevo), `frontend/layouts/default.vue`, `frontend/pages/configuracion/index.vue`, `backend/database/seeders/{UsuarioSeeder,DemoSeeder}.php`.

---

## 2026-06-23 — Filtro de stock por origen, onboarding/vaciado, e importaciones con peso

### Filtro `con_stock`/`sin_stock` ahora contempla stock de terceros (commit `72268f7`)
El filtro de stock en `ProductoController@index` solo miraba `stock_deposito`, que únicamente existe para productos propios. Los productos de **terceros** (distribuidores con API / Resellers) guardan su disponibilidad en la columna `productos.stock` (la sincroniza [[modulos/resellers|SincronizarApiController]] desde el mayorista) y **nunca tienen filas en `stock_deposito`** → con el filtro viejo, `con_stock` los excluía a todos y `sin_stock` los incluía a todos.

Ahora el filtro **ramifica por origen** (un `where(fn)` con dos sub-`where` unidos por `orWhere`):
- **Propios** (`distribuidor_id IS NULL`): por `stock_deposito.cantidad > 0` en depósito NO ilimitado (igual que antes; la columna global `productos.stock` no cuenta).
- **Terceros** (`distribuidor_id NOT NULL`): `con_stock` = `stock > 0`; `sin_stock` = `stock <= 0 OR stock IS NULL`.

Matiz importante: la columna `productos.stock` es basura del import **para los propios**, pero es la fuente de verdad **para los terceros**. Ver [[contexto#Reglas de stock|contexto]].

Precursor relacionado (commit `320a645`, 2026-06-16): `precios()` ahora filtra `whereNull(distribuidor_id) + whereHas(stocks)` para listar/exportar **solo internos con inventario real**, excluyendo los ~1800 productos sin distribuidor y sin stock (basura del import).

### Onboarding: vaciado de ERP, asistente inicial y autor de productos (commit `2c45e61`)
Prepara el ERP para entregarlo a un cliente nuevo desde cero.
- **`php artisan erp:vaciar`** (`Console/Commands/VaciarErp.php`): deja la base limpia conservando **admin, depósitos y configuración**; evita el re-seed de boot. Ignora `/backups/` en git (dumps de base).
- **Asistente de configuración inicial** en el dashboard (`components/AsistenteInicial.vue` + `utils/onboarding.ts`): guía el camino **usuarios → mercadería → precios → stock → distribuidores**, con autodetección de cada paso vía `GET /api/onboarding/estado` (`OnboardingController`).
- **Autor de productos** (`created_by`, migración `0044`): alta manual e importación masiva registran el usuario; se muestra en el catálogo. `ProductoResource` expone el campo.

**Archivos:** `Console/Commands/VaciarErp.php` (nuevo), `OnboardingController.php` (nuevo), `frontend/components/AsistenteInicial.vue` (nuevo), `frontend/utils/onboarding.ts` (nuevo), migración `0044`, `Producto.php`, `ProductoResource.php`, `ImportacionCatalogoController.php`, `frontend/pages/{index,mercaderia/catalogo}`, `routes/api.php`.

### Importaciones de mercadería: cartón, qty y kg por ítem (commit `e9ec075`)
Columnas `carton`/`qty`/`kg` por ítem de importación y totales de cabecera (`total_carton`/`total_qty`/`total_kg`), con captura en el wizard de importación y la vista de detalle.

**Archivos:** `ImportacionMercaderiaController.php`, `Models/{ImportacionMercaderia,ItemImportacionMercaderia}.php`, migración `add_carton_qty_kg_to_importaciones_mercaderia`, `frontend/pages/mercaderia/importaciones/{nueva,[id],index}.vue`.

---

## 2026-06-17 — Guía interactiva / tour de onboarding por sección

Sistema de **ayuda paso a paso** que se activa en cada sección del ERP. Sin dependencias externas — motor propio. Detalle en [[arquitectura#Guía interactiva (onboarding tour)|arquitectura]] y [[contexto#Guía interactiva — reglas|contexto]]. *(En working tree, sin commit aún.)*

### Cómo funciona
- **Botón "Ayuda"** (`lucide:circle-help`) en el topbar → arranca la guía de la sección actual. Solo aparece si hay guía para esa ruta.
- **Auto-inicio**: la primera vez que se visita una sección, la guía salta sola. Una vez cerrada queda marcada como vista en `localStorage` (key `gigaerp_guias_vistas`) y no vuelve a saltar.
- Cada paso resalta un elemento real con *spotlight* (`box-shadow: 0 0 0 9999px`) + tooltip, o se muestra centrado si no hay `target`.
- Navegación: Anterior / Siguiente / Finalizar, puntitos de progreso clickeables, contador "X de N", atajos de teclado (→/Enter, ←, Esc).

### Piezas (todo en `frontend/`)
- `utils/guias.ts` (nuevo) — contenido por sección. `guias: GuiaSeccion[]`, cada una `{ clave, titulo, pasos[] }`. `PasoGuia = { titulo, texto, target?, posicion? }`. `target` = selector CSS; sin él, paso centrado.
- `composables/useGuia.ts` (nuevo) — estado global singleton (patrón `useNotification`). Match de ruta por la clave-prefijo más larga. `localStorage` de vistas. Expone `iniciar`, `iniciarSiPrimeraVez`, `siguiente`, `anterior`, `irA`, `cerrar`, `hayGuia`.
- `components/GuiaTour.vue` (nuevo) — overlay con `<Teleport to="body">`, spotlight + tooltip, recálculo en resize/scroll.
- `layouts/default.vue` — botón Ayuda en topbar, auto-inicio (`onMounted` + `watch(route.path)`), `<GuiaTour />` montado.
- `components/NavItem.vue` — `:data-guia="'nav-' + to"` para anclar pasos a los ítems del menú.

### Anclajes `data-guia` disponibles
`nav-<ruta>` (cada ítem del sidebar), `topbar-search`, `topbar-ayuda`.

### Para extender
Editar solo `utils/guias.ts`. Para anclar a un botón de página, agregar `data-guia="..."` al elemento y referenciarlo en el paso. Hoy los pasos de página son centrados (no se tocaron las páginas); solo los de menú están anclados.

**Archivos:** `frontend/utils/guias.ts` (nuevo), `frontend/composables/useGuia.ts` (nuevo), `frontend/components/GuiaTour.vue` (nuevo), `frontend/layouts/default.vue`, `frontend/components/NavItem.vue`

---

## 2026-06-16 — Listas de precio: nombres, default por cliente, permisos por usuario

Tres features sobre las 4 listas de precio (`productos.precio_lista_1..4`). Detalle en [[contexto#Listas de precio — reglas|contexto]].

### Nombres configurables de listas (commit `cfa87c1`)
- Se guardan en la tabla `configuraciones` (claves `nombre_lista_1..4`) vía `/api/config` — sin migración ni tabla nueva.
- Composable `frontend/composables/useListasPrecio.ts`: cachea nombres en `useState` y expone `labelLista(n)` → "Lista N · Nombre" (fallback "Lista N").
- Se editan en Configuración → pestaña "Listas de precio". Se muestran en OrdenItems, stock, precios y edición de productos.

### Lista de precio por defecto del cliente (commit `b1dd6f4`)
- Migración `0042`: `clientes.lista_precio_defecto` (tinyint nullable).
- Al armar orden, los ítems entran con la lista preasignada del cliente (overrideable por ítem). `OrdenItems` recibe prop `cliente`.
- Selector en la edición del cliente (con nombres de lista).

### Permisos de lista por usuario (commit `c33be1e`)
- Migración `0043`: `usuarios.listas_precio` (JSON). **Admin = todas; no-admin = exactamente las asignadas; vacío/null = todas** (no bloquea).
- `Usuario::listasPermitidas()`; `UsuarioResource` expone `listas_precio` (cruda) y `listas_permitidas` (efectiva).
- Checkboxes por lista en Configuración → Usuarios. Los selectores muestran solo las listas permitidas; la lista inicial respeta permisos.
- `OrdenVentaController::validar()` rechaza con 422 si un no-admin manda una lista no permitida.
- ⚠️ Un usuario ya logueado no ve sus nuevas restricciones hasta re-login (front cachea `usuario`); el backend sí las aplica siempre.

### Importación masiva de precios por global_part (commit `554527a`)
- Botón **Importar** en Mercadería → Precios (junto al export existente). Flujo: exportar `.xlsx` → editar → re-importar.
- **El archivo se parsea en el navegador** con SheetJS (misma librería del export) y se mandan las filas como JSON → esquiva que el container NO tenga PhpSpreadsheet. Funciona `.xlsx` y `.csv`.
- Detección tolerante de columnas: `Global Part` + `Lista N` (aunque el header tenga el nombre, ej. "Lista 1 · Mayorista"). Solo actualiza las columnas de lista con valor; las vacías quedan igual.
- Backend `POST /api/precios/importar` (`ProductoController@importarPrecios`): update por `global_part` sobre productos propios. Devuelve `{ actualizados, productos_afectados, omitidos, errores }`. Sin migración.

**Archivos:** `migrations/0042,0043`, `Cliente.php`, `Usuario.php`, `Cliente/UsuarioResource.php`, `Cliente/Usuario/OrdenVentaController.php`, `frontend/composables/useListasPrecio.ts` (nuevo), `frontend/pages/{clientes,configuracion,mercaderia/{stock,precios},productos,ordenes-venta/{nueva,[id]}}`, `components/OrdenItems.vue`

---

## 2026-06-16 — Depósito con stock ilimitado + reglas de catálogo/stock propio

Sesión de trabajo sobre depósitos, stock y qué entra en Catálogo / Stock Bodega. Detalle en [[contexto#Stock y depósitos — reglas|contexto]].

### Depósito "Stock Ilimitado" (migración `0041`)

Nueva columna `depositos.stock_ilimitado` (boolean default false). Al armar una orden o pre-orden con un depósito ilimitado se puede poner **cualquier cantidad**, sin tope de stock.

- Backend: `Deposito` (fillable + cast), `DepositoController` (validación en store/update). El endpoint `/depositos` ya devuelve el flag.
- Frontend Depósitos: checkbox "Stock ilimitado" en el modal + badge ∞ en la card.
- `OrdenItems.vue`: si el depósito es ilimitado libera el tope de cantidad, permite agregar aunque el stock sea 0, lo incluye siempre en el selector y muestra **∞**.
- Stock Bodega: la columna de un depósito ilimitado muestra ícono `lucide:infinity`.
- ⚠️ El backend HOY no descuenta ni valida stock en ningún momento — el tope real solo lo imponía el frontend, que es lo que el flag libera.
- Fix (`8a9eee5`): en Stock Bodega el `+` del pedido estaba deshabilitado para productos sin stock físico. `depositoDe` ahora cae al depósito ilimitado si no hay stock real y `maxStock` devuelve `Infinity`, habilitando el stepper sin tope → se pueden agregar al pedido los productos disponibles por depósito infinito.

### Definición de "producto propio" y filtro de stock por depósito

- **Producto propio = `distribuidor_id IS NULL`** (creado a mano o por carga masiva de catálogo). Los productos con distribuidor van a Stock Distri / APIs Distri / Resellers y NO se mezclan.
- **Catálogo** (`solo_catalogo`) y **Stock Bodega** (`solo_inventario`) ahora filtran `whereNull('distribuidor_id')` — muestran TODOS los propios, tengan o no stock. La disponibilidad la maneja el filtro de stock, no la membresía.
- Se agregaron pestañas **Todos / Con stock / Sin stock** a la pantalla Catálogo.
- **Filtro de stock 100% basado en `stock_deposito`**, NO en la columna global `productos.stock` (basura del import: `StockController@update` solo toca `stock_deposito`, nunca la columna global):
  - `con_stock` = existe `stock_deposito.cantidad > 0` en un depósito **no** ilimitado.
  - `sin_stock` = negación exacta (sin filas, todo en 0, o solo en depósito ilimitado).
  - **Depósito ilimitado NO cuenta como "con stock"** (el infinito no es stock real).

### Quirk de datos detectado

~1819 productos propios pero solo **12 con inventario real** (seedeados GIGABYTE, codigo_distribuidor `GB-*`); los otros ~1807 entraron sin distribuidor pero sin filas de stock. Quedan visibles en Catálogo bajo "Sin stock"/"Todos". Pendiente decidir limpieza. Ver [[contexto#TODOs pendientes]].

**Archivos:** `backend/database/migrations/0041_add_stock_ilimitado_to_depositos_table.php` (nuevo), `app/Models/Deposito.php`, `app/Http/Controllers/DepositoController.php`, `app/Http/Controllers/ProductoController.php`, `frontend/components/OrdenItems.vue`, `frontend/pages/mercaderia/depositos/index.vue`, `frontend/pages/mercaderia/stock/index.vue`, `frontend/pages/mercaderia/catalogo/index.vue`

---

## 2026-06-11 — Carga masiva y edición de catálogo GIGABYTE

Pedido del contacto de GIGABYTE (mail): poder cargar la base de productos con campos propios del catálogo (sin stock) y cruzar el stock después.

### Campos de catálogo en `productos` (migración `0040`)

Nuevas columnas: `bu_code`, `chipset`, `item_no`, `global_part`, `link`, `ean`, `carton_box_qty`, `carton_peso_kg`, `carton_largo_mm`, `carton_ancho_mm`, `carton_alto_mm`. **UPC NO se usa** (explícito en el mail).

**Convención clave:** en el catálogo GIGABYTE `sku` = `codigo_distribuidor` = **ITEM NO**, `nombre`/`modelo` = Global Part, `marca`=GIGABYTE, `distribuidor_id`=null. Así el importador de stock de mercadería existente (matchea por sku/codigo_distribuidor) cruza el stock por ese código sin cambios.

### Importador masivo de catálogo (`ImportacionCatalogoController`)

- `POST /api/importaciones-catalogo/parsear` — sube xlsx/csv, devuelve headers + filas + campos mapeables
- `POST /api/importaciones-catalogo` — **upsert** de productos por `item_no` (crea/actualiza, no duplica); devuelve `{creados, actualizados, omitidos, errores}`
- Parseo **CSV nativo** (`fgetcsv`, detecta delimitador `, ; \t`) + xlsx vía PhpSpreadsheet si está disponible

### Frontend

- `/productos/importar` — wizard subir → mapear (auto-detecta las columnas del mail) → resultado. Botón "Cargar catálogo" en `/productos`.
- Toggle **"Mostrar stock"** en la lista de productos (oculta columna + badge en grid/lista).
- Bloque "Datos de catálogo" en el modal de detalle del producto.
- **Pestaña Catálogo** en Inventario (`/mercaderia/catalogo`), junto a Stock · Depósitos · Subir Masivo — listar / editar / crear productos con todos los parámetros del catálogo. ITEM NO se mantiene sincronizado con SKU al guardar.

### Gotchas resueltos

- `$request->validate()` con reglas anidadas (solo `mapping.item_no`) devuelve **únicamente las claves validadas** del array → se perdían los demás mapeos. Fix: `'mapping.*' => 'nullable|integer|min:0'`.
- `productos.codigo_distribuidor` es NOT NULL sin default → al crear, setear = item_no.
- **PhpSpreadsheet no está instalado en el container** (imagen vieja; `maatwebsite/excel` figura en composer.json pero nunca corrió `composer install`) → rompe el parseo xlsx en AMBOS importadores (catálogo y mercadería). CSV anda; para habilitar xlsx falta `docker compose build backend`. Ver [[troubleshooting#8. PhpSpreadsheet no instalado en el container|troubleshooting]].

**Commit:** `d08b3a4`
**Archivos:** `backend/app/Http/Controllers/ImportacionCatalogoController.php` (nuevo), `Producto.php`, `ProductoController.php`, `ProductoResource.php`, `database/migrations/0040_add_catalogo_campos_to_productos_table.php`, `routes/api.php`, `frontend/pages/productos/importar.vue` (nuevo), `frontend/pages/mercaderia/catalogo/index.vue` (nuevo), `productos/index.vue`, tabs en `mercaderia/{stock,depositos,importaciones}`

---

## 2026-06-04 — Integración partpicker + módulo Resellers

### Integración real con API partpicker (`SincronizarApiController`)

Reemplazó la simulación del botón "Sincronizar APIs" por integración real con `https://partpicker.blustudioinc.com`.

**Fuentes mayoristas disponibles:** Air (8368 items), Ceven (466), Invid (1203), Stylus (908).

Flujo de sincronización desde el modal en `/productos`:
1. `GET /api/sincronizar/fuentes` — lista fuentes mayoristas (sin prefijo `preciosgamer_`)
2. Por cada fuente: `POST /api/sincronizar/{source}` — upsert masivo paginando 500 items
   - Crea el `Cliente` (distribuidor) si no existe
   - Upsert por `(distribuidor_id, codigo_distribuidor)`
   - Mapea: `nro_parte → modelo`, `precio_sin_iva → precio_usd`, `stock → stock`
3. `POST /api/sincronizar/vincular-skus` — asigna `sku = strtoupper(trim(modelo))` a todos los productos sin SKU; habilita agrupación en Stock Distri

**Gotchas resueltos en esta sesión:**
- `stock` puede venir negativo (`-1`) → `max(0, (int)$item["stock"])`
- `precio_sin_iva`, `precio_final`, `pct_iva` pueden ser null → defaults `0, 0, 21`
- Ruta `vincular-skus` debe declararse **antes** del wildcard `{source}` en routes/api.php

**Distribuidores nuevos en DB:** Ceven (id=5), Stylus (id=6) — creados al primer sync.

**Commit:** `b7c7377`
**Archivos:** `backend/app/Http/Controllers/SincronizarApiController.php` (nuevo), `backend/routes/api.php`

---

### Módulo Resellers (`ResellersController` + `/resellers`)

Nueva sección que muestra productos de resellers (37 tiendas vía PreciosGamer) directamente desde la API, sin importar a la DB.

- `GET /api/resellers/fuentes` — lista resellers (fuentes con prefijo `preciosgamer_`)
- `GET /api/resellers/items` — proxy a partpicker con filtros: source, fabricante, isinstock, q, limit/offset

**Frontend `/resellers`:** tabla live con imagen, nombre, link a ficha, nro_parte, marca, categoría, precio ARS (`precio_convertido`, no `precio_ars` que siempre es null), badge de stock. Paginación 50 en 50.

**Sidebar:** "Resellers" agregado debajo de "APIs Distri" en sección Operaciones.

**Archivos:** `backend/app/Http/Controllers/ResellersController.php` (nuevo), `frontend/pages/resellers/index.vue` (nuevo), `frontend/layouts/default.vue`

---

### Filtro de marca con default GIGABYTE

Agregado en tres secciones:
- **APIs Distri** (`/productos`): input marca, `filtroMarca = "GIGABYTE"`, param `?marca=` → `WHERE marca LIKE "%X%"`
- **Stock Distri** (`/existencias`): ídem, param `?marca=` en `ExistenciaController`
- **Resellers** (`/resellers`): input marca, `filtroMarca = "GIGABYTE"`, param `?fabricante=` → exact match case-insensitive en partpicker

El filtro se puede borrar para ver todas las marcas.

**Archivos:** `backend/app/Http/Controllers/ProductoController.php`, `backend/app/Http/Controllers/ExistenciaController.php`, `frontend/pages/productos/index.vue`, `frontend/pages/existencias/index.vue`

---
