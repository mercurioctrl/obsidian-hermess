# Stack — Libre Opcion

## Frontend (sitio-web-app-v3)

| Tecnología | Versión | Uso |
|---|---|---|
| Nuxt.js | 2.x | Framework SSR |
| Vue | 2.x | UI reactiva |
| SCSS | — | Estilos con mixins globales |
| PM2 | — | Process manager (local y prod) |
| vue-slick-carousel | — | Sliders/carousels |

### Dependencias clave
- `@nuxtjs/google-fonts` — Descarga Inter localmente (display:optional, subset latin)
- `critters` (custom module) — Inline critical CSS en SSR
- `vue-gtag` — Google Analytics 4 (NO dentro de GTM)

## Backend (sitio-api-rest-v4-laravel)

| Tecnología | Versión | Uso |
|---|---|---|
| PHP | 8.1 | Runtime |
| Laravel | 10 | API REST |
| Redis | — | Cache + queues |
| SQL Server | — | Base de datos (remota) |
| Docker | — | Containerización |

## Servicios externos

- **GTM**: GTM-TK5TLKG (carga diferida con requestIdleCallback)
- **GA4**: Vía vue-gtag (separado de GTM, regla crítica)
- **Firebase**: Push notifications (lazy-loaded en window.load)
- **static.libreopcion.com.ar**: CDN de imágenes con resize dinámico (`LIO_img_size_w{N}_{checksum}`)

## Ver también

- [[arquitectura|Arquitectura]]
- [[changelog|Changelog]]
