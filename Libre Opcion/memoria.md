# Memoria del proyecto

Consolidación de la memoria de Claude para Libre Opcion (sitio-web-app-v3).
Última sincronización: 2026-04-16.

---

## Usuario

- Dev fullstack, e-commerce, enfocado en SEO/performance

## Feedback (reglas de trabajo)

- **No autoría**: Nunca agregar Co-Authored-By en commits
- **Build local**: Siempre `npm ci` → `npm run build` → `npx pm2 restart` (sin saltear npm ci)
- **Sass mixed-decls**: Declaraciones planas SIEMPRE antes de bloques anidados
- **Animaciones**: Pedir referencia visual antes de implementar (no asumir)
- **PNG con canvas**: PNGs con canvas transparente engañan heights CSS, usar negative margins
- **Iframes**: No usar para micrositios (rompen print/PDF), inlinear como Vue
- **Placeholders vacíos**: Si falta asset, eliminar la sección
- **Flex centering**: `width:100%` + `max-width` sin `margin:0 auto` + `align-items:center` no centra en flex column
- **CLS skeletons**: Skeleton y card real deben tener la misma altura
- **CSS defer trade-off**: Defer ahorra render-blocking pero explota CLS si el inline no cubre todo
- **box-shadow en %transition**: Con 84+ @extend cada propiedad non-composited se multiplica
- **sr-only + Bootstrap deferido**: h1 sr-only colapsa al llegar CSS deferido, fix: style inline
- **Promo ROG**: Solo productos línea ROG (no Prime/TUF/AYW)

## Proyecto

- PM2 local en localhost:3003 con `npx pm2`
- Imágenes: resize dinámico `static.libreopcion.com.ar/i/LIO_img_size_w{N}_{checksum}`
- GTM + GA4: NO meter tag GA4 dentro del container GTM-TK5TLKG
- Firebase: Plugin lazy-loaded en window.load (antes bloqueaba vendor bundle)
- Inter font: @nuxtjs/google-fonts download:true, subsets latin, display:optional
- PRODUCT_IDS en .env: 757166,757188,757232,757254 (CTA random de la GPU TUF BO7)

## Referencias

- Tareas SEO en Obsidian: vault con diagnóstico y tareas pendientes
- Sitio oficial RE Requiem: URLs CSS/fonts/masks Capcom

## Ver también

- [[arquitectura|Arquitectura]]
- [[changelog|Changelog]]
- [[stack|Stack]]
- [[00-resumen-diagnostico-seo-performance|Diagnóstico SEO]]
