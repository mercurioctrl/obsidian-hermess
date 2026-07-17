# Libre Opcion

Diagnóstico, mejoras de SEO/performance, features y landings para libreopcion.com.ar.
Última sincronización: 2026-07-02.

---

## Proyecto

- [[arquitectura|Arquitectura]] — Checkout integrado (MP/GetNet/Payway/MODO), iframeResizer, banners
- [[stack|Stack]] — Tecnologías, versiones, servicios externos
- [[changelog|Changelog]] — Registro de trabajo por fecha
- [[memoria|Memoria]] — Consolidación de feedback, reglas y contexto del proyecto (frontend + backend gotchas)

## Backend API v4 (sitio-api-rest-v4-laravel)

PHP 8.3 + Laravel 10, Docker, SQL Server remoto. Patrón Controller → Service → Repository con SQL crudo.

- **SyncUp items** (`POST`/`PATCH /v4/syncUp/items`) — sincroniza el catálogo al motor de búsqueda; lo llama PEGA cada hora. Fix 2026-06-12: dedupe en los MERGE + logging en controllers. Ver [[changelog#2026-06-12|Changelog 2026-06-12]] y [[memoria#Backend API v4 — Gotchas|Memoria § Backend gotchas]].
- **Gotcha OPcache**: tras editar PHP hay que recargar php-fpm (`kill -USR2`) y verificar por HTTP, no por tinker. Detalle en [[memoria#OPcache validate_timestamps=Off — el código editado no se aplica a requests web|Memoria]] y [[TareaWallet/contexto#2026-06-07|TareaWallet/contexto]].

## Pasarelas de pago (en desarrollo)

Checkout con formulario embebido para múltiples proveedores. Ver [[arquitectura#Pasarelas de pago — Checkout integrado|Arquitectura § Pasarelas]].

| ID | Proveedor | Estado |
|---|---|---|
| 5076 | MercadoPago | ✅ Producción |
| 5077 | GetNet by Santander | ⚠️ Bloqueado (IP whitelist pendiente Santander) |
| 5078 | Payway | 🔧 Implementado, pendiente test navegador |
| 5079 | MODO | ✅ QR operativo en sandbox (2026-06-07) |

**Pendiente:** Contactar Santander para habilitar IP `190.189.93.116` en sandbox GetNet.

## Herramientas internas

### enviosMailDrop
Script Python para envío masivo de emails HTML. Integración con SQL Server para control de campañas.
- [[enviosMailDrop/enviosMailDrop|enviosMailDrop]] — Índice
- [[enviosMailDrop/arquitectura|Arquitectura]] · [[enviosMailDrop/stack|Stack]] · [[enviosMailDrop/contexto|Contexto]] · [[enviosMailDrop/changelog|Changelog]]

## Wallet & Categorización — API v4

### TareaWallet
Análisis e implementación del módulo de billetera y features relacionadas. Integración pasarelas de pago checkout. Airdrop OpcionFest $15.000 ARS. Sistema de recategorización de productos.
- [[TareaWallet/TareaWallet|TareaWallet]] — Índice
- [[TareaWallet/contexto|Contexto]] — MODO QR fix, OPcache gotcha, flujo wallet, TR_CODIGO 476, queries, HMAC
- [[TareaWallet/changelog|Changelog]] — Historial por fecha
- [[TareaWallet/arquitectura-recategorizacion|Arquitectura recategorización]]

## SEO y Performance

Diagnóstico y fixes de Core Web Vitals para libreopcion.com.ar.
- [[Libre Opcion/00-resumen-diagnostico-seo-performance|Diagnóstico SEO y Performance]] — resumen ejecutivo
- [[Libre Opcion/01-fix-cls-imagenes|01 — Fix CLS imágenes]]
- [[Libre Opcion/02-fix-lcp-render-blocking|02 — Fix LCP render blocking]]
- [[Libre Opcion/03-fix-header-min-height|03 — Fix header min-height]]
- [[Libre Opcion/04-fix-fuentes-innecesarias|04 — Fix fuentes innecesarias]]
- [[Libre Opcion/05-fix-fouc-css-tardio|05 — Fix FOUC CSS tardío]]
- [[Libre Opcion/06-fix-cls-tbt-ronda-2|06 — Fix CLS/TBT ronda 2]]
- [[Libre Opcion/07-fix-cls-mobile-h1-sr-only-ronda-3|07 — Fix CLS mobile H1 sr-only ronda 3]]
- [[Libre Opcion/08-fix-cls-listings-ronda-4|08 — Fix CLS listings ronda 4]]

## Tareas de desarrollo

- [[Libre Opcion/tareas/tareas|Tareas]] — backlog de desarrollo del proyecto

## Estrategia comercial

- [[Libre Opcion/Gestion X/00 - Índice Gestión X|Gestión X]] — documentación estratégica (diagnóstico, hoja de ruta, posicionamiento, 19 docs)
  - [[Libre Opcion/Gestion X/01 - Estudio de Mercado - Referentes|01 · Estudio de Mercado — Referentes]]
  - [[Libre Opcion/Gestion X/02 - Hoja de Ruta - Fase 1 Diferenciación y Confianza|02 · Fase 1 — Diferenciación y Confianza]]
  - [[Libre Opcion/Gestion X/03 - Hoja de Ruta - Fase 2 Rentabilización y Profundidad|03 · Fase 2 — Rentabilización y Profundidad]]
  - [[Libre Opcion/Gestion X/04 - Hoja de Ruta - Fase 3 Escala y Plataforma|04 · Fase 3 — Escala y Plataforma]]
  - [[Libre Opcion/Gestion X/05 - Roles por Fase|05 · Roles por Fase]]
  - [[Libre Opcion/Gestion X/06 - Ventajas Competitivas y Posicionamiento|06 · Ventajas Competitivas y Posicionamiento]]
  - [[Libre Opcion/Gestion X/07 - Idea Hunnox - Marca propia Smart Home|07 · Idea Hunnox — Marca propia Smart Home]]
  - [[Libre Opcion/Gestion X/08 - Detección de Tendencias - Método y Herramientas|08 · Detección de Tendencias — Método y Herramientas]]
  - [[Libre Opcion/Gestion X/09 - Estudio de Catálogo - Compra Gamer|09 · Estudio de Catálogo — Compra Gamer]]
  - [[Libre Opcion/Gestion X/10 - Reposicionamiento - De Precio a Confianza|10 · Reposicionamiento — De Precio a Confianza]]
  - [[Libre Opcion/Gestion X/11 - Estrategia de Cuotas y Precio|11 · Estrategia de Cuotas y Precio]]
  - [[Libre Opcion/Gestion X/12 - Modelo Operativo - Importador-Mayorista con Red de Vendedores|12 · Modelo Operativo — Importador-Mayorista con Red de Vendedores]]
  - [[Libre Opcion/Gestion X/13 - El Verdadero Cuello de Botella es la Demanda|13 · El Verdadero Cuello de Botella es la Demanda]]
  - [[Libre Opcion/Gestion X/14 - Liquidacion de Aging como Motor de Demanda|14 · Liquidación de Aging como Motor de Demanda]]
  - [[Libre Opcion/Gestion X/15 - Plan de Accion - Proximos 6 Meses|15 · Plan de Acción — Próximos 6 Meses]]
  - [[Libre Opcion/Gestion X/16 - Armador, Combos Dinamicos y Builds de la Comunidad|16 · Armador, Combos Dinámicos y Builds de la Comunidad]]
  - [[Libre Opcion/Gestion X/17 - Exclusivas - Marcas Conocidas que Nadie Trae|17 · Exclusivas — Marcas Conocidas que Nadie Trae]]
  - [[Libre Opcion/Gestion X/18 - Analisis Performance Ventas 12 Meses (FODA)|18 · Análisis de Performance de Ventas — 12 Meses (FODA)]]
  - [[Libre Opcion/Gestion X/19 - Politica de Envios|19 · Política de Envíos]]
  - [[Libre Opcion/Gestion X/Informe Diagnostico Conversion - Mayo 2026|Informe de diagnóstico de conversión — Mayo 2026]]
  - [[Libre Opcion/Gestion X/combos-armables|Combos y PCs armables con tu catálogo (vs Compra Gamer)]]
  - [[Libre Opcion/Gestion X/arquitectura|Arquitectura — pipelines de datos y entregables]]
  - [[Libre Opcion/Gestion X/contexto|Contexto — orígenes de datos, forecast y decisiones]]
  - [[Libre Opcion/Gestion X/memoria|Memoria operativa]] · [[Libre Opcion/Gestion X/changelog|Changelog]]

## Mini-juegos

### shoppingAndGoblins
Mini-juego *endless runner* (Grinch/Goblin) para activación de marca. HTML5 Canvas en un único archivo, sin dependencias. Repo: `git@github.com:BluIncStudio/miniJuegos-shoppingAndGoblins.git`.
- [[shoppingAndGoblins/shoppingAndGoblins|shoppingAndGoblins]] — Índice del juego (LIBRE RUN)

### Penales
Banner jugable "Penales Mundial 2026" en el home, con ranking. Microsite Canvas en iframe (front) + API v4 (back), con token one-time-use y firma HMAC.
- [[Penales/Penales|Penales]] — Índice del juego
- [[Penales/arquitectura|Arquitectura]] · [[Penales/contexto|Contexto]] · [[Penales/changelog|Changelog]]

## Otras notas

- [[Libre Opcion/hot sale|Hot Sale 2026]] — ideas de landing pages
- [[Libre Opcion/sync-curls|Sync Curls]] — proceso de sincronización periódica
