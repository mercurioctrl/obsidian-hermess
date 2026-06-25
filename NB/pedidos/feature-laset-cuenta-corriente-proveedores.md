# Feature — Cuenta corriente de PROVEEDORES Laset (comp=11)

Importa la cuenta corriente histórica de proveedores Laset (comp=11) desde
`Estado de Cuenta - Proveedores 2023.12.21 (2).xlsx` a `NEW_BYTES.dbo.MS_MOV_CTACTE_PROVEEDORES`.
Análogo a [[feature-laset-cuenta-corriente|cta cte de clientes]] pero para proveedores.

## Entregables
- `scripts/laset_prov_ccte_to_json.py` — parser del Excel a JSON.
- `app/Console/Commands/LasetProvCtaCteImportCommand.php` — `laset:prov-ccte-import {--dry-run} {--file=}`.

## Estructura del Excel
Una hoja por proveedor (libro a nivel factura, columnas detectadas por header, no fijas):
`Fecha, Invoice, Status, Facturado, Asignado, Saldo, Pagado, Comment`. Al **pie** de cada hoja:
bloque resumen `A favor / Deuda` y `NC Disponible` (ojo: NO arriba como la plantilla — están al final, p.ej. Asus fila 658).

## Saldo objetivo (regla del usuario)
`target = A favor/Deuda + NC` **si hay DEUDA (afd>0)**; si es a favor (afd≤0) `target = A favor/Deuda`.
Convención: positivo = **deuda** (le debemos al proveedor); negativo = a favor.
- Asus (deuda) → 53.258,11 − 5.361,89 = 47.896,22
- AMI (a favor) → −2.685,00 (NC no se resta de nuevo, la "A favor/Deuda" ya ES la NC)
- Crown → 0

## Movimientos (importe = magnitud + signo por TR, igual que clientes)
- Facturado > 0 → factura/deuda → **TR 38** (Pedidos Proveedores, +)
- Facturado < 0 → NC/RMA → **TR 30** (Créditos Varios, −)
- Pagado → pago → **TR 40** (Pago a Proveedores, −)
- NC Disponible (solo si deuda) → **TR 30** (−)
- ajuste de cierre → **TR 30/32** para clavar el target exacto

## ⚠️ Clave correcta: CCODPRO, no Id_Proveedor
La cta cte legacy keyea por **`FP_Proveedores.CCODPRO`** (código de proveedor legacy), NO por el
`Id_Proveedor` interno. Asus Id_Proveedor 16679 → **CCODPRO `002605`**. Los movimientos van bajo
ese CCODPRO; la pantalla del proveedor lo busca así. (1er intento se cargó bajo `016679` y no se veía
→ rollback por `USU='Laset'` + re-import con CCODPRO.) Todos los comp=11 tienen CCODPRO.

## Mecánica
- Resuelve hoja → `FP_Proveedores` comp=11 (por nombre + alias). `ID_PROVEEDOR` = CCODPRO.
- Crea el proveedor en `MS_PROVEEDORES` si falta (no estaban; saldo 0).
- `ID_MOVIMIENTO` **no es identity** → MAX+1 fila a fila (dblib-safe).
- **Idempotente**: re-import borra `WHERE ID_PROVEEDOR=? AND USU_IDENTIFICACION='Laset'` y reinserta.
- **Rollback** total: `DELETE … WHERE USU_IDENTIFICACION='Laset'` (no toca legacy NB).
- Guard anti-colisión (2 hojas → mismo CCODPRO aborta).

## Estado (2026-06-24, dev)
**66 proveedores comp=11 · 5.573 movimientos · 66/66 reconcilian** contra target. Legacy NB (29.171) intacto.
Verificado vs números del usuario: AMI −2.685, Asus 47.896,22, MSI 1.068.597.

## Pendientes
- **EUR (17 hojas)**: proveedores europeos (Robot, Irinox, Eurocave, Rational…) en EUR → 2ª pasada (falta conversión a USD).
- **10 hojas con saldo que NO son comp=11** (Estudio −113k, Acer −71k, Suntec −58k, Expand Tech +47k, Melery −40k, Thermaltake −3k…): decidir alta como comp=11 o fuera de scope.
- **Asus**: residuo $16,49 (mi NC = celda "NC Disponible" −5.361,89 vs el −5.345,40 exacto).

## Ver también
[[feature-laset-cuenta-corriente]] · [[contexto#Cuenta corriente de proveedores (comp=11)]] · [[changelog]] · [[pedidos]]
