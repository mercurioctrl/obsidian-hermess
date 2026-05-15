# Memoria del proyecto

Consolidación de la memoria de Claude para Libre Opcion (sitio-web-app-v3).
Última sincronización: 2026-05-15.

---

## Usuario

- Dev fullstack, e-commerce, enfocado en SEO/performance y marketing digital

## Feedback (reglas de trabajo)

- **No autoría**: Nunca agregar Co-Authored-By en commits
- **Build local**: Secuencia OBLIGATORIA: `npm ci` → `npm run build` → `pm2 restart WebAppLO`. Sin `npm ci` el build falla o produce resultados incorrectos
- **Rama activa**: `development` (el usuario trabaja aquí en local, `master` es producción)
- **Sass mixed-decls**: Declaraciones planas SIEMPRE antes de bloques anidados
- **Animaciones**: Pedir referencia visual antes de implementar (no asumir)
- **PNG con canvas**: PNGs con canvas transparente engañan heights CSS, usar negative margins
- **Iframes**: No usar para micrositios (rompen print/PDF), inlinear como Vue
- **Placeholders vacíos**: Si falta asset, eliminar la sección
- **Flex centering**: `width:100%` + `max-width` sin `margin:0 auto` en flex column no centra
- **Slick carousel + Vue**: Siempre envolver componentes Vue en `<div>` dentro del Carousel — Slick cuenta nodos DOM, no componentes Vue. Sin el wrapper los bullets no funcionan correctamente
- **CLS skeletons**: Skeleton y card real deben tener la misma altura
- **asyncData para SSR crítico únicamente**: Datos secundarios van en `mounted`
- **iframeResizer — cleanup completo**: Ver sección "Contenido A+" abajo. La solución correcta NO es solo `disconnect()`, requiere despachar `pageInfoStop`/`parentInfoStop` antes.
- **Fetch async en watch handlers**: Siempre usar AbortController con timeout + guard `this._isDestroyed` antes de mutar estado reactivo
- **CSP en localhost**: `aplus.libreopcion.com.ar` tiene `frame-ancestors` que no incluye localhost. El HEAD fetch sí funciona pero el iframe se bloquea. Fix: timeout 5s para ocultar si iframeResizer no recibe respuesta
- **Debugging librerías de terceros — navegación rota**: Cuando la navegación asincrónica se rompe post-navigate, sospechar primero de ResizeObserver/MutationObserver globales no limpiados. Leer el source minificado del CDN para entender qué hace y qué NO hace `disconnect()`. El fix es triggerear el cleanup ANTES de borrar el registry, no después.

## Proyecto

- **Stack**: Nuxt 2.18.1 (Vue 2.7.16), SSR, PM2 cluster (`WebAppLO`, 2 instancias)
- **Puerto local**: `localhost:3000`
- **Working dir**: `/var/www/lo/sitio-web-app-v3/app/`
- **`.env`** está en `/var/www/lo/sitio-web-app-v3/app/.env` (en .gitignore, no se pushea)
- PM2 proceso: `WebAppLO`
- Imágenes: resize dinámico `static.libreopcion.com.ar/i/LIO_img_size_w{N}_{checksum}`
- GTM + GA4: NO meter tag GA4 dentro del container GTM-TK5TLKG
- `PRODUCT_IDS` en .env: 757166,757188,757232,757254 (CTA random GPU TUF BO7)
- `HOME_HERO_BANNER=1` activa slider hero animado
- `HOME_BANNER_BULLETS_APPLE=1` activa bullets estilo Apple (derecha desktop, abajo mobile)
- `banners[1]` = slides desktop, `banners[2]` = slides mobile (index.vue)
- `rutas/rutaRetorno` en store: si está seteado, la home redirige. El Logo lo limpia antes de navegar

## Contenido A+ (aplus.libreopcion.com.ar)

Implementación en `pages/producto/_id.vue`. Librería: `@iframe-resizer/parent` v5.5.9 (CDN jsdelivr).

### Flujo
1. `watch.producto` → `checkAPlusContent()` — HEAD fetch con AbortController 3s
2. Si 200 → `aPlusContentAvailable = true` → iframe renderiza
3. `onAPlusIframeLoad(event)` → `await loadIframeResizerScript()` → `window.iframeResize({...}, iframe)`
4. `_aPlusIframeEl = iframe` (referencia no reactiva para beforeDestroy)
5. Timer 5s: si no hubo comunicación → `_disconnectAPlusResizer()` + ocultar iframe
6. `beforeDestroy` → `_disconnectAPlusResizer()`

### La solución correcta para cleanup (commit 5d922efb3, 2026-05-15)

El bug era: `disconnect()` → `Le()` borra `ee[id]`, pero el `ResizeObserver` sobre `document.body` (creado por iframeResizer cuando el child envía `pageInfo`) sigue activo. Cuando Vue desmonta → observer dispara → `l()` crashea → `window.onerror` → navegación rota.

**Fix definitivo en `_disconnectAPlusResizer()`:**
```js
// Despachar ANTES de disconnect() para triggerear l() con ee[id] vivo
["pageInfoStop", "parentInfoStop"].forEach((type) => {
  window.dispatchEvent(new MessageEvent("message", {
    data: `[iFrameSizer]${iframe.id}:::${type}`,
    origin: new URL(iframe.src).origin,
  }));
});
iframe.iFrameResizer.disconnect();
```

### Código muerto eliminado
`syndicationIframe` (desktop + mobile) — referenciaba `onSyndicationIframeLoad`, `limitedEditionSyndicatedContentSrc`, `syndicationIframeHeight` que no existían en el script. Eliminado en `5d922efb3`.

### `_aPlusIframeEl` — por qué existe
`$refs.aplusIframe` se vuelve `null` si el timer de 5s remueve el iframe del DOM antes de `beforeDestroy`. `_aPlusIframeEl` (prefijo `_` = no reactivo en Vue 2) guarda la referencia directa.

## OpcionFest (rama feat/landing-opcionfest)

- Landing `/opcionfest`: hero video bg, 15 productos curados, countdown, sección flash lazy
- Imágenes MKT en `static/micrositios-files/opcionFest/mkt/sin_borde/`
- Timer visual en cards flash: prop `timerBarMode` en `ProgresoInstantFlash.vue`
- Banner en home slider: `SliderHeroOpcionFest.vue`

## Variables .env activas (local)

```
HOME_HERO_BANNER=1
HOME_BANNER_BULLETS_APPLE=1
PRODUCT_IDS=757166,757188,757232,757254
API_HOST4=http://localhost:8097/v4/
NODE_PORT=3000
```

## Referencias

- Tareas SEO en Obsidian: carpeta `Libre Opcion/` con diagnóstico y fixes
- CLAUDE.md del monorepo: `/var/www/lo/CLAUDE.md`

## Ver también

- [[arquitectura|Arquitectura]]
- [[changelog|Changelog]]
- [[stack|Stack]]
- [[00-resumen-diagnostico-seo-performance|Diagnóstico SEO]]
