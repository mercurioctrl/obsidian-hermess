# Fix FOUC — Critical CSS inline para header/layout en Nuxt 2

> Volver a [[00-resumen-diagnostico-seo-performance|Resumen General]]
> Relacionado: [[02-fix-lcp-render-blocking]] (ambos tratan la carga de CSS)
> Relacionado: [[04-fix-fuentes-innecesarias]] (fuentes también causan flash visual)

## Estado: ✅ IMPLEMENTADO

**Branch:** `fix/fouc-critical-css-critters`
**Archivos modificados:**
- `app/modules/critters.js` (nuevo — módulo custom Nuxt 2)
- `app/nuxt.config.js` (agrega módulo + configuración `critters`)
- `app/package.json` (agrega `critters-webpack-plugin` como devDependency)

**Deploy:** requiere `npm install` antes del build.

---

## Contexto del problema

Al entrar al sitio libreopcion.com.ar, durante ~700ms la página se ve "desarmada" — sin estilos. Esto es un FOUC (Flash of Unstyled Content).

**Stack confirmado:** Nuxt 2, Vue 2, SSR habilitado, `extractCSS: true`, webpack, Cloudflare.

**Causa raíz:** Nuxt 2 con `extractCSS` divide el CSS en ~216 archivos. Solo ~7 llegan como `<link rel="stylesheet">` en el HTML inicial (sync). Los archivos CSS del **header, layout y navegación** están en chunks lazy que Nuxt carga via JS después de la hidratación. El navegador pinta el HTML SSR antes de que esos estilos lleguen → el header se ve sin fondo, el logo aparece gigante, el layout está roto.

---

## Solución implementada: Inline CSS directo (sin Critters)

### Por qué NO se usó Critters

Se evaluaron 3 enfoques:

| Enfoque | Problema |
|---------|----------|
| `nuxt-critters` (npm) | No existe para Nuxt 2. `@nuxtjs/critters` es solo Nuxt 3. |
| `critters` vía módulo custom | Convierte CSS sync a async (`media="print"`), lo que **rompe los botones de producto** en mobile (componentes `client-only` pierden estilos). |
| **Inline directo (elegido)** | Inyecta CSS de chunks lazy como `<style>` sin tocar los `<link>` sync existentes. Sin regresión. |

### Cómo funciona

El módulo `app/modules/critters.js` (nombre heredado, no usa la librería critters):

1. En el primer request SSR, lee TODOS los CSS del build (`.nuxt/dist/client/css/`)
2. Filtra solo los que contienen selectores críticos del header/layout:
   - `cabecera-desktop`, `cabecera-logo`, `cabecera-top`, `cabecera-bottom`
   - `cabecera-navegacion`, `cabecera-carrito`, `cabecera-envios`
   - `layout-desktop`, `layout-mobile`
   - `pie-desktop`, `pie-mobile`
3. Concatena su contenido y lo cachea en memoria
4. En cada `render:route`, inyecta el CSS como `<style>` antes de `</head>`
5. **No toca** ningún `<link rel="stylesheet">` existente

### Qué cambia en el HTML

**ANTES:**
```html
<head>
  <!-- CSS base (sync, incluye Bootstrap, main.scss, botones) -->
  <link rel="stylesheet" href="/_nuxt/css/b89f375.css">
  <!-- ... 6 más ... -->
  
  <!-- CSS del header/layout NO está aquí — llega via JS -->
</head>
```

**DESPUÉS:**
```html
<head>
  <!-- CSS del header/layout inyectado inline — se aplica INMEDIATAMENTE -->
  <style>
    .cabecera-desktop[data-v-3f511e4d]{background-color:#1b1b1f;...}
    .cabecera-logo[data-v-70a9489c]{display:block;max-width:250px;...}
    .layout-desktop[data-v-...]{...}
    /* ~13 archivos CSS de header/layout */
  </style>
  
  <!-- CSS base INTACTO — sigue sync, botones no se rompen -->
  <link rel="stylesheet" href="/_nuxt/css/b89f375.css">
  <!-- ... 6 más ... -->
</head>
```

---

## Impacto medido

| Métrica | Antes | Después | Cambio |
|---------|-------|---------|--------|
| FOUC header | ~700ms sin estilos | Sin FOUC | ✅ Resuelto |
| CSS inline | 0 KB | ~213 KB (raw) | Aumento |
| HTML gzip | ~15 KB | ~34-43 KB | +20 KB aprox |
| CSS sync `<link>` | 7 | 7 (intactos) | Sin cambio |
| Botones producto | Con estilos | Con estilos | Sin regresión |
| TTFB | ~600ms | ~600ms | Sin cambio (string replace instantáneo) |
| CLS | Alto (shift por CSS tardío) | Mejora | ✅ |
| FCP | Normal | Neutro | = |

**Nota:** El SSR cache (`nuxt-ssr-cache`) hace que el CSS inline se calcule solo en el primer request de cada ruta cacheada. Requests siguientes se sirven del cache sin overhead.

---

## Limitación conocida: componentes `client-only`

Los botones "Agregar al carrito" y "Comprar ahora" en la ficha de producto son `client-only` (no están en el HTML SSR). Su CSS depende de los `<link>` sync que cargan Bootstrap/main.scss. En mobile con incógnito, primera carga, pueden aparecer sin estilos por una fracción de segundo hasta que el CSS sync termina de cargar y JS hidrata. **Esto NO es una regresión** — pasa con y sin el módulo.

---

## Configuración en nuxt.config.js

```javascript
// En el array modules:
modules: [
  // ... otros módulos ...
  '~/modules/critters',
  // ...
],

// Bloque de configuración (se mantiene por compatibilidad, no lo usa el módulo actual):
critters: {
  config: {
    preload: 'media',
    inlineFonts: false,
    pruneSource: false,
    mergeStylesheets: true,
    reduceInlineStyles: true,
    compress: false,
  }
},
```

---

## Rollback

Si causa problemas:

1. Quitar `'~/modules/critters'` del array `modules` en `nuxt.config.js`
2. Quitar el bloque `critters: { ... }`
3. Rebuild: `rm -rf .nuxt/ && npm run build`

El archivo `app/modules/critters.js` puede quedarse — sin estar en `modules`, no se ejecuta.

---

## Archivos del módulo

| Archivo | Función |
|---------|---------|
| `app/modules/critters.js` | Módulo Nuxt 2: lee CSS de chunks lazy, filtra por selectores críticos, inyecta inline |
| `app/nuxt.config.js` | Registra el módulo y configuración |
| `app/package.json` | `critters-webpack-plugin` como devDependency (trae la librería `critters` — no se usa en runtime actualmente pero se mantiene por si se quiere volver al enfoque critters) |
