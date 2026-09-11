# Changelog

## 2026-09-11 — Fix: heroes "producto + specs" centrados

En los GIF de hero tipo **producto fijo + specs rotando** (DAP-X3060 y DCS-6501LH) el número quedaba
**separado del texto**: la caja del número era de ancho fijo, así que valores angostos ("2.5G", "2K", "8 m")
dejaban un hueco. Se rearmó la métrica como **líneas completas (número + texto) centradas como unidad**
(`.cam-line` con flex `justify-content:center`, en `gif-src/hero-dap.html` y `gif-src/hero-dcs.html`) y se
re-renderizaron `img/dap_hero.gif` e `img/dcs_hero.gif`. Los heroes mesh (M15/M30) usan otra estructura y no
tenían el problema.


## 2026-09-11 — Newsletter DAP-X3060 (Access Point B2B) — 4º template

Se agregó el **4º newsletter** al set: **DAP-X3060** (`dap-x3060-email.html`), Access Point Wi-Fi 6 AX3000 PoE.
Es la **primera pieza de email B2B** de la campaña (negocio/instaladores), en línea con el track B2B de
[[newsletter-campana]].

- **Specs reales** traídas de la ficha oficial (`dlink.com/.../dap-x3060...`) con WebFetch — **nada inventado**:
  AX3000 (2882 Mbps 5 GHz + 574 Mbps 2.4 GHz), puerto **2.5G PoE 802.3at**, 4 antenas internas 3 dBi, MU-MIMO 2×2 ·
  OFDMA · Beamforming · Band Steering, WPA3 Personal/Enterprise + RADIUS + captive portal, gestión **Nuclias
  Connect**, montaje techo/pared, 190×190×42,8 mm.
- **Hero animado** (`img/dap_hero.gif`, 2.4 MB): AP + anillos de cobertura Wi-Fi + specs rotando (3 Gbps →
  2.5G PoE → 2×2 MU-MIMO → WPA3). Fuente `gif-src/hero-dap.html` (misma técnica que la cámara: producto fijo +
  rings + specs). Imagen oficial bajada a `img/dap-x3060/`.
- **Sin sección de video** (el único video disponible es el del router EAGLE PRO AI consumer, no pega en un AP B2B).
- **Integrado al set:** 4ª pestaña en el editor, 4ª tarjeta en la muestra, y key `dap` en `servidor.py`
  (versiones compartidas también para el AP).

A confirmar: "Dónde comprar" (usé el genérico LATAM, puede no listar este SKU global), ficha técnica (apunta a la
página global `dlink.com`), y si el badge de garantía 10 años aplica a un producto B2B global.


## 2026-09-11 — Set de 3 newsletters (M30 + DCS) + editor web con versiones

