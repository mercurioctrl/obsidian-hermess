# Feature: Asignación OC ↔ Venta (pedclil ↔ pedprol)

Registra de qué orden de compra (`PedProT/pedprol`) se toma cada unidad de cada línea de venta (`pedclit/pedclil`), **antes** de la serialización ([[modulo-makesale|MakeSale]]). El operador ve el saldo disponible por OC en tiempo real y puede asignar manualmente desde un modal con sugerencia FIFO precargada.

> **Documentación canónica completa**: `docs/asignacion-oc-pedclil.md` en el monorepo (path absoluto: `/Users/hermess/www/pedidos/docs/asignacion-oc-pedclil.md`). Esta nota es el resumen vivo en la bóveda.

## Status

- **Branch**: `feature/asignacion-oc-pedclil` en ambos repos (basadas en `Development`).
- **Estado**: Funcional end-to-end en dev (companies habilitadas: 4=NBE, 11=LASET).
- **Pendiente para mergear**: definir si vamos con migración retroactiva (Opción A vs B) y abrir PRs.

## Decisiones de negocio cerradas

| # | Decisión |
|---|---|
| 1 | Política default: **FIFO por fecha de OC** ascendente, tiebreaker por `nNumPed`. |
| 2 | Override manual desde modal mientras `pedclit.cestado='P'`. Default precarga FIFO o asignación vigente. |
| 3 | Asignación parcial **permitida** (`ASSIGNMENT_ALLOW_PARTIAL=true`). Hoy informativa, no bloquea MakeSale. |
| 4 | Filtro multi-marca por CSV en `ASSIGNMENT_COMPANIES` (ej. `4,11`). |
| 5 | Sin migración retroactiva en v1 — solo aplica a ventas nuevas. |
| 6 | Cross-warehouse permitido a nivel de asignación. Almacén filtra recién al consumir stock. |
| 7 | Toda OC con saldo es candidata, sin filtrar por `cEstado`. Pendiente futuro: corte por fecha. |
| 8 | Permisos solo por `companyCode` (sin rol específico edit vs ver). |
| 9 | **No tocar [[modulo-makesale|MakeSale]] / [[modulo-removesale|RemoveSale]]** — la transición V↔C la maneja un trigger SQL. |

## Arquitectura

```
Frontend (Nuxt 2)              Backend (Laravel 9)            SQL Server
─────────────────              ──────────────────             ──────────
Detail.vue ─┬─► Badge          AsignacionController            pedclil_oc_asignacion (TABLA)
            └─► Modal              │                              ├─ V vigente
                                   ▼                              ├─ L liberada (soft-del)
store/asignaciones.js          AsignacionService                  └─ C consumida
plugins/api.js                     │
publicRuntimeConfig                ▼                            vw_saldo_oc (vista)
                               AsignacionRepository             vw_pedclil_estado_*
                               (bind params, locks)             tg_pedclit_cestado_* (trigger)
```

## Schema (resumen)

**Tabla `[NewBytes_DBF].[dbo].[pedclil_oc_asignacion]`**:
- PK `id BIGINT IDENTITY`
- FK lógica `pedclil_id INT` (a `pedclil.id` IDENTITY)
- OC origen: tupla `(n_num_ped_oc, n_linea_oc?, cref_oc)` — pedprol no tiene IDENTITY
- `cantidad DECIMAL(15,3)`, `origen CHAR(1)` ∈ A/M, `estado CHAR(1)` ∈ V/L/C
- Auditoría: `created_at/by`, `updated_at/by`, `released_at/by/reason`
- 3 índices (sin `WHERE` — el driver dblib no soporta índices filtrados sin SET options ANSI)

**Vistas**:
- `vw_saldo_oc` — saldo dinámico por línea de OC. **Sin filtros** por `cEstado` ni `serialized` (Opción C: el operador ve todo).
- `vw_pedclil_estado_asignacion` — estado por línea pendiente: `SIN_ASIGNAR/PARCIAL/COMPLETA`.

**Trigger `tg_pedclit_cestado_asignacion`** (`AFTER UPDATE` en `pedclit`):
- `'P' → 'S'`: vigentes (`V`) pasan a consumidas (`C`).
- `'S' → 'P'` (revertSale): consumidas vuelven a vigentes.

Cero acoplamiento con [[modulo-makesale]] / [[modulo-removesale]].

## API HTTP

