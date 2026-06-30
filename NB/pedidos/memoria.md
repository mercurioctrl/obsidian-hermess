# Memoria

Contexto acumulado de sesiones de trabajo con Claude en este proyecto.

## Usuario

- Desarrollador fullstack senior argentino
- Idioma: español rioplatense
- Prefiere iterar rápido y soluciones simples
- No agregar features no solicitadas

## Feedback

- Siempre verificar cambios con pruebas reales (curl, dev server) antes de reportar como terminado
- MakeSale/RemoveSale usan SQL concatenado — verificar nulls con ISNULL antes de interpolar en queries
- **Cancelaciones LO vs carritos abandonados:** pedidos sin pedclit no son cancelaciones sino carritos abandonados. `motivoCancelacion` tiene prioridad sobre `mp_payment_status`. Total cancelados = created - active (no sumar flags que se solapan)
- **No tocar MakeSale/RemoveSale** desde features nuevos — usar triggers SQL o capa nueva. Decisión explícita en [[feature-asignacion-oc|asignación OC]].
- **Antes de tirar SQL contra dev compartida**, mostrar al usuario host/db/user para que confirme.
- **Queries ad-hoc a SQL Server** (container `api-rest-pedidos-apirest-laravel`): usar archivo PHP + `php artisan tinker archivo.php`, NO `--execute` con `\$`/`::`/comillas anidadas (el escaping shell→tinker rompe con `T_NS_SEPARATOR`). El repo back `app/` está montado en `/var/www/app/` → los archivos del repo se ven adentro sin `docker cp`.

## Proyecto