Se completó el **juego de 3 templates** de email y se armó una herramienta para **editarlos y versionarlos
en equipo**. Todo en `/var/www/newsletter/`. Operacionaliza el track B2C de [[newsletter-campana]] (ver
[[newsletter-campana#10. Set de 3 templates + editor web (2026-09-11)|sección 10]]).

- **2 newsletters nuevos** con la estructura/diseño del M15 (datos **reales** de los reels, nada inventado):
  - **M30 AQUILA PRO AI** (`m30-aquila-email.html`) — Router Mesh Wi-Fi 6 AX3000. Stats: 3 Gbps · 360° ·
    5 puertos · IA. Hero mesh (routers M30 1→2→3, "360° de cobertura esférica"). GIF `img/m30_mesh.gif`,
    fuente `gif-src/hero-m30.html`.
  - **DCS-6501LH** (`dcs-6501lh-email.html`) — Cámara Wi-Fi PTZ 2K. Stats: 2K · 355° · 180° · 8 m. Hero
    cámara fija + specs rotando (nueva animación, distinta al mesh). GIF `img/dcs_hero.gif`, fuente `gif-src/hero-dcs.html`.
  - **Video teaser:** fragmentos DISTINTOS del mismo video de YouTube (`mJUJVnljncg`) — M30 = onda "Better
    Wi-Fi Channel" (~27s), DCS = escena hogar+app (~47s); el M15 usó el principio. Bajado con **yt-dlp** + FFmpeg.
- **Muestra** (`muestra-newsletters.html`): los 3 templates lado a lado (iframes a **680px = desktop real**).
- **Editor web** (`editor-newsletters.html`): edición inline de **todo el texto** (contentEditable por
  elemento, con hover resaltado), doble-click en imagen → cambiar URL, toggle **Desktop (680) / Mobile (375)**.
  Detalle: el email gatilla su CSS mobile con `max-width:620px`, por eso el "desktop" usa viewport 680.
- **Versiones COMPARTIDAS** (`servidor.py`, http.server + API): "Guardar versión" con nombre → se guarda
  **en disco del servidor** (`versiones/<k>/<id>.html` + `versiones/index.json`), **no en localStorage** →
  todos los que entran al mismo server ven la misma lista y persiste. Cargar / descargar / borrar. Server en
  `0.0.0.0:8000`; el equipo entra por `http://<IP>:8000/editor-newsletters.html`.

Pendiente a confirmar: URLs de ficha técnica (`/productos/m30/`, `/productos/dcs-6501lh/` supuestas), si el
badge de garantía 10 años aplica a la cámara, y el "Darse de baja" placeholder.


## 2026-09-10 — Email M15 (HTML animado) + envío por SMTP

Pieza de **email HTML del Mesh Router M15** (héroe B2C) producida y enviada a lista de prueba (equipo Blu
+ contactos D-Link). Vive en `/var/www/newsletter/` (no en `/var/www/d-link/`). Operacionaliza el track
B2C de [[newsletter-campana]].

- **Email:** `router-mesh-v2-fondo-gif.html` (rutas locales, para editar) + `router-mesh-v2-fondo-gif.SEND.html`
  (URLs absolutas, para enviar). Hero teal plano `#07a0bb`; secciones: stats, rendimiento Wi-Fi 6, video,
  tecnología, specs, CTA **"Dónde comprar"**, botón **ficha técnica** bajo specs, contacto/vCard, footer con
  **registro de garantía 10 años**.
- **Hero animado (GIF):** `img/m15_mesh_v3.gif` (600×452, loop 15s, ~3.2 MB). Escena "mesh": routers
  flotando 1→2→3 nodos con red/anillos/haces + Pack x1/x2/x3 + cobertura 210/370/500 m². Fuente
  `gif-src/hero-mesh-opaque.html`, render con `reels-dlink-para-compartir/tools/capture-gif.mjs` (Chrome
  headless frame-a-frame + FFmpeg, paleta 256 + dither bayer).
- **Aprendizaje clave (GIF):** el GIF **transparente** da "manchas" (alfa de 1 bit → fundidos y sombras
  blandas se posterizan; frames de transición mezclados por desajuste de fps del matte). Se resolvió con
  **bloque OPACO** cuyo fondo se funde a `#07a0bb` (igual que el hero → sin costura) y **cortes secos**
  entre estados. Ver [[contexto#Newsletter / envío de emails (sep-2026)]].
- **Envío:** por **SMTP** (`box.lio.red:465` SSL, `testing@blustudioinc.com`) con `tools/enviar-smtp.py`.
  La integración de Gmail de Claude **borra las `<img>` externas** (verificado con el `.eml`) → NO usarla
  para newsletters. Imágenes hosteadas en WordPress `https://la.dlink.com/la/wp-content/uploads/AAAA/MM/`.
- Enviado a hermess87, cmercurio@blustudioinc.com, axguidobono, catrielmercurio@outlook.com.ar y
  sol.verkindere / gaston.finkelstein / mcaycho @la.dlink.com.


## 2026-09-10 — Clip orgánico M15 (UGC con persona real IA)

- **Nuevo formato: clip UGC "orgánico"** (`clips/clip_m15_organico_v2_subs.mp4`, 9:16, ~25s): una
  persona realista se mueve por la casa mostrando el M15 mesh (B2C). Persona con **Veo 3** (image-to-video
  vía fal), varias tomas hilvanadas (hook / acción con el celu / **producto en la mano** / cierre). Voz
  masculina clonada `arg-02` + **lipsync** (`sync-lipsync/v2`) + subtítulos solo cuando habla. Ver [[videos-clips-ia]].
- **Avatar E** `biblioteca/avatares/E-hombre-casa-openai/` (retrato gpt-image, look argentino, elegido de
  4 opciones) animado con Veo 3.
- **Técnica validada "producto en la mano":** **gpt-image edit** con retrato + varias **vistas reales**
  del producto (M15 oficial de dlink.com, fondo transparente, `material/m15_angles/`) → producto fiel en
  la mano → **Veo 3 con movimiento acotado** → el producto se mantiene estable. Camino IA más cercano al
  look "clip de MercadoLibre" (los reales son filmación; la IA no maneja el producto exacto sin este truco).
- **Fondo NUEVO de marca:** `clips/material/fondos/fondo.png` (1080×1920, teal `#03B6C9→#029FB9` +
  textura) = colores a imponer; se usa como **bitmap directo** en placas/animaciones (producto
  transparente encima), no el degradado CSS.
- **Costo/estrategia:** Veo 3 = lo más caro (≈USD 3-4 por toma de 8s). Validar **toma por toma**, b-roll
  local (gratis) + producto real, Kling como alternativa barata. Saldo en `fal.ai/dashboard/billing`.
  **Google Flow** usa Veo 3 → mismo motor, se accede por la API de fal.


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
