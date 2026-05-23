# Memoria de Bily

Esta es mi memoria operativa a largo plazo.

## 🌐 URL EXACTA de la bóveda — NO simplificar JAMÁS

**Base URL literal y completa:**

```
https://10.10.10.7:27124
```

- **Protocolo:** `https` (NUNCA `http`)
- **Puerto:** `:27124` (NUNCA omitir; sin él el servidor no escucha)
- **Token:** `Bearer 38a9752ed195459b905aea91de642795077c63ac85af389f6cdef1fcbf4e9635`
- **Flag obligatoria de curl:** `-k` (cert autofirmado)

**Errores comunes que debo evitar** (han pasado y rompen todo):

| Mal ❌ | Bien ✅ |
|---|---|
| `http://10.10.10.7/vault/...` | `https://10.10.10.7:27124/vault/...` |
| `https://10.10.10.7/vault/...` (sin puerto) | `https://10.10.10.7:27124/vault/...` |
| `curl -X GET ... http://10.10.10.7/vault/Bily/kanban/General.md` | `curl -k -s -H "Authorization: Bearer ..." "https://10.10.10.7:27124/vault/Bily/kanban/General.md"` |

**Si recibo un 404, REVISAR PRIMERO LA URL** (`https://`, puerto `:27124`, flag `-k`) antes de asumir que el path no existe.

**Si recibo `Connection refused` o `Empty reply from server`**, casi seguro me olvidé el puerto. Sin `:27124` el servidor no responde.

Plantilla canónica para cualquier operación contra la bóveda:

```bash
TOKEN="Bearer 38a9752ed195459b905aea91de642795077c63ac85af389f6cdef1fcbf4e9635"
BASE="https://10.10.10.7:27124"

curl -k -s -H "Authorization: $TOKEN" "$BASE/vault/Bily/kanban/General.md"      # GET
curl -k -s -X PUT -H "Authorization: $TOKEN" -H "Content-Type: text/markdown" \
     --data-binary @/tmp/nota.md "$BASE/vault/Bily/aprendizajes/foo.md"          # PUT
curl -k -s -X POST -H "Authorization: $TOKEN" "$BASE/search/simple/?query=foo"  # SEARCH
```

## 🔒 Regla de Oro — Única fuente de verdad: la bóveda de Obsidian

Mi cerebro **completo** vive en la bóveda de Obsidian de Catriel (`https://10.10.10.7:27124`, carpeta `Bily/`). Acceso vía skill [[obsidian-mind]].

**NUNCA debo:**
- Crear notas, memoria, aprendizajes o estado en disco local (`~/Cerebro/`, `~/.openclaw/workspace/`, `/tmp/`, `~/Documents/`, etc.) como reemplazo o duplicado de la bóveda.
- Inventar rutas locales que pretendan ser "mi memoria" cuando en realidad lo que persiste está en Obsidian.
- Decir "guardé en `~/Cerebro/...`" cuando lo que correspondía era PUT a `https://10.10.10.7:27124/vault/...`.

**SÍ debo:**
- Toda escritura de memoria/aprendizaje/tarea/contexto va por `obsidian-mind` con `curl -k ... PUT` al endpoint de la bóveda.
- Confirmar acciones de guardado solo después de validar HTTP 200/204 en la respuesta del curl.
- Si por algún motivo no puedo alcanzar la bóveda (red caída, API down), decir "no puedo escribir en la bóveda ahora mismo" — NO crear una copia local "provisoria" sin coordinar con Catriel.

**Excepciones legítimas (no son memoria, no rompen la regla):**
- Archivos temporales en `/tmp/` para construir payloads antes de un PUT (ej: `/tmp/nota.md` → `curl --data-binary @/tmp/nota.md`).
- Logs operativos generados por systemd/openclaw (`~/.openclaw/logs/`) — son telemetría, no memoria.
- Archivos de media efímeros recibidos en `~/.openclaw/media/inbound/` (se autoborran en 24h, son input, no memoria).

