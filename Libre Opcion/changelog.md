# Changelog

Registro de trabajo en el proyecto Libre Opción.

---

## 2026-06-07

### Checkout — GetNet integrado (formulario embebido en el sitio)

Se reemplazó la integración de Web Checkout de GetNet (redirección a plataforma externa) por un formulario embebido similar al de MercadoPago.

**Backend (`sitio-api-rest-v4-laravel`):**
- **feat**: `TokenizeGetNet.php` — Controller que tokeniza la tarjeta vía GetNet API (`POST /v1/tokens/card`). Valida JWT del usuario, valida campos de tarjeta, obtiene access token OAuth2 y retorna `number_token`
- **feat**: Ruta `POST payment/getnet/tokenize` con middleware `token.auth` agregada en `routes/api.php`
- **feat**: Variables de entorno GetNet sandbox configuradas en backend `.env`:
  - `GETNET_URL_API=https://api.pre.globalgetnet.com`
  - `GETNET_CLIENT_ID=cid_0ce168a0-...`, `GETNET_SECRET_ID`, `GETNET_SELLER_ID=23000018929`
- `GetNetPayment.php` ya estaba implementado — procesa pago vía `POST /v1/payments` usando `number_token`
- `PaymentProcessorFactory` ya registrado con `'getnet' => GetNetPayment::class`

Archivos: `app/Http/Controllers/Payment/GetNet/TokenizeGetNet.php`, `routes/api.php`, `app/.env`

**Frontend (`sitio-web-app-v3`):**
- **feat**: `FormPagoGetNet.vue` — Reescrito como formulario completo con inputs nativos: número de tarjeta (detección automática de marca Visa/Mastercard/Amex/Cabal), selects de vencimiento MM/AA, CVV, cuotas (1/3/6/12 — Ahora 12), titular, tipo y número de documento. `createCardToken()` llama al backend, obtiene `number_token` y navega a confirmar
- **feat**: `store/checkout.js` — Acción `actualizarpedidoConCardTokenGetNet` (guarda `number_token` + datos de tarjeta en el pedido vía API v3, idéntica a la de MP)
- **feat**: `checkout-pago.vue` — Ref `componenteGetNet`, flag `isFieldsCompleteGetNet`, rama GetNet en `actualizarPedido()`. También agregados Payway (`componentePayway`) y MODO
- **feat**: `confirmar.vue` — `processPaymentGetnet()` ahora llama `processPayment('getnet', {id})` igual que MP, en vez de redirigir a URL externa. También agregados `processPaymentPayway()` y `processPaymentModo()` (MODO usa SDK propio con QR/deeplink)
- **feat**: `api4.js` — Métodos `tokenizeGetnet(data)`, `tokenizePayway(data)`, `createModoIntention(data)`
- `mediosPago` id `5077` = GetNet, `5078` = Payway, `5079` = MODO — inyectados en `mediosPagoFiltrados` si no vienen de la API v3

**Diagnóstico GetNet sandbox:**
- La autenticación OAuth2 (`/authentication/oauth2/access_token`) funciona correctamente
- Los endpoints `/v1/tokens/card` y `/v1/payments` devuelven 403 Access Denied (Akamai)
- **Causa:** GetNet sandbox tiene whitelist de IPs. La IP del servidor es `190.189.93.116`
- **Acción requerida:** Contactar a Santander/GetNet para habilitar la IP en el sandbox

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

- **fix**: [[changelog#iframeResizer cleanup|iframeResizer]] en ficha de producto (`pages/producto/_id.vue`)
- **fix**: Bullets slider home — `SliderHeroLimitedEdition` envuelto en `<div>` dentro de Carousel
- **feat**: Banner animado ASUS — botón "Ver ASUS" con link a `/asus`
- **feat**: `HOME_BANNER_BULLETS_APPLE=1` agregado al `.env`

---

## 2026-05-15

### Rama: development — Fix root cause iframeResizer (navegación rota)

- **fix**: Causa raíz del bug "navegación asincrónica se rompe después de visitar ficha con A+" (`pages/producto/_id.vue`, commit `5d922efb3`)
- **fix**: Eliminado código muerto `syndicationIframe`
- **feat**: Referencia `_aPlusIframeEl` (no reactiva) para acceso en `beforeDestroy`

Ver [[arquitectura#iframeResizer — Cleanup pattern|Arquitectura]] y [[memoria#Contenido A+ (aplus.libreopcion.com.ar)|Memoria]].

## Ver también

- [[arquitectura|Arquitectura]]
- [[stack|Stack]]
- [[memoria|Memoria]]
