# Cookbook — Asignación OC ↔ Venta

Recetas prácticas para trabajar sobre [[feature-asignacion-oc|el feature]] sin tener que releer toda la arquitectura. Complementa la [[feature-asignacion-oc#Lookup rápido|tabla de lookup]] con código y queries concretos.

> Doc canónica completa: `/Users/hermess/www/pedidos/docs/asignacion-oc-pedclil.md`

---

## Recetas de modificación

### Agregar columna nueva al modal de asignación

Tres puntos, en orden:

1. **Backend — repo**: `AsignacionRepository::candidatasFifo`. Agregar el campo al `SELECT`, y JOIN si viene de otra tabla. Patrón ya usado para `proveedor_nombre` (FP_Proveedores), `proforma` (PedProT.CSUPROF_TEMP) y `costo` (pedprol.nPreDiv, JOIN por `nNumPed + cRef`). **No tocar `vw_saldo_oc`** — el JOIN queda en la query del repo, nunca en la vista.

2. **Backend — service**: `AsignacionService::sugerirFifo`. Propagar el campo dentro del array `items` (cada elemento del foreach `$candidatas`). El endpoint `/candidatas` ya devuelve raw del repo, no requiere cambio.

3. **Frontend — modal**: `AsignarOCModal.vue`:
   - `columnas()` — agregar `{ title: '...', dataIndex: '...', ... }` en el orden deseado. Para numéricos usar `customRender` con `toLocaleString('es-AR', { minimumFractionDigits: 2, maximumFractionDigits: 2 })` (patrón del campo `costo`).
   - `inicializar() → this.filas.map(...)` — mapear `nuevoCampo: c.nombre_backend || null`. Para numéricos castear: `costo: c.costo != null ? Number(c.costo) : null`.
   - Si sumás muchas columnas, subir el `width` del `<a-modal>` (de 800 → 900 al agregar costo).

### Cambiar política de orden FIFO

Solo un lugar: `AsignacionRepository::candidatasFifo`, el `ORDER BY vs.fecha_oc ASC, vs.n_num_ped_oc ASC`. Cambiarlo afecta a `sugerirFifo`, `aplicarFifoLinea` y al modal (que recibe las candidatas ya ordenadas).

Si se quiere soportar múltiples políticas, agregar parámetro `?policy=fifo|lifo|...` al endpoint y switch en repo.

### Habilitar una company nueva

Coordinado en dos `.env`:

- Backend `api-rest-pedidos-laravel/app/.env` → `ASSIGNMENT_COMPANIES=4,11,12`
- Frontend `pedidos-web-app-v1/app/.env` → idem

Después: `php artisan config:clear` en backend, restart `npm run dev` (Nuxt no toma `publicRuntimeConfig` en HMR).

### Agregar validación al guardar

`AsignacionService::reemplazarAsignacionLinea`. Va antes del `usort` y del `liberarVigentesDeLinea`. Tirar excepción con código HTTP en el segundo arg (`new \Exception('msg', 422)`).

### Agregar campo a la tabla de asignaciones

1. SQL `ALTER TABLE` directo (no migration Laravel, igual que el resto del feature).
2. Si participa del INSERT: editar `AsignacionRepository::insertAsignacion` (el array $data y el SQL).
3. Si participa del SELECT al frontend: editar `AsignacionRepository::asignacionesDeLinea`.

### Modo solo lectura para pedidos remitidos

Cuando `pedclit.cestado='S'` (remitido), el modal se puede abrir igual pero todo queda read-only. Trigger automático: el ícono del botón en `Detail.vue` cambia de ✏️ (edit) a 👁️ (eye) cuando `!isPending`, y el prop `:read-only="!isPending"` se pasa al modal.

En modo read-only:
- Alerta info arriba: "Pedido ya remitido — modo solo lectura".
- Botones "Aplicar FIFO" y "Limpiar" del header se ocultan.
- `a-input-number` de Cantidad y `a-checkbox` de Costo: `:disabled="readOnly"`.
- Footer: solo "Cerrar" (primary) — desaparecen "Guardar" y "Guardar con costo".
- `inicializar()` acepta asignaciones con estado **`'V'` o `'C'`** cuando readOnly (el trigger SQL promueve V→C al pasar `pedclit.cestado` P→S).
- **Filas huérfanas**: asignaciones vigentes/consumidas cuya OC ya no aparece en `candidatasFifo` (saldo agotado) se agregan como filas sintéticas con `proveedor=null, proforma=null` y los datos disponibles (OC, fecha, costo, cantidad). Sin esto, el operador no podría ver qué OC consumió el pedido después de serializar.

### Persistir checkbox de "costo seleccionado" en DB (no localStorage)

La columna `pedclil_oc_asignacion.costo_seleccionado BIT NOT NULL DEFAULT 0` (agregada el 2026-04-25) reemplaza la persistencia previa en `localStorage`. Motivo: portable entre máquinas — si el operador abre el pedido desde otra PC, los tildes siguen ahí.

Camino de datos:
- **Escritura**: al apretar "Guardar" o "Guardar con costo", cada item del PUT incluye `costo_seleccionado: true/false`. `ReemplazarAsignacionRequest` lo valida como `nullable|boolean`. `AsignacionService::reemplazarAsignacionLinea` lo propaga a `$itemsNorm[...][costoSel]` y `insertAsignacion` lo graba.
- **Lectura**: `AsignacionRepository::asignacionesDeLinea` devuelve el flag. El modal, al mapear filas, hace `costoSeleccionado: c.costo != null && !!Number(vigente.costo_seleccionado)`.
- **En memoria (antes de guardar)**: `toggleCostoSeleccionado(fila, checked)` solo muta `fila.costoSeleccionado`. El click del checkbox no dispara un endpoint granular — si cerrás el modal sin guardar, se pierde. Si se quiere persistencia inmediata, agregar un PATCH granular al endpoint.

### Gotchas SSMS al aplicar ALTERs (Microsoft SQL Server Management Studio)

1. **"Sintaxis incorrecta cerca de 'database'"** — pasa al referenciar `[NewBytes_DBF].INFORMATION_SCHEMA.COLUMNS` en cross-db. Fix: usar `USE [NewBytes_DBF]; GO` al principio del script y luego `sys.columns` + `sys.tables` (más robustos que `INFORMATION_SCHEMA`).

2. **"ROLLBACK TRANSACTION no tiene BEGIN TRANSACTION"** — cosmético, aparece si la sesión tiene `SET IMPLICIT_TRANSACTIONS ON`. Los DDL se aplican igual. Desactivar en `Tools → Options → Query Execution → SQL Server → ANSI`, o poner `SET IMPLICIT_TRANSACTIONS OFF;` al inicio del script.

3. **DROP COLUMN falla por dependencia del default constraint** — hay que dropear primero el constraint y **después** la columna, con `GO` entre medio (si no, los dos queries van al mismo batch y SQL Server valida dependencias antes de ejecutar ambos).

4. **Evitar pegar apply + drop en la misma ventana** — el segundo borra lo que el primero hizo. Ya pasó: después de correr el apply, SSMS con ambos scripts abiertos ejecutó también el drop. Resultado: columna desaparece y el backend rompe con *"Invalid column name 'costo_seleccionado'"*. Mantener apply y rollback como archivos separados y ejecutarlos deliberadamente.

### Agregar un bloque de contexto al modal (no editable)

Patrón usado para **Stock por depósito** y **Órdenes / Remitos comprometidos**. Sirve para mostrar info alrededor del SKU que ayude al operador a decidir sin convertirla en columna de la tabla editable.

1. **Backend — repo**: método nuevo que recibe `int $idArticulo` (no `$pedclilId`) — las queries no dependen de la línea. Si necesitás filtrar por marca, agregar `?int $companyCode`.
2. **Backend — service**: método `xxxDeLinea(int $pedclilId)` que hace `repo->pedclilInfo()` para resolver `id_articulo` + `company_code`, y luego llama al repo. Retorna `[]` si la línea no existe (no tirar excepción — el modal queda tolerante).
3. **Backend — controller**: método nuevo + `Route::get('/xxx', ...)` bajo el prefijo `asignaciones`. Usar feature flag (`featureEnabled()`) pero **no** `companyHabilitada` (la info es read-only, no muta estado).
4. **Frontend — plugin**: wrapper en `plugins/api.js` dentro del namespace `asignacion`.
5. **Frontend — modal**: agregar estado en `data()`, cargar en `Promise.all` dentro de `inicializar()`, renderizar **fuera** del `<a-table>` de asignación. Para listas cortas usar `a-tag` (stock); para listas largas usar `a-collapse` con `a-table` y `scroll: { y: 180 }` (compromisos).

Clave: mantener separado el estado de asignación (filas editables) del contexto (lectura). Nunca meter datos de contexto en `this.filas`.

### Pisar costForSale desde el modal con el promedio ponderado de asignaciones

El modal tiene un botón "Guardar con costo" que, además de persistir la asignación, hace `PATCH /v1/orders/addItem` con `costForSale` = promedio ponderado de las OCs tildadas. Lecciones aprendidas:

1. **Endpoint existente** — Usamos `/v1/orders/addItem` (ruta `OrderUpdate@__invoke`). Requiere body completo: `order`, `branch`, `itemId`, `amount`, `selectedPrice`, `costForSale`, `stockWarehouseId`. No hay variante "solo costo".

2. **`selectedPrice` NO es `pedclil.listaPrecio`** — es el precio unitario real (`pedclil.npreunit`). `listaPrecio` es un código (0, 1, 2…) y el backend valida `selectedPrice > 0`, así que mandar `0` tira 500 con *"No se permite un precio menor o igual a 0"*. `AsignacionService::sugerirFifo` expone `precio_unitario` para esto.

3. **Para que funcione, `pedclilInfo` trae**: `id_articulo`, `producto_nombre` (`articulo.cDetalle`), `id_almacen`, `lista_precio`, `npreunit`. El service los propaga en el payload de sugerencia. El modal los usa tanto para el título (`branch - order - id - nombre`) como para armar el PATCH.

4. **Refresh del detalle tras "Guardar con costo"** — El modal emite `'saved', { conCosto }` y `Detail.vue → onAsignacionGuardada(payload)` llama `refreshModalOrder(this.order)` solo cuando `conCosto=true`. Sin eso, la columna Costo en la tabla muestra el valor viejo (el store del pedido no se recarga solo).

### Redondeo consistente entre display y PATCH (bug de 0,01)

Bug observado: el modal mostraba `139,73` pero el backend guardaba `139,72` — mismo cálculo, reglas de redondeo distintas.

- `Number(x).toLocaleString('es-AR', { maximumFractionDigits: 2 })` redondea half-to-even o half-up según el motor.
- `x.toFixed(2)` aplica half-away-from-zero pero sobre la representación IEEE-754, que para `139.725` es `139.7249999…` ⇒ trunca a `139.72`.

**Fix canónico** — redondear UNA vez con `Math.round((x + Number.EPSILON) * 100) / 100` y reutilizar ese número tanto en display como en PATCH. `Number.EPSILON` corrige el drift en bordes como `139.725 → 139.73`. Ver `costoCalculo` en `AsignarOCModal.vue` y `costoPonderadoPorLinea` en `store/asignaciones.js` — comparten la misma fórmula para que match exacto sea posible.

### Heurística "ASIGNADA" en el dropdown de Costo (Detail.vue)

Para marcar visualmente cuando `costForSale` vino de una asignación OC (sin columna `cost_source` en DB), comparamos:

```js
Math.round((record.price.costForSale + Number.EPSILON) * 100) / 100
  === store.getters['asignaciones/costoPonderadoPorLinea'](branch, order, pedclilId)
```

Si coincide ⇒ tag violeta **"ASIGNADA"**; si no ⇒ tag verde **"ACTUAL"**.

Requisitos para que el getter funcione:
- `AsignacionRepository::asignacionesDeLinea` trae `costo` (JOIN `pedprol.nPreDiv ON nNumPed + cRef`).
- El store usa el mismo redondeo que el modal (ver sección anterior).

Esta heurística es **frágil** (si cambia una asignación vigente, el tag deja de aparecer aunque el costo provenga de un "Guardar con costo" anterior). Si necesitás trazabilidad persistente, agregar columna `cost_source` VARCHAR a `pedclil`.

### Persistir preferencias UI del modal en localStorage

Los checkboxes de costo se recuerdan entre aperturas via `localStorage['asignarOC.costoTildados.{pedclilId}']` = JSON array de `"{n_num_ped_oc}|{cref}|{n_linea_oc}"`.

- **Guardar**: cada `@change` llama `persistirCostoSeleccion()` que serializa filas con `costoSeleccionado=true`. Si el set queda vacío, elimina la key (no deja basura).
- **Cargar**: `inicializar()` llama `loadCostoSeleccion()` que devuelve un `Set`; al mapear `this.filas` chequea `Set.has(key)`.
- **Tolerante**: si `localStorage` no existe (SSR) o falla (quota), fallback a Set vacío sin romper.

Útil para preferencias UI por línea que no justifican una columna en DB.

### Footer custom en a-modal con múltiples botones

Para tener más de 2 botones (Cancelar + Guardar) usar el slot `footer`:

```vue
<a-modal :z-index="lastZIndex + 1" @cancel="$emit('close')">
  <template slot="footer">
    <a-button @click="$emit('close')">Cancelar</a-button>
    <a-button :disabled="!condicion" @click="guardar({ modo: 'A' })">Opción A</a-button>
    <a-button type="primary" @click="guardar()">Guardar</a-button>
  </template>
  ...
</a-modal>
```

Quitar `:ok-button-props`, `ok-text`, `cancel-text` y `@ok` — el slot reemplaza eso.

### Dropdown de select más ancho que el trigger

El select de la columna Costo en `Detail.vue` mide ~110px, pero su dropdown necesita más ancho para entrar precio + tag + bandera + proveedor:

```vue
<a-select
  :dropdown-match-select-width="false"
  dropdown-class-name="cost-dropdown"
  :dropdown-style="{ minWidth: '320px' }"
>
```

El trigger queda del tamaño de la celda; el dropdown crece al abrir. Combinar con `font-variant-numeric: tabular-nums` en el CSS del valor para que los precios queden alineados como columna.

**OJO**: los estilos del dropdown NO pueden ir en `<style scoped>` — los a-select-option se portal-izan al `body`, fuera del componente. Usar `<style lang="less">` global o `<style>` sin scoped.

---

## SQL queries útiles para debug

### Ver estado de una línea específica

```sql
DECLARE @pedclilId INT = 1477851;

SELECT id, estado, cantidad, n_num_ped_oc, cref_oc,
       origen, created_at, released_at, released_reason
FROM NewBytes_DBF.dbo.pedclil_oc_asignacion
WHERE pedclil_id = @pedclilId
ORDER BY created_at DESC;
```

### Ver candidatas raw para un SKU + company

```sql
SELECT TOP 20 *
FROM NewBytes_DBF.dbo.vw_saldo_oc
WHERE id_articulo = 122323
  AND company_code = 11
  AND cantidad_disponible > 0
ORDER BY fecha_oc ASC, n_num_ped_oc ASC;
```

### Forzar `pedclit` de pendiente a serializado (test de trigger)

```sql
-- ⚠️ solo dev, usar pedclit creado a propósito
UPDATE NewBytes_DBF.dbo.pedclit
   SET cestado = 'S'
WHERE cnumsuc = '0001' AND cnumped = '00012345';

-- verificar que las vigentes pasaron a 'C'
SELECT estado, COUNT(*)
FROM NewBytes_DBF.dbo.pedclil_oc_asignacion
WHERE cnumsuc = '0001' AND cnumped = '00012345'
GROUP BY estado;
```

### Liberar manualmente una asignación atascada

```sql
UPDATE NewBytes_DBF.dbo.pedclil_oc_asignacion
   SET estado          = 'L',
       released_at     = SYSUTCDATETIME(),
       released_reason = 'manual_dba'
WHERE id = <id_asignacion>;
```

### Stock del SKU por depósito

```sql
SELECT s.ID_ALMACEN, a.CNOMBRE, a.CCODALM, a.companyCode,
       s.nstock, s.nstock_reserva_pedidos, s.nstock_virtual
  FROM NewBytes_DBF.dbo.stocks s
  LEFT JOIN NewBytes_DBF.dbo.FP_Almacen a ON a.ID_ALMACEN = s.ID_ALMACEN
 WHERE s.ID_ARTICULO = 122562
   AND a.deleted_at IS NULL
   AND (s.nstock > 0 OR s.nstock_reserva_pedidos > 0);
```

### Qué está consumiendo stock del SKU (pedidos pendientes + remitos sin facturar)

```sql
-- Pedidos pendientes (cestado='P') — reservan stock lógicamente
SELECT TOP 50 l.cnumsuc, l.cnumped, l.ncanped, t.dFecPed,
       t.ccodcli, c.cnomcli, l.ID_ALMACEN
  FROM NewBytes_DBF.dbo.pedclil l
  INNER JOIN NewBytes_DBF.dbo.pedclit t
          ON t.cnumsuc=l.cnumsuc AND t.cnumped=l.cnumped
  LEFT JOIN NewBytes_DBF.dbo.clientes c ON c.ccodcli=t.ccodcli
 WHERE l.ID_Articulo = 122562
   AND t.cestado = 'P'
   AND ISNULL(l.anulado,0)=0
   AND t.companyCode = 11
 ORDER BY t.dFecPed DESC;

-- Remitos sin facturar (albclit.lfacturado=0) — reserva formal
SELECT TOP 50 l.cnumsuc, l.cnumalb, l.ncanent, t.dfecent,
       t.ID_CLIENTE, c.cnomcli, l.ID_ALMACEN
  FROM NewBytes_DBF.dbo.albclil l
  INNER JOIN NewBytes_DBF.dbo.albclit t
          ON t.cnumsuc=l.cnumsuc AND t.cnumalb=l.cnumalb
  LEFT JOIN NewBytes_DBF.dbo.clientes c ON c.ID_CLIENTE=t.ID_CLIENTE
 WHERE l.ID_Articulo = 122562
   AND ISNULL(t.lfacturado,0) = 0
 ORDER BY t.dfecent DESC;
```

---

## Curl ejecutables

Reemplazar `{TOKEN}` con un JWT válido y `{HOST}` (ej. `localhost:8093` en local, `api.orders.lio.red` en prod).

### Sugerencia FIFO

```bash
curl -s "https://{HOST}/v1/asignaciones/sugerencia-fifo?pedclilId=1477851" \
  -H "Authorization: Bearer {TOKEN}" | jq
```

### Candidatas raw

```bash
curl -s "https://{HOST}/v1/asignaciones/candidatas?pedclilId=1477851" \
  -H "Authorization: Bearer {TOKEN}" | jq '.data[] | {oc:.n_num_ped_oc, prov:.proveedor_nombre, prof:.proforma, disp:.cantidad_disponible}'
```

### Asignar (reemplazar)

```bash
curl -s -X PUT "https://{HOST}/v1/asignaciones/lineas/1477851" \
  -H "Authorization: Bearer {TOKEN}" \
  -H "Content-Type: application/json" \
  --data-raw '{"items":[{"n_num_ped_oc":12607,"n_linea_oc":5,"cref_oc":"122323","cantidad":10}]}'
```

### Liberar todo (DELETE)

```bash
curl -s -X DELETE "https://{HOST}/v1/asignaciones/lineas/1477851" \
  -H "Authorization: Bearer {TOKEN}"
```

### Equivalente al DELETE via PUT con items vacíos

```bash
curl -s -X PUT "https://{HOST}/v1/asignaciones/lineas/1477851" \
  -H "Authorization: Bearer {TOKEN}" \
  -H "Content-Type: application/json" \
  --data-raw '{"items":[]}'
```

### Estado por pedido completo

```bash
curl -s "https://{HOST}/v1/orders/0001-00012345/asignaciones" \
  -H "Authorization: Bearer {TOKEN}" | jq '.data.lineas'
```

### Stock por depósito del SKU de una línea

```bash
curl -s "https://{HOST}/v1/asignaciones/stock-almacenes?pedclilId=1477851" \
  -H "Authorization: Bearer {TOKEN}" | jq '.data[] | {almacen:.nombre, stock, reservado}'
```

### Compromisos (pedidos pendientes + remitos sin facturar)

```bash
curl -s "https://{HOST}/v1/asignaciones/comprometido?pedclilId=1477851" \
  -H "Authorization: Bearer {TOKEN}" | jq '{pedidos:(.data.pedidos|length), remitos:(.data.remitos|length)}'
```

---

## Mapa de archivos por funcionalidad

### Backend (`api-rest-pedidos-laravel/app/`)

| Archivo | Responsabilidad |
|---|---|
| `app/Http/Controllers/Asignacion/AsignacionController.php` | 7 endpoints HTTP (`sugerencia`, `candidatas`, `stockAlmacenes`, `comprometido`, `porPedido`, `reemplazar`, `liberar`). Resolveuser, gates de feature flag y company. |
| `app/Http/Requests/Asignacion/ReemplazarAsignacionRequest.php` | Validación shape de payload del PUT. |
| `app/Services/Asignacion/AsignacionService.php` | Lógica transaccional + lectura. `reemplazarAsignacionLinea`, `aplicarFifoLinea`, `sugerirFifo`, `liberarAsignacionLinea`, `stockPorAlmacenDeLinea`, `comprometidoDeLinea`. |
| `app/Repositories/Asignacion/AsignacionRepository.php` | Queries directas. Escritura: `insertAsignacion`, `liberarVigentesDeLinea`, `lockYRecalcularSaldoOc`. Lectura: `candidatasFifo`, `asignacionesDeLinea`, `estadoAsignacionDePedido`, `lineasSinAsignacion`, `stockPorAlmacen`, `pedidosPendientesPorArticulo`, `remitosSinFacturarPorArticulo`. |
| `app/Models/AsignacionPedclilOC.php` | Eloquent model (poco usado, las queries son raw). |
| `app/Console/Commands/AsignacionesFifo.php` | Command CLI `asignaciones:fifo`. |
| `database/sql/2026_04_22_001_create_pedclil_oc_asignacion.sql` | DDL inicial: tabla, índices, vistas, trigger. |
| `database/sql/2026_04_22_001_drop_pedclil_oc_asignacion.sql` | Rollback inicial. |
| `database/sql/2026_04_25_001_add_costo_seleccionado.sql` | Agrega columna `costo_seleccionado BIT NOT NULL DEFAULT 0`. Idempotente. |
| `database/sql/2026_04_25_001_drop_costo_seleccionado.sql` | Rollback de la columna. Idempotente. |
| `routes/api.php` | Definición de rutas (búsqueda: `asignaciones`). |
| `config/asignacion.php` | Lee env vars. |

### Frontend (`pedidos-web-app-v1/app/`)

| Archivo | Responsabilidad |
|---|---|
| `components/Modal/AsignarOCModal.vue` | Modal editable principal (también soporta `readOnly` para pedidos remitidos, con filas huérfanas para OCs consumidas). Título dinámico `branch - order - id - nombre`. Tabla de OCs candidatas (columna Costo con checkbox + valor) + bloque de stock por depósito (chips) + collapse con pedidos pendientes y remitos sin facturar. FIFO local, validación en vivo, costo promedio ponderado de OCs tildadas, footer con 3 botones (Cancelar / Guardar con costo / Guardar) o solo "Cerrar" en modo readOnly. Checkboxes persisten en DB (`pedclil_oc_asignacion.costo_seleccionado`). |
| `components/Orders/AsignacionBadge.vue` | Tag de estado por línea con tooltip. |
| `components/Orders/Detail.vue` | Integración: columna "OC" + botón ✏️ (si `isPending`) o 👁️ (si remitido, abre el modal en modo readOnly). Dropdown de costo con tags ACTUAL/PROMEDIO/ASIGNADA (ver `costoVieneDeAsignacion` y estilos `.cost-option`). Handler `onAsignacionGuardada` refresca el detalle tras "Guardar con costo". |
| `store/asignaciones.js` | Vuex module. Getters `estadoPorLinea`, `cantidadesPorLinea`, `asignacionesPorLinea`, `costoPonderadoPorLinea` (usa mismo redondeo que el modal para heurística ASIGNADA). Acciones `reemplazarAsignacion`, `liberarAsignacion`, etc. |
| `plugins/api.js` | Namespace `asignacion` con 7 wrappers (`getAsignacionesPedido`, `getSugerenciaFifo`, `getCandidatasOC`, `getStockAlmacenes`, `getComprometido`, `putAsignaciones`, `deleteAsignaciones`). |
| `nuxt.config.js` | `publicRuntimeConfig.assignmentFeatureEnabled` + `assignmentCompanies`. |

---

## Setup de test local

### Verificar que el feature está activo

```bash
# Backend (.env)
grep ASSIGNMENT_ /Users/hermess/www/pedidos/api-rest-pedidos-laravel/app/.env

# Frontend (.env)
grep ASSIGNMENT_ /Users/hermess/www/pedidos/pedidos-web-app-v1/app/.env
```

Esperar:
- `ASSIGNMENT_FEATURE_ENABLED=true`
- `ASSIGNMENT_COMPANIES=4,11`
- `ASSIGNMENT_ALLOW_PARTIAL=true`

### Refrescar config sin restart

```bash
docker exec -it api-rest-pedidos-apirest-laravel php artisan config:clear
```

Frontend sí requiere restart (`npm run dev`) — Nuxt 2 lee `publicRuntimeConfig` al boot.

### Encontrar un pedido pendiente para testear

```sql
SELECT TOP 5 t.cnumsuc, t.cnumped, t.companyCode, l.id AS pedclil_id, l.cref, l.ncanped
FROM NewBytes_DBF.dbo.pedclit t
INNER JOIN NewBytes_DBF.dbo.pedclil l
        ON l.cnumsuc = t.cnumsuc AND l.cnumped = t.cnumped
WHERE t.cestado = 'P'
  AND t.companyCode IN (4, 11)
  AND ISNULL(l.anulado, 0) = 0
ORDER BY t.dFecPed DESC;
```

---

## Workflow de branch

> Ver [[memoria]] para el detalle.

La rama `feature/asignacion-oc-pedclil` ya recibió 3 merges parciales a Development (PRs #1193, #1196, #1197). Cualquier cambio sobre `AsignarOCModal.vue` u otros archivos compartidos requiere bajar Development primero:

```bash
# Frontend (mismo concepto en backend si Development se adelantó)
cd pedidos-web-app-v1
git stash push -m "preserve" -- app/plugins/firebase-messaging.js app/store/index.js  # si hay cambios locales no relacionados
git fetch origin
git reset --hard origin/Development
# editar archivos
git add ... && git commit -m "..."
git push --force-with-lease origin feature/asignacion-oc-pedclil
git stash pop
```

---

## Ver también

- [[feature-asignacion-oc]] — Resumen del feature
- [[arquitectura]] — Estructura general del proyecto
- [[changelog]] — Historial cronológico de cambios
- [[memoria]] — Memoria consolidada
- [[modulo-makesale]] / [[modulo-removesale]] — Flujos que el trigger conecta
