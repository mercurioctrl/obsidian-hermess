# Whisper local (transcripción para WhatsApp)

Servicio HTTP local de [whisper.cpp](https://github.com/ggerganov/whisper.cpp) para que **OpenClaw/Bily** transcriba audios de WhatsApp sin gastar tokens ni mandar audio a terceros.

Instalado por Claude (Opus 4.7) el **2026-05-23** a pedido de Catriel. Relacionado: [[Bily/Productos/Billy-Bot]], [[Bily/Productos/Bot-WhatsApp-Nativo]].

## Topología

```
WhatsApp .ogg/opus
        │
        ▼
   OpenClaw / Bily ──── shellea ───► ~/bin/transcribir <audio>
                                              │
                                              ▼
                                    ffmpeg (~/bin/ffmpeg)
                                       convierte → wav 16k mono
                                              │
                                              ▼
                              POST /inference  (multipart)
                                              │
                                              ▼
                       whisper-server systemd --user  (puerto 9000)
                       modelo ggml-small-q5_1 (~190 MB en disco, ~275 MB RAM)
```

## Archivos y rutas

| Ruta | Qué es |
|---|---|
| `~/whisper/whisper.cpp/` | Repo + build |
| `~/whisper/whisper.cpp/build/bin/whisper-server` | Binario del server |
| `~/whisper/models/ggml-small-q5_1.bin` | Modelo small multilingüe q5_1 |
| `~/whisper/logs/whisper.{log,err}` | Logs |
| `~/.config/systemd/user/whisper.service` | Unit systemd (usuario) |
| `~/bin/transcribir` | Wrapper para OpenClaw |
| `~/bin/ffmpeg`, `~/bin/ffprobe` | Binarios estáticos (sin sudo) |

## Endpoint

- URL: `http://127.0.0.1:9000/inference`
- Método: `POST` multipart/form-data
- Idioma default del server: `es` (se puede pasar `language=auto` o `language=en`, etc.)
- Solo acepta WAV/MP3 ya decodificados — para `.ogg` de WhatsApp hay que pasar por ffmpeg primero (lo hace el wrapper).

## Uso desde OpenClaw / Bily

**Forma simple (recomendada):**
```bash
~/bin/transcribir /ruta/al/audio.ogg            # idioma default: es
~/bin/transcribir /ruta/al/audio.ogg auto       # auto-detect
~/bin/transcribir /ruta/al/audio.ogg en         # inglés
```

Devuelve el texto plano por stdout. Exit code 0 si OK, ≠0 si falla.

**Forma cruda (curl):**
```bash
ffmpeg -i audio.ogg -ar 16000 -ac 1 -c:a pcm_s16le /tmp/out.wav
curl -sS -X POST \
  -F "file=@/tmp/out.wav" \
  -F "language=es" \
  -F "response_format=json" \
  -F "temperature=0.0" \
  http://127.0.0.1:9000/inference
```

## Performance medida (i3-6100, 4 cores, sin GPU)

| Audio | Modelo small q5_1 | RTF |
|---|---|---|
| 11s WAV, idioma forzado (es/en) | ~9 s | 0.8× realtime |
| 11s WAV, language=auto | ~16 s | 1.5× realtime |

Una nota de voz típica de WhatsApp (30 s) → ~25-30 s transcribiendo. Aceptable para respuestas "casi inmediatas". Si en el futuro hace falta más velocidad: subir a GPU + faster-whisper, o bajar a modelo `base` q5.

## Gestión del servicio

```bash
systemctl --user status whisper          # ver estado
systemctl --user restart whisper         # reiniciar
journalctl --user -u whisper -f          # logs en vivo
tail -f ~/whisper/logs/whisper.log       # mismo logs, vía archivo
```

## ⚠️ Pendiente: auto-start al boot

Como `systemctl --user` solo arranca cuando el usuario `hermess` está logueado, para que el servicio sobreviva reinicios sin login interactivo hay que habilitar **linger** (necesita sudo, no ejecutado todavía):

```bash
sudo loginctl enable-linger hermess
```

Mientras tanto, el servicio arranca cuando hay sesión abierta.

## Troubleshooting

- **"Invalid request"** → el archivo no es WAV/MP3 decodificable. Convertir con ffmpeg primero.
- **Texto en idioma equivocado** → el server default es `es`; pasar `language=auto` si el audio puede ser inglés.
- **Cuelgues / timeout** → revisar `journalctl --user -u whisper -n 50`. Audios > 30 min pueden necesitar `--max-context` ajustado.
- **RAM alta** → modelo small son ~275 MB residentes. Si pesa, bajar a `ggml-base-q5_1.bin` (~95 MB en disco).
