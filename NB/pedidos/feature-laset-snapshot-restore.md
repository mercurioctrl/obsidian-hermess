# Feature: Snapshot / Restore Laset (reversibilidad comp=11)

> Punto de restauración de **toda** la tajada `companyCode=11` que el proceso
> [[feature-laset-import|Laset Import Framework]] muta. Pensado para tocar
> producción con red: si algo sale mal, `laset:restore` deja todo como estaba.

Branch: `lasetImportFramework`. Construido y probado end-to-end 2026-05-15.

---

## Por qué existe

El proceso Laset (Fase B/C/D, fixes) hace INSERT/UPDATE/DELETE sobre tablas
del ERP. Aunque todo está filtrado a `companyCode=11`, es destructivo. El
usuario lo pidió explícito: **"cuando lo hagamos en producción, si pasa algo
malo, poder dejar todo como estaba antes"**. Los backups previos eran ad-hoc,
por paso, nombres inconsistentes. Esto los unifica en un punto de
restauración consistente y verificable.

## Qué muta el proceso (alcance comp=11)

Fuente única: `app/Support/LasetSnapshotRegistry.php` — 14 tablas:

- **Órdenes/remitos** (NewBytes_DBF): `pedprot`, `pedprol`, `pedproi`,
  `pedclit`, `pedclil`, `pedclil_oc_asignacion`, `albprot`, `albprol`,
  `albclit`, `albclil`.
- **Stock** (NewBytes_DBF): `stocks` — doble filtro
  `articulo.companyCode=11 AND ID_ALMACEN ∈ FP_Almacen(comp=11)`.
- **Maestros** (NewBytes_DBF): `FP_Proveedores`, `clientes` (comp=11).
- **Cross-DB** (NB_WEB): `registro_stock` — sin companyCode, identificable
  solo por marcador `fichero LIKE 'Laset Fase D%'`.

Si se agrega una tabla al proceso, **agregarla al registro**.

## Comandos

```bash
# ANTES de cualquier proceso/sesión (tag descriptivo)
php artisan laset:snapshot prod_pre_pasada2
php artisan laset:snapshot prod_pre_pasada2 --dry-run   # solo conteos
php artisan laset:snapshot prod_pre_pasada2 --drop       # liberar el punto

# Si algo sale mal: volver al punto exacto
php artisan laset:restore prod_pre_pasada2 --dry-run     # pre-check, no escribe
php artisan laset:restore prod_pre_pasada2 --force
```

- `snapshot`: `SELECT * INTO laset_snap_<tag>_<tabla>` por tajada (read-only
  sobre las reales) + fila en `laset_snapshot_manifest`. Snap tables en la DB
  de origen; manifiesto siempre en NewBytes_DBF.
- `restore`: 1 transacción → DELETE tajada actual (hijos→padres) + re-INSERT
  desde snap (padres→hijos) con `IDENTITY_INSERT` y columnas explícitas (sin
  computadas); trigger `tg_pedclit_cestado_asignacion` deshabilitado durante
  y rehabilitado en `finally`; pre-check contra el manifiesto ANTES de tocar
  nada (si algún snap falta o no cuadra, aborta sin escribir).

## SQL

`database/sql/2026_05_15_003_create_laset_snapshot_manifest.sql` (+drop) —
tabla `laset_snapshot_manifest (tag, db_name, table_key, table_name,
row_count, created_at, created_by, notes)`. El comando la auto-crea si falta.

## Workflow obligatorio

```
1. laset:snapshot <tag>          # antes de tocar comp=11
2. … proceso (Fase D pasada 2 / fix / prod) …
3a. OK   → seguir; opcional laset:snapshot <tag> --drop
3b. mal  → laset:restore <tag> --force   # estado = momento del snapshot
```

Es restauración **a un punto**, no undo incremental: cualquier cambio sobre
comp=11 (del proceso o de otro origen) posterior al snapshot se pisa.

## Gotchas (ver [[memoria#Snapshot / Restore Laset (reversibilidad)]])

- `DISABLE/ENABLE TRIGGER` **no admite prefijo de DB** → se ejecuta con
  `EXEC NewBytes_DBF.sys.sp_executesql N'DISABLE TRIGGER [dbo].[..] ON [dbo].[..]'`
  (la conexión default es NB_WEB).
- `IDENTITY_INSERT` exige lista de columnas explícita y una tabla a la vez →
  un solo `unprepared` batch por tabla.
- Tablas con identity: `pedprot.id_pedprod`, `pedclit.id`, `pedclil.id`,
  `pedclil_oc_asignacion.id`, `pedproi.id`, `albclit.id`,
  `albclil.IdDetalleRemito`, `stocks.id_auto`, `FP_Proveedores.ID_PROVEEDOR`,
  `registro_stock.id` (NB_WEB). `pedprol`/`albprol`/`clientes` sin identity.

## Estado

Probado end-to-end 2026-05-15: daño simulado (borrar albclil/pedproi,
`stocks=99999`, registro_stock) → `laset:restore` → estado **bit-idéntico**,
identidad contable igual (684/721), trigger rehabilitado. Punto
`postPasada1` creado (15949 filas, 14 tablas) como estado bueno
post-pasada-1.

---

## Ver también

- [[pedidos|Índice del proyecto]]
- [[feature-laset-import|Feature: Laset Import Framework]] — el proceso que esto respalda
- [[contexto#Reversibilidad: snapshot/restore (regla operativa)]]
- [[memoria#Snapshot / Restore Laset (reversibilidad)]]
- [[changelog#2026-05-15 (cont. 2) — Laset Fase D pasada 1 ejecutada + snapshot/restore]]
- Código: `app/Support/LasetSnapshotRegistry.php`, `app/Console/Commands/LasetSnapshot*`/`LasetRestore*`
- SQL: `database/sql/2026_05_15_003_*`
