# Bily — Carpeta del producto (Blu Studio Inc)

**Status:** 🎯 Documentación de planificación v2.0 COMPLETA (reset estratégico Apple-style premium).
**Última actualización:** 2026-05-24

---

## Documentos en esta carpeta

| Doc | Status | Audiencia | Acción |
|---|---|---|---|
| [[Bot-WhatsApp-MVP/Spec\|Spec MVP v2.0]] | ✅ FINAL | Todo el equipo | Lectura referencial |
| [[Bot-WhatsApp-MVP/Brief-Diseno\|Brief Diseño v2]] | ✅ FINAL | Equipo diseño | **Compartir, pueden arrancar** |
| [[Bot-WhatsApp-MVP/Brief-Marketing\|Brief Marketing v2]] | ✅ FINAL | Equipo marketing | **Compartir, pueden arrancar** |
| [[Bot-WhatsApp-MVP/ADR\|Architecture Decision Record v1.0]] | ✅ FINAL | Tech lead + devs | Sin cambios (arquitectura misma) |
| [[Bot-WhatsApp-MVP/Brief-Devs\|Brief Técnico Devs]] | ✅ FINAL | 4 devs + QA | Sin cambios significativos |

---

## Resumen ejecutivo v2.0 (Apple-style reset)

### Producto
- **Nombre:** Bily (1 L) · empresa **Blu Studio Inc**
- **Dominio:** `billy.blustudioinc.com`
- **Pricing:** **$249 USD/mes** (~275k ARS) single tier premium
- **Trial:** 14 días self-service, sin tarjeta, sin demo
- **Target:** dueños PyME + profesionales premium (Arg primero)
- **Strategy:** **Apple-style** (premium minimal sin friction)

### Economics v2.0 (realista para Argentina)
- **Velocidad realista:** 10 nuevos paying users/mes
- **Costo equipo:** $18k/mes (SUBSIDIADO por Blu Studio Inc — contable pero no cashflow puro)
- **Costo marketing:** $8-15k/mes (cashflow real)
- **Margen por user:** $219/mes
- **Cashflow break-even:** ~mes 6 (~55 users cubren marketing real)
- **Contable break-even total:** ~mes 16 (~140 users cubren equipo+marketing)
- **Runway cashflow real necesario:** $50-80k USD
- **Plateau steady-state:** ~200 users → $44k margen/mes ($14k profit estable)

### Stack técnico (sin cambios vs v1.0)
- **Lenguajes:** Híbrido TypeScript + Python
- **DBs:** SQLite-per-agente + PostgreSQL central
- **WhatsApp:** Phone farm Androids + whatsapp-web.js
- **Browser:** Puppeteer compartido (WA tab + browse tabs)
- **LLM:** Vercel AI SDK + router con Ollama fallback
- **Brain:** Markdown REST API custom + SQLite FTS5
- **Auth:** Custom JWT
- **Deploy:** On-prem (server actual Catriel) + cloud storage backups
- **Monorepo:** pnpm workspaces + turbo

### Cronograma
- **8-10 semanas dev** a MVP cobrable (4 stages)
- **+1-2 meses** iteración con beta
- **Launch público:** mes 3-4 post-arranque dev
- **Tracción real:** 100+ users mes 12, 175+ mes 24

### Equipo
- 3 Sr devs + 1 Jr + 1 QA + diseño + marketing
- Catriel como PM (50-100% tiempo) + **founder-led sales** para primeros 30 clientes
- Equipo subsidiado por Blu Studio Inc (no es cashflow puro nuevo)

---

## Decisiones clave del reset v2.0

| Categoría | Decisión v2.0 |
|---|---|
| Pricing | **$249/mes single tier** (vs $59 v1.0) |
| Strategy | **Apple-style** premium minimal sin friction |
| Sales motion | Self-service + founder-led primeros 30 (NO demos formales) |
| Customer success | Reactivo (responde si escriben), NO outbound |
| Trial | 14 días sin tarjeta, full features con cap |
| Marketing | Brand premium + storytelling + boca-en-boca · NO ads gritones · NO descuentos |
| Costo equipo | Subsidiado por Blu Studio Inc (contable, no cashflow) |
| Runway real | $50-80k (solo cashflow marketing) |
| Velocidad realista | 10 nuevos/mes Arg (recalibrado vs proyecciones SaaS internacionales) |

---

## Próximos pasos inmediatos

| Paso | Owner | Status |
|---|---|---|
| Compartir Brief-Diseno v2 + assets Blu Studio | Catriel | **Esta semana** |
| Compartir Brief-Marketing v2 + presupuesto + abogado | Catriel | **Esta semana** |
| Compartir Spec + ADR + Brief-Devs con tech lead | Catriel | **Esta semana** |
| Pasar a diseño: logo Blu + paleta + 10-20 avatars ejemplo | Catriel | Semana 1 |
| Kickoff técnico con equipo dev (1h call) | Catriel + Sr 1 | Semana 1 |
| Asegurar runway cashflow $50-80k disponible | Catriel | Pre-launch |
| Bloquear agenda 2-3hrs/sem para founder-led sales | Catriel | Pre beta |

---

## Riesgos críticos a vigilar

1. **PM (Catriel) saturado** — si no liberás 50%+ tiempo + founder-led sales, todo se traba
2. **Adquisición real <10/mes** — Apple-style necesita probar que funciona; si no, replantear
3. **Conversión trial→paid <25%** — premium $249 necesita conversión alta de los pre-cualificados
4. **WhatsApp ban** — Meta puede banear si detecta automation patterns
5. **Apple-style no convierte como esperamos** — mes 3 review obligatorio
6. **Equipo Blu Studio desbalanceado** — vigilar carga, no over-allocate a Bily

---

## Cambios respecto a v1.0

**Qué cambió:**
- Pricing $59 → $249 (4x más caro, target diferente)
- Strategy mass-market → premium Apple-style
- Trial con tarjeta → sin tarjeta, 14 días
- Sales: self-service masivo → self-service + founder-led primeros 30
- Marketing: ads agresivos → brand minimalist + boca-en-boca
- Métricas: volumen → calidad (NPS, conversion, retention premium)
- Economics: $18k cashflow real → $18k subsidiado por Blu Studio Inc
- Targets: 1000+ users mes 12 → 100-150 users mes 12 (más realista AR)
- Break-even: mes 10-11 → mes 6 cashflow / mes 16 contable
- Runway: $100-130k → $50-80k cashflow

**Qué NO cambió:**
- Producto (mismas features MVP)
- Arquitectura técnica (mismo stack del ADR)
- Sprint plan dev (mismos 4 stages)
- Equipo (mismas personas, mismos roles)
- Geo (Argentina MVP, LATAM fase 2)
- Brand foundations (Bily + Blu Studio Inc)
- Phone farm setup
- Whisper stack reuso

---

## Relacionado

- [[Bily/Productos/Billy-Bot|Arquitectura Billy Bot (referencia)]]
- [[Bily/Productos/Bot-WhatsApp-Nativo|Idea original del producto]]
- [[Bily/MEMORIA|MEMORIA de Bily — reglas operativas]]
- [[Claude/Whisper|Stack whisper local reusable]]
- [[Claude/Vault-Wrappers|Patrón vault-wrappers]]
