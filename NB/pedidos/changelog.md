## 2026-07-14 — Descarga masiva de comprobantes de venta (PDF)

Tarea operativa (no cambio de código): bajar en lote los PDF de comprobantes de venta de **NB DISTRIBUIDORA MAYORISTA SRL** (`companyCode = 4`). Procedimiento completo en [[runbook-descarga-comprobantes-venta]].

- **Pedido:** todos los comprobantes de los **primeros 4 días hábiles** (dentro de los primeros 10 días) de **enero 2024, febrero 2024, mayo 2025 y diciembre 2025** → **1.461 PDFs, 0 fallos** (1.335 facturas, 116 NC, 4 fact. export., 3 ND, 3 FCE). Salida en `/var/www/nb/pedidos/comprobantes de venta/{YYYY-MM}/` + `_manifiesto.json`.
- **Gotcha clave:** el link `comprobantes.lio.red/voucher/F/{id}/{token}` NO es un PDF server-side — es un **SPA Nuxt que arma el PDF con jsPDF en el navegador** (pide JSON a `ms-comprobantes.lio.red/v2/F/{id}/{token}`). `curl` devuelve el HTML del SPA, no el PDF → hay que **renderizar con Chrome headless** e interceptar la descarga.
- **Descargador:** `puppeteer-core` + `google-chrome`, 6 en paralelo (~7 min). `Page.setDownloadBehavior` es global y los workers se pisan → usar `Browser.setDownloadBehavior` (`allowAndName`, `eventsEnabled`) a un dir compartido y **correlacionar cada descarga por `frameId`** (`downloadWillBegin`/`downloadProgress`). Idempotente (saltea existentes).
- **Selección:** SQL directo sobre `FP_FactWebCliEncabezado` con el filtro base del endpoint (`LANULADA=0`, `CAE NOT NULL`, `NCNOTOCASALDONISTOCK IS NULL`, `CODEMP=4`); "día hábil" ≈ Mon–Fri con actividad (salta feriados). Mayo 2025: 1 = feriado y 2–4 finde/puente → primeros hábiles = 5,6,7,8.

---

## 2026-07-03 — LST GLOBAL (cta cte proveedores, intercompañía) + aclaración Crown

Ajuste puntual sobre la cta cte de proveedores Laset comp=11 ([[feature-laset-cuenta-corriente-proveedores]]).

### LST GLOBAL — pasivo intercompañía Laset ⟷ New Bytes Inc. (ahora SÍ se carga)

La hoja **"LST Global"** estaba en el `SKIP` del parser porque su celda "Proveedor" dice el literal **"New Bytes Inc."**. Pero **es una cuenta real**: 831 líneas, 335 facturas / 210 pagos, saldo **A favor/Deuda = 11.294.120,34 USD** (≈7× la suma de todos los demás proveedores juntos). Es el pasivo global de Laset con la casa matriz.

- **Decisión del usuario**: cargarla como proveedor comp=11 **"LST GLOBAL"** (nombre de la pestaña, NO el literal "New Bytes Inc.").
- Ya existía en `FP_Proveedores` (`Id_Proveedor 16681 / CCODPRO 002607`) con 0 movimientos → el import solo linkea + crea master `MS_PROVEEDORES` + 564 movimientos. **No** se dio de alta un proveedor nuevo.
- **Cambios en `scripts/laset_prov_ccte_to_json.py`**: (1) sacar `'LST Global'` del `SKIP`; (2) `if norm(name)=='LST GLOBAL': prov_name='LST GLOBAL'` (evita matchear/crear "New Bytes Inc."); (3) nueva constante `SUMMARY_LABELS` — el loop de movimientos **ignora** filas de resumen que llevan fecha ("NC Disponible", "ADEUDA" con valor en Pagado) → antes generaban pagos espurios en cualquier hoja.
- Verificado en dev: 564 movs, saldo exacto 11.294.120,34, reconcilia. Ajuste de cierre residual 179.901,40 (0,35 % del facturado de 50 M). Snapshot previo `laset:snapshot prov_ccte_lstglobal`.
- **Estado dev**: 111 cuentas comp=11 (110 con movimientos), 6.328 movimientos, todas reconcilian. Σ saldos = **12.914.427,59 USD** (LST GLOBAL 11.294.120,34 + 1.620.307,25 el resto — idéntico al total previo → solo se agregó LST GLOBAL).

### Aclaración cliente Crown (no era bug)

El "movimiento de más" de 30.900 que aparecía en la cta cte del ERP es el **pago de la factura Y25DG005** (30.900), que **sí está en la planilla** (fila 173, columna Pagado). Se ve después del último movimiento visible (23.920, marzo) porque en el archivo ese pago está fechado **31/12/2026** (fecha futura, placeholder de "pagada, fecha exacta desconocida") → ordena al final. Factura + pago se cancelan → saldo Crown = 0, coincide con la planilla. Sin ese pago, Crown quedaría debiendo 30.900. No hay duplicado (una factura y un pago de Y25DG005). Pendiente opcional: normalizar esa fecha futura si molesta en pantalla.

## 2026-06-30 — Cta cte proveedores (alta automática) + Stock por almacén (depósito por línea)

Cierre de dos arcos sobre la operación Laset comp=11 (rama `lasetImportFramework`). Commits back `ed45cfaf`→`6388b771` (proveedores) y `057fefbd` (stock). Docs nuevos: `docs/cuenta-corriente/proveedores.md`, `docs/laset-stock-almacen.md`.

### Cuenta corriente de PROVEEDORES — completa ([[feature-laset-cuenta-corriente-proveedores]])

- **Alta automática de faltantes**: un proveedor pertenece a una sola empresa; las hojas que no matchean ningún proveedor comp=11 (ni por nombre de pestaña ni por el nombre real de la celda "Proveedor") se **dan de alta** en `FP_Proveedores` con `CCODPRO` secuencial (`MAX(CAST(CCODPRO AS INT))+1`, 6 díg.; `ID_PROVEEDOR` es IDENTITY → INSERT sin especificarlo). El parser emite `prov_name` + `nb_inc`; resolución con **paridad NB Inc** (Seaside NB Inc 002641 ≠ Seaside 002454). El nombre real evita duplicar existentes (PNY Tech Asia → 002449). Idempotente. El modal de `/syncLaset` muestra "Proveedores a dar de alta" antes de confirmar.
- **Estado final**: **110 proveedores comp=11**, todos reconcilian, Σ saldos ≈ 1.620.307,25 USD. (83→114 filas en FP comp=11; 31 altas `CCODPRO 002611–002641`.)
- **Excluidos a propósito** (SKIP del parser): **Transcargo** (fletes — hojas "Trans"/"Trans Laset"; decisión del usuario: NO va en comp=11), `Egre`/`Egresos` (logs globales de todos los proveedores), `Pendiente Euros` (lista de contactos), `LST Global` (=NB Inc), templates y `Cálculos Trans`. **No falta ninguna cuenta real.**

### Stock por almacén comp=11 ([[feature-laset-stock-almacen]])

- **Bug** (`LasetImportFaseCCommand`): el `pedclil` heredaba el `ID_ALMACEN` del **encabezado** del pedido en vez del `deposito` de cada línea → pedidos multi-depósito dejaban líneas en el almacén equivocado → stock negativo en un almacén e inflado en otro (el total por artículo queda bien). La compra (pedprol/albprol) sí respeta el depósito por línea.
- **Fix importador**: el depósito entra en la clave de consolidación de `pedclil` (`pedclit_key|ID_Articulo|ID_ALMACEN`); cada línea va a su almacén (+ ajuste en linkeo de asignación 4c y dup-links 4d).
- **Fix retroactivo** `laset:fix-stock-almacen-comp11` (`{--dry-run}`, comp=11, idempotente): re-apunta ventas (pedclil+albclil) al depósito de la planilla por DELTA exacto + balancea negativos remanentes con **transferencias inter-depósito** (planilla compró en un depósito y vendió desde otro). Invariante: stock total por artículo no cambia. Wireado a `laset:run-import-job` (paso 3.6). Aplicado dev: **14 → 0 almacenes negativos**.
- **Gotcha planilla-vs-físico** (distinto del bug): el total comp=11 = lo que dice la planilla (comprado − facturado); si el archivo físico difiere (G5060: archivo 921 vs ERP 833) es una compra real no registrada en la planilla, NO un bug — no detectable desde la DB (cruzar `stock_comp11.csv` por SKU). Export de 218 artículos generado para diff.

Archivos: back `scripts/laset_prov_ccte_to_json.py`, `app/Services/Laset/LasetProvCtaCteImportService.php`, `app/Console/Commands/{LasetProvCtaCteImportCommand,LasetImportFaseCCommand,LasetFixStockAlmacenComp11Command,LasetRunImportJobCommand}.php`, `app/Http/Controllers/Laset/LasetProvCtaCteImportRun.php`, `routes/api.php`. Front `plugins/api.js`, `pages/syncLaset.vue`.

---

## 2026-06-18 — Descarga xlsx de listados (pedidos y clientes)

Botón (solo icono `download`) en las pestañas de **pedidos** y **clientes** que descarga el listado actual a `.xlsx` **respetando todos los filtros de la URL**. Detalle completo en [[feature-descarga-listado-xlsx]]. Rama `descargarListadoXlsx` (ambos repos). Back `d6c7e13` / cherry-pick Gamma `b433f53`; front `2d4ba8e` / cherry-pick gamma `64d4c9d`.

- **Endpoint nuevo:** `GET /v1/orders/download` — replica el patrón de `clients/download` (genera el xlsx en disco `public/downloads`, responde `{ success, path }`).
- **Clave de implementación:** el service **reutiliza `OrderListRepository::getOrders($filters, ['offset'=>0,'limit'=>ORDER_DOWNLOAD_MAX_ROWS])`** — el mismo método público del listado, sin paginar → mismas filas, filtros y totales que ve el usuario, sin duplicar la query gigante.
- **Medio de envío:** se resuelve `id → nombre` vía `LO.dbo.mediosEnvio` (`ShippingMethodRepository`).
- **Clientes:** ya tenía `clients/download`; solo se unificó el botón a solo-icono.

Archivos: back `OrderDownloadController.php`, `OrderDownloadService.php`, `ExcelExportOrders.php`, `routes/api.php`. Front `components/Filters/Orders.vue`, `components/Filters/Clients.vue`.

---

## 2026-06-17 — Ranking de vendedores (travel miles) + Incentivo Netac

Dos features de dashboard previas a la descarga xlsx (commits back/front `bd063bd`, `7275ca1`, `0083994`).

- **Ranking de vendedores** ([[feature-ranking-vendedores]], rama `rankingTravelVendedores`): pestaña "Ranking de vendedores" junto a "Ranking de aceleración"; rankea vendedores por la suma de **puntos** (travel miles) que generan sus clientes, con modal de desglose por objetivo cumplido (cliente, objetivo, fecha, puntos). Endpoints `clientsObjectives/acelerateRankingSellers` y `clientsObjectives/sellers/{sellerId}/travelMiles`. Incluye descripción del juego "NB Travel Mundial de resellers". La columna "Millas" se renombró a "Puntos".
- **Incentivo Netac** ([[feature-incentivo-netac]], rama `incentivoNetac`): reemplaza el "Incentivo Gigabyte" (oculto, no borrado). Suma unidades vendidas de productos marca **Netac** (`articulo.Id_Marca = 211`), solo categorías Memorias (`ID_FAMILIA=1`) y Discos SSD (`ID_FAMILIA=56`); cada 12 unidades = USD 4; período 10–24/06/2026. Endpoint `objectives/netacIncentive` + detalle por vendedor (`objectives/netacIncentive/sellers/{sellerId}`) con producto, fecha y pedido (pedclit/pedclil). Conteo por remitos.

---

## 2026-06-16 — Filtro Pedidos Olvidados + fix de timeout

Nuevo filtro oculto en la lista de órdenes: **"Pedidos olvidados"** — órdenes pendientes o remitidas (no facturadas) con más de 2 meses, hasta 3 años de antigüedad. Detalle completo en [[feature-pedidos-olvidados]]. Rama `feature/pedidos-olvidados` (ambos repos). Commits front `15df1ee`→`5214032`, back `307dedfc`/`da311088`.

### Highlights

- **Fix de timeout (clave):** la versión inicial usaba `dfecped < hace 3 meses` sin tope inferior → escaneaba ~59.642 órdenes en la query gigante de listado (joins + subconsultas correlacionadas + GROUP BY de ~50 cols) → `Adaptive Server connection timed out` a los 30s. Solución: acotar la ventana a 3 años (el front envía `between` = 3 años atrás excluyendo los últimos 2 meses) → query completa ~6.3s.
- **Estado:** `forgottenOrders=1` agrega solo `(cestado='p' OR (cestado='s' AND MS_VENTAS_REMITOS.REMITO_FP IS NULL))`; la fecha la maneja el `between` normal.
- **UX (decisión del usuario):** el filtro **escribe** el rango de fecha en el datepicker (3 años → 2 meses), nunca lo deja vacío. Al desactivar, restaura los 15 días por defecto.
- **Fix de re-render:** el range-picker se keyea sobre `$route.query.between` y se sincroniza vía `syncDateFromQuery()` en el watcher profundo de `$route.query` (el path-watcher específico no era confiable).

Archivos: back `OrderList.php`, `OrderListRepository.php`. Front `components/Filters/Orders.vue`, `components/Filters/General.vue`.

---

## 2026-06-02 — Import Laset: reconciliación, dedup multi-renglón y modelo "snapshot completo"

Sesión larga depurando casos reales del import comp=11 (rama `lasetImportFramework`). Varios bugs sistémicos que sólo aparecían al correr el pipeline real. Commits back `7e92c5ee` → `32f49b81`. Modelo final consolidado en [[feature-laset-import]].

### Bugs encontrados y arreglados

