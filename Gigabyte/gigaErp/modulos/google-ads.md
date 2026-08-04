# Módulo Google Ads (reportes)

Sección **Marketing → Google Ads**: listado de cuentas y, al entrar, el reporte de cada cuenta **navegable entre fechas** (presets, `SelectorFecha` y flechas ◀▶), con métricas de negocio, gráfico diario y tabla de campañas. Funcionando con **datos reales** desde 2026-07-31; mergeado a `Development` (PRs #4/#5/#6, + #7 "Compras sin decimales"). Deploy en `docs/DEPLOY_GOOGLE_ADS.md`.

## Decisión de arquitectura

La guía original (`docs/INTEGRACION_ERP.md.docx`) proponía un microservicio Python (FastAPI) embebido por iframe. **Se descartó**: todo **nativo Laravel + Nuxt**, mismo patrón proxy read-only que [[modulos/envios|Envíos]] y [[modulos/resellers|Resellers]]. Se le pega a la **API REST de Google Ads** (`googleAds:searchStream`, lenguaje **GAQL**) — sin SDK gRPC, sin Python, un solo stack, un solo deploy. El reporte se renderiza nativo con el design system (no iframe).

## Backend

- **`App\Services\GoogleAdsService`** — corazón:
  - `accessToken()`: canjea el refresh token → access token, cacheado en Redis 55 min.
  - `buscar($cid, $gaql, $login)`: POST a `…/customers/{cid}/googleAds:searchStream`, headers `developer-token` + `login-customer-id` (opcional) + Bearer.
  - `reporte()`: serie diaria, top de campañas, presupuesto diario, compras/monto (nivel campaña), carritos. Cache 5 min. `esDemo()` → fixture determinístico si faltan credenciales.
- **`App\Http\Controllers\GoogleAdsController`** — valida el `cid` contra `google_ads_cuentas` (no confía en el navegador), resuelve presets → fechas.
- **Rutas** (auth, estáticas): `GET /api/google-ads/cuentas` · `GET /api/google-ads/reporte?cid=&desde=&hasta=&preset=` (presets `LAST_7_DAYS`/`LAST_30_DAYS`/`THIS_MONTH`/`LAST_MONTH`).
- **Config** `services.google_ads`; migración **0059** `google_ads_cuentas` + modelo `GoogleAdsCuenta`.
- **Script** `backend/scripts/obtener_refresh_token_google_ads.py` — genera el refresh token (OAuth loopback puerto 8765, solo stdlib, cliente Desktop).

## Cuentas (MCC "BLU STUDIO" = 3863921811)

| Cuenta | CID | Moneda | login_customer_id |
|--------|-----|--------|-------------------|
| Gigabyte Argentina | 9373933264 | USD | 3863921811 (MCC) |
| Gigabyte Uruguay | 5837677270 | USD | 3863921811 (MCC) |
| Gigabyte Chile | 9370009552 | USD | 3863921811 (MCC) |

Las cuentas de Gigabyte **cuelgan del MCC**, por eso llevan `login_customer_id`. *Libre Opción* (6794990154, ARS) es de acceso directo (login NULL) — fuera del seed. La columna `login_customer_id` es **por cuenta** (`.env` global vacío). `customer_client` enumera las hijas del MCC; `listAccessibleCustomers` las accesibles.

## Métricas del reporte

Presupuesto/día (total cuenta) · Inversión · Impresiones · Clics · Agregar al carrito (entero) · Compras · Monto de compra · Costo por compra (8 tarjetas). Cada tarjeta tiene un ícono **(i)** con **texto literal del cliente** (prop `info` en [[componentes-ui|StatsCard]], reutilizable). Tabla de campañas: tipo, presupuesto, compras, monto. **Alcance y Frecuencia NO existen en Google** (son de Meta). Se quitaron ROAS y la tabla de Destinos (landing pages) a pedido de marketing (Leo Saran). Ajustes 2026-08-04: se quitaron los sublabels **CPC** (Inversión) y **CTR** (Impresiones) — PR #9; "Agregar al carrito" pasó a **entero**; textos (i) reemplazados por los literales del cliente.

## ⚠️ Gotchas clave (ver [[troubleshooting#Google Ads]])

1. **Compras y Monto de compra = a NIVEL CAMPAÑA** (`metrics.conversions`/`conversions_value`, goal-aware = objetivo custom). Sumar por `conversion_action_category` PURCHASE **duplica** (acciones solapadas: "Compra todos" incluye "GB"+"otros"). Verificado UY: 9.545,27 (correcto) vs 28.977 (duplicado).
2. **`api_version = v22`** (v18 fue sunseteada → 404). Google rota versiones ~1/año.
3. **`login-customer-id` por cuenta / opcional**: forzarlo sobre cuenta de acceso directo → `USER_PERMISSION_DENIED`.
4. Sin `config:cache` tras cargar credenciales → sigue en modo demo (gotcha `env()` en PHP-FPM).

## Frontend

`pages/google-ads/index.vue` (tarjetas de cuenta) + `[cid].vue` (reporte navegable). Sección en `secciones.ts` con permiso `VER_SECCION_GOOGLE_ADS` (asignable por usuario en Configuración; admin ve todo).

## Pendiente

- **Carritos** (ADD_TO_CART vía `all_conversions`) puede duplicar igual que las compras; falta definir la acción de carrito canónica por cuenta con marketing.
- Configurar qué métricas se ven por reporte (UI); export PDF; Meta Ads; total de presupuesto en el índice de cuentas.

## Ver también

- [[modulos/envios]] — mismo patrón proxy read-only a API externa
- [[troubleshooting]] — gotchas de Google Ads
- [[changelog#2026-07-31 — Sección Google Ads (reportes)|changelog]]
- [[arquitectura]] — controllers, servicios, rutas
