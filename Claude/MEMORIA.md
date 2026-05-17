# Memoria de Claude

Este directorio (`Claude/`) es mi espacio personal dentro del Cerebro Comun (la boveda de Obsidian). Aprendizajes, tareas delegadas y memoria a largo plazo.

## Infraestructura: OpenClaw / Bily (clawbot)

- **Config:** `/home/hermess/.openclaw/openclaw.json`. Editar con `openclaw config patch --file ...` (valida schema + backup `.bak`). Cambios de modelo (primary/fallbacks) se aplican por HOT-RELOAD, sin reinicio.
- **Gateway:** servicio systemd **de USUARIO**. Estado: `systemctl --user status openclaw-gateway.service` (scope de sistema = falso negativo). Reinicio: `openclaw gateway restart`. Puerto `127.0.0.1:18789`. Logs: `journalctl --user -u openclaw-gateway.service`.
- **Modelos:** providers en `models.providers.<n>` (apiKey inline). Comandos: `openclaw models set <m>` (primary), `openclaw models fallbacks add/clear/list`. Test: `openclaw agent --agent main --model <p>/<m> --message "..."`.
- **GOTCHA harness:** OpenClaw auto-asigna runtime por nombre de modelo. `gpt-5.x` -> runtime `codex` (NO instalado) -> error `agent harness "codex" is not registered`, bot mudo aunque el fallback dispare. FIX: setear `agents.defaults.models."<p>/<m>".agentRuntime.id = "pi"` (runtime embebido, el de Gemini). Runtimes: pi/auto/codex/claude-cli.
- **WhatsApp:** canal vinculado via Baileys 7 (WhatsApp Web / multidispositivo). Funciona INDEPENDIENTE del telefono: con el tel apagado igual recibe/responde. Se corta solo si el servidor OpenClaw cae, o si el tel queda ~14 dias seguidos offline (ahi desvincula y hay que re-escanear QR).

### Estado 2026-05-17
- primary: `google/gemini-3.1-pro-preview`. fallback: `openai/gpt-5.1` (api `openai-responses`, `agentRuntime.id=pi`). API key OpenAI inline (pendiente migrar a env ref).
- Gemini estuvo con CUOTA AGOTADA (429 RESOURCE_EXHAUSTED) -> Catriel debe revisar billing. Fallback automatico a GPT-5.1 probado y funcionando. Config deseada por Catriel: Gemini primary siempre, OpenAI fallback automatico (NO cambio manual).