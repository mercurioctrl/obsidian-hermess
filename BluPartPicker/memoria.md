# Memoria — BluPartPicker

## Estado actual (2026-06-04)

- **4 fuentes:** invid, ceven, stylus, preciosgamer_* (37 resellers)
- **147.673 productos** en total — 2.565 mayoristas + 145.108 resellers
- **API v2.1.0** — conversión de precios en tiempo real con tipos de cambio
- Todos los syncs con cron cada 4h, desfasados hora por hora (0, 1, 2, 3)
- Exchange rates: cada 30 min desde dolarapi.com

## Gotchas activos

- La DB se llama `invid.db` — herencia del primer distribuidor, no renombrar (rompe paths)
- PreciosGamer: `source = preciosgamer_{resellerId}`, no por nombre de tienda
- El oráculo de marcas usa qty≥2 — marcas con 1 sola ocurrencia se ignoran como ruido
- Playwright solo para Ceven; nunca intentar mover las llamadas a requests
- **Invid moneda:** el Excel devuelve `"US$"`, no `"USD"` — siempre normalizar en `parse_excel()`. El CASE en la API usa `moneda = 'USD'` exacto; si llega `"US$"` la conversión falla silenciosamente.
- Los precios en la API están en moneda original (`moneda` field). Para comparar USD vs ARS necesitar pasar `moneda_out`; sin eso `precio_final` es el valor crudo de cada fuente.

## Próximos pasos posibles

- Alertas de precio: webhook/email cuando `precio_final` baja N% en `price_stock_history`
- Endpoint `/items/comparar?codigo=X` — mismo producto en múltiples fuentes
- Frontend mínimo de comparación de precios
- Scrapear categorías de PreciosGamer si la API las expone en otro endpoint

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
