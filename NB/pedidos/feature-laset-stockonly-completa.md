# Feature: Compra completa para stock-only + Reservas

> Regla de negocio (usuario, 2026-06-23): **una compra se carga COMPLETA**, aunque el ítem no se haya vendido. Antes, las filas stock-only que caían en categoría C (SKU/proveedor sin alta en el catálogo comp=11) se **salteaban** → la OC quedaba **rota** (le faltaban líneas). Ahora se auto-crea el catálogo y se materializan, y las que tienen un cliente real se cargan como **reserva**.

Branch: `lasetImportFramework`. Commit `e2828cd8`. Ver [[feature-laset-import]] y [[feature-laset-fix-pedprot-stockonly]].

---

## El problema

El auto-create de artículos vivía SOLO en Fase C (camino de la VENTA / MATCHED). Las filas **stock-only** (compra sin venta, `year=1900`, sin `customer_invoice`) van por `laset:fix-stock-only-pedprol`, que en **categoría C** (SKU sin artículo comp=11) **salteaba** la fila. Resultado: la compra quedaba incompleta (ej. la OC 13812 sin su línea de `G507T-MLGC`).

## La solución (2 commands nuevos + wiring)

### 1. `laset:stockonly-autocreate-catalog`
Auto-crea en comp=11 **artículo** (clone del gemelo de otra company, o *fresh* con descripción/marca de la planilla), **marca** (`NB_WEB.dbo.marcas`) y **proveedor** (`FP_Proveedores`) faltantes, para las stock-only categoría C. Reusa textual los INSERT de Fase C. **Excluye RMA** (`sku LIKE 'RMA%'` → IGNORED: son ajustes, no stock). Idempotente.

### 2. `laset:fix-stock-only-pedprol` (existente)
Con el catálogo ya creado, las cat C pasan a **B/D** y se materializa `pedprol` + stock. La compra queda completa.

### 3. `laset:stockonly-reservas`
Las stock-only con **razón social de cliente REAL** (no el sentinel `'STOCK'`) se cargan como **RESERVA**: `pedclit` con `cestado='P'` (pendiente) + `pedclil` + asignación OC↔venta, **SIN remito** (`albclit`/`albclil`). La mercadería está en stock (la compra); la reserva es el compromiso del cliente, todavía sin entregar.

## Clasificación stock-only

| `razon_social` | Caso | Qué se carga |
|---|---|---|
| cliente real (ej. INVERSIONES SIPO SPA) | **Reserva** | compra + stock + pedclit/pedclil `cestado=P` (sin remito) |
| `'STOCK'` (sentinel) | **Stock puro** | compra + stock, sin venta |
| `RMA%` | Ajuste | IGNORED (excluido) |

## Patches de soporte

- **Fase D** `collectPedclitSinRemito`: excluye `cestado='P'` → las reservas NO generan remito.
- **`reconcile()`**: cuenta ventas **ENTREGADAS** (`albclil.ncanent`), no pedidas (`pedclil`). Una reserva (pedclil sin albclil) no descuenta stock, así que con la fórmula vieja marcaba falso delta. Identidad correcta: **compras − entregado − stock = 0**.
- **aggregate-match** + **fix-stock-only**: `sku NOT LIKE 'RMA%'` en el predicado stock-only.

## Durabilidad (Borrar todo → Importar todo)

**Fase C delega en orden**: `autocreate-catalog → fix-stock-only → reservas`. Como el job de "Importar todo" corre `aggregate-match → Fase C → Fase D → reconcile`, **todo esto se reproduce solo** en un wipe+reimport, sin pasos manuales.

## Estado dev (2026-06-23)

11 artículos + 1 proveedor (EVGA) creados, **12 compras materializadas** (3 OCs nuevas), **4 reservas** de INVERSIONES SIPO SPA en la OC 13812 (G507T-16FEC, GGB-FE, G507T-MLGC, PROA620ABEVO — 5 u c/u, sin remito), **0 STOCK_ONLY pendientes**. Snapshots: `pre_stockonly_catalog`, `pre_reservas`.

## Ver también

- [[feature-laset-import]] · [[feature-laset-fix-pedprot-stockonly]] · [[feature-sync-laset-botones]]
- [[contexto#Compra completa y reservas (stock-only)]]
- [[relacion-tablas-ped-alb|ventas pedclit/pedclil/albclit/albclil]]
