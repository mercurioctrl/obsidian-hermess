# Videos / Clips IA

Videos verticales (9:16) de producto para **MercadoLibre / Reels / TikTok**, generados con IA
(fal.ai) + composición ffmpeg + escenas animadas HTML. Viven en `/var/www/d-link/clips/`
(documentación completa en `clips/README.md`). Bajan la estrategia de [[plan-campana]] a contenido
de redes.

## Entregables finales
- **`explainer_rico2_final.mp4`** (16.9s) ⭐ — Explainer con **presentadora IA** (voz argentina
  clonada) → escenas animadas (cobertura + mesh) → placa final estilo pieza oficial. Cuenta el dolor
  "el celu dice WiFi conectado pero no carga" → zonas muertas → mesh D-Link = misma velocidad en
  cada rincón.
- **`reel_conexion.mp4`** (25.5s) — Reel de producto "CONEXIÓN EN CADA RINCÓN" (3-pack + beauty
  shots Veo 3 + placa).

## Pipeline (modelos en fal.ai)
- **Video de producto:** foto real → **Veo 3** (mejor calidad; A/B: Veo 3 > Kling 2.1 master > Kling
  turbo). Con Kling, **`CFG=0.2`** es clave (evita "rayos de luz" inventados sobre el router).
- **Presentadora (talking-head):** retrato `flux-pro` → base **Veo 3** → **lip-sync** `sync-lipsync/v2`
  (lipsync-2-pro, bounce). OmniHuman es más realista en 1 pasada pero estuvo **caído** en fal.
  InfiniteTalk descartado (lento, se cuelga).
- **Voz:** clon de una voz **argentina real** con `minimax/voice-clone` (sample de un video de
  YouTube). `emotion:"neutral"` + `speed 0.97` = más calma.
- **Subtítulos:** Whisper (timings reales) → ASS quemado (contorno, sin caja).
- **Esquemas + placa:** **motion graphics HTML** (`clips/scheme-anim.html`, motor `window.__seek`)
  renderizado con `.claude/scripts/render_video.py`. El usuario rechazó los esquemas como imágenes
  estáticas ("collage") → deben ir **animados** e integrados.

## Estética
- Azul D-Link real **`#0187AA`** (muestreado de las piezas oficiales), **badges redondeados** (no
  cuadrados), **logo real** `DLinklogo.png`. La placa final replica `dlink_brand_garantia`
  (3-pack, badge "10 AÑOS DE GARANTÍA EXTENDIDA", "AX1500 Mesh · M15", `LA.DLINK.COM`).
- Claim **"El WiFi que anda"**, pilares ANDA/FÁCIL/RESPALDADO, nunca TP-Link.
- Material/stock del M15 (packshots, lifestyle, esquemas oficiales, logos, microsites) en
  `clips/material/` (carpetas `m15`, `m15-2`, `m15-3`).

## ⚠️ Derechos
La voz clonada es de una **persona real** (video de YouTube). Para publicar la campaña hace falta
**consentimiento / derechos de uso de voz**.

## Config
- `clips/.env.local` → `FAL_KEY` (⚠️ **rotar** en fal.ai: se pegó en el chat durante el desarrollo).
- `clips/.job_*` / `.url_*` → request_ids y URLs de fal (para recuperar jobs si se reinicia la PC).

## Ver también
[[plan-campana]] · [[instagram-plan]] · [[arquitectura]] · [[contexto]] · [[changelog]] · [[D-Link]]
