# Landings HTML

Piezas HTML autocontenidas. Dos en la **raíz** (`/var/www/d-link/`) con la paleta corporativa de
campaña (azul insignia `#4481a7` + neutros); una tercera en subcarpeta con estilo de producto. Aparte,
la **familia [[plan-trabajo]]** (2º entregable cara al cliente, teal `#0083A5`).

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
  - Presupuesto **USD 1.800/mes** · Alcance **Argentina y Chile** · garantía **"hasta 10 años"**.
- **Copy de cierre:** "No vamos a gritar más fuerte. Vamos a decir algo con más respaldo." →
  "D-Link. Conectividad que responde."

## `brand-guidelines/index.html` — guía de marca como web (2026-07-16)
Presenta el contenido del PDF **Brand_Guidelines_2015** de D-Link como página web navegable,
**en inglés** (fiel 100% al documento fuente). Documenta la marca, no vende.

- Estilo tomado de la landing de producto `m15-2/` (fuentes self-hosted Inter + Plus Jakarta,
  nav fija con blur, hero con halos/rings, reveal-on-scroll, cards).
- **Paleta: teal oficial `#0087A9`** (Pantone 3145 C) — el que el propio documento especifica.
- **PDF gemelo** `brand-guidelines/D-Link-Brand-Guidelines.pdf` (25 págs, A4): generado con
  **Chrome headless** (`--print-to-pdf`) directo del HTML — **NO** pasa por `md2pdf.py`. Bloque
  `@media print` fuerza `.reveal` visible, oculta nav fija, controla saltos; índice en flexbox.

## Familia `plan-trabajo.*` — propuesta operativa (2026-08)
2º entregable cara al cliente, **deployado en `dlink.blu.net.ar`**, distinto de `propuesta.html`.
Landing `plan-trabajo.html` + deck PDF (14 slides) + video 16:9 + video 9:16. Teal `#0083A5`, 6
workstreams (incl. Site), **USD 2.300/mes**, AR·PE·CL. Detalle completo en [[plan-trabajo]].

## Ver también
[[arquitectura]] · [[contexto]] · [[plan-trabajo]] · [[pitch-punchlines-propuesta]] · [[D-Link]]