5 endpoints bajo `/v1`, dentro de `middleware('permission')`:

| Método | Ruta | Acción |
|---|---|---|
| GET | `/asignaciones/sugerencia-fifo?pedclilId={id}` | Sugerencia FIFO calculada (no persiste). |
| GET | `/asignaciones/candidatas?pedclilId={id}` | Lista raw de OCs candidatas. |
| GET | `/orders/{branch}-{order}/asignaciones` | Estado por línea + asignaciones del pedido. |
| PUT | `/asignaciones/lineas/{pedclilId}` | Reemplaza vigentes (transaccional, locks). |
| DELETE | `/asignaciones/lineas/{pedclilId}` | Libera todas las vigentes. |

Cuando `feature_flag=false` o company no habilitada: respuesta `{enabled:false}` (HTTP 200), 403 o 409 según corresponda. Validaciones: `pedclit.cestado='P'`, `cref` matchea, suma ≤ pedido, cantidad ≤ disponible (con UPDLOCK+HOLDLOCK).

## Frontend

- **`store/asignaciones.js`** — Vuex module. Getter `estadoPorLinea` deriva 4 estados UI: `COMPLETA / PARCIAL / DISPONIBLE (hay candidatas pero no asignado) / SIN_ASIGNAR (no hay candidatas)`.
- **`components/Orders/AsignacionBadge.vue`** — tag verde/amarillo/naranja/rojo + tooltip con cantidades + OCs candidatas.
- **`components/Modal/AsignarOCModal.vue`** — tabla editable con sugerencia FIFO precargada, validación en vivo, tooltips explicando FIFO al usuario final.
- **`components/Orders/Detail.vue`** — columna "OC" en `allColumns` después de `cant`, gateada por `assignmentFeatureEnabled && companyHabilitada`. Botón ✏️ por línea cuando `isPending`.
- **`plugins/api.js`** — namespace `asignacion` (5 wrappers).
- **`nuxt.config.js`** — `publicRuntimeConfig.assignmentFeatureEnabled` y `assignmentCompanies`.

**Cambios extra al backend para que el front funcione**:
- `OrderDetailDto.companyCode` (de `pedclit.companyCode`).
- `OrderItemDto.pedclilId` (de `pedclil.id`) — porque `item.id` ya estaba mapeado a `articulo.ID_ARTICULO`, no a la línea.

## Command CLI

```bash
php artisan asignaciones:fifo
    [--branch=0002] [--order=12345] [--company=4]
    [--limit=50] [--dry-run]
```

Idempotente (no toca líneas con asignación vigente). Transaccional con UPDLOCK por OC. No está scheduled en `Console/Kernel.php` — sumarlo cuando se quiera automatización nightly.

## Variables de entorno

Deben **coincidir entre backend y frontend**:

| Var | Default | Uso |
|---|---|---|
| `ASSIGNMENT_FEATURE_ENABLED` | `false` | Kill switch global. |
| `ASSIGNMENT_COMPANIES` | (vacío) | CSV de companyCodes habilitados. Ej: `4,11`. |
| `ASSIGNMENT_ALLOW_PARTIAL` | `true` | Solo backend. Hoy informativo (no bloquea MakeSale). |

Cambios: `php artisan config:clear` en backend; restart `npm run dev` en frontend (Nuxt lee `publicRuntimeConfig` al boot, no por HMR).

## Deployment

Scripts SQL en `api-rest-pedidos-laravel/app/database/sql/`:
- `2026_04_22_001_create_pedclil_oc_asignacion.sql`
- `2026_04_22_001_drop_pedclil_oc_asignacion.sql` (rollback)

Aplicar via `sqlcmd` o vía `tinker` splitting por `GO`. Ver `database/sql/README.md` para el comando exacto.


## Iteraciones post-merge inicial (2026-04-24)

Cambios incrementales sobre la base ya mergeada en Development. Branch: `feature/asignacion-oc-pedclil`.

### UX del modal
- **Columna Proveedor** entre Fecha y Estado — viene de `FP_Proveedores.cnompro` via JOIN.
- **Columna Proforma** entre Proveedor y Estado — viene de `PedProT.CSUPROF_TEMP`.
- **Número de OC clickeable** — abre `compras.saftel.com/orders` con `search={oc}` y `companyCode` en nueva pestaña.
- **No auto-sugerir FIFO al reabrir si ya hay vigentes**. Si la línea ya tiene asignaciones guardadas, el modal las respeta y deja el resto en 0. Antes, las OCs sin vigente se llenaban con la sugerencia FIFO, lo que parecía que el save anterior no había funcionado. El botón "Aplicar FIFO" sigue disponible para redistribuir on-demand.

