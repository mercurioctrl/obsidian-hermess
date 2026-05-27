# Memoria — gigaErp

Consolidación de la memoria de Claude para este proyecto. Sincronizado **2026-05-26**.

Vive en `~/.claude/projects/-var-www-gigabyte-gigaErp/memory/` — esta nota es el espejo.

---

## Contexto rápido

**gigaErp** — sistema interno Gigabyte (hardware IT) en `http://localhost:8824`.

| Email | Pass | Rol |
|-------|------|-----|
| `admin@gigabyte.com` | `admin123` | ADMIN |
| `maria.gomez@gigabyte.com` | `demo1234` | OPERATIVO |
| `lucas.herrera@gigabyte.com` | `demo1234` | OPERATIVO |

**Distribuidores**: Elit (GBA $50k, saldo $8,310), New Bytes (Córdoba $40k, saldo $7,180), Invid (Mendoza $35k, saldo $5,760), Air (Rosario $30k, saldo $4,445)

---

## Memoria — Usuario

### Perfil de Catriel

Catriel Mercurio (`hermess`), trabaja para Blu Studio Inc. Es el dueño/desarrollador
principal de `gigaErp`. Trabaja en español argentino — responder en español, con
tildes correctas. Prefiere mensajes concisos, directos, sin relleno.

Tiene varios proyectos ERP en paralelo (este `gigaErp` para Gigabyte; otro
`erp.blustudioinc.com` para Blu — referencia visual para presupuestos/invoices).

Hace `git pull` manualmente entre sesiones — a veces hay commits propios entre
medio que no escribí yo. Siempre chequear `git log --oneline -5` antes de
asumir el estado del repo.

---

## Memoria — Feedback (workflow)

### Workflow git

En este proyecto el usuario trabaja **directo sobre `main`** — no usa feature branches.

- NO crear branch antes de commitear.
- NO agregar `Co-Authored-By: Claude...` en los mensajes.
- `git commit` solo cuando el usuario lo pide explícitamente.
- `git push` igual — solo cuando dice "push" o "subilo".
- Mensajes de commit en español, con scope `feat(modulo): ...` o `fix: ...`.

**Why:** proyecto chico de un solo desarrollador, sin code review, sin CI gates.

### Deploy dance del backend (sin rebuild)

Secuencia obligatoria al cambiar código backend en runtime:

```bash
# 1. copiar
docker cp backend/app/... gigaerp-backend:/var/www/html/app/...

# 2. migrar (borrar dup Sanctum antes)
docker exec gigaerp-backend sh -c 'rm -f database/migrations/*_create_personal_access_tokens_table.php'
docker exec gigaerp-backend php artisan migrate --force

# 3. re-cachear config — sin esto cae a sqlite y todo es 500
docker exec gigaerp-backend php artisan config:cache

# 4. si tocaste routes/blade
docker exec gigaerp-backend php artisan route:clear
docker exec gigaerp-backend php artisan view:clear
```

**Después de cualquier rebuild de container app:** `docker restart gigaerp-nginx` o
nginx queda con IP cacheada → 502.

**Frontend:** siempre rebuild `--no-cache`. Nitro tiene manifest de assets en build
time; `docker cp` a `.output/public/` no funciona.

### CLAUDE.md ≤200 líneas (regla dura)

El `CLAUDE.md` del proyecto NO puede pasar de 200 líneas. Toda la información importante
vive en esta bóveda, no en el CLAUDE.md.

---

## Memoria — Proyecto (gotchas)

### Nuxt 3 — conflicto `[id].vue` + `[id]/` directorio

Si coexisten `pages/foo/[id].vue` y el directorio `pages/foo/[id]/`, Nuxt trata
el `.vue` como **layout padre** de todas las rutas hijas. El contenido hijo no reemplaza al padre.

**Solución:** Mover `[id].vue` → `[id]/index.vue`. Así las rutas son hermanas independientes.

```
pages/clientes/
  [id]/
    index.vue              → /clientes/:id
    cuenta-corriente.vue   → /clientes/:id/cuenta-corriente  ✓
```

**Detectado en:** migración de `/clientes/[id].vue` al agregar la sub-ruta `/cuenta-corriente`.

### API Resource wrapper — `c?.data ?? c`

La API devuelve `{ data: {} }` para recursos individuales (Laravel Resource).
En todos los `api.get()` de páginas de detalle usar:

```js
const data = await api.get('/clientes/1')
cliente.value = data?.data ?? data   // ✓
// cliente.value = data              // ✗ → .nombre === undefined
```

### `withSum` para saldo en listado

Para mostrar el saldo de cuenta corriente en el listado de distribuidores sin N+1:

```php
// ClienteController@index
Cliente::withSum('movimientosCuenta as debe_total_usd', 'debe_usd')
       ->withSum('movimientosCuenta as haber_total_usd', 'haber_usd')
       ->paginate(20);

// ClienteResource
'saldo_usd' => round((float)($this->debe_total_usd ?? 0) - (float)($this->haber_total_usd ?? 0), 2),
```

### Sanctum republica su migración en cada boot

El `docker-entrypoint.sh` del backend corre `php artisan vendor:publish` para Sanctum
en cada arranque, generando un archivo nuevo con timestamp. Como la tabla
`personal_access_tokens` ya existe, `migrate` revienta.

**Workaround:** `rm -f database/migrations/*_create_personal_access_tokens_table.php` antes de migrar.

### html2canvas rompe SVG con viewBox offset

`aorus_logo_black.svg` tiene `viewBox="519 657 1819 455"` (no empieza en 0,0). html2canvas
ignora el offset y recorta el logo en el PDF.

**Solución:** PNG embebido como data URI base64 en el blade (`aorus_logo_black.png`).

### Filtros de stock en backend — parámetros exactos

- `?stock=con_stock` → productos con stock > 0
- `?stock=sin_stock` → productos con stock = 0
- Sin parámetro → todos

**No usar** `?stock=con` o `?stock=sin` — el backend no los reconoce.

### Credenciales y endpoints dev

- **Login:** `admin@gigabyte.com` / `admin123` (modelo `Usuario` → tabla `usuarios`)
- **URL:** `http://localhost:8824`
- **DB:** `gigaerp/changeme` host port `3310`
- **Token compartible:** `?token=${encodeURIComponent(token)}` en URL, backend valida con `PersonalAccessToken::findToken()`

---

## Memoria — Módulo Cuenta Corriente

### Estructura

```
Tabla: movimientos_cuenta
Enum TipoMovimiento: FACTURA, PAGO, NOTA_CREDITO, AJUSTE
Saldo = sum(debe_usd) - sum(haber_usd). Positivo = cliente debe. Negativo = cliente tiene crédito.
```

### Endpoint

```
GET /api/clientes/{cliente}/cuenta-corriente
Respuesta: { movimientos: [...con saldo_acumulado por fila...], resumen: { debe_usd, haber_usd, saldo_usd } }
```

### Ruta Nuxt

`/clientes/[id]/cuenta-corriente.vue` — hermana de `[id]/index.vue`.

---

## Memoria — Referencias externas

### Blu ERP — referencia visual

`https://erp.blustudioinc.com` — referencia visual cuando pide reproducir features.

Patrón ya replicado (commit `001f8c8`):
- Preview HTML en blade con html2pdf.js cliente-side (no DomPDF)
- Helvetica Neue, max-width 780px, márgenes minimalistas

---

## Ver también

- [[gigaErp]] — índice del proyecto
- [[troubleshooting]] — versión expandida de los gotchas
- [[contexto]] — reglas de negocio y datos seed
- [[arquitectura]] — patrones frontend/backend completos
