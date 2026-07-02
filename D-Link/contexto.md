# Contexto

## La agencia: Blu
El estudio de marketing del usuario se llama **Blu** (`blustudioinc.com`). Arma propuestas de marca
para clientes como páginas web token-gated, en `blustudioinc.com/propuestas/<marca>?token=<código>`.

- Referencia: propuesta de **Gigabyte** (`/propuestas/gigabyte?token=gbt-mkt-2026`) — se replicó su
  header co-branded y su grilla de 6 bloques de servicio para la [[landings|propuesta de D-Link]].
- **Token por propuesta:** formato `<marca>-mkt-2026` (D-Link → `dlk-mkt-2026`).
- **Convención de assets al deployar:** logo cliente `/clients/<marca>/<marca>.png`, logo Blu
  `/img/logo.svg`. En `propuesta.html` el logo de Blu va inline (SVG); el de D-Link, wordmark de
  texto (aún no existe `/clients/dlink/dlink.png` en su server → 404).

## El cliente y el problema
D-Link Argentina está por contratar a Blu. En ~10 años perdió prestigio y top-of-mind; la gente
ya no se identifica con la marca y le cuesta competir contra TP-Link (líder). El producto es bueno:
el problema es **relevancia**, no calidad.

## Decisiones del usuario durante el trabajo
- La `propuesta.html` se editó mucho: se **removieron** las secciones Roadmap, Entregables y
  "Necesitamos"; se reescribió el copy en tono más positivo ("D-Link tiene producto, garantía y
  respaldo; el desafío es convertirlo en relevancia").
- Se pidió **paleta corporativa real** (`#4481a7` + neutros) en vez del teal oficial `#0087A9`, y
  **íconos flat** en vez de emojis a color.
- **Presupuesto y alcance divergen a propósito** en la propuesta (1.800 / Argentina+Chile) respecto
  del resto de los entregables (2.000 / Argentina). Al bajar a 1.800 se pidió explícitamente NO
  tocar los otros archivos.

## Gap a cerrar (antes de fijar metas)
Scraping de MercadoLibre (share-of-shelf, precios, reviews vs TP-Link/Mercusys) + sell-through de
D-Link. Las metas numéricas se fijan **después del mes 1**, con baseline real.

## Ver también
[[arquitectura]] · [[landings]] · [[memoria]] · [[D-Link]]
