# Memoria — BluPartPicker

## Estado actual (2026-06-04)

- **4 fuentes:** invid, ceven, stylus, preciosgamer_* (37 resellers)
- **147.673 productos** en total — 2.565 mayoristas + 145.108 resellers
- **API v2.0.0** — filtros por `categoria`, `fabricante`, `distribuidor`; endpoints `/categorias` y `/fabricantes`
- Todos los syncs con cron cada 4h, desfasados hora por hora (0, 1, 2, 3)

## Gotchas activos

- La DB se llama `invid.db` — herencia del primer distribuidor, no renombrar (rompe paths)
- PreciosGamer: `source = preciosgamer_{resellerId}`, no por nombre de tienda
- El oráculo de marcas usa qty≥2 — marcas con 1 sola ocurrencia se ignoran como ruido
- Playwright solo para Ceven; nunca intentar mover las llamadas a requests

## Próximos pasos posibles

- Indexar `(source, categoria)` y `(source, fabricante)` para queries más rápidas en la API con 147k items
- Alertas de precio: webhook/email cuando `precio_final` baja N% en `price_stock_history`
- Endpoint `/items/comparar?codigo=X` — mismo producto en múltiples fuentes
- Scrapear categorías de PreciosGamer si la API las expone en otro endpoint
- Frontend mínimo de comparación de precios

## Credenciales y accesos

- **Invid:** ver `sync_invid.py` (campo `CREDENTIALS`)
- **Stylus:** ver `sync_stylus.py` (campo `CREDENTIALS`)
- **Ceven:** ver `sync_ceven.py` (campo `CREDENTIALS`)
- **PreciosGamer:** API pública, no requiere auth

---

## Ver también

- [[BluPartPicker]] — índice del proyecto
- [[arquitectura]] — detalles técnicos
- [[changelog]] — historial completo