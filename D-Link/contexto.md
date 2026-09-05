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

## Cómo trabajar (reglas del usuario)
- **Pedir autorización antes de conectarse o ejecutar procesos (confirmada sep-2026):** siempre pedir
  el OK antes de **conectarse a un servicio externo** (fal.ai, API de Obsidian, yt-dlp/YouTube, subir a
  storage, cualquier API con token) o **ejecutar un proceso** (renders de video/audio, generaciones IA,
  scripts pesados). Si en la sesión se va a hacer **varias veces**, **avisar el lote por adelantado**
  ("voy a hacer N llamadas a fal para X") en vez de pedir permiso uno por uno. Extiende la regla de costo
  de video/audio a **toda** conexión/proceso. Motivo: control de costo y de cuándo se sale a la red.

- **Nunca borrar/pisar recursos (confirmada sep-2026):** al iterar entregables (HTML, MP4, imágenes,
  assets), **crear una versión nueva** (`-v2`, `-v3` o nombre descriptivo) y conservar el anterior; no
  sobrescribir. Motivo: poder volver atrás/comparar; algunos assets vienen de generaciones pagas.

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
- **[[videos-clips-ia|Videos/clips con IA] (sep-2026):** el usuario pidió clips de producto para
  MercadoLibre/redes generados por IA. Feedback iterado y confirmado:
  - Estilo **UGC "sin manos"** full-bleed (rechazó el recuadro con barras y el "collage" de imágenes
    pegadas); los esquemas deben ir **animados** (motion graphics), no estáticos.
  - **Calidad:** Veo 3 (el turbo de Kling le pareció flojo). Sin "rayos de luz" sobre el router.
  - **Voz argentina real clonada** (el TTS neutro no le gustó); más calma, sin decir "che".
  - Badges/gráficos con **esquinas redondeadas** y **logos reales**; placa final estilo pieza oficial.
  - ⚠️ **Derechos de voz** pendientes (la voz clonada es de un tercero).

- **Videos IA — avances (sep-2026):** biblioteca reutilizable de **avatares y voces clonadas**
  (mujer morocha, mujer ojos verdes, hombre común; voces arg-01 fem y arg-02-hombre). El personaje
  masculino: "menos cliché", "más normal, no tan atractivo", "menos canas" (se eligió de una tanda de 10).
  **Regla de costo:** no generar video/voz (fal) sin preguntar. **Comerciales de animación pura** (sin
  personas). **Paleta real** tomada del **PSD oficial** (teal brillante `#0CCBD7→#0587a2` + textura de
  líneas concéntricas); se rechazó el teal/verde oscuro. El usuario iba a subir el fondo real a
  `clips/material/fondos/`. Ver [[videos-clips-ia]].

- **Videos IA — Caso VLAN B2B + presentadora (sep-2026):** primer contenido **B2B** (switches/VLAN),
  nacido de superar un video que **rebotó gerencia** (`clips/ejemplo guion.mp4`). Producto héroe real
  **DGS-1210-28P**. Se sumó **gpt-image-1 de OpenAI (vía fal)** para ilustración de alta calidad (switch
  ilustrado, edificio de oficina, red plana, grupos de PCs) y **OmniHuman** para la **presentadora IA**
  (foto→habla con lipsync) intercalada 3× con las animaciones. Voz clonada femenina con diálogo adaptado;
  subtítulos solo cuando ella habla. Costo: OpenAI directo es algo más barato que vía fal, pero fal reusa
  la misma key (para volumen conviene OpenAI directo). Ver [[videos-clips-ia]].

## Gap a cerrar (antes de fijar metas)
Scraping de MercadoLibre (share-of-shelf, precios, reviews vs TP-Link/Mercusys) + sell-through de
D-Link. Las metas numéricas se fijan **después del mes 1**, con baseline real.

## Ver también
[[arquitectura]] · [[landings]] · [[plan-trabajo]] · [[videos-clips-ia]] · [[memoria]] · [[D-Link]]
