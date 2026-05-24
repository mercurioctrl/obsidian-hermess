# Architecture Decision Record (ADR) — Bily

**Status:** v1.0 — 4 decisiones críticas cerradas con Catriel · Claude (Opus 4.7).
**Última actualización:** 2026-05-24
**Doc relacionado:** [[Bily/Productos/Bot-WhatsApp-MVP/Spec|Spec MVP v1.0]]

> Documento técnico vivo. **🔴 [DECISIÓN ABIERTA]** = necesita input de Catriel/tech lead. **🟡 [PROPUESTA]** = sugerencia con rationale, confirmar. **🟢** = decidido y aceptado.

---

## 1. Contexto técnico

Bily es un **asistente IA multi-tenant** donde cada usuario tiene su propio agente independiente con:
- Identidad propia (nombre random + avatar minteado + personalidad randomizada)
- Su propio número de WhatsApp (chip físico en Android dedicado)
- Cerebro persistente en markdown
- Toolkit para acción (web browse, whisper, brain ops, mail/cal futuro)

Multi-tenancy a escala objetivo: **30-50 agentes simultáneos por servidor**, target 1000+ agentes totales mes 12.

Equipo: 3 srs dev + 1 jr + 1 QA + diseño + marketing + Catriel como PM.

Cronograma: 8-10 semanas a MVP cobrable + 1-2 meses iteración → launch público mes 3-4.

---

## 2. Diagrama de arquitectura (alto nivel)

```
                            ┌─────────────────────────────────────┐
                            │   USUARIOS (WhatsApp)               │
                            └─────────────┬───────────────────────┘
                                          │
                            ┌─────────────▼───────────────────────┐
                            │ PHONE FARM (Androids con SIM)       │
                            │ 50+ phones × 1 chip × 1 WA account  │
                            └─────────────┬───────────────────────┘
                                          │ (WA Web pairing)
                            ┌─────────────▼───────────────────────┐
                            │ SERVERS (per-agent runtimes)         │
                            │                                       │
                            │  ┌──────────────────────────────┐    │
                            │  │ Agent #N (systemd unit)      │    │
                            │  │  ├ puppeteer browser         │    │
                            │  │  │  ├ tab: WA Web (pinned)   │    │
                            │  │  │  └ tabs: browse toolkit   │    │
                            │  │  ├ agent loop (TS/Node)      │    │
                            │  │  ├ LLM router                │    │
                            │  │  ├ Tool registry             │    │
                            │  │  └ Plugins (whisper, etc)    │    │
                            │  └──────────────────────────────┘    │
                            │  ... × N agents ...                  │
                            └─────────────┬───────────────────────┘
                                          │
                ┌─────────────────────────┴─────────────────────────┐
                │                                                     │
        ┌───────▼────────┐  ┌───────────────┐  ┌──────────────┐  ┌──▼──────────┐
        │ BRAIN REST API │  │ WHISPER STACK │  │ LLM ROUTER   │  │ OLLAMA      │
        │ (markdown +    │  │ (server :9000 │  │ (Vercel AI   │  │ (last resort│
        │  SQLite FTS5)  │  │ + sidecar     │  │ SDK + custom │  │ fallback)   │
        │                │  │ :9001)        │  │ fallback)    │  │             │
        └────┬───────────┘  └───────────────┘  └──────┬───────┘  └─────────────┘
             │                                          │
             │                                          ├──→ Anthropic
             │                                          ├──→ Google
             │                                          ├──→ OpenAI
             │                                          └──→ Ollama (fallback)
             │
        ┌────▼───────────┐
        │ BACKUP         │
        │ ORCHESTRATOR   │  → S3/B2/R2
        └────────────────┘

        ┌────────────────────────────────────────────────────────┐
        │ SHARED SERVICES                                          │
        │  ┌────────────┐  ┌──────────────┐  ┌────────────────┐  │
        │  │ MINT API   │  │ ADMIN PANEL  │  │ BILLING        │  │
        │  │ (avatar +  │  │ (Catriel +   │  │ (MercadoPago)  │  │
        │  │  name)     │  │  ops team)   │  │                │  │
        │  └────────────┘  └──────────────┘  └────────────────┘  │
        │  ┌────────────┐  ┌──────────────┐  ┌────────────────┐  │
        │  │ AUTH       │  │ COST TRACKER │  │ MONITORING     │  │
        │  │ (users)    │  │ (LLM tokens) │  │ (logs+metrics) │  │
        │  └────────────┘  └──────────────┘  └────────────────┘  │
        └────────────────────────────────────────────────────────┘
```

