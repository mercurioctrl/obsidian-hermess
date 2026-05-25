# Image OCR Preflight — plugin OpenClaw para imágenes de WhatsApp

**Status: production · funcionando end-to-end · 2026-05-25**

OpenClaw recibe imágenes de WhatsApp, las pasa por `tesseract` localmente y le inyecta al LLM el **texto extraído** como contexto adicional, junto al bloque multimodal de la imagen. El modelo ya no depende solo de su visión interna para leer texto en screenshots — recibe el OCR pre-masticado.

Hecho por Claude (Opus 4.7) a pedido de Catriel, en respuesta a dos incidentes donde [[Bily]] no procesó imágenes correctamente. Espejo exacto del [[Claude/Whisper|whisper preflight]] para audios. Producto que lo va a aprovechar: [[Bily/Productos/Bot-WhatsApp-MVP/Inicio|Bily MVP]] · [[Bily/Productos/Billy-Bot|Billy-Bot]].

## El incidente que motivó esto

**2026-05-25 20:24 UTC** — Bily recibe captura de comprobante VISA, intenta `tesseract -l spa` → `command not found`. En vez de releer el bloque multimodal que ya tenía en contexto, asume "no puedo ver" y pide transcripción al usuario.

**2026-05-25 21:08 UTC** — Tras instalar tesseract, Bily recibe otra imagen y **otra vez** dice "estoy ciego". Esta vez ni siquiera intentó tesseract: probó `gemini` CLI (falla por auth), `gocr/ocrad/cuneiform` (no instalados) y se rindió. Conclusión: el problema no era la herramienta, era el criterio del agente.

**Decisión:** hook automático (no skill opcional) — igual que con audios, el texto llega pre-extraído sin que el modelo deba decidir.

## Topología completa

```
WhatsApp → Baileys (OpenClaw whatsapp plugin)
            │
            ▼
  ~/.openclaw/media/inbound/<uuid>.jpg   ← OpenClaw guarda la imagen
            │
            ▼
  [hook message_received del plugin]      ← ~/.openclaw/extensions/image-ocr-preflight/
       └─ scanea inbound/ por imagen nueva (<30s, jpg/png/webp/bmp/tiff)
       └─ execFile("tesseract", [path, "stdout", "-l", "spa+eng"])
            │
            ▼
   tesseract 5.3.4 (instalado vía apt) → texto plano (stdout)
            │
            ▼  texto extraído
            │
   plugin guarda en cache (keyed por sessionKey, TTL 5min)
            │
            ▼
  [hook before_prompt_build del plugin]
       └─ await la promesa in-flight (bloquea LLM hasta tener OCR)
       └─ si text.length ≥ 3 chars → prependContext con:
          "[Imagen del usuario, texto extraído localmente con tesseract OCR
            — el archivo original sigue disponible como adjunto multimodal,
            esto es solo una ayuda para texto literal]
           <texto>
           [fin del OCR]"
            │
            ▼
   LLM (gemini-3.1-pro-preview) recibe AMBOS: el OCR literal + el bloque multimodal
```

## Performance medida (prueba real 2026-05-25 21:22 UTC)

Comprobante Santander VISA (jpg 34K):
- `21:22:43.577` — detected (llega imagen)
- `21:22:45.192` — OCR ok (358 chars, **1.6s**)
- `21:22:46.088` — INJECTING (texto pegado al prompt, **+900ms**)
- **Total: ~2.5s** desde imagen entrante hasta texto en el contexto del LLM

## Config relevante en `~/.openclaw/openclaw.json`

```json
{
  "plugins": {
    "entries": {
      "image-ocr-preflight": {
        "enabled": true,
        "hooks": { "allowConversationAccess": true }
      }
    }
  }
}
```

Hot-reload aplicado al cambiar `enabled`; cambios en `index.js` sí requieren `openclaw gateway restart`.

## Defaults relevantes (overrideables en `pluginConfig`)

- `tesseractBin`: `"tesseract"` (en `PATH`, resuelve a `/usr/bin/tesseract`)
- `languages`: `"spa+eng"` (combinado para mensajes ARG que mezclan)
- `timeoutMs`: 30_000
- `minTextLength`: 3 (si el OCR devuelve <3 chars no inyecta — evita ensuciar prompt con ruido de selfies/paisajes)
- `imageExtensions`: jpg/jpeg/png/webp/bmp/tiff/tif
- `cacheTtlMs`: 5 * 60_000
- `allowedProviders`: `["whatsapp"]`
- `inboundDir`: `/home/hermess/.openclaw/media/inbound`

