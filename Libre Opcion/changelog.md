# Changelog

Registro de trabajo en el frontend (sitio-web-app-v3).

---

## 2026-04-16

### Rama: LIO-618 (hero limited edition BO7 + tienda oficial ASUS)

- **merge**: Resueltos conflictos entre `LIO-618` y `development` en `SliderTienda.vue` y `officialStores.js`
- **fix**: Agregada variable `PRODUCT_IDS` al `.env` (4 IDs de GPU TUF BO7) para que el CTA random funcione
- **feat**: Centrado del hero banner en home — `justify-content: center` con `gap: 64px` (antes `space-between` empujaba copy y producto a extremos)
- **feat**: Variante `compact` en `SliderHeroLimitedEdition` para tienda oficial — reduce títulos, producto, botones y gaps ~30% proporcionalmente al banner más angosto

Archivos: `components/Home/Banners/SliderHeroLimitedEdition.vue`, `pages/busquedas/partials/SliderTienda.vue`, `storeConfig/officialStores.js`

### Contexto del PR #1173

La rama `LIO-618` reemplaza el hero de video ROG (HTML inline) por un componente reutilizable `SliderHeroLimitedEdition` que muestra la ASUS TUF RX 9070 XT Black Ops 7 Special Edition. Se usa tanto en el home (via `SliderPrincipal`) como en la tienda oficial ASUS (via `SliderTienda` en modo compact). El CTA "Ver producto" elige al azar entre 4 product IDs desde `$config.productIdsParsed`.

---

## 2026-04-10

### Rama: feat/landing-asus-rog-requiem

- Quita 3 mothers ASUS no-ROG del listado de productos
- Fix Sass mixed-decls warning en `.rq-cta--primary`
- Add badge envío gratis + 3 mothers ASUS, fix color CTA Canjear
- Fix CTAs hero /asus/rog descentrados en mobile
- Add CTAs canjear/bases en /asus/rog + bullets left-align mobile

## 2026-04-05 – 2026-04-08

### SEO / Performance (múltiples ramas)

- Fix CLS listings /placas-de-video + Inter font preload + display:optional
- Fix CLS mobile 0.519: inline style en h1 sr-only + width/height en pin envíos
- Fix CLS/TBT desktop: width/height en imgs, box-shadow fuera de %transition, push-notification diferido
- Fix CLS desktop: critical CSS para home-destacado/categorias-list/iflash-banner
- Lazy-load Firebase SDK (–196KB del vendor bundle)
- Preload dinámico de imagen del banner principal (LCP)
- Deferir CSS no-crítico de Nuxt y GTM al evento load
