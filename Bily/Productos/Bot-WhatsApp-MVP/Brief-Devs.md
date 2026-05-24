# Brief Técnico — Equipo Dev de Bily (Stage 1 sprint plan)

**Para:** 3 Sr devs + 1 Jr dev + 1 QA · **De:** Catriel + Claude · **Fecha:** 2026-05-24

**Docs requeridos** (lectura antes de arrancar):
1. [[Bily/Productos/Bot-WhatsApp-MVP/Spec|Spec MVP v1.0+]] — qué es el producto
2. [[Bily/Productos/Bot-WhatsApp-MVP/ADR|Architecture Decision Record v1.0]] — cómo se construye
3. Este doc — qué hacés vos esta semana

---

## 1. Contexto técnico en 1 minuto

Construimos **Bily**: un asistente IA multi-tenant donde cada usuario tiene su propio agente con su WhatsApp dedicado, cerebro markdown propio, y personalidad única. Pricing $59 USD/mes. Target: profesionales + PyME en Argentina.

**Stack consolidado:**
- **TypeScript/Node 22** para: agent runtime, WA channel, puppeteer + browse tool, LLM router, admin panel
- **Python 3.12** para: Brain REST API, intelligence plugins (wikilink-weaver, person-profiler, pattern-detector), whisper sidecar (ya existe), cost tracker, analytics
- **SQLite per-agent** + **PostgreSQL central** para metadata global
- **whatsapp-web.js** + phone farm de Androids para WA
- **Vercel AI SDK** + custom router con fallback a Ollama
- **On-prem** deployment (server actual de Catriel)
- **Custom JWT** auth
- **Monorepo** con pnpm workspaces + turbo

**Cronograma:** 8-10 semanas a MVP cobrable, 4 stages (single-tenant → multi-tenant → intelligence → ops+beta).

---

## 2. Equipo y responsabilidades

| Persona | Rol | Owner principal | Skills clave |
|---|---|---|---|
| **Sr 1** | Tech lead + Agent Core | TS: agent loop, LLM router, tool framework, auth | TS senior, LLM APIs, async patterns, decisions arquitecturales |
| **Sr 2** | Brain + Intelligence | Python: Brain REST API, wikilink-weaver, person-profiler, pattern-detector, backup orchestrator | Python senior, FastAPI, SQLite FTS5, prompt engineering |
| **Sr 3** | Channels + Tools + Infra | TS: WhatsApp channel, puppeteer pool, browse toolkit · Bash/Python: deploy scripts, systemd templates, monitoring | Node + puppeteer + linux sysadmin |
| **Jr** | Soporte transversal | Admin panel CRUD (Next.js), scripts deploy/bootstrap, integration tests, dashboards monitoring · pair con Sr1 en auth, con Sr3 en infra | TS/React + ganas de aprender |
| **QA** | Calidad transversal | E2E test framework (playwright + vitest), test plans, regression suite, exploratory testing, verificación bugfixes | Testing strategy + ojo crítico |

**Definiciones de "owner":**
- Owner = responsable de que algo se entregue, no necesariamente el único que codea
- Pairing encouraged: Jr siempre tiene buddy Sr para tareas complejas
- Code reviews: TODO PR review obligatorio por al menos 1 sr antes de merge
- Tech lead (Sr 1) tiene veto en decisiones arquitecturales

---

## 3. Estructura del monorepo