---

## 3. Componentes principales

| # | Componente | Responsabilidad | Tipo | Owner sugerido |
|---|---|---|---|---|
| 1 | **Agent Core** | Agent loop (poll → context → LLM → tools → respond), per-agent runtime | Library + per-agent process | Sr 1 (tech lead) |
| 2 | **LLM Router** | Multi-provider con fallback, circuit breaker, cost tracking | Library compartida | Sr 1 |
| 3 | **Brain REST API** | Markdown vault server con search FTS5, backlinks, snapshots | Servicio HTTP shared multi-tenant | Sr 2 |
| 4 | **Intelligence Plugins** | wikilink-weaver, person-profiler, pattern-detector (cron jobs) | Plugins del Agent Core | Sr 2 |
| 5 | **Channels & Tools** | WhatsApp channel (whatsapp-web.js), puppeteer pool, browse toolkit | Plugins del Agent Core | Sr 3 |
| 6 | **Infra/Orchestration** | Agent spawner, chip allocator, minteo bot, deploy, monitoring | Servicios + scripts | Sr 3 + Jr |
| 7 | **Admin Panel + Auth** | User accounts, billing, agent management UI | Web app | Jr (con Sr 1 supervisando) |
| 8 | **Mint API** (externa) | Generación de nombre + avatar | Servicio externo (Catriel ya tiene) | N/A |
| 9 | **Whisper Stack** (existente) | Transcripción local de audios | Servicio compartido | Reusado de lo construido 2026-05-23 |

---

## 4. Stack tecnológico

### 4.1. Lenguajes y runtimes

🟢 **DECISIÓN: Híbrido TypeScript + Python** según fortalezas de cada lenguaje y del equipo.

**Rationale:** El equipo es más fuerte en Python, pero hay piezas donde Node/TS son la elección natural por ecosystem (WA, puppeteer, Vercel AI SDK). En vez de forzar todo a un lado, dividimos por afinidad.

### 4.1.1. Split TS / Python

**TypeScript / Node 22 LTS** — donde es obligatorio o claramente mejor:

| Componente | Por qué TS |
|---|---|
| **Agent runtime** (per-agent process) | Maneja puppeteer + WA channel directamente |
| **WA channel** (whatsapp-web.js) | Único lugar donde WA Web funciona bien |
| **Puppeteer pool + browse toolkit** | Mejor soporte y maturity en Node |
| **LLM Router** (Vercel AI SDK) | El SDK es TS-native; LiteLLM en Python es decente pero no superior |
| **Admin Panel** (Next.js) | React ecosystem |
| **Mint bot público** | Mismo runtime que agentes |

**Python 3.12** — donde el equipo brilla y es naturalmente mejor:

| Componente | Por qué Python |
|---|---|
| **Brain REST API** | FastAPI + SQLite es excelente; equipo es fuerte acá |
| **Intelligence plugins** (wikilink-weaver, person-profiler, pattern-detector) | NLP/text analysis es zona fuerte de Python; pandas/scipy disponibles |
| **Whisper sidecar** (ya existe) | Re-uso 100% |
| **Cost tracker + analytics** | Pandas + SQL para crunchear datos |
| **Cron jobs / batch jobs** | Equipo lo va a hacer mejor en Python |
| **ETL / data ops** | Natural |

### 4.1.2. Comunicación entre TS y Python

- **HTTP REST** (principal): Agent TS → Brain Python via HTTP. Wrappers tipo `brain_*` lo encapsulan.
- **Message queue** (cuando aplique): Redis Pub/Sub o BullMQ para trigger de cron jobs desde el agente.
- **Shared types**: definir schemas con JSON Schema o Protobuf, generar TS types y Pydantic models desde la misma fuente.

