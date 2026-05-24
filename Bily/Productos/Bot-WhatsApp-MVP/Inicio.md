# Bily — Carpeta del producto (Blu Studio Inc)

**Status:** 🎯 Toda la documentación de planificación COMPLETA. Listo para arrancar dev.
**Última actualización:** 2026-05-24

---

## Documentos en esta carpeta

| Doc | Status | Audiencia | Acción |
|---|---|---|---|
| [[Bot-WhatsApp-MVP/Spec\|Spec MVP v1.0+]] | ✅ FINAL | Todo el equipo | Lectura referencial |
| [[Bot-WhatsApp-MVP/Brief-Diseno\|Brief Diseño]] | ✅ FINAL | Equipo diseño | **Compartir hoy, pueden arrancar** |
| [[Bot-WhatsApp-MVP/Brief-Marketing\|Brief Marketing]] | ✅ FINAL | Equipo marketing | **Compartir hoy, pueden arrancar** |
| [[Bot-WhatsApp-MVP/ADR\|Architecture Decision Record v1.0]] | ✅ FINAL | Tech lead + Sr devs | Lectura previa a kickoff técnico |
| [[Bot-WhatsApp-MVP/Brief-Devs\|Brief Técnico Devs + Sprint Plan Stage 1]] | ✅ FINAL | 4 devs + QA | **Compartir en kickoff técnico** |

---

## Resumen ejecutivo (todo lo decidido)

### Producto
- **Nombre:** Bily (1 L) · empresa **Blu Studio Inc**
- **Dominio:** `billy.blustudioinc.com`
- **Pricing:** $59 USD/mes single tier · trial 14 días sin tarjeta
- **Target:** profesionales individuales + dueños PyME en Argentina (LATAM fase 2)
- **Diferenciador:** "No es un bot. Es un asistente con nombre, cara y memoria propia, que aprende tu vida y se vuelve irreemplazable porque acumula tu historia personal en un cerebro que es tuyo."

### Stack técnico
- **Lenguajes:** Híbrido TypeScript + Python según componente
- **DBs:** SQLite-per-agente + PostgreSQL central
- **WhatsApp:** Phone farm Androids + whatsapp-web.js
- **Browser:** Puppeteer compartido (WA tab pinned + browse tabs efímeras)
- **LLM:** Vercel AI SDK con router multi-provider + Ollama fallback
- **Brain:** Markdown REST API custom + SQLite FTS5
- **Auth:** Custom JWT
- **Deploy:** On-prem (server actual de Catriel) + object storage cloud para backups
- **Monorepo:** pnpm workspaces + turbo

### Economics
- **Costos mensuales:** $18k equipo+infra + $8-15k marketing = **~$29.5k/mes**
- **Break-even:** ~720 paying users (mes 10-11 post-launch)
- **Runway necesario:** $100-130k USD para cubrir mes 0-10
- **Mes 12 (1000 users):** $41k margen ($11.5k profit/mes)
- **Mes 24 (3500-5000 users):** $144-205k margen ($108-170k profit/mes)

### Cronograma
- **8-10 semanas dev** a MVP cobrable (4 stages: single-tenant → multi-tenant → intelligence → ops+beta)
- **+1-2 meses** iteración con beta
- **Launch público:** mes 3-4 post-arranque dev

### Equipo
- 3 Sr devs + 1 Jr + 1 QA + diseño + marketing
- Catriel como PM (50-100% tiempo) — **cuello de botella a vigilar**

---

## Próximos pasos (acción concreta esta semana)

### Catriel — compartir y arrancar equipos en paralelo

| Acción | Quién recibe |
|---|---|
| Compartir Brief-Diseno + acceso al vault | Equipo diseño |
| Pasar: logo Blu actual + paleta colores + 5-10 ejemplos avatar API | Equipo diseño |
| Compartir Brief-Marketing + presupuesto autorizado ($8-15k/mes) | Equipo marketing |
| Conectar marketing con abogado de confianza | Marketing |
| Compartir ADR + Brief-Devs | 3 Sr devs + Jr + QA |
| Agendar kickoff técnico (1h) | Equipo dev |
| Conseguir runway $100-130k | Catriel |

### Sr 1 (tech lead) — pre-kickoff

| Acción | Plazo |
|---|---|
| Leer Spec + ADR + Brief-Devs | Pre-kickoff |
| Cerrar las 4 ADRs secundarias con Sr 2 + Sr 3 | Semana 0 día 1-2 |
| Crear estructura del monorepo según ADR | Semana 0 día 3-4 |
| Setup CI/CD básico (GitHub Actions) | Semana 0 día 4-5 |

### Equipos paralelos (todos arrancan misma semana)

- **Diseño:** brand identity master + avatar guidelines
- **Marketing:** posicionamiento + landing copy + lista de influencers
- **Devs:** semana 0 setup + onboarding

---

## Riesgos conocidos a vigilar

1. **PM (Catriel) saturado** — si no liberás 50%+ tiempo, todo se traba
2. **Mix de uso Pro vs caps** — si users power consumen 2× LLM estimado, margen se erosiona
3. **WhatsApp ban** — Meta puede banear números si detecta automation patterns
4. **Conversión trial → paid <12%** — si pasa, replantear pricing o producto
5. **Runway insuficiente** — sin $100-130k no llegamos a break-even

---

## Relacionado

- [[Bily/Productos/Billy-Bot|Arquitectura Billy Bot (referencia inicial)]]
- [[Bily/Productos/Bot-WhatsApp-Nativo|Idea original del producto]]
- [[Bily/MEMORIA|MEMORIA de Bily — reglas operativas]]
- [[Claude/Whisper|Stack whisper local reusable]]
- [[Claude/Vault-Wrappers|Patrón vault-wrappers]]