```
bily/
├── apps/                           # Aplicaciones desplegables
│   ├── agent-runtime/              # TS — per-agent process (Sr 1 owner)
│   ├── brain-rest/                 # Python — markdown REST API (Sr 2 owner)
│   ├── mint-bot/                   # TS — bot público de minteo (Sr 3 owner)
│   ├── admin-panel/                # Next.js — panel admin (Jr owner)
│   └── intelligence-worker/        # Python — cron jobs (Sr 2 owner)
│
├── packages/                       # Librerías compartidas
│   ├── agent-core/                 # TS — agent loop library (Sr 1)
│   ├── llm-router/                 # TS — Vercel AI SDK + fallback (Sr 1)
│   ├── channels-whatsapp/          # TS — WA via whatsapp-web.js (Sr 3)
│   ├── tools-browse/               # TS — puppeteer browse toolkit (Sr 3)
│   ├── tools-brain-client/         # TS — client del Brain REST API (Sr 1 + Sr 2)
│   ├── tools-whisper-client/       # TS — client del whisper sidecar existente
│   ├── shared-types/               # TS + Python — types desde JSON Schema
│   ├── shared-utils-ts/            # TS — helpers genéricos
│   └── shared-utils-py/            # Python — helpers genéricos
│
├── infra/                          # Infra as code (Sr 3 + Jr)
│   ├── systemd-templates/          # bily-agent@.service, etc.
│   ├── ansible/                    # provisioning del server on-prem
│   ├── nginx/                      # reverse proxy configs
│   ├── monitoring/                 # Prometheus + Grafana configs
│   └── scripts/                    # bootstrap, backup, restore, etc.
│
├── tests/                          # E2E tests (QA owner)
│   ├── e2e-agent-flow/             # playwright — flujo completo agente
│   ├── e2e-minteo/                 # playwright — minteo público
│   └── load-tests/                 # K6 o artillery
│
├── docs/                           # Docs internas
│   ├── adr/                        # Architecture Decision Records (este doc + futuros)
│   ├── api/                        # OpenAPI specs
│   ├── runbooks/                   # incident response playbooks
│   └── onboarding/                 # este brief + setup local + FAQ
│
├── .github/workflows/              # CI/CD
├── package.json                    # root con pnpm workspaces
├── pnpm-workspace.yaml
├── turbo.json
├── pyproject.toml                  # Python workspace root
└── README.md
```

**Convenciones de naming:**
- TS apps/packages: kebab-case (`agent-runtime`, `tools-browse`)
- Python apps/packages: snake_case dentro de carpeta kebab-case
- Tests: mismo nombre que el package + `.test.ts` / `_test.py`

---

## 4. Setup local

### 4.1. Prerequisitos
- Node 22 LTS (via `fnm` o `nvm`)
- Python 3.12 (via `pyenv` o `uv`)
- pnpm 9+
- uv (Python package manager — más rápido que pip/poetry)
- Docker + Docker Compose (para Postgres + Redis locales)
- Git
- Editor: VSCode con extensiones recomendadas (lista en `.vscode/extensions.json`)

### 4.2. Bootstrap (10 min)
```bash
git clone git@github.com:blu-studio-inc/bily.git
cd bily
./scripts/bootstrap.sh   # instala deps TS + Python, levanta docker compose, corre migraciones
cp .env.example .env     # editar con credenciales locales
pnpm dev                 # arranca todos los servicios en watch
```

### 4.3. Servicios locales que levanta el bootstrap
- **Postgres** (`localhost:5432`, db `bily_dev`)
- **Redis** (`localhost:6379`, para queues/pub-sub)
- **Brain REST** (`localhost:8080`)
- **Agent runtime** (1 agente fake en `localhost:9080`)
- **Admin panel** (`localhost:3000`)
- **Whisper stack** (reuso del existente, `127.0.0.1:9000` + sidecar `:9001`)

### 4.4. Credenciales para dev local
- Anthropic API key (compartida en 1Password/Doppler del equipo)
- Google Gemini API key (idem)
- OpenAI API key (idem, optional)
- Sin WhatsApp real en dev — usar mock channel

---

## 5. Sprint plan Stage 1 (semanas 0, 1, 2)

### Semana 0 — Kickoff y setup (5 días)

**Lun-Mar:** Onboarding al stack para todos
- Lectura: Spec + ADR + este brief (cada uno, ~2h)
- Setup local de cada dev (~3h)
- Walkthrough del codebase actual con Catriel + Sr 1 (1h call)
- QA monta playwright skeleton

