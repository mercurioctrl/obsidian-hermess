# Diagnóstico SEO y Performance — libreopcion.com.ar

## Fecha del análisis
Abril 2026 (5 sesiones de trabajo acumuladas)

## Qué se investigó y por qué

Catriel notó una caída de visitas en libreopcion.com.ar después de hacer cambios de SEO y velocidad. Se realizaron múltiples sesiones de diagnóstico para identificar la causa y monitorear la recuperación.

## Sesiones 1-3: Investigación de la caída de tráfico

### Hallazgo principal
La caída de tráfico **NO fue por SEO**. Fue causada por los canales de publicidad (Display y Cross-network/Google Ads) que habían bajado temporalmente. El tráfico orgánico se mantenía estable.

### Datos de GA4
- El tráfico total pasó de **-34.91%** a **+27.92%** en el transcurso de las sesiones
- Cross-network se recuperó de **-45%** a **+51.88%**
- Organic Search mostró una leve caída de **-9.54%** (a monitorear)

### Conclusión
La caída fue temporal y se debió a variaciones normales en campañas publicitarias, no a problemas técnicos del sitio.

## Sesión 4: Revisión de Google Search Console

### Core Web Vitals — Mobile (estado actual)

| Métrica | Estado | URLs afectadas |
|---------|--------|---------------|
| CLS > 0.25 | POBRE | 73 URLs (patrón /tv) |
| INP > 200ms | Necesita mejorar | 82 URLs |
| LCP > 2.5s | Necesita mejorar | 73 URLs |
| LCP > 4s | POBRE | 9 URLs |

Se inició una **validación de CLS** en Search Console el 28/3/26 (tarda hasta 28 días).

## Sesión 5: Análisis profundo del sitio

### PageSpeed Insights — /tv (mobile)

| Métrica | Valor | Estado |
|---------|-------|--------|
| Rendimiento | 54 (mejoró de 35) | Naranja |
| Accesibilidad | 74 | Naranja |
| Recomendaciones | 100 | Verde |
| SEO | 92 | Verde |
| LCP (campo) | 4.1s | Pobre (>4s) |
| CLS (campo) | 0.38 | Pobre (>0.25) |
| FCP (campo) | 1s | Bueno |
| INP (campo) | 302ms | Necesita mejorar |

### Stack técnico detectado
- Framework: **Nuxt.js** (Vue)
- CDN: **Cloudflare** (con Rocket Loader activo)
- Imágenes: servidas desde `static.libreopcion.com.ar`
- Analytics: GA4 + GTM
- Terceros: Facebook Pixel, Metricool, Sendinblue/Brevo

### Problemas encontrados (ordenados por impacto)

#### 1. CLS — Imágenes sin dimensiones (CRÍTICO) ✅ IMPLEMENTADO
- 25 de 42 imágenes sin atributos `width`/`height`
- 17 imágenes de producto (200x200px natural) dentro de `.imagen > .producto > img` sin dimensiones HTML
- 8 imágenes above-the-fold con `loading="lazy"` innecesario
- Sin `aspect-ratio` en CSS (usa `auto`)
- 18 badges "Verificado" sin dimensiones
- Íconos del header sin dimensiones
- **Solución aplicada:**
  - Agregado `width`/`height` a imágenes de producto en 7 módulos (A, AHome, B, C, D, E, FilaA)
  - Lazy loading condicional: `eager` para las primeras 4 imágenes, `lazy` para el resto
  - `fetchpriority="high"` en la primera imagen de cada listado
  - `aspect-ratio: 1/1` en CSS de `.producto img`
  - `width`/`height` en iconos del header (carrito, notificaciones, aviso carrito)
  - Optimizado `size_h` en URLs de imágenes para coincidir con el alto real del contenedor CSS (ahorro de bytes)
  - Badge "Verificado" ya tenía dimensiones en ModuloB y ModuloC
- **Branch:** `fix/cls-imagenes-width-height-v2` (basada en `fix/fouc-critical-css-critters`)
- **Instrucciones y detalle:** [[01-fix-cls-imagenes]]

#### 2. LCP — Recursos render-blocking (ALTO)
- 23 hojas de estilo CSS (excesivo)
- Render-blocking con ahorro estimado de 1,520ms
- 348 KiB de JavaScript no utilizado
- 70 KiB de CSS no utilizado
- 6 scripts de terceros compitiendo por ancho de banda
- **Instrucciones:** [[02-fix-lcp-render-blocking]]

#### 3. Header fijo sin min-height (MEDIO) ✅ IMPLEMENTADO
- Header con `position: fixed` y 91px de altura pero sin `min-height`
- Puede causar CLS al cargar fuentes web
- **Solución aplicada:** Agregado `min-height` a Desktop.vue (89.92px) y Simple.vue (58.92px). Mobile.vue ya lo tenía (57.09px).
- **Branch:** `fix/fouc-critical-css-critters`
- **Instrucciones y detalle:** [[03-fix-header-min-height]]

#### 4. Fuentes web innecesarias (MEDIO) ✅ REVISADO (sin cambios necesarios)
- Roboto: no existe en código fuente, solo aparecía en cache/build artifacts
- Inter: ya carga solo 3 pesos (400, 500, 700) con `display: swap`
- Slick font: base64 inline (~2KB), usada en 23 componentes — no vale la pena hacerla condicional
- Font Awesome: ya se carga async con `media="print"` + `onload`
- **Instrucciones y detalle:** [[04-fix-fuentes-innecesarias]]

