# Feature: Import Cuenta Corriente histórica Laset (comp=11)

> Importa la cuenta corriente histórica USD de clientes **exclusivos Laset (CODEMP=11)** desde la planilla Excel `Estado de Cuenta - Clientes 2023.12.21.xlsx` (~148 hojas, **1 hoja = 1 cuenta**) hacia `NEW_BYTES.dbo.MC_CCORRIENTES_MOVIMIENTOS` con `ID_PROCEDENCIA=99`.

Branch: `lasetImportFramework`. Botón **"Importar cuenta corriente"** en `/syncLaset` (preview → confirmar). Spec completa en el repo: `docs/cuenta-corriente/README.md`.

---

## Arquitectura

PhpSpreadsheet es inviable para este archivo → el parseo lo hace un **sidecar Python/openpyxl**: `scripts/laset_ccte_to_json.py` (parser PURO, sin DB). El service PHP hace el matching, las excepciones y el INSERT.

- **Parser** `scripts/laset_ccte_to_json.py` — por hoja detecta dinámicamente el bloque USD `[Fecha][Debe][Haber][Saldo]` anclando en el header **"Debe"** (columnas NO fijas), reconstruye movimientos por **delta-de-Saldo**, y extrae razón social (C1) + celda **"A favor / Deuda"**. Materializa cada hoja una sola vez (read_only O(n²) si se accede aleatorio).
- **Service** `app/Services/Laset/LasetCtaCteImportService.php` — exclusiones, matching hoja→cliente comp=11 (crea faltantes), validación (reconcilia + cruce A favor/Deuda), cierres uniformes, INSERT.
- **Command** `php artisan laset:ccte-import {file} {--dry-run}`.
- **Controller** `LasetCtaCteImportRun` → `POST /v1/laset/ccte-import` (multipart).
- **Front** `pages/syncLaset.vue` + `plugins/api.js#cctImport`.

## Método delta-de-Saldo

`delta = Saldo[i] − Saldo[i−1]`; `imp = abs(delta)` (SIEMPRE magnitud positiva); `tr = '24'` si delta>0 si no `'42'`. Concilia por construcción.

**Convención de signo (este ERP la invierte)**: `CC_IMPORTEUSD` siempre positivo, el signo lo da `TR_CODIGO`. En `AccountRepository`, `tr ∈ (4,24,125,14,34,32,41)` se multiplica ×(−1) → **tr24 (débito) se muestra NEGATIVO**, **tr42 (crédito/pago) POSITIVO**. Por eso `SUM(CASE)` del ERP == −1 × saldo final de la planilla. Ver [[contexto#Cuenta corriente Laset — convención de signo y ajustes]].

## Reemplazo POR CUENTA (incremental)

`execute()` NO borra todo `proc=99`: borra y recarga **solo las cuentas (`ID_CLIENTE`) presentes en el archivo subido**; las ausentes quedan intactas → se puede subir una planilla **parcial** (solo cuentas nuevas/corregidas). Subir el master completo replaza todas = wipe total. No toca movimientos manuales (`proc IS NULL`). El preview muestra **cuentas a reemplazar** vs **cuentas a agregar**.

## Matching cliente — NB Inc es cliente DISTINTO

Una cuenta `-NBinc` (vía New Bytes Inc) SIEMPRE es un cliente distinto del homónimo normal (ej. EMAP SA `096882` vs EMAP SA (NB Inc) `100122`). El token-search ahora respeta la NB-Inc-ness: **una hoja NB Inc solo matchea clientes NB Inc, una hoja normal nunca matchea un cliente NB Inc**. Sin esto, la hoja quedaba **ambigua → OMITIDA → con dato viejo de una import previa** (síntoma que reportó el usuario: EMAP daba 63.160,50 en vez de 14.761,50). **Lección: una hoja ambigua/omitida deja la cuenta stale → revisar siempre las advertencias del preview.**

## Cierres y huérfanas

Para hojas que NO cruzan la celda "A favor/Deuda": `closing = sign(SUM)·|afavor| − SUM` (tr24 si neg, tr42 si pos). Reproduce las huérfanas (Mugello A-3771, IIA A-3760, Ceologistics) y los cierres `-NBinc` sin hardcodear montos.

## Exclusiones

Intercompañía (`NB`, `New Bytes`, `Laset`, `NB-Laintek`), tesorería USDT (`Iris USDT`, `USDT Egresos`, **`USDT`** — la hoja suelta entraba como cliente trucho con cierre ~1,47M), y sub-ledger `MG Interno` (dup de MG Soluciones). Ambiguas reales (`I y T` = 3 clientes INVERSIONES Y TECNOLOGIA) se OMITEN y se avisan.

## Rollback

Todo lo importado lleva `ID_PROCEDENCIA=99` → `DELETE FROM NEW_BYTES.dbo.MC_CCORRIENTES_MOVIMIENTOS WHERE ID_PROCEDENCIA=99` borra solo la import (no toca movimientos manuales).

## Bug resuelto — autoFilter (openpyxl 3.1.x)

openpyxl en read_only crashea con `ValueError: Value must be either numerical or a string containing a wildcard` si una hoja tiene un autoFilter con un `customFilter` no numérico/no comodín (planillas con filtros aplicados a mano). El parser parchea `CustomFilterValueDescriptor.__set__` para guardar el valor crudo en vez de abortar. No usamos autofiltros.

## Estado

Import real ejecutado (2026-06-22): **5.640 movimientos / 125 cuentas** (`proc=99`). EMAP verificado en 14.761,50. **Falta**: desplegar `scripts/laset_ccte_to_json.py` a prod (python3+openpyxl); resolver `I y T` a mano.

## Ver también

- [[feature-laset-import]] — import de compras/ventas comp=11
- [[contexto#Cuenta corriente Laset — convención de signo y ajustes]]
- [[feature-sync-laset-botones]] — patrón service+command+controller+UI
- [[memoria#Cuenta corriente histórica Laset]]