**Mier:** Decisiones tech secundarias del ADR
- Sr 1 + Sr 2 + Sr 3 cierran ADRs pendientes (Ollama placement, cron framework, monitoring, backup storage)
- Documentar en `docs/adr/`

**Jue-Vie:** Setup del monorepo + CI
- Crear estructura completa de `bily/`
- Configurar pnpm workspaces + turbo + pyproject.toml
- CI básico funcionando (GitHub Actions): lint + typecheck + tests + build
- Cada dev hace 1 PR de "hello world" para validar el flow

**Output semana 0:** repo armado, CI verde, todos los devs corriendo el sistema localmente, primer commit de cada uno mergeado.

### Semana 1 — Componentes individuales en paralelo (5 días)

| Dev | Tarea | Output esperado fin de semana |
|---|---|---|
| **Sr 1** | Esqueleto agent-runtime + LLM router básico | `pnpm run agent` levanta proceso, recibe inbound mock, llama Claude/Gemini con 1 tool fake, persiste log |
| **Sr 2** | Brain REST API + SQLite FTS5 | `curl localhost:8080/v1/agents/test/vault/foo.md` GET/PUT/DELETE funciona, search FTS5 OK |
| **Sr 3** | WhatsApp channel + puppeteer pool | Process levanta puppeteer, abre WA Web, recibe msg de testfono y lo loguea |
| **Jr** | Admin panel scaffolding + auth básica | Next.js corriendo con login JWT, lista vacía de agentes |
| **QA** | Test framework + primer test E2E | `pnpm test:e2e` corre con 1 test del agent loop con mocks |

**Standup diario** 15 min, mostrar progreso + bloqueos.

### Semana 2 — Integración + tu Bily migrado (5 días)

**Lun-Mier:** Integración de los componentes
- Sr 1 + Sr 3: agent-runtime + channel WA se hablan
- Sr 1 + Sr 2: agent-runtime usa tools-brain-client para hablar con Brain REST
- Sr 1: whisper-client integrado (reuso del existente)
- Jr: admin panel muestra el agente real

**Jue:** End-to-end smoke test con tu Bily
- Sr 3 + Catriel: migrar el WA de Catriel al nuevo stack
- Mandás un mensaje WA → el nuevo agent-runtime lo procesa → responde
- QA corre suite E2E completa

**Vie:** Fix bugs + documentación + retro
- Cualquier bug del smoke test
- Cada dev documenta su package (README + ejemplos)
- Retro de sprint: qué funcionó, qué no, ajustes para Stage 2

**Output Stage 1 (fin semana 2):** Tu Bily corriendo en el nuevo stack custom. Recibe texto + audio por WA, responde, persiste en Brain markdown, todo con LLM router y fallback. Single-tenant funcional.

---

## 6. Convenciones técnicas

### 6.1. Git workflow
- **Branch model:** trunk-based con feature branches cortas (<3 días)
- **Branch naming:** `<dev-initial>/<short-desc>` ej: `s1/agent-loop-skeleton`, `jr/admin-login`
- **Commits:** Conventional Commits (`feat:`, `fix:`, `chore:`, `refactor:`, `docs:`, `test:`)
- **PR template:** descripción + screenshots/output + checklist de DoD
- **Reviews:** 1 sr aprobando mínimo. Sr 1 tiene veto arquitectural.
- **NUNCA merge directo a main sin PR** (incluido Sr 1)

### 6.2. Code style
**TypeScript:**
- ESLint + Prettier (configs en root)
- Strict mode obligatorio (`"strict": true` en tsconfig)
- No `any` excepto con comentario justificando
- Async/await sobre callbacks
- Zod para validación de inputs externos

**Python:**
- Black + Ruff (configs en `pyproject.toml`)
- Type hints obligatorios (`mypy --strict`)
- Async donde aplique (FastAPI nativo)
- Pydantic v2 para validación