### Semántica de `cantidad: 0`
- En el payload del `PUT /v1/asignaciones/lineas/{id}`, items con `cantidad: 0` ahora se **ignoran silenciosamente** (antes tiraba 422). FormRequest cambió de `min:0.001` a `min:0`.
- Si **todos** los items vienen en 0 (o el array `items` viene vacío), el endpoint actúa como `DELETE`: libera todas las vigentes y devuelve `liberadas` extra en el payload.

### Backend — campos nuevos en `candidatasFifo`
La query del repo ahora hace JOIN `vw_saldo_oc → PedProT → FP_Proveedores` y expone:
- `proveedor_nombre` (de `FP_Proveedores.cnompro`)
- `proforma` (de `PedProT.CSUPROF_TEMP`)

`sugerirFifo` también propaga ambos en cada item del array `items`. **Sin cambios de DDL** — el JOIN se hace solo en el query del repo, no se tocó la vista.

### Gotcha de merge
La rama `feature/asignacion-oc-pedclil` ya había sido mergeada a Development varias veces (PRs #1193, #1196, #1197). Después de eso, alguien empujó refactores directos a Development que tocaban `AsignarOCModal.vue` (z-index, focus, label de estado). Para evitar conflictos al mergear nuevos cambios:

> **Antes de pushear cambios al modal en esta rama, hacer `git fetch && git reset --hard origin/Development`** (después de stashear cualquier change local) y reaplicar solo el commit nuevo. Esto fue lo que se hizo el 2026-04-24 — force-push con `--force-with-lease`.

## Decisiones diferidas

- **Backfill histórico** de pedclit pendientes (Opción B). Hoy no se hace.
- **Corte por fecha** en candidatas para no mostrar OCs de 2013. Definir con negocio.
- **Validación dura en MakeSale** (bloquear serialización si hay líneas no asignadas). Si se hace, NO tocar MakeSale — usar trigger BEFORE UPDATE o capa nueva.
- **Permisos diferenciados** view vs edit.
- **Tests automatizados** contra SQL Server real (no SQLite).
- **Reportería de margen por OC origen** — la data está, falta dashboard.

## Gotchas técnicos

- **Driver dblib** no setea SET options ANSI requeridos para índices filtrados (`WHERE estado='V'`). Por eso los 3 índices de la tabla NO usan `WHERE` — son completos. Si más adelante migramos al driver `sqlsrv` puro, se pueden filtrar.
- **`pedprol` no tiene IDENTITY** ni PK formal — la identificación es la tupla `(nNumPed, nLinea, cRef)`, snapshoteada en cada insert.
- **Saldo y disponible son siempre dinámicos** (`vw_saldo_oc`) — no hay tabla de "disponibles" que mantener sincronizada.
- **Asignación es informativa hasta MakeSale** — el saldo verdadero post-consumo lo gestiona el legacy. Por ahora no descontamos el consumo histórico (Opción C de modelado).

## Lookup rápido

| Si necesito... | Mirar... |
|---|---|
| Cambiar política FIFO | `AsignacionRepository::candidatasFifo` línea del `ORDER BY`. |
| Agregar validación al guardar | `AsignacionService::reemplazarAsignacionLinea`. |
| Cambiar lo que muestra el badge | `AsignacionBadge.vue` + getter `estadoPorLinea` en `store/asignaciones.js`. |
| Habilitar/deshabilitar company | `.env` ambos lados: `ASSIGNMENT_COMPANIES`. |
| Re-correr FIFO masivo | `php artisan asignaciones:fifo --limit=N`. |
| Saber qué pasó con una asignación | `SELECT * FROM pedclil_oc_asignacion WHERE id = X` (estado + released_reason). |

## Ver también

- [[arquitectura]] — Estructura general del proyecto
- [[modulo-makesale]] — Flujo MakeSale (no se toca desde este feature)
- [[modulo-removesale]] — Flujo RemoveSale (no se toca desde este feature)
- [[contexto]] — Gotchas técnicos del repo
- [[changelog]] — Historial cronológico
