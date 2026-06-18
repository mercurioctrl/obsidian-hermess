# Arquitectura — informe-landing

Deck/landing de **un solo `index.html`** (HTML + CSS inline + JS inline). Sin build, sin servidor, sin dependencias externas. Se abre con doble clic y funciona offline.

## Autocontenido (~776 KB)
Para que funcione desde cualquier carpeta y los **exports sean portables**, fuentes e imágenes están embebidas como **data-URI**:
- Fuentes subseteadas a **woff2** con `pyftsubset` (Teko bajó de ~280 KB a ~16 KB c/u).
- Imágenes (logos GIGABYTE/AORUS, fondos `bg-black-1/2`, `mascot-mask`) en base64.
- La máscara de mascota se usa como `mask-image` para teñir los 3 gatos AORUS (cian/naranja/magenta).
- 0 referencias `assets/` externas; la carpeta `assets/` queda solo como fuente original.

## Sistema de slides (14)
Cada slide es `<section class="section" id="...">` con `.slide-tag` (etiqueta arriba-derecha + subrayado RGB), `.slide-no` (`NN / 14`) y `.shead` (eyebrow + h2). Navegación por dots laterales + barra de progreso. `IntersectionObserver` para los reveals y el dot activo.

## Iconos y esquemas (estética AORUS)
- **Iconos = SVG monoline inline** (no emojis). Los de tarjetas se inyectan por JS desde un objeto `ICONS` vía `data-i`. Los de esquemas son SVG inline directos: necesitan la regla base `#seccion svg{fill:none;stroke:currentColor}` o salen rellenos negros.
- Esquemas (slides 02·03·06·07): paneles con `clip-path` (bisel), etiqueta vertical naranja, fondo oscuro en degradado, header con icono + título mayúscula + barra naranja. Flechas SVG, desconexión de píxeles con punteado + icono de enlace roto, conexión con "embudo" naranja.
- **Responsive**: los esquemas colapsan a 1 columna en mobile. Ojo: el `.disc` centralizado tiene grid inline → hay que vencerlo con `!important` en el media query.

## Capa de herramientas (3 IIFEs de JS al final del body)
- **Editor** (botón Editar): ocultar/mostrar slides (ojito) y reordenar (↑↓). Mueve las `<section>` en el DOM, persiste en `localStorage.deckState`. "Restablecer original" limpia las 3 claves y recarga.
- **Presentación** (botón Presentar): fullscreen, 1 slide por vez, teclado/click/barra. El ojito oculta los controles.
- **Edición de textos** inline (contenteditable) con toolbar: negrita, blanco, naranja, limpiar y **A−/A+/↺ tamaño**. Persiste en `localStorage.deckTexts` y `localStorage.deckSizes`. Solo textos sin SVG son editables (para no romper iconos).
- **Export "Descargar HTML"**: clona el DOM, quita las herramientas de edición (queda solo Presentar + ojito), hornea textos/tamaños y quita slides ocultos.

## Dos variantes del deck
- **`index.html`** — versión **interna** (14 slides, pitch GIGABYTE+BLU, ventajas para la marca, casos con datos).
- **`reseller.html`** — versión **de cara al reseller** (7 slides). Derivada de `index.html` por **cirugía con Python**: se quitan las secciones internas (situación, oportunidad, impacto, atribución, efecto-red, modelo, ventajas-Gigabyte, diferencial), se reconstruyen `#dots`/`nav`, se renumeran los `slide-no` y se reescriben los textos a segunda persona **sin nombrar a BLU** ("GIGABYTE coordina"). Reutiliza el mismo CSS, fuentes base64 y capa de herramientas → sigue siendo editable, presentable y exportable.
- Para regenerar la variante se parte de una **copia** de `index.html`; mantener ambas en sync es manual (la reseller es un recorte curado, no un build automático).

## Sección de instalación (solo en `reseller.html`)
- Slide `#instalacion` con 4 tags listos para copiar: **GTM** (snippet head + body), **Meta Pixel**, **Google tag/GA4** y **conversión Google Ads**. IDs de ejemplo que el reseller reemplaza.
- Cada snippet va en `<pre><code id="snip-…">` con el HTML **escapado** (`&lt;script&gt;`); el botón `.copybtn` lee `code.innerText` (el navegador lo desescapa) y lo copia con `navigator.clipboard.writeText` + fallback `textarea`+`execCommand`.
- Los `<pre><code>` quedan **fuera** del selector de edición de textos (no son contenteditable) → los snippets no se pueden romper editando.

## Decisiones / gotchas
- **localStorage**: `deckState` (orden/ocultos), `deckTexts` (innerHTML por `ekey = slideId:n`), `deckSizes` (font-size inline).
- **Bug del export resuelto**: el editor mueve las secciones al final del body → el export debe **reubicarlas antes de los scripts** (si no, los scripts corren sin encontrarlas y los slides salen vacíos) y marcar `.reveal` como `.in`.
- **Validación visual**: editar con Python (`str.replace`) y renderizar con `google-chrome --headless --screenshot`. Para el export real: capturar la salida del Blob con `--dump-dom`.

## Ver también
- [[informe-landing]]
- [[stack]]
- [[contexto]]
- [[changelog]]
- [[memoria]]
