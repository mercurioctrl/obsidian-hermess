# Changelog

## 2026-04-16

- **init**: Estructura inicial del proyecto.
  - Caddy 2 + Fastify 4 + Docker Compose
  - HMAC signing de assets con TTL configurable
  - Rate limit por IP (30/min HTML, 300/min assets)
  - Referer check + CSP `frame-ancestors` desde env `ALLOWED_REFERERS`
  - Container watermark one-shot (ffmpeg + imagemagick) separado de compose
  - Scripts: `start.sh` (idempotente), `add-product.sh`, `watermark.sh`
  - Auto-gen de `TOKEN_SECRET` en primer `start.sh`
- **content**: primer producto agregado → `tuf-rtx5080`
- **docs**: `CLAUDE.md` del proyecto con gotchas, no-hacer, convenciones
- **obsidian**: carpeta del vault vinculada (`aplus-server/`) via `/configurarBoveda`
