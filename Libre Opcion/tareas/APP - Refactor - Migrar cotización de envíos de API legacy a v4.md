# APP - Refactor - Migrar cotización de envíos de API legacy a v4

**Proyecto:** [[Libre Opcion/Libre Opcion|Libre Opción]]
**Estado:** Pendiente
**Fecha:** 2026-04-06

---

## Descripción

El frontend (`sitio-web-app-v3`) utiliza la API legacy (v3, `omega-api`) para las cotizaciones de envío. Los mismos endpoints ya existen en la API v4 (`omega-api4`) y deben reemplazarse para reducir la dependencia del backend legacy.

**Endpoints afectados:**

| Endpoint | Legacy (v3) | v4 |
|----------|-------------|-----|
| Cotización producto | `$axios.api3.$post('envios/producto/cotizacion', ...)` | `$axios.$post('envios/producto/cotizacion', ...)` |
| Cotización checkout | `$axios.api3.$post('envios/checkout/cotizacion', ...)` | `$axios.$post('envios/checkout/cotizacion', ...)` |

## Archivos a modificar

### 1. `app/plugins/api.js` (líneas 113-133)

Cambiar las llamadas de `ctx.$axios.api3.$post(...)` a `ctx.$axios.$post(...)` en:
- `obtenerCotizacionCheckout()` — línea 116
- `obtenerCotizacionProducto()` — línea 126

### 2. Componentes que consumen estos métodos (no requieren cambios)

- `app/pages/producto/partials/Entrega.vue` — llama `this.$api.envios.obtenerCotizacionProducto()` (línea 385)
- `app/pages/mi-compra/checkout-envio.vue` — llama `this.$api.envios.obtenerCotizacionCheckout()` (línea 515)

Estos componentes usan la abstracción de `$api.envios`, así que no necesitan cambios directos.

## Criterios de aceptación

- [ ] `obtenerCotizacionProducto` usa `$axios` (v4) en vez de `$axios.api3` (legacy)
- [ ] `obtenerCotizacionCheckout` usa `$axios` (v4) en vez de `$axios.api3` (legacy)
- [ ] La cotización de envío en la página de producto (`Entrega.vue`) funciona correctamente
- [ ] La cotización de envío en el checkout (`checkout-envio.vue`) funciona correctamente
- [ ] Verificar que los payloads y responses son compatibles entre v3 y v4
- [ ] Test manual: ingresar CP en producto → se muestran opciones de envío con precios
- [ ] Test manual: avanzar al paso de envío en checkout → se cargan las cotizaciones

## Notas técnicas

- **`$axios`** (instancia principal) apunta a `API_HOST4` (`omega-api4.libreopcion.com.ar/v4/`) — ver `nuxt.config.js:661`
- **`$axios.api3`** apunta a `API_HOST` (`omega-api.libreopcion.com.ar`) — ver `plugins/axios.js:122-125`
- Ambas rutas en v4 están sin prefijo de autenticación, igual que en legacy:
  - `Route::post('/envios/producto/cotizacion', EnvioController::class)` — `api.php:139`
  - `Route::post('envios/checkout/cotizacion', CheckoutQuote::class)` — `api.php:305`
- **Riesgo bajo:** el cambio es solo la instancia de axios usada, la ruta y payload son idénticos
- **Considerar:** verificar que el endpoint v4 no requiera autenticación JWT (el legacy no la requiere para estos endpoints)

## Ver también

- [[Libre Opcion/Libre Opcion|Índice del proyecto]]
