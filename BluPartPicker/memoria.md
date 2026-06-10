# Memoria — BluPartPicker

## Estado actual (2026-06-04)

- **4 fuentes:** invid, ceven, stylus, preciosgamer_* (37 resellers)
- **~10k productos activos de PreciosGamer** (últimas 48h) + 2.565 mayoristas
- **API v2.1.0** — conversión de precios en tiempo real con tipos de cambio
- Todos los syncs con cron: invid cada 4h, ceven/stylus/preciosgamer cada 4h desfasados, exchange rates cada 30 min

## Gotchas activos

- La DB se llama `invid.db` — herencia del primer distribuidor, no renombrar (rompe paths)
- **PreciosGamer source:** formato `preciosgamer_{slug}` — ej: `preciosgamer_venex`, `preciosgamer_libre-opcion`. NO es el resellerId numérico (ya migrado).
- **PreciosGamer modelo:** DELETE + INSERT en cada sync. No hay "actualizados", siempre son "nuevos". La tabla muestra solo los items actualizados en las últimas 48h.
- El oráculo de marcas usa qty≥2 — marcas con 1 sola ocurrencia se ignoran como ruido
- Playwright solo para Ceven; Akamai bloquea cualquier intento con requests/curl
- **Invid moneda:** el Excel devuelve `"US$"`, no `"USD"` — siempre normalizar en `parse_excel()`. La expresión SQL usa `moneda = 'USD'` exacto.
- Los precios en la API están en moneda original. Para comparar USD vs ARS usar `moneda_out`; sin eso `precio_final` es el valor crudo de cada fuente.
- Ceven puede tener timeouts de login transitorios — si falla en cron, correr manual primero para confirmar que el sitio esté operativo.

## Próximos pasos posibles

- Alertas de precio: webhook/email cuando `precio_final` baja N% en `price_stock_history`
- Endpoint `/items/comparar?codigo=X` — mismo producto en múltiples fuentes
- Frontend mínimo de comparación de precios

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
