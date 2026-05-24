# Bily — Carpeta del producto (Blu Studio Inc)

**Status:** spec cerrada (v1.0+), briefs FINALIZADOS para handoff a equipos, ADR en draft.
**Última actualización:** 2026-05-24

---

## Documentos en esta carpeta

| Doc | Status | Audiencia | Acción |
|---|---|---|---|
| [[Bot-WhatsApp-MVP/Spec\|Spec MVP v1.0+]] | ✅ Cerrada | Todo el equipo | Lectura referencial |
| [[Bot-WhatsApp-MVP/Brief-Diseno\|Brief Diseño]] | ✅ FINAL | Equipo de diseño | **Compartir hoy, pueden arrancar** |
| [[Bot-WhatsApp-MVP/Brief-Marketing\|Brief Marketing]] | ✅ FINAL | Equipo de marketing | **Compartir hoy, pueden arrancar** |
| [[Bot-WhatsApp-MVP/ADR\|Architecture Decision Record]] | 🟡 v0.1 draft | Tech lead + Sr devs | **Cerrar 4 decisiones abiertas → v1.0** |
| [[Bot-WhatsApp-MVP/Brief-Devs\|Brief técnico para devs]] | ⏳ Pendiente | Equipo técnico | Después del ADR final |

---

## Resumen ejecutivo

**Producto:** Bily (grafía oficial, 1 L) — asistente IA con identidad propia (nombre random B-* + avatar único + personalidad propia), vive en su propio número de WhatsApp, cerebro markdown persistente.

**Empresa:** Blu Studio Inc.

**Dominio:** `billy.blustudioinc.com` (excepción de grafía con el producto Bily).

**Pricing:** $59 USD/mes single tier · trial 14 días sin tarjeta.

**Target:** profesionales individuales + dueños PyME en Argentina (LATAM en fase 2).

**Costos operativos mensuales:**
- Equipo + infra base: $18,000
- Marketing agresivo: $8,000-15,000 (promedio $11,500)
- **Total: ~$29,500/mes**

**Break-even:** ~720 paying users (estimado mes 10-11 post-launch).

**Runway necesario:** $100-130k USD para cubrir gap mes 0-10.

**Cronograma:** 8-10 semanas dev MVP + 1-2 meses iteración + launch público mes 3-4.

---

## Decisiones clave ya tomadas

| Categoría | Decisión |
|---|---|
| Stack agente | Custom thin orchestrator (NO OpenClaw/Hermes/Letta) |
| Lenguaje | TypeScript/Node (propuesto, confirmar) |
| Cerebro | Markdown REST API propio + SQLite FTS5 (NO Obsidian app) |
| WhatsApp | Phone farm Androids + whatsapp-web.js + puppeteer compartido con browse tool |
| LLM | Vercel AI SDK + router custom con fallback Ollama |
| Brain access | Wrappers `brain_*` como tools (LLM nunca escribe URLs) |
| Per-tenant | 1 systemd process por agente (K8s scale-to-zero post-MVP) |
| Whisper | Reuso del stack ya construido (whisper.cpp + sidecar) |
| Geo | Argentina + español rioplatense (LATAM fase 2) |
| Identidad agente | Nombre random B-* INMUTABLE + avatar único minteado |
| MercadoPago | Cuenta operativa con recurrentes habilitados |
| Abogado | Estudio de confianza disponible |
| PM | Catriel (50-100% del tiempo) |

---

## Próximos pasos inmediatos

| Paso | Owner | Status |
|---|---|---|
| Compartir Brief-Diseno con equipo diseño | Catriel | **Hoy** |
| Compartir Brief-Marketing con equipo marketing | Catriel | **Hoy** |
| Pasar a diseño: logo Blu + paleta colores + 5-10 avatars de ejemplo | Catriel | Esta semana |
| Cerrar 4 ADRs abiertas en el ADR v0.1 | Catriel + Claude | Próxima sesión |
| Brief técnico para devs (sprint plan stage 1) | Tech lead + Claude | Después del ADR final |
| Conseguir runway $100-130k USD | Catriel | Pre-launch |
| Kickoff técnico con equipo completo | Catriel | Semana 0 dev |

---

## Relacionado

- [[Bily/Productos/Billy-Bot|Arquitectura Billy Bot (referencia inicial)]]
- [[Bily/Productos/Bot-WhatsApp-Nativo|Idea original del producto]]
- [[Claude/Whisper|Stack whisper local reusable]]
- [[Claude/Vault-Wrappers|Patrón vault-wrappers]]
