# Feature — Remito de compra faltante (albprol)

Cierra el gap por el cual algunos artículos Laset (comp=11) quedaban con **stock pero sin "ingreso"** (remito de compra `albprot`/`albprol`) → compra incompleta.

## Causa
**Fase D** (`LasetImportFaseDCommand`) crea el remito de compra decidiendo a **nivel OC**: `collectPedprotSinRemito()` agarra `pedprot` comp=11 que NO tienen `albprot`. Una vez que la OC tiene albprot, Fase D no la vuelve a mirar. Las líneas **stock-only** que `fix-stock-only-pedprol` adjunta a una OC ya remitada (en un import incremental anterior) nunca reciben su `albprol` → stock colgado sin documento de ingreso.

## Solución — `laset:fix-albprol-faltante`
`{--dry-run} {--skip-stock}`. Cierra el gap a **nivel línea**:
- OC que ya tiene `albprot` → **append** de la(s) `albprol` faltante(s).
- OC sin `albprot` → crea `albprot` + `albprol` (misma forma que Fase D).
- Stock: suma el delta de las líneas creadas, salvo `--skip-stock` (backfill retroactivo donde el stock ya está presente).

Idempotente (si no hay gap, no hace nada), dblib-safe (inserts fila a fila, stock vía tmp+JOIN con doble filtro comp=11 + almacén Laset), pre-checks con THROW + rollback. Invariante: tras escribir, 0 líneas pedprol comp=11 sin albprol.

## Durabilidad
Wireado en **`laset:run-import-job`** ("Importar todo") tras Fase D y antes de la reconciliación (sin `--skip-stock` → suma el stock de las líneas que Fase D se salteó). Un wipe+reimport **limpio** ya cerraba solo (Fase D pasa una vez); el gap aparece en el flujo **incremental** ("Importar seleccionadas"), que es como se generó.

## Backfill dev (2026-06-23)
12 albprol creados (3 headers nuevos + 5 OCs con append). OCs 13737/13749/13812/13826/13858/13859/13860/13861. Stock intacto. Commit `4e983957`. Snapshot `pre_albprol_20260623`.

## Ver también
[[feature-laset-stockonly-completa]] · [[feature-laset-import]] · [[contexto#Remito de compra (albprol) — gating por OC en Fase D]] · [[changelog]]
