# Fix CLS 0.38 — Imágenes sin width/height y lazy loading incorrecto

> Volver a [[00-resumen-diagnostico-seo-performance|Resumen General]]
> Relacionado: [[03-fix-header-min-height]] (también contribuye al CLS)
> Siguiente: [[02-fix-lcp-render-blocking]]

## Contexto del problema

El sitio libreopcion.com.ar tiene un CLS (Cumulative Layout Shift) de 0.38 en mobile, muy por encima del umbral aceptable de 0.1. Esto afecta 73 URLs bajo el patrón `/tv` y perjudica el ranking en Google.

El sitio está construido con **Nuxt.js**. Las imágenes de productos se sirven desde `static.libreopcion.com.ar`.

## Causa raíz

- **25 de 42 imágenes** en la página `/tv` no tienen atributos HTML `width` y `height`
- **37 de 42 imágenes** usan `loading="lazy"`, incluyendo **8 imágenes above-the-fold** que no deberían ser lazy
- Las imágenes de producto no tienen `aspect-ratio` en CSS (usan `aspect-ratio: auto`)
- Los badges "Verificado" (18 unidades) y los íconos del header (carrito, notificaciones, avatar) tampoco tienen `width`/`height`

## Estructura actual del componente de producto

```
a (card de producto, display: flex)
├── div.imagen (200x197px, display: flex, padding: 10px)
│   └── div.producto (179x165px, display: flex)
│       └── img (sin width/height, loading="lazy", object-fit: contain, 179x165px por CSS)
└── div.detalle (contiene nombre, precio, botones)
    └── img (badge verificado, 16x16, tiene width="16" height="16")
```

Las imágenes naturales de producto son de **200x200px** (cuadradas).

## Tareas a realizar

### 1. Agregar `width` y `height` a las imágenes de producto

Buscar el componente Vue/Nuxt que renderiza las tarjetas de producto (probablemente en `components/` o `pages/`). El `<img>` dentro de `.producto` o `.imagen` necesita:

```html
<!-- ANTES -->
<img :src="producto.imagen" :alt="producto.nombre" loading="lazy">

<!-- DESPUÉS -->
<img :src="producto.imagen" :alt="producto.nombre" loading="lazy" width="200" height="200">
```

Usar 200x200 porque es el tamaño natural de las imágenes servidas.

### 2. Agregar `aspect-ratio` en CSS

En el archivo CSS que define `.producto img` o `.imagen img`, agregar:

```css
.imagen img,
.producto img {
  aspect-ratio: 1 / 1;
  width: 100%;
  height: auto;
  object-fit: contain;
}
```

Esto asegura que aunque el navegador no haya descargado la imagen, ya sabe cuánto espacio reservar.

### 3. Quitar `loading="lazy"` de las primeras imágenes visibles

En el componente que renderiza la grilla de productos, las primeras 4-6 tarjetas NO deben tener `loading="lazy"`. Implementar con el índice del loop:

```vue
<img
  :src="producto.imagen"
  :alt="producto.nombre"
  :loading="index < 4 ? 'eager' : 'lazy'"
  :fetchpriority="index === 0 ? 'high' : undefined"
  width="200"
  height="200"
>
```

El `fetchpriority="high"` en la primera imagen también ayuda al LCP.

### 4. Agregar `width` y `height` a los íconos del header

Buscar el componente del header/cabecera. Los íconos afectados son:

| Elemento | Clase del padre | Tamaño display | width/height a agregar |
|----------|----------------|----------------|----------------------|
| Carrito | `.cabecera-carrito` | 23x23 | `width="23" height="23"` |
| Notificaciones | `.cabecera-notificaciones` | 23x23 | `width="23" height="23"` |
| Avatar/usuario | `.icono` | 25x25 | `width="25" height="25"` |
| Ícono ubicación | `.show-modal` | 28x28 | `width="28" height="28"` |
| Ícono filtro | `.icon` | 15x15 | `width="15" height="15"` |

### 5. Agregar `width` y `height` a los badges "Verificado"

Hay 18 imágenes con `alt="Verificado"` sin dimensiones. Se muestran a 15x15px:

