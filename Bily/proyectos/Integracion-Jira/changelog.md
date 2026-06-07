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

## 2026-06-07 (segunda parte) — F2.5 deployed

### 22:40 · Re-diseño preflight + tools de alto nivel + MCP

**Motivación:** Catriel señaló que mi propuesta original de extender el preflight con regex para "qué hizo Marbe esta semana" estaba en la capa equivocada. El LLM ya hace intent recognition — la respuesta correcta es exponerle APIs/tools bien shaped, no hardcodear interpretación con string matching. Lección guardada como principio operativo (ver memoria operativa interna de Claude: `feedback-intent-over-regex`).

### Parte A — Tools de alto nivel (intent-friendly)

Agregado a `Jira` class:
- `resolve_user(query)` — name/email/'me'/accountId → `{accountId, displayName, email}`. Maneja ambigüedad (multi-match en "catriel" preferentemente al currentUser).
- `_parse_since(natural)` — "esta semana", "ayer", "hoy", "este mes", "ultimos 15 dias", "7d", "2w" → días enteros.
- `by_user(name, since, project, include_reported)` — tickets de un usuario en ventana.
- `activity(since, project, user)` — cualquier ticket tocado en ventana, filtrable.

Endpoints sidecar nuevos: `GET /resolve-user`, `GET /by-user`, `GET /activity`.

Wrappers `~/bin/` nuevos:
- `jira-by-user <name|me> [--since "<rango>"] [--project <PROJ>] [--reported]`
- `jira-activity [--since "<rango>"] [--project <PROJ>] [--user <name>]`

**Tests validados:**
- `jira-by-user marbe --since "esta semana"` → 35 tickets reales (NBWEB, LIO, MKT, ADATA).
- `jira-by-user catriel` → 5 matches resueltos preferentemente al currentUser.
- `jira-by-user guille --since "ultimos 3 dias"` → JQL `updated >= -3d` correctamente generada.
- `jira-activity --project SNB --since ayer` → 1 ticket.

### Parte B — MCP server

`~/jira/mcp_server.py` (~250 líneas Python stdlib, JSON-RPC 2.0 sobre stdin/stdout). Habla al sidecar HTTP. 10 tools registradas con JSON Schema completo:

| Tool | Descripción para LLM |
|---|---|
| `jira_issue` | Obtiene un ticket por KEY |
| `jira_search` | JQL crudo |
| `jira_my` | Tickets del currentUser |
| `jira_by_user` | "¿qué hizo X esta semana?", "¿en qué anda Y?" |
| `jira_activity` | "¿qué hay nuevo en proyecto X?", "¿qué se movió hoy?" |
| `jira_transitions` | Lista transiciones disponibles de un ticket |
| `jira_create` | Crear ticket (reversible) |
| `jira_comment` | Comentar (bajo riesgo) |
| `jira_assign` | Reasignar (reversible) |
| `jira_transition` | DESTRUCTIVO: cambiar estado (siempre confirmar antes) |

**Smoke test:** initialize + tools/list (10) + tools/call jira_by_user marbe → 35 tickets devueltos con JQL exacta.

**Registrado en Claude Code:** `claude mcp add jira python3 -- /home/hermess/jira/mcp_server.py` (corrido por Catriel manualmente — auto-mode classifier correctamente bloquea self-modification del config de Claude Code).

### Parte C — Preflight slim

Cambio en el plugin OpenClaw `jira-context-preflight`:
- Eliminado el regex genérico `\bjira\b` (era demasiado amplio).
- Mantenidos solo 2 shortcuts alta frecuencia: `qué tengo hoy/pendiente/ahora/hacer` y `mis tickets/tareas/issues`.
- Header del bloque inyectado completamente reescrito. Ahora declara explícitamente "este bloque solo cubre menciones de keys + 'qué tengo hoy'; para TODO lo demás usá los wrappers/MCP", y enumera TODAS las tools (read + writes + las nuevas de alto nivel) con ejemplos de intent → tool.

Resultado: cuando Catriel manda "qué hizo marbe esta semana" por WhatsApp, el regex NO matchea (correcto), pero el header inyectado ya está en el contexto del agente — Bily ve "tenés `jira-by-user` disponible" y lo ejecuta vía Bash con args correctos. **El LLM hace el routing semántico, no el regex.**

### Archivos propagados al skill portable

`~/.claude/skills/jira/files/`:
- `jira.py` (actualizado con resolve_user, by_user, activity, _parse_since)
- `mcp_server.py` (nuevo)
- `bin/jira-by-user`, `bin/jira-activity` (nuevos)

## Pendiente

- **F5** (pospuesto por decisión 2026-06-07): webhook receiver `:9003` + notificaciones proactivas WhatsApp. Requiere resolver exposición externa (Cloudflared / Tailscale Funnel). Decisión: hacer cuando esté esa pieza.

## Ver también

- [[Inicio|Diseño completo]]
- [[estado|Estado vivo (qué corre ahora)]]
- [[Bily/jira/Inicio|Notas de tickets autopopuladas]]
