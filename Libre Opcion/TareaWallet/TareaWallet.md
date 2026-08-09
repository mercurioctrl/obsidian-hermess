# TareaWallet — Libre Opción API v4 + Frontend

Documentación de análisis e implementación de features en la API Laravel v4 y frontend Nuxt.js del marketplace Libre Opción.

## Notas

- [[changelog]] — Historial de cambios por fecha
- [[contexto]] — Decisiones de sesión, gotchas, flujos técnicos importantes
- [[entorno-local]] — Setup local del stack (v3+v4+front), dependencia login v4→v3, gotchas Docker/OPcache, CORS
- [[tiendas-oficiales]] — Módulo OfficialStore: branding CMS, scoping por marca, reemplazo de identidad en ficha
- [[arquitectura-recategorizacion]] — Sistema de recategorización de productos (Job, Matcher, DB tables)
- [[calificaciones-vendedor]] — Reseñas del vendedor: endpoints, validación principal y script de verificación

## Resumen por área

### Entorno local — v3 + v4 + front (2026-08-06)
Setup del stack en local sobre rama `blu-dev-staff`.
- El login de la v4 (`POST /v4/auth/login`) **depende de la API v3**: `loginV3` hace `curl` server-side; si la v3 no responde → 500 (`json_decode(false)`). No es CORS.
- Se levantó la v3 legacy en local (`lo-website-api-rest`, 8081) con `docker-compose.yml` propio (`name: lo-api-rest-v3`, red de la v4).
- Fix clave: `API_V3_URL=http://lo-website-api-rest` (nombre de contenedor, no `localhost`, porque la llamada es server-side desde el contenedor v4).
- Gotchas: colisión de nombre de proyecto compose con `nb-api-rest`; recargar php-fpm tras cambiar `.env` (OPcache). CORS ya estaba en wildcard.
- Detalle en [[entorno-local]]

### Tiendas Oficiales (2026-08-04)
Módulo `OfficialStore` — LIO-720/769/771/772/776.
- `GET /v4/tienda-oficial/{slug}` (público) devuelve branding cargado en CMS (colores, fuentes, banners, secciones hero/video, menús)
- Tablas nuevas `official_store_branding` (+`_banners`) vinculan `seller_id` ↔ `brand_id`
- Ficha de producto: reemplaza el nombre del vendedor por "Tienda oficial {name}" y bloquea su reputación
- Inventario del seller scopeado a la marca de su tienda (`OfficialStoreInventoryScopeService`, 403/404)
- Detalle en [[tiendas-oficiales]]

### Calificaciones del vendedor (2026-07-30)
Verificación de la "Validación principal" del endpoint de reseñas.
- Script de caja negra `scripts/verify-calification-reviews.sh` (curl + jq)
- **Bug abierto:** `pagination.total` sobrecuenta — `countCalificaciones` no aplica los filtros del SELECT de `data`
- Detalle en [[calificaciones-vendedor]]

### Pasarelas de pago (2026-06-07)
Integración de MODO, GetNet y Payway en el checkout.
- MODO QR operativo en sandbox (`ecommerce-modal.preprod.modo.com.ar`)
- Fix crítico en [[contexto#2026-06-07]]: `medioPagoId` sobreescrito por `ACTUALIZAR_PEDIDO` en Vuex
- Fix crítico: OPcache PHP-FPM cachea rutas — reiniciar contenedor tras agregar rutas nuevas

### Recategorización (2026-05-12)
- Review de rama LIO-630 (Franco): concurrencia, restricción stock
- Ver [[arquitectura-recategorizacion]] para diseño DB-driven propuesto

### Wallet / Airdrop (2026-05-11)
- Análisis flujo wallet (TR_CODIGO 475/476, HMAC SHA256)
- Diseño airdrop OpcionFest $15.000 ARS — queries y lógica en [[contexto#2026-05-11]]

## Última sincronización

2026-08-09
