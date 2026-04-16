# Arquitectura — Frontend (sitio-web-app-v3)

## Stack

- **Framework**: Nuxt.js 2 (Vue 2, SSR)
- **CSS**: SCSS con mixins globales (`%transition`, `%tipografia-bold`, etc.)
- **Proceso de build**: `npm ci` → `npm run build` → `npx pm2 restart`
- **Dev local**: PM2 en `localhost:3003`

Ver [[stack|Stack completo]].

## Estructura de banners y tiendas oficiales

### Componentes de banner hero

```
SliderPrincipal.vue          → Usado en HOME (altura completa, 360px)
  └─ SliderHeroLimitedEdition.vue  → Componente reutilizable del hero con video

SliderTienda.vue             → Usado en TIENDA OFICIAL (max-height: 345px)
  └─ SliderHeroLimitedEdition.vue  → Mismo componente, con prop `compact`
```

`SliderHeroLimitedEdition` acepta un prop `compact` (Boolean) que reduce proporcionalmente todos los elementos (~30%) para adaptarse al banner más angosto de la tienda oficial.

### Configuración de tiendas oficiales

`storeConfig/officialStores.js` define la config de cada tienda (ASUS):
- Banners, menú, categorías, promos
- `limitedEdition`: datos de la sección de edición limitada (hero, gallery, specs, bundle)
- `productLink`: ruta base del producto; el ID se elige al azar desde `$config.productIdsParsed`

### Variables de entorno relevantes

- `HOME_HERO_BANNER` — Activa/desactiva el slide hero de video en home
- `PRODUCT_IDS` — Lista CSV de IDs de producto para el CTA random (ej: `757166,757188,757232,757254`)

## Principios de diseño UI aplicados

- **Gestalt (proximidad)**: copy + producto centrados como unidad (`justify-content: center` + gap) en vez de separados a extremos (`space-between`)
- **Escala proporcional**: modo compact reduce ~30% parejo para mantener relaciones internas entre elementos

## Decisiones de arquitectura

- **Componente reutilizable vs HTML inline**: el hero de video se extrajo de `SliderTienda` a `SliderHeroLimitedEdition` para reutilizar entre home y tienda sin duplicar código
- **CTA random desde .env**: los product IDs se configuran en `.env` (`PRODUCT_IDS`) y se parsean en `nuxt.config.js` como `productIdsParsed`, evitando hardcodear IDs en componentes
- **CSS scoped + prop compact**: en vez de intentar override desde el padre (problemas de especificidad con scoped styles), se usa un prop que aplica una clase modificadora BEM (`--compact`)

## Ver también

- [[changelog|Changelog]]
- [[stack|Stack]]
- [[00-resumen-diagnostico-seo-performance|Diagnóstico SEO]]