### 4.1.3. Consecuencias del híbrido

- **(+)** El equipo trabaja en lo que sabe → menos errores, más velocidad
- **(+)** Componente correcto a cada lenguaje (no force-fits)
- **(+)** Reuso del whisper sidecar (Python) y proyectos existentes WA (Node)
- **(−)** 2 stacks para mantener → 2 setups de dev, 2 lints, 2 CI pipelines
- **(−)** Refactoring cross-stack es más laburo (cambio de schema afecta TS + Python)
- **(−)** Onboarding más caro (devs necesitan poder leer ambos)

**Mitigación:** turbo monorepo soporta workspaces multi-language. CI puede correr ambos en paralelo. Shared types generados desde una source of truth.

### 4.2. Frameworks y librerías clave

| Capa | Librería | Por qué |
|---|---|---|
| HTTP server | **Fastify** | Rápido, schema validation built-in, OpenAPI nativo. Alternativa: Express si el equipo lo prefiere |
| LLM SDK | **Vercel AI SDK** (`ai` package) | Provider abstraction multi-vendor, tool use, streaming, fácil agregar Ollama |
| WhatsApp | **whatsapp-web.js** | Ya conocido por el equipo, mantiene auth, soporta media, groups |
| Browser/scrape | **puppeteer** | Ya conocido, control fino, mismo browser que WA |
| DB metadata | 🔴 **[DECISIÓN ABIERTA-002]** ver 4.3 | |
| Search markdown | **better-sqlite3 + FTS5** | Embedded, rápido, sin server extra |
| Validation | **zod** | Schemas + TS types en un mismo lugar |
| Auth | 🔴 **[DECISIÓN ABIERTA-003]** ver 4.4 | |
| Logging | **pino** | Rápido, JSON estructurado, child loggers per-agent |
| Metrics | **prom-client** + Grafana | Estándar, fácil scraping |
| Tests | **vitest** + **playwright** | Vitest para unit, playwright para E2E (reusa puppeteer expertise) |
| Frontend admin | **Next.js 15** + Tailwind + shadcn/ui | Productivo, server components, ecosistema |
| Cron | **node-cron** o **bullmq** (Redis-backed) | Para wikilink-weaver, person-profiler, backup |

### 4.3. DB para metadata

🟢 **DECISIÓN: SQLite-per-agente + PostgreSQL central**

- **SQLite por agente** (`~/agents/<agentId>/data.sqlite`): brain index FTS5, conversation history, agent-local state, cron job state local. Cada agente totalmente self-contained.
- **Postgres central** (managed o on-prem): users, billing, agent registry (qué agentes existen, status), chip pool, marketing funnel data, audit logs.

**Stack:**
- **TS:** Drizzle ORM para Postgres (typed, lightweight)
- **Python:** SQLAlchemy 2.0 async para Postgres + better-sqlite3 bindings (o `sqlite3` stdlib)
- Migrations: Drizzle migrations + Alembic (Python) — coordinadas

**Backup:**
- SQLite-per-agente: snapshot file completo a object storage cada hora
- Postgres: pg_dump diario + WAL archiving

### 4.4. Auth para users

🟢 **DECISIÓN: Custom JWT** (con buenas prácticas).

**Stack:**
- bcrypt para password hashing (cost factor 12+)
- JWT con HS256 o RS256, expiración 15 min + refresh tokens 30 días
- Refresh tokens en DB para revocar
- Rate limiting en endpoints de auth
- 2FA opcional vía TOTP (post-MVP)
- Password reset via email con token de un solo uso

**Quién lo codea:** Sr 1 lidera, Jr ayuda. **NO** dejar al Jr solo en auth (zonas de seguridad sensibles).

**Migration path:** si vemos que el setup nos cuesta más de 2 semanas o aparecen issues de seguridad, migrar a Clerk (es drop-in).

---

## 5. Contratos entre componentes (APIs internas)

### 5.1. Brain REST API

Base: `http://brain.bily.internal:8080` (interno, no expuesto a internet)

