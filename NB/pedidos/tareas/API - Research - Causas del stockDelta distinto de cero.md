# API - Research - Causas del stockDelta != 0 (auditoría global)

**Proyecto:** [[pedidos|Pedidos]]
**Estado:** Investigación cerrada
**Fecha:** 2026-06-11
**Relacionado:** [[API - Fix - Corregir doble-descuento de stock por race en MakeSale|Fix doble-descuento]] · [[API - Fix - Script de regularización stock doble-descuento|Script de regularización]]

Barrido del `stockDelta` (panel de inventario, `ms-metadata`) sobre **los 14.184 artículos**. **1.768 tienen delta ≠ 0**, pero se reparten en **6 causas distintas** — y el bug de doble-descuento (ya resuelto) resultó ser **el contribuyente más chico**. La conclusión grande: **~95% del delta es ruido estructural**, no faltante real.

---

## Clasificación de causas (delta ≠ 0)

| # | Causa | Items | Suma delta | ¿Bug real? |
|---|---|---:|---:|---|
| 1 | **Servicios / granel** (`serialAGranel=1`) | 216 | −1.120.709 | ❌ no es stock |
| 2 | **Laset (empresa 11)** — import framework | 292 | +31.317 | ❌ esperado |
| 3 | **Race doble-descuento** | 50 | +215 | ✅ sí (resuelto) |
| 4 | **Sin ingresos `albprol`** (horizonte/legacy) | 263 | −18.409 | ❌ estructural |
| 5 | **Delta negativo** (horizonte parcial) | 313 | −91.585 | ❌ estructural |
| 6 | **Delta positivo real (cola larga)** | 634 | +14.588 | ⚠️ drift histórico |
| | **TOTAL** | **1.768** | **−1.184.583** | |

---

## Detalle de cada causa

### 1. Servicios / granel — el elefante (−1,12M)
Items con `articulo.serialAGranel = 1`: conceptos no-físicos y a granel. Ejemplos:
- `102157` = **"COSTO FINANCIERO"** → stock 979.852 (sin sentido físico) → delta **−1.005.431** él solo.
- `102048` = **"SERVICIO DE TRANSPORTE"** (delta −67.706).
- `119749` = **"CABLE SUBTERRÁNEO x1MT"** (se vende por metro).

Sus números de stock/venta no reconcilian como unidades. **No deberían entrar al panel de delta.**

### 2. Laset / empresa 11 (+31k)
292 artículos comp 11, cargados por el [[feature-laset-import|Laset Import Framework]]. Stock importado sin ventas históricas equivalentes (o viceversa). Artefacto **conocido** del import, no un bug de stock.

### 3. Race doble-descuento (+215, 50 items "puros")
El bug ya diagnosticado y corregido (lock en [[modulo-makesale|MakeSale]]/[[modulo-removesale|RemoveSale]]). Aparece chico acá porque en muchos items afectados el delta queda **enterrado** bajo un negativo grande de las causas 1/4/5. La pérdida real del bug sigue siendo las **683 u / 138 items** medidas aparte (ver nota del fix).

### 4 y 5. Horizonte de historia (−110k)
Dato clave de fechas:
- Ventas (`albclit`): desde **2010**.
- Ingresos de proveedor (`albprol`): efectivos desde ~**2024**.

Todo lo vendido antes de que arranque el registro de ingresos da delta negativo porque la fórmula no "ve" su entrada. Es **estructural**, no faltante físico.

### 6. Cola larga — drift histórico multi-path (+14,5k, 634 items)
Productos físicos reales (no granel, no Laset) con delta positivo chico (típ. 50–700). **No** es el race.

**Caso drilleado — 102462 (DISCO SSD ADATA SU650, delta 692):** su stock fue tocado por **~12 subsistemas distintos** a lo largo de años:

| fichero (subsistema) | movs | neto |
|---|---:|---:|
| `generarRemitoTipo.php` (legacy) | 1292 | −13.453 |
| `remitos.class.php` | 729 | −2.661 |
| `eliminarRemito.php` | 599 | +4.247 |
| `crearCopiarRemito.php` | 422 | +4.076 |
| `agregar-detalle-remito.php` | 315 | −1.597 |
| `PedidoModel.php` | 576 | −649 |
| `Mover stock entre depósitos` | 81 | +5.064 |
| `MakeSaleService` (el nuevo) | 43 | −480 |

Venta neta según el kardex de MakeSale = **399**, pero `albclil` documenta **7.882** ventas → la mayoría pasó por los **paths legacy**, no por `MakeSaleService`. El delta de 692 es el **residual acumulado** de miles de movimientos en una docena de subsistemas. **No hay un único bug**: es drift contable histórico. Contribuyentes concretos: `PedidoModel.php` (descuenta stock sin documento de venta), y la asimetría de logueo de `Mover stock entre depósitos`.

---

## Items reales (entregable)

CSV `items_reales_delta.csv`: **682 productos físicos** (sin granel, sin Laset, sin pseudo-facturación) con delta > 0, suma **9.565 u**. Columnas: `id, cref, nombre, empresa, ingresos, ventas, stock, delta, explica_race`.

Reparto:
- **50** explicados por el race (`explica_race=si`).
- **28** parciales.
- **604** otra causa (drift histórico, mermas, ajustes).

Top candidatos a **faltante físico real** (delta alto, sin race) → conviene conteo:
`102462` SSD ADATA SU650 (692) · `103098` SSD Hikvision C100 (289) · `108734` Memoria ADATA SODIMM (273) · `102421` HDD Seagate 1TB (218).

---

## Recomendaciones para el panel de delta

1. **Excluir `serialAGranel = 1`** (servicios/granel) — elimina ~1,12M de ruido.
2. **Excluir pseudo-artículos** por nombre (`FACTURAC%`, `SIN ITEM`, `FLETE`) que no tengan la bandera granel.
3. **Acotar ventas al horizonte con ingresos** (post-inicio de `albprol`, ~2024) o marcar/filtrar items pre-horizonte — elimina los −110k de causas 4/5.
4. **(Opcional) Empresa 11 aparte** mientras dure la operación de import Laset.
5. Tras 1–3, el panel mostraría solo discrepancias accionables: el race (resuelto) + la cola larga real.

## Metodología

Delta por artículo replicando la fórmula de `stocks.py` con CTEs pre-agregadas (stock por `stocks`, inbound por `albprol`, sales/reserved por `albclil`+`albclit`, NC postventa por `ST_RMADETALLE`). Causa del race vía la firma `(cref, remito, sAnterior)` con ≥2 `MakeSaleService`. Drill por `fichero` en `registro_stock`. Scripts ad-hoc (no versionados) corridos contra producción (190.210.23.97:4444) con `OPENSSL_CONF` permisivo.

## Ver también

- [[API - Fix - Corregir doble-descuento de stock por race en MakeSale|Fix del race]]
- [[API - Fix - Script de regularización stock doble-descuento|Regularización 683 u]]
- [[relacion-tablas-articulo-stocks|Artículo y stocks]] · [[relacion-tablas-ped-alb|pedclit/albclit]]
- [[feature-laset-import|Laset Import Framework]]
