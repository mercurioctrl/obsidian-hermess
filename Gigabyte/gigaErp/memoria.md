# Memoria — gigaErp

Consolidación de la memoria de Claude para este proyecto. Sincronizado **2026-05-26**.

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

**Distribuidores**: Elit (GBA $50k, saldo $8,310), New Bytes (Córdoba $40k, saldo $7,180), Invid (Mendoza $35k, saldo $5,760), Air (Rosario $30k, saldo $4,445)

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
docker exec gigaerp-backend php artisan route:clear   # si cambiaron rutas
docker exec gigaerp-backend php artisan config:cache  # SIEMPRE
```

**Frontend:** siempre rebuild `--no-cache`. Después: `docker restart gigaerp-nginx`.

### CLAUDE.md ≤200 líneas (regla dura)

El `CLAUDE.md` NO puede pasar de 200 líneas. Toda la info importante vive en esta bóveda.

---

## Memoria — Gotchas críticos

### API Resource wrapper — `res?.data ?? res`

**SIEMPRE** desempaquetar la respuesta:
```js
// colección (index)
const res = await api.get('/usuarios')
usuarios.value = res?.data ?? res   // ✓ — UsuarioResource::collection devuelve { data: [] }

// recurso individual (show)
const res = await api.get('/ordenes-venta/1')
orden.value = res?.data ?? res      // ✓
```

**Síntoma del bug:** solo se ve el primer elemento del listado, o la UI queda vacía.

### Permiso en frontend — inicializar authStore en `<script setup>`

```js
// ✓ Correcto — disponible en template
const authStore = useAuthStore()
const puedeAprobar = computed(() => authStore.tienePermiso('aprobaciones'))

// ✗ Incorrecto — solo disponible dentro de esa función
function aprobar() {
  const authStore = useAuthStore()  // no disponible en template
}
```

### Flujo de estados — Órdenes de Venta

```
BORRADOR → APROBADA → FACTURADA
    ↓           ↓
  ANULADA    ANULADA
```

- Solo usuarios con permiso `aprobaciones` pueden ir a APROBADA
- Solo desde APROBADA se puede generar invoice (FACTURADA)

### Dos tablas de stock (no sincronizan)

- `productos.stock` — Stock Distri / APIs Distri
- `stock_deposito` — Stock Bodega / Órdenes de Venta
- Importaciones XLSX actualizan solo `stock_deposito`

### Import XLSX — lookup doble

Busca primero por `sku`, luego por `codigo_distribuidor`. Los Excel de proveedores suelen usar `codigo_distribuidor`.

### Nuxt `[id].vue` + carpeta `[id]/` — conflicto

Mover el `.vue` a `[id]/index.vue` para que conviva con rutas hijas.

### `no such table: X (Connection: sqlite)`

```bash
docker exec gigaerp-backend php artisan config:cache
```

Causa: config cache perdido — `env()` no funciona en PHP-FPM.

### Nginx 502 después de rebuild

```bash
docker restart gigaerp-nginx
```

---

## Memoria — Sistema de permisos

```js
// Frontend
authStore.isAdmin                        // true si ADMIN
authStore.tienePermiso('aprobaciones')   // true si ADMIN o tiene el permiso

// Backend
$request->user()->tienePermiso('aprobaciones')  // → 403 Response si falla
```

**Para agregar un permiso nuevo:**
1. Definir la clave string
2. Agregar a `PERMISOS_DISPONIBLES` en `configuracion/index.vue`
3. Usar en backend con `tienePermiso()`
4. Usar en frontend con `authStore.tienePermiso()`

---

## Memoria — Referencias externas

- **Blu ERP:** `https://erp.blustudioinc.com` — referencia visual para invoices (html2pdf.js, Helvetica Neue, max-width 780px)
- **Bóveda Obsidian:** `https://localhost:27124/` · Token en memoria del usuario

---

## Ver también

- [[gigaErp]] — índice del proyecto
- [[arquitectura]] — patrones frontend/backend completos
- [[contexto]] — reglas de negocio y datos seed
- [[troubleshooting]] — versión expandida de los gotchas
