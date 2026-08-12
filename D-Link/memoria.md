# Memoria del proyecto

Consolidado de la memoria de Claude (`~/.claude/projects/-var-www-d-link/memory/`) al 2026-08-12.

## Proyecto (project)
Estudio [[contexto|Blu]] contratado por D-Link Argentina para reposicionar la marca (perdió
relevancia/top-of-mind en ~10 años; compite contra TP-Link). Entregables en `/var/www/d-link/`:
investigación → estrategia → campaña → pitch, + landings web.

**Estado al 2026-08-12:** los 4 entregables core están completos, más 3 planes por canal, y las
piezas web: `index.html` (consumidor), `propuesta.html` (propuesta token-gated), `brand-guidelines/`
(guía de marca como web) y la **nueva familia [[plan-trabajo]]** — 2º entregable cara al cliente
deployado en `dlink.blu.net.ar` (landing + PDF de 14 slides + video 16:9 + video 9:16). Ver
[[changelog]] y [[arquitectura]].

**3 variantes de presupuesto/alcance coexisten a propósito (no unificar sin pedido):**
- docs 01–04 → **solo Argentina, ~USD 2.000/mes**.
- [[landings|propuesta.html]] → **Argentina + Chile, USD 1.800/mes**.
- [[plan-trabajo]] → **Argentina + Perú + Chile, USD 2.300/mes** (incluye el 6º workstream Site).

## Usuario (user)
Tiene un estudio de marketing digital llamado **Blu** (`blustudioinc.com`) que arma propuestas web
token-gated con lockup co-branded "<Cliente> × Blu". Detalle en [[contexto]].

**Preferencias observadas:** numerar workstreams/slides secuencialmente sin saltos en piezas cara al
cliente; logo Blu **negro sobre claro / blanco sobre oscuro** (nunca el azul `#0474f4` en piezas D-Link);
íconos flat, no emojis a color; cuando cambia contenido de [[plan-trabajo]] pide regenerar los 4
artefactos juntos ("los dos videos, la presentación y demás").

## Referencia (reference)
- Propuesta modelo (Gigabyte): `blustudioinc.com/propuestas/gigabyte?token=gbt-mkt-2026`.
- Sitio oficial D-Link LA: `la.dlink.com`. Paletas: azul insignia `#4481a7` (landings de campaña),
  teal `#0083A5`/`#0087A9` (m15-2, brand-guidelines, familia plan-trabajo).
- **Logos oficiales de Blu:** `/var/www/blu/logos/03. SVG-.../03. SVG/` (variantes B./Blu. ×
  Azul/Blanco/Gris/Negro; azul de marca Blu `#0474f4`).
- **Pipeline de video/PDF** de plan-trabajo: `.claude/scripts/render_video.py` + motor `window.__seek(t)`.
  Gotcha: la ruta HTML debe ser absoluta; screenshots con `reduced_motion="reduce"`.
- Bóveda Obsidian local: `/var/www/obsidian-hermess`, carpeta `D-Link`.

## Pendiente
Cerrar gaps de data (scraping MercadoLibre + sell-through) antes de fijar metas numéricas. Definir si
el orden Inversión/Modelo de los videos+PDF se alinea al de la landing (Modelo→Inversión).

## Ver también
[[D-Link]] · [[contexto]] · [[arquitectura]] · [[plan-trabajo]]
