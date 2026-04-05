# Claude Code - Base de Conocimiento

> Ver también: [[arquitectura]] · [[stack]]

## Información del Proyecto

- **Framework**: Nuxt 3 con Vue 3 → ver [[stack|Stack Técnico]] para versiones y dependencias
- **Estilos**: SCSS con variables globales en `assets/scss/_colors.scss` → ver [[stack#Colores de servicios|colores]]
- **i18n**: Vue I18n para internacionalización → ver [[arquitectura#i18n|config i18n]]
- **Imágenes**: @nuxt/image para optimización

## Estructura de Archivos Importantes

```
components/
├── Landing/
│   └── HeroSection.vue      # Hero principal con animación de chica
├── GlowBackground.vue      # Fondo negro con orbs azules animados (reutilizable)
├── Services/
│   ├── ServiceBg.vue        # Wrapper de GlowBackground con fixed:true
│   ├── ServiceHero.vue      # Hero de página de servicio (título, stats, CTA)
│   ├── BentoGrid.vue        # Grid de 4 cards expandibles (acordeón)
│   ├── BentoIcon.vue        # Iconos SVG animados por servicio
│   ├── ServiceProcess.vue   # Sección de 3 pasos "Cómo trabajamos"
│   ├── ServiceCTA.vue       # CTA final con botón a /hablemos?tab=cita
│   └── JobBoard.vue         # Búsquedas activas de recruiting (solo en recruiting.vue)
├── CalendarContactUs.vue    # Calendario de citas (consume API timeslots)
├── UnicornBackground.vue    # Fondo animado Unicorn Studio (solo vCard)
└── UnicornControls.vue      # Controles de fondo (bullets, solo vCard)

composables/
├── useUnicornControls.js    # Estado global para controles de fondo
└── useSeo.js                # Composable para SEO

stores/
└── auth.js                  # Pinia: auth JWT, token localStorage, apiFetch()

middleware/
└── admin.js                 # Route guard: redirige a /cmsadmin/login si no auth

layouts/
├── default.vue              # Público: Header + Footer + globalOverlay
└── admin.vue                # Admin: sidebar con nav + logout

pages/services/
├── it.vue                   # Layout: Timeline vertical
├── marketing.vue            # Layout: Cards flotantes
├── bi.vue                   # Layout: Scroll horizontal
└── recruiting.vue           # Layout: Acordeón expandible

public/img/clients/             # Logos SVG de clientes (blancos, monocromáticos)
├── asus.svg                    # viewBox recortado al contenido
├── acer.svg
├── brother.svg
├── adata.svg
└── xpg.svg

pages/cmsadmin/
├── login.vue                # Login standalone (layout: false)
├── index.vue                # Dashboard
├── contactos.vue            # Mensajes de contacto
├── citas.vue                # Gestión de citas
├── timeslots.vue            # Generar/ver/borrar horarios
└── usuarios.vue             # CRUD usuarios
```

## Admin Panel (/cmsadmin)

> Detalle de rutas y auth en [[arquitectura#Panel admin cmsadmin|arquitectura → Panel admin]] y [[arquitectura#Auth admin|arquitectura → Auth]]

**Convenciones:**
- Todas las páginas admin usan `definePageMeta({ layout: 'admin', middleware: 'admin' })`
- Login usa `definePageMeta({ layout: false })` (sin layout)
- Rutas excluidas de [[arquitectura#i18n|i18n]] en `nuxt.config.ts > i18n.pages` con `false`
- API calls via `auth.apiFetch(url, options)` que agrega Bearer token automático → ver [[stack#Backend consumido|endpoints del backend]]
- Estilos admin son scoped, dark mode (#0a0a0a fondo, #111 cards, #222 bordes)

**Para agregar nueva sección admin:**
1. Crear `pages/cmsadmin/nueva-seccion.vue`
2. Agregar `definePageMeta({ layout: 'admin', middleware: 'admin' })`
3. Agregar link en `layouts/admin.vue` nav
4. Agregar `'cmsadmin/nueva-seccion': false` en `nuxt.config.ts > i18n.pages`

## JobBoard (Búsquedas activas de Recruiting)

**Componente:** `components/Services/JobBoard.vue`
**Ubicación en página:** `recruiting.vue`, entre BentoGrid y ServiceProcess → ver [[arquitectura#Sitio público|mapa de páginas]]
**i18n keys:** `services.rcr.jobBoard.*`
**Color de acento:** `#00CFCE` (cyan) → ver [[stack#Colores de servicios|colores]]

### Estructura del componente
- **Header:** Título "Búsquedas activas" + contador "Mostrando X de Y"
- **Filtros:** 3 dropdowns (rol, tecnología, seniority) + 3 checkboxes (Remoto/Híbrido/Presencial)
- **Listado:** Filas con empresa, puesto, badges (seniority + modalidad), ubicación, tags de techs, botón "Postularme"
- **Banner empresas:** CTA "¿Necesitás incorporar talento?" → abre modal para solicitar búsqueda
- **Modal postulación (candidatos):** nombre*, email*, teléfono, LinkedIn, mensaje
- **Modal solicitud (empresas):** empresa*, contacto, email*, teléfono, puesto*, descripción

### Datos de búsquedas
Actualmente hardcodeados en el componente (array `jobs` en `ref([])`).
Cada job tiene: `id`, `company` (null = "Cliente confidencial"), `role`, `techs[]`, `seniority`, `modality`, `location`, `category`.

**Categorías disponibles:** commercial, marketing, backend, frontend, fullstack, devops, data, design, qa, pm

### Para agregar una búsqueda nueva
Agregar un objeto al array `jobs` en `JobBoard.vue`:
```js
{
  id: 11, // incrementar
  company: 'Nombre Empresa', // o null para confidencial
  role: 'Título del Puesto',
  techs: ['Tech1', 'Tech2'],
  seniority: 'junior' | 'semisenior' | 'senior',
  modality: 'remote' | 'hybrid' | 'onsite',
  location: 'AMBA, Argentina',
  category: 'commercial', // una de las categorías disponibles
}
```

### Para migrar a API (futuro)
- Reemplazar array `jobs` por `useFetch()` o `apiFetch()` al [[stack#Backend consumido|backend]]
- Crear endpoints CRUD en el backend (dominio `JobListing`)
- Agregar sección en [[#Admin Panel (/cmsadmin)|admin panel]] `/cmsadmin/busquedas`
- Los modales de postulación y solicitud también necesitarán endpoints (`POST /api/job-application`, `POST /api/job-request`)

### Patrones usados
- `--accent` CSS variable (igual que otros componentes de servicios) → ver [[stack#Colores de servicios|colores]]
- IntersectionObserver para animación de entrada escalonada
- `<TransitionGroup>` para animación de filtrado
- `<Teleport to="body">` para modales
- Estilos consistentes con ServiceProcess y ServiceCTA (mismos border-radius, paddings, colores)

## Patrones y Convenciones

### Colores de Servicios

> Tabla completa en [[stack#Colores de servicios|stack → Colores]]

```scss
$it: #00D985;          // IT - verde
$marketing: #FF00D0;   // Marketing - magenta
$bi: #9c44ff;          // Business Intelligence - violeta
$recruiting: #00CFCE;  // Recruiting - cyan
```

**Colores definidos en:** `assets/scss/_colors.scss` (variables SCSS) y hardcodeados como props `accent-color` en cada [[arquitectura#Sitio público|página de servicio]] (`pages/services/*.vue`).

**Flujo del color de acento:** Cada página pasa `accent-color="#HEX"` a los componentes hijos (ServiceHero, BentoGrid, ServiceProcess, ServiceCTA, JobBoard). Los componentes setean `--accent` como CSS variable via `:style` binding.

### Clases CSS Comunes
- `.services-detail` - Contenedor principal de páginas de servicios
- `.h-section` - Header de sección (logo + título + descripción)
- `.cont` - Contenedor con max-width centrado
- `.wrapper-transparent` - Cards con efecto glassmorphism

## Optimizaciones de Rendimiento

### Animaciones CSS Performantes

> Librerías de animación usadas: [[stack#Dependencias principales|GSAP + Lottie]]

```scss
// BIEN - Solo usar transform (GPU-accelerated)
@keyframes girlBreathing {
  0%   { transform: scale(1) translateY(0); }
  50%  { transform: scale(1.03) translateY(-0.5%); }
  100% { transform: scale(1) translateY(0); }
}

// Propiedades para forzar GPU:
will-change: transform;
backface-visibility: hidden;
transform-origin: right bottom;
```

### Evitar en Animaciones
- Múltiples propiedades animadas simultáneamente en pseudo-elementos pesados
- `translateY` combinado con `scale` en pseudo-elementos pesados
- NOTA: `slowPan` en HeroSection usa `background-position` (causa repaint) pero se mantiene porque `transform: translate()` no replica el mismo efecto visual sobre background-image. Es un trade-off aceptado.

### Patrón: Pausar animaciones al cambiar pestaña
```js
// Evita saltos al volver a la pestaña — usar en componentes con animaciones largas
document.addEventListener('visibilitychange', () => {
  element.style.animationPlayState = document.hidden ? 'paused' : 'running';
});
```

### Easing Recomendado
```scss
animation: nombre 12s cubic-bezier(0.4, 0, 0.2, 1) infinite;
```

## Fondos de Página

### GlowBackground (componente compartido)
Fondo negro (#000) con 3 orbs azules (`$azul`) animados con CSS. Posiciones aleatorias en cada visita.

**Componente:** `components/GlowBackground.vue`
**Props:**
- `fixed` (Boolean, default: false) — `position: fixed` para páginas con scroll largo (servicios, nosotros), `absolute` para páginas de viewport único (hablemos)

**Usado en:** → ver [[arquitectura#Sitio público|mapa de páginas]]
- `letsTalk.vue` — `<GlowBackground />` (absolute)
- `aboutUs.vue` — `<GlowBackground :fixed="true" />`
- `Services/ServiceBg.vue` — wrapper que pasa `fixed:true` (usado por las 4 páginas de servicios)

**Técnica:**
- 3 divs con `radial-gradient` azul + `filter: blur(120px)` + `will-change: transform`
- Animaciones CSS `alternate` de 18-25s (solo `transform`, GPU-accelerated)
- `onMounted` randomiza `top`/`left` de cada orb para que cada visita sea distinta

### Unicorn Studio (Home hero + vCard)
Fondo WebGL animado. Los controles (bullets) para cambiar escenas están extraídos a nivel de `app.vue`.

**Arquitectura:**
1. `useUnicornControls.js` - Composable con estado global
2. `UnicornBackground.vue` - Renderiza el fondo WebGL (fps: 60, dpi: 1.5)
3. `UnicornControls.vue` - Renderiza bullets, usa composable para comunicarse
4. Usado en: `Landing/HeroSection.vue` (home) y `[email].vue` (vCard)
5. Escenas JSON en `public/json/copy_of_raycast_bg_remix*.json` (~21KB c/u)
6. Librería: `public/js/unicornStudio.umd.js` (166KB)

### Hero Section (Landing/HeroSection.vue)

**Capas de animación (de atrás hacia adelante):**
1. **Unicorn Studio** (z-index: -2) — Fondo WebGL con escenas aleatorias
2. **Background image** (z-index: -1) — Fondo espacial con `slowPan` (animación de `background-position`, 60s). NOTA: `background-position` causa repaint, pero se mantiene por calidad visual.
3. **Girl image** (`::before`, z-index: 1) — Chica PNG cargada vía CSS var `--girl`. Animación `girlBreathing` (scale sutil, 30s, ease-in-out). Sin efecto glitch (removido 2026-03).
4. **Texto hero** — Título + typewriter effect (setInterval 80ms) + cursor parpadeo

**Imágenes de la chica** (`public/img/bgs/girl/`):
- WebP (usadas): mobile.webp (121KB), desktop.webp (92KB), hd.webp (193KB)
- PNG (backup): mobile.png (2MB), desktop.png (1.3MB), hd.png (3.7MB), estandar@2x.png (5MB)
- Selección automática por `window.innerWidth * devicePixelRatio` en `setGirlImage()`

**Visibilidad:** Al cambiar de pestaña, las animaciones del `.background-image` se pausan vía `visibilitychange` para evitar saltos al volver.

**Posición del texto (hero-content) por breakpoint:**
- Estándar (1281–1919px): `translateY(-35%)`
- QHD (1920–2559px): `translateY(-35%)`
- 4K (2560px+): `translateY(-35%)`
- Mobile (≤576px): `translateY(-10%)`

## Layouts de Servicios

> Cada servicio tiene su propia [[arquitectura#Sitio público|página]] y color de [[stack#Colores de servicios|acento]]

### 1. Timeline Vertical (IT)
- Línea central con `::before`
- Items alternando lados con `nth-child(odd/even)`
- Iconos posicionados sobre la línea con `position: absolute`

### 2. Cards Flotantes (Marketing)
- Sin contenedores/bordes
- Cards alternando izquierda/derecha con margin-left/right auto
- Iconos con glow sutil usando `radial-gradient` + `filter: blur`

### 3. Scroll Horizontal (BI)
- `overflow-x: auto` con `scroll-snap-type: x mandatory`
- Cards con `flex: 0 0 380px` y `scroll-snap-align: start`
- Navigation dots sincronizados con scroll

### 4. Acordeón Expandible (Recruiting)
- Estado manejado con `ref([])` para múltiples items abiertos
- Animación de altura con `max-height` y `opacity`
- Iconos +/- animados con CSS transforms
- Incluye [[#JobBoard (Búsquedas activas de Recruiting)|JobBoard]] debajo del BentoGrid

## Efectos de Texto para Contraste

Sin contenedor glass, usar text-shadow intenso:
```scss
text-shadow:
  0 0 40px rgba(0, 0, 0, 0.9),
  0 0 80px rgba(0, 0, 0, 0.7),
  0 4px 12px rgba(0, 0, 0, 0.95),
  0 2px 4px rgba(0, 0, 0, 1);
```

## Comandos Útiles

```bash
npm run dev      # Desarrollo
npm run build    # Build producción
npm run preview  # Preview del build
```