```
GET    /v1/agents/:agentId/vault/<path>           → markdown content o folder JSON
PUT    /v1/agents/:agentId/vault/<path>           → write (content-type por ext)
DELETE /v1/agents/:agentId/vault/<path>           → delete
PATCH  /v1/agents/:agentId/vault/<path>           → { append?: string, prepend?: string }
POST   /v1/agents/:agentId/search?q=X             → FTS5 search → JSON results
GET    /v1/agents/:agentId/backlinks/<path>       → backlinks listed
GET    /v1/agents/:agentId/graph                  → wikilink graph
POST   /v1/agents/:agentId/wikilinks/resolve      → trigger weaver job
POST   /v1/agents/:agentId/snapshot               → create snapshot, return id
POST   /v1/agents/:agentId/restore                → from snapshot id
POST   /v1/agents/:agentId/export                 → zip download
```

### 5.2. Agent Core (interno per-process)

```
POST /internal/inbound      → message arrived from WA, trigger agent turn
GET  /internal/status        → agent health check
POST /internal/tools/:name   → execute specific tool (for debugging)
GET  /internal/metrics       → prometheus format
```

### 5.3. LLM Router (in-process library)

```ts
const router = new LLMRouter(chainsConfig, costTracker, logger);
const result = await router.invoke({
  task: 'conversation' | 'routing' | 'background_analysis' | 'vision' | ...,
  messages: Message[],
  tools?: Tool[],
  agentId: string,  // for cost tracking
  maxTokens?: number,
});
```

### 5.4. Channels (Plugin API)

```ts
interface Channel {
  id: string;                                     // 'whatsapp', 'telegram', etc.
  start(agentId: string, config: any): Promise<void>;
  stop(): Promise<void>;
  on(event: 'inbound', handler: (msg: InboundMessage) => void): void;
  send(target: ChannelTarget, payload: OutboundPayload): Promise<SendResult>;
}
```

### 5.5. Tools (Plugin API)

```ts
interface Tool {
  name: string;                                   // 'brain_get', 'browse', etc.
  description: string;                             // for LLM tool selection
  parameters: ZodSchema;                           // JSON Schema for LLM
  execute(args: any, ctx: ToolContext): Promise<ToolResult>;
}
```

### 5.6. Admin Panel API

```
GET    /api/admin/agents              → list with filters
GET    /api/admin/agents/:id          → detail
POST   /api/admin/agents/:id/restart  → restart agent runtime
GET    /api/admin/chips               → pool status
GET    /api/admin/metrics             → MRR, churn, cost-to-serve
POST   /api/admin/agents/:id/freeze   → freeze (when user stops paying)
POST   /api/admin/agents/:id/delete   → after 90-day freeze
```

---

## 6. ADRs individuales (decisiones documentadas)

### ADR-001: NO usar framework de agente (custom thin orchestrator)

**Status:** Accepted

**Context:** Considerados OpenClaw (lo probamos), Hermes (Nous Research), LangGraph, Letta/MemGPT, CrewAI. Todos diseñados para single-user. Multi-tenancy a nuestra escala es problema nuestro independiente del framework.

**Decision:** Construir un orchestrator thin custom (~300-800 LOC) que llama directamente a Vercel AI SDK. Sin abstracciones pesadas.

**Consequences:**
- **(+)** Control total sobre agent loop, multi-tenancy, plugin system
- **(+)** No framework constraints en memoria/brain (markdown propio)
- **(+)** Sin sangre técnica acumulada por pelearse al framework
- **(−)** Más código inicial (1-2 semanas extra de boilerplate)
- **(−)** Menos features "gratis" (channels, tools comunes hay que adaptarlos)

### ADR-002: Markdown REST API custom (NO Obsidian)

**Status:** Accepted

**Context:** El brain es el moat del producto. Obsidian (la app) no escala multi-tenant. Usar Obsidian's Local REST API plugin requiere 1 instancia GUI por agente.

**Decision:** Construir servicio HTTP propio que sirve markdown files + SQLite FTS5 para search + graph indexing. Compatible con clientes Obsidian para que usuarios power abran su cerebro en su Obsidian local.

