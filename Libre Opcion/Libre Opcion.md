# Libre Opcion

Diagnóstico, mejoras de SEO/performance, features y landings para libreopcion.com.ar.
Última sincronización: 2026-05-15.

---

## Proyecto

- [[arquitectura|Arquitectura]] — Estructura de componentes, decisiones de diseño, patrones, iframeResizer cleanup
- [[stack|Stack]] — Tecnologías, versiones, servicios externos
- [[changelog|Changelog]] — Registro de trabajo por fecha
- [[memoria|Memoria]] — Consolidación de feedback, reglas y contexto del proyecto

## Herramientas internas

### enviosMailDrop
Script Python para envío masivo de emails HTML. Integración con SQL Server para control de campañas.
- [[enviosMailDrop/enviosMailDrop|enviosMailDrop]] — Índice
- [[enviosMailDrop/arquitectura|Arquitectura]] · [[enviosMailDrop/stack|Stack]] · [[enviosMailDrop/contexto|Contexto]] · [[enviosMailDrop/changelog|Changelog]]

## Wallet & Categorización — API v4

### TareaWallet
Análisis e implementación del módulo de billetera y features relacionadas. Airdrop OpcionFest $15.000 ARS. Sistema de recategorización de productos.
- [[TareaWallet/TareaWallet|TareaWallet]] — Índice
- [[TareaWallet/contexto|Contexto]] — Flujo de ingreso, TR_CODIGO 476, queries, HMAC, análisis recategorización
- [[TareaWallet/arquitectura-recategorizacion|Arquitectura Recategorización]] — Job, CategoriaMatcher, tablas DB, algoritmo propuesto
- [[TareaWallet/changelog|Changelog]] — Historial de cambios recientes (favoritos, cupones, estadísticas, imágenes)

## Landings y campañas MKT

### OpcionFest (activa — rama feat/landing-opcionfest)
Landing de evento e-commerce con hero video, grid de productos curados y precios flash.
- Ruta: `/opcionfest`
- Banner animado en home slider: `SliderHeroOpcionFest.vue`
- Assets: `static/micrositios-files/opcionFest/mkt/sin_borde/`
- CTA externo: https://bit.ly/Opcion_Fest_2026

### ASUS ROG x Resident Evil Requiem
- Ruta: `/asus/rog`
- Rama: `feat/landing-asus-rog-requiem` (mergeada)

### ASUS TUF RX 9070 XT Black Ops 7 Special Edition
- Banner home: `SliderHeroLimitedEdition.vue` — botón "Ver ASUS" → `/asus`
- Activado con `HOME_HERO_BANNER=1` en `.env`
- Bullets estilo Apple activados con `HOME_BANNER_BULLETS_APPLE=1`
- Rama: `LIO-618` (mergeada)

## Fixes recientes

### 2026-05-15 — iframeResizer root cause (commit `5d922efb3`)
Bug crítico resuelto: visitar una ficha con contenido A+ rompía la navegación asincrónica posterior (búsquedas, links, todo dejaba de funcionar hasta F5).

- **Causa raíz**: `disconnect()` borraba el registry `ee[id]` pero no desconectaba el `ResizeObserver` creado por iframeResizer. El observer crasheaba en el siguiente cambio de DOM, propagando un TypeError a `window.onerror` que corrompía el estado de la app.
- **Fix**: despachar `pageInfoStop`/`parentInfoStop` como `MessageEvent` sintéticos antes de `disconnect()`, forzando que el cleanup corra mientras el registry existe.
- Eliminado código muerto `syndicationIframe` (refs a métodos inexistentes).
- Ver [[arquitectura#iframeResizer — Cleanup pattern|Arquitectura]] y [[memoria#Contenido A+ (aplus.libreopcion.com.ar)|Memoria]].

### 2026-05-14 — Fixes UX y slider
- iframeResizer: disconnect, AbortController 3s, timeout CSP, guard `_isDestroyed`
- Bullets slider home: `SliderHeroLimitedEdition` envuelto en `<div>` para Slick
- Banner ASUS: botón "Ver ASUS" + bullets Apple

## SEO & Performance

- [[00-resumen-diagnostico-seo-performance|Resumen del diagnóstico]] — Hallazgos principales y plan de acción
- [[01-fix-cls-imagenes]] — Fix CLS de imágenes sin dimensiones
- [[02-fix-lcp-render-blocking]] — Fix LCP render-blocking
- [[03-fix-header-min-height]] — Fix header sin min-height
- [[04-fix-fuentes-innecesarias]] — Fix fuentes web innecesarias
- [[05-fix-fouc-css-tardio]] — Fix FOUC (flash sin estilos)
- [[06-fix-cls-tbt-ronda-2]] — Ronda 2: CLS + TBT + animaciones no compuestas
- [[07-fix-cls-mobile-h1-sr-only-ronda-3]] — Ronda 3: CLS mobile h1 sr-only
- [[08-fix-cls-listings-ronda-4]] — Ronda 4: CLS listings + Inter font preload

## Tareas

- [[Libre Opcion/tareas/APP - Refactor - Migrar cotización de envíos de API legacy a v4|Migrar cotización de envíos]]
- [[Libre Opcion/tareas/API - Feat - Imágenes personalizadas del reseller por producto|Imágenes personalizadas reseller]]
- [[Libre Opcion/tareas/APP - Feat - Gestión de imágenes del reseller en ficha de producto|Gestión de imágenes reseller (frontend)]]
- [[Libre Opcion/tareas/APP - Fix - Tooltip de codigo postal aparece al cargar el sitio|Fix tooltip código postal]]
- [[Libre Opcion/tareas/API - Refactor - Migrar recurso de preguntas y respuestas a v4|Migrar preguntas y respuestas a v4]]

## Contexto comercial

- [[hot sale]] — Preparación Hot Sale 2026

## Ver también

- [[Libre Opcion/tareas/tareas|tareas]] — Tareas de desarrollo del proyecto [[Libre Opcion/Libre Opcion|Libre Opcion]].
- [[Libre Opcion/sync-curls|Sync Curls — Proceso de sincronización periódica]]
