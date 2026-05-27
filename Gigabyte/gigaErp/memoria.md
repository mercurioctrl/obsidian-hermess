# Memoria — gigaErp

Consolidación de la memoria de Claude para este proyecto. Sincronizado **2026-05-27**.

Vive en `~/.claude/projects/-var-www-gigabyte-gigaErp/memory/` — esta nota es el espejo.

---

## Contexto rápido

**gigaErp** — sistema interno Gigabyte (hardware IT) en `http://localhost:8824`.

| Email | Pass | Rol | Permisos |
|-------|------|-----|----------|
| `admin@gigabyte.com` | `admin123` | ADMIN | todos |
| `carolina.lagos@gigabyte.com` | `demo1234` | OPERATIVO | aprobaciones + VER_MONTOS |
| `martin.fierro@gigabyte.com` | `demo1234` | OPERATIVO | VER_MONTOS |
| `julia.mendez@gigabyte.com` | `demo1234` | OPERATIVO | ninguno |

**Distribuidores** (línea de crédito / saldo actual):
- Elit: $30k crédito / $8,310 a cobrar
- New Bytes: $20k crédito / $7,180 a cobrar
- Invid: $40k crédito / $5,760 a cobrar
- Air: $12k crédito / $4,445 a cobrar

---

## Memoria — Usuario

### Perfil de Catriel

Catriel Mercurio (`hermess`), trabaja para Blu Studio Inc. Dueño/desarrollador principal de `gigaErp`. Trabaja en español argentino. Prefiere mensajes concisos, directos, sin relleno.

Tiene varios proyectos ERP en paralelo (este `gigaErp` para Gigabyte; `erp.blustudioinc.com` para Blu — referencia visual para invoices).

Hace `git pull` manualmente entre sesiones. Siempre chequear `git log --oneline -5` antes de asumir el estado del repo.

---

## Memoria — Feedback (workflow)

### Workflow git

Trabaja **directo sobre `main`** — no usa feature branches. NO agregar `Co-Authored-By: Claude...`. `git commit` y `git push` solo cuando lo pide explícitamente.

### Deploy dance backend (sin rebuild)

```bash
docker cp backend/app/... gigaerp-backend:/var/www/html/app/...
docker cp backend/routes/api.php gigaerp-backend:/var/www/html/routes/
docker exec gigaerp-backend php artisan migrate --force     # si hay migraciones
docker exec gigaerp-backend php artisan route:clear
docker exec gigaerp-backend php artisan config:cache        # SIEMPRE
```

**Frontend:** siempre rebuild `--no-cache`. Después: `docker restart gigaerp-nginx`.

### CLAUDE.md ≤200 líneas (regla dura)

El `CLAUDE.md` NO puede pasar de 200 líneas. Toda la info importante vive en esta bóveda.

---

## Memoria — Gotchas críticos

### API Resource wrapper — `res?.data ?? res`

```js
// Colección (index) — Resource::collection → { data: [], meta: {} }
usuarios.value = res?.data ?? res

// Recurso individual (show) — Resource → { data: {} }
cliente.value = res?.data ?? res
```
**Síntoma:** solo primer elemento visible, o UI vacía.

### authStore — inicializar en `<script setup>`, no dentro de funciones

```js
// ✓ Correcto — disponible en template
const authStore = useAuthStore()
const puedeAprobar = computed(() => authStore.tienePermiso("aprobaciones"))
```

### Flujo de estados — Órdenes de Venta

```
BORRADOR → APROBADA → FACTURADA → (nota de crédito)
    ↓           ↓
  ANULADA    ANULADA
```

- Solo `aprobaciones` puede aprobar
- Solo APROBADA puede generar invoice
- Solo FACTURADA puede emitir nota de crédito

### Dos tablas de stock (no sincronizan)

- `productos.stock` → Stock Distri / APIs Distri
- `stock_deposito` → Stock Bodega / Órdenes de Venta
- Importaciones XLSX → solo actualizan `stock_deposito`

### Import XLSX — lookup doble

```php
$candidatos = Producto::where("sku", $sku)->pluck("id");
if ($candidatos->isEmpty()) {
    $candidatos = Producto::where("codigo_distribuidor", $sku)->pluck("id");
}
```
Los Excel de proveedores usan `codigo_distribuidor`.

### Nota de crédito — dos orígenes

1. **Cuenta corriente**: ítems libres (texto), cualquier monto
2. **Orden FACTURADA**: pre-llenada con productos de la orden, editable para parciales

Ambos van al mismo endpoint `POST /api/clientes/{cliente}/notas-credito`.

### Nuxt `[id].vue` + carpeta `[id]/` — conflicto

Mover el `.vue` a `[id]/index.vue`.

### `no such table: X (Connection: sqlite)`

```bash
docker exec gigaerp-backend php artisan config:cache
```

### Nginx 502 después de rebuild

```bash
docker restart gigaerp-nginx
```

### Patrón de filtros — card blanca

```html
<div class="bg-white rounded-xl border border-[#E8E8E3] p-4 flex flex-wrap gap-3 items-center">
```
Todas las páginas con filtros usan este patrón. Verificar que Stock Bodega ya lo tiene.

---

## Memoria — Sistema de permisos

```js
// Frontend
authStore.isAdmin                           // true si ADMIN
authStore.tienePermiso("aprobaciones")      // true si ADMIN o tiene el permiso

// Backend
$request->user()->tienePermiso("aprobaciones")  // → 403 si falla
```

**Permisos actuales:** `aprobaciones`, `VER_MONTOS`

**Para agregar permiso nuevo:**
1. Definir clave string
2. Agregar a `PERMISOS_DISPONIBLES` en `configuracion/index.vue`
3. Usar con `tienePermiso()` en ambos lados

---

## Memoria — Preview de documentos (invoice y nota de crédito)

```js
// Abrir en nueva tab
window.open(`/api/ventas/${id}/preview?token=${encodeURIComponent(authStore.token)}`, "_blank")
window.open(`/api/notas-credito/${id}/preview?token=${encodeURIComponent(authStore.token)}`, "_blank")
```

Ambos controllers validan el token Sanctum aunque la ruta sea pública.
Las vistas blade usan logo PNG embebido como base64 (workaround html2canvas + SVG viewBox).

---

## Memoria — Referencias externas

- **Blu ERP:** `https://erp.blustudioinc.com` — referencia visual para invoices
- **Bóveda Obsidian:** `https://localhost:27124/` · Token en `memory/obsidian_vault.md`

---

## Ver también

- [[gigaErp]] — índice del proyecto
- [[arquitectura]] — modelos, rutas, patrones
- [[contexto]] — reglas de negocio y datos seed
- [[troubleshooting]] — gotchas expandidos
