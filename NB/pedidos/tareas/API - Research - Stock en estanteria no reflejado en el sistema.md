# API - Research - Stock en estantería no reflejado en el sistema

**Proyecto:** [[pedidos|Pedidos]]
**Estado:** Investigación cerrada — lista lista para conteo físico
**Fecha:** 2026-06-11
**Relacionado:** [[API - Research - Causas del stockDelta distinto de cero|Causas del stockDelta != 0]] · [[API - Fix - Corregir doble-descuento de stock por race en MakeSale|Fix doble-descuento]]

Pregunta: **¿qué artículos están físicamente en la estantería pero el sistema marca stock 0?** Se cruzaron **dos métodos independientes** y se construyó una lista de **máxima confianza** para conteo físico.

---

## Dos métodos independientes

### Método A — Documental (`stockDelta`)
`delta = ingresos(albprol) − ventas(albclil) − stock(stocks) ± ajustes`. Si `delta > 0` y el stock del sistema = 0, los documentos implican que debería haber unidades. **Debilidad:** arrastra ruido (drift histórico multi-path, horizonte de ingresos).

### Método B — Físico (números de serie)
`NEW_BYTES.dbo.ST_DETALLE_STOCK` registra cada unidad serializada con `FECHA_INGRESO` / `FECHA_EGRESO`. **Serial sin egreso = físicamente en el estante.** Conteo: 587.517 seriales presentes en total.
- **Debilidad:** ventas legacy que **no grabaron `FECHA_EGRESO`** dejan seriales "presentes" que ya salieron → **sobreestima** en ítems viejos/de volumen (ej. una fuente con 8.168 seriales presentes es casi seguro inflado).

### Intersección = máxima confianza
Un ítem entra si **ambos** lo confirman: `delta > 0` **Y** `stock sistema = 0` **Y** `seriales presentes > 0`.
Cantidad confiable = **`min(delta, seriales)`** — el delta (documental) actúa de **tope** que capa los seriales stale inflados.

---

## Resultado

| Vista | Items | Unidades |
|---|---:|---:|
| Método A solo (delta>0, stock 0) | 443 | 5.814 |
| Método B solo (seriales > sistema) | 1.144 | 66.082 |
| **Intersección (máxima confianza)** | **258** | **3.083** |

### Top de máxima confianza

| id | nombre | delta | seriales | confianza | race |
|---|---|--:|--:|--:|:--:|
| 102462 | DISCO SSD ADATA SU650 120GB | 692 | 480 | **480** | no |
| 108734 | MEMORIA ADATA SODIMM DDR4 8GB | 273 | 296 | **273** | no |
| 103098 | DISCO SSD HIKVISION C100 120GB | 289 | 269 | **269** | no |
| 7658 | MOUSE GENIUS DX-120 G5 | 198 | 1212 | **198** | parcial |
| 103928 | DISCO SSD MAXTOR 240GB | 134 | 118 | **118** | no |
| 102421 | DISCO HDD 1TB SEAGATE | 218 | 113 | **113** | no |
| 116343 | MEMORIA PATRIOT DDR4 8GB | 50 | 50 | **50** | no |
| 119699 | MOUSE WIRELESS GENIUS NX-7000X | 70 | 20 | **20** | **sí** |

**Casos de certeza máxima** = donde `delta ≈ seriales` (dos métodos caen en el mismo número sin coordinarse): `116343` (50=50), `108734` (273≈296), `103098` (289≈269), `101756` (64≈62).
**Triple confirmación** = los `race=sí` (119699, 119135): delta + seriales + firma exacta del bug de doble-descuento.

---

## Entregables (CSV)

- `items_maxima_confianza.csv` — **258 ítems** intersección (la lista para conteo). Cols: id, cref, nombre, empresa, delta_doc, seriales_presentes, confianza_min, explica_race.
- `items_faltantes_stock0.csv` — 443 (método A: delta>0 + stock 0).
- `items_estanteria_no_sistema.csv` — 1.144 (método B: seriales > sistema).
- `items_reales_delta.csv` — 682 productos físicos con delta>0.

---

## Recomendación

1. **Conteo físico** de los 258 de máxima confianza, ordenados por `confianza_min` (arrancar por SSDs/memorias 50+).
2. Lo confirmado en estante → **stock recuperable** que el sistema no ve → regularizar con el mecanismo de [[API - Fix - Script de regularización stock doble-descuento|el script de regularización]] (extendiéndolo a este set, no solo al race).
3. Lo no confirmado → era ruido (drift / seriales stale) → sirve para depurar la fórmula del panel.

## Notas técnicas

- SQL Server **muy viejo** (pre-2012): sin `TRY_CONVERT`, y requiere `OPENSSL_CONF` permisivo (TLSv1/SECLEVEL=0) para conectar desde macOS con Driver 17/18.
- Algunos `FECHA_INGRESO` en `ST_DETALLE_STOCK` tienen valores fuera de rango (rompen `DATEADD`) → el filtro de recencia se descartó; `min(delta, seriales)` ya mitiga el stale.
- Scripts ad-hoc (no versionados), corridos contra producción (190.210.23.97:4444).

## Ver también

- [[API - Research - Causas del stockDelta distinto de cero|Causas del stockDelta != 0]]
- [[API - Fix - Script de regularización stock doble-descuento|Script de regularización]]
- [[relacion-tablas-articulo-stocks|Artículo y stocks]]