### 6.3. Testing
- **Unit tests:** cada función no trivial. Target coverage 70%+ en packages core
- **Integration tests:** cada API endpoint, cada plugin
- **E2E tests:** flows críticos (minteo, agent loop, brain ops)
- **NUNCA mergeás un PR con tests rojos**

### 6.4. CI/CD pipeline
1. **PR opened:** lint + typecheck + unit tests + build (max 5 min)
2. **PR mergeado a main:** + integration tests + E2E en staging
3. **Tag `v*`:** deploy a producción (manual approval por Catriel o Sr 1)

### 6.5. Logging
- TODOS los servicios usan structured JSON logging
- TS: `pino` con child loggers per-agent (`logger.child({ agentId })`)
- Python: `structlog` similar
- Format: `{ts, level, msg, agentId?, sessionId?, ...context}`
- Logs van a stdout, journald los captura, agregamos a Loki en monitoring

### 6.6. Secrets
- **NUNCA en git, NUNCA en .env committed.**
- `.env.example` con keys vacías, comprometido en git
- `.env` con valores reales: gitignored + en 1Password/Doppler del equipo
- Producción: Doppler/1Password Connect inyecta secrets al systemd service

---

## 7. Definition of Done (DoD)

Una feature/tarea está "done" cuando:

- [ ] Código mergeado a `main`
- [ ] Tests unitarios + integration cubren el comportamiento (coverage ≥70% del código nuevo)
- [ ] Linter + typecheck pasan sin warnings
- [ ] Documentación actualizada (README del package o doc en `docs/`)
- [ ] PR aprobado por al menos 1 Sr
- [ ] CI verde en main post-merge
- [ ] Si tiene UI: screenshot adjunto en PR + revisado por diseño (cuando aplique)
- [ ] Si toca seguridad/auth: revisión específica por Sr 1
- [ ] QA confirma que se puede testear (E2E test escrito o exploratory plan)

---

## 8. Comunicación y cadencia

### 8.1. Reuniones recurrentes
- **Standup diario** 15 min (sincrónico o async en canal): qué hice ayer, qué hago hoy, bloqueos
- **Planning de sprint** lunes 1h: review backlog + asignaciones
- **Demo + Retro** viernes 1h: mostrar progreso + discutir mejoras
- **Tech sync** miércoles 30 min: decisiones técnicas no urgentes pero importantes

