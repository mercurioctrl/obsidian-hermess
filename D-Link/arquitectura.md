# Arquitectura del proyecto

Proyecto **NO es un repo de código**: son documentos markdown encadenados + piezas HTML
autocontenidas. No hay build, test ni lint. Vive en el web root `/var/www/d-link/`.

## Cadena de dependencia de entregables

```
01-investigacion/  →  02-estrategia-marca/  →  03-plan-campana/  →  04-pitch/
   (evidencia)          (qué + porqué)          (cómo + plata)       (cómo se cuenta)
```

Cada documento hereda del anterior. Editar uno de arriba puede invalidar afirmaciones de los de
abajo — revisar la cadena al cambiar cosas de fondo.

- **01** — [[informe-mercado]] (hallazgos con nivel de confianza) + [[analisis-catalogo]] (32 SKUs,
  define los "héroes"). `productos-dlink-argentina.json` = catálogo crudo, fuente de verdad de SKUs.
- **02** — [[estrategia-marca]]: territorio "Confiabilidad simple", 3 pilares, marca única + 2 relatos.
- **03** — [[plan-campana]] + planes por canal: [[instagram-plan]], [[facebook-plan]], [[newsletter-campana]].
- **04** — deck en slides (`04-pitch/index.html`) + [[pitch-guion-presentador]] + [[pitch-punchlines-propuesta]].
- **Raíz** — landings HTML de campaña: ver [[landings]]. Familia de propuesta operativa: ver [[plan-trabajo]].

## Piezas HTML (todas autocontenidas, sin dependencias)

| Archivo | Para quién | Paleta |
|---------|-----------|--------|
| `04-pitch/index.html` | D-Link (presentación en vivo, 17 slides) | navy `#0a1f44` + naranja `#ff7a00` |
| `index.html` (raíz) | Consumidor final | azul insignia `#4481a7` + neutros |
| `propuesta.html` (raíz) | D-Link (cliente, propuesta de Blu) | azul insignia `#4481a7` + neutros |
| `brand-guidelines/index.html` | Guía de marca como web (documento) | teal oficial `#0087A9` |
| `m15-2/index.html` | Landing de producto M15 EAGLE PRO AI | teal `#0083A5`, fuentes Inter + Plus Jakarta |
| `plan-trabajo.html` (raíz) | D-Link (cliente, propuesta operativa) | teal `#0083A5` + naranja `#F08A24`, Inter + Plus Jakarta |

Las dos landings **de campaña** (raíz) usan `#4481a7` + íconos SVG flat. `m15-2/` es una landing de
producto con su propio sistema de estilos (fuentes self-hosted, cards, reveal-on-scroll) y **sirvió de
base visual** para `brand-guidelines/` y para la **familia [[plan-trabajo]]** (misma tipografía y teal
`#0083A5`). El deck de slides conserva navy + naranja.

## Familia `plan-trabajo.*` — 4 artefactos en sincronía

Landing + PDF + 2 videos que comparten marca y contenido (ver [[plan-trabajo]]). Deployado en
`dlink.blu.net.ar`. **Al cambiar contenido, propagar a los 4.**

- **PDF** `plan-trabajo-print.html` → `plan-trabajo-dlink.pdf` (14 slides, `@page size:1280px 720px`).
  Números de pie `NN / 14` **hardcodeados** → renumerar a mano al agregar/quitar slides.
- **Videos** `plan-trabajo-video.html` (16:9 1280×720) y `plan-trabajo-video-vertical.html` (9:16
  1080×1920). Motor: un único `window.__seek(t)` scrubea todas las animaciones CSS (Web Animations API
  `currentTime`) + count-ups → live y MP4 idénticos. Escenas `.vscene[data-dur]`; contador `NN/total`
  **automático** (`durs.length`) → no requiere renumerar al agregar escenas.

## Generación de PDF/MP4 — tres caminos
- **`md2pdf.py`** (md → PDF): convierte los `.md` de entregables (01–04) a PDF con estilo navy+naranja
  vía Chrome headless. Cada carpeta queda con `.md` + `.pdf`.
- **HTML → PDF directo** (Chrome headless `--print-to-pdf`): `brand-guidelines/` y `plan-trabajo-print.html`.
  Requiere `@media print` que fuerce `.reveal` visible (dependen de IntersectionObserver), oculte nav
  fija y controle saltos. Las landings de raíz `index.html`/`propuesta.html` NO se pasan a PDF.
- **HTML → MP4** (`render_video.py`, Playwright + ffmpeg, cuadro a cuadro): solo la familia plan-trabajo.
  **Gotcha:** la ruta del HTML fuente debe ser **absoluta** (relativa → `ERR_INVALID_URL`).

## Invariantes editoriales (reglas duras)
- **Filtro de 3 pilares:** todo refuerza ANDA / FÁCIL / RESPALDADO, o no va.
- **Regla de oro:** nunca nombrar a TP-Link en comunicación al público.
- **Outlets nunca se comunican** (SKUs "CAJA DAÑADA": ODCS-942L, ODCS-2103, O311GT).
- **Beneficio, no specs** ("WiFi en toda la casa", no "AX1500 dual band").
- **Honestidad:** metas numéricas se fijan tras el mes 1, con baseline real.

## Herramientas
- `.claude/scripts/md2pdf.py` — convierte todos los `.md` de entregables (01–04) a PDF (Chrome headless).
- `.claude/scripts/render_video.py` — renderiza `plan-trabajo-video*.html` a MP4 cuadro a cuadro
  (Playwright + ffmpeg). Uso: `python3 .claude/scripts/render_video.py <fps> <salida.mp4> <fuente.html ABSOLUTA> <ancho> <alto>`.

## Ver también
[[contexto]] · [[changelog]] · [[landings]] · [[plan-trabajo]] · [[D-Link]]
