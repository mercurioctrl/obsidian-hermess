# Libre Opcion

Diagnóstico, mejoras de SEO/performance, features y landings para libreopcion.com.ar.
Última sincronización: 2026-06-07.

---

## Proyecto

- [[arquitectura|Arquitectura]] — Checkout integrado (MP/GetNet/Payway/MODO), iframeResizer, banners
- [[stack|Stack]] — Tecnologías, versiones, servicios externos
- [[changelog|Changelog]] — Registro de trabajo por fecha
- [[memoria|Memoria]] — Consolidación de feedback, reglas y contexto del proyecto

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

## Otras notas

- [[Libre Opcion/hot sale|Hot Sale 2026]] — ideas de landing pages
- [[Libre Opcion/sync-curls|Sync Curls]] — proceso de sincronización periódica
