# Memoria — BluPartPicker

## Estado actual (2026-06-25)

- **5 mayoristas:** invid, ceven, stylus, nb, air + ~37 resellers preciosgamer_*
- **API v2.3.0** — matching (`oracular_sku`) + curación `/ui` + auth por API Key + Swagger completo
- ~37.9k items agrupados (~63-65%) bajo `oracular_sku`; spec-conflict=0; 10.061 pares en manual_matches
- **Rama activa:** `feat/api-auth` — auth X-Api-Key (tablas `api_keys`/`api_usage`, `/admin/*`), no mergeada a main
- **Para activar auth en producción:** `AUTH_REQUIRED=1` + `ADMIN_KEY=<secret>` en el env del servicio systemd
- Syncs en cron; **matching sin cron** — cron sugerido en `docs/runbook.md` §4 listo para pegar

> Estado 2026-06-18: API v2.2.0, matching completo pero sin auth.
> Estado 2026-06-04: 4 fuentes (sin nb/air), API v2.1.0, sin matching ni frontend.

## Gotchas activos

- La DB se llama `invid.db` — herencia del primer distribuidor, no renombrar (rompe paths)
- **PreciosGamer source:** formato `preciosgamer_{slug}` — ej: `preciosgamer_venex`, `preciosgamer_libre-opcion`. NO es el resellerId numérico (ya migrado).
- **PreciosGamer modelo:** DELETE + INSERT en cada sync. No hay "actualizados", siempre son "nuevos". La tabla muestra solo los items actualizados en las últimas 48h.
- El oráculo de marcas usa qty≥2 — marcas con 1 sola ocurrencia se ignoran como ruido
- Playwright solo para Ceven; Akamai bloquea cualquier intento con requests/curl
- **Invid moneda:** el Excel devuelve `"US$"`, no `"USD"` — siempre normalizar en `parse_excel()`. La expresión SQL usa `moneda = 'USD'` exacto.
- Los precios en la API están en moneda original. Para comparar USD vs ARS usar `moneda_out`; sin eso `precio_final` es el valor crudo de cada fuente.
- **Ceven credenciales:** el distribuidor las rota sin aviso → login falla con "correo/contraseña incorrectos" y el script corta con Timeout. Última rotación 2026-07-17. Ver [[resellers#Ceven]].
- **Ceven loop de categorías:** sin retry — un `Failed to fetch` transitorio (throttling Akamai) aborta todo el sync y descarta los items ya bajados. Reintento manual suele pasar.
- Ceven puede tener timeouts de login transitorios — si falla en cron, correr manual primero para confirmar que el sitio esté operativo (y descartar credenciales rotadas).

### Matching (`oracular_sku`) — ver [[matching-productos]]
- `match_products.py` recalcula TODO cada corrida (borra `product_groups`/`item_oracular_map`); idempotente, no destructivo. Las decisiones humanas/LLM viven en `manual_matches` y sobreviven.
- Part number NO es clave única: compatibles de terceros citan el código OEM (cromink "ALT. HP CE320A" ≠ HP). Por eso `audit_group` rechaza grupos con marcas en conflicto.
- EAN: nunca extraer dígitos de un alfanumérico (`BX80768225F` ≠ EAN; la F distingue 225 de 225F).
- `oracular_sku` se deriva del item representante (consenso) + sufijo de unicidad — evita colisiones por un part number mal cargado en origen (caso UPS con part number de CPU).
- Correr siempre `match_products.py` **y luego** `gen_candidates.py` (la cola de curación depende del estado de asignación).

## Próximos pasos posibles

- **Ceven:** agregar retry con backoff al loop de categorías para que un `Failed to fetch` transitorio no tumbe todo el sync. Considerar mover credenciales a env vars (`CEVEN_EMAIL`/`CEVEN_PASSWORD`) para no editar código en cada rotación.
- **Mergear `feat/api-auth` a main** y configurar `AUTH_REQUIRED=1` + `ADMIN_KEY` en producción
- **Agregar cron del matching** (comando listo en `docs/runbook.md` §4): `45 23 * * * cd /var/www/blupartpicker && python3 match_products.py >> match_products.log 2>&1 && python3 gen_candidates.py >> gen_candidates.log 2>&1`
- Alertas de precio: webhook/email cuando `precio_final` baja N% en `price_stock_history`
- Escalar la curación: limpiar residuo de clusters caóticos (Raptor) via `/ui` o `manual_matches veredicto='different'`
- **HECHO** ✅ Auth por API Key con gestión de usuarios y tracking de consumo
- **HECHO** ✅ Swagger v2.3.0 completamente documentado (tags, security scheme, responses)
- **HECHO** ✅ Runbook de producción en `docs/runbook.md`
- **HECHO** ✅ Comparador del mismo producto en N fuentes → `GET /groups/{oracular_sku}`
- **HECHO** ✅ Frontend de comparación + curación → `/ui`

## Credenciales y accesos

- **Invid:** ver `sync_invid.py` (campo `CREDENTIALS`)
- **Stylus:** ver `sync_stylus.py` (campo `CREDENTIALS`)
- **Ceven:** ver `sync_ceven.py` (`EMAIL`/`PASSWORD`, líneas 22-23). Rotadas 2026-07-17 → `jdebello@nb.com.ar`. El distribuidor las cambia sin aviso.
- **PreciosGamer:** API pública, no requiere auth
- **Exchange rates (dolarapi.com):** sin auth requerida

---

## Ver también

- [[BluPartPicker]] — índice del proyecto
- [[arquitectura]] — detalles técnicos
- [[matching-productos]] — matching de `oracular_sku` y curación
- [[changelog]] — historial completo
- [[resellers]] — auth, formatos y gotchas por fuente
