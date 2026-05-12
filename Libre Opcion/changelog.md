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

### Contexto del PR #1173

La rama `LIO-618` reemplaza el hero de video ROG (HTML inline) por un componente reutilizable `SliderHeroLimitedEdition` que muestra la ASUS TUF RX 9070 XT Black Ops 7 Special Edition. Se usa tanto en el home (via `SliderPrincipal`) como en la tienda oficial ASUS (via `SliderTienda` en modo compact). El CTA "Ver producto" elige al azar entre 4 product IDs desde `$config.productIdsParsed`.

---

## 2026-04-08

### API v4 — Nuevas features y migraciones (múltiples PRs)

- **feat**: Imágenes personalizadas del reseller por producto — endpoint para subir, ver y eliminar imágenes propias en la ficha de cada producto (LIO-598, PR #574)
- **feat**: Features de cuenta mobile — `GET /account/lo/features/{id_lo}` con auto-registro de usuario activo como side effect (PR #570)
- **feat**: Estado de verificación de teléfono de vendedor — nuevo endpoint de consulta de estado (PR #562)
- **refactor**: Migración del resumen de pedidos por mes/año a Laravel — endpoint migrado desde API legada (PR #576)
- **fix**: Estadísticas de referidos — corrección de división por cero en cálculo de conversion rate (PR #572)
- **fix**: Estadísticas de referidos — corrección de tipos de datos en la respuesta JSON (PR #578)

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

---

## 2026-05-07

### Historias técnicas para devs jr

- **docs**: Historia técnica para migración del recurso `/favoritos` de API v3 (legada, PHP Restler) a API v4 (Laravel)
  - Cubre los 5 endpoints: `GET /v4/favoritos`, `POST /v4/favoritos`, `POST /v4/favoritos/item`, `DELETE /v4/favoritos/item/{id}`, `DELETE /v4/favoritos`
  - Tabla: `[LO].[dbo].[favoritos]` (productoId, usuarioId) — ya existe, sin migración de DB
  - Payloads, respuestas, criterios de aceptación y notas de implementación
  - Archivo: `/home/hermess/Documentos/lo/historia-backend-migracion-favoritos.md`

---

## 2026-05-10 / 2026-05-11

### Rama: feat/landing-opcionfest

- **feat**: Nueva landing `/opcionfest` — hero con video bg (mp4/webm), grid de 9 productos curados con imágenes MKT (`sin_borde/`), countdown 3 días, sección Precios Flash lazy-loaded en `mounted` (no bloquea SSR)
- **feat**: `SliderHeroOpcionFest.vue` — banner animado en home slider, se muestra primero (antes del de la placa TUF). CTA "Ver productos" → `https://bit.ly/Opcion_Fest_2026`
- **feat**: Logo OpcionFest en navbar desktop — `filter: grayscale(1) brightness(10)` en blanco, `filter: none` al hover para mostrar colores reales
- **feat**: `HOME_HERO_BANNER=1` habilitado en `.env` (activa slider hero animado)
- **refactor**: Header sección Precios Flash rediseñado — estructura eyebrow + título bicolor + subtítulo, igual al de "Ofertas Opción Fest"
- **fix**: Flash products lazy load — movido de `asyncData` a `mounted` para que el SSR no espere la query de precios flash
- **fix**: Botón "Tienda Oficial" oculto en `SliderHeroLimitedEdition`
- **fix**: Hero landing mobile — `height: auto`, columnas stackeadas verticalmente, CTAs full-width, beneficios separados con border-top
- **fix**: Centrado vertical del banner OpcionFest en mobile (`position: absolute; inset: 0` → revertido a `height: 100%` con root `display: flex; flex-direction: column`)
- **fix**: Rayitos eliminados del eyebrow "PRECIOS QUE NO DURAN" en la landing

Archivos clave: `pages/opcionfest.vue`, `components/Home/Banners/SliderHeroOpcionFest.vue`, `components/Home/Banners/SliderPrincipal.vue`, `components/Home/Banners/SliderHeroLimitedEdition.vue`, `components/Layouts/Cabecera/partials/NavegacionDesktopPrincipal.vue`

Assets: `static/micrositios-files/opcionFest/mkt/sin_borde/` (10 imágenes por producto, sin bordes ni logo)

## Ver también

- [[arquitectura|Arquitectura]]
- [[stack|Stack]]
- [[memoria|Memoria]]