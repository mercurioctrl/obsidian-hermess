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

#### 1. CLS — Imágenes sin dimensiones (CRÍTICO)
- 25 de 42 imágenes sin atributos `width`/`height`
- 17 imágenes de producto (200x200px natural) dentro de `.imagen > .producto > img` sin dimensiones HTML
- 8 imágenes above-the-fold con `loading="lazy"` innecesario
- Sin `aspect-ratio` en CSS (usa `auto`)
- 18 badges "Verificado" sin dimensiones
- Íconos del header sin dimensiones
- **Instrucciones:** [[01-fix-cls-imagenes]]

#### 2. LCP — Recursos render-blocking (ALTO)
- 23 hojas de estilo CSS (excesivo)
- Render-blocking con ahorro estimado de 1,520ms
- 348 KiB de JavaScript no utilizado
- 70 KiB de CSS no utilizado
- 6 scripts de terceros compitiendo por ancho de banda
- **Instrucciones:** [[02-fix-lcp-render-blocking]]

#### 3. Header fijo sin min-height (MEDIO)
- Header con `position: fixed` y 91px de altura pero sin `min-height`
- Puede causar CLS al cargar fuentes web
- **Instrucciones:** [[03-fix-header-min-height]]

#### 4. Fuentes web innecesarias (MEDIO)
- Roboto declarada en 3 pesos pero ninguno se usa (unloaded)
- Inter con 18 variantes declaradas, solo 3 en uso
- Slick font cargada en páginas sin carrusel
- **Instrucciones:** [[04-fix-fuentes-innecesarias]]

## Plan de acción recomendado

1. **Inmediato:** Implementar fix #1 (imágenes) — mayor impacto en CLS
2. **Corto plazo:** Fix #3 (header) y #4 (fuentes) — cambios simples
3. **Mediano plazo:** Fix #2 (render-blocking) — requiere más testing
4. **Monitoreo:** Esperar 2-4 semanas para que Google recoja datos de campo actualizados
5. **Seguimiento:** Revisar Core Web Vitals en Search Console después de los cambios

## Archivos en esta carpeta

| Archivo | Contenido |
|---------|-----------|
| [[00-resumen-diagnostico-seo-performance]] | Este resumen |
| [[01-fix-cls-imagenes]] | Instrucciones para Claude Code: fix CLS de imágenes |
| [[02-fix-lcp-render-blocking]] | Instrucciones para Claude Code: fix LCP render-blocking |
| [[03-fix-header-min-height]] | Instrucciones para Claude Code: fix header sin min-height |
| [[04-fix-fuentes-innecesarias]] | Instrucciones para Claude Code: fix fuentes innecesarias |
