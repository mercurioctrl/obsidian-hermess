# Memoria del proyecto — Tarjetas

> [[Tarjetas]] · [[contexto]]
> Consolidado de la memoria de Claude para este proyecto (`~/.claude/projects/-var-www-Tarjetas/memory/`).

## Proyecto

`/var/www/Tarjetas`: análisis de resúmenes Santander Río — Visa `1103119048` y Amex `1103152386`, titulares Delorenzi Guidobono (titular) + Catriel Ed Mercurio (adicional). Objetivo: estrategia de pago y control de gastos. Doc técnica y pipeline en `CLAUDE.md` y `docs/PIPELINE.md` del repo; notas en `Finanzas/Tarjetas` de la bóveda.

## Feedback / cómo trabajar

- Preferir **gráficos como imagen (PNG + SVG)** por sobre Mermaid (leyenda garantizada, independiente de la versión de Obsidian).
- matplotlib bloqueado (PEP 668) → SVG a mano + `convert` (ImageMagick) para rasterizar.
- Valora **fidelidad exacta de montos** (verificar contra el PDF) y **análisis accionables** (estrategia), no solo datos.
- Español rioplatense.

## Estado (sep 2026)

Resúmenes de septiembre (cierre 27-ago, ambos a **TNA 78%**):
- **Amex:** total $13.995.697,52; pagó **$7.000.000** el 07-09 (vto) → saldo financiándose **~$6.995.697,52**.
- **Visa:** total $14.689.557,63; pagó **$6.350.000** ($5,3M el 03-09 + $50k el 05-09 + **$1,0M extra el 08-09**) → saldo financiándose **~$8.339.557,63**.
- Saldo financiándose combinado: **~$15,34M** a TNA 78%.

Regla de decisión aplicada: con TNA igual entre tarjetas, el pago extra va a la de **mayor saldo financiado** (Visa) para cortar más interés compuesto. Meta: financiado en $0 antes de fin de 2026.

### Estado previo (ago 2026)

Deuda total ~$28,2M; saldo financiado ~$16,7M (TNA 77,9%). Pagó $5,5M a Visa el 2026-08-08 y $6,1M a Amex ($1,0M + $2,4M + $0,8M el 09-ago + $0,9M el 14-ago + $1,0M el 18-ago, parciales, tarjeta ****-34375 → cubre el mínimo $4,198M). Resumen Amex agosto: quedan $7,27M por pagar (vto 10-ago ya pasó → financiándose).
