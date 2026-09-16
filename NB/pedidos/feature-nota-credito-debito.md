# Feature: Nota de Crédito/Débito (creditDebitNote) — de eze

Feature de **eze** (commit `b90c00a1`, PR #1642, `PED-1436`, mergeado a Development): emitir **Nota de Crédito/Débito en cuenta corriente** + comprobante manual.

## Qué hace

- Nuevo accionable de **Nota de Crédito/Débito desde la cuenta corriente del cliente**.
- **Endpoint:** `POST /voucher/creditDebitNote`, **circuito exclusivo de sucursal `0010`** (no fiscal, **no genera comprobante AFIP**), protegido por `CreditDebitNoteMiddleware`.
- **Escribe en:** `NEW_BYTES.dbo.MC_CCORRIENTES_MOVIMIENTOS` — la observación va a `CC_OBSERVACIONES`; anular un movimiento = `CC_ANULADO='SI'`.

## Permiso RBAC: `creditDebitNote`

- Columna BIT en `NB_WEB.dbo.permisos_agente` (DEFAULT 0). Migración `app/database/sql/2026_09_14_001_add_credit_debit_note_permission.sql`.
- **Independiente de `createManualVoucher`**, que a partir de esta feature solo autoriza comprobantes tipo **FACTURA** vía `/makeVoucherManual`.
- Implementado en los 4 lugares del checklist: columna + `AuthRepository` (login/getByToken) + `UserDto` + middleware/ruta. Ver [[decision-permiso-nuevo-agente]].
- **Otorgar:** `UPDATE NB_WEB.dbo.permisos_agente SET creditDebitNote=1 WHERE id_usuario_web=<UserId>;` y el usuario debe **reloguear** (el token bakea los permisos).

## Incidente 2026-09-15 — hecho sobre BETA (no dev)

Al probar la feature se descubrió que el backend local escribe en **`beta.nb.com.ar`** (red productiva), no en dev — ver [[contexto#⚠️ El backend local escribe en BETA (red productiva)]].

- Se aplicó el `ALTER` que agrega la columna y se otorgó `creditDebitNote` a **catriel** (`UserId 7463`, `permisos_agente.id`=8).
- Una NC de prueba (suc 10, obs "Test") creó el movimiento real **`ID_CCMOVIMIENTO=1031266`** en la cta cte del cliente **102335 (LA NUEVA LIGA GG SAS)**, USD 2424, `CC_ANULADO='NO'`. Sin comprobante AFIP.
- **PENDIENTE:** anularlo → `UPDATE NEW_BYTES.dbo.MC_CCORRIENTES_MOVIMIENTOS SET CC_ANULADO='SI' WHERE ID_CCMOVIMIENTO=1031266;` y decidir si dejar/revertir el grant + columna en beta.

## Ver también

- [[feature-comprobantes-emisor]] — fix de la grilla de Comprobantes en paralelo
- [[decision-permiso-nuevo-agente|Checklist: agregar un permiso nuevo]]
- [[runbook-alta-usuario-interno]]
- [[changelog#2026-09-15 — Nota de Crédito/Débito (eze) + incidente en base beta]]