- Frontend necesita `NODE_OPTIONS=--openssl-legacy-provider` con Node v17+
- Firebase no configurado en local, plugin usa stub vacío
- Tablas clave: pedclit (pedidos), albclit/albclil (remitos), clientes, agentes, articulo
- Gotcha: columnas duplicadas en SELECT por JOINs, case sensitivity en nombres de columna PHP
- Backend usa varias DBs: NB_WEB (default), NewBytes_DBF, LO, NEW_BYTES, CS
- Rutas syncUp usan TOKEN_SYNCUP del .env, no JWT
- Branching: Development como base, hotfix/*, deploy frontend via gamma
- **Dashboard LO** en branch `feature/dashboard-lo` — ver [[modulo-dashboard-lo]]
  - Entregados = `MS_VENTAS_REMITOS.ID_STATUS > 1` (no `pedclit.delivered`)
  - Carritos cuenta desde pedidosCabecera sin requerir pedclit
  - navList[1] = Libre Opción, navList[2] = Pedidos (desplazado)
  - opcache PHP: ejecutar `docker exec api-rest-pedidos-apirest-laravel php -r "opcache_reset();"` después de modificar PHP
  - Filtros OrderList agregados: `loOnly`, `loCancelled`, `motivoCancelacion`, `mpPaymentStatus`, `mpPaymentStatusDetail`, `sinMotivo`
- **[[feature-asignacion-oc|Asignación OC ↔ Venta]]** en branch `feature/asignacion-oc-pedclil` (ambos repos)
  - Tabla `pedclil_oc_asignacion` (NewBytes_DBF). FK lógica `pedclil_id` (pedclil.id IDENTITY).
  - Vistas `vw_saldo_oc` y `vw_pedclil_estado_asignacion`. Trigger `tg_pedclit_cestado_asignacion`.
  - 5 endpoints HTTP en `Asignacion/AsignacionController` + command `asignaciones:fifo`.
  - Env vars: `ASSIGNMENT_FEATURE_ENABLED`, `ASSIGNMENT_COMPANIES`, `ASSIGNMENT_ALLOW_PARTIAL` (deben coincidir backend↔frontend).
  - **Driver dblib no soporta índices filtrados** → todos los índices del feature van sin `WHERE`.
  - **pedprol no tiene IDENTITY** → identificación por tupla `(nNumPed, nLinea, cRef)`.
  - Decisiones cerradas con el usuario:
    - FIFO por fecha de OC (sin otras políticas en v1)
    - Asignación parcial permitida; no bloquea MakeSale
    - Sin migración retroactiva (Opción A)
    - Cross-warehouse permitido a nivel asignación
    - Toda OC con saldo es candidata sin filtrar por cEstado (Opción C)
  - Cambios colaterales en backend: `OrderDetailDto.companyCode`, `OrderItemDto.pedclilId`. Eran necesarios para que el frontend del feature funcione (item.id estaba mapeado a articulo.ID_ARTICULO, no a la línea de venta).
  - Documentación canónica: `/Users/hermess/www/pedidos/docs/asignacion-oc-pedclil.md` y `database/sql/README.md`.
  - **Iteraciones 2026-04-24** post primer merge a Development:
    - `cantidad: 0` en `PUT /asignaciones/lineas/{id}` se ignora silenciosamente; items vacíos / todos en 0 = liberar todo (DELETE-like).
    - Modal: columnas nuevas **Proveedor** (`FP_Proveedores.cnompro`) y **Proforma** (`PedProT.CSUPROF_TEMP`) via JOIN en `candidatasFifo` (sin tocar la vista).
    - Modal: número de OC clickeable → `compras.saftel.com/orders` con `companyCode`.
    - **Fix sutil**: el modal NO debe rellenar OCs sin vigente con sugerencia FIFO si la línea ya tiene asignaciones guardadas. Si lo hace, parece que el save anterior falló. Ver [[feedback_modal_asignacion_no_fifo_si_vigentes]] (en memoria local).
    - Workflow de merge: cuando Development recibe PRs paralelos sobre `AsignarOCModal.vue`, hacer `git fetch && git reset --hard origin/Development` antes de pushear, force-push con `--force-with-lease`.
  - **Iteraciones 2026-04-24 (segunda tanda)** — bloques de contexto read-only en el modal:
    - Columna **Costo** (`pedprol.nPreDiv` por `nNumPed + cRef`) agregada a la tabla editable.
    - Dos endpoints GET nuevos: `/asignaciones/stock-almacenes` (stock del SKU por depósito) y `/asignaciones/comprometido` (pedidos pendientes + remitos sin facturar del SKU). Total: **7 endpoints** en `AsignacionController`.
    - Render en modal: chips con `a-tag` para stock (verde si >0) + `a-collapse` con dos `a-table` compactas para órdenes/remitos.
    - Regla general: **separar estado editable (filas con input) de contexto read-only** (chips / collapse). El contexto va fuera del `<a-table>` principal. Ver [[feedback_modal_contexto_vs_edicion]] en memoria local.
    - Schema confirmado (gotchas): `FP_Almacen.CNOMBRE` (no `cDesAlm`); `clientes` tiene dos PKs (`ccodcli` string para pedclit, `ID_CLIENTE` int para albclit); `albclit.lfacturado=0` = reserva formal sin factura; `stocks.nstock` = físico, `stocks.nstock_reserva_pedidos` = ya reservado.
  - **Iteraciones 2026-04-25** — modo read-only, persistencia en DB, JWT extendido:
    - Modal en modo **solo lectura** para pedidos remitidos (`cestado='S'`) — prop `readOnly`, botón 👁️ en `Detail.vue`, acepta asignaciones en estado V o C, filas huérfanas para OCs sin saldo disponible. Permite ver la asignación consumida sin modificarla.
    - **Columna DB nueva** `pedclil_oc_asignacion.costo_seleccionado BIT NOT NULL DEFAULT 0` — reemplaza la persistencia en localStorage (que era por-navegador). Portable entre máquinas. Camino: PUT items → request valida → service propaga → insertAsignacion graba → asignacionesDeLinea devuelve. Persistencia solo al Guardar (no hay endpoint PATCH granular por toggle).
    - Scripts DDL `database/sql/2026_04_25_001_{add,drop}_costo_seleccionado.sql` — con `USE [NewBytes_DBF]; GO` y `sys.columns/sys.tables` para cross-db robusto.
    - **JWT extendido a 60 días** — `.env backend` `JWT_EXPIRATION_TIME="now + 60 days"` (antes 24 hours); `nuxt.config.js` `refreshToken.maxAge = 60 * 60 * 24 * 60`. Rotar `JWT_SIGNATURE_KEY` si hay que invalidar todos los tokens.
    - **Gotcha crítico SSMS**: pegar apply + drop en la misma ventana los ejecuta a ambos, borrando el schema recién creado. Hay que tratarlos como scripts separados. Ver [[feedback_ssms_gotchas|feedback memoria local]].
    - **Gotcha cosmético SSMS**: `SET IMPLICIT_TRANSACTIONS ON` produce warning "ROLLBACK TRANSACTION sin BEGIN TRANSACTION" tras los DDL. Ignorar o desactivar.
  - **Iteraciones 2026-04-24 (tercera tanda)** — flujo "Guardar con costo" y rediseño del dropdown:
    - Título dinámico del modal: `branch - order - id_articulo - producto_nombre (Asignar línea de compra)`. Requiere JOIN a `articulo.cDetalle` en `pedclilInfo`.
    - Checkboxes por fila en columna Costo con persistencia en `localStorage['asignarOC.costoTildados.{pedclilId}']`. El bloque "Costo promedio ponderado" suma las filas tildadas con cantidad > 0.
    - Botón **"Guardar con costo"** hace `PATCH /v1/orders/addItem` con el promedio ponderado como `costForSale`, después persiste la asignación OC. El modal emite `saved: { conCosto }` y `Detail.vue` refresca el detalle solo si `conCosto=true` (sino la columna Costo sigue mostrando el valor viejo).
    - **Gotcha crítico del PATCH `/orders/addItem`**: `selectedPrice` DEBE ser `pedclil.npreunit` (precio unitario real > 0), NO `listaPrecio` (código 0/1/2… — el backend rechaza con *"No se permite un precio menor o igual a 0"* si se manda 0). `pedclilInfo` ahora expone `precio_unitario`, `id_almacen`, `lista_precio`.
    - **Tag "ASIGNADA"** (violeta) en dropdown de Costo de `Detail.vue` cuando `costForSale === costoPonderadoPorLinea` (mismo redondeo en ambos lados). Alternativa al no tener columna `cost_source` en DB; heurística frágil pero suficiente.
    - **Bug de redondeo JS** — `toLocaleString` y `toFixed` redondean distinto en bordes como `139.725` (IEEE-754 lo guarda como `139.7249999…`). Fix: usar `Math.round((x + Number.EPSILON) * 100) / 100` como única regla, tanto en display como en PATCH/store. Ver [[feedback_redondeo_js_consistente]] en memoria local.
    - Dropdown de Costo rediseñado (`Detail.vue`): tags redondeados (ACTUAL/PROMEDIO/ASIGNADA), `tabular-nums` para alinear precios, `dropdown-match-select-width=false` + `minWidth: 320px`. Los estilos van en `<style lang="less">` **no scoped** porque los `a-select-option` se portal-izan al `body`.

## Referencias

- Bugs trackeados en Jira (integrado via apiJira.client.js)
- Docker container backend: `api-rest-pedidos-apirest-laravel` (puerto 8093)
- DB dev: SAFDB2 (host 190.210.23.108:1433), user `eferreyra_devweb01` — autorizada para uso por el usuario
- Documentación de features grandes vive en `docs/` del monorepo + nota dedicada en bóveda

## Ver también

- [[pedidos]] — Índice del proyecto
- [[contexto]] — Gotchas técnicos
- [[arquitectura]] — Estructura
- [[feature-asignacion-oc]] — Feature actual
- [[modulo-dashboard-lo]] — Feature reciente
- [[modulo-makesale]] / [[modulo-removesale]]

- **[[feature-laset-import|Laset Import Framework]]** en branch `lasetImportFramework` (ambos repos)
  - CompanyCode=11. Importadora uruguaya — ver [[contexto#Empresas activas (FP_Empresas)]].
  - **Regla cero**: nunca modificar tablas ERP existentes (`pedprot`/`pedprol`/`pedproi`/`pedclit`/`pedclil`/`stocks`/`FP_*`/`forwarders`/`rebates`). Solo lectura. Toda metadata de matching vive en `laset_import_staging.matched_*`. Ver [[contexto#Regla cero: tablas ERP son read-only]].
  - **Modelo canónico ERP**: compras = `pedprot` + `pedprol` + `pedproi` (incluye cargos extra), ventas = `pedclit` + `pedclil`, stock = `stocks` (por almacén, sin `companyCode`). Ver [[contexto#Modelo canónico ERP (compras / ventas / stock)]].
  - **Gotcha `pedproi`**: NO es solo impuestos — guarda cargos extra del pedido de compra (`cdescrip='camion'` $50/$200). Linkea a `pedprot.nNumPed`, NO a `pedclit`. 158 rows total para companyCode=11.
  - **Gotcha `stocks`**: no tiene `companyCode`. Filtrar por almacenes Laset: DOM, BON, GRI, SAF, URU, ASI.
  - **Gotcha `rebates` huérfana**: 12 rows, schema primitivo, sin `companyCode`, creada con `NewTable` vacía el 2025-11-01. Restos de intento abandonado. NO usar.
  - **Schema staging creado 2026-05-14**: `laset_import_batches` (cabecera por carga) + `laset_import_staging` (67 cols crudas NVARCHAR lossless + 8 cols matching con CHECK enum). Scripts `database/sql/2026_05_14_001_{create,drop}_laset_import_staging.sql`. Aplicados.
  - **Identidad contable**: `SUM(pedprol.nCanPed) − SUM(pedclil.ncanped) = stocks.nstock + nstock_ingresando` por SKU+almacén+companyCode. Sanity check para reconciliación.
  - **CFE Uruguay ya implementado**: tablas `FP_FactWebCliEncabezado_Uy` (179 rows), `FP_FactWebCliDetalle_Uy` (1411), `FP_DocumentosUY` (6), `FP_ComprobantesUY` (9). IVA 22%, DOL, tipoCfe 101=eTicket/102=NC/103=ND. Adendas confirman beneficiario "Laset Sociedad Anonima". Es la mitad downstream del flujo de Laset ya migrada.
  - **Forwarders Laset**: 84 rows con `companyCode=11` en tabla `forwarders` — DHL, Peniel International (Miami), etc.
  - **Insight planilla**: cada fila es 1 venta ↔ 1 compra (Qty=CANTIDAD 100% del tiempo). 339 de 438 Vendor Invoices se repiten en >1 fila → split manual antes de cargar al Excel.
  - **Sistema soporta 11 empresas activas**, no solo NB/NBElectric/LO como decía el CLAUDE.md histórico. Ver [[contexto#Empresas activas (FP_Empresas)]].
  - Próximos pasos: cargador PHP que parsee `docs/laser.xlsx` → poblar staging → reconciliación heurística → migración del delta.
  - Documentación canónica: `docs/laset-import-framework.md` (repo) y [[feature-laset-import]] (Obsidian).

- **[[feature-laset-import|Laset Import]] post aggregate matching (2026-05-14 PM)**:
  - **Decisión**: planilla = fuente de verdad para comp=11 (ERP comp=11 ex-carga-fallida). Ver [[contexto#Laset: planilla = fuente de verdad]].
  - **Regla de aislamiento**: cualquier `DELETE`/`INSERT` sobre tablas ERP durante este feature debe llevar `WHERE companyCode = 11` SIEMPRE. Otras companies intocables. Ver [[contexto#Laset: regla de aislamiento companyCode != 11]].
  - **Bridge SKU**: `articulo.ID_PRODUCTO` (varchar) = SKU fabricante, `articulo.ID_ARTICULO` (int) = PK interna que linkea pedprol/pedclil/stocks. Cobertura inicial 84% directa, +14 con normalizaciones automáticas, +5 servicios.
  - **Tabla `laset_sku_alias`** (en `NewBytes_DBF.dbo`): persiste alias planilla↔ID_Articulo + services + ignored. Bridge view UNIONa articulo + alias. CHECK constraint en source (`auto:trim|auto:nospace|auto:nohyphen|auto:hyph2sp|auto:sp2hyph|auto:alnum|auto:split-slash|auto:last-word|manual|service|ignored`).
  - **Aggregate matching aplicado**: 2461/3007 filas MATCHED (82% importable), 147 UNMATCHED por SKU huérfano, 399 IGNORED basura+services. Score 100=ERP-exact, 90=trust-planilla-discrepancia, 80=trust-planilla-delta-puro, 0=bloqueado/basura.
  - **Plan migración 3 fases**: A) alta huérfanos en articulo por catálogo, B) DELETE ERP comp=11 sin contraparte, C) INSERT 2461 MATCHED → ERP + asignaciones.
  - **CSV huérfanos** generado en `docs/laset_orphan_skus.csv` (+ `.md` legible) — 100 SKUs únicos para que catálogo dé de alta.
  - **Gotchas dblib/SQL 2012** acumulados (ver `feedback_dblib_gotchas` en memoria local):
    - PhpSpreadsheet inviable con xlsx grandes → preprocesar con Python+openpyxl en host (`scripts/laset_xlsx_to_json.py`).
    - Segfault con UPDATE prepared en loop → tabla tmp + UPDATE FROM JOIN single-statement.
    - dblib no auto-castea DECIMAL → INT en columnas tmp.
    - `CREATE OR ALTER VIEW` y `DROP VIEW IF EXISTS` no soportados en 2012 → `IF OBJECT_ID(…,'V') IS NOT NULL DROP VIEW`.
    - `pedprot.sitio=0` vs `pedprol.sitio=NULL` → joinear solo por `nNumPed`.
  - **Scripts SQL versionados**: `database/sql/2026_05_14_00{1,2,3}_*.sql` (+ drops simétricos). Lista en `database/sql/README.md`.
  - **Comando**: `php artisan laset:import-staging /tmp/laset.json --imported-by=hermess [--force] [--dry-run]`.
  - **Estado vivo** del feature en archivo: `project_laset_import_framework` (memoria local) y `docs/laset-import-framework.md` (repo).

- **[[feature-laset-import|Laset Import]] post Fase B + discovery Fase C (2026-05-14 PM)**:
  - **Fase B ejecutada**: DELETE total ERP comp=11 — 7822 filas borradas (pedprot=386, pedprol=1349, pedproi=31, pedclit=363, pedclil=1847, albprot=526, albprol=1205, albclit=331, albclil=1746, pedclil_oc_asignacion=38). Backups in-DB en `NewBytes_DBF.dbo.laset_phase_b_backup_*` (10 tablas). Otras companies intactas (verificado pre/post snapshot). Script: `database/sql/2026_05_14_004_phase_b_delete_comp11.sql`.
  - **Decisión Fase B**: DELETE total + re-INSERT en lugar de row-level matching, porque el matching staging↔ERP es agregado por SKU.
  - **Bug crítico atrapado en revisión SQL**: `pedclit.cnumped` NO es único globalmente (5 colisiones comp=11↔comp=4: 10338002, 10338022, 10338027). PK efectiva `(cnumped, cnumsuc)` — uq_pedclit. Refactorizado a `DELETE x FROM x JOIN pedclit ON cnumped+cnumsuc WHERE companyCode=11`. Ver `feedback_pedclit_pk_compuesta` (memoria local).
  - **Bug también atrapado**: conteo inicial `albprot=370` era falso (subselect cruzado nnumalb↔nNumPed). Real: 526 (todos comp=11, rango 2026-03-02→2026-05-12). 369 con pedprot padre + 157 huérfanos (compras directas sin OC).
  - **Pre-check assertions** (pedido del usuario): batch separado con `DECLARE @bad / SELECT @bad / IF @bad > 0 THROW 50001` antes de cada DELETE. Loader PHP propaga excepción y aborta. Ver `feedback_pre_check_assertions_destructivos` (memoria local).
  - **Discovery Fase C**: schema 6 tablas mapeado. 2461 MATCHED → 417 pedprot + 396 pedclit + ~1349 pedprol + ~1847 pedclil ≈ 4078 INSERTs. nNumPed manual desde MAX+1=13219, cnumped manual desde MAX+1=10459501.
  - **Tabla maestra moderna `FP_Proveedores`** (no `proveedo` legacy que tiene `cnompro` vacío). 80 proveedores comp=11 ya existentes. Match staging.proveedor → FP_Proveedores `WHERE companyCode=11`: 25/28, 3 a auto-crear. Ver `project_erp_master_tables_fp` (memoria local).
  - **Regla "nunca compartido entre companies"** (confirmada por usuario): proveedores y clientes pertenecen a EXACTAMENTE una company. CCODPRO único globalmente; ccodcli puede tener duplicados pero solo intra-company. Ex-carga-fallida pedprot/pedclit comp=11 referenciaba CCODPRO/ccodcli de NB (comp=4) — data sucia, ignorar al planear Fase C.
  - **Match clientes** (`WHERE companyCode=11` estricto): 50/56 OK, 6 a auto-crear.
  - **Match SKUs**: 806/820 OK vía `articulo.ID_PRODUCTO`, 14 bloqueados (Fase A pendiente).
  - **Decisiones de implementación Fase C**: artisan command PHP con `--dry-run/--limit/--chunk`, auto-crear FP_Proveedores/clientes mínimos comp=11, idempotencia via `match_status=IMPORTED`. NO implementado todavía.

- **[[feature-integrar-eccn|integrarECCN]]** en branch `integrarECCN` (ambos repos, desde `lasetImportFramework`)
  - **ECCN** = Export Control Classification Number — string de normativa de exportación EE.UU. (`EAR99`/`5A992`/`4A994`/`4A001`/`5A992C`). Depende de **dos ejes**: familia del producto + proveedor.
  - **Tabla `ecc_familia_proveedor`** (`NewBytes_DBF.dbo`) — matriz familia × proveedor → `eccn` + `codigo_arancelario`. FK lógicas (no enforced) a `familias`/`FP_Proveedores`. `origen` `C`=CSV / `M`=manual. SQL `database/sql/2026_05_21_001_create_ecc_familia_proveedor.sql`.
  - **Comando `ecc:import-categorias`** — lee `database/data/eccCategorias.csv`, resuelve proveedor/familia por `companyCode` con match exacto normalizado, descarta filas sin match en ambos ejes. Idempotente (borra+reinserta `origen='C'`, respeta `origen='M'`).
  - **Decisión usuario**: solo match exacto, NO fuzzy.
  - **Permiso `eccView`** (columna `permisos_agente.eccView`): viaja en el JWT vía la query `login()` → gotcha: tokens viejos no lo traen, hay que re-loguearse. Activado a 5 usuarios (agente 12 Catriel + 4 de Laset comp=11).
  - **Detalle de orden**: el `ecc` por ítem (`{value, editable}`) se agrega a la query **solo si hay permiso** (JOIN concatenado condicionalmente → cero costo para quien no lo tiene). Proveedor desde la OC asignada (`pedclil_oc_asignacion`, `OUTER APPLY TOP 1`). Gating del campo en JSON: propiedad tipada sin default + `property_exists` → `json_encode` la omite sin permiso.
  - **Carga manual** `POST /v1/ecc`: upsert con `origen='M'` (protege la edición de un futuro `ecc:import-categorias`, que reemplaza solo `origen='C'`). Front: lápiz + popover inline en la columna ECCN de `Detail.vue`.
  - **Estado 2026-05-21**: tabla + 94 vínculos del CSV + permiso + columna ECCN con carga manual, todo en **dev**. Commiteado y pusheado (back `2c87867e`, front `d0083b6`). SQL `2026_05_21_00{1,2}` pendientes en prod. **Doc vivo y completo en `CLAUDE.md` → sección `### Feature integrarECCN`.**
  - `familias` (modelo `App\Models\Category`, PK `ID_FAMILIA`) tiene `companyCode` y `defaultTariffPosition` (HS por familia); linkea a artículos por `articulo.ID_FAMILIA`.

### FP_* vs legacy

El ERP tiene **dos generaciones** de tablas maestras:
- **Legacy** (`proveedo`, `articulo`): char(N) con padding, `cnompro` vacío para Laset, deprecadas para flujos nuevos.
- **Moderna** (`FP_Proveedores`, `FP_Marcas`): nvarchar, columnas modernas (NombreComercial, Direccion, Id_Pais, Fecha_Alta, etc), datos poblados.

Para resolver un proveedor/cliente, **usar la tabla moderna** con `WHERE companyCode = N` estricto. NO usar legacy. El INSERT de nuevo proveedor/cliente debe ir a la moderna.

### PK compuesta pedclit

`pedclit.cnumped` NO es único globalmente (verificado: 5 colisiones reales entre comp=11 y comp=4). PK efectiva = `(cnumped, cnumsuc)` (`uq_pedclit` UNIQUE). Misma regla aplica a `albclit.cnumalb`. Cualquier `DELETE/UPDATE/JOIN` sobre pedclit/pedclil/albclit/albclil debe usar **JOIN compuesto**, NO `WHERE cnumped IN (SELECT cnumped FROM ...)`.

`pedprot.nNumPed` y `albprot.nnumalb` SÍ son únicos globalmente — esos pueden usar subselect IN.

Distribución cnumsuc en pedclit comp=11 (al pre-Fase B): `0002`=357, `0000`=5, `0010`=1.

### Pre-check assertions destructivos

Para DELETE/UPDATE destructivos en SQL Server, agregar pre-check en su propio batch antes:
```sql
DECLARE @bad INT = 0;
SELECT @bad = COUNT(*) FROM <set a borrar> WHERE <criterio que detecte filas que NO cumplen aislamiento>;
IF @bad > 0 THROW 50001, [ABORT <tabla>], 1;
GO
DELETE ... ;
GO
```
THROW (severity 16) está disponible desde SQL 2012, aborta el batch. Loader PHP del README (`unprepared` en loop sin try/catch silencioso) propaga la excepción y aborta el script entero antes de tocar nada. Defense in depth.

### Almacenes Laset reales

Para `companyCode=11` (Laset), los almacenes válidos en `FP_Almacen` son **únicamente** DOM, BON, GRI, URU, ASI (más TES de test). **`SAF` NO es almacén de Laset** — pertenece a NB (comp=4) y nunca debería aparecer en pedprot/pedclit/pedclil/stocks comp=11.

Mapping `staging.deposito` → almacén Laset (cCodAlm/warehousesId/ID_ALMACEN):
- `DOMESTIC MIAMI` → DOM (9)
- `BONDED PROVEEDOR`/`BONDED-FASTMARK`/`BONDED-SEASIDE` → BON (11) — todos los bonded consolidan a BON (BON tiene 3 IDs: 11, 13, 16)
- `GRIS` → GRI (10)
- `URUGUAY` → URU (14)
- `ASIA` → ASI (15)

Las 3 columnas (`cCodAlm`+`warehousesId` en pedprot, `ccodalm`+`ID_ALMACEN` en pedclit, `ID_ALMACEN` en pedclil) deben quedar **coordinadas**. Para descubrir almacenes de una company N: `SELECT CCODALM, ID_ALMACEN FROM FP_Almacen WHERE companyCode = N AND deleted_at IS NULL`.

NO confiar en backups de carga fallida (ej. `laset_phase_b_backup_pedprot` listaba SAF, pero era data sucia que mezclaba data NB).

### Doble filtro: company del item + del almacén

Para `stocks` (y otras tablas compartidas sin `companyCode` propio), filtrar por **AMBOS criterios simultáneos** al hacer DELETE/UPDATE/SELECT por company:

```sql
WHERE s.cCodAlm IN (almacenes de la company)
  AND s.ID_ARTICULO IN (SELECT ID_ARTICULO FROM articulo WHERE companyCode = N)
```

**Caso real** (Laset reset stocks 2026-05-14): 286 filas legítimamente comp=11 reseteadas; 302 filas con articulo NB (comp=4) en almacenes Laset preservadas (17 unidades, items compartidos físicamente entre NB y Laset). Si se hubiera filtrado solo por almacén, se habría tocado data NB.

**Identidad contable post-reset**: saldo neto comp=11 = 0 ✓. SKU global 657/657 cuadran (100%). Por (SKU, almacén) 1059/1090 (97%); las 31 discrepancias son cross-warehouse internas del ERP (compra en X, venta desde Y, neto SKU=0) — no bug.

### Resolución de maestros filtra companyCode

Toda resolución de un identificador de negocio a su ID interno
(SKU→`articulo.ID_ARTICULO`, razón social→`clientes.ccodcli`,
proveedor→`FP_Proveedores.CCODPRO`) **debe filtrar siempre `companyCode=N`**.
Un mismo `ID_PRODUCTO`/nombre existe en varias companies con ID distinto; sin
el filtro se liga la línea a un artículo de OTRA company.

**Caso real (Fase C, 2026-05-15)**: `resolveMasters` resolvía SKU sin
`companyCode=11` → 56 `pedprol` + 56 `pedclil` de órdenes comp=11 apuntaron a
44 artículos NB (comp=4). Lo detectó el pre-check de aislamiento de Fase D
(THROW si el delta de stock toca un artículo no-comp-11), no un test. Fix:
filtro en `resolveMasters` + SQL `2026_05_15_002` (remap de los 5 con gemelo
comp=11). 39 SKUs sin gemelo → Fase A.

**Cómo aplicar**: query de resolución con `->where('companyCode', N)`; si no
hay match, BLOQUEAR la fila (no agarrar otra company). Antes de UPDATE sobre
tabla compartida sin companyCode (`stocks`): JOIN a la maestra + `companyCode=N`
+ pre-check THROW. Relacionado con [[memoria#Doble filtro: company del item + del almacén]].

### Snapshot / Restore Laset (reversibilidad)

`laset:snapshot <tag>` copia la tajada comp=11 (14 tablas del registro
`App\Support\LasetSnapshotRegistry`, incl. cross-DB `NB_WEB.registro_stock`
por marcador `fichero LIKE 'Laset Fase D%'`) a `laset_snap_<tag>_*` +
`laset_snapshot_manifest`. `laset:restore <tag>` borra la tajada actual y la
repone desde el snapshot (IDENTITY_INSERT + columnas explícitas sin
computadas; trigger `tg_pedclit_cestado_asignacion` off/on; pre-check vs
manifiesto; todo en 1 transacción). **Correr snapshot ANTES de cada
proceso/sesión.** Probado end-to-end 2026-05-15.

Gotchas: `DISABLE/ENABLE TRIGGER` NO admite prefijo de DB → ejecutar con
`EXEC NewBytes_DBF.sys.sp_executesql N'DISABLE TRIGGER [dbo].[..] ON [dbo].[..]'`.
`IDENTITY_INSERT` exige lista de columnas y una tabla a la vez (1 unprepared
batch). Tablas con identity: pedprot.id_pedprod, pedclit.id, pedclil.id,
pedclil_oc_asignacion.id, pedproi.id, albclit.id, albclil.IdDetalleRemito,
stocks.id_auto, FP_Proveedores.ID_PROVEEDOR, registro_stock.id.

### Identidad contable Laset

`Σ compras(pedprol) − Σ ventas(pedclil) − stocks.nstock = 0` por
`(ID_Articulo, almacén)` comp=11. Fase D la cumple por construcción (resetea
stock a 0 y escribe `nstock = compras − ventas`). Si no da 0 en algún grupo,
o falta procesar ese trade (orden diferida) o hay bug — verificar contra
órdenes diferidas antes de asumir error.

### Stocks: tabla por (ID_ARTICULO, ID_ALMACEN), requiere UPSERT

`stocks` es tabla real 21 cols (`id_auto` IDENTITY). Un artículo comp=11 NO
tiene fila en `stocks` para cada almacén — hay que **INSERT fila mínima** si
falta (no solo UPDATE), si no se pierde el movimiento. ccodalm/almacén
válidos = `FP_Almacen WHERE companyCode=11` (NUNCA hardcodear IDs).

---

## 2026-05-29/30 — Bugs históricos en Fase C resueltos

Tres bugs en `LasetImportFaseCCommand` resueltos con patches + comandos retroactivos. Doc completa en [[feature-laset-fix-pedprot-stockonly]].

### Bug A — pedprol no consolidaba por (pedprot, ID_Articulo)

Cada staging row generaba 1 pedprol independiente. N filas del mismo SKU dentro de la misma OC = N líneas (prohibido). Fix: nuevo `buildPedprolGroups()`, espejo del `buildPedclilGroups`. Backfill: `laset:fix-pedprot-dup` fase intra.

### Bug B — pedprot no se reusaba cross-batch

`$pedprotByKey` se armaba solo desde rows del run actual. Cuando llegaba la misma `(prov, vpi, vinv)` en un batch posterior, creaba pedprot duplicada en vez de agregar línea al existente. Fix: nuevo `mergeExistingPedprot()` consulta ERP. Backfill: `laset:fix-pedprot-dup` fase inter.

### Bug C — stock-only descartado como basura

Filas `year=1900 + customer_invoice vacío + vpi/vinv/sku/qty>0` son **stock disponible** (compra al proveedor sin venta aún), no basura. Aggregate-match paso 4a las marcaba IGNORED → pedprol quedaba corta. Fix: nuevo paso `4a-pre` en aggregate-match reclasifica como `STOCK_ONLY`. Fase C delega a `laset:fix-stock-only-pedprol` via `Artisan::call`. Backfill: el mismo comando aplica retroactivo.

Detalles en [[feature-laset-fix-pedprot-stockonly#Bug A]], [[#Bug B]], [[#Bug C]].

## Re-numerar PK/UNIQUE con buffer negativo

Cuando hay que re-numerar `nLinea` (o cualquier columna que forma parte de un UNIQUE compuesto) y los valores nuevos pueden chocar transitoriamente con los viejos, hacer el UPDATE en **2 pasos** con un valor "imposible" intermedio:

```sql
-- Paso 1: mover al buffer negativo
UPDATE pl SET pl.nLinea = -(m.new_nLinea + 1000000)
FROM pedprol pl JOIN #map m ON ...;

-- Paso 2: aplicar el valor final desde el buffer
UPDATE pl SET pl.nNumPed = m.winner, pl.nLinea = m.new_nLinea
FROM pedprol pl JOIN #map m ON pl.nLinea = -(m.new_nLinea + 1000000) ...;
```

Caso real: `LasetFixPedprotDupCommand::applyInter` fallaba con violación de PK al mover pedprol entre OCs sin buffer. Patrón aplicable a cualquier renumeración por ROW_NUMBER sobre tablas con UNIQUE compuesto.

## Invariante con hash para fixes destructivos

En comandos que mutan data en lote, capturar **dos** invariantes pre/post:
1. `SUM(qty)` total.
2. `SUM(qty * ID_Articulo)` como hash.

Un solo conteo puede coincidir por casualidad si dos errores se compensan. Agregar el hash que mezcla dos columnas atrapa bugs donde la qty se preserva pero terminó en el ID_Articulo equivocado.

Caso real: primer intento de `LasetFixPedprotDupCommand` perdió 48.427 unidades por colisión de nLinea. `total_qty` pasó de 139.240 a 90.813. Restore inmediato del snapshot + bug fix (introducir buffer negativo). Sin la doble invariante, el daño habría pasado por verify simple ("0 grupos dup restantes" era cierto).

## NVARCHAR length cap en columnas enum/status

Antes de agregar nuevos valores al CHECK constraint de una columna string, verificar largo declarado con INFORMATION_SCHEMA. SQL Server tira `String or binary data would be truncated` sin decir qué columna ni qué valor — fácil de pasar por alto cuando el ALTER del CHECK funcionó OK pero el primer UPDATE de aplicación falla y rompe la transacción global.

Caso real: `laset_import_staging.match_status` era `NVARCHAR(20)`. Agregué `STOCK_ONLY_SUPERSEDED` (21 chars) al CHECK; `markSuperseded` falló por truncate y abortó toda la consolidación (rollback OK gracias a transacción). Fix: `ALTER COLUMN match_status NVARCHAR(30)` antes del CHECK.

**Recomendación**: declarar columnas enum/status como `NVARCHAR(30)` por defecto en tablas nuevas. Costo de storage despreciable.

## Reglas operativas Laset (afianzadas)

1. **Snapshot SIEMPRE antes** de cualquier fix con `laset:snapshot <tag>`. Si algo sale mal: `laset:restore <tag> --force`.
2. **Dry-run primero**, real después. Cada comando de fix tiene `--dry-run`.
3. **Pre-check THROW** en cada comando: aislamiento comp=11, no cross-company.
4. **Verify integrado con invariantes**: si el delta no es exactamente lo esperado, THROW + rollback.
5. **Idempotencia obligatoria**: re-correr sobre data limpia = 0 cambios.
6. **dblib-safe**: tabla tmp + UPDATE FROM JOIN single-statement. NUNCA loops de UPDATE individuales (segfault).


## articulo.Id_Marca → NB_WEB.dbo.marcas (NO FP_Marcas)

La FK lógica de `articulo.Id_Marca` apunta a **`NB_WEB.dbo.marcas.id`**, no a `NewBytes_DBF.dbo.FP_Marcas`. Toda la app joinea por `articulo.ID_MARCA = marcas.id`: Brand model, TotalSales, Statistics, Marketing, Product, ChangeClientOrder, Downloader, Report, etc.

`NB_WEB.dbo.marcas` tiene `companyCode` — **scope por empresa**, una "ASUS" para comp=4 (id=65) NO es la misma que "ASUS" para comp=11 (id=1290). El importer Laset estaba creando marcas en `FP_Marcas` (tabla legacy sin PK ni companyCode) y rompió `articulo.Id_Marca` para 151 artículos comp=11.

Regla: al crear/auto-crear artículos, SIEMPRE resolver/crear marca en `NB_WEB.dbo.marcas` con `companyCode=N` (la empresa del articulo). Lookup case-insensitive scopeado: `WHERE UPPER(LTRIM(RTRIM(referencia))) = ? AND companyCode = N`. Aislamiento estricto: una marca de comp=4 NO sirve para comp=11; si "ASUS" existe en comp=4 pero no en comp=11, hay que **crear otra entrada** comp=11.

## IDENTITY + dblib

Para tablas SQL Server con `id INT IDENTITY` accedidas vía driver `dblib`, NO usar:
- INSERT con id explícito (`Cannot insert explicit value for identity column when IDENTITY_INSERT is set to OFF`).
- `SET IDENTITY_INSERT ON/OFF` dentro de `DB::unprepared` (dblib pierde estado entre statements).
- `MAX(id) + 1` para pre-reservar (rompe contrato IDENTITY, colisiona bajo concurrencia).

Patrón correcto: omitir `id` del INSERT y capturar inmediato con `SELECT CAST(SCOPE_IDENTITY() AS INT) AS id`:

```php
foreach ($items as $name) {
    DB::connection('sqlsrv')->insert(
        "INSERT INTO NB_WEB.dbo.marcas (referencia, oculto, siteShow, companyCode, ocultarNbeB) VALUES (?, 0, 0, ?, 0)",
        [$name, 11]
    );
    $r = DB::connection('sqlsrv')->selectOne("SELECT CAST(SCOPE_IDENTITY() AS INT) AS id");
    $newId = (int)$r->id;
    // usar $newId para FKs en INSERTs siguientes
}
```

Para detectar si una columna es IDENTITY: `SELECT COLUMNPROPERTY(OBJECT_ID('schema.tabla'), 'col', 'IsIdentity')`.

Si el código se refactorea de "pre-reservar ids" a IDENTITY: revisar TODOS los lugares donde se usaba el id pre-reservado y atrasarlos al post-INSERT (en `LasetImportFaseC` movimos la resolución de `articulosAutoCreate[].marca_id` de la fase de planificación a `executePlan` post-INSERT de marcas).

## dblib + batches multi-statement (results pending)

`DB::unprepared` con SQL que contiene `DECLARE` / `IF` / `PRINT` / `CURSOR` / `SELECT INTO` produce `Attempt to initiate a new Adaptive Server operation with results pending`. dblib no consume el rowset implícito y rompe el batch siguiente.

Patrón: orquestar desde PHP — un statement por llamada (`DB::statement`/`DB::insert`/`DB::update`/`DB::select`), branching y verifies en PHP. Los archivos `.sql` quedan como referencia histórica; el ejecutor real es el service.

Ver también [[memoria#Reglas operativas Laset (afianzadas)]].

## Status terminal nuevo en staging — tocar 4 capas

Cuando agregás un nuevo `match_status` terminal (no requiere acción del usuario, como `IGNORED`, `STOCK_ONLY_SUPERSEDED`) a `laset_import_staging`, hay que actualizar **4 capas** o queda inconsistente:

1. **`SyncLasetList.php`** (`view=pending`): agregar el nuevo status al `NOT IN (...)` del WHERE.
2. **`SyncLasetSummary.php`** (contador `pending`): excluir el status del incremento.
3. **`syncLaset.vue`** (checkbox + `selectableIds`): no permitir tildar filas terminales.
4. **`syncLaset.vue`** (map de colores `counters`/`statusColor`): agregar entry o el tag sale sin color.

Caso: 2 filas de batch 6 quedaron eternamente en "Falta sincronizar" porque eran `STOCK_ONLY_SUPERSEDED` y el filtro no las reconocía. Si solo arreglás el filtro y dejás los counters, el badge sigue contando mal.

Status mapping para staging:
- **synced**: solo `IMPORTED`.
- **terminal-not-synced**: `IGNORED`, `STOCK_ONLY_SUPERSEDED`.
- **pending**: `MATCHED`, `UNMATCHED`, `PARTIAL`, `CONFLICT`, `NEW`, `STOCK_ONLY` (espera fix-stock-only).

## Patrón service-first para botones de Sync Laset

Cada feature de mantenimiento Laset que se quiere disparar desde la UI sigue el patrón:

1. **Service** (`app/Services/Laset/*.php`) — preview/execute, lógica completa, idempotente.
2. **Command CLI** (`Laset*Command.php`) — wrapper delgado del service.
3. **Controller invokable** (`Laset*Run.php`) — body `{dry_run}`, delega al service.
4. **Ruta** (`POST /v1/laset/<accion>`).
5. **api.js wrapper** (`plugins/api.js` namespace `laset`).
6. **UI** (botón + modal preview→confirmar en `syncLaset.vue`).

Implementaciones actuales: `RelinkFacturasService` y `FixMarcasComp11Service`. Ver [[feature-sync-laset-botones]].

## Wipe comp=11 — borrar hijos→padres + barrer huérfanos (2026-05-31)

Al borrar tajadas jerárquicas comp=11 cuyos scopes hacen JOIN al padre, **borrar SIEMPRE hijos→padres**. Borrar el padre primero deja al hijo huérfano (el JOIN del scope no matchea) y el verify post (mismo scope) lo cuenta 0 → **pasa ciego**. Bug en `WipeTransactionalService` (iteraba padre→hijo) que acumulaba ~42k huérfanos en cada wipe+reimport → Fase D no descontaba stock de ventas. Fix: `array_reverse(DELETE_KEYS)` + barrido de huérfanos.

- **Una herramienta basada en scope con JOIN al padre nunca ve/limpia huérfanos.** Agregar barrido separado: LÍNEAS por `articulo.companyCode=11`+sin padre; CABECERAS de remito por MAESTRO comp=11 (`clientes.CODEMP=11` vía ccodcli / `FP_Proveedores.companyCode=11` vía ccodpro), NO por sus líneas (respeta orden FK). Pre-filtro `(companyCode=11 OR NULL)` evita escanear 404k filas y el timeout dblib. Guard de aislamiento: baseline de cabeceras por empresa antes/después, THROW+rollback si cambia.
- **albprot/albclit con companyCode NULL masivo** (~11.875 albprot): scopear remitos comp=11 por JOIN al padre (`albprot.nnumped`→`pedprot.nNumPed`, único global; NO `nnumalb`) o al maestro, nunca por su companyCode propio.

## Frontend — selección "todo" no debe recortarse a la página visible (2026-05-31)

En `syncLaset.vue` el computed `selectableIds` intersectaba `selectedRowKeys` contra `this.rows` (las 50 filas visibles del `a-table`) → "Importar todo" previsualizaba/importaba solo ~50 (síntoma "se van a importar 2098"). La selección cross-página vive en `selectedRowKeys`, no en `this.rows`. Fix: confiar en `selectedRowKeys` (ya restringido a no-terminales por checkboxes + backend), descartar solo terminales visibles. "Importar todo" fuerza `batchId='all'` para no importar 1 batch y dejar el resto (→ duplicación si después se corre Fase C manual). Preview y create deben usar el mismo set completo.


## Import Laset — modelo final y bugs de reconciliación (2026-06-02)

Sesión depurando casos reales del import comp=11. Modelo final en [[feature-laset-import#Modelo de import — actualizado 2026-06-02]]. Principio del usuario: **"siempre lo que importa es la planilla más reciente"**.

- **Reimportar planilla REEMPLAZA el staging completo** (borra batches/filas previos, inserta el snapshot nuevo). Se quitó el dedup por `row_hash` que colapsaba renglones idénticos legítimos (un SKU listado 2 veces con misma cantidad → perdía unidades). Cada batch = snapshot completo.
- **Dedup cross-batch en Fase C = "batch más completo gana"** por (pedclit, sku, OC), conservando todas las filas del grupo. `source_row_number` NO es estable entre batches (no sirve de clave).
- **Stock: única fuente de verdad = Fase D.** `fix-stock-only` con `--skip-stock` (sólo suma a pedprol). Sin esto: doble conteo (fix-stock-only escribía stock + Fase D lo re-derivaba). Ganador stock-only por (vpi, sku, depósito), no por factura.
- **Canonicalización de factura (Fase C)**: si un (prov, vendor_pi) tiene 1 sola factura no vacía, las vacías la adoptan → no parte la compra en 2 OCs cuando la factura llega en un batch posterior.
- **CSUPROF_TEMP = vendor_pi completo** (cExped varchar(20) trunca). Fecha de compras stock-only = invoice_date.
- **Flujo operativo:** Reimportar planilla → Borrar todo → Importar todo. Nunca incremental sin Borrar todo.
- **Gotcha verificación:** el guard de auto-mode bloquea correr Fase C/D desde sesión de investigación → verificar con simulaciones read-only en tinker.
## 2026-05-30 — albclit recibe columna companyCode

`albclit` no tenía `companyCode`. Fix ejecutado:
1. `ALTER TABLE NewBytes_DBF.dbo.albclit ADD companyCode INT NULL`
2. `UPDATE albclit SET companyCode = pedclit.companyCode FROM albclit JOIN pedclit ON ...` (solo los que tienen pedclit padre)
3. 164.506 registros legacy sin pedclit → asignados cc=4 (NB legacy, 2010-2025)
4. `MakeSaleRepository::createHeader()` escribe `companyCode` en cada nuevo remito

**A partir de esta sesión**, `albclit.companyCode` es confiable como filtro de company. Para registros muy legacy, validar también via JOIN con `pedclit`.

---

## Esquema ERP — mapa de relaciones (2026-05-30)

Documentación completa de relaciones entre tablas, PKs, FKs y reglas de integridad en la bóveda:

- [[relacion-tablas-ped-alb]] — ventas: pedclit/pedclil ↔ albclit/albclil, PK compuesta `(cnumped, cnumsuc)`, join por `ID_NROREMCLI_ENC`
- [[relacion-tablas-pedprot-pedprol-pedproi]] — compras OC: pedprot/pedprol/pedproi, PK global `nNumPed`
- [[relacion-tablas-albprot-albprol]] — remitos de compra: albprot/albprol, join por `nnumalb`
- [[relacion-tablas-articulo-stocks]] — artículos y stocks: `ID_Articulo` canónico (sobre `cref`), `(ID_ARTICULO, ID_ALMACEN)` como PK lógica de stocks
- [[relacion-tablas-stocks-almacen]] — depósitos: FP_Almacen, depósitos compartidos SAF/NBE solo entre NB (cc=4) y NBElectric (cc=9)
- [[relacion-companycode]] — mapa completo de `companyCode` por tabla, regla SAF/NBE, integridad de stocks

### Reglas clave del esquema

- **PK ventas:** `(cnumped, cnumsuc)` — nunca usar solo `cnumped`
- **PK compras:** `nNumPed` — único global
- **Join albclit↔albclil:** por `ID_NROREMCLI_ENC`, NO por `CNUMALB`
- **Join artículo:** siempre por `ID_Articulo`, no por `cref`
- **Depósito compartido:** SAF y NBE son de NB (cc=4) + NBElectric (cc=9) ÚNICAMENTE
- **pedprol.stockWarehouseId NULL:** 99.5% de OC legacy no tienen este campo → fallback SAF (ID_ALMACEN=2)
- **13.462 pedclil con ID_Articulo ≠ cref:** son líneas Laset donde `cref` apunta al gemelo cc=4 y `ID_Articulo` al cc=11. Siempre usar `ID_Articulo`.

---

## Filtro Pedidos Olvidados (2026-06-16)

Filtro oculto en la lista de órdenes: pendientes o remitidas (no facturadas) con >2 meses hasta 3 años de antigüedad. El front setea el `between` a esa ventana (nunca lo deja vacío); el backend con `forgottenOrders=1` agrega solo la condición de estado. **Sin tope de fecha la query expira** (escaneaba ~59.6k órdenes) → se acota a 3 años. Detalle en [[feature-pedidos-olvidados]]. Rama `feature/pedidos-olvidados`.

---

## Descarga xlsx de listados — pedidos y clientes (2026-06-18)

Endpoint nuevo `GET /v1/orders/download` que exporta el listado de pedidos filtrado a xlsx, **reutilizando `OrderListRepository::getOrders($filters, ['offset'=>0,'limit'=>ORDER_DOWNLOAD_MAX_ROWS])`** (público, sin paginar) → mismas filas/filtros/totales que el listado. Replica el patrón de `clients/download` (clientes ya tenía descarga). Front: botón solo-icono en `Filters/Orders.vue` y `Filters/Clients.vue`. Rama `descargarListadoXlsx`, a development y gamma en ambos repos. Detalle en [[feature-descarga-listado-xlsx]].

## Cuenta corriente histórica Laset

Import de cuenta corriente USD de clientes exclusivos Laset (CODEMP=11) a `NEW_BYTES.dbo.MC_CCORRIENTES_MOVIMIENTOS` (`ID_PROCEDENCIA=99`). Botón en `/syncLaset`, parser Python `scripts/laset_ccte_to_json.py`, service `LasetCtaCteImportService`. Detalle vivo en [[feature-laset-cuenta-corriente]].

- **Reemplazo por cuenta**: `execute()` borra/recarga solo las cuentas (`ID_CLIENTE`) del archivo → planillas parciales OK; las ausentes intactas; no toca manuales (`proc IS NULL`).
- **NB Inc = cliente distinto**: una hoja `-NBinc` nunca matchea el cliente normal y viceversa. Si no, la hoja quedaba ambigua → omitida → con dato viejo (EMAP daba 63.160,50 vs 14.761,50 real). Una hoja ambigua/omitida deja la cuenta stale → revisar advertencias del preview.
- **Signo**: `CC_IMPORTEUSD` siempre +, el signo lo da `TR_CODIGO`; el ERP invierte (`tr24` negativo, `tr42` positivo). "ajuste faltante"→tr42, "ajuste sobrante"→tr24.
- **Parser**: openpyxl 3.1.x crashea con autoFilter `customFilter` inválido → parche en `CustomFilterValueDescriptor`. Bloque USD en columnas variables (anclar header "Debe").
- **Exclusiones**: intercompañía, tesorería USDT (incl. hoja suelta `USDT`), `MG Interno`. Ambiguas reales (`I y T`) se omiten y avisan.

## FLETE nunca en la compra

El FLETE (art `121944`) se factura a la VENTA (pedclil/albclil) pero NUNCA va en la compra (pedprol/albprol). `LasetImportFaseCCommand::INTERNAL_NO_PURCHASE_ARTICULOS=[121944]`. Ortogonal a INTERNAL_NO_STOCK. Ver [[contexto#FLETE nunca en la compra]].

## Conexión DB dev (remota)

`.env` no versionado. A 2026-06-19 la DB dev es remota: `db-nb-dev.blu.net.ar:41433`. Error `Adaptive Server unavailable (10.10.10.47)` = host viejo en `.env`, no bug → cambiar host/puerto + `config:clear`. Ver [[contexto#Conexión a la base de datos dev]].

## Compra completa para stock-only + Reservas

Regla (2026-06-23): la compra Laset se carga COMPLETA aunque el ítem no se haya vendido. Las stock-only categoría C (SKU/proveedor sin catálogo comp=11) ya NO se saltean: `laset:stockonly-autocreate-catalog` auto-crea artículo/marca/proveedor (como Fase C) y fix-stock-only las materializa. Las que traen cliente real (no el sentinel `STOCK`) se cargan como RESERVA (`laset:stockonly-reservas`): `pedclit cestado='P'` + `pedclil` + asignación, sin remito. RMA → IGNORED. Fase D excluye `cestado='P'` del remito; `reconcile()` usa `albclil` (entregado). Wireado en Fase C → durable en Borrar todo/Importar todo. Detalle: [[feature-laset-stockonly-completa]].

## País de la OC y IVA 0 (comp=11)

- **IVA 0**: artículos Laset comp=11 SIEMPRE IVA 0 (`ctipoiva/ctipoivac=NULL`). El auto-create copiaba el del gemelo NB (10,5/21%) → corregido en los 3 sitios de alta (Fase C, stockonly-autocreate-catalog, fix-cross-company) + 209 datos. Ver [[contexto#Laset (comp=11) — siempre IVA 0]].
- **País OC**: `pedprot.countryId` desde la **columna H** de la planilla (`pais_proveedor`) vía `LasetCountryResolver` (alias de USA + fallback USA), no más hardcode 5. 2 sitios crean pedprot (Fase C + fix-stock-only) → ambos wireados. 191/523 OCs corregidas. Ver [[contexto#País de la OC (countryId) — columna H de la planilla]].


## Remito de compra faltante (albprol) — gating por OC

Fase D gatea el remito de compra por OC (`pedprot` sin `albprot`); líneas stock-only adjuntadas a una OC ya remitada quedan sin albprol → stock sin ingreso (compra incompleta). `laset:fix-albprol-faltante` cierra el gap a nivel línea (idempotente, comp=11, dblib-safe), wireado en `run-import-job` tras Fase D. El gap aparece en imports incrementales, no en wipe+reimport limpio. Backfill dev: 12 albprol. Ver [[contexto#Remito de compra (albprol) — gating por OC en Fase D]].

## ID fiscal de clientes (cdnicif)

Backfill del `cdnicif` de los 47 clientes comp=11 creados por el import (sin ID fiscal) desde la pestaña Database Clientes de `docs/laser.xlsx` (col C), formato compacto. 36 completados; gemelos NB Inc comparten el CUIT del cliente real. Ver [[contexto#ID fiscal de clientes Laset (cdnicif)]].


## Cuenta corriente de proveedores Laset (comp=11)

Import a `MS_MOV_CTACTE_PROVEEDORES` (NEW_BYTES). **Clave = CCODPRO**, no Id_Proveedor (Asus 16679→002605). Magnitud+TR (38 deuda / 40 pago / 30 NC / 32 débito), rollback por `USU=Laset`, MAX+1 fila a fila. Saldo = "A favor/Deuda" neto de "NC Disponible" solo si hay deuda. 66 prov / 5.573 movs / 66 reconcilian (dev 2026-06-24). Pendiente EUR (17) + 10 no-comp11. Ver [[feature-laset-cuenta-corriente-proveedores]].

## (2026-06-30) Stock por almacén comp=11 — depósito por línea
Bug del importador Laset: `pedclil` heredaba el `ID_ALMACEN` del encabezado del pedido en vez del `deposito` por línea → pedidos multi-depósito → stock negativo por almacén (total por artículo OK). Fix en `LasetImportFaseCCommand` (depósito en la clave de consolidación de pedclil) + comando retroactivo `laset:fix-stock-almacen-comp11` (re-apunta ventas pedclil+albclil por DELTA exacto + balancea negativos con transferencias inter-depósito; invariante de total por artículo; idempotente; wireado a `laset:run-import-job` paso 3.6). Dev: 14→0 negativos. **Gotcha aparte**: total comp=11 = planilla (comprado−facturado); diferencia vs archivo físico = compra no registrada en la planilla, no es bug, no detectable desde la DB. Ver [[feature-laset-stock-almacen]].

## (2026-06-30) Cta cte proveedores — alta automática + Transcargo fuera
Las hojas de la planilla de cta cte de proveedores que no matchean un proveedor comp=11 se dan de alta solas en `FP_Proveedores` (CCODPRO secuencial; ID_PROVEEDOR es IDENTITY). Paridad NB Inc (Seaside NB Inc ≠ Seaside). Saldo = "A favor/Deuda" bruto (no netear NC). 110 proveedores comp=11, todos reconcilian. **Transcargo NO va en comp=11** (decisión del usuario); Egre/Egresos (logs), Pendiente Euros (contactos), LST Global (=NB Inc) tampoco son cuentas. Ver [[feature-laset-cuenta-corriente-proveedores]].
