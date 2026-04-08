# Ronda 2 — Fix CLS desktop 0.283 + TBT 1030ms + 134 animaciones no compuestas

## Fecha
2026-04-08

## Contexto

Después de la ronda 1.5 (commits `3c3dd1a29` + `00548cd42`), una medición de PageSpeed home desktop reveló:

- **CLS desktop**: 0.283 (mejoró desde 1.654 pero seguía por encima del umbral)
- **Animaciones no compuestas**: 134 (subió desde 49 — regresión nueva)
- **TBT desktop**: 1,030ms (subió +360ms vs los 670ms previos — regresión nueva)
- **Main thread**: 4.1s

Tres regresiones a investigar simultáneamente.

## Diagnóstico

### 1. CLS 0.283 — imágenes sin width/height en above-the-fold

Componentes con `<img>` sin `width`+`height` en el HTML (solo CSS):

| Componente | Problema |
|---|---|
| `Home/Destacado/MiniBannersScroll.vue` | 3 imgs sin dimensiones (specialForYou, basedOnYourSearches, bigguestDiscounts) |
| `Home/Destacado/Categorias.vue` | Icono SVG de categoría sin dimensiones |
| `Home/CategoriasSlider.vue` | Img de categoría sin dimensiones |
| `Home/Marcas.vue` | `width: 100%` en CSS — variable según flex container |
| `Home/Destacado/BannerPrincipal.vue` | 2 slides del slick sin dimensiones |
| `Home/Destacado/PrecioRelampago.vue` | Img del producto sin dimensiones |

Bonus: en `MiniBannersScroll.vue` quedaba un bug sin commitear — el template usaba `${specialForYou.description}` directo en la URL en vez de pasarlo por `mixinObtenerURI()`, además de un espacio en blanco al final del template literal.

### 2. 134 animaciones no compuestas

**Causa raíz identificada:** los placeholders `%transition*` en `app/assets/scss/_shared-vars.scss` y `app/assets/scss/partials/transitions.scss` incluían `box-shadow .15s ease-in-out` desde el commit `8d7aa8477` (Fix CLS desktop animaciones, ronda anterior).

Esos placeholders se usan vía `@extend` en **84+ lugares** del codebase. Cada `@extend` se compila a una regla CSS real, así que cada propiedad non-composited del placeholder se multiplica:

- 49 (baseline pre-regresión) + ~84 (nuevos `@extend %transition*` con box-shadow) ≈ **134** ✓ exacto.

`box-shadow` es una propiedad que se pinta en CPU, no se compone en GPU, por eso PageSpeed la cuenta como "non-composited animation".

### 3. TBT desktop +360ms

**Causa raíz identificada:** `app/plugins/push-notification.js` (commit `f9f815a04`, refactor v3→v4) llamaba `initFirebase()` directamente en el factory del plugin (línea 122). Eso disparaba el dynamic import del SDK de Firebase apenas Vue montaba el plugin, **anulando completamente el lazy-load del commit `66e95e6d6`**.

```js
// Antes (mal):
export default function (ctx, inject) {
  initFirebase().then(({ firemessaging }) => { ... }); // ← se ejecuta en el factory
  inject("notification", notification);
}
```

El SDK de Firebase (~273KB con auth+messaging) volvía al bundle inicial parseado/compilado en TBT.

## Soluciones aplicadas (commit `00185f1c6`)

### CLS — width/height en imgs above-the-fold

| Archivo | Cambio |
|---|---|
| `MiniBannersScroll.vue` | `width="120" height="120"` en las 3 imgs + fix de `mixinObtenerURI` |
| `Destacado/Categorias.vue` | `width="40" height="40"` |
| `CategoriasSlider.vue` | `width="60" height="60"` |
| `Marcas.vue` | `width="180" height="100"` + `max-width: 180px; object-fit: contain` |
| `Destacado/BannerPrincipal.vue` | `width="773" height="232"` + `fetchpriority="high"` en slide 0 |
| `Destacado/PrecioRelampago.vue` | `width="162" height="162"` (90% de los 180px del wrapper) |

### CLS — min-height en carousels

| Archivo | Cambio |
|---|---|
| `CategoriasSlider.vue` | `.carousel-categorias { min-height: 160px }` |
| `Marcas.vue` | `min-height: 100px` en `.index-marcas` y `.cont-1170` |