- **Stock-only atascado en IGNORED** (44.5k u perdidas): el paso 4a "basura" de `aggregate-match` re-pisaba a IGNORED las filas `year=1900` que el 4a-pre acababa de marcar STOCK_ONLY. Fix: excluir STOCK_ONLY/STOCK_ONLY_SUPERSEDED del `NOT IN`. Además Fase C ahora corre `fix-stock-only` SIEMPRE (rompe el chicken-egg: con todo en IGNORED nunca se llamaba).
- **Doble conteo de stock** (reconciliación −33k): `fix-stock-only` escribía la qty stock-only en `pedprol` Y en `stocks`, y Fase D la re-derivaba de `pedprol−pedclil` → 2×. Fix: `--skip-stock` (Fase C lo pasa) → **Fase D es la única fuente de verdad del stock**.
- **Stock-only acumulado entre corridas** (reconciliación +6861): importar incremental aplicaba snapshots viejos de stock-only encima de los nuevos. Fix: ganador stock-only por `(vendor_pi, sku, depósito)` (no por factura) + modelo snapshot-completo (abajo).
- **Compra partida en 2 OCs + venta duplicada** (caso 14178/14190): la factura del proveedor llega en un batch posterior a la proforma; filas con factura vacía generaban un pedprot extra. Fix: canonicalización de factura en Fase C (si un `(prov, vendor_pi)` tiene 1 sola factura no vacía, las vacías la adoptan).
- **Dedup que comía renglones** (caso 9800X3D, venta A-3765): un SKU listado 2 veces con misma cantidad en la misma factura perdía unidades. Causa: el dedup por `row_hash` de `ReimportLaset` descartaba renglones idénticos legítimos. Fix doble: (1) Fase C dedup cross-batch = "batch más completo gana" conservando todas las filas del grupo; (2) `ReimportLaset` ya no deduplica por hash.
- **Fecha inválida en compras stock-only** (14204): cat D tomaba `dFecPed` de `fecha_arribo` (vacío). Fix: usa `invoice_date`.
- **CSUPROF_TEMP vacío**: `cExped` es varchar(20) y trunca el vendor_pi; `CSUPROF_TEMP` (nvarchar 50) guarda el PI completo. Fase C/stock-only lo setean + backfill `laset:fix-csuprof-temp` (+ botón en /syncLaset).

### Decisión de modelo (usuario): "la planilla más reciente es la verdad"

- **Reimportar planilla = REEMPLAZA el staging completo** (borra batches/filas previos, inserta el snapshot nuevo como único batch). Antes acumulaba versiones viejas → staging inflado (>5000 ids → error) y datos obsoletos (ej. venta A-3748 ya no presente) en la reconciliación.
- Límite `staging_ids` subido 5000 → 100000 en import-jobs.
- Resultado: con un solo batch (la planilla vigente) Fase C deduplica limpio y no hay interferencia de datos viejos.

### Gotcha de verificación

El guard de auto-mode bloquea correr Fase C/D (modifican ERP compartido) desde la sesión → se verificó con simulaciones read-only en tinker; el usuario corre wipe+reimport por la UI.

Archivos: `Console/Commands/LasetAggregateMatchCommand.php`, `LasetImportFaseCCommand.php`, `LasetFixStockOnlyPedprolCommand.php`, `LasetFixCsuprofTempCommand.php`, `Services/Laset/{WipeTransactionalService,FixCsuprofTempComp11Service}.php`, `Http/Controllers/Laset/{ReimportLaset,LasetFixCsuprofTempRun,LasetImportJobCreate,LasetImportJobPreview}.php`. Front: `pages/syncLaset.vue`, `plugins/api.js`.

---

## 2026-05-21 (cont.) — integrarECCN: permiso, detalle de orden y carga manual

Continuación del feature **[[feature-integrar-eccn|integrarECCN]]** — ahora el ECCN se ve y se carga desde el detalle de la orden. Commiteado y pusheado a la rama `integrarECCN` (back `2c87867e`, front `d0083b6`).

- **Permiso RBAC `eccView`** — columna `NB_WEB.dbo.permisos_agente.eccView` (SQL `2026_05_21_002_add_ecc_view_permission.sql`, `DEFAULT 0`). Agregado a las dos queries de `AuthRepository` (`login()` + `getByToken()`) y a `UserDto` → viaja en el JWT y en el objeto `user`. Front: `$can('eccView')` en `plugins/permissions.js`. Activado en dev a 5 usuarios (agente 12 Catriel + 4 de Laset comp=11). **Gotcha**: tokens previos al deploy no lo traen → re-login necesario (igual que `lasetView`).
- **ECCN por ítem en el detalle de orden** (`GET /v1/orders/{branch}-{order}`) — cada ítem trae `ecc: {value, editable}` **solo si el usuario tiene el permiso**. El JOIN se concatena condicionalmente a la query de `OrderRepository::getOrderDetail` (`$eccSelect`/`$eccApply`): sin permiso la query queda idéntica a la original (cero penalización de performance). `value` = ECCN resuelto por (familia, proveedor de la OC asignada, vía `OUTER APPLY TOP 1` sin fan-out); `editable` = la clave es resoluble. Gating del JSON: `OrderItemDto::$ecc` es propiedad tipada sin default + `property_exists` → `json_encode` la omite sin permiso.
- **Carga manual del ECCN** — `POST /v1/ecc` (`Http/Controllers/Ecc/EccStore.php`, invokable): body `{pedclilId, eccn}`, resuelve `(company_code, id_familia, ccodpro)` desde la línea y hace upsert en `ecc_familia_proveedor` con `origen='M'` (protege la edición de un futuro `ecc:import-categorias`). Gateado por `eccView` (403), 422 si la línea no tiene familia/OC.
- **Frontend** (`Detail.vue`) — columna **ECCN** en la tabla de ítems (`visible: $can('eccView')`). Si hay valor lo muestra; si está vacío y es editable, un **lápiz** abre un popover inline (input + Guardar) → `POST /v1/ecc` → `refreshModalOrder` re-trae el detalle (así toda línea con la misma clave deja de verse en null). `$api.ecc.save()` en `plugins/api.js`.

Archivos back: `Dto/Auth/UserDto.php`, `Dto/Order/OrderItemDto.php`, `Repositories/Auth/AuthRepository.php`, `Repositories/Order/OrderRepository.php`, `Http/Controllers/Ecc/EccStore.php`, `routes/api.php`, `database/sql/2026_05_21_002_{add,drop}_ecc_view_permission.sql`.
Archivos front: `components/Orders/Detail.vue`, `plugins/permissions.js`, `plugins/api.js`.

**Pendiente prod**: los 3 SQL (`2026_05_21_00{1,2}`) están aplicados solo en dev.

---

## 2026-05-21 — Feature integrarECCN (paso 1)

Arranque del feature **[[feature-integrar-eccn|integrarECCN]]** — clasificación ECCN (Export Control Classification Number) de la operación de exportación de Laset (`companyCode=11`). El ECCN depende de **dos ejes**: el tipo de producto (familia) y el proveedor.

- **Rama `integrarECCN`** creada en ambos repos desde `lasetImportFramework`.
- **Tabla nueva `ecc_familia_proveedor`** (`NewBytes_DBF.dbo`) — matriz de doble entrada familia × proveedor → `eccn` + `codigo_arancelario`. FK lógicas (no enforced) a `familias`/`FP_Proveedores`. Columna `origen` `C`=CSV / `M`=manual. SQL `database/sql/2026_05_21_001_create_ecc_familia_proveedor.sql` (+ drop). **Aplicado en dev**.
- **Comando `ecc:import-categorias`** (`EccImportCategoriasCommand`) — lee `database/data/eccCategorias.csv`, resuelve proveedor/familia por `companyCode` con match exacto normalizado (mayúsculas, sin puntos/comas), descarta filas sin match en ambos ejes. Idempotente: borra+reinserta `origen='C'`, respeta `origen='M'`.
- **CSV fuente** `eccCategorias.csv` versionado en `database/data/`.
- **Ejecutado en dev**: **94 vínculos** cargados comp=11, idempotencia verificada. Sin match: 2 proveedores (`NEW BYTES INC`=comp 4, `PNY TECHNOLOGIES INC` inexistente comp=11) y 18 categorías del CSV sin familia comp=11.
- **Decisión** (usuario): solo matches exactos, NO fuzzy. `CABLES`↔`CABLE`, `ODD`↔`OPTICAL DRIVE`, `FAN`↔`AIR COOLING` quedan afuera a propósito.
- **Gotcha workflow**: queries ad-hoc a SQL Server vía el container — usar archivo PHP + `php artisan tinker archivo.php`, no `--execute` (el escaping shell→tinker rompe con `T_NS_SEPARATOR`). El repo `app/` está montado en `/var/www/app/` del container → los archivos del repo se ven adentro sin `docker cp`.

Archivos: `api-rest-pedidos-laravel/app/database/sql/2026_05_21_001_{create,drop}_ecc_familia_proveedor.sql`, `database/data/eccCategorias.csv`, `app/Console/Commands/EccImportCategoriasCommand.php`, `database/sql/README.md`, `CLAUDE.md`.

Branch: `integrarECCN` (ambos repos, basada en `lasetImportFramework`).

---

## 2026-05-20 (cont.) — Botón "Importar seleccionadas" + auto-create de artículos + cadena de fixes

Sesión larga sobre el viewer Sync Laset. Se agregó el flujo de importación al ERP desde la UI y se corrigieron varios bugs descubiertos al probarlo end-to-end.

### Importar al ERP desde la UI

- **Tabla `laset_import_jobs`** (SQL `2026_05_20_002`, aplicado) — estado de cada job: status, phase, progress, result JSON, reconciliation JSON, error.
- **`laset:run-import-job {jobId}`** — orquestador async: corre aggregate-match (si hay UNMATCHED/NEW) → Fase C → Fase D → reconciliación, escribiendo progreso a la tabla.
- **Controllers** `LasetImportJobCreate` (POST, dispara `nohup php artisan` en background), `LasetImportJobStatus` (GET polling), `LasetImportJobPreview` (POST, calcula closure sin crear job).
- **`LasetSelectionClosure`** — cierre transitivo: tildar 1 fila arrastra todas las de su OC y su venta, recursivamente (BFS sobre grafo bipartito fila↔OC↔venta). Necesario para fidelidad: importar el subgrafo conexo completo. En Laset el grafo es denso (2 filas → 1755 expandidas).
- **Frontend** `syncLaset.vue`: checkboxes de selección, botón "Importar seleccionadas (N)", 3 modales (preview con compras/ventas/stock/SKUs a auto-crear, progreso con polling 2s, resultado con tabla de deltas de reconciliación).

### Auto-create de artículos y marcas (Fase C)

- Antes los SKUs sin alta en `articulo` comp=11 bloqueaban la fila. Ahora Fase C los **auto-crea**: clona del gemelo de otra company si existe, o crea desde la planilla (description + marca). Marcas faltantes se crean en `FP_Marcas` (tabla global, sin companyCode).
- `aggregate-match`: `NO_BRIDGE` ahora → `MATCHED score=70` ("auto-creable"), ya no `UNMATCHED`. Heurística service-like (`Flete`, `NC %`, `Ajuste%`, `Nuevo precio %`, `Gastos%`, SKU con `$` o > 40 chars) → `IGNORED`.
- `--staging-ids=` agregado a `laset:import-fase-c` para filtrar al subset del job.

### Cadena de bugs corregidos (descubiertos probando)

- **`[national]`** es palabra reservada SQL Server → brackets en todas las columnas del INSERT de `articulo`.
- **`ivaCompra`/`ivaVenta`** son columnas calculadas → fuera del INSERT.
- **URU/ASI** estaban hardcodeados como 17/18 en `DEPOSITO_TO_CCODALM` de Fase C; los reales en `FP_Almacen` comp=11 son **14/15**. Corregido.
- **`aggregate-match` no procesaba `NEW`** (solo `UNMATCHED`) → las filas del reimport via UI quedaban sin clasificar. Fix: `WHERE match_status IN ('UNMATCHED','NEW')`.
- **Gotcha trigger `tg_pedclit_cestado_asignacion`**: promueve asignación V→C en ON UPDATE de `pedclit.cestado`. Fase C inserta `pedclit` directo en `'S'` → el trigger nunca corre → 2644 asignaciones comp=11 quedaron en `'V'` sobre ventas ya servidas. Fix: UPDATE bulk 2644 → `'C'` + Fase C ahora inserta el estado derivado del `cestado`.
- **Stock huérfano**: 50 grupos (SKU+almacén) comp=11 con `compras − ventas − stock ≠ 0` por residuos pre-feature. Reset global aplicado (−1601 unidades netas), 100% aislado a comp=11. Snapshot `pre_reset_huerfanos_20260520_2200`.
- **`vw_pedclil_estado_asignacion`** solo incluía `cestado='P'` → los pedidos Laset (servidos) no aparecían en el listado ni en el modal AsignarOC. SQL `2026_05_20_003`: la vista ahora incluye `cestado='S'` **solo para companyCode=11** (NB/NBE/LO intactas), join cuenta `estado IN ('V','C')`, nueva columna `pedido_estado`. `lineasSinAsignacion` (FIFO) filtra `pedido_estado='P'`.
- **`AsignacionRepository::asignacionesDeLinea`**: (1) no traía nombre de proveedor → agregado JOIN `FP_Proveedores` (`proveedor_nombre` + `proforma`); (2) el JOIN a `pedprol` por `cRef` duplicaba filas en OCs multi-línea del mismo SKU → corregido a JOIN por `nLinea`.

### Infra Docker

- `docker/php/apache-uploads.ini` montado en `docker-compose.yml` → `upload_max_filesize=100M`.
- `python3 + openpyxl` agregados al `Dockerfile`.

### Snapshots de seguridad creados

`pre-fix-job-cleanup-20260520-2005`, `pre_fase_c_fix_national_2150`, `pre_reset_huerfanos_20260520_2200`.

### Pendiente / no resuelto por diseño

- 4 `pedprot` + 5 `pedclit` con `cCodAlm='SAF'` comp=11 — data productiva cargada a mano por un operador (almacén equivocado, SAF es de NB). No son del feature; se dejaron como están. Sus 8 `pedclil` figuran como `SIN_ASIGNAR` (legítimo).
- El `registro_stock` del reset de huérfanos no se insertó (bug `||` vs `+` en el script one-shot); el UPDATE de `stocks` sí quedó aplicado.

---

## 2026-05-20 — Reimport de planilla Laset via UI (botón Examinar)

Feature nuevo: el usuario puede subir una `.xlsx` desde la UI de Sync Laset y el sistema agrega solo las filas nuevas, sin tocar las históricas.

