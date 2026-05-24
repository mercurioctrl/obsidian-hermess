# 2026-05-23: Stack whisper local + vault wrappers — instalación completa

**Sesión:** nocturna 2026-05-23/24 con Claude (Opus 4.7 - 1M context)
**Objetivo:** que audios de WhatsApp lleguen a Bily como texto, sin gastar tokens de audio multimodal de Gemini.
**Resultado:** ✅ production end-to-end. Plus: 5 wrappers `vault-*` para que no aluciné URLs cuando corre en deepseek.

## Lo que se construyó (3 piezas + 1 abstracción)

1. **Whisper local** — whisper.cpp como systemd-user en `:9000`, modelo `ggml-small-q5_1` (~190 MB, ~0.8× realtime en este i3-6100).
2. **Sidecar Python** — `~/whisper/sidecar.py` en `:9001`, expone `/transcribe` (nativo) y `/v1/audio/transcriptions` (OpenAI-compat). Convierte cualquier audio a WAV con ffmpeg y proxea al whisper-server.
3. **Plugin OpenClaw `whisper-audio-preflight`** — engancha `message_received` (detecta audio en `~/.openclaw/media/inbound/`, dispara transcripción) y `before_prompt_build` (espera la promesa in-flight y inyecta el texto como `prependContext`). Cache keyed por `sessionKey`.
4. **Wrappers `vault-*`** — 5 comandos en `~/bin/` que encapsulan la API REST de Obsidian. Documentados en [[Claude/Vault-Wrappers]].

## Decisiones no obvias (para el yo del futuro)

- **`tools.media.audio.models` apuntando a localhost NO sirve** — OpenClaw aplica SSRF guard a providers oficiales, bloquea 127.0.0.1 sin opción de destrabar. Por eso hizo falta el plugin (fetch desde código de usuario sí pasa).
- **`child_process` está prohibido en plugins** — escaneo de seguridad bloquea install. Por eso existe el sidecar Python en lugar de shellear ffmpeg desde el plugin.
- **Cache por `sessionKey`, no `messageId`** — `before_prompt_build` no recibe messageId confiablemente.
- **`before_prompt_build` debe `await` la promesa de whisper** — sin eso, race condition: el hook dispara antes que termine la transcripción → cache miss → no inyecta.
- **Hooks conversational silenciosamente bloqueados** — hasta setear `plugins.entries.<id>.hooks.allowConversationAccess=true`. El warning solo aparece en logs info.
- **Cuando Gemini quedó sin créditos, Bily cayó a deepseek** (fallback openrouter). Deepseek aluciná URLs. Solución: wrappers `vault-*`. Ver [[Bily/MEMORIA#API canónica]].

## Reglas operativas grabadas en MEMORIA

- 🔒 Regla de Oro: única fuente de verdad = la bóveda. NUNCA crear memoria local que la reemplace.
- 🌐 URL EXACTA: `https://10.10.10.7:27124` literal — nunca simplificar.
- 🛠️ API canónica: usar wrappers `vault-*`, no escribir curl crudo salvo casos avanzados.
- 🎤 Audios WhatsApp: ya llegan transcriptos en el prompt — responder al contenido, no decir "whisper roto / fix lunes".

## Cómo iterar a futuro

Para agregar otro tipo de preprocesamiento (imágenes, PDFs, video):

1. Extender el sidecar con un endpoint nuevo (`/describe-image`, `/extract-pdf`).
2. Agregar otro hook al plugin que detecte ese contenttype en inbound y llame al endpoint correspondiente.
3. La misma estrategia de cache por sessionKey + await en `before_prompt_build` funciona.

Modelo a swappear: cuando salga `small-q8` o si pasamos a GPU → cambiar `--model` en `whisper.service` unit + restart.

## Relacionado

- [[Claude/Whisper]] — doc técnica completa del stack con troubleshooting
- [[Claude/Vault-Wrappers]] — API de los wrappers
- [[Bily/MEMORIA]] — reglas operativas grabadas para Bily
- [[Bily/Productos/Billy-Bot]] · [[Bily/Productos/Bot-WhatsApp-Nativo]] — productos que aprovechan esto
