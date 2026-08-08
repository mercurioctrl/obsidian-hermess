# Vault MCP — la bóveda como tools nativas de Bily

**Creado:** 2026-08-08 por Claude (Opus 5) — sesión de diagnóstico "Bily dice que no tiene acceso a Obsidian".
**Reemplaza (para Bily):** el skill `obsidian-mind`, que murió en el update del 2026-08-02.
**Server:** `/home/hermess/vault/mcp_server.py` — python3 stdlib, JSON-RPC 2.0 por stdin/stdout.

---

## El síntoma

Catriel le manda a Bily un VEP de autónomos pagado y le pide cargarlo en la bóveda. Bily responde:

> *"Como no tengo acceso directo a la API de Obsidian desde acá, necesito que me confirmes dos cosas..."*

Y le pide a Catriel la ruta de la nota y el formato de la tabla. Raro: Bily venía escribiendo bitácoras en la bóveda hacía meses.

## El diagnóstico

Tres hechos que juntos explican todo:

1. **El skill `obsidian-mind` dejó de existir.** Vivía en `~/.openclaw/plugin-skills/obsidian-mind/SKILL.md`. Dos problemas:
   - `plugin-skills/` es un **directorio manejado por los plugins**, no un skill root de usuario. El update a OpenClaw `2026.7.1-2` (2026-08-02, ver [[Bily/aprendizajes/2026-08-02-fix-gpt5-openclaw-relink-whatsapp|aprendizaje 2026-08-02]]) lo regeneró entero: `browser-automation/` y `canvas/` quedaron con fecha ago-2 20:22, `obsidian-mind/` quedó huérfano con fecha may-16.
   - El `SKILL.md` **no tenía frontmatter YAML** (`name:` / `description:`), hoy obligatorio para que se indexe.
   - Resultado: `openclaw skills info obsidian-mind` → *"Skill not found"*. No figura entre los 53 skills listados.

2. **El `AGENTS.md` de Bily lo mandaba a ese skill fantasma.** Decía literal *"Para buscar contexto global, usa la API de Obsidian (ver skill `obsidian-mind`)"* — sin IP, sin token, sin mencionar los wrappers `~/bin/vault-*`. El puntero apuntaba a la nada.

3. **Bily nunca intentó nada.** En la trayectoria de la sesión (`sessions/e32d1af6-*.trajectory.jsonl`) tenía **33 tools disponibles, incluido `exec`** con `security:full`, y los 10 de Jira por MCP. No hubo error de red: la API respondía `HTTP 200` en 16 ms. Simplemente, en su contexto era verdad que no tenía cómo.

**Daño previo, no detectado:** la bitácora del 2026-08-05 nunca subió. Quedó en `~/.openclaw/workspace/memory/pending-obsidian/Bily/bitacoras/2026-08-05.md`, con un pendiente autoescrito que dice *"Subir esta bitácora a Cerebro cuando vuelva a estar disponible la API local de Obsidian"*. La API estaba perfecta; lo que faltaba era el acceso en contexto.

## La lección

> Un markdown que el modelo tiene que **acordarse de cargar** es frágil. Una tool en su lista **siempre está**.

El contraste estaba a la vista en la misma sesión: **Jira le funciona** porque está como MCP nativo ([[Bily/aprendizajes/2026-08-02-fix-gpt5-openclaw-relink-whatsapp|10 tools siempre presentes]]), y la bóveda no, porque dependía de una decisión del modelo. Es el mismo principio de *intent al LLM, no regex* aplicado al **acceso a datos**: no le expliques cómo componer el `curl`, dale la tool bien formada.

Catriel eligió el camino MCP explícitamente por esta razón.

## El servidor

Mismo molde que [[jira/jira|el MCP de Jira]] (`~/jira/mcp_server.py`). Stdlib only, sin dependencias.

| Tool | Verbo | Notas |
|---|---|---|
| `vault_search` | POST `/search/simple/` | Recorta a 3 contextos por match y agrega `total`/`shown` para no inundar el contexto |
| `vault_get` | GET `/vault/<path>` | Devuelve el markdown crudo |
| `vault_ls` | GET `/vault/<folder>/` | Parsea `files[]` del JSON |
| `vault_append` | **POST** `/vault/<path>` | Agrega al final, crea si no existe. **Default recomendado para escribir** |
| `vault_put` | PUT `/vault/<path>` | Sobrescribe la nota entera |
| `vault_delete` | DELETE `/vault/<path>` | Guardrail: solo `Bily/` y `Claude/`, el resto tira `RuntimeError` |

