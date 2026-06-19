# Memoria — BluPartPicker

## Estado actual (2026-06-18)

- **5 mayoristas:** invid, ceven, stylus, **nb, air** + ~37 resellers preciosgamer_*
- **API v2.2.0** — conversión de precios en tiempo real + **matching de productos** (`oracular_sku`) + consola de curación en `/ui`
- ~37.9k items agrupados (~63-65% del catálogo de ~59.6k) bajo `oracular_sku`
- Syncs con cron a horas fijas de madrugada (ver `crontab -l`). **Falta agregar `match_products.py` + `gen_candidates.py` al cron** (correr después de los syncs).

> Estado 2026-06-04: 4 fuentes (sin nb/air), API v2.1.0, sin matching ni frontend.

## Gotchas activos

- La DB se llama `invid.db` — herencia del primer distribuidor, no renombrar (rompe paths)
- **PreciosGamer source:** formato `preciosgamer_{slug}` — ej: `preciosgamer_venex`, `preciosgamer_libre-opcion`. NO es el resellerId numérico (ya migrado).
- **PreciosGamer modelo:** DELETE + INSERT en cada sync. No hay "actualizados", siempre son "nuevos". La tabla muestra solo los items actualizados en las últimas 48h.
- El oráculo de marcas usa qty≥2 — marcas con 1 sola ocurrencia se ignoran como ruido
- Playwright solo para Ceven; Akamai bloquea cualquier intento con requests/curl
- **Invid moneda:** el Excel devuelve `"US$"`, no `"USD"` — siempre normalizar en `parse_excel()`. La expresión SQL usa `moneda = 'USD'` exacto.
- Los precios en la API están en moneda original. Para comparar USD vs ARS usar `moneda_out`; sin eso `precio_final` es el valor crudo de cada fuente.
- Ceven puede tener timeouts de login transitorios — si falla en cron, correr manual primero para confirmar que el sitio esté operativo.

### Matching (`oracular_sku`) — ver [[matching-productos]]
- `match_products.py` recalcula TODO cada corrida (borra `product_groups`/`item_oracular_map`); idempotente, no destructivo. Las decisiones humanas/LLM viven en `manual_matches` y sobreviven.
- Part number NO es clave única: compatibles de terceros citan el código OEM (cromink "ALT. HP CE320A" ≠ HP). Por eso `audit_group` rechaza grupos con marcas en conflicto.
- EAN: nunca extraer dígitos de un alfanumérico (`BX80768225F` ≠ EAN; la F distingue 225 de 225F).
- `oracular_sku` se deriva del item representante (consenso) + sufijo de unicidad — evita colisiones por un part number mal cargado en origen (caso UPS con part number de CPU).
- Correr siempre `match_products.py` **y luego** `gen_candidates.py` (la cola de curación depende del estado de asignación).

## Próximos pasos posibles

- Alertas de precio: webhook/email cuando `precio_final` baja N% en `price_stock_history`
- Agregar `match_products.py && gen_candidates.py` al cron (después del último sync, ej. 03:45)
- Escalar la curación: limpiar el residuo de clusters caóticos (Raptor) a mano vía `/ui` o `manual_matches` `veredicto='different'`
- **HECHO** ✅ Comparador del mismo producto en N fuentes → `GET /groups/{oracular_sku}`
- **HECHO** ✅ Frontend de comparación + curación → `/ui`

## Credenciales y accesos

- **Invid:** ver `sync_invid.py` (campo `CREDENTIALS`)
- **Stylus:** ver `sync_stylus.py` (campo `CREDENTIALS`)
- **Ceven:** ver `sync_ceven.py` (campo `CREDENTIALS`)
- **PreciosGamer:** API pública, no requiere auth
- **Exchange rates (dolarapi.com):** sin auth requerida

---

## Ver también

- [[BluPartPicker]] — índice del proyecto
- [[arquitectura]] — detalles técnicos
- [[changelog]] — historial completo
- [[resellers]] — auth, formatos y gotchas por fuente
