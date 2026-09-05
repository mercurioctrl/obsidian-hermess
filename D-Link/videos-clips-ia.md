# Videos / Clips IA

Videos verticales (9:16) de producto para **MercadoLibre / Reels / TikTok**, generados con IA
(fal.ai) + composición ffmpeg + **motion graphics HTML** renderizadas cuadro a cuadro. Viven en
`/var/www/d-link/clips/` (doc completa en `clips/README.md`). Bajan la estrategia de [[plan-campana]]
a contenido de redes.

## Tipos de pieza
1. **Explainer con persona** (avatar IA que habla) — UGC.
2. **Reel de producto** (beauty shots + placa).
3. **Comerciales de animación pura** (sin personas, motion graphics con el material del M15). ⭐ lo más nuevo.

## Entregables actuales
- **Comerciales animados 30s** (render local, sin costo) — 3 ángulos:
  - `comercial_m15.mp4` — overview (WiFi 6, 128 disp., beamforming, fácil).
  - `comercial_m15_ia.mp4` — **EAGLE PRO AI / red inteligente** (gauge "940 Mbps", self-healing).
  - `comercial_m15_cobertura.mp4` — **cobertura / pack de 3** (500 m², ambientes, familia, roaming).
- **Explainers** (persona hablando): `explainer_rico2_final.mp4` (mujer morocha), `explainer_B_final.mp4`
  (mujer ojos verdes), `explainer_C_hombre.mp4` (hombre común).
- **Reel** `reel_conexion.mp4` (25.5s).

## Biblioteca reutilizable (`clips/biblioteca/`)
Para no regenerar todo en cada variante. Cada activo con su `ficha.md` (prompt + IDs de fal):
- **Avatares:** `A-morocha`, `B-ojos-verdes`, `C-hombre-comun` (retrato flux + base Veo).
- **Voces (clonadas MiniMax):** `arg-01` fem (`Voiceffd48d031788466565`), `arg-02-hombre`
  (`Voice250301861788470495`). Reutilizables por `custom_voice_id` sin reclonar.
- **Casos:** los videos finales (explainers + comerciales).

## Pipeline (modelos fal.ai)
- **Video de producto:** foto real → **Veo 3** (mejor; A/B: Veo 3 > Kling 2.1 master > turbo). Kling con
  **`CFG=0.2`** evita rayos de luz inventados.
- **Persona:** retrato `flux-pro` → base **Veo 3** → lip-sync `sync-lipsync/v2` (lipsync-2-pro, bounce).
  Voz: clon **MiniMax** de sample argentino real. Subtítulos: **Whisper** → ASS quemado.
- **Motion graphics:** HTML con motor `window.__seek` → `.claude/scripts/render_video.py` (Playwright+ffmpeg).
  Escenas animadas (gauge, cobertura, mesh, count-ups) + placa. **NO imágenes pegadas** (el usuario
  rechazó el "collage").

## Paleta / estética REAL (del PSD oficial)
Fuente de verdad: `clips/material/PSD/CUS_DLINK_TRIADA...psd` (pieza de la cámara DCS-6501LH + mydlink).
- **Teal** `#0CCBD7`/`#18ccda` (brillante) → `#0587a2`/`#0693AF` (profundo), degradado radial con
  **textura de líneas concéntricas** (moiré). **Nunca el teal/verde oscuro** (rechazado).
- Fondos claros `#EEF0F2`/blanco; ink teal `#0a2e37`. Dos modos: **fondo teal + blanco** / **fondo claro + teal**.
- Logo teal `clips/material/psd_assets/dlink_teal_real.png`, íconos de línea flat (nunca emojis), badge
  "10 AÑOS DE GARANTÍA", placa estilo pieza oficial. Assets del PSD en `clips/material/psd_assets/`.

## Reglas / pendientes
- ⚠️ **Costo:** no generar video ni voz (fal) sin pedir permiso; imágenes/transcripción son baratas.
- ⚠️ **Derechos de voz:** las voces clonadas son de terceros → consentimiento antes de publicar.
- ⚠️ **`FAL_KEY`** en `clips/.env.local` — rotar (se pegó en el chat).
- El usuario iba a subir el **fondo real** a `clips/material/fondos/` (estaba en 0 bytes) para usar el bitmap exacto.

## Ver también
[[plan-campana]] · [[instagram-plan]] · [[arquitectura]] · [[contexto]] · [[changelog]] · [[D-Link]]
