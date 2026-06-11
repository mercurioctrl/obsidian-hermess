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
