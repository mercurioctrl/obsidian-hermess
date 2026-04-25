---
name: replicar-microsite
description: Genera una réplica fiel en HTML+CSS+JS de un microsite de producto (ASUS, MSI, Gigabyte, NVIDIA, Razer, etc.) a partir de su URL. Descarga videos MP4, imágenes, sliders y extrae los colores reales desde el CSS del sitio original. Pensado para embeber en iframe. Invocar con `/replicarMicrosite <url>` o cuando el usuario pida "replicar", "clonar" o "hacer una versión" de un microsite de producto por URL.
---

# Replicar Microsite de Producto

Este skill replica un microsite de producto en HTML estático fiel al original, optimizado para embeber en un iframe.

## Cuándo invocar

- Usuario pide replicar / clonar / rehacer un microsite de producto con URL
- Usuario pasa un link de ASUS, MSI, Gigabyte, NVIDIA, Razer, Corsair, etc. y pide una versión HTML
- Tras invocarse: pedir al usuario confirmación del directorio de salida, idioma y si va embebido en iframe

## Parámetros a preguntar antes de empezar

1. **URL** del microsite original (obligatorio)
2. **Directorio de salida** (ej: `~/proyectos/nombre-producto/`)
3. **Idioma** del contenido final (español por defecto)
4. **Iframe?** Si sí → usar container queries + postMessage de altura
5. **CTAs comerciales?** Algunos usuarios quieren solo exposición del producto, sin botones de compra

## Proceso (en orden)

### 1. Reconocimiento del microsite

```bash
mkdir -p <output>/assets/videos
curl -s "<URL>" -o /tmp/microsite.html
```

Luego usá **Grep** (NO regex shell) sobre `/tmp/microsite.html` para detectar:
- `\.mp4|\.webm` → lista de videos y sus posters
- `swiper|slick|glide|splide|carousel` → sliders presentes
- `<link.*\.css` → archivos CSS externos para extraer colores
- `og:image|hero|kv` → imagen principal
- `<video.*poster="([^"]+)"` → posters de video
- URLs absolutas a CDNs del fabricante (dlcdnwebimgs, asset.msi.com, etc.)

### 2. Extracción de colores (CRÍTICO — no asumir colores de marca)