#### 5. FOUC — Flash of Unstyled Content (ALTO) ✅ IMPLEMENTADO
- Al cargar el sitio, se veía "desarmado" por ~700ms antes de que se apliquen los estilos
- CSS del header/layout estaba en chunks lazy que Nuxt cargaba via JS después de la hidratación
- **Solución aplicada:** módulo custom que inyecta CSS de header/layout como `<style>` inline sin tocar los `<link>` sync existentes
- **Branch:** `fix/fouc-critical-css-critters`
- **Limitación:** componentes `client-only` (botones "Agregar al carrito") siguen dependiendo del CSS sync — no es regresión
- **Instrucciones y detalle:** [[05-fix-fouc-css-tardio]]

## Plan de acción recomendado

1. ~~**Inmediato:** Implementar fix #5 (FOUC) — el usuario lo ve en cada visita~~ ✅ Implementado
2. ~~**Inmediato:** Implementar fix #1 (imágenes) — mayor impacto en CLS~~ ✅ Implementado
3. ~~**Corto plazo:** Fix #3 (header) y #4 (fuentes) — cambios simples~~ ✅ Implementado / Revisado
4. **Mediano plazo:** Fix #2 (render-blocking):
   - ~~Sub-tarea A: diferir scripts de terceros (Metricool, FB Pixel, Brevo)~~ ✅
   - ~~Sub-tarea B: deferir CSS render-blocking de Nuxt~~ ✅ (~440ms)
   - ~~Sub-tarea C: diferir GTM con bootstrap:false~~ ✅ (~158ms)
   - Sub-tarea D: consolidar CSS splitting — **descartado**
   - ~~Sub-tarea E: lazy-load Firebase SDK~~ ✅ (-196KB del vendor inicial)
   - ~~Sub-tarea F: fix CLS desktop (animaciones no compuestas)~~ ✅ + revisión ronda 2 (box-shadow)
   - ~~Sub-tarea G: LCP preload del banner principal~~ ✅
   - ~~Sub-tarea H: width/height en imgs above-the-fold + min-height carousels~~ ✅ ronda 2
   - ~~Sub-tarea I: diferir push-notification.js al evento load (anulaba lazy-load Firebase)~~ ✅ ronda 2
7. **Cloudflare:** ✅ Rocket Loader desactivado + BIC rule en home (3,636ms → 7ms)
5. **Monitoreo:** Esperar 2-4 semanas para que Google recoja datos de campo actualizados
6. **Seguimiento:** Revisar Core Web Vitals en Search Console después de los cambios

## Última ronda de cambios — commit `274bce6ee` (2026-04-08, ronda 4)

Detalle completo en [[08-fix-cls-listings-ronda-4]].

### Hallazgo crítico de CrUX field (28 días, usuarios reales)

**La home está perfecta. El problema son las listings.**

| URL | Desktop CLS | Mobile CLS | Estado |
|---|---|---|---|
| `/` (home) | 0.00 | 0.06 | ✅ |
| `/placas-de-video` (listing) | **0.45** | **0.37** | ❌ deficiente |
| Origin completo | **0.34** | **0.35** | ❌ |

Los productos individuales no tienen muestra suficiente para CrUX (caen a "origen"), pero las listings sí dominan el promedio. Si arreglamos las listings, baja el origin completo.

### Causa raíz identificada

`ModuloCCargando` (skeleton, 289px) era ~90px más bajo que `ModuloC` real (~380px). Al hidratar `/placas-de-video`, cada fila del masonry crecía 90px → con 4-6 filas visibles = ~360-540px de shift acumulado por viewport = CLS 0.37-0.45.

Más bugs complementarios: sidebar `.left` con altura 0 en SSR, banner "Recibílo en" cambiando width, FOUT de Inter.

### Pendiente medir (ronda 4)
- CLS desktop `/placas-de-video`: bajaba a <0.1? (era 0.45)
- CLS mobile `/placas-de-video`: bajaba a <0.1? (era 0.37)
- CrUX origin (esperar 2-4 semanas)
- Verificar que `npm run build` regenera `app/assets/fonts/Inter-*-latin*.woff2`

### Pendiente atacar (próxima ronda)
- (Opcional, no urgente) `.sr-only` global en `app/layouts/desktop.vue` y `mobile.vue` para eliminar deuda latente
- Sacar `<ClientOnly>` del wrap de productos en `general.vue:103-131` (riesgoso, hay que verificar Masonry SSR)
- BootstrapVue tree-shake en `app/plugins/bootstrap.js`
- VeeValidate lazy (importado global aunque solo lo usan formularios)
- vendor splitChunks granular en `nuxt.config.js` (`vendor: true` mete todo en un chunk)
- Migrar Firebase v8 → v9 modular para tree-shaking real

## Archivos en esta carpeta

| Archivo | Contenido |
|---------|-----------|
| [[00-resumen-diagnostico-seo-performance]] | Este resumen |
| [[01-fix-cls-imagenes]] | Instrucciones para Claude Code: fix CLS de imágenes |
| [[02-fix-lcp-render-blocking]] | Instrucciones para Claude Code: fix LCP render-blocking |
| [[03-fix-header-min-height]] | Instrucciones para Claude Code: fix header sin min-height |
| [[04-fix-fuentes-innecesarias]] | Instrucciones para Claude Code: fix fuentes innecesarias |
| [[05-fix-fouc-css-tardio]] | Instrucciones para Claude Code: fix FOUC (flash sin estilos) |
| [[06-fix-cls-tbt-ronda-2]] | Ronda 2: width/height imgs, box-shadow fuera de mixins, push-notification diferido |
| [[07-fix-cls-mobile-h1-sr-only-ronda-3]] | Ronda 3: CLS mobile 0.519 (h1 sr-only colapsando) + tabular-nums cronómetro |
| [[08-fix-cls-listings-ronda-4]] | Ronda 4: CLS listings /placas-de-video (skeleton vs card mismatch) + Inter font config |
