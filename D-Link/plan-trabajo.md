# Plan de trabajo (familia `plan-trabajo.*`)

Segundo entregable **cara al cliente** de D-Link, **independiente de la [[landings|propuesta.html]]**.
Nace de convertir a web el docx `documentos/PORPUESTA DLINK INICIAL.docx`. **Deployado en
`dlink.blu.net.ar`** (el usuario lo revisa ahí). Creado en agosto 2026.

Son **4 artefactos que comparten marca y contenido** — al cambiar contenido hay que **propagar a los 4**
(el usuario pide "regenerá los dos videos, la presentación y demás"):

| Fuente HTML | Output | Formato |
|---|---|---|
| `plan-trabajo.html` | (la landing) | web, **fuente de verdad** del contenido |
| `plan-trabajo-print.html` | `plan-trabajo-dlink.pdf` | deck A4 landscape 16:9, **14 slides** |
| `plan-trabajo-video.html` | `plan-trabajo-video.mp4` | video **16:9** 1280×720, ~68 s |
| `plan-trabajo-video-vertical.html` | `plan-trabajo-video-vertical.mp4` | video **9:16** 1080×1920 (rediseño vertical real) |

La landing tiene botones **Descargar PDF / Ver presentación / Video 16:9 / Video 9:16** que linkean a
esos outputs por nombre de archivo.

## Estética
Azul D-Link web **`#0083A5`** + naranja CTA `#F08A24`, fuentes **Plus Jakarta Sans + Inter** (reusa
`m15-2/assets/fonts/`), íconos SVG flat. Logo D-Link teal; logo **Blu inline SVG**. Convención de logo
Blu: **negro (`#000`) sobre fondo claro, blanco sobre fondo oscuro** (nunca el azul de marca `#0474f4`
en estas piezas). Ver [[contexto]].

## Contenido (los 4)
6 workstreams — E-commerce y Marketplaces · Top Accounts · Motor de Contenido · Calendarización y
Fechas · Activación y Soporte al Canal · **Site** (mantenimiento web no programático / monitoreo de
rendimiento / seguridad) — · Modelo de trabajo (5 pasos) · **Inversión USD 2.300/mes** · "**Nuestra
propuesta no contempla**" (exclusiones: viáticos, merchandising, prensa, publicidad, videos
institucionales, Google+Meta Ads) · cierre "**Visibilidad, presencia y relevancia en el momento de compra.**".

## Divergencias (3 variantes coexisten a propósito — no unificar sin pedido)
- `plan-trabajo.*` → **AR · Perú · Chile**, **USD 2.300/mes**.
- [[landings|propuesta.html]] → AR + Chile, USD 1.800/mes.
- docs 01–04 → solo AR, ~USD 2.000/mes.

## Motor de los videos + render
Un único `window.__seek(t)` scrubea todas las animaciones CSS (Web Animations API `currentTime`) +
los count-ups JS → la reproducción en vivo y el MP4 salen **idénticos y deterministas**. El contador
`NN/total` es automático → los videos NO se renumeran al agregar escenas; el **PDF SÍ** (números de pie
hardcodeados). Render con `.claude/scripts/render_video.py` (Playwright `channel=chrome` + ffmpeg,
**ruta HTML absoluta**) y Chrome `--print-to-pdf` para el deck. Detalle en [[arquitectura]].

## Preferencias del usuario observadas
- Numerar workstreams/slides **secuencialmente, sin saltos** en piezas cara al cliente.
- Los **chibis** (mascotas robot en `chibis/`) se probaron y **se removieron** (no se usan); quedan los
  PNG y el pipeline chroma-key + recolor por si se retoman.

## Ver también
[[landings]] · [[arquitectura]] · [[contexto]] · [[changelog]] · [[memoria]] · [[D-Link]]
