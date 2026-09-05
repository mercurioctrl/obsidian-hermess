# Changelog

## 2026-09-05 — Caso VLAN B2B + presentadora IA (OpenAI)

- **Nuevo comercial B2B "VLAN"** (`clips/comercial_vlan.mp4`, 9:16, ~50s): versión **superadora** del
  ejemplo que rebotó gerencia (`clips/ejemplo guion.mp4`, sobre switches/VLANs). Reencuadre a venta de
  resultado (ahorro + orden + seguridad), producto héroe real **DGS-1210-28P** (Smart Managed PoE),
  motion graphics con paleta/textura del PSD, voz clonada femenina (`arg-01`). Ver [[videos-clips-ia]].
- **Imágenes con gpt-image-1 (OpenAI) vía fal:** foto oficial real del switch (fondo removido),
  **switch redibujado en estilo ilustrado** (edit con referencia), esquema del **edificio/oficina**,
  ilustración "red plana / todo mezclado", y **grupos de PCs** verde/azul/naranja. Mejor calidad de
  ilustración que Kling/flux para este uso.
- **Variantes (versionadas, sin pisar):** `comercial_vlan_edificio.mp4` (escena extra del edificio),
  `comercial_vlan_v2.mp4` + `_edificio_v2.mp4` (switch y PCs ilustrados, look unificado).
- **Explainer con presentadora IA** (`comercial_vlan_presentadora.mp4`, ~48s): mujer ojos verdes
  generada con **gpt-image-1** y animada con **OmniHuman** (foto+audio→habla con lipsync), intercalada
  **3 veces** con las animaciones. Diálogo adaptado, voz clonada. Versión con **subtítulos** solo en los
  tramos de ella (`_subs.mp4`). Nuevo avatar `biblioteca/avatares/D-ojos-verdes-openai/`.
- **Reglas de trabajo confirmadas:** pedir autorización antes de **conectarse/ejecutar procesos**
  (avisar si es en lote); **nunca borrar/pisar recursos → crear versiones nuevas** (`-v2`, etc.).
- **Fix pipeline:** `render_video.py` requiere ruta HTML **absoluta** (relativa → `ERR_INVALID_URL`,
  render fallaba en silencio).


## 2026-09-05

- **Biblioteca de activos reutilizables** (`clips/biblioteca/`): avatares (A-morocha, B-ojos-verdes,
  C-hombre-comun), **voces clonadas** (arg-01 fem, arg-02-hombre) reutilizables por `custom_voice_id`,
  y casos. Scripts `clone_voice.sh`/`veo_generate.sh`. Ver [[videos-clips-ia]].
- **2 nuevos avatares:** mujer ojos verdes (B) y hombre común 40 (C, elegido de una tanda de 10 caras).
  Voz masculina clonada de un video de YouTube. Regla del usuario: **no generar video/voz (fal) sin
  preguntar** (cuesta); imágenes/transcripción sí.
- **3 comerciales de animación pura 30s** (sin personas, render HTML local, sin costo): overview,
  **EAGLE PRO AI / red inteligente** (gauge + self-healing, reusa el HUD animado del microsite m15-3),
  **cobertura / pack de 3** (500 m², ambientes, familia, roaming). Íconos de línea flat (no emojis).
- **Paleta REAL de marca desde el PSD oficial** (`clips/material/PSD/CUS_DLINK_TRIADA...`, pieza de la
  cámara DCS-6501LH + mydlink): degradado **teal** `#0CCBD7→#0587a2` con **textura de líneas
  concéntricas**; se **descartó el teal/verde oscuro** anterior. Logo teal, ink teal, fondos claros.
  Los 3 comerciales rehechos con esta lógica. Assets en `clips/material/psd_assets/`.


## 2026-09-03

- **Nuevo formato: [[videos-clips-ia|videos/clips de producto con IA]]** para MercadoLibre / Reels /
  TikTok (en `/var/www/d-link/clips/`). Dos entregables finales: **explainer con presentadora IA**
  (`explainer_rico2_final.mp4`, 16.9s) y **reel de producto** "CONEXIÓN EN CADA RINCÓN"
  (`reel_conexion.mp4`, 25.5s).
- **Pipeline nuevo con fal.ai:** Veo 3 (video de producto/base de presentadora), `sync-lipsync/v2`
  (lip-sync), `flux-pro` (retrato), `minimax/voice-clone` (voz argentina clonada), Whisper
  (subtítulos). Kling con **`CFG=0.2`** para evitar rayos de luz inventados. Scripts reutilizables en
  `clips/` (`generate.sh`, `veo_generate.sh`, `build_*.sh`) + `clips/README.md`.
- **Esquemas + placa como motion graphics animados** (no imágenes pegadas): `clips/scheme-anim.html`
  renderizado con `.claude/scripts/render_video.py`. La placa final replica la pieza oficial
  `dlink_brand_garantia` con logo real.
- **Voz:** se clonó una voz **argentina real** (sample de YouTube) porque el TTS neutro no convencía.
  ⚠️ **Derechos de voz** pendientes para publicar. Copy final corto y rioplatense (sin "che").
