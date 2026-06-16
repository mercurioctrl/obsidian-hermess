# Feature: Pedidos Olvidados

Filtro oculto en la lista de órdenes que trae **órdenes pendientes o remitidas (no facturadas)** con antigüedad de **más de 2 meses, hasta 3 años atrás**. Pensado para detectar pedidos que quedaron "olvidados" sin avanzar.

Implementado el **2026-06-16**. Rama `feature/pedidos-olvidados` en ambos repos (partiendo de `development` / `Development` actualizado).

## Ubicación en la UI

Lista de órdenes → botón **"Más filtros"** (ícono embudo) → select **"Pedidos olvidados"** (opción "Si"), junto a *Dropshipping*.

## Estados de orden (SQL Server, `pedclit.cestado`)

- `'p'` = pendiente
- `'s'` = remitido. Para "remitido no facturado": `cestado='s' AND MS_VENTAS_REMITOS.REMITO_FP IS NULL`
- El dropdown de estado es single-select, por eso "pendiente OR remitido" necesita un flag aparte (`forgottenOrders`).

Ver mapeo de estados en [[modulo-makesale]] y la relación pedido↔remito en [[relacion-tablas-ped-alb]].

## Backend — `api-rest-pedidos-laravel`

- `Http/Controllers/Order/OrderList/OrderList.php`: `forgottenOrders` agregado a `allowedFields('list')`. (El controller hace `$request->only(...)` pero usa `$request->all()`, así que el param fluye igual.)
- `Repositories/Order/OrderList/OrderListRepository.php` (`setFilter`): si `forgottenOrders` ∈ `['1','true']`, agrega **solo** la condición de estado `(cestado='p' OR (cestado='s' AND MS_VENTAS_REMITOS.REMITO_FP IS NULL))`. La **fecha la maneja el `between`** normal que envía el front.
- `MS_VENTAS_REMITOS` ya viene joineado en la query base.

## Frontend — `pedidos-web-app-v1`

- `components/Filters/Orders.vue`: nuevo `<a-select>` "Pedidos olvidados" (`forgottenOrders=1`), `forgottenOrdersOptions` en data, sumado a `countByModalFilters`. En `handleChange`:
  - Al activar → setea `query.between = [hace 3 años]_[hace 2 meses]` (formato `DD-MM-YYYY`).
  - Al desactivar → restaura el rango por defecto (15 días). **La fecha nunca queda vacía** (requisito del usuario).
- `components/Filters/General.vue`: el range-picker se keyea sobre `:key="$route.query.between || 'empty'"` para re-montarse al cambiar la fecha. La sincronización picker/tag se hace en `syncDateFromQuery()`, llamado desde el watcher profundo de `$route.query` (el que siempre dispara). En la pantalla `orders` el picker tiene `allow-clear` deshabilitado.

## Fix de TIMEOUT (la parte importante)

- **Síntoma:** al activar el filtro → `SQLSTATE[HY000] ... 20003 Adaptive Server connection timed out`.
- **Causa:** la condición `dfecped < hace 3 meses` sin tope inferior escaneaba ~59.642 órdenes (solo company 4) dentro de la query gigante de listado (joins + subconsultas correlacionadas por fila + GROUP BY de ~50 columnas + ORDER BY). El COUNT solo era rápido (1.2s); el costo es materializar/ordenar todas las filas. Expiraba a los 30s.
- **Fix:** acotar la ventana. El front envía `between` = últimos 3 años excluyendo los últimos 2 meses → la query completa pasó a ~6.3s.
- **Mediciones (company 4):** sin piso → timeout; 2 años → 146 filas / 6.85s; 1 año → 64 / 7.59s; 6 meses → 17 / 5.68s; ventana final 3a–2m → 15 (página) / 6.30s.

## Comportamiento con el filtro de fecha

"Pedidos olvidados" **escribe** en el filtro de fecha (no lo ignora): al marcarlo, el datepicker se llena con la ventana de 3 años y el usuario puede luego acotar ese rango a mano. Nunca queda vacío.

## Commits

- Front: `15df1ee`, `4a59865`, `da3b373`, `5214032`
- Back: `307dedfc`, `da311088`

## Ver también

- [[arquitectura]] — patrón Controller → Service → Repository del listado de órdenes
- [[contexto]] — gotchas de SQL Server y multi-empresa
- [[changelog#2026-06-16 — Filtro Pedidos Olvidados + fix de timeout]]