### 8.2. Async
- **Slack/Discord/Telegram** (donde el equipo prefiera): canal por área (#agent-core, #brain, #channels, #admin) + canal general
- **GitHub Discussions** para decisiones arquitecturales documentables
- **Notion/Linear** para tareas y backlog (si usás algo, sino GitHub Issues)
- **El vault de Bily en Obsidian es la documentación canónica del producto** — leer y mantener actualizado

### 8.3. Cuando estás bloqueado
1. **5 min:** intentar resolver vos
2. **15 min:** googlear / leer docs / preguntar a Claude/Copilot
3. **>30 min:** preguntar en canal del equipo, no te quedes peleando solo
4. Si después de 1h no hay respuesta y es bloqueante: ping directo a Sr 1 o tech lead

---

## 9. Métricas de éxito de Stage 1

Al final de las 2 semanas, estos KPIs definen si Stage 1 fue exitoso:

| Métrica | Target |
|---|---|
| Coverage de tests en packages core | ≥70% |
| Builds CI verdes en main | 100% |
| Tu Bily migrado al nuevo stack y funcionando | ✅ Sí/No |
| Latencia mediana respuesta a msg de texto | <5s |
| Latencia mediana audio (con whisper) | <30s |
| Bugs reportados por QA y NO arreglados | 0 críticos, <3 menores |
| Documentación de cada package | Existe y es útil |
| Devs sin bloqueos crónicos | Todos productivos |

---

## 10. FAQ / unblocking

**P: ¿Puedo elegir lib X en lugar de la que dice el ADR?**
R: Tirar la propuesta en canal o tech sync. Si Sr 1 + tech sync aprueban, sí. Sin aprobación, no.

**P: ¿Mockeo X o uso el real?**
R: Para WA en dev: mockear (no consumir chips reales). Para LLM: real con keys de dev. Para brain: real local (SQLite).

**P: ¿Puedo agregar una feature que no está en spec?**
R: NO. Comunicar a Catriel para que decida si entra en MVP o post-MVP.

**P: ¿Cómo agrego una nueva tool al agente?**
R: Crear nuevo package `tools-<name>` en `packages/`, implementar interface `Tool`. Registrar en `agent-core/registry.ts`. Sr 1 review.

**P: ¿Tests E2E corren en mi máquina o solo en CI?**
R: Ambos. En dev: `pnpm test:e2e --watch`. En CI: automático post-merge.

**P: ¿Cómo simulo un agente nuevo localmente?**
R: `./scripts/spawn-fake-agent.sh test-001` — crea agente fake con mock WA.

**P: ¿Quién hace las decisiones arquitecturales?**
R: Decisiones grandes (nuevo componente, cambio de stack, refactor cross-package) → tech lead Sr 1 + Catriel. Decisiones internas a un package → owner del package.

**P: ¿Cómo trato secretos en local?**
R: `.env` local con valores reales, jamás committed. Para new secrets, agregalos al `.env.example` con placeholder + agregar en 1Password/Doppler del equipo.

**P: ¿Puedo deploy a producción yo mismo?**
R: Stage 1 y 2: solo Catriel + Sr 1. Stage 3+: cualquier sr con review previo.

---

## 11. Roadmap stages siguientes (referencia)

| Stage | Semanas | Foco | Owners principales |
|---|---|---|---|
| **Stage 1** | 1-2 | Single-tenant pulido | Todos |
| **Stage 2** | 3-4 | Multi-tenant (minteo, spawner, chip allocator) | Sr 3 + Sr 1 |
| **Stage 3** | 5-6 | Intelligence (weaver, profiler, pattern, backup) | Sr 2 + Sr 3 |
| **Stage 4** | 7-8 | Ops + beta (cost tracking, monitoring, runbooks) | Sr 1 + Sr 3 |

Después: 1-2 meses de bugs + iteración + features de feedback de beta antes de launch público.

---

## 12. Apéndice: por qué cada decisión técnica

Decisiones documentadas con rationale en el ADR. Highlights:

- **No usamos framework de agente (custom thin orchestrator)** — porque OpenClaw/Hermes/etc. son single-user, multi-tenancy es problema nuestro igual
- **Markdown REST propio (no Obsidian)** — escalable multi-tenant, control total del moat
- **TS + Python híbrido** — usamos lo mejor de c/u según el componente
- **Phone farm + whatsapp-web.js** — barato, conocido por el equipo, reuso de proyecto existente
- **Puppeteer compartido** — ahorra 300-400 MB/agente, pero CRITICAL: tools de browse SIEMPRE abren tab nueva
- **Vault wrappers como tools** — LLMs flojos alucinan URLs, los wrappers eliminan ese vector de error
- **SQLite-per-agent** — isolation perfecta, backup simple, alineado con per-agent process
- **Custom JWT** — control + cero costo, pero auth la lidera Sr 1

---

## Relacionado

- [[Bily/Productos/Bot-WhatsApp-MVP/Spec|Spec MVP completa]]
- [[Bily/Productos/Bot-WhatsApp-MVP/ADR|Architecture Decision Record]]
- [[Bily/Productos/Bot-WhatsApp-MVP/Brief-Diseno|Brief Diseño]]
- [[Bily/Productos/Bot-WhatsApp-MVP/Brief-Marketing|Brief Marketing]]
- [[Claude/Whisper|Stack whisper local — componente reusable]]
- [[Claude/Vault-Wrappers|Patrón vault-wrappers — precedente del approach brain-tools]]
