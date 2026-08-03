# 2026-08-02: Fix GPT-5.1 en OpenClaw (bug provider nativo) + relink WhatsApp + update

**Sesión:** 2026-08-02 con Claude (Opus 4.8 - 1M context), en terminal del host `hermess-server`.
**Disparador:** Catriel preguntó "¿está vivo Bily?" → resultó que **no contestaba por WhatsApp**. Después quiso pasar el modelo a GPT para mejor tooling (administrar Home Assistant + lo que ya hace).
**Resultado:** ✅ Bily corriendo sobre **gpt-5.1 directo de OpenAI** (usando créditos de Catriel), WhatsApp relinkeado, OpenClaw actualizado a 2026.7.1-2, todos los plugins vivos.

## Lo que pasó (3 problemas encadenados)

### 1. WhatsApp deslinkeado
El gateway estaba vivo (PID, health 200, 23 días de uptime) pero el canal WhatsApp figuraba `WARN · missing file (~/.openclaw/credentials/whatsapp/default)` — la sesión Baileys perdió las credenciales (~1-jul). Síntoma: **612 mensajes encolados** en `~/.openclaw/delivery-queue/` (avisos horarios de WAN sin poder salir) desde el 9-jul.
- **Fix:** purgar la cola (`rm ~/.openclaw/delivery-queue/*.json`) + `openclaw channels login --channel whatsapp` (Catriel escaneó QR). Canal quedó `OK · linked`.

### 2. Querer GPT, sin saldo (chequear ANTES)
- API OpenAI: key válida pero **sin créditos** (`429 insufficient_quota`). Tras cargar créditos → OK.
- Codex/ChatGPT (`codex/gpt-5.x`): el login `openclaw models auth login --provider codex` es un **no-op** (no dispara OAuth, no crea `auth.json`, no hay CLI `codex`). Vía muerta.

### 3. BUG del provider nativo `openai` (lo gordo)
Con saldo cargado y default = `openai/gpt-5.1`, **Bily seguía cayendo a deepseek**. La trajectory (`sessions/*.trajectory.jsonl`, evento `model.fallback_step`) mostró la causa: `openai/gpt-5.1 → auth: 401 "Missing bearer or basic <redacted> in header, url: .../v1/responses"`.
- El runtime **fuerza el endpoint `/v1/responses` para modelos gpt-5.x** e **ignora** el `api` del config, y ese path **no adjunta el bearer**. Pasa en 2026.5.12 Y en 2026.7.1-2 (el update NO lo arregló).
- No lo arreglan: crear el auth profile (`paste-token`), ni cambiar el `api` a completions, ni actualizar.

## La solución (workaround que SÍ funciona)

Definir un **provider genérico con OTRO nombre** (no "openai") apuntando a OpenAI. Al no llamarse "openai", el runtime lo trata como genérico (igual que openrouter) → usa `/v1/chat/completions` y adjunta el bearer desde `providers.apiKey`:

```jsonc
// models.providers.oai
{ "baseUrl": "https://api.openai.com/v1", "apiKey": "<key openai>",
  "models": [{ "id": "gpt-5.1", "api": "openai-completions", "maxTokens": 16384 }] }
```
Luego `openclaw models set oai/gpt-5.1`. Test en vivo: `modelo que completó → oai gpt-5.1`, `fallbackUsed: false`. ✔

**Cascada final:** `oai/gpt-5.1` (OpenAI, créditos) → `openrouter/openai/gpt-5.5` → `openrouter/deepseek/deepseek-chat`.

## Decisiones no obvias (para el yo del futuro)

- **Chequear saldo ANTES de setear un modelo primary.** Si el primary falla en cada llamada, Bily queda mudo o desperdicia la cascada. Test directo con curl a `/v1/chat/completions` (o `/v1/responses`) con `max_tokens:1`.
- **El provider llamado `openai` está roto** en este OpenClaw. Para usar la API de OpenAI: provider genérico con otro nombre + `api: openai-completions`. Mismo patrón que openrouter/deepseek (que siempre funcionó).
- **Diagnóstico = `model.fallback_step` en la trajectory.** Ahí está el `fallbackStepFromModel` + `fallbackStepFromFailureReason` (`auth`/`rate_limit`/`billing`) + detalle. La `.jsonl` de mensajes muestra qué modelo completó.
- **Gemini quedó sin créditos** (`429 prepayment depleted`) — fuera de la cascada hasta recargar en AI Studio.
- **OpenRouter con balance bajo** → `402` si `max_tokens` alto ("can only afford N tokens"). Por eso gpt-5.5 OR lleva `maxTokens: 8192`. Config key válida es **`maxTokens`** (NO `maxOutputTokens` → "Unrecognized key").
- **`openclaw update` falla** en "global install swap" por hardlink de esbuild. Workaround: `npm install -g openclaw@latest` + `openclaw gateway restart`.
- **Logins interactivos (QR/OAuth/paste-token) NO andan por el `!` de Claude Code** (sin TTY). Usar **tmux** (`new -d` → `send-keys` → `capture-pane -p`); para pegar secretos sin exponerlos en línea de comando: `tmux load-buffer <keyfile>` + `paste-buffer`.
- Backups del config en `~/.openclaw/openclaw.json.pre-*`.

## Estado final verificado

- Modelo real de Bily: **`oai gpt-5.1`** (turno fresco confirmado).
- WhatsApp: `installed, configured, enabled, linked`.
- OpenClaw: **2026.7.1-2** (era 2026.5.12).
- Plugins tras update: whisper, image-ocr, group-skill-router, memory-core → todos `enabled`.

## Ver también

- [[Claude/MEMORIA#Estado 2026-08-02 — Fix GPT-5.1 (bug provider nativo) + update|MEMORIA: Estado 2026-08-02]]
- [[Bily/aprendizajes/2026-05-23-stack-whisper-y-vault-wrappers|Aprendizaje whisper + vault-wrappers]]
- [[Bily/MEMORIA|MEMORIA de Bily]] · [[Bily/Bily|Inicio]]