**Consequences:**
- **(+)** Escalable multi-tenant nativamente
- **(+)** Control total sobre features (backlinks, graph, snapshots, export)
- **(+)** Usuarios pueden seguir abriendo su brain en Obsidian si quieren (es solo .md)
- **(−)** Hay que codear las features de Obsidian que vamos a aprovechar
- **(−)** SLA del servicio recae 100% en nosotros

### ADR-003: WhatsApp Web (whatsapp-web.js) + phone farm

**Status:** Accepted

**Context:** Alternativas: WA Cloud API (oficial Meta, $$$, requiere business verification), Baileys (no oficial pero reverse-engineered, ban-risk), whatsapp-web.js + chips reales (lo que tiene Catriel).

**Decision:** Usar whatsapp-web.js + phone farm de Androids viejos con chips reales en MVP. Reusar tu proyecto existente.

**Consequences:**
- **(+)** Costo bajo ($5/mes/chip vs $0.10/sesión Cloud API)
- **(+)** Compatible con groups, audios, media
- **(+)** Reuso de tu código existente
- **(−)** Cuello de botella físico: 1 phone por agente
- **(−)** Riesgo ban si Meta detecta patrones automation
- **(−)** Mantenimiento: charging, reboots, manual fixes

### ADR-004: Puppeteer compartido WA + browse

**Status:** Accepted

**Context:** Cada agente necesita browse tool (para tools de scraping/research). Tener 2 chrome (uno WA, otro browse) duplica RAM (~600 MB extra/agente).

**Decision:** 1 puppeteer/chrome por agente, con WA Web tab pinned + tabs efímeras para browse.

**Consequences:**
- **(+)** Ahorra ~300-400 MB RAM por agente (×100 agentes = 30-40 GB ahorro)
- **(+)** Cookies/auth compartido entre WA y browse (útil para algunos casos)
- **(−)** Riesgo de "matar" WA si por error se navega la tab pinned. **Mitigación: wrapper `browse(url)` que SIEMPRE abre tab nueva, NUNCA expone control directo a LLM**

### ADR-005: LLM Router multi-provider con Vercel AI SDK + Ollama fallback

**Status:** Accepted

**Context:** Necesitamos: modelos diferentes para tareas diferentes, fallback resiliente, control de costo. Catriel quiere Ollama como last resort.

**Decision:** Vercel AI SDK como base. Encima nuestro `LLMRouter` con: task taxonomy (conversation/routing/background_analysis/vision/embedding), per-task fallback chain, circuit breaker, cost tracking per agente.

**Cadena estándar:**
```yaml
conversation: [anthropic/claude-sonnet-4-6, google/gemini-2.5-pro, openai/gpt-4.1, ollama/llama3.1:8b]
routing:      [anthropic/claude-haiku-4-5, google/gemini-2.5-flash, openai/gpt-4o-mini, ollama/llama3.2:3b]
# ... ver spec sección dedicada
```

**Consequences:**
- **(+)** Resiliencia: nunca down total (Ollama siempre disponible)
- **(+)** Cost optimization: tarea barata → modelo barato
- **(+)** Provider-agnostic: si Anthropic sube precios, swap fácil
- **(−)** Complejidad: hay que mantener la chain config, monitorear fallback rate

### ADR-006: Per-agent process via systemd templates (MVP), K8s después

**Status:** Accepted (MVP), Reviewable (post-MVP)

**Context:** Multi-tenancy options: per-agent VM, shared runtime multi-tenant, K8s pods scale-to-zero.

**Decision MVP:** systemd unit template `bily-agent@<agentId>.service`. 1 unit por agente. Simple, debuggeable, fácil de monitorear.

**Decision Post-MVP (~mes 6+):** migrar a containers (Docker compose o K8s) con scale-to-zero cuando el costo de RAM idle dueles.

**Consequences:**
- **(+)** Setup simple inicial, deploy = `systemctl enable bily-agent@X`
- **(+)** Logs unificados via journald
- **(+)** Restart/health checks built-in en systemd
- **(−)** No scale-to-zero (todos los agentes consumen RAM aunque estén idle)
- **(−)** Migración a K8s es laburo cuando llegue el momento

### ADR-007: Vault wrappers como única interfaz al brain desde el agente

**Status:** Accepted