**Backend** ([[feature-laset-import#14. Reimport de planilla via UI (2026-05-20)]]):

- SQL `2026_05_20_001_add_laset_reimport_support.sql` (+ drop simétrico). Aplicado contra `NewBytes_DBF` con éxito. Agrega:
  - `laset_import_batches.headers NVARCHAR(MAX)` — JSON con los 67 nombres canónicos de columna.
  - `laset_import_staging.row_hash CHAR(64)` — SHA256 normalizado de las 67 cols crudas.
  - Recreate `CK_laset_staging_match_status` para aceptar `'NEW'`.
  - Index `ix_laset_staging_row_hash`.
- `app/Support/LasetRowHasher.php` — hash determinístico: trim por celda, separador `\x01`, sha256 hex. Mismo algoritmo en backfill y reimport para asegurar dedup.
- `app/Console/Commands/LasetBackfillRowHashCommand.php` (`laset:backfill-row-hash [--xlsx=…]`). Recalcula `row_hash` con UPDATE FROM JOIN single-statement (dblib-safe). Si se pasa `--xlsx`, además guarda headers canónicos en el primer batch que los tenga NULL. **Ejecutado en dev**: 3007 filas hasheadas.
- `app/Http/Controllers/Laset/ReimportLaset.php` — `POST /v1/laset/reimport` (multipart `file`). Validación: max 50 MB, mime `xlsx`. Flujo:
  1. Mueve el upload a tmp + corre `scripts/laset_xlsx_to_json.py` (sigue siendo el único parser viable — PhpSpreadsheet inviable, ver [[memoria]]).
  2. Compara headers entrantes vs canónicos guardados en `laset_import_batches.headers` (primer batch con headers NOT NULL). Si **no hay canónicos aún**, este upload los **establece**; si hay y difieren → `422` con diff `[{index, expected, got}, …]`.
  3. Carga set en memoria de todos los `row_hash` existentes (~3k entries). Para cada fila calcula hash y la clasifica `existing` / `dup_in_file` / `new`.
  4. Crea nuevo batch + INSERT chunked de las nuevas con `match_status='NEW'`. Devuelve `{batch_id, total_in_file, new_rows, existing_rows, dup_in_file, header_check.mode}`.
- `scripts/laset_xlsx_to_json.py` ahora emite también `headers: [...]` (fila 1 cruda).
- `routes/api.php` agrega `POST /v1/laset/reimport`.

**Frontend** (`pedidos-web-app-v1/app`):

- `pages/syncLaset.vue`: botón **"Reimportar planilla"** (tipo `primary`, icon `upload`) al lado de los counters, con loading state. Usa `<a-upload :before-upload>` para interceptar el archivo y disparar `store.reimport`. Si el backend responde 422 con `differences`, muestra `notification.error` con las 8 primeras diffs ("col 12: esperado «Qty», llegó «Cant.»"). Si OK, `notification.success` con resumen. Color `purple` para tags `NEW` en counters y filas.
- `plugins/api.js`: `laset.reimport(file)` — POST multipart.
- `store/syncLaset.js`: action `reimport` que despacha al endpoint, setea el nuevo `batchId` y refresca summary + staging.

**Infraestructura Docker** (permanente, comiteable):

- `docker/php/apache-uploads.ini` (nuevo) + montaje en `docker-compose.yml` → `/etc/php/8.1/apache2/conf.d/99-laset-uploads.ini:ro`. Sube `upload_max_filesize=100M`, `post_max_size=110M`, `memory_limit=512M`. Antes Apache mod_php usaba el default Ubuntu (`2M/8M`) y rechazaba el xlsx histórico. **Probado**: container recreado lee los valores del archivo del repo.
- `docker/Dockerfile` agrega `python3 python3-pip` al apt-get + `pip3 install openpyxl==3.1.2`. El parser Python era inejecutable runtime sin esto.

**Comportamiento esperado**:

- Misma planilla histórica → `new_rows=0`, `existing_rows=3007`.
- Planilla con filas extra → solo entran las nuevas, con `match_status='NEW'`, sin matching ERP (deliberado — quedan visibles en el viewer para auditoría manual).
- Cambio de columna (renombre/reorden) → `422`, no se crea batch.

**Pendiente operativo**: copiar `docs/laser.xlsx` a `app/docs/` (o pasarlo manualmente al comando) para que `laset:backfill-row-hash --xlsx=…` registre los headers canónicos desde la planilla histórica. Mientras tanto, el primer reimport via UI los establece automáticamente.

---

## 2026-05-18 — Frontend

Merges a `development` (pull de hoy):

- fix: **etiquetas se borran al agregar producto** (PED-1358) — las etiquetas de la orden desaparecían al agregar un nuevo artículo; relacionado con flag "Mostrar en Orden". `Detail.vue`.
- feat: **comentario de factura** (PED-1363) — se puede agregar un comentario al generar la factura. `Detail.vue` + `CloseSale.vue` (170 líneas modificadas).
- fix: **liquidación — moneda mostrada** (PED-1359) — en LASET (`companyCode=11`) los medios de pago en pesos no debían verse. Refactor usa permiso `.can('viewPesos')` en vez de hardcodear divisas. `CloseSale.vue` + `plugins/api.js`.
- feat: **filtro en selector de forwarders** (PED-1361) — al escribir en el selector de forwarders/condición de venta en el detalle de OC, ahora filtra. Mejoras de tipografía y padding. `Detail.vue`.

Archivos: `app/components/Orders/CloseSale.vue`, `app/components/Orders/Detail.vue`, `app/layouts/basic.vue`, `app/plugins/api.js`.

Ramas nuevas recibidas (aún sin mergear a `development`): `PED-1362-comentario-factura`, `PED-1365-api-refactor`, `LAW-69-api-ped-refactor`.


## 2026-05-13

- feat: **nuevo medio de pago id=21 con comportamiento de pago diferido** — funciona igual que el id=16 (pago diferido): verifica crédito disponible del cliente antes de liquidar y autoriza directo a status 2 (autorizado pendiente de preparar).
  - Archivos: `Services/Liquidate/LiquidateServices.php` (constante `DEFERRED_PAYMENT_21 = 21`, condición en `verifyPaymentDeferred`), `Services/Liquidate/CreateOrder.php` (mapa `payment()` y condición en `authorization()`)
  - Rama: `deve-fix-linea-creidto-laset` (basada en `Development`, pusheada a origin)

# Changelog

Registro de cambios del proyecto, agrupado por fecha.

## 2026-04-25

Continuación de iteraciones sobre [[feature-asignacion-oc|Asignación OC ↔ Venta]]:

- feat: **modo solo lectura para pedidos remitidos** — el modal se puede abrir con `pedclit.cestado='S'` pero todo queda deshabilitado (inputs, checkboxes, botones de acción). Alerta info arriba, botón cambia de ✏️ a 👁️ en `Detail.vue`, footer solo "Cerrar". Acepta asignaciones en estado `'V'` o `'C'` (consumidas por el trigger). Genera filas huérfanas para OCs cuyo saldo ya se agotó y no vienen en `candidatasFifo`.
- feat: **persistencia del checkbox "costo seleccionado" en DB** — nueva columna `pedclil_oc_asignacion.costo_seleccionado BIT NOT NULL DEFAULT 0`. Reemplaza localStorage (que era por-browser). Ahora portable entre máquinas. Camino: PUT items incluyen flag → `ReemplazarAsignacionRequest` valida → service propaga → `insertAsignacion` graba → `asignacionesDeLinea` devuelve → modal precarga.
- feat: **extender duración de sesión JWT a 60 días** — `.env backend` `JWT_EXPIRATION_TIME="now + 60 days"`; `nuxt.config.js` `refreshToken.maxAge = 60 * 60 * 24 * 60`. Rationale: evitar relogins operativos frecuentes. Rotar `JWT_SIGNATURE_KEY` si hay filtración.
- infra: scripts SQL nuevos `database/sql/2026_04_25_001_{add,drop}_costo_seleccionado.sql` — idempotentes, con `USE [NewBytes_DBF]; GO` y `sys.columns + sys.tables` en lugar de `INFORMATION_SCHEMA`.
- gotcha: **SSMS pegar apply+drop en la misma ventana los ejecuta a ambos** → la columna apareció y desapareció, rompiendo `asignacionesDeLinea` con *"Invalid column name 'costo_seleccionado'"*. Fix: tratar cada script como archivo separado.
- gotcha: `SET IMPLICIT_TRANSACTIONS ON` (default en algunas sesiones SSMS) produce warning cosmético "ROLLBACK TRANSACTION sin BEGIN TRANSACTION" en los DDL. Ignorar, o `SET IMPLICIT_TRANSACTIONS OFF;` arriba del script.

Archivos:
- Backend: `Asignacion/AsignacionRepository.php` (SELECT + INSERT con `costo_seleccionado`), `Asignacion/AsignacionService.php` (propagación), `Http/Requests/Asignacion/ReemplazarAsignacionRequest.php` (validación), `database/sql/2026_04_25_001_*.sql`, `.env` (JWT_EXPIRATION_TIME).
- Frontend: `Modal/AsignarOCModal.vue` (prop `readOnly`, filas huérfanas, checkbox persistido, footer condicional), `Orders/Detail.vue` (ícono dinámico edit/eye, `:read-only="!isPending"`), `nuxt.config.js` (refreshToken maxAge).
- Docs: `docs/asignacion-oc-pedclil.md`, `CLAUDE.md`.

**Deploy**:
- Frontend: commit de `nuxt.config.js` ya pusheado a `feature/asignacion-oc-pedclil` (4a36d6c). El resto de cambios aún sin committear.
- Backend: editar `.env` en el servidor + `config:clear` + correr `2026_04_25_001_add_costo_seleccionado.sql` en SQL Server (solo el apply, no el drop).

## 2026-04-24

Iteraciones sobre [[feature-asignacion-oc|Asignación OC ↔ Venta]] post primer merge a Development:

- feat: **`cantidad: 0` = eliminar item** — el endpoint `PUT /v1/asignaciones/lineas/{id}` ahora ignora silenciosamente items con cantidad 0 en vez de tirar 422.
- feat: **items vacíos / todos en 0 = liberar todo** — short-circuit en `reemplazarAsignacionLinea` que actúa como `DELETE`, devolviendo `liberadas` extra en el payload.
- feat: **columna Proveedor** en el modal — JOIN `vw_saldo_oc → PedProT → FP_Proveedores` en `candidatasFifo` expone `proveedor_nombre`. UI con `ellipsis: true` por nombres largos.
- feat: **columna Proforma** en el modal — `pt.CSUPROF_TEMP` propagada en `candidatasFifo` y mapeada en la fila.
- feat: **link OC clickeable** — el número de OC abre `https://compras.saftel.com/orders?currentPage=1&search={oc}&between=...&companyCode={cc}` en nueva pestaña.
- fix: **modal no auto-sugiere FIFO si ya hay vigentes** al reabrir — antes proponía cantidades de FIFO para OCs sin vigente, lo que confundía al operador (parecía que el save no había funcionado). Ahora respeta lo guardado y deja el resto en 0; el botón "Aplicar FIFO" sigue disponible para redistribuir.
- chore: rama frontend rebaseada sobre `Development` actual (incluye refactor `AsignarOcModalMejoras`: z-index modal, focus en input cantidad, estado P/S con label "Pendiente"/"Remitida"). Force-push con `--force-with-lease`.

**Tercera tanda de iteraciones (misma fecha, flujo "Guardar con costo" + UX del dropdown):**

- feat: **título dinámico del modal** — `{branch} - {order} - {id_articulo} - {nombre_producto} (Asignar línea de compra)`. Requiere `articulo.cDetalle` (LEFT JOIN en `pedclilInfo`).
- feat: **checkbox por fila en columna Costo** — permite seleccionar qué OCs usar para el cálculo del costo promedio. Estado persiste en `localStorage['asignarOC.costoTildados.{pedclilId}']` entre aperturas del modal.
- feat: **bloque "Costo promedio ponderado"** debajo de los alerts — fórmula `Σ(costo × cantidad) / Σ(cantidad)` sobre filas tildadas con cantidad > 0. Si hay una sola fila muestra "Costo seleccionado: X"; si son múltiples, "Costo promedio ponderado (N OCs · X u): Y".
- feat: **botón "Guardar con costo"** en footer custom del modal — además de persistir la asignación OC, hace `PATCH /v1/orders/addItem` con `costForSale = promedio ponderado`. `Detail.vue::onAsignacionGuardada` escucha `saved: { conCosto }` y refresca el detalle si aplica.
- feat: **tag "ASIGNADA"** (violeta) en el dropdown de Costo de `Detail.vue` — heurística: compara `Math.round(costForSale * 100) / 100 === store.getters['asignaciones/costoPonderadoPorLinea'](...)`. Requiere que `asignacionesDeLinea` traiga `costo` (JOIN a `pedprol.nPreDiv`).
- fix: **redondeo consistente (bug 139,73 vs 139,72)** — `toLocaleString` y `toFixed` dan resultados distintos en bordes tipo `139.725`. Reemplazado por `Math.round((x + Number.EPSILON) * 100) / 100` en modal Y store, para que match exacto sea posible.
- feat: **dropdown de Costo rediseñado** en `Detail.vue` — cada opción es `precio (monospace, verde) + meta (bandera + proveedor · depósito)` con tags semánticos (ACTUAL / PROMEDIO / ASIGNADA). `dropdown-match-select-width=false` + `minWidth: 320px` para que entre todo. Tabular-nums alinea los precios como columna.
- feat: **endpoint `pedclilInfo` extendido** — ahora retorna `producto_nombre`, `id_almacen`, `lista_precio`, `npreunit` (para armar el PATCH de addItem) y se propagan en el payload de `sugerirFifo`.
- infra: **`selectedPrice` del PATCH `/orders/addItem`** debe ser `pedclil.npreunit` (precio unitario real), NO `listaPrecio` (código de lista). El backend valida `> 0` — mandar 0 tira *"No se permite un precio menor o igual a 0"*.

Archivos:
- Backend: `Asignacion/AsignacionRepository.php` (+3 JOINs en `pedclilInfo`, +costo en `asignacionesDeLinea`), `Asignacion/AsignacionService.php` (propaga campos nuevos).
- Frontend: `Modal/AsignarOCModal.vue`, `Orders/Detail.vue` (método `costoVieneDeAsignacion`, slot de costo rediseñado, handler `onAsignacionGuardada`), `store/asignaciones.js` (+getter `costoPonderadoPorLinea`).
- Docs: `docs/asignacion-oc-pedclil.md`, `CLAUDE.md`.

**Segunda tanda de iteraciones (misma fecha, nuevas features de contexto en el modal):**

- feat: **columna Costo** en el modal — `pedprol.nPreDiv` joineado por `nNumPed + cRef` en `candidatasFifo`. Formato `es-AR` con 2 decimales. Width del modal pasó a 900px.
- feat: **endpoint `/v1/asignaciones/stock-almacenes`** (GET) + método `AsignacionRepository::stockPorAlmacen` → stock físico del SKU por depósito (JOIN `stocks + FP_Almacen`, filtra `deleted_at IS NULL` y `nstock > 0 OR reservado > 0`).
- feat: **endpoint `/v1/asignaciones/comprometido`** (GET) + métodos `pedidosPendientesPorArticulo` y `remitosSinFacturarPorArticulo` → devuelve `{pedidos, remitos}` del mismo SKU (pedidos = `pedclit.cestado='P'` misma company; remitos = `albclit.lfacturado=0`). Top 50 de cada uno.
- feat: **bloques de contexto en el modal** — chips de stock por depósito debajo de la tabla + `a-collapse` con dos paneles (órdenes pendientes / remitos sin facturar) que el operador puede expandir para ver qué compromete el SKU. Contexto read-only **fuera** del `<a-table>` editable (patrón [[feedback_modal_contexto_vs_edicion|separar edición de contexto]] — ver memoria local).
- docs: [[feature-asignacion-oc-cookbook|cookbook]] actualizado con receta nueva "Agregar bloque de contexto al modal", queries SQL de stock/compromisos, curls ejecutables. [[feature-asignacion-oc|feature note]] lista 7 endpoints (antes 5). Memoria local cross-sesión actualizada con schema de `stocks`/`FP_Almacen`/`albclit`/`clientes` (hay dos PKs: `ccodcli` vs `ID_CLIENTE` según tabla).

Archivos (cambios working-tree, aún sin commit):
- Backend: `Asignacion/AsignacionRepository.php`, `Asignacion/AsignacionService.php`, `Asignacion/AsignacionController.php`, `routes/api.php`
- Frontend: `Modal/AsignarOCModal.vue`, `plugins/api.js`
- Docs: `docs/asignacion-oc-pedclil.md`, `CLAUDE.md`

Branch en ambos repos: `feature/asignacion-oc-pedclil` (lista para nuevo PR).


## 2026-04-22

- feat: **[[feature-asignacion-oc|Asignación OC ↔ Venta]]** — nuevo feature end-to-end para registrar de qué OC sale cada línea de venta antes de la serialización
  - Nueva tabla `pedclil_oc_asignacion` (NewBytes_DBF), 3 índices, 2 vistas (`vw_saldo_oc`, `vw_pedclil_estado_asignacion`), 1 trigger (`tg_pedclit_cestado_asignacion`)
  - Backend: 5 endpoints HTTP (sugerencia FIFO, candidatas, estado por pedido, PUT/DELETE asignación), Service transaccional con UPDLOCK+HOLDLOCK por OC, Repository con bind params
  - Frontend: badge con 4 estados (COMPLETA/PARCIAL/DISPONIBLE/SIN_ASIGNAR), modal editable con FIFO precargado, integración en `Detail.vue` columna "OC"
  - Command CLI: `php artisan asignaciones:fifo [--branch --order --company --limit --dry-run]` — idempotente, transaccional
  - Trigger SQL maneja transición V↔C cuando `pedclit.cestado` cambia P↔S — **cero acoplamiento** con [[modulo-makesale|MakeSale]] / [[modulo-removesale|RemoveSale]]
  - Feature flag `ASSIGNMENT_FEATURE_ENABLED` + filtro `ASSIGNMENT_COMPANIES` (CSV companyCodes) + `ASSIGNMENT_ALLOW_PARTIAL`
  - Cambios mínimos colaterales: `OrderDetailDto.companyCode` y `OrderItemDto.pedclilId` agregados al getDetail
  - Documentación completa en `/docs/asignacion-oc-pedclil.md` del monorepo + `database/sql/README.md`
- docs: actualizado [[arquitectura]] con sección del feature; nuevo [[contexto|gotcha]] de driver dblib + índices filtrados
- branch: `feature/asignacion-oc-pedclil` en ambos repos (basadas en Development)

Registro de cambios del proyecto, agrupado por fecha.

## 2026-04-16

- feat: **[[modulo-dashboard-lo|Dashboard Libre Opción]]** — nueva sección completa de estadísticas exclusiva del marketplace LO
  - 6 endpoints backend: summary, funnel, byPaymentMethod, byShippingMethod, resellers, cube OLAP
  - 4 páginas frontend: métricas (KPIs + pies), embudo de conversión, ranking resellers, cubo multidimensional
  - Embudo de 5 etapas: Carritos → Pedido generado → Activos → Facturados → Entregados
  - Cubo OLAP con 7 dimensiones y 4 medidas
  - Visible solo para Administrador, Gerente General, Product Manager
- fix: **Entregados** usa `MS_VENTAS_REMITOS.ID_STATUS > 1` (no `pedclit.delivered`)
- fix: **Carritos vs cancelaciones** — los sin pedclit son carritos abandonados, no cancelaciones
- fix: **Total cancelados** = created - active (no suma de flags que se solapan)
- fix: **Motivos de cancelación** — si hay `motivoCancelacion`, se agrupa por eso sin mostrar payment; payment solo para los sin motivo
- feat: **Links clickeables** en motivos de cancelación navegan a `/orders` con filtros exactos
- feat: **Filtros OrderList** — agregados `loOnly`, `loCancelled`, `motivoCancelacion`, `mpPaymentStatus`, `mpPaymentStatusDetail`, `sinMotivo` (sin afectar existente)

Archivos backend: `Controllers/Statistics/Lo/` (6), `Services/Statistics/Lo/`, `Repositories/Statistics/Lo/`, `routes/api.php`, `OrderListRepository.php`, `OrderList.php`
Archivos frontend: `pages/libreOpcion/` (4), `store/libreOpcion.js`, `components/LibreOpcion/`, `components/Table/TabMenuLO.vue`, `components/Filters/LibreOpcion.vue`, `layouts/basic.vue`
Branch: `feature/dashboard-lo`

## 2026-04-06

- fix: **Retiro siempre visible en shippingMethods** — eliminado early return que impedía agregar "Retiro" (id 3999) cuando la query por `companyCode` no devolvía resultados de la DB
- docs: nuevas memorias de proyecto (syncUp auth, múltiples DBs, branching)

Archivos: `ShippingMethodService.php`
Branch: `hotfix/shipping-retiro-always`

## 2026-03-31

- feat: **Billing Kit Report** — nuevo reporte Excel de kits facturados (controller, service, repository, export)
- fix: nombre de cliente en reporte de kits
- feat: checks post-deploy en Gamma (GitHub Actions workflow)

Archivos: `BillingKitReportController.php`, `BillingKitReportService.php`, `BillingKitReportRepository.php`, `ExcelExportBillingKitReport.php`, `deploy-gamma.yml`

## 2026-03-25 — 2026-03-26

- fix: **ID_ARTICULO null en [[modulo-makesale|MakeSale]]/[[modulo-removesale|RemoveSale]]** — proteger queries con ISNULL para evitar SQL malformado cuando LEFT JOIN no matchea
- fix: usar `ID_Articulo` (de pedclil) en registerStock en vez de `ID_ARTICULO` (de stocks, puede ser null)
- fix: espacio en búsqueda (search)

Archivos: `MakeSaleService.php`, `RemoveSaleService.php`, `MakeSaleRepository.php`

## 2026-03-20

- feat: **Objetivos Gigabyte** — incentivo reutilizable para marca Gigabyte
- feat: objetivos de ventas (backend + frontend)
- fix: respuesta XLSX en reporte

Archivos: `incentivoGigabyte.vue`, `TabMenuDashboard.vue`

## 2026-03-18 — 2026-03-19

- feat: **Kit Report** — reporte de billing de kits
- fix: IVA en kits para sucursal 10
- fix: decompose bundle (descomposición de kits)
- fix: stock en [[modulo-removesale|RemoveSale]]
- fix: listado de productos

## 2026-03-17

- fix: **companyCode en login** — corregir query de auth con ISNULL para includeNull
- fix: **download order warehouse** — respetar `ID_ALMACEN` original del item al descargar pedido
- feat: validación básica post-deploy en Gamma
- refactor: filtro companyCode en ShippingMethods, PaymentMethods y Sellers
- feat: proforma en pedidos (PED-1325)

Archivos: `AuthRepository.php`, filtros de Sellers/Shipping/Payment en frontend

## 2026-03-16

- perf: **optimización de búsqueda de productos** — CONTAINS full-text en vez de LIKE
- perf: eliminar JOINs inutilizados en GetProducts/GetProductById
- perf: reemplazar subconsultas correlacionadas de stockInMyOrder por JOINs
- fix: restaurar LIKE en CDETALLE para substrings
- fix: urldecode en search para compatibilidad

## 2026-03-13

- hotfix: **MercadoLibre sync** — usar `unit_price` como fallback cuando `full_unit_price` no existe
- fix: restaurar JOINs de fotos y prefixar FOT.checksum

## 2026-03-12

- feat: eliminar impuesto interno al agregar a la orden
- fix: **moveItem con kits** — descomponer kits en componentes al mover, preservar precio del origen
- fix: eliminación del origen para items normales en moveItem

## 2026-05-12

- fix: **arreglo join albclitshipping** — corregido JOIN en `OrderListRepository.php` relacionado a la tabla de shipping por albarán de cliente.
- feat: **cupón Libre Opción** — lógica de aplicación de cupones en pedidos LO. Archivos: `OrderRepository.php`, `UnprocessedOrdersRepository.php`, `OrderService.php`.
- fix: **`salespersonId` ahora actualiza también `ccodage`** — al hacer PATCH `/v1/clients/{id}/params`, además de guardar en `ID_VENDEDOR`, se actualiza `ccodage = RIGHT('00'+ISNULL(valor,''),2)`. Regla de negocio: `ccodage` debe mantenerse sincronizado con `ID_VENDEDOR` en `NewBytes_DBF.dbo.clientes`. Archivo: `Services/Client/ClientParametersService.php`.
- fix: **removida restricción `ncosteprom > 0`** en `GetProducts` (`ProductRepository.php`) — artículos con costo promedio en 0 o NULL ahora aparecen en el listado. La restricción impedía buscar artículos recién cargados sin costo.

Archivos: `Services/Client/ClientParametersService.php`, `Repositories/Product/ProductRepository.php`, `Repositories/Order/OrderList/OrderListRepository.php`, `Repositories/Order/OrderRepository.php`

Rama: `hotfix-salesperson-and-ncostreprom-ccodage` (basada en `Development`, pusheada a origin)

## 2026-05-14

Sesión de **descubrimiento + scaffolding del [[feature-laset-import|Laset Import Framework]]** (companyCode=11). Branch `lasetImportFramework` creada en ambos repos basada en `Development`/`development` recién sincronizadas.

- discovery DB: identificadas las 11 empresas activas en `FP_Empresas` (no solo NB/NBElectric/LO como decía el `CLAUDE.md`). Laset = CODEMP 11, importadora uruguaya con `defaultIncoterms=14`.
- discovery ERP: mapeo canónico **compras = `pedprot` + `pedprol` + `pedproi`**, **ventas = `pedclit` + `pedclil`**, **stock = `stocks`** (filtrado por almacén — no tiene `companyCode`). `pedclil_oc_asignacion` linkea ambos. Estado actual companyCode=11: 386 compras + 363 ventas + 179 CFE Uy + 84 forwarders + 158 cargos extra ya migrados.
- gotcha confirmado: **`pedproi` no es solo impuestos** — guarda también cargos extra del pedido de compra (`cdescrip='camion'` $50/$200). Linkea a `pedprot.nNumPed`, NO a `pedclit`.
- gotcha confirmado: tabla `rebates` (12 rows) + `NewTable` (0 rows) son **huérfanas** — restos de intento abandonado del 2025-11-01. Sin `companyCode`. NO usar.
- discovery CFE Uruguay: las 4 tablas `FP_*_Uy` (Encabezado, Detalle, Documentos, Comprobantes) son **la mitad downstream de Laset ya implementada** — emiten CFE uruguayos con IVA 22% en DOL a clientes LATAM. 179 facturas + 1411 líneas con adendas que confirman beneficiario "Laset Sociedad Anonima".
- creadas tablas staging: **`laset_import_batches`** (cabecera por carga, 9 cols) + **`laset_import_staging`** (1 fila por fila de Excel, 67 cols crudas en NVARCHAR lossless + 8 cols de matching con CHECK enum). En `NewBytes_DBF.dbo`. 5 índices: batch, sku, customer_invoice, vendor_invoice, status.
- scripts DDL versionados: `2026_05_14_001_create_laset_import_staging.sql` + drop simétrico. Aplicados al SQL Server.
- regla cero del feature: **NUNCA modificar tablas ERP existentes** (`pedprot`/`pedprol`/`pedproi`/`pedclit`/`pedclil`/`stocks`/`FP_*`/`forwarders`). Solo lectura via JOIN; toda metadata de matching vive en `laset_import_staging.matched_*`.
- bug menor recuperado: `git branch -D development` en backend (case-insensitive macOS) borró también `Development`. Recuperado con `git reset --hard origin/Development`.
- documentación: `docs/laset-import-framework.md` (nuevo, 250+ líneas), sección "Laset Import Framework" agregada al `CLAUDE.md` del repo.

Archivos: `docs/laset-import-framework.md`, `api-rest-pedidos-laravel/app/database/sql/2026_05_14_001_{create,drop}_laset_import_staging.sql`, `api-rest-pedidos-laravel/app/database/sql/README.md` (entrada nueva), `CLAUDE.md`.

Branch: `lasetImportFramework` (ambos repos, basada en development/Development sincronizadas).

Próximo paso: cargador PHP que parsee `docs/laser.xlsx` y popule la staging, después reconciliación.

### 2026-05-14 — continuación (matching agregado + plan migración)

Después de cargar las 3007 filas a staging en la sesión previa, esta jornada se cerró con la reconciliación, el matching agregado y la decisión de migración.

- **Reconciliación implementada** (DB views, read-only sobre ERP):
  - `vw_laset_planilla_compras` / `vw_laset_planilla_ventas` — agregado staging por SKU.
  - `vw_laset_erp_compras` / `vw_laset_erp_ventas` / `vw_laset_erp_stock` — agregado ERP por id_articulo + comp=11 + almacenes Laset.
  - `vw_laset_sku_bridge` — UNION articulo + alias.
  - `vw_laset_reconciliation` — vista maestra con deltas y bridge_status.
- **Bridge SKU descubierto**: `articulo.ID_PRODUCTO` (varchar) = SKU del fabricante, `articulo.ID_ARTICULO` (int) = PK interna. Cobertura inicial 620/739 (84%) directa.
- **Tabla `laset_sku_alias`** creada (en `NewBytes_DBF.dbo`) para persistir normalizaciones automáticas + decisiones manuales. Bridge view refactorizado a UNION articulo + alias. Script `database/sql/2026_05_14_003_create_laset_sku_alias.sql`.
- **Normalizaciones fuzzy aplicadas** (sku planilla → ID_Articulo):
  - `auto:trim` (newlines/whitespace trailing — ej. `'MAG255FE20\n'`)
  - `auto:nospace`, `auto:nohyphen`, `auto:hyph2sp`, `auto:sp2hyph`, `auto:alnum` (paréntesis, mayúsculas)
  - `auto:split-slash` (ej. `'PBE120GS25SSDR / PE000775'` → matchea por la parte izquierda)
  - `auto:last-word` (ej. `'NC Apoyo precio 100-100000593WOF'` → matchea última palabra)
  - 14 SKUs huérfanos recuperados con normalizaciones.
- **5 services marcados** automáticamente con `source='service'` (`Fondos Laset`, `PRINTING FEE`, `Transporte aereo`, `Flete Carga Bonded Fastmark`, `RMA %`).
- **Aggregate matching aplicado** vía tabla tmp + UPDATE FROM JOIN (evitando dblib segfault con UPDATE loops). Categorías:
  - MATCHED (planilla=ERP exact) = 536 filas
  - PARTIAL (discrepancias) = 1860 filas
  - DELTA_ONLY (ERP vacío) = 65 filas
  - NO_BRIDGE = 147 filas
  - IGNORED (basura+services) = 399 filas
- **Decisión clave de negocio (usuario)**: **planilla = fuente de verdad** para comp=11. El ERP comp=11 actual es ex-carga-fallida (146 SKUs con `ERP > Planilla` por duplicación de ~10× en casos como `Ajuste precio A520MAPRO` plC=280 / erpC=2260, 214 con `Planilla > ERP` por undercount).
- **PARTIAL promovido a MATCHED** (score=90) + DELTA_ONLY promovido a MATCHED (score=80). **Total importable: 2461 filas** (82%).
- **Plan de migración 3 fases acordado**:
  - **A**: alta de los 100 SKUs huérfanos en `articulo` por equipo catálogo (CSV en `docs/laset_orphan_skus.csv` + `.md`).
  - **B**: DELETE de filas ERP comp=11 sin contraparte en planilla. REGLA CRÍTICA: `WHERE companyCode = 11` SIEMPRE. Otras companies intocables.
  - **C**: INSERT de las 2461 MATCHED a pedprot/pedprol/pedproi/pedclit/pedclil + pedclil_oc_asignacion.
- **Gotchas técnicos catalogados** (ver [[memoria]] y [[feature-laset-import#10. Gotchas]]):
  - PhpSpreadsheet inviable >15 min → preprocesar con Python+openpyxl en host
  - dblib segfault con UPDATE loops → tabla tmp + UPDATE FROM JOIN
  - dblib no auto-castea DECIMAL → INT en tmp para scores
  - SQL Server 2012 — sin `CREATE OR ALTER VIEW`, sin `DROP VIEW IF EXISTS`
  - `pedprot.sitio=0` vs `pedprol.sitio=NULL` → joinear solo por `nNumPed`
  - macOS case-insensitive: `git branch -D development` puede romper `Development`
- **Scripts SQL versionados (database/sql/)**:
  - `2026_05_14_001_create_laset_import_staging.sql` (+drop) — tablas staging
  - `2026_05_14_002_create_laset_reconciliation_views.sql` (+drop) — vistas
  - `2026_05_14_003_create_laset_sku_alias.sql` (+drop) — alias + refactor bridge
- **Backend**: `LasetImportStagingCommand`, `scripts/laset_xlsx_to_json.py`.
- **Docs**: `docs/laset-import-framework.md` actualizado a v2 (sección 7 decisiones, 8 plan migración, gotchas técnicos), `docs/laset_orphan_skus.{csv,md}` generados.

Próximo: fase A (equipo catálogo), portar aggregate-match a artisan command, diseñar fase B+C.

### 2026-05-14 (PM) — Laset Fase B ejecutada + discovery Fase C

**Fase B aplicada**: DELETE total ERP companyCode=11 — 7822 filas borradas.

| Tabla | Filas borradas |
|---|---:|
| `pedprot` | 386 |
| `pedprol` | 1349 |
| `pedproi` | 31 |
| `pedclit` | 363 |
| `pedclil` | 1847 |
| `albprot` | 526 |
| `albprol` | 1205 |
| `albclit` | 331 |
| `albclil` | 1746 |
| `pedclil_oc_asignacion` | 38 |

- **Decisión**: `DELETE total + re-INSERT` en lugar de row-level matching, porque el matching staging↔ERP es agregado por SKU (no fila-a-fila).
- **Backups in-DB** en `NewBytes_DBF.dbo.laset_phase_b_backup_*` (10 tablas) — mantener hasta validar Fase C. Permiten rollback con INSERT FROM SELECT.
- **Aislamiento verificado**: snapshot pre/post por company. Otras companies (4/9/etc) intactas.
- **Script**: `database/sql/2026_05_14_004_phase_b_delete_comp11.sql` con backups + JOINs compuestos `(cnumped, cnumsuc)` + pre-check assertions con `THROW`.

**Bug crítico atrapado en revisión SQL pre-ejecución**: el script inicial usaba `WHERE cnumped IN (SELECT cnumped FROM pedclit WHERE companyCode=11)` que habría borrado 5 ventas legítimas de NB (cnumped 10338002, 10338022, 10338027 colisivos entre comp=11 y comp=4). PK efectiva de pedclit es `(cnumped, cnumsuc)` — uq_pedclit. Refactorizado a `DELETE x FROM x JOIN pedclit t ON t.cnumped=x.cnumped AND t.cnumsuc=x.cnumsuc WHERE t.companyCode=11`. Misma corrección aplicada a pedclil/albclit/albclil. `pedprot.nNumPed` y `albprot.nnumalb` sí son únicos globalmente, esos OK.

**Otro bug detectado**: conteo inicial `albprot=370` era falso (subselect cruzado mal armado `nnumalb IN nNumPed`). Conteo real `WHERE companyCode=11`: **526 filas** (rango 2026-03-02 → 2026-05-12). De los 526, 369 con pedprot padre + 157 "remitos huérfanos" (compras directas sin OC).

**Pre-check assertions**: pedido explícito del usuario — antes de cada DELETE, batch separado con `DECLARE @bad INT; SELECT @bad = COUNT(*) ... WHERE …; IF @bad > 0 THROW 50001, [ABORT], 1; GO`. El loader PHP propaga la excepción y aborta antes de tocar nada. Defense in depth.

**Discovery Fase C** (no implementada todavía):
- Schema mapeado de las 6 tablas a poblar: pedprot 34 cols (`id_pedprod` IDENTITY, `nNumPed` manual desde MAX+1=13219), pedclit 78 cols (`id` IDENTITY, `cnumped` manual desde MAX+1=10459501, `ccodcli` NOT NULL), pedprol 25, pedclil 42, pedproi 16 (`lcalcuauto` NOT NULL), pedclil_oc_asignacion 19.
- Agrupación: 2461 filas MATCHED → 417 pedprot únicas (por proveedor+vendor_pi+vendor_invoice) + 396 pedclit únicas (por razon_social+customer_pi+customer_invoice). Total ≈ 4078 INSERTs.
- **Bloqueante de mapping resuelto**: tabla maestra moderna es **`FP_Proveedores`** (no `proveedo`, que tiene `cnompro` vacío para Laset). Match staging.proveedor → FP_Proveedores comp=11 estricto: **25/28 OK**, 3 a auto-crear.
- Match clientes: 50/56 OK con `clientes WHERE companyCode=11`, 6 a auto-crear.
- Match SKUs: 806/820 OK vía `articulo.ID_PRODUCTO`, 14 bloqueados (Fase A pendiente).
- **Regla confirmada por usuario**: proveedores y clientes **NUNCA se comparten entre companies**. Si pedprot/pedclit comp=11 referencia un ccodpro/ccodcli de otra company, es data sucia de la ex-carga-fallida (varios ejemplos detectados: ccodpro 002300/000847/001130 = NB comp=4; ccodcli 096117 MASTER COMPUTERS = comp=4).

**Decisiones tomadas con usuario para implementación Fase C**:
- Forma: artisan command PHP `laset:import-fase-c` con `--dry-run / --limit / --chunk`.
- FKs faltantes: auto-crear `FP_Proveedores`/`clientes` mínimos con `companyCode=11`.
- Idempotencia: `WHERE match_status=MATCHED AND matched_pedprot_nnumped IS NULL`. Filas IMPORTED se skipean.

**Pendiente** (próxima sesión): implementar el comando, dry-run, ejecución real.

**Memoria nueva** (local + bóveda):
- [[feedback_pedclit_pk_compuesta]] — PK efectiva `(cnumped, cnumsuc)`, no usar IN sobre cnumped.
- [[feedback_pre_check_assertions_destructivos]] — Patrón THROW antes de DELETE destructivos.
- [[project_erp_master_tables_fp]] — FP_Proveedores moderna vs proveedo legacy + regla nunca-compartido.

**Scripts SQL**:
- `database/sql/2026_05_14_004_phase_b_delete_comp11.sql` (+ esqueleto rollback simétrico).

### 2026-05-14 (noche) — Laset Fase C ejecutada + fix almacenes + reset stocks

**Fase C ejecutada completa**: 2439 filas staging IMPORTED → ERP comp=11.

| Tabla | Insertadas |
|---|---:|
| FP_Proveedores | +3 (auto-create) |
| clientes | +6 (auto-create) |
| pedprot | 506 |
| pedclit | 392 |
| pedprol | 2439 |
| pedclil | 2439 |
| pedclil_oc_asignacion | 2439 |
| **TOTAL INSERTs** | **8224** |

- Comando: `php artisan laset:import-fase-c [--dry-run] [--limit=N] [--chunk=50]`. Idempotencia via `WHERE match_status='MATCHED' AND matched_pedprot_nnumped IS NULL`.
- Ejecución gradual: --limit=10 (validación), --limit=100, --limit=500, sin limit. dblib aguantó las transacciones grandes sin segfault.
- IDs generados: nNumPed 13219→13632, cnumped 10459501→10459887.

**Bug almacenes Laset detectado y arreglado** (corregido por usuario: *"los de laset no pueden estar nunca en SAF"*):
- Mapping inicial mappeaba BONDED-FASTMARK→SAF (almacén de NB comp=4). 3 pedprot mal asignados.
- Mapping intermedio "fix" creó otro bug peor: asumió URU/ASI no existían y los puso en IDs 17/18, pero ya existían como ID 14/15 → 110+53 pedclil con ID_ALMACEN huérfano.
- Mapping final correcto: DOM=9, BON=11 (consolida BONDED-*), GRI=10, URU=14, ASI=15. Todos verificados en `FP_Almacen WHERE companyCode=11`.
- Las 3 columnas relacionadas deben coordinarse SIEMPRE: `pedprot.cCodAlm`+`warehousesId`, `pedclit.ccodalm`+`ID_ALMACEN`, `pedclil.ID_ALMACEN`.

**Reset stocks comp=11** (corregido por usuario: *"lo anterior debías sacarlo, si al pisarlo con lo de la planilla ya te ds el stock"*):
- 286 filas reseteadas a 0 con DOBLE FILTRO: `articulo.companyCode=11 AND stocks.cCodAlm IN (almacenes Laset)`.
- 302 filas con articulo.companyCode=4 (NB) en almacenes Laset PRESERVADAS (17 unidades, items compartidos físicamente).
- Backup en `laset_phase_b_backup_stocks` (incluye snapshot de articulo_companyCode).

**Identidad contable post-reset**:
- Saldo neto agregado comp=11: compras=101517, ventas=101517, **saldo=0** ✓
- Por SKU global: **657/657 cuadran (100%)** ✓
- Por (SKU, almacén): **1059/1090 cuadran (97%)**. Las 31 discrepancias restantes son **cross-warehouse normal** del ERP (compra en X, venta desde Y, neto SKU=0).

**Memorias nuevas** (local + bóveda):
- [[memoria#Doble filtro company del item + del almacén]] — para `stocks` y otras tablas sin companyCode propio.
- [[memoria#Almacenes Laset reales]] — DOM/BON/GRI/URU/ASI; SAF NO es de Laset.

**Backups in-DB activos** (mantener hasta validar B+C en producción):
- `laset_phase_b_backup_*` (10 tablas, Fase B)
- `laset_phase_b_backup_stocks` (Fase reset stocks)

### 2026-05-15 — Replicación a producción: runbook + scripts + comandos versionados

**Objetivo**: dejar todo listo para replicar Fase B+C en producción de manera segura y documentada.

**Generados**:

| Archivo | Tipo | Qué hace |
|---|---|---|
| `app/Console/Commands/LasetAggregateMatchCommand.php` | Artisan | `php artisan laset:aggregate-match [--dry-run]`. Porta el script ad-hoc `/tmp/aggregate_match2.php` con regla planilla=verdad. Tabla tmp + UPDATE FROM JOIN single-statement (evita dblib segfault). |
| `app/scripts/laset_reset_stocks.php` | Script PHP | Reset stocks comp=11 con doble filtro (item+almacén). Backup automático en `laset_phase_b_backup_stocks`. Pre-checks con THROW. Soporta `--dry-run`. |
| `app/scripts/laset_pre_flight_prod.php` | Script PHP | Read-only. 9 secciones: objetos del feature, conteos comp=11 vs baseline dev, actividad reciente, FP_Almacen IDs, snapshot otras companies, MAX(IDs), staging actual, stocks doble filtro, checklist GO/NO-GO. |
| `app/scripts/laset_post_flight_validation.php` | Script PHP | Read-only. Verifica backups in-DB, conteos esperados, identidad SKU global ≥99%, almacenes válidos, doble filtro stocks. Exit code 0/1 para CI. |
| `docs/laset-import-runbook-prod.md` | Doc | Runbook 11 pasos: pre-requisitos, backup DBA, ventana, DDL, carga planilla, aggregate match, Fase B+C, reset stocks, validación, rollback parcial/full, limpieza final. |

**Validación dry-run de los nuevos comandos en dev**:

```
laset:aggregate-match --dry-run
  925 combinaciones SKU → MATCHED 820 / UNMATCHED 100 / IGNORED 5
  MATCHED/100=614, /90=10, /80=10

laset_reset_stocks.php --dry-run
  Filas con doble filtro (item comp=11 + almacén Laset): 286
  Filas a PRESERVAR (item NO comp=11 en almacén Laset): 302 (17 unidades)
```

Coincide con lo aplicado manualmente en la sesión 2026-05-14.

**Actualizado**:
- `CLAUDE.md` (raíz proyecto): sección "Artisan Commands" con los 3 comandos Laset.
- Runbook: referencias a los nuevos artisan commands en lugar de scripts ad-hoc.

**Para correr en producción** (resumen):
1. Pre-flight (read-only) → coordinar surprises
2. Backup full DBA + ventana de mantenimiento
3. DDL 001/002/003 (si falta)
4. `php artisan laset:import-staging` (carga planilla)
5. `php artisan laset:aggregate-match` (NUEVO)
6. Service aliases manuales (si pre-flight detectó)
7. DDL 004 Fase B (con pre-checks THROW)
8. `php artisan laset:import-fase-c` (gradual: --limit=10/100/500/sin limit)
9. `laset_reset_stocks.php` (NUEVO)
10. Post-flight validation
11. Cierre + monitoreo 7-14 días + dropear backups in-DB

Doc canónico: [`docs/laset-import-runbook-prod.md`](repo)

---

### 2026-05-15 (cont.) — Laset Fase D (remitos + pedproi + stock) + fix defecto Fase C

**Hallazgo**: Fase C había creado solo las órdenes comp=11 (pedprot/pedprol +
pedclit/pedclil), sin remitos ni pedproi ni stock. Se implementó **Fase D**.

**Generado**:

| Archivo | Tipo | Qué hace |
|---|---|---|
| `app/Console/Commands/LasetImportFaseDCommand.php` | Artisan | `laset:import-fase-d [--dry-run --limit --chunk]`. Crea albprot/albprol/albclit/albclil + pedproi camion + stock compra(+)/venta(−) sobre órdenes comp=11 existentes. Fechas de documento respetadas. Idempotente. Pre-check de aislamiento (THROW si ID_Articulo del delta no es comp=11). |
| `database/sql/2026_05_15_001_reset_stock_comp11.sql` (+drop) | SQL | Paso 0 Fase D: reset stock comp=11 en almacén Laset, doble filtro articulo.companyCode=11, backup `laset_phase_b_backup_stocks`. |
| `database/sql/2026_05_15_002_fix_fasec_articulo_comp11.sql` (+drop) | SQL | Fix defecto Fase C: remap 5 SKUs con gemelo comp=11, backup + pre-check THROW. |
| `docs/laset_fasec_skus_sin_comp11.csv` | CSV | 39 SKUs sin artículo comp=11 para Fase A (catálogo), con impacto por SKU. |

**Defecto de Fase C detectado por el pre-check de Fase D**: `resolveMasters`
resolvía SKU→ID_ARTICULO sin filtrar companyCode → 56 pedprol + 56 pedclil de
órdenes comp=11 apuntaban a 44 artículos NB (comp=4).

**Fix**: (1) `resolveMasters` ahora filtra `articulo.companyCode=11`;
(2) SQL `2026_05_15_002` **aplicado en dev** — 8 pedprol + 8 pedclil remapeadas
a los gemelos comp=11, backups 56+56, articulo y otras companies intactas;
(3) 39 SKUs restantes → Fase A catálogo.

**Dry-run Fase D**: albprot=506, albprol=2439, albclit=392, albclil=2439,
pedproi=111, registro_stock=2439, stock neto=0.

**Estado**: Fase D BLOQUEADA hasta Fase A (39 SKUs) + re-bind Fase C. Ver
[[feature-laset-import#12. Sesión 2026-05-15 (cont.) — Fase D + fix defecto Fase C]].

---

### 2026-05-15 (cont. 2) — Laset Fase D pasada 1 ejecutada + snapshot/restore

**Fix Fase C aplicado**: SQL `2026_05_15_002` remapeó 8 pedprol + 8 pedclil
(5 SKUs con gemelo comp=11) a sus artículos comp=11. Backups 56+56.

**Fase D pasada 1 ejecutada en dev** (`laset:import-fase-d --skip-bloqueadas`):
493 albprot + 1454 albprol + 111 pedproi + 379 albclit + 2155 albclil + 2155
registro_stock. Stock 672/672 = delta. Difirió 15+15 órdenes (39 SKUs → Fase A).

Tres fixes en el camino (todos atajados por guards, sin data corrupta):
- Consolidación de líneas de remito por artículo (PK albclil = (ID_Articulo,
  ID_NROREMCLI_ENC); norma ERP confirmada en backups).
- UPSERT de stock (INSERT fila mínima si el combo no existía; ~64% faltaban).
- Set de almacenes Laset desde `FP_Almacen WHERE companyCode=11` (no
  hardcodear; URU/ASI reales = 14/15, no 17/18). Corrige reset SQL + comando.

Guards nuevos: ASSERT rollback si queda stock sin aplicar; auto-auditoría
remitos reales vs plan.

Identidad `compras − ventas − stock = 0` verificada: 684/721 = 0, los 37 ≠ 0
100% explicados por órdenes diferidas (cierran en pasada 2).

**Snapshot/Restore unificado** (reversibilidad total del proceso):
| Archivo | Qué |
|---|---|
| `app/Support/LasetSnapshotRegistry.php` | Registro único del alcance comp=11 (14 tablas, incl. cross-DB NB_WEB.registro_stock) |
| `app/Console/Commands/LasetSnapshotCommand.php` | `laset:snapshot {tag}` (--dry-run/--drop) |
| `app/Console/Commands/LasetRestoreCommand.php` | `laset:restore {tag}` (--dry-run/--force), IDENTITY_INSERT + trigger off/on, pre-check vs manifiesto |
| `database/sql/2026_05_15_003_create_laset_snapshot_manifest.sql` (+drop) | Tabla manifiesto |

Probado end-to-end: daño simulado (borrar albclil/pedproi, stocks=99999,
registro_stock) → `laset:restore` → estado bit-idéntico, identidad igual,
trigger rehabilitado. Punto `postPasada1` creado (15949 filas, 14 tablas).
Gotcha: `DISABLE/ENABLE TRIGGER` no admite prefijo de DB → `sp_executesql`
en contexto NewBytes_DBF.

**Workflow**: `laset:snapshot <tag>` ANTES de cada proceso/sesión →
si algo sale mal `laset:restore <tag> --force`. Ver
[[feature-laset-snapshot-restore]].

---

## 2026-05-29 — Bugs Fase C: pedprot/pedprol duplicados (fix-pedprot-dup)

Sesión disparada por la usuaria al reportar que la "compra" 13669 + 13916 (mismo proveedor MSI, mismo PI 11179042, mismo invoice 22028796) deberían ser **una sola OC** + la 13669 tenía 2 líneas del mismo art 122169 (qty 50 + 10) que deberían consolidarse. Investigación reveló 2 bugs en `LasetImportFaseCCommand`:

- **Bug A (intra-pedprot)**: cada staging row generaba 1 pedprol independiente; el espejo `buildPedclilGroups` existía para ventas pero faltaba `buildPedprolGroups` para compras. Resultado en dev: 456 casos de `(nNumPed, ID_Articulo)` con N>1 pedprol.
- **Bug B (inter-pedprot, cross-batch)**: `$pedprotByKey` se armaba solo desde rows del run actual; nunca consultaba ERP. Resultado en dev: 234 grupos pedprot duplicados / 369 sobrantes (~44% del total de 847 pedprot comp=11).

**Patches preventivos** (commit `e251a8bd`):
- Nuevo `buildPedprolGroups()` en `LasetImportFaseCCommand` agrupa por `(pedprot_key, ID_Articulo)` con FOB ponderado.
- Nuevo `mergeExistingPedprot()` pre-carga pedprot existentes en ERP comp=11 por `(cExped, CSUFAC_TEMP)` y reusa `nNumPed`; `executePlan` skipea pedprot reusados; pedprol insertadas/updateadas según si ya existía la línea.

**Comando retroactivo `laset:fix-pedprot-dup`** (`LasetFixPedprotDupCommand.php`) en 2 fases + compactación:
- Fase 1 (inter): tabla tmp única `#pedprol_inter_map` con `ROW_NUMBER` para asignar nLinea contiguo por ganador. **UPDATE pedprol en 2 pasos** con `nLinea = -(new+1_000_000)` como buffer negativo — evita colisión transitoria de PK cuando winner y loser comparten nLineas. Re-apunta `pedclil_oc_asignacion.(n_num_ped_oc, n_linea_oc)`, `pedproi.nnumped`, `albprot.nnumped` (filtro `companyCode=11 OR NULL`), `laset_import_staging.(matched_pedprot_nnumped, matched_pedprol_nlinea)`.
- Fase 2 (intra): consolida `(nNumPed, ID_Articulo)` con qty sumada + nPreDiv ponderado. DELETE losers.
- Compactación: re-numera nLinea contiguo 1..N por pedprot tras gaps de DELETE.
- Verify: doble invariante `total_qty` + `hash(SUM(art*qty))` debe preservarse → THROW + rollback si difiere. Atrapa bugs sutiles donde una qty se compensa con otra (caso real: primer intento del comando perdió 48.427 unidades por colisión de nLinea — restore inmediato del snapshot).

**Resultados dev** (snapshot pre `pedprot_dedup_20260529`):
- pedprot 847 → 478 (-369 losers consolidados).
- pedprol 3166 → 1366 (-1800 consolidaciones de líneas dup).
- `total_qty=139240` preservada exacta.
- Caso reportado 13669/art 122169: 1 sola pedprot 13669 lin=1 qty=260 fob=70. ✓

Snapshot, dry-run, real, idempotencia (re-run = 0 cambios). Commit + push. Doc en [[feature-laset-fix-pedprot-stockonly]].

---

## 2026-05-30 — Bug Fase C: stock-only descartado (fix-stock-only-pedprol)

Continuación del análisis del 13669 — la usuaria notó que la compra real debía ser **300 unidades** (no 260) porque había 40 unid de stock no vendido. Investigación en staging:

```
vendor_pi=11179042 + vendor_invoice=22028796 + sku=PROB760PD4:
- id=2258  batch=1 IMPORTED qty=50  customer_invoice=A-3656
- id=2913  batch=1 IMPORTED qty=10  customer_invoice=A-3732
- id=2914  batch=1 IGNORED  qty=240 customer_invoice=∅ (year=1900)
- id=3702  batch=6 IMPORTED qty=200 customer_invoice=A-3767
- id=3703  batch=6 IGNORED  qty=40  customer_invoice=∅ (year=1900)
```

Las dos filas IGNORED no son basura — son **snapshots del stock disponible** al final de cada batch. La fila del batch más alto (id=3703 qty=40) es el stock real al cierre del período. La 2914 (qty=240) es un snapshot anterior (después de vender 60 de las 300, quedaban 240).

**Alcance del bug** en dev:
- 491 filas IGNORED candidatas / 361 grupos únicos (vpi, vinv, sku).
- Categorías post-categorización:
  - F (pedprol existe, le falta qty): 198 grupos / 13.698 unid.
  - B (pedprot existe pero no pedprol del art): 107 grupos / 10.797 unid.
  - D (pedprot no existe — compra 100% stock): 49 grupos / 9.919 unid.
  - C (sin SKU/proveedor en comp=11): 7 grupos.
  - A (redundante) y E (qty=0): **0** ← regla robusta.
- **Total: 34.414 unidades perdidas** (33.058 procesables, 1.356 cat C bloqueadas por Fase A catálogo).

**Patches preventivos**:
- `LasetAggregateMatchCommand` paso `4a-pre` (commit `1fb94e42`) reclasifica como nuevo status `STOCK_ONLY` filas con `year != 2025/2026 + vpi/vinv/sku no vacíos + qty>0 + customer_invoice vacío + (no SELECTOR, no service-like)`.
- DDL `2026_05_30_001_add_stock_only_match_status.sql`: amplía `match_status` `NVARCHAR(20) → NVARCHAR(30)` (`STOCK_ONLY_SUPERSEDED` tiene 21 chars y no entraba — caso real, primer intento falló por truncate post-CHECK) + extiende `CK_laset_staging_match_status`.
- `LasetImportFaseCCommand::handle` (commit `422a3c86`) delega tras MATCHED: `Artisan::call('laset:fix-stock-only-pedprol', [], $this->getOutput())` si hay STOCK_ONLY pendientes. Futuros imports manejan stock-only automáticamente en una sola corrida.

**Comando retroactivo `laset:fix-stock-only-pedprol`** (`LasetFixStockOnlyPedprolCommand.php`):
- Step 0: reclasifica IGNORED legacy → STOCK_ONLY con el mismo predicado del patch (paridad dev↔prod).
- Step 1: por `(vpi, vinv, sku)`, fila del **batch más alto** gana; las anteriores → `STOCK_ONLY_SUPERSEDED`.
- Step 2: aplica por categoría F/B/D + skip C.
- Step 3: suma stock a `stocks` con tabla tmp `laset_stockonly_delta` + doble filtro (`articulo.companyCode=11 + FP_Almacen.companyCode=11`), excluye `INTERNAL_NO_STOCK_ARTICULOS` (FLETE 121944).
- Step 4: marca staging ganadoras → IMPORTED con `matched_pedprot_nnumped + matched_pedprol_nlinea`.
- Verify: STOCK_ONLY pendientes == cat C skipped + 0 huérfanas.

**Resultados dev** (snapshot pre `stockonly_20260530`):
- 490 IGNORED reclasificadas → STOCK_ONLY (360 ganadoras + 130 SUPERSEDED).
- F=198 (+13.698 unid), B=113 (+12.127 unid), D=42 (+7.233 unid), C=7 skip.
- pedprol comp=11 total_qty: 139.240 → **172.298** (+33.058).
- arts distintos: 731 → 764 (+33 SKUs nuevos visibles en stock).
- Caso reportado 13669/art 122169: qty 260 → **300** ✓.
- Idempotente, dblib-safe, transacción global con rollback en error.

Commit + push. Doc en [[feature-laset-fix-pedprot-stockonly]].

## 2026-05-30 — Análisis de esquema ERP y companyCode en albclit

### Análisis de relaciones entre tablas ERP

Sesión de documentación y análisis del esquema ERP. Se relevaron y documentaron las relaciones entre todas las tablas de pedidos, remitos, artículos, stock y depósitos.

Notas creadas en la bóveda:
- [[relacion-tablas-ped-alb]] — pedclit/pedclil/albclit/albclil (ventas)
- [[relacion-tablas-pedprot-pedprol-pedproi]] — pedprot/pedprol/pedproi (compras)
- [[relacion-tablas-albprot-albprol]] — albprot/albprol y su relación con pedprot
- [[relacion-tablas-articulo-stocks]] — articulo y stocks con todas las tablas de líneas
- [[relacion-companycode]] — mapa completo de qué tablas tienen companyCode propio
- [[relacion-tablas-stocks-almacen]] — FP_Almacen, stocks, columnas de depósito en líneas

Hallazgos clave:
- Solo las cabeceras (pedprot, pedclit, albprot, albclit) y articulo tienen companyCode propio. Las líneas lo heredan del padre.
- La columna de depósito en líneas de ventas se llama `ID_ALMACEN`; en líneas de compras se llama `stockWarehouseId`. Ambas son FK a `FP_Almacen.ID_ALMACEN`.
- **NBE** es un depósito compartido entre cc=4 (NB) y cc=9 — no es error que líneas de pedidos cc=4 apunten a NBE.

### Fix: companyCode en albclit

`albclit` no tenía columna `companyCode`, lo que obligaba a hacer JOIN con `pedclit` para filtrar por empresa.

**Cambios aplicados:**
1. `ALTER TABLE [NewBytes_DBF].[dbo].[albclit] ADD companyCode INT NULL` — columna nueva
2. `UPDATE` masivo: 231,454 registros poblados desde `pedclit` vía `(cnumped, cnumsuc)`
3. 164,506 registros históricos (legacy ERP sin pedclit padre, 2010–2025) asignados a `companyCode=4` (NB) — todos los registros legacy pertenecían a NB
4. `MakeSaleRepository::createHeader()` modificado para escribir `companyCode` en cada nuevo remito, heredándolo del `$order` (que viene de `pedclit`)

Archivos modificados: `api-rest-pedidos-laravel/app/app/Repositories/MakeSale/MakeSaleRepository.php`

## 2026-05-30 (cont.) — Análisis profundo articulo/stocks/depósitos y correcciones de documentación

### Correcciones a la documentación

- **SAF y NBE** son los únicos depósitos compartidos — exclusivamente entre NB (cc=4) y NBElectric (cc=9). Cualquier otro cruce de companyCode en almacén es error de datos.
- **`ID_Articulo` y `cref`** son ambos obligatorios y únicos en las tablas de líneas. `ID_Articulo` es la FK canónica. La discrepancia de 13.462 filas en pedclil es un caso puntual de Laset (cref conserva el código NB cc=4, ID_Articulo apunta al clon cc=11).
- **`pedprol.stockWarehouseId` NULL en 99.5%** es esperado: son OCs legacy de NB que en la práctica pertenecen todas a SAF (ID_ALMACEN=2). No es error, es dato histórico.
- **Regla de integridad stocks**: no deben existir filas en stocks donde el companyCode del artículo difiera del companyCode del almacén, salvo SAF/NBE.

### Errores de datos documentados (no corregidos)

- 10 pedidos DIGITO BINARIO (cc=5) con líneas en SAF (cc=4) — 2025
- 1 pedido cc=1 con líneas en SAF — 2026-05-26
- 6 pedprot NB (cc=4) con líneas en almacenes Laset (DOM/GRI/ASI) — mayo 2026, residuo migración

Notas actualizadas: [[relacion-tablas-articulo-stocks]], [[relacion-tablas-stocks-almacen]]


## 2026-05-30 — Fix retroactivo articulo.Id_Marca comp=11 + refactor Fase C marcas

Bug histórico descubierto: `LasetImportFaseC` escribía marcas en `NewBytes_DBF.dbo.FP_Marcas` (legacy, sin PK ni companyCode) en vez de `NB_WEB.dbo.marcas` (que es la FK efectiva de `articulo.Id_Marca` en todo el codebase). Resultado: 151 artículos Laset con `Id_Marca` apuntando a marcas equivocadas (e.g. ASUS aparecía como ROCCAT comp=4 en TotalSales, Statistics, Marketing, Product, etc.) y 204 filas basura en FP_Marcas (199 en ID=80 + 5 en ID=81).

**Refactor Fase C**:
- Cambia INSERT/lookup de marcas a `NB_WEB.dbo.marcas` filtrado por `companyCode=11`.
- `marcas.id` es IDENTITY → INSERT row-by-row + `SELECT CAST(SCOPE_IDENTITY() AS INT)` para capturar id real.
- `articulosAutoCreate[].marca_id` se resuelve post-INSERT de marcas (no se pre-reserva). Pre-reservar IDs sobre IDENTITY falla con `Cannot insert explicit value for identity column when IDENTITY_INSERT is set to OFF`.
- Aislamiento estricto: una marca de comp=4 no sirve para comp=11; si "ASUS" existe en comp=4 pero no en comp=11, crea otra entrada con `companyCode=11`.

**Backfill ejecutado en dev (idempotente vía service)**:
- 151 articulos comp=11 remapeados a su `Id_Marca` correcto en NB_WEB.marcas.
- 5 marcas creadas en NB_WEB.marcas comp=11: ACER (1320), HP (1321), LENOVO (1322), MICROVIP (1323), WD (1324).
- 204 filas basura eliminadas de FP_Marcas (ID_Marca IN 80, 81).
- Backups: `NewBytes_DBF.dbo.laset_fix_marcas_backup_articulo` + `laset_fix_marcas_backup_fp` (mantener hasta validar prod).

**Botón en UI**: "Fix marcas comp=11" en `/syncLaset` (junto a "Re-vincular facturas") con modal preview→confirmar. Dispara `POST /v1/laset/fix-marcas-comp11`. Mismo flujo desde CLI: `php artisan laset:fix-marcas-comp11 [--dry-run]`.

**Archivos**: `app/Services/Laset/FixMarcasComp11Service.php`, `app/Console/Commands/LasetFixMarcasComp11Command.php`, `app/Http/Controllers/Laset/LasetFixMarcasComp11Run.php`, `app/Console/Commands/LasetImportFaseCCommand.php` (refactor), `routes/api.php`, `database/sql/2026_05_30_002_fix_articulo_id_marca_comp11.sql` (+ drop), frontend `pages/syncLaset.vue` + `plugins/api.js`.

Doc: [[feature-laset-fix-marcas-comp11]], [[feature-sync-laset-botones]].

## 2026-05-31 — Portado relink-facturas a botón UI + STOCK_ONLY_SUPERSEDED como status terminal

**Re-vincular facturas — patrón service**: el comando CLI `laset:relink-facturas` ya existía; lo extraje a `app/Services/Laset/RelinkFacturasService.php` (preview/execute), agregué controller invokable `LasetRelinkFacturasRun.php` y ruta `POST /v1/laset/relink-facturas`. Botón "Re-vincular facturas" en `/syncLaset` con modal preview→confirmar. Stats: facturas a re-vincular / multi-pedido / sin match. El command CLI ahora es wrapper delgado del service.

**Status terminal `STOCK_ONLY_SUPERSEDED` (fix)**: el usuario reportó 2 filas del batch 6 que aparecían eternamente en "Falta sincronizar". Eran `STOCK_ONLY_SUPERSEDED` (perdedoras del grupo stock-only — la ganadora ya está `IMPORTED`). El status es terminal pero NO synced (como `IGNORED`), pero el filtro `view=pending` solo conocía `IMPORTED` e `IGNORED`. Fix en **4 capas**:
- `SyncLasetList.php`: `match_status NOT IN ('IMPORTED','IGNORED','STOCK_ONLY_SUPERSEDED')`.
- `SyncLasetSummary.php`: `!in_array($status, ['IGNORED','STOCK_ONLY_SUPERSEDED'])` para incrementar `pending`.
- `syncLaset.vue`: `TERMINAL = ['IMPORTED','IGNORED','STOCK_ONLY_SUPERSEDED']` en `getCheckboxProps.disabled` y `selectableIds`.
- `syncLaset.vue` (map de colores): `STOCK_ONLY` cyan, `STOCK_ONLY_SUPERSEDED` default.

Verificado vía curl batch 6: `view=pending` ahora 0 filas (antes 2). Summary pending=0, synced=380, total=400 (380 IMPORTED + 18 IGNORED + 2 STOCK_ONLY_SUPERSEDED).

**Lección**: al introducir un status terminal nuevo al staging, tocar siempre las 4 capas (list filter + summary counter + frontend checkbox + color map). Grep `IMPORTED.*IGNORED` para encontrar los puntos exactos.

Doc: [[feature-sync-laset-botones]], [[memoria#NVARCHAR length cap en columnas enum/status]].

## 2026-05-31 (cont.) — Borrado transaccional comp=11 + barrido de huérfanos + reimport limpio

Feature nuevo [[feature-laset-wipe-reimport|Borrar todo comp=11 + reimport limpio]] y resolución de un bug de fondo que corrompía cada ciclo de reimport. Commits: back `434beff8`, front `15ae1f4` (rama `lasetImportFramework`).

- **Botón "Borrar todo comp=11"** (`WipeTransactionalService` + `laset:wipe-transactional` + `POST /v1/laset/wipe-transactional`) — borra toda la tajada transaccional comp=11 con snapshot `pre_wipe_*` previo, reset de stocks/staging y desvinculación de facturas. Flujo Borrar todo → Importar todo.
- **Botón "Validar stocks"** (`CheckStocksOrphansService` + `GET /check-stocks-orphans`) — casos A/B de inconsistencia de stock, con drill-down de compras/ventas (`ArticleUsageService`, `GET /article-usage`) y limpieza de fantasmas (`CleanGhostStocksService` + `POST /clean-stocks-ghosts`).
- **Seleccionar/Importar todo cross-página** (`SyncLasetSelectableIds` + `GET /selectable-ids?batchId=all`, opción "Todos los batches").
- **Bug CRÍTICO — wipe borraba padres antes que hijos**: los scopes de los hijos hacen JOIN al padre; borrar el padre primero dejaba al hijo **huérfano** y el verify (mismo scope) pasaba ciego. Acumulaba duplicados en cada wipe+reimport (~42k huérfanos) → Fase D no descontaba stock de ventas → reconciliación con miles de deltas. Fix: `array_reverse(DELETE_KEYS)` (hijos→padres, FK-safe) + **barrido de huérfanos** con guard de aislamiento de otras empresas.
- **Bug `albprot`/`albprol` scope por companyCode**: ~11.875 albprot con `companyCode=NULL` quedaban afuera del scope `WHERE companyCode=11`. Fix en `LasetSnapshotRegistry`: scope por `JOIN pedprot` (nnumped).
- **Bug frontend `selectableIds`**: el computed recortaba la selección a la página visible (`this.rows`) → "Importar todo" previsualizaba/importaba solo ~50 (síntoma "se van a importar 2098"). Fix: confiar en `selectedRowKeys`, descartar solo terminales visibles; "Importar todo" fuerza `batchId='all'`.
- **Bug `nnumalb`/`cnumalb` Fase D**: reservar desde MAX de cabecera Y línea (no solo cabecera) para no colisionar con orphans.
- **Recuperación dev**: ciclo limpio Borrar todo → Importar todo → 3161 IMPORTED, **reconciliación 0 grupos con delta** (compras − ventas − stock = 0).

Archivos: `app/Services/Laset/{WipeTransactional,CheckStocksOrphans,CleanGhostStocks,ArticleUsage}Service.php`, `app/Support/LasetSnapshotRegistry.php`, `app/Http/Controllers/Laset/{LasetWipeTransactionalRun,LasetCheckStocksOrphans,LasetCleanGhostStocksRun,LasetArticleUsage,SyncLasetSelectableIds}.php`, `pages/syncLaset.vue`, `plugins/api.js`.

## 2026-05-31 (cont. 2) — Tipo de pedido Laset = INTERNO (orderTypeId=2)

Las órdenes Laset comp=11 quedaban con `pedclit.orderTypeId=NULL` y `cobserv=''` (Fase C no seteaba esas columnas) → no aparecían en el filtro por tipo de `/orders` ni en `listOrderTypes`, y `OrderDto` casteaba `(int)NULL=0`. `orderTypeId` es el código del tipo y `cobserv` su etiqueta (van juntos). Catálogo: 1=DESCARGADO, 2=INTERNO, 3=PEDIDO APP ANDROID, 4=PEDIDO DE INTERNET, 5=PEDIDO LIBRE OPCION, 6=PRESUPUESTO, 7=POSTVENTA.

- **Decisión usuario**: Laset = **INTERNO (orderTypeId=2)**.
- **Importador**: `LasetImportFaseCCommand` ahora setea `cobserv='INTERNO'`+`orderTypeId=2` en el INSERT del pedclit (commit back `f31fceb2`). Vale para todo re-import tras "Borrar todo".
- **Backfill**: `UPDATE pedclit SET orderTypeId=2, cobserv='INTERNO' WHERE companyCode=11` → 423 órdenes actualizadas en dev (sin tocar `cestado`, no dispara el trigger de asignación).

## 2026-06-22 — Cuenta corriente histórica Laset (botón) + FLETE nunca en la compra

Nueva feature [[feature-laset-cuenta-corriente|Import de cuenta corriente histórica comp=11]] y dos reglas de negocio nuevas. Rama `lasetImportFramework`.

- **Botón "Importar cuenta corriente"** en `/syncLaset` (preview→confirmar): parser Python `scripts/laset_ccte_to_json.py` + `LasetCtaCteImportService` + `laset:ccte-import` + `POST /v1/laset/ccte-import`. Carga `MC_CCORRIENTES_MOVIMIENTOS` con `proc=99`. Commits back `73b284b2`, front `1c2e21e`.
- **Incremental POR CUENTA** (back `eecb793e`, front `0261587`): `execute()` reemplaza solo las cuentas presentes en el archivo; las ausentes quedan intactas → se pueden subir planillas parciales. Preview muestra "cuentas a reemplazar" vs "agregar".
- **Parser tolera autoFilter inválido** (`65ac1b16`): bug openpyxl 3.1.x con `customFilter` no numérico/comodín; se parchea `CustomFilterValueDescriptor`.
- **Matching consciente de NB Inc** (`e7f162ae`): una cuenta `-NBinc` es cliente distinto. Antes EMAP quedaba ambigua (096882 vs 100122 NB Inc) → omitida → con dato viejo (daba 63.160,50 en vez de 14.761,50). Ahora hoja NB Inc solo matchea clientes NB Inc y viceversa. Import real: 5.640 movs / 125 cuentas.
- **Excluir hoja USDT** (`33dafcfd`): tesorería que entraba como cliente trucho (cierre ~1,47M).
- **FLETE nunca en la COMPRA** (`9181b687`): el FLETE (art 121944) es un cargo a la VENTA, no una línea de la OC al proveedor. Fase C deja de meterlo en `pedprol`/asignación (`INTERNAL_NO_PURCHASE_ARTICULOS=[121944]`); Fase D deriva `albprol` de `pedprol` → también sale del remito de compra. La venta (pedclil/albclil) lo conserva. Se removieron en dev las 4 pedprol + 4 albprol + 4 asignaciones FLETE comp=11 (OCs 13339/13439/13795/13808). Ver [[feature-laset-import#FLETE]] y [[contexto#FLETE nunca en la compra]].
- **DB dev pasó a remota** (`db-nb-dev.blu.net.ar:41433`, `.env` no versionado): si aparece `Adaptive Server unavailable (10.10.10.47)` es host viejo, no bug. Ver [[contexto#Conexión a la base de datos dev]].

Archivos: `app/Services/Laset/LasetCtaCteImportService.php`, `scripts/laset_ccte_to_json.py`, `app/Console/Commands/{LasetCtaCteImportCommand,LasetImportFaseCCommand}.php`, `app/Http/Controllers/Laset/LasetCtaCteImportRun.php`, `pages/syncLaset.vue`, `plugins/api.js`.

## 2026-06-23 — Compra completa para stock-only + Reservas

Regla: una compra se carga COMPLETA aunque el ítem no se haya vendido. Antes las stock-only categoría C (SKU/proveedor sin alta en catálogo comp=11) se salteaban → OC rota. Nueva nota [[feature-laset-stockonly-completa]]. Commit back `e2828cd8` (rama `lasetImportFramework`).

- **`laset:stockonly-autocreate-catalog`** (command nuevo): auto-crea artículo (clone gemelo/fresh) + marca + proveedor comp=11 para las stock-only cat C. Excluye RMA (→ IGNORED).
- **`laset:stockonly-reservas`** (command nuevo): las stock-only con razón social de cliente real (no el sentinel `STOCK`) se cargan como RESERVA: `pedclit cestado='P'` + `pedclil` + asignación, SIN remito.
- **Wiring**: Fase C delega `autocreate-catalog → fix-stock-only → reservas` → durable en "Borrar todo/Importar todo".
- **Fase D**: `collectPedclitSinRemito` excluye `cestado='P'` (reservas sin remito).
- **`reconcile()`**: ventas = entregado (`albclil`), no pedido (`pedclil`) → la reserva no marca falso delta (compras − entregado − stock = 0).
- **aggregate-match + fix-stock-only**: RMA fuera del predicado stock-only.
- Dev: 11 artículos + 1 proveedor (EVGA), 12 compras materializadas, 4 reservas SIPO en OC 13812 (sin remito), 0 STOCK_ONLY pendientes.

Archivos: `app/Console/Commands/{LasetStockOnlyAutocreateCatalog,LasetStockOnlyReservas,LasetImportFaseC,LasetImportFaseD,LasetRunImportJob,LasetFixStockOnlyPedprol,LasetAggregateMatch}Command.php`.

## 2026-06-23 (cont.) — IVA 0 comp=11 + país de la OC desde columna H

Dos correcciones de datos de Laset (comp=11) detectadas por el usuario. Rama `lasetImportFramework`.

- **Artículos comp=11 SIEMPRE IVA 0** (commits `75ac0782` + `476a97a0`): el auto-create copiaba el `ctipoiva` del gemelo NB (10,5%/21%) o defaulteaba `'M'`. Laset es FOB/exportación → IVA 0 (`ctipoiva/ctipoivac=NULL`, ivaCompra/ivaVenta calculadas = 0). Corregido en los **3 sitios** que crean artículo comp=11 (Fase C, `stockonly-autocreate-catalog`, `fix-cross-company`). Data fix: 209 artículos corregidos. Regla en [[contexto#Laset (comp=11) — siempre IVA 0]].
- **País de la OC desde la columna H de la planilla** (commit `aa5e6b53`): antes Fase C y fix-stock-only hardcodeaban `countryId=5` (USA) en TODAS las OC, pero muchas son de Chile/Paraguay/Colombia/Taiwán/China. Ahora sale de `laset_import_staging.pais_proveedor` (col H) mapeado a `FP_Paises.Id_Pais` vía **`LasetCountryResolver`** (`app/Support/`), con alias de "Estados Unidos" (USA/EEUU/United States/…) y fallback USA. Solo 2 sitios crean `pedprot` (Fase C + fix-stock-only cat D), ambos wireados. Data fix: 191 de 523 OCs corregidas (Chile 102, Paraguay 48, Colombia 38, Taiwán 2, China 1). Ver [[contexto#País de la OC (countryId) — columna H de la planilla]].

Archivos: `app/Support/LasetCountryResolver.php`, `app/Console/Commands/{LasetImportFaseC,LasetFixStockOnlyPedprol,LasetFixCrossCompany}Command.php`.


## 2026-06-23 (cont. 2) — Remito de compra faltante (albprol) + ID fiscal de clientes

- **Remito de compra a nivel línea** (commit `4e983957`): Fase D crea el remito (`albprot`/`albprol`) gateando por OC (`pedprot` sin `albprot`); una vez remitada, no la vuelve a mirar. Las líneas stock-only adjuntadas a una OC ya remitada (import incremental) quedaban **sin albprol → stock colgado sin ingreso** (compra incompleta). Nuevo **`laset:fix-albprol-faltante {--dry-run} {--skip-stock}`** cierra el gap a nivel línea (append al albprot existente o crea header+líneas), suma stock salvo `--skip-stock`. Idempotente, dblib-safe, comp=11. Wireado en `laset:run-import-job` tras Fase D, antes de reconciliar. Backfill dev: 12 albprol (OCs 13737/13749/13812/13826/13858/13859/13860/13861). Ver [[contexto#Remito de compra (albprol) — gating por OC en Fase D]].
- **ID fiscal de clientes creados** (data, sin código): los 47 clientes comp=11 sin `cdnicif` (NB Inc + nuevos del 2026-06-18) recibieron su NRO ID FISCAL desde la pestaña **Database Clientes** (col C) de `docs/laser.xlsx`, formato compacto sin separadores. 36 completados (los gemelos NB Inc comparten CUIT con su cliente normal); 11 sin dato (7 no figuran en la planilla, 4 con placeholder `-`/`INACTIVE`).

Archivos: `app/Console/Commands/{LasetFixAlbprolFaltante,LasetRunImportJob}Command.php`.


## 2026-06-24 — Cuenta corriente de PROVEEDORES Laset (comp=11)

Import de la cta cte histórica de proveedores Laset a `NEW_BYTES.dbo.MS_MOV_CTACTE_PROVEEDORES` (análogo al de clientes). Detalle: [[feature-laset-cuenta-corriente-proveedores]].

- Parser `scripts/laset_prov_ccte_to_json.py` + comando `laset:prov-ccte-import` (idempotente por `USU=Laset`, dblib-safe, comp=11).
- Saldo objetivo = `A favor/Deuda` neto de `NC Disponible` **solo si hay deuda**; movimientos magnitud+TR (factura→38, pago→40, NC→30, ajuste→30/32).
- **Clave correcta = `FP_Proveedores.CCODPRO`** (no el Id_Proveedor interno): Asus 16679 → CCODPRO `002605`. 1er intento bajo `016679` no se veía → rollback (`USU=Laset`) + re-import con CCODPRO.
- Estado dev: 66 proveedores comp=11, 5.573 movimientos, 66/66 reconcilian; legacy NB (29.171) intacto.
- Pendiente: 17 hojas EUR (2ª pasada) + 10 hojas con saldo que no son comp=11.
- Aparte: se restauró el host de DB en `.env` a `db-nb-dev.blu.net.ar:41433` (estaba en el viejo 10.10.10.47).

Commit `ed45cfaf`. Archivos: `app/Console/Commands/LasetProvCtaCteImportCommand.php`, `scripts/laset_prov_ccte_to_json.py`.


## 2026-06-25 — Botón "Importar cta cte proveedores" en /syncLaset

Expone el import de cta cte de proveedores (comp=11) como botón preview→confirmar, mismo patrón que el de clientes. Detalle: [[feature-laset-cuenta-corriente-proveedores#Botón en /syncLaset (preview→confirmar)]].

- Backend (`431219cf`): `LasetProvCtaCteImportService` (lógica canónica) + `LasetProvCtaCteImportRun` (`POST /v1/laset/prov-ccte-import`) + ruta; comando refactorizado a wrapper que delega al servicio.
- Frontend (`cbd8d50`): `provCctImport()` en `api.js` + botón/modal en `syncLaset.vue`.
- Aparte: `.env` a host local de casa `10.10.10.47:1433` (oficina = `db-nb-dev:41433`; misma base, según ubicación).

Archivos: `app/Services/Laset/LasetProvCtaCteImportService.php`, `app/Http/Controllers/Laset/LasetProvCtaCteImportRun.php`, `pages/syncLaset.vue`, `plugins/api.js`.


## 2026-06-26 — Cta cte proveedores: saldo bruto + LST Global + conversión EUR

Commit `d05ddd4c`. Correcciones tras revisar contra la pantalla del ERP:
- **Saldo = celda "A favor / Deuda" TAL CUAL (bruto)** — la "NC Disponible" es crédito informativo y NO va al ledger. Antes la neteaba → Asus daba 47.896 en vez de **53.258,11** (lo que muestra la pantalla). Afectó también AllPlus y TDS (los 3 con deuda + NC). Todos corregidos.
- **"LST Global" excluida**: su C1 es "New Bytes Inc." (intercompañía), no el proveedor LST GLOBAL (le atribuía US$11,3M).
- **2ª pasada EUR**: 13 hojas europeas (Tiroler 79.982 · Winter 7.445 · Danicoop −11.790 + 10 saldadas) convertidas a USD al **TC de cierre** (facturas y pagos EUR × TC_cierre → saldo = afd_EUR × TC_cierre); el **TC real de cada pago se guarda en COTIZACION**. El servicio importa USD + EUR.
- Estado dev: **78 proveedores comp=11 (65 USD + 13 EUR), 5.303 movimientos, todos reconcilian**.
- Pendiente (no comp=11): Rational (EUR US$451k), La Guera, Santa Margherita, Egre + 10 USD con saldo. Ver [[feature-laset-cuenta-corriente-proveedores]].


## 2026-07-15 — Alta de usuario interno: Maximiliano Salomon (NBE ELECTRIC)

Alta de nuevo agente/usuario web en producción, empresa **NBE ELECTRIC (companyCode 9)**, con los permisos clonados de `antonellalo`. Inserción transaccional en 4 tablas: `agentes`, `clientes` (`NewBytes_DBF`), `usuarios_nb`, `permisos_agente` (`NB_WEB`).

- Claves: `ccodage/ID_VENDEDOR 102`, `ccodcli/ID_CLIENTE 100964`, `UserId 84051`, `permisos_agente.id 68`. Login `msalomon` / `msalomon@nbe.com.ar`.
- Se destrabó un **segfault del driver `pdo_sqlsrv`**: crashea al reinsertar valores `datetime` leídos con `SELECT *` (los devuelve como `'May 31 2026 12:00:00:AM'`, irreconvertible). Además **tinker enmascara el segfault como exit 0**. Fix: correr como PHP bootstrapeado normal (no tinker) + nulear todas las columnas datetime del clon salvo `FECHA_ALTA`.
- Runbook actualizado con el fix y el mapeo de `companyCode` por empresa: [[runbook-alta-usuario-interno]].


## 2026-07-23 — Alta de usuario interno: mscomprobantes (template catriel, NB)

Alta de agente/usuario web clonando **catriel** (cuenta admin sobre el agente compartido 12 "Sistema Web"). Empresa **NB (companyCode 4)**. Se optó por crear **agente + cliente nuevos** (no reusar los de catriel). Login `mscomprobantes` / `comprobantes@nb.com.ar`. Tiene permiso de **expedición** (`expedicion=1` y `expedicion_admin=1`, heredados de catriel).

- **Prod (container local):** `ccodage/ID_VENDEDOR 103`, `ccodcli/ID_CLIENTE 101230`, `UserId 84108`, `permisos_agente.id 69`.
- **Replicado en host dev** `db-nb-massql-dev.blu.net.ar,4444` (login `cmercurio`): keys **redescubiertas allí** = `ccodage 102`, `ccodcli 100141`, `UserId 84817`, `permisos_agente.id 68`. Conexión vía override en PHP de `database.connections.sqlsrv.*` + `DB::purge('sqlsrv')`; naming de 3 partes para no depender de la DB default.
- Al clonar de catriel se nuleó `tokenFb` (Firebase) + `ip/os/browser/user_agent` para no arrastrar sesión/push; datetime del cliente nuleados salvo `FECHA_ALTA`. El cliente hereda CUIT/tel/dir del template (cliente interno "no usar").
- Runbook actualizado con este ejemplo y el método de conexión a otro host: [[runbook-alta-usuario-interno]].
