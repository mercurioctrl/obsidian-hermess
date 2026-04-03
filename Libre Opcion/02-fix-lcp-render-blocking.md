# Fix LCP 4.1s — Render-blocking resources y scripts de terceros

> Volver a [[00-resumen-diagnostico-seo-performance|Resumen General]]
> Relacionado: [[04-fix-fuentes-innecesarias]] (fuentes innecesarias suman al peso de red)
> Anterior: [[01-fix-cls-imagenes]] | Siguiente: [[03-fix-header-min-height]]

## Contexto del problema

El LCP (Largest Contentful Paint) del sitio libreopcion.com.ar es de 4.1s en mobile, cuando debería ser menor a 2.5s. PageSpeed Insights reporta un ahorro estimado de **1,520ms** solo eliminando recursos render-blocking.

El sitio está construido con **Nuxt.js** y usa **Cloudflare** (rocket-loader.min.js presente).

## Datos del diagnóstico

- **23 hojas de estilo** CSS externas (excesivo, generan muchos round-trips)
- **12 preloads** (todos de tipo `style`)
- **27 scripts con src**, de los cuales 14 son async y 9 defer
- **6 dominios de terceros** cargando scripts: google-analytics.com, googletagmanager.com, sibautomation.com (Brevo/Sendinblue), connect.facebook.net, tracker.metricool.com, static.cloudflareinsights.com
- **JavaScript no utilizado: 348 KiB** de ahorro potencial
- **CSS no utilizado: 70 KiB** de ahorro potencial
- **7 tareas largas** en el hilo principal

## Tareas a realizar

### 1. Reducir archivos CSS render-blocking

Actualmente hay 23 archivos CSS separados que bloquean el renderizado. En Nuxt, esto se configura en `nuxt.config.js` o `nuxt.config.ts`.

**Opción A — Extraer CSS crítico (recomendado):**

```javascript
// nuxt.config.js
export default {
  build: {
    extractCSS: true,
    optimization: {
      splitChunks: {
        cacheGroups: {
          styles: {
            name: 'styles',
            test: /\.(css|vue)$/,
            chunks: 'all',
            enforce: true
          }
        }
      }
    }
  },
  render: {
    // Inline CSS crítico para la primera carga
    inlineSSR: true
  }
}
```

**Opción B — Si usan Nuxt 3 con Vite:**

```javascript
// nuxt.config.ts
export default defineNuxtConfig({
  vite: {
    build: {
      cssCodeSplit: false // Combina CSS en menos archivos
    }
  }
})
```

**Opción C — Crittical CSS plugin:**

```bash
npm install --save-dev nuxt-critters
```

```javascript
// nuxt.config.js
export default {
  modules: ['nuxt-critters'],
  critters: {
    config: {
      preload: 'swap'
    }
  }
}
```

### 2. Diferir scripts de terceros no esenciales

Los scripts de tracking (Facebook, Metricool, Sendinblue) no son necesarios para el renderizado inicial. Deben cargarse después del evento `load`.

**En nuxt.config.js, mover scripts no esenciales:**

```javascript
// nuxt.config.js
export default {
  head: {
    script: [
      // Google Tag Manager - mantener como está (necesario para analytics)
      // {
      //   src: 'https://www.googletagmanager.com/gtag/js?id=...',
      //   async: true
      // },

      // Facebook Pixel - diferir
      // QUITAR de aquí y cargar con el plugin de abajo

      // Metricool - diferir
      // QUITAR de aquí y cargar con el plugin de abajo

      // Sendinblue/Brevo - diferir
      // QUITAR de aquí y cargar con el plugin de abajo
    ]
  }
}
```

**Crear un plugin para cargar scripts después del load:**

```javascript
// plugins/deferred-scripts.client.js
export default () => {
  window.addEventListener('load', () => {
    // Facebook Pixel
    const fb = document.createElement('script')
    fb.src = 'https://connect.facebook.net/en_US/fbevents.js'
    fb.async = true
    document.head.appendChild(fb)

    // Metricool
    const mc = document.createElement('script')
    mc.src = 'https://tracker.metricool.com/resources/be.js'
    mc.async = true
    document.head.appendChild(mc)

    // Sendinblue/Brevo Automation
    const sib = document.createElement('script')
    sib.src = 'https://sibautomation.com/sa.js?key=TU_KEY_AQUI'
    sib.async = true
    document.head.appendChild(sib)
  })
}
```

```javascript
// nuxt.config.js
export default {
  plugins: [
    { src: '~/plugins/deferred-scripts.client.js', mode: 'client' }
  ]
}
```

### 3. Optimizar Cloudflare Rocket Loader

Cloudflare Rocket Loader (`rocket-loader.min.js`) está activo y puede interferir con la carga de scripts. Evaluar si es necesario:

- Ir a **Cloudflare Dashboard → Speed → Optimization → Content Optimization**
- Desactivar **Rocket Loader** si ya estás manejando la carga de scripts con Nuxt
- Alternativamente, agregar `data-cfasync="false"` a los scripts críticos que no deben ser diferidos por Rocket Loader

### 4. Reducir CSS no utilizado (70 KiB)

```bash
# Buscar CSS que puede no estar usándose
grep -r "@import\|@use" --include="*.css" --include="*.scss" --include="*.vue" -l

# Buscar si se importa una librería CSS grande completa (ej: Font Awesome, Slick)
grep -r "font-awesome\|fontawesome\|slick" --include="*.js" --include="*.vue" --include="*.css" -l
```

Si se importa Font Awesome completo, cambiar a importar solo los íconos que se usan:

```javascript
// ANTES - importa todo
import '@fortawesome/fontawesome-free/css/all.css'

// DESPUÉS - solo lo que se usa
import '@fortawesome/fontawesome-free/css/fontawesome.css'
import '@fortawesome/fontawesome-free/css/solid.css' // solo si usás fas
```

### 5. Reducir JavaScript no utilizado (348 KiB)

```bash
# Analizar el bundle
npx nuxt build --analyze

# Esto genera un reporte visual del bundle donde se puede ver
# qué módulos ocupan más espacio y cuáles no se usan
```

Buscar imports dinámicos que se puedan hacer lazy:

```javascript
// ANTES - se carga siempre
import HeavyComponent from '~/components/HeavyComponent.vue'

// DESPUÉS - se carga cuando se necesita
const HeavyComponent = () => import('~/components/HeavyComponent.vue')
```

## Cómo encontrar los archivos

```bash
# Configuración de Nuxt
find . -name "nuxt.config.*" -not -path "*/node_modules/*"

# Scripts en el head
grep -r "head\|script" nuxt.config.* --include="*.js" --include="*.ts"

# Plugins que cargan scripts de terceros
grep -r "facebook\|metricool\|sendinblue\|sibautomation\|fbevents" --include="*.js" --include="*.vue" --include="*.ts" -rl

# Archivos CSS importados
grep -r "import.*\.css\|require.*\.css" --include="*.js" --include="*.vue" --include="*.ts" -l
```

## Verificación

1. Correr `npm run build` y comparar tamaño del bundle antes/después
2. Abrir Chrome DevTools → Network → filtrar por CSS y verificar que hay menos archivos
3. Correr PageSpeed Insights y verificar que el ahorro de render-blocking bajó
4. Verificar que los scripts de terceros se cargan DESPUÉS del evento load (ver Network timeline)
5. Confirmar que el LCP mejoró (objetivo: < 2.5s)
