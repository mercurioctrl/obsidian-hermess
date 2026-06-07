---
tags: [jira, index, bily]
sync_source: jira-sidecar
---

# Jira (sync automático)

Carpeta sincronizada automáticamente por `jira-sidecar` (`~/jira/jira.py`).
Cada vez que algún wrapper o el plugin OpenClaw consulta un ticket
(`GET /issue/<KEY>`) o lo modifica (POST writes), el sidecar:

1. Hace fetch completo del ticket con descripción + comentarios.
2. Convierte ADF → Markdown.
3. Hace PUT a `Bily/jira/<KEY>.md` en esta bóveda (debounce 30s por key).

## Para qué sirve

- **Búsqueda full-text:** `vault-search "deslogueo"` encuentra tickets relevantes.
- **Lectura offline:** otros agentes (Claude Code, skills) leen Jira sin token.
- **Linkeable:** desde cualquier nota podés escribir `[[SNB-3946]]` y Obsidian conecta.
- **Snapshot histórico:** cada nota lleva timestamp de sync — útil para auditar.

## Convenciones

- Filename: `<KEY>.md` (ej: `SNB-3946.md`).
- Frontmatter: `jira_key, status, assignee, assignee_email, reporter, priority, issuetype, project, updated, created, url, tags, sprint`.
- Tags automáticos: `jira`, el `project` (ej: `SNB`), y `status` slugificado (ej: `esperando-por-ayuda`).
- Body: título `# <KEY> · <summary>`, link a Jira, sección "Descripción", sección "Comentarios" con cada comment como sub-heading.

## Cómo se actualiza

- Automático: cada vez que el sidecar resuelve un `/issue/<KEY>` o un write — debounce de 30s para evitar duplicados.
- Manual: `curl http://127.0.0.1:9002/issue/<KEY>` desde el server.
- Forzar resync de un ticket cualquiera: editá la nota en Obsidian (no recomendado — el sidecar la sobreescribirá en la próxima consulta).

## Para deshabilitar el sync

Editá `~/.config/systemd/user/jira-sidecar.service` y agregá:

```
Environment=JIRA_VAULT_SYNC=0
```

Después: `systemctl --user daemon-reload && systemctl --user restart jira-sidecar`.

## Ver también

- [[Integracion-Jira/Inicio|Diseño completo de la integración Jira]]
- [[Claude/Vault-Wrappers|Vault Wrappers]] (mismo patrón de auth)
- [[Claude/Whisper|Whisper local]] (patrón sidecar análogo)
