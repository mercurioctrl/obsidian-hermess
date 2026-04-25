# aplus-server

Servidor para hostear **A+ content / contenido sindicado** de productos, pensado para ser embebido como **iframe en retailers** (Fravega, Mercado Libre, Compragamer, Libre Opción, etc). Diseñado para que **robar el contenido sea caro** sin complicar el flujo de deploy.

Cada producto es una carpeta `content/<slug>/` con su `index.html` + `assets/` (imágenes, MP4, css, js).

## Notas del proyecto

- [[aplus-server/arquitectura|Arquitectura]] — flujo HMAC, rewriter de HTML, capas defensivas
- [[aplus-server/stack|Stack]] — Caddy 2 + Fastify + Docker Compose + Cloudflare
- [[aplus-server/integracion-retailers|Integración con retailers]] — snippet iframe + config + gotchas por retailer
- [[aplus-server/migracion-libreopcion|Migración desde /micrositios-files/]] — decisión + contexto técnico de LO
- [[aplus-server/contexto|Contexto]] — modelo de amenazas, gotchas, reglas operativas, patrones de replicación de microsites
- [[aplus-server/memoria|Memoria]] — memoria persistente de Claude (estrategia, estado, referencias, feedback)
- [[aplus-server/changelog|Changelog]] — registro de cambios

## Stack resumido

- **Caddy 2** — TLS automático (Let's Encrypt) + reverse proxy
- **Node 20 + Fastify 4** — firma HMAC de assets, rate-limit por IP
- **Watermark one-shot** (ffmpeg + imagemagick) — trazabilidad por retailer
- **Cloudflare proxied** por delante (oculta IP, cache, DDoS)

## Estado actual (2026-04-16)

- Scaffold local completo en `/Users/hermess/www/aplus-server`
- No es git repo todavía
- Productos:
  - `tuf-rtx5080` (scaffold, sin assets reales)
  - `tuf-gaming-b550m-plus-wifi-ii` — **réplica fiel y pulida** del microsite ASUS (34MB totales). Rebuild completo con Swiper + anchors sticky + 3 galerías: producto (lightbox, 8 fotos 2400×2400), Armoury Crate (chips + slider) y fan control (overlay cross-fade). Iframe-ready (container queries + postMessage de altura).
- **No deployado a VPS**, dominio es placeholder `aplus.tudominio.com`
- Migración de LO: planificada, no iniciada — ver [[aplus-server/migracion-libreopcion|migración]]

## Links rápidos

- Repo local: `/Users/hermess/www/aplus-server`
- Deploy: rsync → VPS Ubuntu → `./start.sh`
- README del repo: `/Users/hermess/www/aplus-server/README.md` (quick start, uso, plan de migración, troubleshooting)
- CLAUDE.md del proyecto: ver sección `## Obsidian`

## Skill asociado

Para replicar microsites nuevos (ASUS u otras marcas) el flujo canónico es vía el skill [[Skills/replicar-microsite/SKILL|Replicar Microsite]]. El skill tiene notas específicas ASUS (mapa de CDNs, cómo encontrar la galería del lightbox, patrones de galería reutilizables).

## Proyectos relacionados

- [[Libre Opcion/Libre Opcion|Libre Opción]] — primer retailer objetivo de migración
- [[Asus/Asus|Asus]] — marca principal del contenido A+ servido

---

**Última sincronización:** 2026-04-16
