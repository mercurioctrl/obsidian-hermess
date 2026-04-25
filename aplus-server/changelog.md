# Changelog

## 2026-04-16

### Scaffold inicial
- **init**: Estructura inicial del proyecto.
  - Caddy 2 + Fastify 4 + Docker Compose
  - HMAC signing de assets con TTL configurable
  - Rate limit por IP (30/min HTML, 300/min assets)
  - Referer check + CSP `frame-ancestors` desde env `ALLOWED_REFERERS`
  - Container watermark one-shot (ffmpeg + imagemagick) separado de compose
  - Scripts: `start.sh` (idempotente), `add-product.sh`, `watermark.sh`
  - Auto-gen de `TOKEN_SECRET` en primer `start.sh`
- **content**: primer producto agregado → `tuf-rtx5080`
- **docs**: `CLAUDE.md` del proyecto con gotchas, no-hacer, convenciones
- **obsidian**: carpeta del vault vinculada (`aplus-server/`) via `/configurarBoveda`

### Features
- **feat**: query param `?resize=1` en `GET /:product/` inyecta el script child de `@iframe-resizer` antes de `</body>`. Opt-in: sin el param no cambia nada. Permite que el retailer use el parent script de iframe-resizer para auto-ajustar el alto del iframe sin tener que modificar los `index.html` de cada slug. Ver [[aplus-server/arquitectura#Parámetros de URL soportados|arquitectura]].

### Documentación
- **docs**: `README.md` creado con:
  - Quick start + uso (agregar productos, integración en retailers)
  - Snippet canónico de iframe (adaptado al patrón `.syndication-iframe-wrapper` que ya usa Libre Opción)
  - Plan de migración de 3 fases desde `/micrositios-files/` de Libre Opción a aplus-server (piloto → gradual → cleanup), con rollback por slug vía `APLUS_WHITELIST` en el componente Nuxt
  - Deploy a VPS, tabla de env vars, troubleshooting
- **docs**: [[aplus-server/integracion-retailers|integracion-retailers.md]] en Obsidian con guía de integración + gotchas por retailer (Fravega whitelist por ticket, ML no permite iframes arbitrarios, sanitizers, CSP estricto, FAQs).

### Decisión estratégica
- **decision**: Full migration de LO → aplus-server, descartado hybrid y reverse proxy. Documentado en [[aplus-server/migracion-libreopcion|migración]] con análisis de 3 opciones y por qué se eligió (a).

### Memoria persistente
- **memory**: creados 4 archivos de memoria cross-sesión en `~/.claude/projects/-Users-hermess-www-aplus-server/memory/`:
  - `project_migration_strategy` — la decisión de full migration
  - `project_deploy_status` — estado actual (no VPS, dominio placeholder)
  - `reference_libreopcion_syndication` — detalle técnico observado en DevTools de LO
  - `feedback_decisive_recommendations` — cuando se pide "qué es lo mejor" dar un pick concreto
- **obsidian**: [[aplus-server/memoria|memoria.md]] creada como espejo navegable de la memoria.

### Producto agregado — TUF GAMING B550M-PLUS WIFI II
- **content**: replicado el microsite oficial de ASUS (`https://www.asus.com/ar/motherboards-components/motherboards/tuf-gaming/tuf-gaming-b550m-plus-wifi-ii/`) via skill `/replicarMicrosite`.
  - Slug: `tuf-gaming-b550m-plus-wifi-ii`
  - 94 assets descargados (80 imágenes, 1 video MP4 de 3.3MB, 2 WAVs, 6 libs JS + owl-carousel, 4 CSS)
  - HTML extraído del bloque `<div id="hd">` del SSR de ASUS (líneas 146-1673 del source), con overrides CSS para que las secciones fluyan (el original usa jQuery fullpage.js full-viewport; en iframe necesita auto-height)
  - Color primario extraído: `#f5ba00` (dorado TUF), validado en selectores `.txt-gold`, `#top_word`, no-hover
  - Container queries en `body { container-type: inline-size }` para responsive por ancho del iframe, no del viewport
  - 3 assets externos (fuera de la carpeta del microsite) bajados a `assets/img/external/`: `tuf_z390_intel.png`, `MyASUS.png`, `MyASUS_FAQ_SC.png`
  - Smoke test: HTTP 200 en `index.html`, video MP4, imágenes KV, CSS y JS

### Issue abierto — watermark no recursa subcarpetas ni maneja `.wav`
- El producto nuevo tiene assets en subcarpetas (`assets/img/gaming/bt/...`, `assets/video/...`, `assets/audio/...`) y audios `.wav` que `watermark/run.sh` no procesa (solo itera `$SRC/*.{jpg,png,...}` sin recursión, y no incluye `.wav` en el pass-through).
- Temporalmente se copiaron los assets directos a `content/<slug>/assets/` sin pasar por watermark.
- **Fix pendiente**: extender `watermark/run.sh` para recursar subcarpetas y agregar `.wav|.ogg|.mp3` al pass-through raw. Ver [[aplus-server/contexto|contexto]] para la lista de no-hacer.

### Refactor — Replica B550M reescrita desde cero
- **refactor**: el `index.html` del B550M se rehizo completo (antes: 1576 líneas mantenido sobre la estructura fullpage.js + owl-carousel del original ASUS; ahora: 1354 líneas con Swiper + HTML semántico). Motivo: al embeber en iframe, la arquitectura legacy de ASUS (`jquery.fullpage.js`, `position: absolute` full-viewport, nav lateral `#fp-nav`) rompía los anchors, no inicializaba los owl-carousels y perdía la galería Armoury.
- **gallerías agregadas**:
  - **Armoury Crate**: 4 filter chips + mini-Swiper por chip (2 chips tienen slider prev/next). Bajadas las 6 imágenes faltantes de `www.asus.com/websites/global/products/upuagcxvdypsklzj/img/more/armoury/` (el CDN `dlcdnimgs.asus.com` devolvía 403 AccessDenied).
  - **Galería de producto (lightbox)**: 8 fotos de la mother a 2400×2400 (~16MB) desde `https://dlcdnwebimgs.asus.com/gain/<uuid>/`. UUIDs extraídos del marcador `zoomContainer PanZoom__zoomContainer` del HTML SSR. Main Swiper + thumbs Swiper acoplados + lightbox full-screen con Escape/click-outside para cerrar.
  - **Fan control gallery**: base image + 4 overlays cross-fade controlados por 3 chips descriptivos.
- **UX**: nav sticky con 6 anchors (`Descripción / Galería / Rendimiento / EZ DIY / Gaming / Especificaciones`), `scroll-margin-top: calc(nav-h + 16px)` en cada `section[id]` para que no caigan tapados por la nav. IntersectionObserver para highlight activo.
- **Gestalt aplicado**: bandas alternadas `#0a0a0a` / `#141414` (figure/ground), KSP grid 3-col (proximidad), accent-underline 56×3 dorado bajo H2s (continuidad), tabs + sub-tabs con estado visual idéntico (similitud).
- **Paleta validada**: `#f5ba00` (primary) + `#fabf3a` (soft), extraídas de `hd-main.css` local con grep de contexto para descartar apariciones solo-en-hover.
- **Iframe-ready**: container queries + postMessage de altura al padre + sin viewport units ni position:fixed.
- **Tamaño total del producto**: ~34MB (~16MB galería lightbox 2400×2400 + ~14MB video DTS + resto assets).

### Skill `/replicarMicrosite` actualizado con aprendizajes ASUS
- **skill**: agregada sección "Notas específicas ASUS" al `SKILL.md` (`~/.claude/skills/replicar-microsite/SKILL.md`, pasó de 202 → 331 líneas). Consolida 6 subsecciones:
  1. **Mapa de CDNs de ASUS**: tabla con 4 hosts (`www.asus.com/websites/...` = fallback confiable; `dlcdnimgs` = 403; `dlcdnwebimgs/gain/<uuid>/` = lightbox 2400×2400; `media/global/gallery/` = OJO, puede traer bundle/accesorios no la mother).
  2. **Cómo encontrar la galería real** del producto vía grep de `zoomContainer` / `galleryShowLightboxPDC` + UUIDs.
  3. **Microsites legacy ASUS** (fullpage.js + owl-carousel): **rebuild, nunca patch**.
  4. **3 patrones de galería reutilizables** con snippets: lightbox main+thumbs, Armoury chips+slider, fan overlay cross-fade.
  5. **Profundidad de tabs**: galerías nunca a más de 1 nivel del nav.
  6. **Paletas ASUS conocidas**: tabla TUF / TUF×COD / ROG / ASRock.
- Checklist específico ASUS con 5 chequeos agregado al final del skill.
