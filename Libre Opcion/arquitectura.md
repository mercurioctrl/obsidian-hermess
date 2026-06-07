# Arquitectura — Frontend (sitio-web-app-v3)

## Stack

- **Framework**: Nuxt.js 2 (Vue 2, SSR)
- **CSS**: SCSS con mixins globales (`%transition`, `%tipografia-bold`, etc.)
- **Proceso de build**: `npm ci` → `npm run build` → `pm2 restart WebAppLO`
- **Dev local**: PM2 en `localhost:3003`

Ver [[stack|Stack completo]].

## Pasarelas de pago — Checkout integrado

### Flujo general

```
checkout-pago.vue           → Selección de medio de pago + formulario de tarjeta
  └─ confirmar.vue          → Confirma el pedido y ejecuta el cobro
  └─ finalizada.vue         → Resultado (exitosa / rechazada / pendiente)
```

El `paymentMethodIdSelected` (ID del medio de pago seleccionado) determina el flujo en `confirmar.vue`.

### IDs de medios de pago (env)

| Variable `.env` | ID (prod) | Pasarela |
|---|---|---|
| `ID_PAGO_CON_TARJETA` | 5076 | MercadoPago (formulario embebido) |
| `ID_PAGO_CON_TARJETA_GETNET` | 5077 | GetNet by Santander (formulario embebido) |
| `ID_PAGO_CON_TARJETA_PAYWAY` | 5078 | Payway |
| `ID_PAGO_CON_TARJETA_MODO` | 5079 | MODO (billetera digital, QR/deeplink) |

Los medios de pago vienen de la API v3 (`pedidos/checkout`). Si GetNet/Payway/MODO no están en la respuesta, se inyectan de forma hardcodeada en `mediosPagoFiltrados` (computed de `checkout-pago.vue`).

### Flujo MercadoPago (referencia)

1. `FormPagoTarjetaCreditoDebitoMP.vue` — Usa SDK JS de MP (iframes hosted fields)
2. `createCardToken()` → `mp.fields.createCardToken()` → token MP
3. `submitForm()` → dispatch `checkout/actualizarpedidoConCardToken` → PATCH API v3 (guarda `datosPagoConTarjeta` con token en `payment_gateway_transactions`)
4. Navega a `confirmar.vue`
5. `confirmarPedido()` → `processPayment()` → `POST /v4/payment/mercadopago/process`
6. API v4 lee `payment_gateway_transactions`, procesa con MP SDK

### Flujo GetNet (formulario embebido)

1. `FormPagoGetNet.vue` — Inputs HTML nativos (sin SDK externo)
2. `createCardToken()` → `POST /v4/payment/getnet/tokenize` → `number_token`
3. Dispatch `checkout/actualizarpedidoConCardTokenGetNet` → PATCH API v3 (guarda `number_token` + datos en `payment_gateway_transactions`)
4. Navega a `confirmar.vue`
5. `confirmarPedido()` → `processPaymentGetnet()` → `POST /v4/payment/getnet/process`
6. API v4 lee `payment_gateway_transactions`, carga `number_token`, llama `POST /v1/payments` en GetNet

**Estado actual (2026-06-07):** Sandbox GetNet bloquea con 403 desde IP del servidor (`190.189.93.116`). Requiere whitelist de Santander/GetNet. La autenticación OAuth2 sí funciona.

### Flujo MODO (billetera digital)

1. `FormPagoModo.vue` — Sin formulario, solo info
2. En `confirmar.vue`: `processPaymentModo()` → `POST /v4/payment/modo/create-intention` → obtiene `qr`, `deeplink`, `checkoutId`
3. Carga SDK MODO (`ecommerce-modal.modo.com.ar/bundle.js`)
4. `window.ModoSDK.modoInitPayment(...)` — abre modal con QR + deeplink
5. Callbacks `onSuccess`/`onFailure`/`onCancel` navegan al resultado

### Tabla `payment_gateway_transactions`

Todos los proveedores (MP, GetNet, Payway) usan la misma tabla. Campos clave:
- `token` — MP card token / GetNet `number_token` / Payway token
- `transaction_amount`, `installments`, `payment_method_id`
- `email`, `identification_type`, `identification_number`, `cardholder_name`
- `additional_info` (JSON) — GetNet guarda aquí `brand`, `expiration_month`, `expiration_year`

### Ruta del procesador en API v4

```
POST /v4/payment/{provider}/process
  → ProcessPayment controller
  → PaymentTransactionService::getTransactionData(pedidoId)  ← lee payment_gateway_transactions
  → request->merge(transactionData)
  → PaymentProcessorFactory::make(provider)  ← getnet|mercadopago|payway
  → processor->processPayment(request)
  → updatePaymentStatus + updateOrder
```

---

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
- **GetNet sin SDK**: a diferencia de MP (iframes hosted fields), GetNet se tokeniza vía endpoint propio del backend. Más simple, pero requiere whitelist de IP en el sandbox de GetNet

## iframeResizer — Cleanup pattern

`pages/producto/_id.vue` usa `@iframe-resizer/parent` v5.5.9 (CDN jsdelivr) para el iframe de contenido A+.

### El bug y la causa raíz

`disconnect()` de iframeResizer hace `Le()` que borra `ee[id]` del registry global. Pero si el child iframe envió mensajes `pageInfo`/`parentInfo`, la función interna `w()` habrá creado un `ResizeObserver` sobre `document.body` con `{subtree: true}`. Ese observer **no es desconectado por `Le()`**.

Cuando Vue desmonta el componente (cambios en DOM), el observer dispara → detecta `ee[id]` ausente → llama `l()` para auto-limpiarse → `l()` crashea en `ee[c].iframe` (TypeError, porque `ee[c]` ya fue borrado) → el error llega a `window.onerror` → corrompía navegación global.

### Fix: `_disconnectAPlusResizer()`

```js
_disconnectAPlusResizer() {
  try {
    const iframe = this._aPlusIframeEl || (this.$refs && this.$refs.aplusIframe);
    if (iframe && iframe.iFrameResizer && typeof iframe.iFrameResizer.disconnect === "function") {
      const id = iframe.id;
      if (id) {
        try {
          const origin = iframe.src ? new URL(iframe.src).origin : null;
          if (origin) {
            ["pageInfoStop", "parentInfoStop"].forEach((type) => {
              window.dispatchEvent(new MessageEvent("message", {
                data: `[iFrameSizer]${id}:::${type}`,
                origin,
              }));
            });
          }
        } catch (e2) { /* silencioso */ }
      }
      iframe.iFrameResizer.disconnect();
    }
  } catch (e) { /* silencioso */ }
  this._aPlusIframeEl = null;
},
```

### Por qué `_aPlusIframeEl`

`this.$refs.aplusIframe` se vuelve `null` cuando el timer de 5s (detección CSP) setea `aPlusContentAvailable = false` y Vue remueve el iframe del DOM vía `v-if`. Para garantizar acceso en `beforeDestroy`, se almacena la referencia directa en `_aPlusIframeEl` (prefijo `_` = no reactivo en Vue 2).

## Ver también

- [[changelog|Changelog]]
- [[stack|Stack]]
- [[memoria|Memoria]]
