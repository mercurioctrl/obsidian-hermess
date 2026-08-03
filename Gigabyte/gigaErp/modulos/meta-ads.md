# Módulo Meta Ads (reportes)

Sección **Marketing → Meta Ads**: espejo de [[modulos/google-ads]] para **Facebook/Instagram Ads**. Listado de cuentas y, al entrar, el reporte de cada cuenta **navegable entre fechas** (presets, `SelectorFecha`, flechas ◀▶), con métricas de negocio, gráfico diario y tabla de campañas. Funcionando con **datos reales** desde 2026-08-03; **PR #8** contra `Development`. Deploy en `docs/DEPLOY_META_ADS.md`.

## Decisión de arquitectura

Mismo criterio que Google Ads: **nativo Laravel + Nuxt**, patrón proxy read-only como [[modulos/envios|Envíos]]. Se le pega a la **Marketing API de Meta** (Graph API `graph.facebook.com/vXX/act_<id>/insights`) — sin SDK, sin Python, un solo stack. El reporte se renderiza nativo con el design system.

## Backend

- **`App\Services\MetaAdsService`** — corazón:
  - `graph($path, $params)` / `graphData(...)`: GET al Graph API con el `access_token`.
  - `insights($actId, $params, $desde, $hasta)`: GET a `act_<id>/insights` con `time_range`.
  - `resumen()`: **una** llamada agregada a nivel cuenta (totales, incluye reach/frequency/roas).
  - `serieDiaria()`: insights con `time_increment=1` (Meta arma la serie sola, no hay loop de días).
  - `topCampanias()` + `metaCampanias()`: insights nivel campaña + merge con objetivo/estado/presupuesto.
  - `presupuestoDiario()`: budgets de campañas activas (CBO) + adsets sin budget de campaña. Centavos → /100.
  - `valorAccion($acciones, $tipos)`: extrae el **primer action_type canónico** (clave anti-duplicación).
  - `esDemo()` → fixture determinístico si falta el token.
- **`App\Http\Controllers\MetaAdsController`** — valida el `act_id` contra `meta_ads_cuentas` (no confía en el navegador), resuelve presets → fechas.
- **Rutas** (auth, estáticas): `GET /api/meta-ads/cuentas` · `GET /api/meta-ads/reporte?cid=&desde=&hasta=&preset=`.
- **Config** `services.meta_ads`; migración **0060** `meta_ads_cuentas` + modelo `MetaAdsCuenta`.

## Auth (más simple que Google)

**System User token** de Business Manager: larga duración, **no expira** (salvo revocación), permiso `ads_read`. **Sin refresh_token** — no hay baile OAuth como en Google. Un token accede a todas las cuentas del BM. En `.env`: `META_ADS_ACCESS_TOKEN`, `META_ADS_APP_ID` (647290281668078), `META_ADS_API_VERSION=v21.0`.

## Cuentas (Business Manager de Blu)

| Cuenta | act_id | Moneda |
|--------|--------|--------|
| Gigabyte Argentina | 1922499601658152 | USD |
| Gigabyte Uruguay | 2533454380455971 | USD |
| Gigabyte Chile | 865101106388536 | USD |

El `act_id` se guarda **sin** el prefijo `act_` (se antepone en el service).

## Métricas del reporte

Presupuesto/día · Inversión (+CPC) · Impresiones (+CTR) · **Alcance** · **Frecuencia** · Clics · Agregar al carrito · Compras · Monto de compra · **ROAS** · Costo por compra. Cada tarjeta con ícono **(i)** ([[componentes-ui|StatsCard]] prop `info`). **Alcance, Frecuencia y ROAS son exclusivas de Meta** (Google no las tenía). Tabla de campañas: objetivo, estado, presupuesto, compras, monto.

## ⚠️ Gotchas clave (ver [[troubleshooting#Meta Ads]])

1. **Duplicación de conversiones (idéntico a Google)**: el array `actions` trae la MISMA compra contada ~5 veces (`purchase`, `omni_purchase`, `offsite_conversion.fb_pixel_purchase`, `onsite_web_purchase`, `web_in_store_purchase`, todas mismo valor). Sumar el array multiplica ×5. Se toma **un action_type canónico**: `omni_purchase` (compras/monto) y `omni_add_to_cart` (carritos) — constantes `A_COMPRA`/`A_CARRITO`. Verificado AR: **26 compras / USD 15.072,09** (no 130).
2. **reach/frequency NO son sumables entre días** (reach = únicos deduplicados) → salen de `resumen()` (llamada agregada), nunca de la serie.
3. **Presupuesto en centavos** (`daily_budget` "444" = USD 4,44) → /100.
4. Sin `config:cache` tras cargar el token → sigue en modo demo (gotcha `env()` en PHP-FPM).

## Frontend

`pages/meta-ads/index.vue` (tarjetas de cuenta) + `[cid].vue` (reporte navegable). Sección en `secciones.ts` con permiso `VER_SECCION_META_ADS` (asignable por usuario en Configuración; admin ve todo).

## Pendiente (validar con marketing / Leo Saran)

- Confirmar que **`omni_purchase` / `omni_add_to_cart`** son los eventos que miran en el Administrador de Anuncios (si usan pixel/evento custom, ajustar `A_COMPRA`/`A_CARRITO`).
- **Ventana de atribución**: se usa la default de Meta (7d clic / 1d view); setear `action_attribution_windows` si comparan contra otra.
- Futuro: shell unificado "Reportes de Ads" con pestañas Google/Meta para comparar lado a lado; export PDF.

## Ver también

- [[modulos/google-ads]] — la sección espejo (mismo patrón, API distinta)
- [[modulos/envios]] — mismo patrón proxy read-only a API externa
- [[troubleshooting]] — gotchas de Meta Ads
- [[changelog#2026-08-03 — Sección Meta Ads (reportes)|changelog]]
- [[arquitectura]] — controllers, servicios, rutas
