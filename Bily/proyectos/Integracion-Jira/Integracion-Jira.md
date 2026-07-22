---
tags: [proyecto, integracion, jira, bily]
estado: deployed
creado: 2026-05-26
deployed: 2026-06-07
owner: Catriel
---
como
# Integración Jira para Bily (y agentes futuros)

> **Estado:** F1–F6 **DEPLOYED** 2026-06-07. Bily consume Jira por **MCP nativo** (preflight regex retirado, intent-over-regex). F5 (webhooks) pospuesto. Ver [[estado|estado vivo]] para componentes corriendo y [[changelog|changelog]] para cronología.

> Diseño técnico completo. Objetivo: que **Bily responda sobre tickets/sprints por WhatsApp** y que la capa quede **portable** para reutilizarla desde Claude Code u otros agentes (no acoplada a OpenClaw).

## 1. Objetivos

1. **Bily lee Jira** — Catriel pregunta por WhatsApp ("¿qué tengo hoy?", "estado de EXP-553") y Bily responde con datos vivos.
2. **Bily escribe en Jira** — dictado por WhatsApp: crear ticket, transicionar, comentar, asignar.
3. **Bily avisa proactivamente** — webhooks de Jira → mensaje WhatsApp ("te asignaron COM-300", "se cerró el sprint EXP-S42").
4. **Portable** — la capa de acceso a Jira es invocable desde Claude Code, otros agentes, scripts cron — sin requerir OpenClaw.

## 2. Workspace objetivo

- **URL:** `https://bluinc.atlassian.net`
- **Proyectos activos detectados** (de la bóveda): EXP (Expedición), COM, ASUS, y otros.
- **Auth:** API Token de Atlassian (email + token Basic Auth). Generar en `id.atlassian.com/manage-profile/security/api-tokens`.

## 3. Arquitectura (4 capas + 1 transversal)

```
                           ┌──────────────────────────────┐
   L3 ─ Consumidores       │ OpenClaw   Claude Code  cron │
                           │ plugin     skill        jobs │
                           └────┬─────────────┬────────┬──┘
                                ↓             ↓        ↓
   L2 ─ CLI wrappers       ┌─────────────────────────────┐
        (~/bin/jira-*)     │ jira-issue  jira-search ... │
                           └────────────┬────────────────┘
                                        ↓
   L1 ─ Sidecar local      ┌─────────────────────────────┐
        :9002 (opcional)   │ cache · rate-limit · vault  │
                           │ sync · token mgmt           │
                           └────────────┬────────────────┘
                                        ↓
   L0 ─ Cliente Jira       ┌─────────────────────────────┐
        (jiralib)          │ auth · paginación · JQL     │
                           └────────────┬────────────────┘
                                        ↓
                              Jira Cloud REST v3
                                        │
                                        │  (webhooks salientes)
                                        ↓
   T  ─ Webhook receiver   ┌─────────────────────────────┐
        :9003              │ HMAC · debouncing · ruteo   │
                           └────────────┬────────────────┘
                                        ↓
                              OpenClaw API → WhatsApp
```

**Decisión clave:** los wrappers L2 hablan **preferentemente** con el sidecar L1, pero si `JIRA_SIDECAR_URL` no está seteada caen directo a L0 → Jira REST. Esto hace al skill portable a máquinas sin sidecar (solo necesita el wrapper + creds).

## 4. Componentes en detalle

### L0 · `jiralib` (cliente Python, portable)

- **Ubicación propuesta:** `~/lib/jiralib/` (módulo Python instalable con `pip install -e`).
- **Responsabilidad:** auth, paginación, helpers JQL, retry/backoff sobre 429.
- **Dependencias:** solo `httpx` (sin SDK de Atlassian — son pesados y obsoletos).
- **API mínima:**
  ```python
  from jiralib import Jira
  j = Jira()  # lee env JIRA_BASE_URL, JIRA_EMAIL, JIRA_TOKEN
  j.issue("EXP-553")
  j.search("assignee = currentUser() AND statusCategory != Done")
  j.create(project="COM", summary="...", description="...", issuetype="Task")
  j.transition("EXP-553", to="Done")
  j.comment("EXP-553", "Listo")
  j.sprints(board_id=42, state="active")
  ```
- **Por qué Python y no Node:** ya hay precedente con whisper (ver [[Claude/Whisper|Whisper local]]), Catriel cómodo, mejor para scripting cron. Plugin OpenClaw queda en Node igual (habla con sidecar por HTTP).

### L1 · `jira-sidecar` :9002 (servicio local, opcional)

