# Videos / Clips IA

Videos verticales (9:16) de producto para **MercadoLibre / Reels / TikTok**, generados con IA
(fal.ai + **OpenAI**) + composición ffmpeg + **motion graphics HTML** renderizadas cuadro a cuadro.
Viven en `/var/www/d-link/clips/` (doc completa en `clips/README.md`). Bajan la estrategia de
[[plan-campana]] a contenido de redes.

## Tipos de pieza
1. **Explainer con persona** (avatar IA que habla) — UGC. Ahora también **B2B con presentadora IA**.
2. **Reel de producto** (beauty shots + placa).
3. **Comerciales de animación pura** (sin personas, motion graphics).
4. **Comercial B2B ilustrado** (switch/VLAN) con ilustraciones de OpenAI. ⭐ lo más nuevo.

## Entregables actuales
- **Comerciales animados 30s** M15 (B2C): `comercial_m15.mp4` (overview), `comercial_m15_ia.mp4`
  (EAGLE PRO AI), `comercial_m15_cobertura.mp4` (cobertura / pack de 3).
- **Explainers** M15 (persona): `explainer_rico2_final.mp4`, `explainer_B_final.mp4`, `explainer_C_hombre.mp4`.
- **Reel** `reel_conexion.mp4`.
- **Caso VLAN B2B** (`clips/biblioteca/casos/vlan-b2b/`): ver abajo.

## ⭐ Caso VLAN B2B (switches, sep-2026)
Primer contenido **B2B**. Nació de **superar** un video que rebotó gerencia (`clips/ejemplo guion.mp4`,
sobre switches/VLAN): reencuadre de *"qué es una VLAN"* → **venta de resultado** (ahorro + orden +
seguridad), producto héroe real **DGS-1210-28P** (Smart Managed PoE, catálogo AR), sin slides estáticos
ni errores de armado. Versiones (todas conservadas, **no se pisan**):
- `comercial_vlan.mp4` — base, 7 escenas, ~50s, voz clonada `arg-01`.
- `comercial_vlan_edificio.mp4` — con escena extra del **edificio/oficina**.
- `comercial_vlan_v2.mp4` / `comercial_vlan_edificio_v2.mp4` — **switch y PCs ilustrados** (look unificado).
- `comercial_vlan_presentadora.mp4` — **explainer con presentadora IA** (mujer ojos verdes) intercalada
  **3 veces** con las animaciones; diálogo adaptado. `_subs.mp4` = con subtítulos **solo cuando ella habla**
  (las animaciones ya tienen su texto).
- Fuente HTML: `comercial-vlan*.html` + `comercial-vlan-explainer-anim.html`. Guion: `guion-vlan-*.md`.

## Biblioteca reutilizable (`clips/biblioteca/`)
Cada activo con su `ficha.md` (prompt + IDs de fal):
- **Avatares:** `A-morocha`, `B-ojos-verdes`, `C-hombre-comun` (flux + Veo); **`D-ojos-verdes-openai`**
  (retrato **gpt-image-1** + base **OmniHuman**). ⭐
- **Voces (clonadas MiniMax):** `arg-01` fem (`Voiceffd48d031788466565`), `arg-02-hombre`
  (`Voice250301861788470495`). Reutilizables por `custom_voice_id`.
- **Casos:** los videos finales (incluye `vlan-b2b/`).

## Pipeline (modelos)
- **Video de producto:** foto real → **Veo 3**. Kling con **`CFG=0.2`** evita rayos de luz.
- **Persona (2 caminos):** (a) retrato `flux-pro` → base **Veo 3** → `sync-lipsync/v2` (máx calidad, caro);
  (b) **OmniHuman** (`fal-ai/bytedance/omnihuman`): foto + audio → habla con lipsync en 1 paso
  (realista, mejor costo). Voz: clon **MiniMax**. Subtítulos: **Whisper** → ASS quemado.
- **Ilustración (OpenAI):** **gpt-image-1 vía fal** (`fal-ai/gpt-image-1/text-to-image` y `/edit-image`
  con imagen de referencia) — mejor calidad que Kling/flux para infografía/ilustración. Fondo removido con
  ImageMagick flood-fill + trim. **Costo:** OpenAI directo es algo más barato (sin margen); vía fal reusa
  la `FAL_KEY` (para volumen, ir directo con OpenAI).
- **Motion graphics:** HTML con motor `window.__seek` → `.claude/scripts/render_video.py` (Playwright+ffmpeg).
  ⚠️ **Gotcha:** la ruta del HTML debe ser **absoluta** (relativa → `ERR_INVALID_URL`, el render falla en silencio).

## Paleta / estética REAL (del PSD oficial)
Fuente: `clips/material/PSD/CUS_DLINK_TRIADA...psd`. **Teal** `#0CCBD7`/`#18ccda` → `#0587a2`/`#0693AF`,
degradado radial con **textura de líneas concéntricas** (nunca el teal/verde oscuro). Fondos claros
`#EEF0F2`/blanco; ink teal `#0a2e37`. Logo teal `psd_assets/dlink_teal_real.png`, íconos flat, badge
"10 AÑOS DE GARANTÍA". Assets en `clips/material/` (`switch/`, `oficina/`, `clusters/`, `personas/`, `psd_assets/`).

## Reglas / pendientes
- ⚠️ **Pedir autorización** antes de conectarse a un servicio o ejecutar un proceso (render/generación);
  avisar si es en lote. **No generar video/voz (fal) sin permiso** (cuesta); imágenes/transcripción son baratas.
- ⚠️ **Nunca borrar/pisar recursos → versionar** (`-v2`, `-v3`).
- ⚠️ **Derechos de voz clonada** (terceros) → consentimiento antes de publicar.
- ⚠️ **`FAL_KEY`** en `clips/.env.local` — rotar (se pegó en el chat).

## Ver también
[[plan-campana]] · [[instagram-plan]] · [[arquitectura]] · [[contexto]] · [[changelog]] · [[D-Link]]
