# Feature: Fix marcas comp=11

Fix retroactivo del bug histórico en `LasetImportFaseC` que escribía marcas en la tabla equivocada (`FP_Marcas`) y rompía `articulo.Id_Marca` para todos los artículos Laset.

## El bug

La versión vieja de `LasetImportFaseC` resolvía/creaba marcas en `NewBytes_DBF.dbo.FP_Marcas` — tabla **legacy sin PK ni `companyCode`**. La reserva de IDs vía `MAX(ID_Marca)+1` se rompió por concurrencia: terminó con **199 filas con `ID_Marca=80`** (25 marcas distintas) y **5 filas con `ID_Marca=81`** (4 distintas).

Pero el problema más grave: **`articulo.Id_Marca` apunta semánticamente a `NB_WEB.dbo.marcas.id`**, NO a FP_Marcas. Toda la app (Brand model, TotalSales, Statistics, Marketing, Product, Downloader, Report, etc.) joinea `articulo.Id_MARCA = marcas.id`. Resultado: **151 artículos Laset con `Id_Marca` corrupto**. Ejemplo:

- art 122806 `ROG-THOR-1000P3-GAMING` (cpredef4=`ASUS`, Id_Marca=80)
  - FP_Marcas[80] = KINGSTON ❌
  - NB_WEB.marcas[80] = ROCCAT comp=4 ❌

ASUS aparecía como ROCCAT en toda la app de NB.

## La solución

### 1) Refactor de Fase C (preventivo, futuras corridas)

`LasetImportFaseCCommand` cambió de FP_Marcas a `NB_WEB.dbo.marcas` con `companyCode=11`:

- Lookup case-insensitive scopeado a `companyCode=11`. Una marca de comp=4 NO sirve para comp=11.
- `marcas.id` es **IDENTITY** → INSERT row-by-row + `SELECT CAST(SCOPE_IDENTITY() AS INT) AS id` para capturar el id real (sin `MAX(id)+1`).
- `articulosAutoCreate[].marca_id` se resuelve **post-INSERT** de marcas (no se pre-reserva). Si pre-reservás IDs sobre IDENTITY te explota con `Cannot insert explicit value for identity column when IDENTITY_INSERT is set to OFF`.

### 2) Service + command + endpoint reutilizables (retroactivo)

Mismo patrón que [[feature-laset-relink-facturas]] (ver [[feature-sync-laset-botones]]):

- **Service**: `app/Services/Laset/FixMarcasComp11Service.php` — `preview()` y `execute()` retornando arrays serializables. Toda la lógica vive ahí (transacción, pre-check, verify post).
- **Command CLI**: `php artisan laset:fix-marcas-comp11 [--dry-run]`.
- **Controller**: `POST /v1/laset/fix-marcas-comp11` body `{dry_run}`.
- **Frontend**: botón "Fix marcas comp=11" en `pages/syncLaset.vue` (al lado de "Re-vincular facturas").

### Flujo del service

1. Backup `articulo` comp=11 → `NewBytes_DBF.dbo.laset_fix_marcas_backup_articulo`.
2. Calcular marcas faltantes (cpredef4 distintos sin entry en NB_WEB.marcas comp=11) → INSERT row-by-row.
3. Construir map `(cpredef4_upper → marca_id)` en tabla tmp `laset_fix_marcas_map`.
4. Pre-check: todo cpredef4 debe resolver. Si no, THROW + rollback.
5. `UPDATE articulo SET Id_Marca = m.marca_id` vía `JOIN tabla_map` (single-statement, dblib-safe).
6. Backup `FP_Marcas` filas con ID_Marca duplicado → `laset_fix_marcas_backup_fp`.
7. `DELETE FROM FP_Marcas WHERE ID_Marca IN (... ids con >1 fila distinta ...)`.
8. Verify post: 0 articulos comp=11 con Id_Marca mal vinculado. Si > 0, THROW.

Idempotente: re-correr sobre data limpia devuelve preview con 0 cambios.

## Resultado en dev (2026-05-30)

- **151 articulos comp=11 remapeados** al `Id_Marca` correcto.
- **5 marcas nuevas creadas en `NB_WEB.dbo.marcas`** con `companyCode=11`:
  - ACER (id=1320), HP (1321), LENOVO (1322), MICROVIP (1323), WD (1324)
- **204 filas basura eliminadas de `FP_Marcas`** (199 con ID=80 + 5 con ID=81).
- Backups en `laset_fix_marcas_backup_articulo` y `laset_fix_marcas_backup_fp` — mantener hasta validar prod.

## Archivos

- `api-rest-pedidos-laravel/app/app/Services/Laset/FixMarcasComp11Service.php`
- `api-rest-pedidos-laravel/app/app/Console/Commands/LasetFixMarcasComp11Command.php`
- `api-rest-pedidos-laravel/app/app/Http/Controllers/Laset/LasetFixMarcasComp11Run.php`
- `api-rest-pedidos-laravel/app/app/Console/Commands/LasetImportFaseCCommand.php` (refactor)
- `api-rest-pedidos-laravel/app/routes/api.php` (POST /v1/laset/fix-marcas-comp11)
- `api-rest-pedidos-laravel/app/database/sql/2026_05_30_002_fix_articulo_id_marca_comp11.sql` (referencia histórica)
- `pedidos-web-app-v1/app/pages/syncLaset.vue` (botón + modal)
- `pedidos-web-app-v1/app/plugins/api.js` (`fixMarcasComp11`)

## Deploy a producción

1. Pull del code (back y front).
2. Disparar `POST /v1/laset/fix-marcas-comp11 {dry_run:true}` desde el botón para ver preview.
3. Disparar `dry_run:false` para aplicar. Backups quedan en `laset_fix_marcas_backup_*`.
4. (Opcional) `php artisan laset:fix-marcas-comp11 --dry-run` desde CLI hace exactamente lo mismo.

A futuro, toda nueva importación nace bien (Fase C ya usa NB_WEB.marcas comp=11) — el botón queda para mantenimiento puntual.

## Ver también

- [[feature-laset-import|Laset Import Framework]] — Fase C refactorizada
- [[feature-sync-laset-botones|Patrón Sync Laset]] — service+command+controller+UI
- [[relacion-tablas-articulo-stocks|articulo y stocks]] — schema y FKs
