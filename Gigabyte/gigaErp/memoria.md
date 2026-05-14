# Memoria — gigaErp

Consolidación de la memoria de Claude para este proyecto. Sincronizado 2026-05-14.

---

## Contexto rápido

**gigaErp** — sistema interno Gigabyte (hardware IT) en `http://10.10.10.7:8824`.

| Email | Pass | Rol |
|-------|------|-----|
| `admin@gigabyte.com` | `admin123` | ADMIN |
| `maria.gomez@gigabyte.com` | `demo1234` | OPERATIVO |
| `lucas.herrera@gigabyte.com` | `demo1234` | OPERATIVO |

**Distribuidores**: Elit (GBA $50k), New Bytes (Córdoba $40k), Invid (Mendoza $35k), Air (Rosario $30k)
**Proveedores**: Blu Studio · Imprenta Gráfica Sur · Logística Rápida SA · Tech Events SRL · Media Digital Pro

---

## Convenciones críticas frontend

| Situación | ✅ Correcto | ❌ Incorrecto |
|-----------|------------|--------------|
| Respuesta con Resource | `res?.data ?? res` | `res` directo |
| Colección paginada | `res.data` + `res.meta` | — |
| Colección sin paginar (`get()`) | `res.data ?? res` | `res.data` |
| Errores en catch | `e.message` | `e?.data?.message` |
| DELETE con body | `api.delete(url, { data: {} })` | `{ body: {} }` |
| Middleware auth | global automático | `definePageMeta({ middleware: 'auth' })` |
| Íconos | `lucide:search` | `search` |
| Componentes UI | `<FormField>` | `<UiFormField>` |
| Modal | `v-model="show"` | `v-if` + `@close` |

## Convenciones críticas backend

- `config('x')` nunca `env('X')` — PHP-FPM no lee env vars sin config:cache
- `$table` explícito en `Proveedor` → `proveedores` y `Configuracion` → `configuraciones`
- Rutas estáticas **antes** del `apiResource` en `routes/api.php`
- Enums: `EstadoTarea::LISTO`, nunca `'LISTO'` string
- Al crear `apiResource` en español: verificar `route:list` que `{param}` coincida
- `->keyBy('estado')` falla con enum cast → usar `->keyBy(fn($v) => $v->estado->value)`

---

## apiResource — bug de pluralización española

Síntoma: Resource devuelve todo `null`, sin 404 ni 500.
Diagnóstico: `php artisan route:list --path=api/X` + curl con token.

| Recurso | Generado | Correcto | Fix |
|---------|---------|---------|-----|
| `acciones` | `{accione}` | `{accion}` | `.parameters(['acciones' => 'accion'])` |
| `proveedores` | `{proveedore}` | `{proveedor}` | `.parameters(['proveedores' => 'proveedor'])` |

---

## Paginación vs colección por módulo

| Controller | Método | Leer en frontend |
|-----------|--------|-----------------|
| Clientes, Ventas, Acciones, Productos | `paginate(20)` | `res.data` + `res.meta` |
| Tareas, Etiquetas, Tipos, Estados | `get()` | `res.data ?? res` |

---

## TareaResource / AccionMarketingResource — relaciones por endpoint

**Tarea:**
- `index()`: `cliente`, `proveedor`, `asignadoUsuario`, `etiquetas` — sin `creadoPor`
- `show()`: todo + `asignadoProveedor`, `accion`, `creadoPor`

**AccionMarketing:**
- `index()`: `cliente`, `tipo`, `estado`, `campana`, `creadoPor`
- `show()`: todo + `adjuntos`, `tareas`

---

## Dashboard — GET /api/dashboard

```json
{
  "kpis": { "clientes_activos", "ingresos_mes", "gastos_mes", "resultado_mes", "margen_pct", "ticket_promedio", ... },
  "ventas_por_estado": { "PAGADA": {cantidad, total}, "PENDIENTE": {...}, "CANCELADA": {...}, "total": N },
  "top_clientes": [{ "id", "nombre", "total_ventas" }],
  "ultimos_12_meses": [{ "label", "mes", "anio", "ingresos", "gastos" }]
}
```

- ingresos = ventas PAGADAS · gastos = AccionMarketing.monto_usd

## Pixel Bar Chart — parámetros validados

```ts
PX_SIZE = 5  // ← barW DEBE igualar PX_SIZE para que sean cuadrados
PX_GAP  = 2  // gap vertical entre cuadraditos
CHART_H = 140
MAX_PX  = 20 // filas
// viewBox "0 0 770 {CHART_H+26}", slot 60px/mes
// ingresos: i*60+23, gastos: i*60+31
// font-size SVG: 6 (escala con viewBox)
```

## Branding

```html
<!-- Sidebar logo (layouts/default.vue) -->
<img src="/logos/aorus_logo_black.svg" class="h-8 w-auto" />
<!-- Topbar -->
<span class="text-sm text-[#9B9B93]">Brand ERP</span>
```

---

## Kanban — comportamiento actual

- Drag & drop HTML5 nativo (sin libs externas)
- Click → `GET /tareas/{id}` → modal 2xl estilo Jira
- Anti-conflicto: `draggingId` con `setTimeout 50ms` en `onDragEnd`

---

## Endpoints no obvios

| Endpoint | Descripción |
|----------|-------------|
| `GET /clientes/{id}/fondo?anio=2026` | `{ resumen: { asignado, consumido, disponible } }` |
| `PUT /stock/{producto}/{deposito}` | `{ cantidad: N }` — setea absoluto |
| `PATCH /tareas/{id}/estado` | `{ estado: 'EN_CURSO' }` |
| `GET /tareas` | sin paginación — `{ data: [] }` sin `meta` |

---

## Debugging — checklist "página carga vacía"

1. `curl http://10.10.10.7:8824/api/X/1 -H "Authorization: Bearer TOKEN"` — ver si devuelve datos
2. Si todo `null` → model binding roto → `route:list --path=api/X` → verificar `{param}`
3. Si 500 → `docker exec gigaerp-backend tail -100 storage/logs/laravel.log | grep ERROR`
4. Si datos OK pero UI vacía → frontend no desenvolve `{ data: {} }` → usar `res?.data ?? res`
5. Si `Connection: sqlite` → `docker exec gigaerp-backend php artisan config:cache`

## Token para debugging

```bash
docker exec gigaerp-backend php artisan tinker --execute="echo App\Models\Usuario::find(1)->createToken('test')->plainTextToken;"
```

---

## Deploy sin rebuild de frontend

```bash
# Backend
docker cp backend/app/Http/Controllers/X.php gigaerp-backend:/var/www/html/app/Http/Controllers/
docker exec gigaerp-backend php artisan optimize:clear && docker exec gigaerp-backend php artisan config:cache

# Frontend (SIEMPRE rebuild)
docker compose build --no-cache frontend && docker compose up -d frontend && docker restart gigaerp-nginx
```

---

## TODOs pendientes

- [ ] Export Excel/PDF (libs instaladas, stubs 501)
- [ ] Detalle + formulario nueva venta con items
- [ ] Asignación de fondo desde panel cliente
- [ ] Permisos granulares en sidebar
- [ ] Git repo + backups DB

---

## Ver también

- [[gigaErp]] · [[arquitectura]] · [[contexto]] · [[stack]] · [[changelog]]
