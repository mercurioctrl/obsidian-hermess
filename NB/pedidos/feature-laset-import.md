# Feature: Laset Import Framework

> Importar la operación FOB de **LASET** (CODEMP=11, empresa importadora uruguaya del grupo) desde la planilla histórica `Raw ventas FOB` hacia las tablas existentes del ERP, **sin tocar el resto del ERP**. Solo aplica a `companyCode = 11`.

Branch: `lasetImportFramework` (ambos repos).
Estado al **2026-05-15**: Fase B + Fase C ejecutadas. **Fase D PASADA 1 ejecutada y verificada en dev** (493 albprot + 1454 albprol + 111 pedproi + 379 albclit + 2155 albclil + 2155 registro_stock; stock 672/672 = delta; identidad contable 684/721, residuo = órdenes diferidas). Defecto de Fase C corregido (SQL 002 aplicado, 8+8 remapeadas). **Pasada 2** (15+15 órdenes con 39 SKUs) espera Fase A catálogo. Snapshot/restore unificado disponible y probado (ver §13 y [[feature-laset-snapshot-restore]]).

---

## 1. Contexto

LASET = Laset Sociedad Anónima (Uruguay, RUT 217502910019, dirección Pradines Clemente 1795), CODEMP=11 en [[contexto#Empresas activas (FP_Empresas)|FP_Empresas]]. Es importadora — triangula via **New Bytes Inc** (USA) hacia clientes LATAM (Chile 986, Paraguay 974, Colombia 240, Bolivia 197, Ecuador, Panamá, USA, Argentina). Única empresa con `defaultIncoterms=14`.

La planilla `docs/laser.xlsx` pestaña **`Raw ventas FOB`**: 3008 × 67. Cada fila es un trade completo (compra a vendor + venta a cliente final + costos + rebates + logística + re-facturación NB Inc).

## 2. Decisiones clave de negocio

### Planilla es la fuente de verdad

La data actual ERP para `companyCode=11` (~386 pedprot + ~363 pedclit pre-Fase B) era de una **carga fallida previa**: tenía duplicaciones, faltantes, cantidades incorrectas + referencias a clientes/proveedores de NB (comp=4) por error.

**Regla**: cuando staging y ERP comp=11 difieren, **planilla wins**.

### Regla de aislamiento

Todo lo que NO es `companyCode = 11` queda **intocable**: otras companies (NB=4, NBE=9, LO=12, OXXEN=2, MUGELLO=8, etc.) operan en producción y se cargan desde otros sistemas. Cualquier `DELETE`/`UPDATE` durante este feature debe llevar SIEMPRE `WHERE … companyCode = 11`. Verificado con snapshot pre/post en Fase B.

### Regla "nunca compartido entre companies"

**Proveedores y clientes pertenecen a EXACTAMENTE una company**. Confirmado por usuario:
- `FP_Proveedores.CCODPRO` es único globalmente.
- `clientes.ccodcli` puede tener duplicados pero solo intra-company (0 ccodcli compartido entre comp=11 y otras).
- Si pedprot/pedclit comp=11 referencia un ccodpro/ccodcli de otra company, es **data sucia** (caso típico: ex-carga-fallida).

Aplicación: para Fase C, todo match staging → maestros usa `WHERE companyCode = 11` estricto.

### Manejo de SKUs huérfanos

100 SKUs únicos en planilla no mapean a `articulo.ID_PRODUCTO`. **Deben darse de alta** en `articulo` por equipo de catálogo (Fase A). Listado: `docs/laset_orphan_skus.csv` y `.md`.

## 3. Modelo canónico ERP

El framework ya existe en el ERP, solo bajo otros nombres. Ver [[arquitectura#Modelo canónico ERP|mapeo canónico]]:

- **Compras** = `pedprot` + `pedprol` + `pedproi` (incl. cargos extra)
- **Ventas** = `pedclit` + `pedclil`
- **Stock** = `stocks` (filtrado por almacén — no tiene `companyCode`)
- **Linkeo compra↔venta** = [[feature-asignacion-oc|`pedclil_oc_asignacion`]] (ya habilitado `ASSIGNMENT_COMPANIES=4,11`)
- **CFE Uy** = `FP_FactWebCliEncabezado_Uy` + `FP_FactWebCliDetalle_Uy`
- **Maestros**: `FP_Proveedores` (moderna, no `proveedo`), `clientes`, `articulo`. Ver [[memoria#FP_* vs legacy]].

## 4. Bridge SKU planilla ↔ ERP

`articulo.ID_PRODUCTO` (varchar(50)) = SKU del fabricante. `articulo.ID_ARTICULO` (int) = PK interna que linkea con `pedprol.ID_Articulo`, `pedclil.ID_Articulo`, `stocks.ID_ARTICULO`.

Cobertura: 620/739 (84%) directo + 14 vía normalizaciones (alias `auto:trim`, `auto:nospace`, `auto:split-slash`, `auto:last-word`) + 5 services explícitos. Quedan 100 SKUs huérfanos pendientes de alta.

Tabla **`laset_sku_alias`** persiste alias auto-detectados, services, y decisiones manuales/ignored.

## 5. Arquitectura

```
Excel docs/laser.xlsx (Raw ventas FOB)
    ↓ scripts/laset_xlsx_to_json.py (Python + openpyxl en host)
JSON
    ↓ php artisan laset:import-staging
laset_import_batches + laset_import_staging   ← 3007 filas raw NVARCHAR
    ↓ aggregate matching (script PHP, próximamente artisan)
staging.match_status / match_score / match_notes poblados
    ↓
    ├─ MATCHED (2461) → Fase C: INSERT a ERP
    ├─ UNMATCHED NO_BRIDGE (147) → bloqueado, Fase A: alta huérfanos
    └─ IGNORED (399) → no migrar
```

## 6. Schema (en `NewBytes_DBF.dbo`)

**Tablas nuevas (4):**

- `laset_import_batches` — 9 cols. Cabecera por carga.
- `laset_import_staging` — 79 cols (67 raw NVARCHAR + 4 sistema + 8 matching).
- `laset_sku_alias` — alias SKU↔ID_Articulo + services + ignored.
- `laset_match_decisions_tmp` — temporal, se dropea al final del aggregate match.

**Backups Fase B (10):** `laset_phase_b_backup_pedprot/pedprol/pedproi/pedclit/pedclil/albprot/albprol/albclit/albclil/pedclil_oc_asignacion`. Mantener hasta validar Fase C.

**Vistas (7):** `vw_laset_sku_bridge`, `vw_laset_planilla_compras`, `vw_laset_planilla_ventas`, `vw_laset_erp_compras`, `vw_laset_erp_ventas`, `vw_laset_erp_stock`, `vw_laset_reconciliation`.

**Scripts SQL** en `database/sql/`:

- `2026_05_14_001_create_laset_import_staging.sql` (+ drop)
- `2026_05_14_002_create_laset_reconciliation_views.sql` (+ drop)
- `2026_05_14_003_create_laset_sku_alias.sql` (+ drop, también refactorea bridge view)
- `2026_05_14_004_phase_b_delete_comp11.sql` (+ esqueleto rollback) — **Fase B aplicada 2026-05-14 PM**.

## 7. Distribución final del staging (post aggregate-match)

| match_status | match_score | filas | Significado |
|---|---:|---:|---|
| MATCHED | 100 | 536 | planilla = ERP exacto |
| MATCHED | 90 | 1860 | planilla wins (ERP discrepa) |
| MATCHED | 80 | 65 | planilla wins (delta puro) |
| UNMATCHED | 0 | 147 | NO_BRIDGE — bloqueado, requiere alta de 100 SKUs huérfanos |
| IGNORED | 0 | 399 | basura + services |

**Total importable a ERP: 2461 filas (82%)**.

## 8. Plan de migración (3 fases)

```
Fase A — Alta de huérfanos en articulo (PENDIENTE — equipo catálogo, fuera de scope)
    INSERT INTO articulo (ID_PRODUCTO, …) para los 100 SKUs
    de docs/laset_orphan_skus.csv.
    Después re-correr aggregate match — vw_laset_sku_bridge los toma vía
    articulo automáticamente, baja UNMATCHED a 0.

Fase B — Limpieza ERP comp=11 ✓ EJECUTADA 2026-05-14 PM
    Decisión: DELETE total comp=11 (no row-level matching), porque el
    matching staging↔ERP es agregado por SKU. "Planilla wins" — asumimos
    que las 2461 filas MATCHED cubren toda la realidad y nukeamos comp=11.

    7822 filas borradas (todas comp=11):
      pedprot=386, pedprol=1349, pedproi=31
      pedclit=363, pedclil=1847
      albprot=526, albprol=1205, albclit=331, albclil=1746
      pedclil_oc_asignacion=38

    Backups in-DB: NewBytes_DBF.dbo.laset_phase_b_backup_* (10 tablas).
    Otras companies intactas (snapshot pre/post por company verificado).
    Script: database/sql/2026_05_14_004_phase_b_delete_comp11.sql.

    Gotchas críticos atrapados en revisión SQL pre-ejecución:
      - pedclit.cnumped NO único globalmente (5 colisiones comp=11↔comp=4).
        PK efectiva (cnumped, cnumsuc) — uq_pedclit. Refactorizado a JOINs
        compuestos. Habría borrado 5 ventas legítimas de NB sin esto.
        Ver [[memoria#PK compuesta pedclit]].
      - albprot.companyCode tiene 11875 filas NULL. Conteo inicial 370 era
        falso (subselect cruzado). Conteo real: 526.
      - Pre-check assertions con THROW antes de cada DELETE (pedido del
        usuario). Loader PHP propaga excepción y aborta antes de tocar nada.
        Ver [[memoria#Pre-check assertions destructivos]].

Fase C — INSERT planilla → ERP (PENDIENTE — discovery completa)
    Por cada laset_import_staging.match_status='MATCHED' (2461 filas):
      INSERT a pedprot/pedprol/pedproi (compra)
      INSERT a pedclit/pedclil (venta)
      INSERT a pedclil_oc_asignacion (linkeo)
    UPDATE staging.matched_* + match_status='IMPORTED'

    Schema mapeado: pedprot 34 cols (id_pedprod IDENTITY, nNumPed manual desde
    MAX+1=13219), pedclit 78 cols (id IDENTITY, cnumped manual desde
    MAX+1=10459501, ccodcli NOT NULL), pedprol 25, pedclil 42, pedproi 16
    (lcalcuauto NOT NULL sin default), pedclil_oc_asignacion 19.

    Agrupación: 2461 líneas → 417 pedprot únicas (por proveedor+vendor_pi+
    vendor_invoice) + 396 pedclit únicas (por razon_social+customer_pi+
    customer_invoice) ≈ 4078 INSERTs.

    Mapping a maestros (con WHERE companyCode=11 estricto):
      proveedores via FP_Proveedores.cnompro:  25/28 OK,  3 a auto-crear
      clientes via clientes.cnomcli:           50/56 OK,  6 a auto-crear
      SKUs via articulo.ID_PRODUCTO:          806/820 OK, 14 bloqueados (Fase A)

    Decisiones para implementación (con usuario):
      - Forma: artisan command laset:import-fase-c con --dry-run/--limit/--chunk
      - FKs faltantes: auto-crear FP_Proveedores/clientes mínimos comp=11
      - Idempotencia: skip filas con match_status='IMPORTED'
```

Stock queda correcto como consecuencia de B+C (no se INSERT manualmente).

## 9. Comandos

### Carga planilla → staging

```bash
python3 api-rest-pedidos-laravel/app/scripts/laset_xlsx_to_json.py \
    docs/laser.xlsx "Raw ventas FOB" /tmp/laset.json
docker cp /tmp/laset.json api-rest-pedidos-apirest-laravel:/tmp/laset.json
docker exec api-rest-pedidos-apirest-laravel \
    php artisan laset:import-staging /tmp/laset.json --imported-by=hermess --force
```

### Aggregate matching (planilla wins)

```bash
docker exec api-rest-pedidos-apirest-laravel php artisan laset:aggregate-match --dry-run
docker exec api-rest-pedidos-apirest-laravel php artisan laset:aggregate-match
```

Aplica regla planilla=verdad para comp=11. Decisiones SKU-level:
- bridge OK + ERP=planilla → MATCHED 100
- bridge OK + ERP discrepa → MATCHED 90 (planilla wins)
- BRIDGE_SIN_ERP_DATA → MATCHED 80 (delta puro)
- SERVICE/IGNORED alias → IGNORED
- NO_BRIDGE → UNMATCHED (Fase A pendiente)
- Basura (SELECTOR / year != 2025-2026 / sin SKU) → IGNORED

### Fase C: INSERT staging → ERP

```bash
docker exec api-rest-pedidos-apirest-laravel php artisan laset:import-fase-c --dry-run
docker exec api-rest-pedidos-apirest-laravel php artisan laset:import-fase-c --limit=10
docker exec api-rest-pedidos-apirest-laravel php artisan laset:import-fase-c
```

Idempotente. Resuelve maestros con `WHERE companyCode=11` estricto. Auto-crea `FP_Proveedores` y `clientes` mínimos para los faltantes. Mapping deposito→almacén ya coordinado con FP_Almacen comp=11.

### Reset stocks comp=11 (doble filtro)

```bash
docker exec api-rest-pedidos-apirest-laravel php /var/www/app/scripts/laset_reset_stocks.php --dry-run
docker exec api-rest-pedidos-apirest-laravel php /var/www/app/scripts/laset_reset_stocks.php
```

Doble filtro: `articulo.companyCode=11 AND stocks.cCodAlm IN (almacenes Laset)`. Backup automático en `laset_phase_b_backup_stocks`. Items NB en almacén Laset PRESERVADOS.

### Pre-flight / post-flight para producción

```bash
docker exec api-rest-pedidos-apirest-laravel php /var/www/app/scripts/laset_pre_flight_prod.php
docker exec api-rest-pedidos-apirest-laravel php /var/www/app/scripts/laset_post_flight_validation.php
```

### Inspección manual

```sql
SELECT bridge_status, COUNT(*) FROM vw_laset_reconciliation GROUP BY bridge_status
SELECT match_status, match_score, COUNT(*) FROM laset_import_staging GROUP BY match_status, match_score
SELECT companyCode, COUNT(*) FROM pedclit GROUP BY companyCode
```

## 10. Gotchas

### Negocio

- **Planilla wins** sobre ERP comp=11 para todo PARTIAL.
- **companyCode != 11** jamás se modifica.
- **Proveedores/clientes nunca compartidos entre companies** — usar `WHERE companyCode=11` estricto.
- **`pedproi` NO es solo impuestos**: guarda cargos extra del pedido de compra (`cdescrip='camion'`), linkea a `pedprot.nNumPed`, NO a `pedclit`.
- **`rebates` + `NewTable`** son huérfanas (creadas 2025-11-01) — restos de intento abandonado. NO usar.
- **CFE Uy ya implementado**: `FP_FactWebCliEncabezado_Uy` (179) + `FP_FactWebCliDetalle_Uy` (1411). NO recrearlo.
- **`proveedo` legacy con `cnompro` vacío** — usar `FP_Proveedores` moderna. Ver [[memoria#FP_* vs legacy]].

### Técnicos (ver [[memoria]] para detalle)

- **PhpSpreadsheet inviable** con `docs/laser.xlsx` (>15 min) → preprocesar con Python + openpyxl en host.
- **dblib segfault** con cientos de UPDATE prepared en loop → tabla tmp + UPDATE FROM JOIN single-statement.
- **dblib no auto-castea DECIMAL** → usar INT en columnas tmp para scores/conteos.
- **SQL Server 2012** — sin `CREATE OR ALTER VIEW`, sin `DROP VIEW IF EXISTS`. THROW soportado.
- **`pedprot.sitio=0` vs `pedprol.sitio=NULL`** → JOINear solo por `nNumPed`.
- **`pedclit.cnumped` NO único globalmente** — PK efectiva `(cnumped, cnumsuc)`. Usar JOIN compuesto en queries.
- **`albprot.companyCode` tiene 11875 NULLs** — usar `WHERE companyCode=11` directo, NO subselects cruzados.
- **macOS case-insensitive**: branch `Development` (mayúscula). `git branch -D development` puede romper `Development`. Recovery: `git reset --hard origin/Development`.

## 11. Próximos pasos

- [ ] Fase A: equipo catálogo da de alta los 100 SKUs huérfanos en `articulo`.
- [x] ~~Portar el aggregate-match a artisan command~~ → **`laset:aggregate-match` listo (2026-05-15)**.
- [x] ~~Diseñar y aplicar Fase B (DELETE ERP comp=11)~~ → **Aplicada en dev 2026-05-14, 7822 filas**.
- [x] ~~Diseñar y aplicar Fase C (INSERT staging MATCHED → ERP)~~ → **Aplicada en dev 2026-05-14, 8224 INSERTs, identidad SKU global 100%**.
- [x] ~~Reset stocks comp=11~~ → **`laset_reset_stocks.php` versionado y aplicado en dev**.
- [x] ~~Runbook producción + pre/post flight scripts~~ → **`docs/laset-import-runbook-prod.md` + scripts auxiliares listos (2026-05-15)**.
- [ ] **Replicar a producción**: coordinar ventana, ejecutar runbook. Ver [[changelog#2026-05-15]].
- [ ] Decidir modelo de rebates (`Sell out rebate`, `Reportado AMD/NVIDIA`, `Qty a la que aplica`) — la tabla `rebates` existente está huérfana, hay que modelar nuevo.

---

## 12. Sesión 2026-05-15 (cont.) — Fase D + fix defecto Fase C

### Qué se hizo

Fase C resultó incompleta: creó solo las **órdenes** (`pedprot`/`pedprol` +
`pedclit`/`pedclil` + `pedclil_oc_asignacion`), **sin remitos, sin `pedproi`,
sin movimiento de stock**. Se implementó **Fase D** como paso standalone sobre
las órdenes comp=11 ya existentes:

- Comando `laset:import-fase-d` (`app/Console/Commands/LasetImportFaseDCommand.php`),
  `--dry-run/--limit/--chunk`, idempotente (saltea órdenes con remito).
- Paso 0 obligatorio: SQL `2026_05_15_001_reset_stock_comp11.sql` — resetea
  stock comp=11 en almacén Laset a 0 con **doble filtro**
  (`articulo.companyCode=11 AND ID_ALMACEN in 9,10,11,17,18`); items NB en
  almacén compartido **intactos**; backup `laset_phase_b_backup_stocks`.
- Crea `albprot`+`albprol` (link `nnumped`=pedprot.nNumPed), `albclit`+`albclil`
  (link `(cnumped,cnumsuc)`, `ccodalm` del pedclit — **NO** el `'SAF'`
  hardcodeado de MakeSale), `pedproi cdescrip='camion'` (de staging.camion,
  111 OCs), stock compra(+)/venta(−) vía tabla delta + un solo UPDATE FROM
  JOIN (dblib-safe) + `registro_stock` en `NB_WEB.dbo`.
- **Fechas de documento respetadas**: `dfecalb`/`dfecent` = `pedprot.dFecPed` /
  `pedclit.dfecped` (que Fase C cargó de la planilla), nunca `GETDATE()`.
- `albproi` NO existe como tabla → fuera de scope.

Dry-run validado: albprot=506, albprol=2439, albclit=392, albclil=2439,
pedproi=111, registro_stock=2439, stock neto=0 (entradas +686 = salidas −686,
la identidad contable cierra).

### El defecto de Fase C que destrabó el pre-check

El pre-check de aislamiento de Fase D (THROW si algún `ID_Articulo` del delta
de stock no es `companyCode=11`) detectó que
`LasetImportFaseCCommand::resolveMasters` resolvía SKU→`ID_ARTICULO` con
`articulo.ID_PRODUCTO whereIn(...)` **sin filtrar companyCode**. Cuando un SKU
existía como artículo NB (comp=4), Fase C ligó la línea comp=11 al
`ID_ARTICULO` de NB → **56 `pedprol` + 56 `pedclil` apuntando a 44 artículos
NB**. Sin el guard, Fase D habría tocado stock NB. Ver
[[memoria#Resolución de maestros filtra companyCode]].

### Fix aplicado (2026-05-15)

1. `resolveMasters` ahora filtra `articulo.companyCode=11` (un SKU sin
   artículo comp=11 queda bloqueado, nunca se liga a otra company).
2. SQL `2026_05_15_002_fix_fasec_articulo_comp11.sql` **APLICADO**: remapeó
   **8 `pedprol` + 8 `pedclil`** (los 5 SKUs con artículo gemelo comp=11:
   122527→122264, 122528→122328, 122534→122262, 122580→122042,
   122545→121897), solo orden padre comp=11, backups `laset_fasec_fix_backup_*`
   (56+56), tabla `articulo` y otras companies intactas. Líneas contaminadas:
   56→48 por tabla. Gotcha de aplicación: el loader `GO`+`unprepared` falla
   en los UPDATE por "results pending" dblib tras los pre-check `SELECT @var`
   → los 2 UPDATE se aplican en conexión fresca.
3. Los **39 SKUs sin gemelo comp=11** → Fase A catálogo. Listados con impacto
   en `docs/laset_fasec_skus_sin_comp11.csv` (el más urgente:
   `100-100001973WOF`, 8 líneas). Nota lista para enviar a catálogo:
   [[nota-catalogo-laset]].

### Estado / próximo desbloqueo

Fase D **no se aplica** hasta: (1) catálogo da de alta los 39 SKUs como
`articulo` comp=11 (externo); (2) re-bind/re-correr Fase C para esas órdenes;
(3) `2026_05_15_001` reset stock; (4) `laset:import-fase-d --dry-run` debe dar
**0 artículos no-comp11** → recién ahí el run real.

## 13. Fase D pasada 1 ejecutada + fixes + snapshot/restore (2026-05-15)

### Pasada 1 ejecutada (dev) — modo `--skip-bloqueadas`

`laset:import-fase-d --skip-bloqueadas` difiere las **15 pedprot + 15 pedclit**
que tocan los 39 SKUs sin artículo comp=11 (decisión: 2 pasadas; solo 30 de
~900 órdenes bloqueadas) y migra el resto. Resultado verificado independiente:

- 493 albprot + 1454 albprol + 111 pedproi(camion) + 379 albclit + 2155 albclil
  + 2155 registro_stock (fecha de documento).
- Stock: **672/672 grupos `(artículo, almacén)` con `nstock == delta` exacto**.
- Idempotente (re-run = 0). NB / no-comp11 intacto.

### Tres fixes que costó descubrir (limit=5 → run completo)

1. **Consolidación de líneas de remito.** `albclil` PK = `(ID_Articulo,
   ID_NROREMCLI_ENC)` → 1 línea por artículo por remito (norma del ERP:
   `backup_albclil` 1746 filas, 0 dups; `backup_albprol` idem). `buildPlan`
   ahora agrega por `ID_Articulo` dentro del remito (suma `ncanent`; precio y
   almacén son idénticos dentro del grupo, verificado 0/143). Aplica a
   albprol + albclil + registro_stock.
2. **UPSERT de stock.** `stocks` es tabla por `(ID_ARTICULO, ID_ALMACEN)`;
   ~64% de combos comp=11 no tenían fila → el `UPDATE`-only perdía el
   movimiento. Ahora INSERT de fila mínima si falta (`id_auto` IDENTITY no se
   inserta; NOT NULL en 0; `ccodalm`/almacén desde `FP_Almacen`).
3. **Set de almacenes Laset.** El hardcode `(9,10,11,17,18)` era doblemente
   erróneo: 17/18 no existen como Laset; URU/ASI reales = **14/15**. Fuente de
   verdad única = **`FP_Almacen WHERE companyCode=11`**. Corregido en el reset
   SQL `2026_05_15_001` y en el comando. Ver [[memoria#Almacenes Laset reales]].

Guards agregados que pagaron: **ASSERT** con rollback si queda grupo de stock
sin aplicar, y **auto-auditoría** filas reales vs plan (rollback total si
difiere) — atraparon el PK de albclil y el almacén angosto sin corromper data.

### Identidad contable validada

`Σ compras − Σ ventas − stock = 0` por `(SKU, almacén)` comp=11. Fase D la
cumple **por construcción** (parte de stock reseteado a 0 y escribe
`nstock = compras − ventas`). Verificado: **684/721 grupos = 0**; los **37
≠ 0 están 100% explicados** por las 30 órdenes diferidas (cierran en pasada
2), **0 inexplicados**.

### Snapshot / restore unificado (reversibilidad total)

Todo el proceso es ahora reversible: `laset:snapshot <tag>` antes de cualquier
proceso/sesión, `laset:restore <tag>` deja la tajada comp=11 exactamente como
estaba. Probado end-to-end (daño simulado → restore → estado bit-idéntico).
Doc completa en [[feature-laset-snapshot-restore]].

## Ver también

- [[pedidos|Índice del proyecto]]
- [[arquitectura|Arquitectura]] — modelo canónico ERP, tablas FP_* maestras
- [[contexto|Contexto]] — regla cero ERP, empresas activas, regla planilla=verdad
- [[memoria|Memoria]] — gotchas dblib, PK compuesta pedclit, FP_Proveedores moderna
- [[feature-laset-snapshot-restore|Snapshot/Restore Laset]] — punto de restauración comp=11
- [[feature-asignacion-oc|Feature Asignación OC↔Venta]] — el linkeo que ya existe
- [[changelog#2026-05-14 (PM) — Laset Fase B ejecutada + discovery Fase C]] — sesión completa
- Doc canónico en repo: `docs/laset-import-framework.md`
- SQL DDL: `database/sql/2026_05_14_00{1,2,3,4}_*.sql`
- CSV huérfanos: `docs/laset_orphan_skus.csv`