## Troubleshooting

- **Bily responde "estoy ciego" o no comenta el contenido** → el OCR no llegó al prompt. Chequear `openclaw logs | grep image-ocr-preflight` — si no aparece `INJECTING`, hay race o cache miss.
- **`detected` pero nunca llega `OCR ok`** → tesseract colgado o falló. Probar manual: `tesseract /home/hermess/.openclaw/media/inbound/<file>.jpg stdout -l spa+eng`.
- **`OCR ok` pero `chars=0`** → la imagen no tiene texto reconocible (selfie, foto de paisaje). El plugin no inyecta nada por `minTextLength: 3`. Comportamiento esperado.
- **Texto OCR con garabatos** → falta el lang pack del idioma correcto. Instalar: `sudo apt-get install tesseract-ocr-<lang>` (códigos ISO 639-2: `por`, `ita`, `fra`, etc.) y actualizar `languages` en config.
- **Hook bloqueado por permisos** → setear `plugins.entries.image-ocr-preflight.hooks.allowConversationAccess=true` en `openclaw.json` (igual que whisper).
- **Warning "plugin loaded without install/load-path provenance"** → benigna, mismo origen que la del whisper. Silenciable con `plugins.allow: ["image-ocr-preflight", "whisper-audio-preflight", "whatsapp"]`.

## Diferencias vs whisper preflight

| Aspecto | whisper-audio-preflight | image-ocr-preflight |
|---|---|---|
| Trigger | audios `.ogg/.opus/...` en inbound | imágenes `.jpg/.png/...` en inbound |
| Motor | sidecar HTTP (`POST :9001/transcribe`) → whisper-server (`:9000`) → ggml-small-q5_1 | `execFile("tesseract", ...)` directo, sin sidecar |
| Razón | whisper.cpp como server systemd permite reuso entre procesos + evita bloquear `child_process` (denegado en plugins) | tesseract es 1-shot rápido (<2s), no justifica server. Plugin sí permite `child_process` (esto cambió respecto a la era whisper) |
| Inyección | `[Audio del usuario, transcripto localmente con whisper.cpp] ...` | `[Imagen del usuario, texto extraído localmente con tesseract OCR — el archivo original sigue disponible como adjunto multimodal] ...` (recuerda explícitamente al LLM que la imagen original también está) |

## Archivos en disco (todo lo creado/instalado)

```
/usr/bin/tesseract                              # binario v5.3.4 (apt install)
/usr/share/tesseract-ocr/5/tessdata/            # spa, eng, osd

~/.openclaw/extensions/image-ocr-preflight/
  ├── package.json                              # peerDeps openclaw, type: module
  ├── openclaw.plugin.json                      # manifest + configSchema
  ├── index.js                                  # hooks message_received + before_prompt_build (~190 líneas)
  └── node_modules/openclaw                     # symlink al SDK del whisper preflight
```

## Próximos pasos (no hechos, opcionales)

- Agregar `plugins.allow` con `["image-ocr-preflight", "whisper-audio-preflight", "whatsapp"]` para silenciar la warning de provenance (aplicable también al de whisper).
- Si crece el volumen de imágenes con texto denso: probar `--oem 1` (LSTM only) y/o `--psm 6` (assume uniform block of text) en `runTesseract()` para mejorar accuracy en screenshots de UI.
- Soporte de PDFs: si llegan PDFs por WhatsApp, hoy quedan fuera del hook. Extender `imageExtensions` no aplica (PDF necesita pdftoppm primero). Out of scope por ahora.
- Considerar `--dpi 300` para imágenes de baja resolución (WhatsApp comprime).
- Si Bily empieza a recibir muchas imágenes sin texto (memes, fotos), el `minTextLength: 3` ya filtra. Si hace falta más fino, agregar detector de "imagen vacía de texto" antes de invocar tesseract (ahorra ~1.5s).

## Ver también

- [[Claude/Whisper|Whisper preflight]] — patrón hermano para audios; arquitectura idéntica.
- [[Claude/Vault-Wrappers|Vault Wrappers]] — mismo patrón: encapsular complejidad para que el LLM no se equivoque.
- [[Claude/MEMORIA|MEMORIA de Claude]] — índice del espacio.
- [[Bily/Productos/Bot-WhatsApp-MVP/Inicio|Bily MVP]] — el producto que reusa este stack.