- **Ubicación:** `~/jira/sidecar.py` + systemd `--user` unit (espejo de whisper).
- **Por qué existe:**
  - **Cache** por TTL (default 60s para issues, 300s para searches) — Bily pregunta lo mismo 3 veces seguidas y no quemamos rate limit.
  - **Rate limit interno** — Jira Cloud: 10 req/s por usuario. Sidecar limita a 8/s con burst 20.
  - **Token mgmt** — un solo lugar lee creds del disco, los wrappers no las ven.
  - **Vault sync** — cada issue consultado se persiste como `Bily/jira/<KEY>.md` (configurable). Habilita lectura offline desde cualquier agente que tenga acceso a la bóveda.
- **Endpoints:**
  ```
  GET  /issue/<key>                 → issue completo (cacheado)
  GET  /search?jql=<jql>&fields=... → array de issues
  POST /issue                       → crea (body JSON)
  POST /transition/<key>            → transiciona ({to: "Done"})
  POST /comment/<key>               → comenta ({body: "..."})
  GET  /my?status=open              → mis tickets
  GET  /sprint/active?board=<id>    → sprint activo
  GET  /health
  ```
- **Bind:** `127.0.0.1:9002` (no expuesto a LAN — espejo de la decisión de whisper).

### L2 · Wrappers `jira-*` en `~/bin/` (espejo de `vault-*`)

- **Por qué existen:** mismo motivo que `vault-*` — Bily cuando cae a deepseek alucina URLs/headers. Los wrappers eliminan el vector. Ver [[Claude/Vault-Wrappers|Vault Wrappers]] y [[Claude/Whisper|Whisper local]] punto 7.
- **Comandos:**
  | Cmd | Qué hace |
  |---|---|
  | `jira-issue <KEY>` | JSON del ticket (campos clave por defecto, `--full` para todo) |
  | `jira-search "<JQL>"` | Array JSON de issues |
  | `jira-my [--status open\|all]` | Mis tickets activos |
  | `jira-sprint [--board <id>]` | Sprint activo + issues |
  | `jira-create <PROJ> "<summary>" [--desc ...] [--type Task]` | Crea ticket, devuelve KEY |
  | `jira-transition <KEY> "<estado>"` | Mueve ticket (resuelve `transitionId` automágicamente) |
  | `jira-comment <KEY> "<texto>"` | Agrega comentario |
  | `jira-assign <KEY> <email\|me>` | Reasigna |
- **Comportamiento:** stdout = JSON o texto plano según flag; stderr = errores; exit 0 si OK.
- **Detección de sidecar:** si `JIRA_SIDECAR_URL` está seteada → HTTP al sidecar. Else → Python script directo usando `jiralib`. **Esto es lo que hace al skill portable.**

### L3a · Plugin OpenClaw `jira-context-preflight`

- **Patrón:** copia exacta del `whisper-audio-preflight` + `image-ocr-preflight`. Ver [[Claude/Image-OCR|Image OCR preflight]] y [[Claude/Whisper|Whisper local]].
- **Hook `message_received`:**
  1. Parsear mensaje WhatsApp con regex:
     - Ticket keys: `\b([A-Z]{2,10})-(\d+)\b` → fetch issues.
     - Triggers JQL: "qué tengo hoy", "mis tickets", "mi sprint", "qué hay nuevo en <proj>" → fetch search apropiada.
  2. Fire-and-forget `fetch('http://127.0.0.1:9002/...')`, cachear promise por `sessionKey` (TTL 5min, igual que whisper).
- **Hook `before_prompt_build`:**
  1. Await las promises pendientes.
  2. `prependContext` con bloque enriquecido:
     ```
     [Contexto Jira inyectado preflight]
     EXP-553 "Validar carga masiva" · status=In Review · assignee=Guille · sprint=EXP-S42
     Última actividad: hace 2h — Guille comentó "Esperando QA"
     URL: https://bluinc.atlassian.net/browse/EXP-553
     [fin contexto Jira]
     ```
  3. El LLM responde con datos frescos sin gastar tool calls.
- **Por qué hook y no skill/tool:** mismo motivo que OCR — Bily (con fallback a deepseek) **no elige** llamar herramientas confiables. El hook elimina la decisión del modelo. Ver [[Claude/Image-OCR|Image OCR preflight]] "Why hook y no skill".
- **Writes (crear/transicionar/comentar):** **NO** se ejecutan automáticamente desde el hook. El hook solo enriquece contexto. Para writes, el LLM emite una llamada al wrapper `jira-create` etc. via Bash tool — y un hook `before_tool_use` puede pedir confirmación a Catriel por WhatsApp ("¿Confirmás crear COM-301 'X' asignado a vos? sí/no").

