---
tags: [jira, integracion, estado]
estado: deployed
deploy_date: 2026-06-07
---

# Estado vivo de la integración Jira

Snapshot del 2026-06-07 22:03 — qué está corriendo en el server `hermess-server`. Ver [[changelog|changelog]] para historial de fases y [[Inicio|Inicio]] para diseño completo.

## Resumen ejecutivo

| Capa | Componente | Estado |
|---|---|---|
| Client | `~/jira/jira.py` (~32 KB, Python stdlib only) | active |
| Sidecar | `jira-sidecar.service` :9002 | active, 10 MB RAM |
| CLI | 7 wrappers `~/bin/jira-*` | ejecutables |
| OpenClaw | Plugin `jira-context-preflight` (11 plugins en gateway) | registrado |
| Vault | Notas Markdown en `[[Bily/jira/Inicio|Bily/jira/]]` | sync activo |
| Skill | `~/.claude/skills/jira/` con installer portable | registrada |
| Creds | `~/.config/jira/credentials` chmod 600 | configurado |

## Paths en disco

```
~/.config/jira/credentials           # chmod 600 — JIRA_BASE_URL + JIRA_EMAIL + JIRA_TOKEN
~/jira/
  jira.py                            # cliente + sidecar + CLI en un archivo
  logs/
    sidecar.log                      # stdout
    sidecar.err                      # stderr
~/bin/
  jira-issue                         # GET /issue/<KEY> (read)
  jira-search                        # POST /search/jql (read)
  jira-my                            # GET /my?status=open|all (read)
  jira-create                        # POST /issue/create (write seguro)
  jira-comment                       # POST /comment/<KEY> (write seguro)
  jira-assign                        # POST /assign/<KEY> (write seguro)
  jira-transition                    # POST /transition/<KEY> (DESTRUCTIVO --yes)
~/.config/systemd/user/
  jira-sidecar.service               # systemd --user, auto-start
~/.openclaw/extensions/
  jira-context-preflight/            # plugin instalado
~/openclaw-plugins/
  jira-context-preflight/            # source del plugin
~/.claude/skills/
  jira/
    SKILL.md                         # triggers para Claude Code
    setup-jira.sh                    # instalador portable
    files/jira.py                    # copia del client
    files/bin/jira-*                 # copias de los wrappers
```

## Endpoints del sidecar (127.0.0.1:9002)

### Read
- `GET /health` → `{ok, ts}`
- `GET /myself` → perfil del usuario logueado
- `GET /issue/<KEY>` → ticket compact (cached 60s, dispara vault sync)
- `GET /search?jql=...&max=N` → array de issues (cached 300s)
- `GET /my?status=open|all` → mis tickets (cached 300s)
- `GET /transitions/<KEY>` → transiciones disponibles del ticket

### Write
- `POST /issue/create` body: `{project, summary, description, issuetype, assignee, labels, priority}`
- `POST /transition/<KEY>` body: `{to: "<target>"}`
- `POST /comment/<KEY>` body: `{body: "<texto>"}`
- `POST /assign/<KEY>` body: `{assignee: "me"|"email"|accountId}`

Cada write invalida `ISSUE_CACHE[key]` + limpia `SEARCH_CACHE`, y enqueuea vault sync.

## Cómo verificar que todo anda

```bash
# Servicios
systemctl --user is-active jira-sidecar openclaw-gateway
# → active / active

# Sidecar responde
curl -s http://127.0.0.1:9002/health
# → {"ok": true, ...}

# Auth contra Jira
curl -s http://127.0.0.1:9002/myself | python3 -m json.tool | head -10
# → displayName: Catriel Mercurio

# Smoke test wrapper
jira-my | python3 -c "import sys,json; d=json.load(sys.stdin); print('total tickets:', d['total'])"

# Plugin cargado
journalctl --user -u openclaw-gateway --since "5 minutes ago" | grep jira-context-preflight | tail
```

## Workspace

- **URL:** https://bluinc.atlassian.net
- **Owner:** Catriel Mercurio (team@libreopcion.com, accountId `6070ddbe...`)
- **Proyectos visibles:** 31 (ADATA, SNB, MKT, ASUS, COM, COB, BLUWEB, BROT, BULLY, ACER, LOCAPP, ...)

## Configuración relevante

| Variable env | Default | Override |
|---|---|---|
| `JIRA_ISSUE_TTL` | 60 (segundos) | systemd unit |
| `JIRA_SEARCH_TTL` | 300 (segundos) | systemd unit |
| `JIRA_SIDECAR_HOST` | 127.0.0.1 | systemd unit |
| `JIRA_SIDECAR_PORT` | 9002 | systemd unit |
| `JIRA_VAULT_SYNC` | 1 (enabled) | systemd unit — set 0 para deshabilitar |
| `VAULT_BASE_URL` | https://10.10.10.7:27124 | env del sidecar |
| `VAULT_TOKEN` | (hardcoded default, ver CLAUDE.md) | env del sidecar |
| `JIRA_VAULT_FOLDER` | `Bily/jira` | env del sidecar |

## Performance medida

- `jira-my` cache miss: **768 ms** (round-trip a bluinc.atlassian.net)
- `jira-my` cache hit: **31 ms** (25× speedup)
- Sync vault de un ticket completo (descripción + 7 comments): ~400 ms (background, no bloquea respuesta)
- Rate limit interno: 8 req/s burst 20 (Jira tope: 10 req/s)

## Comandos para mantenimiento

```bash
# Restart sidecar (después de tocar jira.py)
systemctl --user restart jira-sidecar

# Restart gateway (después de tocar el plugin)
openclaw plugins install ~/openclaw-plugins/jira-context-preflight --force
systemctl --user restart openclaw-gateway

# Logs en vivo
journalctl --user -u jira-sidecar -f
journalctl --user -u openclaw-gateway -f | grep jira-context-preflight

# Forzar resync de un ticket
curl -s http://127.0.0.1:9002/issue/<KEY> >/dev/null && sleep 3 && vault-get Bily/jira/<KEY>.md
```

## Ver también

- [[Inicio|Diseño técnico completo]]
- [[changelog|Cronología de fases]]
- [[Bily/jira/Inicio|Notas autopobladas]]
- [[Claude/Whisper|Whisper local]] (patrón sidecar análogo)
- [[Claude/Vault-Wrappers|Vault Wrappers]] (mismo patrón anti-alucinación de URLs)
