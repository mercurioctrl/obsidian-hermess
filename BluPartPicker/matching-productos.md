# Matching de productos (`oracular_sku`)

Resolución de entidades **no destructiva**: items de distintas fuentes que son el **mismo producto físico** se agrupan bajo un `oracular_sku` canónico. Resuelve el problema de comparar precios del mismo producto cuando el SKU/part number es insuficiente o ausente. Generado por `match_products.py` (NO por los syncs). **Precisión > cobertura**: ante la duda, el item queda `NULL`.

Cobertura actual: **~63-65%** del catálogo agrupado. El resto son mayormente singletons reales (un solo lugar los vende → nada que matchear).

## Tablas (todas nuevas, no tocan `itemsRepository`)

```sql
product_groups(oracular_sku PK, nombre_canonico, marca, categoria, nro_parte, ean, n_items, ...)
item_oracular_map(source, codigo, oracular_sku, metodo, confianza, matched_at)  -- trazabilidad
manual_matches(source_a, codigo_a, source_b, codigo_b, veredicto, fuente, nota)  -- adjudicados durables
match_candidates(source_a, codigo_a, source_b, codigo_b, sim, motivo)            -- cola de revisión
```

`itemsRepository.oracular_sku` = columna espejo (puede ser `null`). `metodo` ∈ ean(1.0) · nro_parte(0.95) · adjudicado(0.92) · nombre_exacto(0.90) · imagen(0.85, opt-in) · fuzzy(0.80).

## Pipeline (`match_products.py`, idempotente — recalcula todo cada corrida)

Union-find sobre claves/aristas de precisión decreciente:

1. **Nivel 1 — deterministas:** EAN, nro_parte normalizado, nombre+marca exacto. Con **filtro de promiscuidad** (descarta un EAN/part number compartido por productos sin modelo en común — ej. un reseller reusando un EAN para 6 cables distintos).
2. **Nivel 1.5 — marca:** canonicaliza alias sub-marca→madre (xpg→adata, aorus→gigabyte, wd/westerndigital…) y descarta etiquetas basura (discontinuos, generica…).
3. **Nivel 3b — adjudicados:** une los `manual_matches` con `veredicto='same'`, con red de seguridad (vetos de marca/spec/variante/palabra-rara) para no propagar errores del LLM.
4. **Nivel 2 / 3a — fuzzy:** dentro de bloques (marca + token-modelo), IDF-weighted Jaccard. Vetos: `spec_contradiction` (gb/tb/hz/w/pack), `variant_conflict` (calificador/color/código de modelo en pugna), `brands_compatible`, **token raro discriminativo** (`RARE_CAP`: "vortex"/"blaze" distinguen aunque no tengan dígitos).
5. **Nivel 4 — imagen** (opt-in `--image`): une por `imagen_url` compartida; off por default (señal menos precisa: placeholders + fotos de serie entre variantes).
6. **Auditoría:** `audit_group` deja en `NULL` grupos con marcas/specs en conflicto.

## El loop de "ir completando"

```
match_products.py  →  gen_candidates.py  →  /ui (curación humana)  →  POST /match  →  manual_matches
        ↑__________________________________________________________________________________|
                              (se reaplica al re-correr)
```

- **`gen_candidates.py`** precomputa `match_candidates`: pares en banda gris [0.55, 0.85) que pasan los vetos, no decididos, top-4 por item. ~15.8k candidatos (sin_asignar = recall nuevo · ambiguo_3b = consolidar).
- **Consola de curación** en `http://<host>:4444/ui` (`frontend/index.html`, vanilla JS): vista "Productos matcheados" (comparador de precios) + vista "Revisar candidatos" (Mismo/Distinto/Saltar, atajos 1/2/3). Cada veredicto → `POST /match` → `manual_matches`.

## Endpoints relacionados

- `GET /groups` — productos canónicos con ahorro entre fuentes.
- `GET /groups/{oracular_sku}` — **comparador**: el mismo producto en todas las tiendas, ordenado por precio (`mas_barato_en_stock`).
- `GET /candidates` · `POST /match` — cola de curación y veredicto (único endpoint de escritura).
- `GET /items` ahora incluye `oracular_sku` por item.

## Aprendizajes clave

- El part number **solo no alcanza**: los productos compatibles/alternativos citan el código OEM (toner Cromink "ALT. HP CE320A" ≠ HP real). Por eso la guarda de marca.
- Trampa EAN: no extraer dígitos de un alfanumérico (`BX80768225F` ≠ EAN — la F distingue 225 de 225F).
- Pasada masiva con Haiku (63 agentes, 2.482 clusters): subió cobertura pero **al nivel de precisión exigido la ganancia neta sobre el determinista es chica** (~0.6%) — las redes de seguridad sacan los merges riesgosos. El valor real fue eliminar errores duros y dejar el corpus durable.

## Ver también

- [[BluPartPicker]] — índice del proyecto
- [[arquitectura]] — schema DB y endpoints completos
- [[memoria]] — gotchas y próximos pasos
- [[changelog]] — historial
