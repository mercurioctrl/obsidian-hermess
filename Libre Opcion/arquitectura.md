# Arquitectura — Frontend (sitio-web-app-v3)

## Stack

- **Framework**: Nuxt.js 2 (Vue 2, SSR)
- **CSS**: SCSS con mixins globales (`%transition`, `%tipografia-bold`, etc.)
- **Proceso de build**: `npm ci` → `npm run build` → `pm2 restart WebAppLO`
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
      // Despachar pageInfoStop/parentInfoStop ANTES de disconnect()
      // para que l() corra mientras ee[id] existe y desconecte los ResizeObservers
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

### Mapa del source de iframeResizer v5.5.9

| Función | Rol |
|---------|-----|
| `ee` | Registry global (closure del módulo) — `ee[id]` = estado del iframe |
| `Le(iframe)` | disconnect: borra `ee[id]` + `iframe.iframeResizer`. NO desconecta observers |
| `Ne(iframe)` | close: remueve iframe del DOM + llama `Le()` — mismo problema |
| `_e()` | once-function: instala `window.addEventListener('message', We)` permanente |
| `We` | Handler global de mensajes. Early-return si `id not in ee`. Safe post-disconnect |
| `w(fn, name)()` | Setup pageInfo/parentInfo observers — solo si child envía esos mensajes |
| `l()` | Cleanup observers: scroll/resize + `u.disconnect()` + `d.disconnect()` + removeEventListener (esta última crashea si `ee[c]` es undefined) |
| `errorBoundary` | Captura instancias de `Error`. Rethrowea `throw undefined` (Ge) |

## Ver también

- [[changelog|Changelog]]
- [[stack|Stack]]
- [[00-resumen-diagnostico-seo-performance|Diagnóstico SEO]]
