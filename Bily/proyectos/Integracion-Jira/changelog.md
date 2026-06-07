---
tags: [jira, integracion, changelog]
---

# Changelog · Integración Jira

Cronología de implementación. Ver [[Inicio|diseño]] para arquitectura y [[estado|estado vivo]] para componentes corriendo ahora.

## 2026-06-07 — F1+F2+F3+F4 deployed (sesión completa)

### 21:00 · Token Atlassian generado y validado
- Token guardado en `~/.config/jira/credentials` chmod 600.
- Validación contra `/rest/api/3/myself`: HTTP 200 como Catriel Mercurio, 31 proyectos visibles (ADATA, SNB, MKT, ASUS, COM, COB, BLUWEB, BROT, BULLY, ACER, ...).

### 21:21 · F1 deployed — read básico
- `~/jira/jira.py` (~270 líneas Python stdlib, sin venv).
- Sidecar systemd `jira-sidecar.service` en `127.0.0.1:9002` (10 MB RAM idle).
- 3 wrappers: `jira-issue`, `jira-search`, `jira-my` en `~/bin/`.
- Métricas: cache miss `jira-my` 768ms, cache hit **31ms** (25× speedup).

### 21:25 · F2 deployed — plugin OpenClaw preflight (v1)
- `~/openclaw-plugins/jira-context-preflight/` instalado en gateway.
- 11 plugins activos. Hook `message_received` detecta keys (regex tolerante `EXP-553`, `EXP553`, `EXP 553`) + triggers ("qué tengo", "mis tickets", "mi sprint").
- Hook `before_prompt_build` inyecta contexto al prompt antes del LLM.

### 21:34 · Bug fix preflight — provenance en injection
- Síntoma reportado por Catriel: mensaje 1 funciona perfecto, followup ("eso está todo a mi nombre?") alucina ("es una mezcla del equipo").
- Causa: bloque inyectado no incluía la JQL exacta. Turnos futuros sin re-trigger leían el bloque y especulaban.
- Fix: header del bloque ahora explícito (capabilities + reglas operativas) + listado `/my` declara JQL `assignee = currentUser() AND statusCategory != Done`.
- Lección capturada en memoria operativa de Claude: `feedback_preflight_provenance` ([[feedback-preflight-provenance]]).

### 21:47 · F3 deployed — writes
- Métodos `create()`, `comment()`, `assign()`, `transition()` en clase `Jira`.
- ADF (Atlassian Document Format) para descripciones y comentarios.
- 4 wrappers: `jira-create`, `jira-comment`, `jira-assign`, `jira-transition`.
- **Guardrail destructivos:** `jira-transition` sin `--yes` muestra preview (status actual + 7 transiciones disponibles) y sale con `exit 2`. Bily aprende vía header del plugin: pedir confirmación → re-ejecutar con `--yes`.
- Sidecar invalida `ISSUE_CACHE[key]` + `SEARCH_CACHE` después de cada write.
- Smoke test live validado por Catriel: create + comment + transition con confirmación funcionan end-to-end por WhatsApp.

### 22:03 · F4 deployed — vault sync + skill portable
- **Parte A — vault sync:**
  - `_adf_to_markdown()` converter recursivo (doc, paragraph, heading, text, marks, listas, codeBlock, blockquote, mention, emoji).
  - `Jira.issue_full(key, comment_limit=20)` fetch con descripción + comentarios.
  - Background worker `_sync_worker()` con `queue.Queue(maxsize=200)`, debounce 30s por key.
  - Cada `/issue/<KEY>` cache-miss + cada write enqueuea sync. `/search` y `/my` NO (mucho volumen).
  - PUT a `https://10.10.10.7:27124/vault/Bily/jira/<KEY>.md` (vía urllib + ssl.CERT_NONE).
  - Verificado: `SNB-3946.md` y `COB-1.md` con 7 comentarios renderizados + frontmatter completo + tags `[jira, SNB, esperando-por-ayuda]`.
- **Parte B — skill portable:**
  - `~/.claude/skills/jira/SKILL.md` con triggers (`/jira`, "ver ticket", "instalar jira").
  - `setup-jira.sh` interactivo (213 líneas): pide URL+email+token, valida `/myself` ANTES de escribir, copia `jira.py` + 7 wrappers, smoke test con `jira-my`, opcional systemd unit.
  - `files/` contiene copias de `jira.py` + los 7 wrappers ejecutables.
  - Skill detectada en hot por Claude Code (sin reinicio).

## Pendiente

- **F5** (pospuesto por decisión 2026-06-07): webhook receiver `:9003` + notificaciones proactivas WhatsApp. Requiere resolver exposición externa (Cloudflared / Tailscale Funnel). Decisión: hacer cuando esté esa pieza.

## Ver también

- [[Inicio|Diseño completo]]
- [[estado|Estado vivo (qué corre ahora)]]
- [[Bily/jira/Inicio|Notas de tickets autopopuladas]]
