# Memoria — gigaErp

Patrones recurrentes, gotchas y workflow del proyecto. Consultar antes de cada sesión.

---

## Gotchas críticos (errores que ya pasaron)

### 1. `optimize:clear` rompe la conexión a DB

**Síntoma:** Backend devuelve 500 "no such table" o `Connection: sqlite`.
**Causa:** `optimize:clear` borra el config cache; en PHP-FPM `env()` no lee el `.env`.
**Fix:** Siempre correr `php artisan config:cache` después de cualquier `optimize:clear`.

### 2. Nginx 502 después de rebuild

**Síntoma:** 502 Bad Gateway en cualquier request.
**Causa:** Nginx cachea la IP del upstream cuando levanta; rebuild cambia la IP del container.
**Fix:** `docker restart gigaerp-nginx` — obligatorio después de CUALQUIER rebuild de container.

### 3. `migrate` falla con "Table personal_access_tokens already exists"

**Causa:** El entrypoint del container republica la migración de Sanctum en cada boot.
**Fix:** `docker exec gigaerp-backend sh -c "rm -f database/migrations/*_create_personal_access_tokens_table.php"` antes de migrar.

### 4. Logo recortado en PDF (html2canvas + SVG con viewBox)

**Síntoma:** Logo bien en HTML, recortado en el PDF generado.
**Causa:** html2canvas no respeta `viewBox` con offset en SVG.
**Fix:** Usar PNG como data URI base64 en lugar del SVG.

### 5. Asset nuevo en `frontend/public/` no se sirve

**Causa:** Nitro tiene manifest de assets en build time — no detecta archivos nuevos sin rebuild.
**Fix:** Rebuild del container frontend, o embeber en backend.

### 6. Enum en `->keyBy()` — Object could not be converted to string

**Síntoma:** Error "Object of class App\Enums\X could not be converted to string".
**Causa:** `->get()->keyBy("estado")` en modelos con cast a enum — PHP no convierte enum a string.
**Fix:**
```php
// ❌ Falla
->get()->keyBy("estado")

// ✅ Correcto
->get()->keyBy(fn($v) => $v->estado->value)
```

---

## Workflow de deploy (sin rebuild)

```bash
# 1. Copiar archivos modificados
docker cp backend/app/Http/Controllers/FooController.php gigaerp-backend:/var/www/html/app/Http/Controllers/
docker cp backend/routes/api.php gigaerp-backend:/var/www/html/routes/

# 2. Si hay migraciones
docker exec gigaerp-backend php artisan migrate --force

# 3. SIEMPRE al final
docker exec gigaerp-backend php artisan config:cache

# 4. Si tocaste routes
docker exec gigaerp-backend php artisan route:clear
```

**Frontend — siempre rebuild completo:**
```bash
docker compose build --no-cache frontend && docker compose up -d frontend && docker restart gigaerp-nginx
```

---

## Checklist "página vacía / datos no cargan"

1. Abrir DevTools → Network → ver si el request API falla
2. Testear el endpoint directo: `curl -s -H "Authorization: Bearer TOKEN" http://localhost:8824/api/endpoint`
3. Si falla con sqlite → `php artisan config:cache`
4. Si 502 → `docker restart gigaerp-nginx`
5. Si datos son `null` sin error → verificar wrapper Resource (`res?.data ?? res`)
6. Si colección paginada → usar `res.data` + `res.meta`, NO `res` directamente

---

## Patrones UI recurrentes

### KPI card
```html
<div class="bg-white rounded-xl border border-[#E8E8E3] p-5">
  <p class="text-[11px] font-medium font-mono tracking-[0.08em] uppercase text-[#8B8B83]">LABEL</p>
  <p class="text-[32px] font-semibold tracking-tight tabular-nums mt-2 leading-none">VALOR</p>
  <p class="text-[12px] text-[#9B9B93] mt-2">sublabel</p>
</div>
```

### Filtros — card blanca obligatoria
```html
<div class="bg-white rounded-xl border border-[#E8E8E3] p-4 flex flex-wrap gap-3 items-center">
  <!-- buscador con bg-[#F8F8F5] -->
</div>
```

### Dashboard pixel bar chart (parámetros validados)
```ts
PX_SIZE=5, PX_GAP=2, CHART_H=140, MAX_PX=20
barW debe IGUALAR PX_SIZE (si no, los píxeles son rectangulares)
Ingresos: fill=#1A1A1A  empty=#EBEBEB
Gastos:   fill=#C0392B  empty=#F5E8E8
```

### Layout dashboard (pages/index.vue)
```
Row 1-2: 6 KPI cards (grid-cols-3)
Row 3:   Pixel bar chart 12 meses (full width)
Row 4:   Tareas por estado  |  Próximos 14 días (calendario)
Row 5:   Últimas 8 OV       |  Cuentas corrientes / top deudores
Row 6:   Resultado período  |  Ventas por estado + Top clientes
Row 7:   Productos por distribuidor (full width)
```

---

## Patrones backend recurrentes

### Nunca `env()` — siempre `config()`
PHP-FPM no hereda variables de entorno sin config cache.

### Rutas estáticas ANTES del apiResource
```php
Route::get(/tareas/export, ...);  // ANTES
Route::apiResource(tareas, ...);  // DESPUÉS
```

### `$table` explícito en modelos con nombres españoles
```php
protected $table = ordenes_venta;  // Eloquent no sabe pluralizar bien en español
```

### Validación SKU única por distribuidor
```php
"unique:productos,sku,{$id},id,distribuidor_id,{$distribuidorId}"
```

---

## Ver también

- [[gigaErp]] — índice del proyecto
- [[arquitectura]] — estructura técnica completa
- [[contexto]] — reglas de negocio
- [[troubleshooting]] — errores conocidos con más detalle