**Context:** Aprendimos en testing con deepseek que LLMs flojos alucinan URLs. La solución fue armar wrappers `vault-*` que encapsulan URL/token/flags.

**Decision:** El Agent Core expone tools `brain_get`, `brain_put`, `brain_search`, `brain_ls`, `brain_delete` al LLM. Internamente llaman al Brain REST API. **EL LLM JAMÁS escribe HTTP requests directos.**

**Consequences:**
- **(+)** Imposible alucinar URLs / formatos
- **(+)** Testeable (mock fácil)
- **(+)** Audit trail (cada llamada al brain queda registrada)

### ADR-008: Monorepo con pnpm workspaces + turbo

**Status:** Proposed (confirmar con tech lead)

**Context:** Para team de 4 devs con muchos packages relacionados (agent-core, brain-rest, admin, channels, tools), monorepo simplifica refactoring + CI/CD.

**Decision:** **pnpm workspaces** para package management + **turbo** para build/test orchestration. Estructura:

```
bily/
├── apps/
│   ├── agent-runtime/      ← per-agent process
│   ├── brain-rest/          ← markdown server
│   ├── mint-bot/            ← public minteo bot
│   ├── admin-panel/         ← Next.js
│   └── ops-cli/             ← admin scripts
├── packages/
│   ├── agent-core/          ← agent loop library
│   ├── llm-router/          ← LLM abstraction
│   ├── channels/            ← WA, future Telegram, etc.
│   ├── tools/               ← brain, browse, whisper, etc.
│   ├── plugins/             ← wikilink-weaver, person-profiler, etc.
│   ├── shared-types/        ← TS types compartidos
│   └── shared-utils/        ← helpers
├── infra/
│   ├── systemd-templates/
│   ├── docker/              ← post-MVP
│   ├── ansible/             ← provisioning scripts
│   └── terraform/           ← post-MVP infra as code
└── docs/
```

**Consequences:**
- **(+)** Atomic commits across packages
- **(+)** Refactoring fácil
- **(+)** CI build incremental con turbo
- **(−)** Onboarding nuevos devs es un poquito más complejo

---

## 7. Cross-cutting concerns

### 7.1. Security

- **Secrets:** vía `.env` local + Doppler/1Password Connect para producción. NUNCA en git.
- **Per-tenant isolation:** cada agent-runtime corre como user systemd diferente (o namespace separado). DB queries siempre filtradas por agentId.
- **API auth:** internal APIs (brain, agent-core) escuchan solo en loopback o private network. Admin API con JWT.
- **WhatsApp:** auth state per-agente, encriptado at-rest.
- **LLM keys:** rotadas trimestralmente, monitoreado uso anómalo.

### 7.2. Logging

- **Structured JSON via pino** en todos los servicios.
- **agentId siempre presente** en logs de runtimes per-agent.
- **Centralized:** logs van a journald + agregados a Loki (o similar) para search.
- **Retention:** 30 días hot, 1 año cold.

### 7.3. Métricas

- **Prometheus** scraping de cada agente + servicios shared.
- **Grafana** dashboards: per-agent health, LLM cost, message volume, latency.
- **Alertas:** PagerDuty / Telegram bot a operador cuando un agente muere > 15 min, costos diarios > threshold, error rate > 5%.

### 7.4. Backup

- **Snapshot brain de cada agente cada hora** → S3/B2/R2 con encryption at-rest.
- **Retention:** 30 daily + 12 monthly + 5 yearly.
- **Test restore semanal automatizado** sobre 1 agente al azar.

### 7.5. Cost tracking

- Cada llamada LLM registra: agentId, provider, model, input tokens, output tokens, cost.
- Aggregation diaria por agente. Alertas si supera budget.
- Forzar downgrade automático (chain switches a Ollama) si cost > $1/día/agent.

---

## 8. Deploy y operations

### 8.1. Dónde corren los servers

🟢 **DECISIÓN: On-prem en el lugar de Catriel** (MVP).

**Rationale:**
- La phone farm necesita lugar físico de todos modos
- El servidor actual de Catriel (donde corre Bily/OpenClaw) es el embrión de la infra prod
- Cero renta mensual de cloud durante el período de runway crítico
- Latencia mínima entre agentes y phone farm (mismo LAN)