Razón: los carousels (`vue-slick-carousel`) inician en cliente y, sin min-height, el contenedor colapsa hasta que slick los inicializa.

### Animaciones no compuestas — sacar box-shadow de los mixins

Quitado `box-shadow .15s ease-in-out` de los 5 placeholders en ambos archivos:

```scss
// app/assets/scss/_shared-vars.scss y app/assets/scss/partials/transitions.scss
%transition {
  // antes: ..., transform .15s ease-in-out, box-shadow .15s ease-in-out;
  // ahora:
  transition: color .15s ease-in-out, background-color .15s ease-in-out, border-color .15s ease-in-out, opacity .15s ease-in-out, transform .15s ease-in-out;
}
// idem %transition-lenta, %transition-desplegables, %transition-nav, %transition-rapida
```

Si algún componente puntual necesita transicionar `box-shadow`, debe declararlo inline en su propio bloque CSS — no en el mixin global.

### TBT — diferir push-notification al evento load

```js
// app/plugins/push-notification.js
export default function (ctx, inject) {
  const setupForegroundMessaging = () => {
    initFirebase().then(({ firemessaging }) => {
      if (!firemessaging) return;
      firemessaging.onMessage(async (payload) => { /* ... */ });
    });
  };

  if (process.client) {
    if (document.readyState === "complete") {
      setupForegroundMessaging();
    } else {
      window.addEventListener("load", setupForegroundMessaging, { once: true });
    }
  }

  inject("notification", notification); // los métodos del objeto siguen siendo lazy
}
```

Los métodos del objeto `$notification` que se inyecta ya eran lazy (cada uno hace `await initFirebase()` solo cuando se llama), así que login/push siguen funcionando sin cambio funcional.

## Métricas previas (a verificar después del deploy)

| Métrica | Antes (ronda 1.5) | Esperado (ronda 2) |
|---|---|---|
| CLS desktop | 0.283 | <0.1 |
| TBT desktop | 1030ms | ~700-800ms |
| Animaciones no compuestas | 134 | ~50 |
| Main thread | 4.1s | <3.5s |

## Hashes relevantes

- `8d7aa8477` — Fix CLS desktop animaciones (introdujo box-shadow en mixins, regresión)
- `f9f815a04` — Refactor v3→v4 push notifications (introdujo init en factory, regresión)
- `66e95e6d6` — Lazy-load Firebase SDK (anulado por f9f815a04)
- `3c3dd1a29` + `00548cd42` — Fix CLS post-defer (ampliación de critters + min-heights)
- **`00185f1c6`** — Esta ronda 2 (fixes documentados acá)

## Lecciones aprendidas

1. **Mixins SCSS reutilizados con `@extend` multiplican el costo de cada propiedad incluida**. 84 usos × 1 propiedad nueva (box-shadow) = 84 nuevas non-composited animations en PageSpeed. Antes de agregar algo a un placeholder global, contar los `@extend`.

2. **Lazy-load se cancela trivialmente**. Si un plugin (o cualquier código en el factory de un plugin) llama una función que dispara el dynamic import, el lazy-load no sirve para nada. Verificar que el dynamic import solo ocurra detrás de un evento del usuario o de `window.load`.

3. **`width`/`height` en HTML es indispensable aunque la CSS ya fije dimensiones**. PageSpeed audita los atributos HTML, no la CSS resuelta. Los carousels client-side necesitan ambos: width/height en las imgs Y min-height en el wrapper.

## Próximos pasos

- [ ] Re-medir home desktop en PageSpeed después de `00185f1c6` deployado
- [ ] BootstrapVue tree-shake en `app/plugins/bootstrap.js` (importa 6 componentes pero el side-effect del paquete trae más)
- [ ] VeeValidate lazy (importado global aunque solo lo usan formularios)
- [ ] vendor splitChunks granular en `nuxt.config.js` (actualmente `vendor: true` mete todo en un chunk)
- [ ] Migrar Firebase v8 → v9 modular para tree-shaking real

## Ver también

- [[00-resumen-diagnostico-seo-performance]]
- [[01-fix-cls-imagenes]]
- [[02-fix-lcp-render-blocking]]
- [[05-fix-fouc-css-tardio]]
- [[Libre Opcion]]