### L3b · Skill de Claude Code (portable)

- **Ubicación:** `~/.claude/skills/jira/` con `SKILL.md` describiendo triggers ("/jira", "estado de", "ticket X").
- **Implementación:** invoca los wrappers `jira-*`. Si la máquina no tiene wrappers instalados, el skill incluye un script `setup-jira.sh` que:
  1. Pide email + token interactivo.
  2. Los guarda en `~/.config/jira/credentials` (chmod 600).
  3. Instala `jiralib` (`pip install`) y los wrappers (`cp ~/bin/jira-* ...`).
- **Esto cumple el requisito de portabilidad** que pediste: el skill se mueve entre máquinas y se autoconfigura.

### L3c · MCP de Atlassian (futuro / opcional)

- Atlassian publica un MCP oficial (ya cargado en mi entorno como `mcp__claude_ai_Atlassian__*`).
- **Cuándo usarlo:** queries ad-hoc complejas desde Claude Code donde no querés mantener un wrapper.
- **Cuándo NO:** flujo de WhatsApp/Bily (latencia + costo de tool call por consulta es prohibitivo a escala).

### T · Webhook receiver `:9003` (notificaciones proactivas)

- **Servicio:** micro-server Python (FastAPI) en `~/jira/webhook.py`, systemd `--user`.
- **Endpoint:** `POST /jira/event/<secret>` (el `<secret>` actúa como shared key — Jira Cloud no firma HMAC por defecto).
- **Eventos suscriptos** (configurados en Jira Settings → System → Webhooks):
  - `jira:issue_updated` (filtrado a status changes y assignee changes)
  - `jira:issue_created` (filtrado a assignee=Catriel o mention=Catriel)
  - `comment_created` (filtrado a mentions o issues donde Catriel es assignee/reporter)
  - `sprint_started` / `sprint_closed`
- **Debouncing:** ventana de 30s — si el mismo issue cambia 5 veces seguidas, una sola notificación.
- **Ruteo:** POST a OpenClaw API → mensaje WhatsApp a Catriel con resumen + URL.
- **Exposición externa:** depende del setup (ver decisiones abiertas).

## 5. Modelo de datos en la bóveda

Cada ticket consultado se persiste como `Bily/jira/<KEY>.md`:

```markdown
---
jira_key: EXP-553
status: In Review
assignee: Guille
sprint: EXP-S42
updated: 2026-05-26T14:22:00Z
project: EXP
url: https://bluinc.atlassian.net/browse/EXP-553
tags: [jira, EXP, in-review]
---

# EXP-553 · Validar carga masiva

**Descripción:** ...

## Comentarios
- @Guille (2h): Esperando QA
- @Catriel (1d): Probado, ok

## Sincronizado
- Última sync: 2026-05-26 14:22 ART
- TTL cache sidecar: 60s
```

**Beneficios:**
- Otros agentes (incluido Claude Code en cualquier proyecto) leen Jira **sin tener acceso al token**.
- Búsqueda full-text vía `vault-search "EXP-553"`.
- Linkable con `[[EXP-553]]` desde cualquier nota.

**Costo:** suma notas al grafo Obsidian. Mitigación: carpeta `Bily/jira/` excluida del graph view por default.

## 6. Seguridad

| Tema | Decisión |
|---|---|
| API token | `~/.config/jira/credentials` chmod 600. **Nunca** en repo ni en CLAUDE.md. |
| Bind sidecar | `127.0.0.1` only, no LAN. |
| Webhook auth | Shared secret en path + IP allowlist (rango Atlassian Cloud). |
| Writes destructivos | Hook `before_tool_use` pide confirmación WhatsApp antes de transitions/deletes. |
| Audit log | Sidecar loguea toda operación con timestamp + user-agent del wrapper invocador en `~/jira/logs/audit.log`. |
| Rotación token | Recordatorio cron cada 6 meses (Atlassian no fuerza, pero buena práctica). |

## 7. Roadmap (fases entregables)

