# Fix Fuentes web — Eliminar Roboto no utilizada y optimizar carga

> Volver a [[00-resumen-diagnostico-seo-performance|Resumen General]]
> Relacionado: [[03-fix-header-min-height]] (las fuentes causan el shift del header)
> Relacionado: [[02-fix-lcp-render-blocking]] (fuentes innecesarias suman al peso de red y LCP)
> Anterior: [[03-fix-header-min-height]]

## Contexto del problema

El sitio libreopcion.com.ar carga múltiples familias de fuentes web que compiten por ancho de banda y pueden causar FOUT (Flash of Unstyled Text) que contribuye al CLS. Se detectaron fuentes declaradas pero no cargadas ("unloaded"), lo que indica que se descargan innecesariamente.

El sitio está construido con **Nuxt.js**.

## Datos del diagnóstico

Fuentes detectadas en la página `/tv`:

| Fuente | Pesos | Estado |
|--------|-------|--------|
| **Inter** | 400, 500, 700 | loaded (con muchas variantes unloaded) |
| **Roboto** | 400, 500, 700 | **unloaded** (no se usa) |
| **Font Awesome 5 Free** | 900 | loaded |
| **slick** | normal | **unloaded** (solo se usa si hay carrusel) |

Problemas específicos:

- **Roboto** se declara en 3 pesos pero NINGUNO se carga → no se está usando en ningún elemento visible
- **Inter** tiene **18 variantes declaradas** pero solo 3 se cargan (400, 500, 700) → las 15 restantes son innecesarias
- **slick** es la fuente del carrusel Slick.js pero aparece como unloaded en la página `/tv` → solo debería cargarse en páginas con carrusel
- Hay **4 preconnects** configurados, lo cual es correcto

## Tareas a realizar

### 1. Eliminar la fuente Roboto

Roboto no se usa en ningún elemento visible. Buscar y eliminar su declaración:

```bash
# Buscar dónde se importa/declara Roboto
grep -r "Roboto\|roboto" --include="*.vue" --include="*.css" --include="*.scss" --include="*.js" --include="*.ts" -l

# Buscar en nuxt.config
grep -r "Roboto\|roboto" nuxt.config.*
```

Puede estar en:

- Un `@import` de Google Fonts en CSS
- Un `<link>` en `nuxt.config.js` → `head.link`
- Un `@font-face` en los archivos CSS
- Un plugin de Google Fonts para Nuxt

**Eliminar completamente** la referencia a Roboto. Si se usa como fallback en algún `font-family`, reemplazar:

```css
/* ANTES */
font-family: 'Inter', 'Roboto', sans-serif;

/* DESPUÉS */
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

### 2. Reducir variantes de Inter

Solo se necesitan 3 pesos de Inter: 400, 500, 700. Si se importa desde Google Fonts:

```html
<!-- ANTES (posiblemente importa todo) -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">

<!-- DESPUÉS (solo lo necesario) -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
```

Si se usa `@fontsource/inter` o similar:

```javascript
// ANTES
import '@fontsource/inter'  // Importa todas las variantes

// DESPUÉS
import '@fontsource/inter/400.css'
import '@fontsource/inter/500.css'
import '@fontsource/inter/700.css'
```

### 3. Cargar Slick font condicionalmente

La fuente "slick" solo es necesaria en páginas que usen el carrusel Slick.js. En la página `/tv` no hay carrusel visible, pero la fuente se declara igual.

```bash
# Buscar dónde se importa Slick
grep -r "slick" --include="*.vue" --include="*.css" --include="*.scss" --include="*.js" -l
```

Si Slick CSS se importa globalmente, moverlo a import dinámico:

```javascript
// ANTES - en nuxt.config.js o un CSS global
import 'slick-carousel/slick/slick.css'
import 'slick-carousel/slick/slick-theme.css'

// DESPUÉS - solo en el componente que usa el carrusel
// components/Carrusel.vue
<script>
export default {
  async mounted() {
    await import('slick-carousel/slick/slick.css')
    await import('slick-carousel/slick/slick-theme.css')
  }
}
</script>
```

O usar un plugin de Nuxt con carga lazy:

```javascript
// plugins/slick.client.js - solo cargar cuando se necesita
if (document.querySelector('.slick-slider')) {
  import('slick-carousel/slick/slick.css')
  import('slick-carousel/slick/slick-theme.css')
}
```

### 4. Optimizar Font Awesome

Font Awesome 5 Free (peso 900 = solid) está loaded. Verificar que no se está importando el CSS completo:

```bash
# Buscar importaciones de Font Awesome
grep -r "font-awesome\|fontawesome\|fa-" --include="*.vue" --include="*.css" --include="*.scss" --include="*.js" -l
```

Si se importa el CSS completo, considerar:

**Opción A — Importar solo el subset necesario:**

```css
/* Solo fontawesome base + solid icons */
@import '@fortawesome/fontawesome-free/css/fontawesome.css';
@import '@fortawesome/fontawesome-free/css/solid.css';
/* NO importar brands.css ni regular.css si no se usan */
```

**Opción B — Reemplazar por SVG inline:**

Si solo se usan 5-10 íconos, reemplazar Font Awesome por SVG inline en los componentes. Esto elimina la descarga de la fuente por completo.

### 5. Asegurar `font-display: swap` en todas las fuentes

Verificar que todas las declaraciones `@font-face` usen `font-display: swap`:

```bash
grep -r "@font-face" --include="*.css" --include="*.scss" --include="*.vue" -A 5
```

Si alguna no tiene `font-display: swap`, agregarla:

```css
@font-face {
  font-family: 'Inter';
  font-display: swap; /* CRÍTICO: evita texto invisible */
  src: url(...) format('woff2');
}
```

## Cómo encontrar los archivos

```bash
# Configuración de fuentes en Nuxt
grep -r "font\|Font\|google.*font" nuxt.config.* --include="*.js" --include="*.ts"

# Google Fonts links
grep -r "fonts.googleapis\|fonts.gstatic" --include="*.vue" --include="*.js" --include="*.ts" --include="*.css" -l

# @font-face declarations
grep -r "@font-face" --include="*.css" --include="*.scss" --include="*.vue" -l

# CSS global files
find assets/ static/ -name "*.css" -o -name "*.scss" 2>/dev/null
```

## Verificación

1. Después de los cambios, abrir DevTools → Network → filtrar por Font
2. Verificar que **NO** se descarga Roboto
3. Verificar que solo se descargan 3 archivos de Inter (400, 500, 700)
4. En la página `/tv`, verificar que NO se descarga slick font
5. Abrir DevTools → Console → ejecutar: `document.fonts.forEach(f => console.log(f.family, f.weight, f.status))` y verificar que no hay fuentes "unloaded" innecesarias
6. Medir el ahorro en tamaño total de descarga (objetivo: reducir al menos 100-200 KB de fonts)
