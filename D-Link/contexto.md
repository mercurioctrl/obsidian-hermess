# Contexto

## La agencia: Blu
El estudio de marketing del usuario se llama **Blu** (`blustudioinc.com`). Arma propuestas de marca
para clientes como páginas web token-gated, en `blustudioinc.com/propuestas/<marca>?token=<código>`.

- Referencia: propuesta de **Gigabyte** (`/propuestas/gigabyte?token=gbt-mkt-2026`) — se replicó su
  header co-branded y su grilla de 6 bloques de servicio para la [[landings|propuesta de D-Link]].
- **Token por propuesta:** formato `<marca>-mkt-2026` (D-Link → `dlk-mkt-2026`).
- **Convención de assets al deployar:** logo cliente `/clients/<marca>/<marca>.png`, logo Blu
  `/img/logo.svg`. En las piezas el logo de Blu va **inline** (SVG).
- **Logos oficiales de Blu:** `/var/www/blu/logos/03. SVG-.../03. SVG/` (variantes B./Blu. ×
  Azul/Blanco/Gris/Negro). Azul de marca Blu = `#0474f4`.
- **Regla de uso del logo Blu (confirmada ago-2026):** **negro (`#000`) sobre fondo claro, blanco
  sobre fondo oscuro** — NO usar el azul `#0474f4` en piezas de D-Link (compite con el teal D-Link).

## El cliente y el problema
D-Link Argentina está por contratar a Blu. En ~10 años perdió prestigio y top-of-mind; la gente
ya no se identifica con la marca y le cuesta competir contra TP-Link (líder). El producto es bueno:
el problema es **relevancia**, no calidad.

## Decisiones del usuario durante el trabajo
- La `propuesta.html` se editó mucho: se **removieron** Roadmap, Entregables y "Necesitamos"; copy en
  tono más positivo ("D-Link tiene producto, garantía y respaldo; el desafío es la relevancia").
- Se pidió **paleta corporativa real** (`#4481a7` + neutros) e **íconos flat** (no emojis a color).
- **3 variantes de presupuesto/alcance coexisten a propósito** (al cambiar una, NO tocar las otras
  salvo pedido explícito): docs 01–04 = **AR, ~2.000/mes**; `propuesta.html` = **AR+CL, 1.800/mes**;
  [[plan-trabajo]] = **AR+PE+CL, 2.300/mes**.
- **Familia [[plan-trabajo]] (ago-2026):** 2º entregable cara al cliente, deployado en
  `dlink.blu.net.ar`. El cliente sumó el workstream **Site** e **Inversión USD 2.300/mes**. El usuario
  pide regenerar los **4 artefactos juntos** (landing + PDF + 2 videos) al cambiar contenido, y numerar
  workstreams/slides **secuencialmente sin saltos**. Los **chibis** se probaron y se removieron.

## Gap a cerrar (antes de fijar metas)
Scraping de MercadoLibre (share-of-shelf, precios, reviews vs TP-Link/Mercusys) + sell-through de
D-Link. Las metas numéricas se fijan **después del mes 1**, con baseline real.

## Ver también
[[arquitectura]] · [[landings]] · [[plan-trabajo]] · [[memoria]] · [[D-Link]]
