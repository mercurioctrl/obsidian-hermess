# Bot-WhatsApp-MVP — Carpeta del producto

**Status:** spec cerrada (v1.0), briefs listos, pendiente arrancar arquitectura.
**Última actualización:** 2026-05-24

---

## Documentos en esta carpeta

| Doc | Status | Audiencia |
|---|---|---|
| [[Bot-WhatsApp-MVP/Spec\|Spec MVP v1.0]] | ✅ Cerrada | Todo el equipo, fuente de verdad |
| [[Bot-WhatsApp-MVP/Brief-Diseno\|Brief Diseño]] | ✅ Listo | Equipo de diseño — pueden arrancar |
| [[Bot-WhatsApp-MVP/Brief-Marketing\|Brief Marketing]] | ✅ Listo | Equipo de marketing — pueden arrancar |
| [[Bot-WhatsApp-MVP/ADR\|Architecture Decision Record]] | ⏳ Pendiente | Equipo técnico — bloqueado hasta que se escriba |
| [[Bot-WhatsApp-MVP/Brief-Devs\|Brief técnico para devs]] | ⏳ Pendiente | Equipo técnico — depende del ADR |

---

## Resumen ejecutivo del producto

**One-liner:** Asistente IA premium con nombre, cara y memoria propia que vive en su propio WhatsApp y aprende tu vida.

**Pricing:** $59 USD/mes (~66k ARS), single tier, trial 14 días sin tarjeta.

**Target:** profesionales individuales + dueños PyME en Argentina (LATAM en fase 2).

**Costo operativo equipo:** $18,000/mes fijo.

**Break-even:** ~440 paying users (estimado mes 6-7 post-launch).

**Runway necesario:** $40-50k USD para cubrir gap mes 0-7.

**Cronograma:** 8-10 semanas a beta cobrable + 1-2 meses de bugs/iteración = launch público mes 3-4 post-arranque dev.

**Equipo:** 3 srs dev + 1 jr + 1 QA + diseño + marketing + Catriel como PM (50-100% tiempo).

---

## Decisiones clave ya tomadas

1. **Stack técnico:** custom thin orchestrator (NO OpenClaw/Hermes), TypeScript/Node, markdown REST API propio (NO Obsidian)
2. **WhatsApp:** phone farm con Androids viejos + whatsapp-web.js
3. **Browser tool:** puppeteer compartido con WA Web
4. **LLM:** router multi-provider con fallback (Claude/Gemini/OpenAI + Ollama local)
5. **Cerebro:** markdown files + REST API custom + wikilink-weaver + person-profiler
6. **Identidad agente:** nombre random B-* inmutable + avatar único (API ya existente)
7. **Geo MVP:** Argentina + español rioplatense
8. **Diferenciador:** "no es ChatGPT, es un asistente con identidad propia y memoria irreemplazable"

---

## Próximos pasos inmediatos

| Paso | Owner | ETA |
|---|---|---|
| Briefs a diseño y marketing → ellos arrancan | Catriel | Hoy |
| Catriel resuelve preguntas pendientes de briefs | Catriel | Esta semana |
| Escribir ADR (arquitectura) | Catriel + Sr1 (tech lead) + Claude | Próxima semana |
| Brief técnico para devs + sprint plan | Sr1 (tech lead) | Después del ADR |
| Kickoff con equipo completo | Catriel | Semana 0 del dev |

---

## Relacionado (otros productos / docs)

- [[Bily/Productos/Billy-Bot|Arquitectura Billy Bot original (referencia)]]
- [[Bily/Productos/Bot-WhatsApp-Nativo|Idea original del producto]]
- [[Claude/Whisper|Stack whisper local (componente reusable)]]
- [[Claude/Vault-Wrappers|Patrón vault-wrappers (lección aprendida)]]
