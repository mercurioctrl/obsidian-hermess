# Bily — Skills por grupo (group-skill-router)

**Fecha:** 2026-06-18 · Plugin OpenClaw en host `hermess`. Idea de Catriel: **cada grupo de WhatsApp con su propio set de instrucciones**, y Bily sabe cuál usar según de qué grupo viene el mensaje. Escalable sin tocar código.

## Cómo funciona
Plugin **`group-skill-router`** (`~/openclaw-plugins/group-skill-router/`, modelado sobre los preflights de whisper/OCR). Hook `before_prompt_build`: extrae el JID de grupo del `sessionKey`, lee `~/openclaw-groups/<jid>/instructions.md` y lo **inyecta al prompt** (`prependContext`, con provenance declarada). Si el grupo no tiene archivo, no inyecta nada.

```
~/openclaw-groups/
  └── <group-jid>/instructions.md   ← el "skill" de ese grupo
```

## Agregar un grupo nuevo
Solo crear `~/openclaw-groups/<jid>/instructions.md` con las instrucciones — **sin reiniciar ni tocar código** (el plugin lee el archivo en cada mensaje). El JID se obtiene mandando un mensaje en el grupo y buscando el `sender-key-<jid>` recién creado en `~/.openclaw/credentials/whatsapp/`.

## Instalación (referencia)
- `openclaw plugins install ~/openclaw-plugins/group-skill-router` + `openclaw plugins enable group-skill-router`.
- Patch en `openclaw.json` → `plugins.entries.group-skill-router`: `hooks.allowConversationAccess=true` (para ver el grupo) + `config.groupsDir`.
- `openclaw gateway restart`. Verificar: `openclaw plugins list | grep router`.

## Grupos configurados
- **Infra Blu** (`120363427504587972@g.us`): skill de infraestructura. Ante pedidos de estado/velocidad de WAN, Bily corre `~/wan-mon/status.sh` (vía skill tmux) y reporta. **Probado y funcionando.** Ver [[Monitoreo_WAN]].

## Notas
- `groupPolicy` está en **"open"** → Bily responde en grupos donde está (cuando lo mencionan/le hablan directo).
- Los monitores automáticos de WAN también postean en Infra Blu.

## Ver también
- [[Monitoreo_WAN]] — el script `status.sh` y los monitores que Bily usa.