**⚠️ NUNCA asumas el color primario por la marca.** Aunque TUF Gaming sea "amarillo" históricamente, el microsite actual puede usar naranja (#f36d21). Cada edición especial tiene su paleta propia.

```bash
# Descargar los CSS que referencia el HTML
curl -s "<CSS_URL>" -o /tmp/site.css

# Extraer todos los hex únicos
grep -oE '#[0-9a-fA-F]{6}' /tmp/site.css | sort -u
```

Luego:
- **Descartá** grises (#000, #fff, #111, #333, #eee, #ccc…), verdes/azules de íconos UI, transparencias
- ⚠️ **MIRÁ EL CONTEXTO, no solo el color**. Un hex que solo aparece en `:hover`, `:focus`, `:active` o `::selection` **NO es el primario** — es un color de feedback de interacción. El primario está en reglas de **estado por defecto**: `a {}`, `.btn {}`, `.title {}`, variables `--primary`/`--accent`.
- Usá `grep -B1 -A1` para ver el contexto de cada hex candidato:
  ```bash
  grep -B1 -A1 -E '#ff[0-9a-f]{4}' /tmp/site.css | head -40
  ```
  Si todas las apariciones del hex están dentro de selectores con `:hover`, descartalo del candidato a primario.
- El **color primario** suele estar en: variables `--primary`, `--accent`, `color-primary`, `bg-primary`, en botones `.btn` (estado normal, no hover), en links `a {}` (no `a:hover`), en headings, o en backgrounds de banners.
- Buscá nombres semánticos: `--color-primary`, `color-cod`, `brand-color`, `accent`.
- **Distinguí dos roles separados** y guardalos como variables distintas:
  - `--primary` → acento de marca visible siempre (links default, títulos destacados, badges)
  - `--hover` → color que aparece al pasar el mouse, click, focus (puede ser distinto del primario)
- Si el CSS no expone variables claras, contá hex por **selector base** vs **pseudo-clase**:
  ```bash
  # hex que NO están en hover
  grep -E '\{[^}]*#[0-9a-f]{3,6}' /tmp/site.css | grep -v ':hover\|:focus\|:active'
  ```
- Si no hay CSS accesible, **extraé dominante del logo o hero** con ImageMagick:
  ```bash
  convert logo.png -resize 1x1 txt: | grep -oE '#[0-9A-F]{6}'
  ```

**Casos reales documentados (errores que ya cometí):**
1. ASUS TUF COD BO7: asumí amarillo `#ffd100` por la marca histórica; el real era `#f36d21` (naranja).
2. ASRock A520M/ac: extraje `#ffff00` y lo usé como primario, pero solo aparecía en `:hover`. El primario real era `#55ffff` (cyan, en `a {}` y `.Buttons`).

Guardá la paleta final en un comentario al inicio del CSS del output: `/* Extraído de <URL>: primary=#f36d21, bg=#0a0a0a */`

### 3. Descarga de assets en paralelo

Todos los videos, imágenes, iconos y logos al subdirectorio `assets/` (videos a `assets/videos/`). Usá `&` + `wait` para paralelizar:

```bash
curl -s -o assets/hero.jpg "<url1>" & \
curl -s -o assets/product.png "<url2>" & \
curl -s -o assets/videos/feature-1.mp4 "<url3>" & \
wait
```

Verificá que ningún archivo sea 0 bytes ni HTML de error.

### 4. Extracción de contenido estructurado

Del HTML crudo, extraé para cada sección:
- Título (h1/h2/h3)
- Descripción (párrafos adyacentes)
- Imágenes/videos relacionados
- Si hay swiper: las slides con su título+texto+media

Formato interno (podés mantenerlo en memoria o escribir a manifest.json):
```json
{
  "hero": { "title": "...", "subtitle": "...", "bg": "...", "product": "..." },
  "sections": [
    { "type": "ksp-grid", "items": [...] },
    { "type": "slider", "id": "durability", "title": "...", "slides": [...] },
    { "type": "video-dual", "videos": [...] },
    { "type": "specs", "rows": [...] }
  ],
  "colors": { "primary": "#f36d21", "bg": "#0a0a0a", "text": "#e5e5e5" }
}
```

### 5. Traducción

Traducí el copy al idioma pedido (español por defecto), manteniendo marcas registradas, nombres de tecnologías (RDNA, FSR, HYPR-RX, Axial-Tech) y números de modelo en su forma original.

### 6. Render del template

Usá `templates/base.html` como punto de partida. Es un template con secciones modulares. Reemplazá las variables CSS al inicio con los colores extraídos:

```css
:root {
  --primary: #f36d21;     /* del CSS original */
  --primary-soft: #ff9e1b;
  --bg: #0a0a0a;
  --bg-alt: #141414;
  --border: #262626;
  --text: #e5e5e5;
  --text-dim: #a0a0a0;
}
```

Armá las secciones según el manifest. Si hay sliders → Swiper.js desde CDN. Si hay videos → wrapper con botón play/pause custom y autoplay por IntersectionObserver.

### 7. Soporte iframe (si el usuario lo pidió)

- `container-type: inline-size` en `<body>` y media queries via `@container (max-width: ...)` en vez de viewport
- Script de `postMessage` al padre con la altura real del contenido (ResizeObserver + window load/resize)
- Sin `100vw`, sin `position: fixed`, sin scrolls internos
- El padre recibe con:
  ```js
  window.addEventListener('message', e => {
    if (e.data?.type === 'microsite:height') {
      iframe.style.height = e.data.height + 'px';
    }
  });
  ```

### 8. Sin CTAs comerciales (si el usuario lo pidió)

Quitar botones de "comprar", "reservar", "canjear", "encontrar distribuidor", "where to buy". La landing queda puramente expositiva.

## Estructura final esperada

```
<output>/
├── index.html          # archivo único con Tailwind + Swiper + GSAP desde CDN
└── assets/
    ├── hero-bg.jpg
    ├── product-front.png
    ├── icon-*.svg
    ├── logo-*.png
    └── videos/
        ├── feature-1.mp4
        ├── feature-1.jpg   # poster
        └── ...
```

## Checklist antes de entregar

- [ ] Colores extraídos del CSS original, NO asumidos por la marca
- [ ] Todos los videos descargados y funcionando (verificar tamaño > 0)
- [ ] Sliders con navegación prev/next + paginación + pausa automática de videos al cambiar slide
- [ ] Videos con botón play/pause visible y autoplay al entrar en viewport
- [ ] Responsive via container queries (no viewport)
- [ ] postMessage de altura activo (si es para iframe)
- [ ] Sin CTAs de compra si el usuario así lo pidió
- [ ] Idioma correcto en todo el copy
- [ ] `index.html` en un solo archivo (Tailwind CDN, Swiper CDN, GSAP CDN)

## Errores comunes a evitar

1. **Asumir colores por la marca** → siempre extraer del CSS real
2. **Confundir color de hover con color primario** → mirar en qué selector aparece cada hex; pseudo-clases (`:hover/:focus/:active/::selection`) NO definen el primario
3. **Usar viewport units (`vw`, `vh`) dentro de un iframe** → romper el responsive, usar container queries
4. **Descargar assets secuencialmente** → usar `&` + `wait` para paralelizar
5. **No tener fallback para sitios con anti-bot (Incapsula/Cloudflare)** → si `curl` devuelve <2 KB o contiene "Incapsula"/"challenge"/"Cloudflare", usar `web.archive.org/web/<año>/<url>` como fuente alternativa. Hacer pausas (`sleep 1`) entre tandas para no ser rate-limiteado.
6. **Olvidar los posters de video** → degrada UX si el video tarda en cargar
7. **Agregar features no pedidas** (3D, parallax complejo) → el original puede tener Three.js, pero un video loop del producto es 10× más barato y se ve igual
8. **Traducir nombres propios** ("Axial-Tech" → "Tecnología Axial" ❌) → mantener nombres de tecnología en inglés
9. **Copiar estilos viewport-fullscreen** del original si va a iframe
10. **Asumir que todos los microsites tienen videos/sliders** → algunos son puramente estáticos. El template es modular: omití secciones de video si el original no las tiene.

## Notas específicas ASUS

Cuando la URL es de `asus.com`, aplicar este subproceso. Validado con `tuf-gaming-b550m-plus-wifi-ii` (abril 2026).

### 1. Mapa de CDNs de ASUS

Probar hosts **en este orden** cuando un asset del HTML referencia `websites/global/products/<productId>/...`:

| Host | Uso | Notas |
| --- | --- | --- |
| `https://www.asus.com/websites/global/products/<id>/img/...` | **Fallback confiable para assets A+** | El CDN `dlcdnimgs.asus.com` suele devolver **403 AccessDenied** para estas rutas. Usar siempre el origen `www.asus.com`. |
| `https://dlcdnwebimgs.asus.com/gain/<uuid>/` | **Galería lightbox del producto** (original 2400×2400) | Los UUIDs salen del HTML (ver §2). Sin sufijo = tamaño completo. |
| `https://dlcdnwebimgs.asus.com/gain/<uuid>/w80/fwebp` | Thumbnails de la galería (webp) | Buenos para thumbs, pero si bajás las originales podés generar thumbs vos mismo. |
| `https://dlcdnwebimgs.asus.com/files/media/<uuid>/img/...` | Imágenes sueltas de la ficha comercial | Aparece embebido con srcset. |
| `https://www.asus.com/media/global/gallery/<slug>_setting_xxx_0_90_end_<size>.png` | Galería "carousel grande" estática | ⚠️ Ojo: puede incluir **imágenes de accesorios/gabinetes** si el producto está bundleado. **No es la galería del producto principal** — confirmar mirando una de las imágenes antes de usarla. |

Si nada funciona, caer a `web.archive.org/web/<año>/<URL>` como ya indicaba la guía general.

### 2. Cómo encontrar la galería real del producto (la del lightbox)

La galería de fotos del producto que el usuario espera ver (múltiples ángulos de la mother / placa / laptop) **no está en el HTML overview** que scrapeaste. Está en el componente `PanZoom` / `galleryShowLightboxPDC` embebido en el mismo HTML, pero como elemento separado. Señales a buscar:

```bash
grep -oE 'dlcdnwebimgs\.asus\.com/gain/[a-f0-9-]{36}' /tmp/microsite.html | sort -u
# o el marcador del lightbox
grep -oE 'zoomContainer[^"]*' /tmp/microsite.html
grep -oE 'galleryShowLightboxPDC|Lightbox__lb-container' /tmp/microsite.html
```

Los UUIDs devueltos son las fotos reales del producto (normalmente 6–10 imágenes, 2400×2400). Descargar con:

```bash
for u in <uuid1> <uuid2> ...; do
  curl -sL -o "assets/img/gallery/$(printf '%02d' $i).png" "https://dlcdnwebimgs.asus.com/gain/${u}/" &
  i=$((i+1))
done; wait
```

**⚠️ No confundir** con las imágenes del carousel `media/global/gallery/` — ésas suelen mostrar accesorios, gabinetes, kits y otros productos relacionados. El lightbox `/gain/<uuid>/` es la galería canónica del producto.

### 3. Microsites legacy ASUS (fullpage.js + owl-carousel + jquery)

Muchos productos ASUS (series TUF, PRIME de 2019–2023) usan una arquitectura legacy:
- `jquery.fullpage.css` + `fullpage.js` para navegación section-based
- `owl-carousel` para sliders
- `scrollreveal.js` para animaciones
- Tabs y sub-tabs manejados inline con scripts jQuery

**NO mantener esta estructura**, aunque sea tentador ("ya viene hecha"). Si el target es iframe, fullpage.js:
- Bloquea el scroll del contenedor padre
- Pone secciones en `position: absolute` con altura fija → rompe `postMessage` de altura
- Inyecta un nav lateral (`#fp-nav`) que no aplica en stacked layout
- Si la neutralizás con overrides, los anchors dejan de funcionar porque fullpage era quien los construía
- Los owl-carousels dejan de inicializar si cambiás el DOM lifecycle

**Hacer rebuild completo desde cero** con:
- HTML semántico sin `#hd .section .fixscreen` y derivados
- Swiper (en vez de owl-carousel) para TODOS los sliders
- Tabs implementadas con `[data-tab]` + JS vanilla (patrón en §5)
- Nav sticky propia con anchors `<a href="#seccion">` + `scroll-margin-top: calc(nav-h + 16px)` en cada `section[id]`

### 4. Patrones de galería reutilizables ASUS

**Galería lightbox de producto (principal)** — main Swiper + thumbs Swiper + lightbox full-screen:

```html
<div class="main-swiper swiper"><!-- imágenes grandes --></div>
<div class="thumbs-swiper swiper"><!-- thumbs clickeables --></div>
```

```js
var thumbs = new Swiper(thumbsEl, { slidesPerView: 6, spaceBetween: 10, watchSlidesProgress: true });
var main = new Swiper(mainEl, { thumbs: { swiper: thumbs }, navigation:{...}, pagination:{...} });
// click en imagen → abrir lightbox con misma URL, Escape y click-outside para cerrar
```

**Galería tipo Armoury Crate** (filter chips + slider por chip) — cada chip muestra 1+ imágenes. Si tiene 2+, es un mini-Swiper independiente con `pagination` + `navigation`:

```html
<div class="armoury">
  <div class="armoury-chips"> <!-- botones verticales --> </div>
  <div class="armoury-stage">
    <div class="armoury-slide-wrap is-active" data-slide="x">
      <div class="swiper"> ... </div>
    </div>
    <!-- ...más wraps ocultos -->
  </div>
</div>
```

Al cambiar chip: togglear `.is-active` en el wrap + `swiper.update()` en todos los Swipers (los ocultos no miden bien al inicializar).

**Galería de overlays cross-fade** (estilo "fan control" ASUS) — imagen base con overlays superpuestos que cambian por click de chip:

```html
<div class="fan-stage">
  <img src="base.png" class="fan-base">
  <img src="overlay-1.png" class="fan-overlay is-active" data-fan="1">
  <img src="overlay-2.png" class="fan-overlay" data-fan="2">
</div>
```
CSS: `position:absolute; inset:0; opacity:0; transition:opacity .35s` en overlays; `.is-active{opacity:1}`.

### 5. Profundidad de tabs — la galería NUNCA va 3 niveles adentro

El original ASUS esconde la Armoury Crate en **EZ DIY → Configuración → Armoury Crate** (3 niveles de tabs). Es horrible UX y el usuario no la encuentra. **Siempre surfacear galerías** como:
- Sección propia con anchor en el nav superior (`#galeria`, `#armoury`), o
- Tab de primer nivel directamente

Regla: si al hacer click en un anchor del nav la galería no aparece en el primer viewport, está mal ubicada.

### 6. Paletas ASUS conocidas

No confiar en estos valores sin validar con grep del CSS de la página específica — las líneas de producto varían edición por edición:

| Línea | Primary típico | Soft/hover | Fuente CSS |
| --- | --- | --- | --- |
| TUF Gaming (clásico) | `#f5ba00` (oro) | `#fabf3a` | `hd-main.css` |
| TUF Gaming × COD BO7 | `#f36d21` (naranja) | `#ff9e1b` | edición especial |
| ROG Strix | rojo `#aa2328` o cyan según edición | variable | — |
| ASRock Steel Legend | `#55ffff` (cyan) | — | confirmado |

## Checklist específico ASUS (agregar al general)

- [ ] Si el HTML original usa `fullpage.js` o `owl-carousel` → **rebuild, no patch**
- [ ] Descargar galería del lightbox con UUIDs de `dlcdnwebimgs.asus.com/gain/`
- [ ] Verificar que los assets que bajás no son 163-byte errors de `dlcdnimgs` — usar `www.asus.com/websites/...` como primary
- [ ] Ninguna galería termina a más de 1 nivel de profundidad del nav principal
- [ ] Sliders con `swiper.update()` tras cada toggle de tab (resuelve glitches de medición)

## Archivos del skill

- `templates/base.html` — template HTML base con todas las secciones modulares y Tailwind/Swiper/GSAP ya cargados. Reemplazar las variables CSS al inicio con los colores extraídos.
- `scripts/scrape.sh` — helper bash que descarga HTML+CSS, hace greps básicos de mp4/swiper/colores. Para reconocimiento rápido.
