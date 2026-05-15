# Changelog

Registro de trabajo en el proyecto Libre Opción.

---

## 2026-04-16

### Rama: LIO-618 (hero limited edition BO7 + tienda oficial ASUS)

- **merge**: Resueltos conflictos entre `LIO-618` y `development` en `SliderTienda.vue` y `officialStores.js`
- **fix**: Agregada variable `PRODUCT_IDS` al `.env` (4 IDs de GPU TUF BO7) para que el CTA random funcione
- **feat**: Centrado del hero banner en home — `justify-content: center` con `gap: 64px` (antes `space-between` empujaba copy y producto a extremos)
- **feat**: Variante `compact` en `SliderHeroLimitedEdition` para tienda oficial — reduce títulos, producto, botones y gaps ~30% proporcionalmente al banner más angosto

Archivos: `components/Home/Banners/SliderHeroLimitedEdition.vue`, `pages/busquedas/partials/SliderTienda.vue`, `storeConfig/officialStores.js`

---

## 2026-04-08

### API v4 — Nuevas features y migraciones (múltiples PRs)

- **feat**: Imágenes personalizadas del reseller por producto (LIO-598, PR #574)
- **feat**: Features de cuenta mobile — `GET /account/lo/features/{id_lo}` (PR #570)
- **feat**: Estado de verificación de teléfono de vendedor (PR #562)
- **refactor**: Migración resumen pedidos por mes/año a Laravel (PR #576)
- **fix**: Estadísticas referidos — división por cero + tipos de datos (PR #572, #578)

---

## 2026-04-10

### Rama: feat/landing-asus-rog-requiem

- Fix CTAs hero /asus/rog descentrados en mobile
- Add CTAs canjear/bases en /asus/rog + bullets left-align mobile
- Add badge envío gratis + 3 mothers ASUS

---

## 2026-04-05 – 2026-04-08

### SEO / Performance (múltiples ramas)

- Fix CLS listings + Inter font preload + display:optional
- Fix CLS mobile: inline style en h1 sr-only + width/height en pin envíos
- Fix CLS/TBT desktop: width/height en imgs, box-shadow fuera de %transition
- Lazy-load Firebase SDK (–196KB del vendor bundle)
- Preload dinámico de imagen del banner principal (LCP)

---

## 2026-05-07

### Historias técnicas

- **docs**: Historia técnica migración `/favoritos` de API v3 a v4
  - 5 endpoints, tabla `[LO].[dbo].[favoritos]`, sin migración de DB

---

## 2026-05-10 / 2026-05-13

### Rama: feat/landing-opcionfest

- **feat**: Landing `/opcionfest` completa — hero video bg, grid 15 productos curados, countdown, sección flash lazy
- **feat**: Timer visual en cards flash (solo landing) — barra de progreso con tiempo transcurrido/restante. Prop `timerBarMode` en `ProgresoInstantFlash.vue`
- **fix**: Hero mobile: `height: auto`, beneficios alineados con `width: fit-content; margin: 0 auto`, scroll suave a `#productos` con `scrollIntoView` (evita router de Nuxt)
- **fix**: Slick slider: componentes Vue envueltos en `<div>` para ser contados como slides
- **feat**: 6 productos nuevos al inicio de la grilla: PS5, Nintendo Switch 2, 3 TVs Samsung, Monitor LG
- Archivos: `pages/opcionfest.vue`, `components/Productos/ProgresoInstantFlash.vue`, `components/Home/Banners/SliderPrincipal.vue`

---

## 2026-05-14

### Rama: development — Fixes de producción y UX

- **fix**: [[changelog#iframeResizer cleanup|iframeResizer]] en ficha de producto (`pages/producto/_id.vue`):
  - `disconnect()` en `beforeDestroy` para limpiar registry global — sin esto al navegar quedaban referencias colgantes que rompían búsquedas y navegación asincrónica
  - AbortController con timeout 3s en `checkAPlusContent` — evita que fetch colgado bloquee todo el watch handler
  - Timeout 5s para ocultar iframe si CSP `frame-ancestors` lo bloquea (caso localhost)
  - Guard `_isDestroyed` en todos los seteos de estado reactivo asincrónico
- **fix**: Bullets slider home — `SliderHeroLimitedEdition` envuelto en `<div>` dentro de Carousel para que Slick lo cuente como slide. Antes solo aparecían 2 bullets
- **feat**: Banner animado ASUS — botón "Tienda Oficial" → "Ver ASUS" con link a `/asus`
- **feat**: `HOME_BANNER_BULLETS_APPLE=1` agregado al `.env` — activa bullets estilo Apple (círculos blancos a la derecha en desktop)

Archivos: `pages/producto/_id.vue`, `components/Home/Banners/SliderPrincipal.vue`, `components/Home/Banners/SliderHeroLimitedEdition.vue`

---

## 2026-05-15

### Rama: development — Fix root cause iframeResizer (navegación rota)

- **fix**: Causa raíz del bug "navegación asincrónica se rompe después de visitar ficha con A+" (`pages/producto/_id.vue`, commit `5d922efb3`)

  **Mecanismo descubierto:** cuando el iframe A+ carga en producción, la librería child de iframeResizer v5.5.9 envía mensajes `pageInfo`/`parentInfo` que provocan que la función interna `w()` cree un `ResizeObserver` sobre `document.body` (subtree). Al navegar, `disconnect()` → `Le()` borra `ee[id]` del registry, pero el ResizeObserver sigue activo. En el siguiente cambio de DOM (Vue desmontando el componente), el observer dispara, detecta que `ee[id]` no existe, llama `l()` para limpiarse, y `l()` crashea en `ee[c].iframe` (TypeError). El error llega a `window.onerror` → `chunk-reload.client.js` → `originalOnError` → corrompía navegación.

  **Fix:** despachar `pageInfoStop` y `parentInfoStop` como `MessageEvent` sintéticos ANTES de llamar `disconnect()`, para que `l()` corra mientras `ee[id]` existe y desconecte los ResizeObservers limpiamente.

- **fix**: Eliminado código muerto `syndicationIframe` (desktop + mobile) que referenciaba métodos/variables inexistentes en el script (`onSyndicationIframeLoad`, `limitedEditionSyndicatedContentSrc`, `syndicationIframeHeight`)

- **feat**: Almacenamiento de referencia directa al iframe en `_aPlusIframeEl` (no reactivo, prefijo `_`) para que `beforeDestroy` pueda acceder al elemento aunque `$refs.aplusIframe` ya sea null (pasa cuando el timer de 5s ejecuta antes de la destrucción)

Ver [[arquitectura#iframeResizer — Cleanup pattern|Arquitectura]] y [[memoria#Contenido A+ (aplus.libreopcion.com.ar)|Memoria]].

## Ver también

- [[arquitectura|Arquitectura]]
- [[stack|Stack]]
- [[memoria|Memoria]]
