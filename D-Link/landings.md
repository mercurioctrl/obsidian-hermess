# Landings HTML

Piezas HTML autocontenidas. Dos en la **raíz** (`/var/www/d-link/`) con la paleta corporativa de
campaña (azul insignia `#4481a7` + neutros); una tercera en subcarpeta con estilo de producto.

## `index.html` — cara al consumidor
Landing de conversión (índice del sitio). Claim "El WiFi que anda", 3 pilares, héroes
(Mesh M15/M30, R15/R18, cámara DCS), teaser del programa Partner y captura de newsletter.
Deriva a MercadoLibre. Contenido bajado de [[estrategia-marca]] y [[plan-campana]].

## `propuesta.html` — cara a D-Link (propuesta de Blu)
Versión web navegable del pitch, hecha por el estudio [[contexto|Blu]]. Es el archivo sobre el
que el usuario más itera.

**Flujo:** hero → diagnóstico → las **4 murallas** + la grieta → estrategia → qué hacemos (plan por
canal) → inversión (**6 bloques de servicio numerados 01–06**) → KPIs → cierre.

**Particularidades:**
- **Gate por token:** `?token=dlk-mkt-2026` en la URL, o input en la pantalla "Propuesta privada".
  Client-side (disuade, no es seguridad real; el enforcement real sería server-side en la plataforma de Blu).
- **Lockup "D-Link × Blu"** en header y footer (logo de Blu SVG inline).
- **Confetti / papel picado** al clickear el CTA "Avancemos →" del cierre.
- **Divergencias deliberadas** con el resto de entregables (NO propagar salvo pedido):
  - Presupuesto **USD 1.800/mes** (el resto: 2.000).
  - Alcance **Argentina y Chile** (el resto: solo Argentina).
  - Menciona garantía **"hasta 10 años"**.
- **Copy de cierre:** "No vamos a gritar más fuerte. Vamos a decir algo con más respaldo." →
  "D-Link. Conectividad que responde."

## `brand-guidelines/index.html` — guía de marca como web (2026-07-16)
Presenta el contenido del PDF **Brand_Guidelines_2015** de D-Link como página web navegable,
**en inglés** (fiel 100% al documento fuente). Es una pieza aparte de las landings de campaña:
documenta la marca, no vende.

- **Estilo tomado de la landing de producto `m15-2/`** (fuentes self-hosted Inter + Plus Jakarta,
  nav fija con blur, hero con halos/rings, reveal-on-scroll, cards, bandas de sección).
- **Paleta: teal oficial `#0087A9`** (Pantone 3145 C) — el que el propio documento especifica en su
  Colour Palette, NO el azul insignia `#4481a7` de las landings de raíz.
- **Estructura:** hero "Connect to More" → índice (3 secciones) → **Section One: The Brand**
  (Introduction, Purpose & Values, Positioning, Brand Pillars) → **Section Two: The Brand Toolkit**
  (Tone of Voice, Logo, Sub/Co-brands, Typography, Colour Palette, Photography, Iconography) →
  **Section Three: The Brand Applications** (Stationery, Business Cards, PowerPoint, Press Releases,
  Whitepapers, Case Studies, Datasheets, Email Signatures) → cierre.
- **PDF gemelo** `brand-guidelines/D-Link-Brand-Guidelines.pdf` (25 págs, A4): generado con
  **Chrome headless** (`--print-to-pdf`) directo del HTML — **NO pasa por `md2pdf.py`**. Un bloque
  `@media print` fuerza `.reveal` visible (si no, el contenido bajo el pliegue saldría invisible por
  el IntersectionObserver), oculta la nav fija, desactiva animaciones y controla los saltos de página.
  El índice usa **flexbox** en impresión porque el grid de 3 columnas colapsa en Chrome paginado.

## Ver también
[[arquitectura]] · [[contexto]] · [[pitch-punchlines-propuesta]] · [[D-Link]]
