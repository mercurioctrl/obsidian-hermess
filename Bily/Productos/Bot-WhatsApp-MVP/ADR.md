# Architecture Decision Record (ADR) — Bily

**Status:** v0.1 — draft inicial, iterando con Catriel · Claude (Opus 4.7).
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

🟡 **Propuesta: TypeScript / Node 22 LTS** para todo el agent-core y servicios HTTP.

**Rationale:**
- Tu proyecto existente de WhatsApp ya está en Node (`whatsapp-web.js` + puppeteer)
- Vercel AI SDK (TypeScript) es el mejor del mercado para LLM routing
- Async/event-loop excelente para multi-agente
- Tipado strict da seguridad para team de 4 devs
- Ecosistema npm rico

🔴 **[DECISIÓN ABIERTA-001] Lenguaje principal:**
- A) TypeScript/Node (propuesta) — reuso máximo de tu código, ecosistema fuerte
- B) Python — si tu equipo es más fuerte ahí; LiteLLM es alternativa decente a Vercel AI SDK
- C) Híbrido — TS para agent runtime + channels, Python para data/analytics (más complejo de mantener)

**Exception scripts:** Python para data ops one-shot (ETL, análisis) y para el whisper sidecar (ya existe).

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

### 4.3. 🔴 [DECISIÓN ABIERTA-002] DB para metadata

Necesitamos guardar: agentes (id, name, phoneE164, ownerId, vaultPath, status, createdAt, ...), users, billing, sessions, cron jobs, etc.

Opciones:

| Opción | Pros | Contras |
|---|---|---|
| **A. PostgreSQL global** (1 DB para todo) | Fácil queries cross-agente (admin, billing, analytics). Backups centralizados. Tooling rico (Prisma, Drizzle) | SPOF — si la DB cae, todos los agentes caen. Más complejo backup-per-tenant |
| **B. SQLite per-agente** + Postgres global solo para users/billing | Isolation perfecta (cada agente es self-contained). Backups simples (es 1 archivo). Failure isolation | Queries cross-agente más complejas (need aggregation). Menos tooling |
| **C. Postgres + tenant_id en todas las tablas** | Lo mejor de A pero con row-level security | Más cuidado en queries (always filter by tenant). Performance OK hasta ~1000 agents |

🟡 **Recomendación: B (SQLite-per-agente + Postgres central)** para MVP. Razones:
- Isolation se alinea con el resto de la arquitectura (1 process por agente)
- Backup del cerebro es 1 archivo `.sqlite` por agente, simple
- Postgres solo para users + billing + cross-agent aggregates
- Si crece, migrar a Postgres puro es factible

### 4.4. 🔴 [DECISIÓN ABIERTA-003] Auth para users

| Opción | Pros | Contras |
|---|---|---|
| **A. Custom JWT** | Total control, sin dependencia externa, mínimo costo | Hay que hacer todo: signup, password reset, sessions, 2FA, etc. |
| **B. Clerk** | Drop-in, UI ready, 2FA, social login. Free hasta 10k users | $25/mes después de 10k. Dependencia externa |
| **C. Auth0** | Madurísimo, enterprise-ready | Caro, más complejo de configurar |
| **D. Supabase Auth** | Free generoso, viene con DB Postgres si la usás | Acopla auth con DB; menos control |

🟡 **Recomendación: A (Custom JWT)** para MVP por simpleza + control + cero costo. Migrar a Clerk si el setup de auth se vuelve cuello de botella. Considerar B si el Jr no tiene experiencia haciendo auth seguro (es fácil cometer errores).

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

### 8.1. 🔴 [DECISIÓN ABIERTA-004] Dónde corren los servers

| Opción | Pros | Contras | Costo ~50 agentes |
|---|---|---|---|
| **A. Hetzner dedicated servers** (Alemania) | Mejor $/RAM del mundo. Servers físicos potentes ($50-150/mes) | Latencia 200-300ms desde Arg (impacta LLM round trips). EU jurisdiction |
| **B. AWS/DigitalOcean EE.UU.** | Cloud estándar, multi-AZ, ecosistema | Más caro. Latencia ~80-150ms desde Arg |
| **C. On-prem en tu oficina/casa** | Control total, latencia mínima, sin renta mensual | Power/Internet UPS-dependent. Phone farm necesita lugar físico igual |
| **D. Hybrid: phone farm + brain on-prem, agent-runtimes en cloud** | Lo mejor de ambos | Más complejo de mantener |

🟡 **Recomendación:** **C (on-prem)** para MVP por **2 razones específicas a tu setup:**
1. La phone farm necesita lugar físico de todos modos
2. Vos ya tenés un servidor donde corre OpenClaw + Bily — ese es el embrión de la infra

Post-MVP cuando llegue el costo de uptime físico (UPS, internet redundante, AC), migrar lo que no es phone farm a cloud.

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

## 9. Decisiones abiertas — necesitan input antes de cerrar v1.0

- 🔴 **ADR-001:** Lenguaje (TS propuesto)
- 🔴 **ADR-002:** DB metadata (SQLite-per-agent + Postgres central propuesto)
- 🔴 **ADR-003:** Auth (Custom JWT propuesto)
- 🔴 **ADR-004:** Deploy infra (on-prem propuesto)
- ⚪ **ADR-005:** ¿Ollama dónde corre? mismo server o dedicado? Define hardware necesario
- ⚪ **ADR-006:** ¿Cron jobs con node-cron simple o bullmq+Redis? (más robusto pero +1 dep)
- ⚪ **ADR-007:** ¿Monitoring stack: Prometheus+Grafana auto-managed o servicio (Datadog/New Relic)?
- ⚪ **ADR-008:** ¿Object storage para backups: S3/B2/R2/Hetzner Storage?

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