- **Estética:** azul D-Link real **`#0187AA`**, badges **redondeados**, logos reales, claim
  "El WiFi que anda". Material/stock del M15 organizado en `clips/material/`.
- Documentación (`clips/README.md` + memoria del proyecto) y bóveda sincronizadas.

## 2026-08-11

- **Nueva familia `plan-trabajo.*`** (2º entregable cara al cliente, deployado en `dlink.blu.net.ar`):
  landing `plan-trabajo.html` (convertida del docx `documentos/PORPUESTA DLINK INICIAL.docx`) +
  **deck PDF** `plan-trabajo-dlink.pdf` (14 slides, landscape 16:9) + **video 16:9**
  `plan-trabajo-video.mp4` + **video 9:16** vertical `plan-trabajo-video-vertical.mp4`. Ver [[plan-trabajo]].
- **Motor de video reutilizable** `.claude/scripts/render_video.py` (Playwright + ffmpeg, cuadro a
  cuadro) sobre presentaciones HTML con `window.__seek(t)` (scrubbing de animaciones CSS) → MP4
  determinista, idéntico a la reproducción en vivo. Estética moderna: malla de gradientes viva,
  blur-in, clip-reveal, count-ups, texto con brillo.
- **Contenido incorporado por el cliente:** 6º workstream **Site** (mantenimiento web no programático /
  monitoreo / seguridad) e **Inversión total USD 2.300/mes**. Divergencia propia de la familia:
  **AR·PE·CL, USD 2.300** (ver [[plan-trabajo#Divergencias]]).
- Ediciones de copy en la landing: título presupuesto → "Nuestra propuesta no contempla"; cierre →
  "Visibilidad, presencia y relevancia en el momento de compra." + 3 párrafos; renglón Google/Meta Ads
  → "(solicitar presupuesto)"; fix de márgenes en labels en negrita; "D-Link" con `nowrap` en el hero.
- **Logo Blu:** convención **negro sobre claro / blanco sobre oscuro** (se sacó el azul `#0474f4`).
- **Chibis** (`chibis/`): mascotas robot D-Link (PNG fondo negro) — pipeline chroma-key (flood-fill
  desde bordes) + recolor azul→`#0083A5`; se probaron en la landing y **se removieron** a pedido.
- Los 4 artefactos regenerados juntos con el contenido final; documentación (CLAUDE.md + memoria) y
  bóveda sincronizadas.

## 2026-07-16
- **Nueva landing `brand-guidelines/index.html`**: versión web del PDF `Brand_Guidelines_2015`
  de D-Link (contenido 100% fiel, en inglés). Estilo basado en la landing de producto `m15-2/`,
  con el **teal oficial `#0087A9`** (no el azul de campaña). Ver [[landings]].
- **PDF gemelo** `D-Link-Brand-Guidelines.pdf` (25 págs, A4) generado con **Chrome headless**
  directo del HTML mediante un bloque `@media print` (fuerza `.reveal` visible, oculta nav fija,
  controla saltos de página; índice en flexbox). **NO usa `md2pdf.py`** (ese script es md→PDF).

## 2026-07-02
- **Documentación + memoria:** actualizado `CLAUDE.md` (arquitectura, agencia Blu, herramientas) y
  la memoria del proyecto (3 notas: proyecto, [[contexto|Blu]], propuesta-landing). Sincronizada la bóveda.
- Creada [[pitch-punchlines-propuesta|chuleta de punchlines]] para presentar la propuesta (frases
  clave por sección + manejo de objeciones) + su PDF.
- `propuesta.html`: gate por token con input en pantalla; confetti al clickear "Avancemos →";
  se quitó el botón "Abrir pitch en slides".

## 2026-07-01
- `propuesta.html` (nueva landing, propuesta de Blu para D-Link, versión web del pitch): lockup
  co-branded **D-Link × Blu**, gate por token, paleta corporativa `#4481a7`, íconos SVG flat.
- Reescritura de copy a pedido del usuario: 4 murallas (se sumó "Fondos al canal"), grilla de
  **6 bloques de servicio** en Inversión (estilo Gigabyte), pilar Respaldado con "garantía hasta 10
  años", cierre nuevo. Presupuesto **1.800** y alcance **Argentina y Chile** solo en la propuesta.
- `index.html` (landing consumidor) y `propuesta.html`: migradas a paleta corporativa `#4481a7` +
  íconos SVG flat. Ambas movidas a la raíz del proyecto.

## 2026-06-30
- Planes por canal: [[instagram-plan]], [[facebook-plan]], [[newsletter-campana]].
- Deck ampliado a **17 slides** (se sumaron "Canales digitales" y "El recorrido").
- `index.html` consumidor creado con identidad D-Link.
- Script `.claude/scripts/md2pdf.py`: PDF de cada `.md` de entregables.

## 2026-06-29
- Investigación ([[informe-mercado]] + [[analisis-catalogo]]), [[estrategia-marca]],
  [[plan-campana]] y deck del pitch. Vinculación con Obsidian.

## Ver también
[[D-Link]] · [[arquitectura]] · [[contexto]] · [[plan-trabajo]] · [[videos-clips-ia]]
