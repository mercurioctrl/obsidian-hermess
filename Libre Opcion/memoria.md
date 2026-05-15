# Memoria del proyecto

Consolidación de la memoria de Claude para Libre Opcion (sitio-web-app-v3).
Última sincronización: 2026-05-14.

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
- **iframeResizer**: Siempre llamar `disconnect()` en `beforeDestroy` para limpiar el registry global. Sin esto la navegación posterior se rompe (búsquedas dejan de funcionar)
- **Fetch async en watch handlers**: Siempre usar AbortController con timeout + guard `this._isDestroyed` antes de mutar estado reactivo
- **CSP en localhost**: `aplus.libreopcion.com.ar` tiene `frame-ancestors` que no incluye localhost. El HEAD fetch sí funciona pero el iframe se bloquea. Fix: timeout 5s para ocultar si iframeResizer no recibe respuesta

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

## Variables .env activas (local)

```
HOME_HERO_BANNER=1
HOME_BANNER_BULLETS_APPLE=1
PRODUCT_IDS=757166,757188,757232,757254
API_HOST4=http://localhost:8097/v4/
NODE_PORT=3000
```

## Contenido A+ (aplus.libreopcion.com.ar)

- En `pages/producto/_id.vue`
- HEAD fetch con AbortController 3s → si falla, `aPlusContentAvailable = false`
- `ref="aplusIframe"` en el iframe para poder hacer `disconnect()` en beforeDestroy
- Si iframeResizer no recibe respuesta en 5s → ocultar iframe (CSP block en localhost)
- Guard `_isDestroyed` en todos los callbacks async

## OpcionFest (rama feat/landing-opcionfest)

- Landing `/opcionfest`: hero video bg, 15 productos curados, countdown, sección flash lazy
- Imágenes MKT en `static/micrositios-files/opcionFest/mkt/sin_borde/`
- Timer visual en cards flash: prop `timerBarMode` en `ProgresoInstantFlash.vue`
- Banner en home slider: `SliderHeroOpcionFest.vue`

## Referencias

- Tareas SEO en Obsidian: carpeta `Libre Opcion/` con diagnóstico y fixes
- CLAUDE.md del monorepo: `/var/www/lo/CLAUDE.md`

## Ver también

- [[arquitectura|Arquitectura]]
- [[changelog|Changelog]]
- [[stack|Stack]]
- [[00-resumen-diagnostico-seo-performance|Diagnóstico SEO]]