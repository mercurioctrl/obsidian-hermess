# Feature: Patrón Sync Laset — botones de mantenimiento

`/syncLaset` expone botones de mantenimiento que ejecutan fixes idempotentes sobre la operación Laset (comp=11) directamente desde la UI, sin SSH al server. Patrón consolidado tras portar varios comandos CLI a endpoints HTTP.

## Botones actuales en /syncLaset

1. **Reimportar planilla** — sube `.xlsx`, crea batch nuevo en `laset_import_staging`.
2. **Re-vincular facturas** — dispara `RelinkFacturasService` (re-apunta `FP_FactWebCliEncabezado_Uy.ID_NROREMCLI_ENC` a remitos importados).
3. **Fix marcas comp=11** — dispara `FixMarcasComp11Service` (ver [[feature-laset-fix-marcas-comp11]]).
4. **Validar stocks** — dispara `CheckStocksOrphansService` (casos A/B + drill-down + limpiar fantasmas). Ver [[feature-laset-wipe-reimport]].
5. **Borrar todo comp=11** — dispara `WipeTransactionalService` (borra tajada transaccional + barrido de huérfanos + snapshot). Ver [[feature-laset-wipe-reimport]].
6. **Importar seleccionadas / Importar todo** — job async (orquesta aggregate-match + Fase C + Fase D + reconciliación). "Importar todo" usa `selectable-ids?batchId='all'`.

## El patrón (5 piezas)

Para cada feature de mantenimiento Laset:

### 1) Service (`app/Services/Laset/{Feature}Service.php`)

Núcleo: lógica completa, idempotente, dblib-safe. Expone `preview(): array` y `execute(): array` con resultados serializables.

```php
public function preview(): array { /* lee + reporta sin escribir */ }
public function execute(): array {
    DB::beginTransaction();
    try {
        $before = $this->preview();
        // ... operaciones ...
        $this->verifyPost();
        DB::commit();
    } catch (\Throwable $e) {
        DB::rollBack();
        throw $e;
    }
    return [...];
}
```

### 2) Command CLI (`app/Console/Commands/Laset{Feature}Command.php`)

Wrapper delgado. Signature `laset:<accion> [--dry-run]`. Solo formatea output del service. Útil para correr fixes desde server sin UI.

### 3) Controller (`app/Http/Controllers/Laset/Laset{Feature}Run.php`)

Invokable. Body `{dry_run: bool (default true)}`. Delega al service.

```php
public function __invoke(Request $req, {Feature}Service $svc): JsonResponse {
    $dryRun = $req->boolean('dry_run', true);
    return $this->success([
        'dry_run' => $dryRun,
        'result' => $dryRun ? $svc->preview() : $svc->execute(),
    ]);
}
```

### 4) Ruta + permiso

```php
// routes/api.php — dentro del grupo Laset con middleware permission + lasetView
Route::post('/<accion>', \App\Http\Controllers\Laset\Laset{Feature}Run::class);
```

### 5) UI (`pages/syncLaset.vue` + `plugins/api.js`)

- Wrapper async en `api.js` dentro del namespace `laset`.
- Botón en el header (al lado de los existentes).
- Modal preview → confirmar:
  - Click → llama `preview()` (dry_run=true) → muestra stats, listas, muestras.
  - Click "Aplicar" → llama `execute()` (dry_run=false) → muestra resultado + notification.
- `ok-text` dinámico: "Calculando…" → "Aplicar a N…" / "Nada para arreglar" → "Cerrar".

## Reglas de diseño

- **Idempotente obligatorio**: re-correr sobre data limpia → preview con 0 cambios, execute es no-op.
- **Síncrono** (no jobs async): si la operación tarda < 30s. Para procesos largos (importar seleccionadas) usar el patrón `laset_import_jobs` con polling.
- **Verify post**: contar filas en estado inválido. Si > 0, THROW + rollback.
- **Aislamiento estricto comp=11**: todos los UPDATE/DELETE llevan `WHERE companyCode=11` (directo o vía JOIN compuesto a la cabecera). Para operaciones que tocan varias empresas potencialmente, agregar **guard de aislamiento** (baseline antes/después, THROW si cambia otra empresa) — ver [[feature-laset-wipe-reimport]].
- **Borrados jerárquicos**: hijos→padres (FK-safe). El verify por scope con JOIN al padre es **ciego a huérfanos** — agregar barrido aparte. Ver [[feature-laset-wipe-reimport]].
- **dblib-safe**: ver [[memoria#dblib]] — statements individuales, no batches multi-statement con DECLARE/IF/PRINT.
- **Backups**: cada execute crea tabla `laset_<feature>_backup_*` antes de mutar (o snapshot `pre_wipe_*`). Mantener hasta validar prod.

## Implementaciones existentes

- **RelinkFacturasService** + `LasetRelinkFacturasCommand` + `LasetRelinkFacturasRun` — re-vinculación facturas CFE Uruguay.
- **FixMarcasComp11Service** + `LasetFixMarcasComp11Command` + `LasetFixMarcasComp11Run` — fix retroactivo `articulo.Id_Marca` comp=11.
- **WipeTransactionalService** + `LasetWipeTransactionalCommand` + `LasetWipeTransactionalRun` — borrado transaccional comp=11 + barrido de huérfanos (ver [[feature-laset-wipe-reimport]]).
- **CheckStocksOrphansService** + `LasetCheckStocksOrphansCommand` + `LasetCheckStocksOrphans` — validación de inconsistencias de stock (read-only).
- **CleanGhostStocksService** + `LasetCleanGhostStocksCommand` + `LasetCleanGhostStocksRun` — limpieza de filas fantasma de stock.

## Ver también

- [[feature-laset-wipe-reimport|Borrar todo comp=11 + reimport limpio]]
- [[feature-laset-fix-marcas-comp11|Fix marcas comp=11]]
- [[feature-laset-import|Laset Import Framework]]
- [[feature-laset-fix-pedprot-stockonly|Fix pedprot/stockonly]]
- [[arquitectura|Arquitectura]]
