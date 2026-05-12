# Memoria del proyecto

Consolidación de la memoria de Claude para Libre Opcion (sitio-web-app-v3).
Última sincronización: 2026-05-11.

---

## Usuario

- Dev fullstack, e-commerce, enfocado en SEO/performance y marketing digital

## Feedback (reglas de trabajo)

- **No autoría**: Nunca agregar Co-Authored-By en commits
- **Build local**: Siempre `npm run build` → `pm2 delete all && fuser -k 3000/tcp && pm2 start ecosystem.config.js`
- **Sass mixed-decls**: Declaraciones planas SIEMPRE antes de bloques anidados
- **Animaciones**: Pedir referencia visual antes de implementar (no asumir)
- **PNG con canvas**: PNGs con canvas transparente engañan heights CSS, usar negative margins
- **Iframes**: No usar para micrositios (rompen print/PDF), inlinear como Vue
- **Placeholders vacíos**: Si falta asset, eliminar la sección
- **Flex centering**: `width:100%` + `max-width` sin `margin:0 auto` en flex column no centra. En slick carousel el `height:100%` necesita que el root tenga `display: flex; flex-direction: column` para resolver correctamente
- **CLS skeletons**: Skeleton y card real deben tener la misma altura
- **CSS defer trade-off**: Defer ahorra render-blocking pero explota CLS si el inline no cubre todo
- **box-shadow en %transition**: Con 84+ @extend cada propiedad non-composited se multiplica
- **sr-only + Bootstrap deferido**: h1 sr-only colapsa al llegar CSS deferido, fix: style inline
- **asyncData para SSR crítico únicamente**: Datos secundarios (ej: Precios Flash) van en `mounted` para no bloquear el render inicial de la página
- **pm2 restart**: Siempre `pm2 delete all + fuser -k 3000/tcp` para evitar EADDRINUSE en el puerto 3000

## Proyecto

- PM2 en el servidor con `ecosystem.config.js`
- Imágenes: resize dinámico `static.libreopcion.com.ar/i/LIO_img_size_w{N}_{checksum}`
- GTM + GA4: NO meter tag GA4 dentro del container GTM-TK5TLKG
- Firebase: Plugin lazy-loaded en window.load (antes bloqueaba vendor bundle)
- Inter font: @nuxtjs/google-fonts download:true, subsets latin, display:optional
- `PRODUCT_IDS` en .env: 757166,757188,757232,757254 (CTA random GPU TUF BO7)
- `HOME_HERO_BANNER=1` en .env activa el slider hero animado (OpcionFest + TUF BO7)
- `.env` está en `.gitignore` — al hacer checkout en otro entorno hay que agregar las vars manualmente

## OpcionFest (rama feat/landing-opcionfest)

- Landing `/opcionfest`: hero video bg, 9 productos curados, countdown 3 días, sección flash lazy
- Imágenes MKT en `static/micrositios-files/opcionFest/mkt/sin_borde/` — sin bordes ni logo
- Countdown: `endDate: new Date("2026-05-13T23:59:59")`
- Banner en home slider: `SliderHeroOpcionFest.vue` (primero, antes del TUF BO7)
- Logo en navbar: `filter: grayscale(1) brightness(10)` → blanco; hover → color real

## Referencias

- Tareas SEO en Obsidian: vault con diagnóstico y tareas pendientes
- Sitio oficial RE Requiem: URLs CSS/fonts/masks Capcom

## Ver también

- [[arquitectura|Arquitectura]]
- [[changelog|Changelog]]
- [[stack|Stack]]
- [[00-resumen-diagnostico-seo-performance|Diagnóstico SEO]]