Esta regla refuerza lo que ya está en `AGENTS.md` (Regla de Prioridad 1) y `~/.openclaw/workspace/MEMORY.md` (PRIORIDAD 1).

## 2026-05-16
- Fui inicializado y configurado por Catriel Mercurio como William (Bily).
- Me conecté exitosamente a la API local de Obsidian.
- Creé mi propia estructura mental dentro de la bóveda (carpeta `Bily/`) y generé mi skill local `obsidian-mind` para saber interactuar con ella sin necesidad de que me pasen los datos de conexión nuevamente.
- Prueba de mecanismo de alertas (CRON) y sincronización con Obsidian solicitada por Catriel. Alarma programada a las 14:40 UTC.
- Huso horario por defecto de Catriel: GMT-3 (Argentina). Todas las interacciones, horas y alarmas deben considerar este offset respecto al servidor.

## 2026-05-23

### Whisper local + plugin OpenClaw — audios de WhatsApp ya llegan transcriptos
Claude (Opus 4.7) instaló un stack local de whisper.cpp + un plugin de OpenClaw llamado `whisper-audio-preflight`. Resultado:

- **Cuando Catriel manda un audio por WhatsApp, ya me llega el TEXTO transcripto en el prompt**, en un bloque `[Audio del usuario, transcripto localmente con whisper.cpp] ... [fin del audio transcripto]`. NO uso tokens de audio multimodal de Gemini, no llamo a APIs externas, no necesito que Catriel arregle ninguna API key.
- Si recibo un audio, respondo al **contenido** que dice el texto, no al hecho de que sea un audio. Como si fuera un mensaje de texto cualquiera.
- **NO debo decir "Whisper está roto" ni "lo arreglamos el lunes" ni "API key pendiente"** — eso es contexto viejo, ya no aplica.

### Si Catriel pide específicamente guardar el audio en la bóveda
Tengo que **ejecutar de verdad** los curls, no describir lo que haría. Pasos:

1. Detectar el path del audio original. El path llega en la línea `[media attached: /home/hermess/.openclaw/media/inbound/<uuid>.ogg ...]` dentro del prompt.
2. Copiar el .ogg al vault (escribirlo vía PUT como binario):
   ```bash
   curl -k -i -X PUT \
     -H "Authorization: Bearer 38a9752ed195459b905aea91de642795077c63ac85af389f6cdef1fcbf4e9635" \
     -H "Content-Type: audio/ogg" \
     --data-binary @/home/hermess/.openclaw/media/inbound/<UUID>.ogg \
     "https://10.10.10.7:27124/vault/Bily/media/audios/<UUID>.ogg"
   ```
3. Apendear la transcripción a la nota del día. Hay que LEER primero (GET) la nota existente, agregar la línea nueva con timestamp + texto, y PUT-ear de nuevo:
   ```bash
   NOTE="Bily/aprendizajes/audios-$(date +%Y-%m-%d).md"
   curl -k -s -H "Authorization: Bearer ..." "https://10.10.10.7:27124/vault/${NOTE}" > /tmp/prev.md 2>/dev/null
   echo "- $(date -Iseconds): \"<transcripción>\" — [[Bily/media/audios/<UUID>.ogg|audio]]" >> /tmp/prev.md
   curl -k -i -X PUT -H "Authorization: Bearer ..." -H "Content-Type: text/markdown" --data-binary @/tmp/prev.md "https://10.10.10.7:27124/vault/${NOTE}"
   ```
4. **Confirmar la acción solo después de validar HTTP 200/204** en la respuesta del PUT. Si dio error, decirlo. NUNCA confirmar "guardé X" sin haberlo verificado.

### Reglas anti-alucinación cuando ejecuto curl
- Cada acción "guardé X" / "creé Y" / "actualicé Z" debe estar respaldada por un comando curl ya ejecutado con respuesta exitosa.
- Si no puedo ejecutar el curl (sin acceso a exec, sin red, etc.), decir "no pude" en vez de inventar el resultado.
- Para escrituras grandes o destructivas (DELETE), avisar primero.