**Por qué `vault_append` es el default.** Con `curl` crudo Bily solo tenía PUT: para sumar una línea a una bitácora tenía que leer → modificar → reescribir entera. Ahí es donde se pisa contenido. El `POST` del Local REST API hace append nativo; ahora escribir es de una sola operación y no destructivo.

**Detalles:**
- SSL con `CERT_NONE` a propósito (el cert del plugin es autofirmado).
- Overrides por env: `VAULT_BASE_URL`, `VAULT_TOKEN`, `VAULT_MCP_TIMEOUT` (default 30s).
- Errores traducidos a lenguaje útil: un `404` dice *"no existe en la bóveda: <ruta>"*; un fallo de red dice *"¿Obsidian está abierto en 10.10.10.7 con el plugin Local REST API activo?"*.

## Registración

```bash
openclaw mcp add vault --command python3 --arg /home/hermess/vault/mcp_server.py
openclaw mcp reload   # los agentes activos toman la config nueva en el próximo runtime build
```

Queda en `mcp.servers` de `~/.openclaw/openclaw.json` (backup previo en `openclaw.json.pre-vault-mcp`).
Bily las ve con prefijo de server: **`vault__vault_ls`**, `vault__vault_append`, etc.

Verificación:
```bash
openclaw mcp probe vault    # → "vault: 6 tools"
openclaw mcp status         # → jira: stdio · vault: stdio
```

## Verificación end-to-end

Las 6 tools probadas por JSON-RPC directo, incluido el guardrail (`vault_delete Blu/algo.md` → rechazado) y el ciclo append → append → get → delete → 404. La nota de prueba `Claude/_selftest_mcp.md` quedó borrada.

Smoke test con Bily real, en sesión aislada (`--session-key agent:main:vault-mcp-smoketest`, sin `--deliver`, para no tocar el chat de WhatsApp):

> *"Usé la tool `vault__vault_ls` para listar el contenido de la carpeta `Bily/`."*

## Cambios en `AGENTS.md` de Bily

`~/.openclaw/workspace/AGENTS.md`, sección nueva **"🗄️ Cómo acceder a la bóveda"**: tabla de las 6 tools, cuándo usar cada una, y las reglas de escritura. Lo importante que se agregó:

- **`append` por default**, `put` solo para notas nuevas o previo `vault_get`.
- **Nunca inventar rutas** — `vault_ls` primero. Si ya existe una carpeta que sirve, usarla en vez de crear estructuras paralelas.
- **Nunca decir "no tengo acceso" sin haber intentado la tool.** Si falla, reportar el error textual: un error de red significa que Obsidian está cerrado en `10.10.10.7`, y eso sí es información útil para Catriel. En ese caso, dejar lo que iba a escribir en `memory/pending-obsidian/<misma ruta>` y avisar.

Se sacó el puntero al skill fantasma.

## Skill roots válidos en OpenClaw

Por si algún día hace falta un skill de verdad (precedencia de mayor a menor):

| Alcance | Ruta |
|---|---|
| Por agente | `<workspace>/skills` |
| Proyecto-agente | `<workspace>/.agents/skills` |
| Personal | `~/.agents/skills` |
| Compartido | `~/.openclaw/skills` |
| Extra | `skills.load.extraDirs` |

**Nunca** `~/.openclaw/plugin-skills/` — es de los plugins y se regenera en cada update. Y siempre con frontmatter YAML (`name`, `description`).

## Cabos sueltos

- `~/.openclaw/plugin-skills/obsidian-mind/` sigue en disco, inerte (no lo carga nadie). Pendiente decidir si se borra.
- La bitácora pendiente del 2026-08-05 y el pago de autónomos (VEP período 07/2026, $74.003,80, CUIT 20-33457962-0) quedaron para que **los cargue Bily**, como prueba de fuego del fix.
- `Bily/pagos/` y `Bily/Finanzas/` **ya existían** — cuando Bily preguntó "¿tenés alguna estructura para esto?", la respuesta estaba a un `vault_ls` de distancia.
- Pendiente opcional: registrar el mismo MCP en Claude Code para unificar (hoy Claude Code sigue usando los wrappers).

## Ver también

- [[Claude/Vault-Wrappers|Vault Wrappers]] — los 5 comandos `~/bin/vault-*`, ahora fallback de Bily y camino principal de Claude Code
- [[Claude/MEMORIA#Estado 2026-08-08 — Vault MCP|MEMORIA § Estado 2026-08-08]]
- [[Bily/aprendizajes/2026-08-08-vault-mcp|Aprendizaje de Bily 2026-08-08]]
- [[Bily/aprendizajes/2026-08-02-fix-gpt5-openclaw-relink-whatsapp|2026-08-02: el update que rompió esto]]