```html
<!-- ANTES -->
<img :src="badgeUrl" alt="Verificado">

<!-- DESPUÉS -->
<img :src="badgeUrl" alt="Verificado" width="15" height="15">
```

## Cómo encontrar los archivos

```bash
# Buscar componentes de tarjeta de producto
grep -r "producto" --include="*.vue" -l src/ components/ pages/

# Buscar dónde se renderizan las imágenes de producto
grep -r "\.imagen" --include="*.vue" -l src/ components/ pages/
grep -r "loading=\"lazy\"" --include="*.vue" -l src/ components/ pages/

# Buscar el componente del header
grep -r "cabecera-carrito\|cabecera-notificaciones" --include="*.vue" -l src/ components/ layouts/

# Buscar el badge verificado
grep -r "Verificado" --include="*.vue" -l src/ components/

# Buscar CSS de .producto o .imagen
grep -r "\.producto\|\.imagen" --include="*.css" --include="*.scss" --include="*.vue" -l
```

## Verificación

Después de hacer los cambios:

1. Abrir la página `/tv` en Chrome DevTools → Elements
2. Verificar que todas las `<img>` tengan `width` y `height`
3. Verificar que las primeras 4 imágenes NO tengan `loading="lazy"`
4. Correr Lighthouse en modo mobile y verificar que CLS < 0.1
5. Esperar 2-4 semanas para que Google recoja los datos de campo actualizados

---

## Estado: ✅ IMPLEMENTADO (2026-04-04)

**Branch:** `fix/cls-imagenes-width-height-v2` (basada en `fix/fouc-critical-css-critters`)

### Resumen de lo implementado

#### Componentes de producto modificados (7 módulos + padres)
| Módulo | Archivo | size_h | width/height |
|--------|---------|--------|-------------|
| ModuloA | `components/Productos/ModuloA.vue` | h190 | 190x190 |
| ModuloAHome | `components/Productos/ModuloAHome.vue` | h190 | 190x190 |
| ModuloB | `components/Productos/ModuloB.vue` | h165 | 165x165 |
| ModuloC | `components/Productos/ModuloC.vue` | h180 | 180x180 |
| ModuloD | `components/Productos/ModuloD.vue` | h100 | 100x100 |
| ModuloE | `components/Productos/ModuloE.vue` | h100 | 100x100 |
| ModuloFilaA | `components/Home/ModuloFilaA.vue` | h80 | 80x80 |

#### Cambios aplicados en cada módulo
- `width`/`height` HTML acorde al contenedor CSS
- `:loading="index < 4 ? 'eager' : 'lazy'"` — primeras 4 imágenes eager
- `:fetchpriority="index === 0 ? 'high' : 'auto'"` — primera imagen prioridad alta
- `aspect-ratio: 1 / 1` en CSS de `.producto img`
- Prop `index` (Number, default: 99) agregado a cada módulo
- `size_h` en URL optimizado al alto real del contenedor CSS

#### Padres modificados (pasan `:index="index"`)
- `CarouselBanner.vue`, `CarouselScroll.vue`, `Carousel.vue`
- `CarouselDosFilas.vue`, `ProductosMobile.vue`, `ProductosMobileB.vue`
- `pages/busquedas/general.vue`, `pages/mi-cuenta/favoritos.vue`, `pages/mi-cuenta/historial.vue`

#### Header — iconos con width/height
- `Carrito.vue` — `width="23" height="23"`
- `Notificaciones.vue` — `width="23" height="23"`
- `AvisoCarrito.vue` — `width="23" height="23"`

#### No requirió cambios
- Badge "Verificado" en ModuloB y ModuloC — ya tenía `width="16" height="16"`
- Galería de producto (`Galeria.vue`) — ya estaba optimizada

### Notas
- Los `size_h` en la URL controlan el alto de la imagen servida por el CDN. Se ajustaron para no servir imágenes más grandes de lo necesario (PageSpeed lo penaliza como "Properly size images")
- Las imágenes no se deforman a pesar de usar width/height cuadrado porque tienen `object-fit: contain`
