# Changelog — Bily/Productos

Registro cronológico de cambios en la carpeta de productos.

## 2026-05-25

**Infra de visión para Bily (tarde):**
- Bily falló dos veces ante imágenes de WhatsApp con texto (comprobantes bancarios) — patrón de auto-incapacidad post-fallo de herramienta externa, ignorando el bloque multimodal ya cargado.
- Infra nueva reusable por el MVP: tesseract instalado en sistema + plugin OpenClaw `image-ocr-preflight` que pre-extrae texto antes del prompt (espejo del whisper preflight). End-to-end ~2.5s.
- Documentado en [[Claude/Image-OCR]] y linkeado desde [[Bily/Productos/Bot-WhatsApp-MVP/Inicio]] como infra de stack reusable.
- Sin cambios en specs/ADR/briefs — es infra del agente, no producto.

**Migración de convención de índice (Inicio.md → Productos.md):**
- Creado `Productos.md` como hub canónico (skill `/configurarBoveda` manda que la nota índice se llame igual que la carpeta).
- Eliminado `Inicio.md` viejo después de migrar contenido y wikilinks.
- Reescritos wikilinks en: `Bily/Inicio.md`, `Skills/bily/SKILL.md`, `Home.md`.
- Decisión: `Bily/Productos/` queda como isla canónica dentro de la rama Bily (que sigue usando `Inicio.md` como convención). No se uniformó el resto.

**Vinculación con working directory:**
- `/home/hermess/CLAUDE.md` ahora declara `Bily/Productos/` como carpeta de proyecto, con cheatsheet de wrappers `vault-*`.
- Sincronización ejecutada con `/sincronizarBoveda` (skill recién importado en `~/.claude/skills/sincronizar-boveda/SKILL.md`).

Archivos tocados: `Bily/Productos/Productos.md` (nuevo), `Bily/Productos/Inicio.md` (eliminado), `Bily/Productos/changelog.md` (nuevo).

## 2026-05-23 _(consolidado retroactivo)_

**Planificación Bot-WhatsApp-MVP v2.0:**
- Pivot estratégico de $59 freemium → $249/mes Apple-style premium tras reality check (Argentina: ~10 nuevos clientes/mes).
- Documentos vivos del producto: `Spec.md`, `ADR.md`, `Brief-Devs.md`, `Brief-Diseno.md`, `Brief-Marketing.md`, `Inicio.md` (hub del proyecto).
- Stack definido: TypeScript+Python híbrido, SQLite-per-agent, Postgres central para users/billing, JWT custom, on-prem deploy.
- Economics: cashflow break-even mes 6 (~55 users), runway necesario $50-80k (subsidio Blu Studio Inc).
