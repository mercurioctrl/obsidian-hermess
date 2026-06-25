# Contexto — BluPartPicker

## Por qué existe

Proyecto propio para consolidar catálogos de distribuidores mayoristas y resellers de tecnología argentina en una sola API. Permite comparar precios, stock e imágenes entre fuentes sin entrar a cada portal por separado.

## Fuentes integradas

**Mayoristas** (`distribuidor=1`) — precios USD:
- **Invid Computers** — catálogo vía Excel autenticado + scraping imágenes
- **Ceven** — plataforma NetSuite SCA protegida por Akamai → requiere Playwright
- **Stylus S.A.** — listas de precios por marca en TSV

**Resellers** (`distribuidor=0`) — precios ARS:
- **PreciosGamer** — API que agrega 37 tiendas (`preciosgamer_{resellerId}`)
- Incluye: Libre Opcion, Full h4rd, Armytech, Venex, Ignatech, Katech, Shopgamer, etc.

## Casos de uso

- Buscar el precio más bajo de un producto entre distribuidores y tiendas
- Ver historial de variación de precios y stock
- Filtrar por categoría o marca desde una sola API
- Comparar precios mayoristas (USD) y resellers (ARS) en la misma moneda
- Base para futuros desarrollos (comparadores, alertas de precio, etc.)

## Decisiones de diseño

- **SQLite** en vez de Postgres: suficiente para el volumen (~147k items), sin overhead de servidor. WAL mode para reads concurrentes durante syncs.
- **Un solo archivo DB** (`invid.db`) aunque el nombre sea de Invid — herencia del primer sync; renombrar rompería todos los paths.
- **`source + codigo`** como clave compuesta — permite múltiples fuentes con el mismo código.
- **`distribuidor`** distingue mayoristas (1) de resellers (0) — permite filtrar tipos de precio.
- **price_stock_history**: snapshots solo cuando hay cambios reales (no en cada sync).
- **Playwright solo para Ceven**: los otros no tienen bot protection (Akamai bloqueó todos los intentos con requests/curl).
- **Categoría inferida** para PreciosGamer: la API no la expone, se extrae de la primera palabra de la descripción.
- **Oráculo de marcas**: en vez de una lista hardcodeada, usa las marcas ya presentes en el repositorio como fuente de verdad — se auto-mejora con cada sync de distribuidores.
- **Tipos de cambio propios**: tabla `exchange_rates` actualizada cada 30 min desde dolarapi.com. La API usa `mayorista.venta` por default — es el TC más representativo para importadores argentinos.
- **Conversión inline SQL**: no hay lógica en Python para conversión de moneda — la expresión `CASE WHEN moneda='USD'` se inyecta directamente en el SELECT. Sin joins, sin overhead.
- **Caché en memoria**: dict con TTL por worker uvicorn — evita GROUP BY costosos en 147k rows para cada request de `/categorias` o `/fabricantes`.

## Estado actual (jun 2026)

- 5 mayoristas + 37 resellers vía PreciosGamer activos
- ~159.050 productos totales (13.942 mayoristas + 145.108 resellers)
- API en https://partpicker.blustudioinc.com (Apache reverse proxy → :4444), docs en `/docs`
- Syncs automáticos cron, desfasados; matching NO está en cron todavía (se corre a mano)
- Exchange rates actualizados cada 30 min
- **Auth:** rama `feat/api-auth` lista, no mergeada a main. Para activar: `AUTH_REQUIRED=1` + `ADMIN_KEY` en el env del servicio.

## Decisiones recientes (jun 2026)

- **Auth por API Key** (no OAuth): mínima fricción, sin DB externa. `active=0` corta el acceso en el request (303). Plan es campo libre, no hay quota hardcodeada en el servidor.
- **Log de usage async**: escribir cada request a SQLite bloquearía bajo carga → queue asyncio con flush cada 5s en background.
- **`AUTH_REQUIRED=0` por default**: el deploy existente no se rompe hasta que se configure explícitamente.
- **SQLite sigue siendo suficiente**: WAL mode maneja lecturas concurrentes bien. El cuello de botella potencial (writes de usage) está mitigado con el batch async. Migrar a Postgres cuando haya 20+ usuarios activos simultáneos con requests frecuentes.

---

## Ver también

- [[BluPartPicker]] — índice del proyecto
- [[arquitectura]] — decisiones técnicas detalladas
- [[changelog]] — historial de lo implementado
- [[memoria]] — próximos pasos y gotchas activos