**Hardware mínimo recomendado:**
- Server principal: 32 GB RAM, Xeon o i7/Ryzen 7+, SSD NVMe ≥1 TB, Ubuntu 24.04 LTS
- Estante phone farm: 50 Androids + power + USB hub + WiFi dedicado
- UPS para server (mínimo 30 min aguante)
- Internet redundante (fibra + 4G backup)

**Servicios externos (cloud, no on-prem):**
- Object storage para backups (Backblaze B2 o Cloudflare R2 — más baratos que S3)
- LLM providers (Anthropic, Google, OpenAI APIs)
- DNS y CDN para landing (Cloudflare free)
- MercadoPago para billing (API)
- Email transaccional (Postmark / Resend)

**Post-MVP migration plan (mes 6+):**
- Si el costo de uptime físico (UPS, internet, AC) supera $500/mes, migrar agent-runtimes a Hetzner dedicated (mejor $/RAM del mundo)
- Phone farm SIEMPRE on-prem (no se puede mover)
- Brain REST API podría migrar a cloud cerca de los agentes

### 8.2. CI/CD

- **GitHub Actions** o **GitLab CI** según preferencia del equipo.
- Pipeline:
  1. Lint + typecheck en cada PR
  2. Unit tests (vitest) + integration tests
  3. E2E tests (playwright sobre staging)
  4. Build packages con turbo
  5. Deploy a staging automático en merge a `main`
  6. Deploy a prod con tag manual `v*`

### 8.3. Environments

- **dev:** local (cada dev tiene su setup con `docker compose` para deps)
- **staging:** 1 server espejo, datos mockeados, 2-3 agentes de prueba
- **prod:** la cosa real, 30-50+ agentes

---

## 9. Estado de decisiones

**Cerradas en v1.0:**
- [x] **ADR-001:** Lenguaje → **Híbrido TypeScript + Python** (ver 4.1)
- [x] **ADR-002:** DB → **SQLite-per-agente + Postgres central**
- [x] **ADR-003:** Auth → **Custom JWT** (Sr1 lidera, Jr asiste)
- [x] **ADR-004:** Deploy → **On-prem** en lugar de Catriel (MVP) + object storage cloud para backups

**Decisiones secundarias (se pueden cerrar con tech lead, no bloquean dev):**
- [ ] **ADR-005:** Ollama dónde corre — mismo server o GPU dedicada. **Propuesta:** mismo server con modelo small (llama3.2:3b ~2GB) en MVP. GPU dedicada post-MVP cuando crezca uso de fallback.
- [ ] **ADR-006:** Cron jobs — **Propuesta:** `node-cron` para TS, `APScheduler` para Python. BullMQ+Redis solo cuando haga falta queue distribuida (post-MVP).
- [ ] **ADR-007:** Monitoring — **Propuesta:** Prometheus + Grafana self-hosted en el mismo server. Grafana Cloud free tier si necesitamos accesos externos.
- [ ] **ADR-008:** Object storage para backups — **Propuesta:** Backblaze B2 (cheaper que S3) o Cloudflare R2 (zero egress fees). B2 si simpleza, R2 si vamos a leer mucho desde el agente.

---

## 10. Próximos artefactos

1. **Brief técnico para devs** (después de cerrar ADRs abiertas) — onboarding al stack, división de packages, sprint plan stage 1
2. **Diagrama de arquitectura visual** (no ASCII, sino real) — Excalidraw/Figma
3. **Schemas formal de APIs** (OpenAPI specs para Brain REST + Admin)
4. **Threat model + security review**

---

## Relacionado

- [[Bily/Productos/Bot-WhatsApp-MVP/Spec|Spec MVP]]
- [[Bily/Productos/Bot-WhatsApp-MVP/Brief-Diseno|Brief Diseño]]
- [[Bily/Productos/Bot-WhatsApp-MVP/Brief-Marketing|Brief Marketing]]
- [[Claude/Whisper|Stack whisper local reusable]]
- [[Claude/Vault-Wrappers|Patrón vault-wrappers como precedente del approach brain-tools]]
