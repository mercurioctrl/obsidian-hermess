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