| F | Entregable | Estado |
|---|---|---|
| **F1** | `jiralib` + sidecar + wrappers read-only (`jira-issue`, `jira-search`, `jira-my`). | ✅ **DONE 2026-06-07 21:21** |
| **F2** | Plugin OpenClaw `jira-context-preflight` (regex tolerante + triggers). | ✅ DONE 2026-06-07 21:25 → ⚠️ **OBSOLETO: retirado en F6** |
| **F2.5** | Tools de alto nivel (`jira-by-user`, `jira-activity`) + MCP server + preflight slim. | ✅ **DONE 2026-06-07 22:40** |
| **F3** | Wrappers write + dry-run con `--yes` en destructivos. | ✅ **DONE 2026-06-07 21:47**, smoke-tested live por Catriel |
| **F4** | Vault sync de tickets como notas Markdown + skill portable. | ✅ **DONE 2026-06-07 22:03** |
| **F5** | Webhook receiver + notificaciones proactivas WhatsApp. | ⏸️ Pospuesto (necesita Cloudflared/Tailscale) |
| **F6** | **MCP nativo en OpenClaw** (`openclaw mcp set jira`) → Bily usa tools siempre presentes. Preflight regex **RETIRADO**. Intent-over-regex verificado en vivo. + `sync_all.py` (708 tickets a la bóveda). | ✅ **DONE 2026-06-07 (noche)** |
| **F7** | Polish open-ended: índice + cron del bulk sync, cache invalidation inteligente, dashboards de uso. | open-ended |

Ver [[changelog|changelog]] para cronología detallada y [[estado|estado vivo]] para qué corre ahora.

## 8. Decisiones (cerradas 2026-06-07)

| # | Pregunta | Decisión | Razón |
|---|---|---|---|
| 1 | Lenguaje sidecar + jiralib | **Python** | Precedente whisper, ergonomía cron, httpx+FastAPI maduros. |
| 2 | Caché de issues | **Notas Markdown en `Bily/jira/`** (con exclusión del graph) | Habilita lectura desde otros agentes sin compartir token. Linkeable `[[EXP-553]]`. |
| 3 | Webhook receiver (F5) | **Posponer** hasta validar F1-F4 | Reduce scope inicial, decidimos exposición con más info real. |
| 4 | Confirmación en writes | **Solo destructivos: deletes + transitions** | Creates/comments/assigns van auto. Confirma lo difícil de revertir. |
| 5 | Workspace + email | `bluinc.atlassian.net` / `team@libreopcion.com` | Cuenta de Blu de Catriel. |
| 6 | Token storage | `~/.config/jira/credentials` chmod 600 | Nunca en repo ni CLAUDE.md. Sidecar es el único lector. |
| 7 | KEY parsing tolerante | **Sí**, regex acepta `EXP-553`, `EXP553`, `exp 553` | Catriel tipea por WhatsApp con typos. |

## 9. Riesgos

- **Rate limit Jira (10 req/s)** — mitigado por cache sidecar. Pero si Bily entra en bucle de búsquedas, puede tocar el techo. Sidecar tiene rate limit interno.
- **Token leak** — único punto sensible. Está en `~/.config/jira/credentials` chmod 600, fuera de CLAUDE.md y de cualquier repo.
- **OpenClaw bloquea fetch a localhost?** → Probar early. El plugin whisper usa `fetch('http://127.0.0.1:9001/...')` y funciona desde abril 2026, así que estamos OK.
- **Webhook spam** — mitigado por debouncing 30s + filtros pre-receiver.
- **Sincronización stale** — si Catriel edita en Jira UI, el cache de 60s puede mostrar versión vieja. Aceptable. Si molesta, baja TTL a 15s o agregar invalidación por webhook.

## 10. Referencias internas

- Patrón sidecar + plugin OpenClaw: [[Claude/Whisper|Whisper local]]
- Plugin preflight (hook que injecta contexto): [[Claude/Image-OCR|Image OCR preflight]]
- Wrappers `~/bin/`: [[Claude/Vault-Wrappers|Vault Wrappers]]
- Memoria operativa de Bily: [[Bily/MEMORIA|MEMORIA]]
- Workspace Blu (tabla `proyecto_jira_boards`): [[Blu/bluMiniErp/Base de Datos|Base de Datos]]
- Productos Bily: [[Bily/Productos/Productos|Productos]] · [[Bily/proyectos/proyectos|Proyectos]]

## 11. Ver también

- [[Bily/proyectos/Integracion-Jira/changelog|Changelog]] — cronología detallada de las fases F1–F6.
- [[Bily/proyectos/Integracion-Jira/estado|Estado vivo]] — componentes corriendo, paths, endpoints, performance medida.
- [[jira|Bily/jira/]] — notas de tickets autopobladas por el vault sync.
- [[Bily/proyectos/proyectos|Proyectos]] (volver al índice)
- [[Bily/Bily|Inicio Bily]]

---

**Próximo paso sugerido (opcional):** F7 polish — generar índice `Bily/jira/Inicio.md` para los 708 tickets del bulk sync y agendar `sync_all.py` en cron para mantenerlos frescos. Catriel no lo pidió aún.
