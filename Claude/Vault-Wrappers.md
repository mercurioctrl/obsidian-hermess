# Vault Wrappers — API canónica para tocar la bóveda de Catriel

**Creados:** 2026-05-23 por Claude (Opus 4.7) durante la sesión nocturna del whisper stack.
**Motivo:** Eliminar errores de URL/puerto/token/flags que el LLM (sobre todo deepseek-chat cuando Gemini queda sin créditos) tiende a alucinar al escribir `curl` crudo.

## Los 5 comandos en `~/bin/`

| Comando | Verbo HTTP | Devuelve | Ejemplo |
|---|---|---|---|
| `vault-get <ruta>` | GET | body (md si nota, JSON si carpeta) | `vault-get Bily/kanban/General.md` |
| `vault-ls [ruta]` | GET | un nombre por línea (parseado del JSON) | `vault-ls Bily/kanban/` |
| `vault-search <query>` | POST `/search/simple/` | JSON con matches | `vault-search whisper` |
| `vault-put <ruta> <src>` | PUT | mensaje `HTTP <code>` | `echo "# foo" \| vault-put Bily/notas/x.md -` |
| `vault-delete <ruta>` | DELETE | mensaje `HTTP <code>` | `vault-delete Bily/aprendizajes/viejo.md` |

**Defaults hardcodeados** (override con env vars):
- `VAULT_BASE_URL` = `https://10.10.10.7:27124`
- `VAULT_TOKEN` = el de [[Claude/Whisper#config]] / `CLAUDE.md` raíz

**Convenciones:**
- Salida → stdout
- Errores → stderr
- Exit `0` si HTTP 2xx, `!=0` si falla
- `vault-put` infiere `Content-Type` por extensión (md→markdown, ogg→audio/ogg, pdf→application/pdf, etc.)
- `vault-put` acepta `-` como segundo arg para leer de stdin
- `vault-delete` rechaza paths que NO empiecen con `Bily/` (guardrail anti-borrón accidental)

## Por qué existen

Sin los wrappers, Bily (cuando corre en deepseek por fallback de Gemini sin créditos) escribía cosas como:

```bash
curl -X GET -H "Authorization: Bearer ..." http://10.10.10.7/vault/Bily/kanban/General.md
```

Errores típicos: `http` en vez de `https`, falta `:27124`, falta `-k`. Con los wrappers el modelo solo escribe `vault-get Bily/kanban/General.md` — imposible equivocarse.

## Integración con OpenClaw / Bily

El environment del `openclaw-gateway.service` ya hereda `/home/hermess/bin` en su PATH (vía `.profile`), así que Bily invoca por nombre sin path absoluto:

```bash
systemctl --user show openclaw-gateway -p Environment | grep -o 'PATH=[^ ]*'
# PATH=/usr/bin:/home/hermess/.local/bin:/home/hermess/.npm-global/bin:/home/hermess/bin:...
```

La regla está en [[Bily/MEMORIA]] sección "API canónica" + "URL EXACTA" + "Regla de Oro".

## Workflow recomendado para Bily

```bash
# Leer kanban
vault-get Bily/kanban/General.md

# Agregar línea a nota del día (con fallback si no existe)
NOTA="Bily/aprendizajes/audios-$(date +%Y-%m-%d).md"
vault-get "$NOTA" > /tmp/n.md 2>/dev/null || echo "# Audios $(date +%Y-%m-%d)" > /tmp/n.md
echo "- $(date -Iseconds): \"hola Bily\"" >> /tmp/n.md
vault-put "$NOTA" /tmp/n.md

# Copiar audio WhatsApp a la bóveda
vault-put Bily/media/audios/abc.ogg /home/hermess/.openclaw/media/inbound/abc.ogg

# Buscar persona
vault-search "Catriel Mercurio" | jq -r '.[].filename' | head -5
```

## Troubleshooting

| Síntoma | Causa probable | Fix |
|---|---|---|
| `command not found: vault-get` desde Bily | Service no heredó PATH | `systemctl --user restart openclaw-gateway` después de tocar `.profile` |
| `HTTP 401` | Token inválido o se rotó | Actualizar `VAULT_TOKEN` env o hardcoded en wrappers |
| `HTTP 404` con un path que existe | Ojo, la API es case-sensitive y diferencia espacios. `vault-ls` del padre confirma el nombre real. |
| Timeout o `Connection refused` | API REST de Obsidian no escucha. Verificar plugin "Local REST API" del Obsidian de Catriel. |

## Relacionado

- [[Claude/Whisper]] — stack de transcripción, mismo session origen
- [[Bily/MEMORIA]] — reglas operativas que apuntan a esta API
- [[Bily/Productos/Billy-Bot]] — producto que va a aprovechar esto a futuro
