# aplus-server

Servidor para hostear **A+ content / contenido sindicado** de productos, pensado para ser embebido como **iframe en retailers** (Fravega, Mercado Libre, Compragamer, etc). Diseñado para que **robar el contenido sea caro** sin complicar el flujo de deploy.

Cada producto es una carpeta `content/<slug>/` con su `index.html` + `assets/` (imágenes, MP4, css, js).

## Notas del proyecto

- [[aplus-server/arquitectura|Arquitectura]] — flujo HMAC, rewriter de HTML, capas defensivas
- [[aplus-server/stack|Stack]] — Caddy 2 + Fastify + Docker Compose + Cloudflare
- [[aplus-server/contexto|Contexto]] — modelo de amenazas, gotchas, reglas operativas
- [[aplus-server/changelog|Changelog]] — registro de cambios

## Stack resumido

- **Caddy 2** — TLS automático (Let's Encrypt) + reverse proxy
- **Node 20 + Fastify 4** — firma HMAC de assets, rate-limit por IP
- **Watermark one-shot** (ffmpeg + imagemagick) — trazabilidad por retailer
- **Cloudflare proxied** por delante (oculta IP, cache, DDoS)

## Productos actuales

- `tuf-rtx5080`

## Links rápidos

- Repo local: `/Users/hermess/www/aplus-server`
- Deploy: rsync → VPS Ubuntu → `./start.sh`
- CLAUDE.md del proyecto: ver sección `## Obsidian`

---

**Última sincronización:** 2026-04-16
