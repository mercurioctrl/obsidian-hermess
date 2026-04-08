# Fix CLS adicional — Header fijo sin min-height ✅ IMPLEMENTADO

> Volver a [[00-resumen-diagnostico-seo-performance|Resumen General]]
> Relacionado: [[01-fix-cls-imagenes]] (fix principal de CLS, implementar primero)
> Relacionado: [[04-fix-fuentes-innecesarias]] (fuentes que causan el shift del header)
> Anterior: [[02-fix-lcp-render-blocking]] | Siguiente: [[04-fix-fuentes-innecesarias]]

## Contexto del problema

El header del sitio libreopcion.com.ar usa `position: fixed` con una altura de 91px, pero no tiene `min-height` definido. Si las fuentes web (Inter, Font Awesome) tardan en cargar o fallan, el header puede cambiar de tamaño, provocando un layout shift que se suma al CLS de 0.38.

El sitio está construido con **Nuxt.js**.

## Datos del diagnóstico

- Header: `position: fixed`, altura medida: **91px**, `min-height: 0px` (no definido)
- El header usa el role `banner` (tag semántico `<header>` o `[role="banner"]`)
- Las fuentes Inter y Font Awesome se cargan de forma asincrónica
- Si las fuentes no cargan a tiempo, el texto del header se renderiza con fuentes del sistema (que tienen métricas diferentes), y al swapear a la fuente web, el header cambia de altura

## Estructura del header

```
banner [role="banner" / <header>]
├── link "Home" (logo)
├── input[type="search"] (buscador)
├── button "Buscar"
├── nav (carrito, notificaciones, usuario)
├── button "Recibílo en: Capital Federal..."
└── nav (Categorías, Precios flash, Vender, Favoritos, Historial)
```

## Solución aplicada

- Desktop.vue: agregado `min-height: 89.92px` (coincide con margin-top del layout desktop)
- Simple.vue: agregado `min-height: 58.92px` (coincide con margin-top del layout simple)
- Mobile.vue: ya tenía `min-height: 57.09px`, no requirió cambios
- **Branch:** `fix/fouc-critical-css-critters`

## Tareas a realizar

### 1. Agregar `min-height` al header

Buscar el componente del header/layout y agregar:

```css
header,
[role="banner"],
.cabecera,
.header {
  min-height: 91px; /* Altura real medida del header completo */
  box-sizing: border-box;
}
```

Si el header tiene dos filas (barra superior + navegación), idealmente fijar cada una:

```css
/* Barra superior (logo, buscador, iconos) */
.header-top,
.cabecera-principal {
  min-height: 50px; /* Ajustar según medición real */
}

/* Barra de navegación inferior */
.header-nav,
.cabecera-navegacion {
  min-height: 41px; /* Ajustar según medición real */
}
```

### 2. Reservar espacio para el contenido debajo del header

Como el header es `position: fixed`, el contenido principal necesita un `padding-top` o `margin-top` equivalente. Verificar que esto ya existe y que es un valor fijo (no dinámico):

```css
main,
.contenido-principal,
#__nuxt > div > main {
  padding-top: 91px; /* Debe coincidir con la altura del header */
}
```

Si actualmente se calcula dinámicamente con JavaScript (midiendo el header), cambiar a un valor fijo para evitar CLS.

### 3. Agregar `font-display: swap` con tamaño de fallback ajustado

Para minimizar el shift cuando las fuentes web reemplazan a las del sistema:

```css
/* Si definís @font-face manualmente */
@font-face {
  font-family: 'Inter';
  font-display: swap;
  size-adjust: 107%; /* Ajusta el tamaño del fallback para minimizar shift */
  src: url(...) format('woff2');
}
```

Si usás Google Fonts vía link, agregar `&display=swap`:

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
```

## Cómo encontrar los archivos

```bash
# Buscar el componente del header
grep -r "cabecera\|header\|banner" --include="*.vue" -l layouts/ components/

# Buscar estilos del header
grep -r "position.*fixed\|min-height" --include="*.vue" --include="*.css" --include="*.scss" -l layouts/ components/

# Buscar dónde se define el padding-top del body/main
grep -r "padding-top\|margin-top" --include="*.vue" --include="*.css" --include="*.scss" layouts/ components/ assets/

# Buscar font-face declarations
grep -r "@font-face\|font-display" --include="*.css" --include="*.scss" --include="*.vue" -l
```

## Verificación

1. Abrir DevTools → Elements → seleccionar el header → verificar que tiene `min-height: 91px` en Computed
2. Simular fuentes lentas: DevTools → Network → throttle a Slow 3G → recargar y observar si el header salta
3. Bloquear fuentes: DevTools → Network → Block request URL pattern `*.woff2` → recargar y verificar que el header mantiene su altura
4. Correr Lighthouse mobile y verificar que el CLS mejoró
