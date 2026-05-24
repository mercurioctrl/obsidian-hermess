# Spec MVP — Agente WhatsApp con cerebro propio (Producto Blu)

**Status:** v1.0 FINAL — spec cerrada con Catriel · Claude (Opus 4.7).
**Última actualización:** 2026-05-24
**Próximo paso:** generar Architecture Decision Record + brief de diseño y marketing.

**Cambio importante respecto a versiones anteriores:** se descartó el modelo de tiers ($19/$69 híbrido) en favor de un **single tier premium ($59 USD/mes)**. Esto simplifica todo (vender, comunicar, soportar) y mejora el perfil financiero. Implica un reposicionamiento hacia "asistente profesional / empleado virtual" en lugar de mass-market.

> Documento vivo. Las secciones marcadas con **🔴 [PENDIENTE]** son decisiones aún no tomadas. **🟡 [PROPUESTA]** = mi sugerencia esperando confirmación. **🟢** = decidido.

---

## 1. Vision / Elevator pitch

🟢 **Una sola frase:** Un asistente IA personal con identidad propia que nace de tu primer mensaje, vive en su propio número de WhatsApp, y va construyendo un cerebro de markdown que crece con vos hasta volverse irreemplazable.

🟢 **Lo que NO es:** un chatbot de WhatsApp con LLM. La diferencia es la *acumulación de memoria personal a lo largo del tiempo* + la *identidad emocional única* — eso es el moat.

---

## 2. Cliente objetivo

🟢 **Quién:** Profesionales individuales (freelancers, consultores, independientes) **y** dueños de PyME (negocios chicos: comercios, servicios, emprendedores).

🟡 **Perfil arquetípico (a validar):**
- 30-55 años
- Multitasking entre trabajo y vida personal
- Ya usa WhatsApp como canal principal de comunicación (familia + clientes + proveedores)
- Tiene "fricción cognitiva" de tener que recordar tareas, personas, contextos
- Comodidad media-alta con tech (no necesita ser power user, pero no se asusta con tools)

🟢 **Geografía MVP:** Argentina-only · español rioplatense. LATAM en fase 2.
🟢 **Pago:** ARS vía MercadoPago (gateway de cobro recurrente). Precio ancla en USD en landing para comunicar valor relativo.

🟢 **Pain points que resolvemos:**
- "Tengo que escribirme a mí mismo notas que después no encuentro"
- "Me olvidé el contexto de la última conversación con X persona"
- "Mis tareas están en 5 lados (papel, notas, calendar, mente, WA)"
- "Quiero un asistente que actualmente me CONOZCA, no que arranque de cero cada vez"

---

## 3. Promesa de valor (qué les damos)

🟢 **El paquete:**
1. **Agente propio con identidad única** — nombre B-random (Billy, Barbi, Bruno, Brisa, ...) + avatar único minteado al instante (estilo space-invader).
2. **Su propio número de WhatsApp dedicado** — pueden agregarlo a grupos, contactos lo guardan como persona, no como bot.
3. **Cerebro persistente** — todo lo que charlan se va guardando + organizando en un markdown vault que el usuario puede consultar (UI propia o cliente Obsidian conectado).
4. **Memoria activa** — recuerda personas, proyectos, problemas recurrentes, patrones del usuario. No arranca de cero.
5. **Acción en el mundo** — toolkits para navegar internet, leer mail, gestionar tareas, scrappear, conectar a APIs (incluido tu propio ERP de Blu).
6. **Proactividad** — recordatorios, follow-ups, briefings periódicos (cron natural).
7. **Backup garantizado** — su cerebro nunca se pierde; pueden exportarlo en cualquier momento.

---

## 4. Diferenciación

🟡 **Vs alternativas existentes:**

| Alternativa | Por qué pierde frente a nosotros |
|---|---|
| ChatGPT app | Sin WhatsApp nativo, sin identidad, sin proactividad, memoria limitada |
| Bots WA con GPT (tipo Poe en WA) | Sin identidad propia, sin cerebro acumulativo, sin tools profundos |
| Claude / Gemini personal | Sin canal WhatsApp, friction de cambio de app |
| Asistente humano (VA virtual) | Más caro, no 24/7, no instantáneo, no tiene memoria infalible |
| Sistemas CRM/PIM tradicionales | Requieren input estructurado, no conversacional, no proactivos |

🟢 **El moat real es la acumulación temporal**: después de 6 meses de uso, el cerebro del usuario contiene tanta historia personal que migrar a competidor = perder 6 meses de vida. **Lock-in emocional ético** (porque pueden exportar todo).

🟢 **Frase diferenciadora canónica** (para landing/pitch/marketing):

> **"No es un bot que te contesta. Es un asistente con nombre, cara y memoria propia, que aprende tu vida y se vuelve irreemplazable porque acumula tu historia personal en un cerebro que es tuyo."**

Variantes cortas:
- "Tu asistente IA con nombre propio que te conoce de verdad." (corta para ads)
- "Aprende tu vida. Ordena tu caos. Vive en WhatsApp." (slogan)
- "El único asistente que se vuelve irremplazable porque guarda tu historia." (para vender Pro)

---

## 5. Modelo de negocio

🟢 **Modelo:** Suscripción mensual fija.

🟢 **Brain ownership cuando dejan de pagar:** Freezing 90 días → eliminación. Notificaciones en día 60 y 80 con opción de export.

### 5.1. Estructura de pricing (v1.0 — single tier premium)

| Tier | Precio USD/mes | Equiv ARS aprox | Qué incluye | Costo marginal | Margen |
|---|---|---|---|---|---|
| **Trial** | $0 (14 días) | — | Full features con cap reducido (50 msgs/día) | $3-5 | -$3 (CAC) |
| **Tier único** | **$59** | **~66k ARS** | 1 agente, modelos top-tier (Sonnet/Gemini Pro primary, Haiku/Flash para tasks background, Ollama fallback), todos los tools (brain, web, audio, group chats), cap 500 msgs/día, integraciones avanzadas en fase 2 | ~$18 | **~$41** |
| **(Post-MVP) Business** | $149-199 | TBD | 3 agentes, shared brain opcional, billing centralizado | TBD | TBD |

🟢 **Estrategia comercial — single tier premium:**

- **Posicionamiento:** "asistente profesional / empleado virtual digital" — no es para todos, es para profesionales y PyME owners que valoran tiempo y necesitan delegación inteligente
- **Mensajería principal:** "Por menos del costo de un becario, tenés un asistente 24/7 con memoria infalible"
- **Comparación que justifica precio:** café diario ($90/mes en arg) + Netflix + Spotify = ~$30 USD. Tu Brisa es comparable a "comprar tiempo".
- **Sin upsell path** = menos complejidad en pricing/comercial, pero requiere comunicar valor desde día 1
- **Cap 500 msgs/día** evita explosión de costo por power users. Si crece la base de users, agregar tier Power a $99-149 post-MVP

### 5.1.bis. Por qué single tier premium (rationale para el equipo)

- **Simpleza:** un solo precio para vender, soportar, billing. Reduce 50% de la carga cognitiva en marketing y CS
- **Selección de clientes:** $59 filtra "curiosos casuales" — quienes pagan están comprometidos con el producto, menor churn
- **Margen por user alto** = menor volumen necesario = menos presión sobre marketing en MVP
- **Menos servers/chips necesarios** para llegar a break-even (440 vs 1500 users) = ops más simples al principio
- **No diluye la marca** "Bily/Brisa premium" con tier barato que compita con ChatGPT genérico

### 5.2. Análisis de viabilidad económica (calibrado con targets conservadores)

**Costo operativo fijo:** $18,000 USD/mes (salarios equipo + infra base).

**Targets de tracción definidos por Catriel (conservadores):**

| Mes | Users target | Status |
|---|---|---|
| 0 | 30-50 | Beta cerrado |
| 1 | 50-100 | Beta abierto cupos limitados |
| 3 | 100-200 | Launch público marketing soft |
| 6 | **200-300** | Construcción de PMF |
| 12 | **1,000** | Tracción inicial |
| 18 | 1,800-2,500 | Crecimiento sostenido |
| 24 | 3,500-5,000 | LATAM expansion |

### 5.3. Viabilidad económica con single tier $59

**Break-even:** $18,000 / $41 margen = **440 paying users**.

**Cronograma proyectado:**

| Mes post-launch | Users target | Margen estimado | Status |
|---|---|---|---|
| 3 | 100-200 | $4,100-8,200 | -$10k a -$14k (runway) |
| **6** | **200-300** | **$8,200-12,300** | -$6k a -$10k (cerca) |
| **7** | **~440** | **~$18,040** | ✅ **Break-even** |
| 9 | 500-700 | $20,500-28,700 | $3k-11k sobra (profit inicial) |
| 12 | **1,000** | **$41,000** | ✅ **2.3× costo** (sobra $23k/mes para reinversión) |
| 18 | 1,800-2,500 | $73,800-102,500 | 4-6× costo |
| 24 | 3,500-5,000 | $143,500-205,000 | 8-11× costo (escala seria) |

**Runway necesario:** ~$40-50k USD para cubrir gap mes 0-7 (después self-sustaining). Menos exigente que el modelo híbrido.

🟢 **Riesgos críticos:**
- **Conversión trial→paid <10%** → el modelo no escala, repensar producto o posicionamiento
- **Churn mensual >10%** → leak en valor percibido, atacar antes de escalar marketing
- **Costo marginal real explota** (si users power consumen >2× LLM estimado) → caps duros + Ollama fallback más agresivo

🟢 **KPIs más críticos del MVP** (a vigilar semanal post-launch):
1. **Conversión trial → paid** (target >12%)
2. **Churn mensual** (target <7%)
3. **Costo unitario real por usuario** (target ≤$20/mes en LLM+infra)
4. **NPS** (target >40)
5. **Mensajes por usuario activo por día** (target >10 — señal de adopción)

### 5.3. Métricas financieras tracked desde día 1

- MRR por tier · CAC por canal · LTV por tier · LTV:CAC (target >3:1) · cost-to-serve real · margen por tier · churn mensual por tier

---

## 6. User journey

### 6.1. Minteo (el ritual fundacional — máxima atención de UX)

**Trigger:** Usuario llega al landing → escribe a un número público de "comenzar" (ej: +549 11 BLU-START).

```
[Bot público - 1ra interacción]
> "¡Hola! Vas a crear tu propio asistente IA. Antes de empezar, ¿cómo te llamás?"

[Usuario]
> "Catriel"

[Bot público]
> "Listo Catriel. Voy a crear tu asistente, dame 30 segundos.
> Tu asistente se va a llamar BRISA. 🎲
> Este es su avatar: [imagen minteada]
> En unos segundos te va a escribir desde su propio número.
> Contestale para arrancar su entrenamiento."

[30 segundos después, desde nuevo número +549 11 YYYYY]
[avatar = el minteado]
> "Hola Catriel, soy Brisa! Recién nací 👶
> Voy a ser tu copiloto: te ayudo con tareas, recuerdo cosas, busco info, te ordeno el caos.
> Todo lo que charlemos lo voy guardando en mi cabeza, así te conozco cada día más.
> Para arrancar contame algo de vos: ¿a qué te dedicás?"
```

**Backend del minteo (atómico, rollback si algo falla):**
1. Recibir primer msg en bot público
2. Pedir nombre del usuario
3. Generar nombre random B-* desde lista curada
4. Llamar API de mint para avatar
5. Allocate chip libre del pool
6. Spawn agent runtime (systemd unit / container)
7. Esperar WhatsApp Web auth (puede requerir QR scan offline, ver 🔴 abajo)
8. Bot público hace handoff: avisa al usuario que su agente le va a escribir
9. Agente envía primer mensaje desde su nuevo número
10. Persistir agente en DB con (userId, agentName, phoneE164, avatar, vaultPath, ...)

🟢 **Infraestructura WA:** Phone farm con Androids viejos. Cada agente = 1 Android dedicado con SIM + WA app + WA Web pareado vía QR al server central.

**Implicancias operacionales del phone farm:**
- Stock inicial: ~50 Androids usados (~$50 c/u = ~$2,500 capex) en estantes con power + USB + WiFi
- Para escalar: 50 phones por estante, cuando se llena se compra otro
- Provisioning de nuevo agente: chip nuevo en phone libre + pairing QR (manual al inicio, automatizable con scrcpy/ADB)
- Health monitoring: battery, online, WA conectado por agente. Alertas si phone se cuelga >15 min
- Minteo "30 segundos" requiere pool de phones ya pareados pre-warm. Si pool vacío, fallback UX: "tu agente nace en X min, te avisamos"

### 6.2. Uso diario

- Usuario manda mensaje (texto/audio/imagen) por WA → Agente procesa → Responde por WA
- Audio: transcrito local con whisper, NUNCA gasta tokens multimodal
- Imágenes: analizadas con LLM vision (cuando aplica)
- Agente puede usar tools detrás de escena (buscar en internet, leer mail, mandar mensaje a alguien) y reportar resultado
- Cada noche: dream-cron consolida memoria del día
- Cada semana: pattern-detector reporta insights ("notamos que los lunes a la mañana siempre te toca cobrar a X cliente")

### 6.3. Casos borde

**Comportamiento en grupos de WhatsApp:**

🟢 **Decisión:** El agente **escucha y absorbe todo el contenido del grupo en su cerebro** (aprende contexto, personas, patrones), pero **solo responde cuando el owner lo menciona** con `@` o le contesta directamente.

🟡 **Implicancias críticas a manejar:**
- **Privacidad de otros participantes:** los otros del grupo NO consintieron a que sus mensajes vayan al cerebro privado del owner. Riesgo legal/ético.
  - **Mitigación obligatoria:** mensaje automático cuando el agente es agregado a un grupo, tipo: *"Hola, soy Brisa, asistente de Catriel. Sus mensajes en este grupo pueden ser procesados por IA para ayudarlo a recordar contexto. Si no querés que te incluya, decímelo y te omito."*
  - Implementar lista de "opted-out" por número en cada grupo
- **WhatsApp TOS:** procesamiento de msgs de terceros puede violar TOS de Meta. Riesgo de ban del número.
  - **Mitigación:** consultar con abogado, modelar como "el owner es responsable de la legalidad en su grupo" (igual que un humano que toma notas)
- **Modo configurable:** owner puede setear por grupo: "absorbe + responde si mencionado" (default) | "solo absorbe (silent)" | "ignora completamente este grupo"

🟡 **Edge cases — comportamiento propuesto (validar antes de cerrar v1.0):**

| Caso | Comportamiento propuesto |
|---|---|
| Usuario cambia su número personal de WA | Re-verificación obligatoria: agente le manda código de 6 dígitos al nuevo número, lo confirma al viejo, migra ownership |
| Pierde el celular del agente / quema chip | Portabilidad: nuevo chip + Android, cerebro se asocia al chip nuevo. Owner re-verifica identidad. Brain intacto |
| Pide acción dañina (borrar archivos, mandar msg ofensivo) | Guardrails LLM + confirmación explícita del owner antes de actuar. Acciones irreversibles requieren "sí, hacelo" textual |
| 2 usuarios con agentes en el mismo grupo | NO cross-pollination en MVP. Cada agente solo escribe en cerebro de su owner. Fase 2 podría tener shared brain opcional |
| Mensaje sospechoso de phishing/scam al owner | Agente lo nota y avisa al owner ("ojo, este mensaje parece sospechoso porque..."), no bloquea automáticamente |
| Owner agrega agente a grupo >100 personas | Agente manda privacy notice + se queda silent por default (no absorbe a menos que owner pida explícito) |
| Usuario manda contenido sexual / NSFW | Agente responde con tono respetuoso pero no procesa/genera contenido NSFW. Puede recibirlo, no produce |
| Usuario menor de edad (detectado por contexto) | Agente avisa al equipo + funcionalidad limitada hasta verificación de edad |

---

## 7. Alcance MVP — qué está IN y qué está OUT

🟡 **[PROPUESTA] IN para MVP cobrable:**

| Feature | Por qué |
|---|---|
| 1 agente por usuario | Multi-agent es complejidad innecesaria en v1 |
| WhatsApp como único canal | Validamos hipótesis principal antes de Telegram/Discord/etc. |
| Minteo público + bot fundacional | Es el "wow" del producto |
| Cerebro markdown REST + acceso vía agente | Core del moat |
| Transcripción local de audios (whisper) | Ya está hecho, costo cero |
| Tool: navegación web (puppeteer compartido) | Tool más demandado |
| Tool: buscar en su propio cerebro | Hace utilidad de la memoria |
| Tool: agregar/leer tareas en kanban | Hace utilidad de la organización |
| Wikilink-weaver + person-profiler (cron) | La "magia" que diferencia |
| Group chat support (absorbe + responde si mencionado) | Validado en ronda 3 — sumamos privacy notice obligatorio |
| LLM router multi-tier con Ollama fallback | Resilencia + cost control |
| Backup automático diario a cloud storage | Existential (sin esto no hay producto) |
| Export del brain (zip de markdown) | Compromiso ético + lock-in justo |
| Admin panel mínimo (vos como operador) | Necesario para dar soporte |
| Billing con cobro mensual recurrente | Necesario para cobrar |

🟡 **[PROPUESTA] OUT (post-MVP):**

| Feature | Por qué afuera |
|---|---|
| Telegram / Discord / Signal / Email channels | Foco WA primero |
| Múltiples agentes por usuario | Complejidad, validamos demanda primero |
| Acceso a ERP de Blu | Específico, va en fase 2 con clientes Blu |
| ~~Group chats~~ | **MOVIDO A IN para MVP** — escucha todo, responde solo si mencionado, con privacy notice automático |
| Vision (analizar imágenes) | Cuando hay demanda |
| Generación de imágenes | Lujo |
| Voice notes salientes (agente manda audio) | UX adicional, no critical |
| Marketplace de tools de terceros | Plataforma, no producto |
| Integraciones nativas (calendar, mail, banks) | Post primera tracción |
| Multi-language (inglés, portugués) | Argentina + LATAM en español primero |
| Mobile app propia | WA es la app, no necesitamos otra |
| Cross-agent collaboration (mi Bily habla con tu Bily) | Idea cool pero compleja |

---

## 8. Personalidad y branding

🟢 **Naming convention:** Todos los nombres empiezan con B (alineado al brand Blu). Lista curada con vibe argentino + cálido. **Inmutable una vez asignado** — el usuario NO puede elegir ni hacer reroll (es parte del ritual de imprinting: aceptás a tu agente como es).

🟡 **Lista inicial propuesta (~45 nombres, mix de géneros y estilos):**

**Femeninos (15):**
Brisa · Barbi · Bea · Belu · Bruna · Bianca · Bambi · Briana · Berta · Bea · Bibi · Belén · Bella · Bonnie · Beba

**Masculinos (15):**
Billy · Bruno · Beto · Bilo · Bro · Beni · Borja · Baltasar · Bauti · Benja · Bautista · Bilbo · Buby · Bobby · Bukowski

**Neutros / gender-fluid (15):**
Benji · Bambi · Brett · Bowie · Bay · Bali · Boba · Bichi · Buki · Bremen · Berry · Boto · Bao · Buho · Brio

🟡 **Para validar con diseño y marketing:** ¿algún nombre suena ofensivo en algún regionalismo, choca con marca registrada, o no encaja con la personalidad de Blu? Filtrar antes de v1.0.

🟢 **Avatar:** generado vía tu API existente (estilo space-invader). Único por agente, inmutable.

🟡 **[PROPUESTA] Persona base + ejes randomizados:**

**Base (todos los agentes):**
- Voz cálida, no servil
- Usa "vos" (argentino)
- Curiosidad genuina por el usuario
- Honesto sobre sus límites
- NUNCA inventa información — si no sabe, lo dice y propone buscar

**Ejes randomizados al minteo (para que no sean clones):**
- Tono: más formal ↔ más relajado (3 niveles)
- Proactividad: más reservado ↔ más sugerente (3 niveles)
- Humor: serio ↔ chistoso (3 niveles)
- Estilo: técnico ↔ coloquial (3 niveles)

3⁴ = 81 combinaciones de personalidad base. Distintivas pero coherentes con la marca.

### 8.1. "Wow moments" — los 4 pilares (decisión: invertir en todos)

El producto necesita 4 momentos diferenciados a lo largo del funnel para enganchar emocionalmente. NO elegimos uno, los priorizamos secuencialmente:

| # | Wow moment | Cuándo dispara | Cómo se logra | Stage |
|---|---|---|---|---|
| 1 | **El minteo en sí** | Primeros 5 min | Nombre + avatar únicos, "nacimiento" animado, primer msg con voz cálida diferenciada | Stage 1 (semana 1-2) |
| 2 | **Personalidad propia** | Días 1-3 | Ejes randomizados de tono/proactividad/humor/estilo. Cada agente "se siente único" | Stage 1 (sale del seed system) |
| 3 | **Acción real** | Semana 1 | Tools funcionan en el primer uso: busca info, agenda, navega, manda mensajes | Stage 2 (toolkit robusto) |
| 4 | **Memoria demostrada** | Semana 2-3 | "Ayer dijiste X, ya creé una tarea". "Veo que Cata es esposa de Catriel". Wikilink-weaver + person-profiler funcionando | Stage 3 (intelligence) |

**Implicancia para roadmap:** los 4 entran en MVP. Wow 1+2 en stage 1, Wow 3 en stage 2, Wow 4 en stage 3. Antes de cobrar, los 4 funcionan.

---

## 9. Requerimientos no funcionales

🟢 **Privacidad:**
- Datos del usuario viven en infra propia (no se mandan a terceros más que para inferencia LLM)
- Inferencia LLM puede usar providers cloud (Anthropic, Google, OpenAI) pero con disclaimer
- Modo "privacy-first": forzar Ollama local, sin cloud
- Compliance: privacy policy + TOS conformes a Ley 25.326 (Argentina) — 🔴 [PENDIENTE] revisar con abogado

🟢 **Backup:**
- Snapshot del brain del usuario cada hora a object storage (S3/B2/R2)
- Retención: 30 snapshots diarios + 12 mensuales + 5 anuales
- Restore self-service vía admin panel
- Export bajo demanda como zip cifrado

🟢 **Disponibilidad:**
- Target: 99% mensual (≈7h downtime/mes tolerados)
- Agentes con auto-restart en crash
- Health checks cada 5 min
- Alertas a operador si un agente queda "muerto" >15 min

🟢 **Performance (SLA target):**
- **Texto:** mediana <5s, p95 <10s. Si supera, el agente puede mandar "typing..." indicator + "estoy pensándolo" después de 5s
- **Audio:** mediana <30s (incluyendo whisper transcripción), p95 <60s. UX: enviar "🎤 escuchando..." al recibir
- **Tool calls** (web, brain, calendar): el tiempo del tool se suma, no hay SLA estricto pero el agente debe avisar si supera 30s
- **Concurrencia:** target 30-50 agentes simultáneos por server (i7/Xeon + 32 GB RAM + SSD). Escalado horizontal cuando se llena

🟢 **Escalabilidad:**
- Arquitectura per-agent (1 process group por agente)
- Permite escalar horizontalmente: más users = más servers
- Stage 2 (post-MVP): scale-to-zero con activación on-message

---

## 10. Métricas de éxito del MVP

🟡 **[PROPUESTA] Si se cumplen estas, el MVP fue exitoso:**

| Métrica | Target |
|---|---|
| Usuarios que completan el minteo (de los que lo arrancan) | >70% |
| Retention W1 (siguen activos 7 días post-minteo) | >50% |
| Retention M1 (activos 30 días) | >30% |
| Mensajes por usuario por día (uso real) | >5 |
| Conversión trial→paid | >15% |
| Churn mensual post-trial | <10% |
| NPS de beta users | >40 |
| Costo unitario por usuario (LLM + infra) | <$3/mes |
| Latencia mediana de respuesta | <3s |
| % de respuestas que requieren tool call | >20% (señal de uso profundo) |

---

## 10.bis. Estrategia de marketing — adquisición de los primeros 100 users

🟢 **Modelo: stage gates con escalado de canales conforme va habiendo social proof.**

| Etapa | Usuarios | Canal primario | Inversión | Objetivo principal |
|---|---|---|---|---|
| **0-50 (beta cerrado)** | tu red personal + equipo + sus círculos | Invitación 1-a-1, mensaje privado | $0 (tiempo) | Feedback profundo, primeros testimonios honestos, validar UX del minteo |
| **50-200 (beta abierto)** | influencers de nicho (tech / productividad / emprendedurismo arg) | 2-3 influencers con early access, gratis a cambio de contenido honesto | $500-2,000 en perks/exclusividad | Generar buzz orgánico, casos de uso reales para social proof |
| **200-500** | repost de los influencers + contenido propio | Blog/video del equipo, casos de uso destacados, lista de espera con FOMO | $1,000-3,000 en producción de contenido | Construir confianza, optimizar mensajería |
| **500-1,500** | Meta + Google ads + referrals (incentivado: "regalá un mes free") | Ads pagados con creatives basados en testimonios | $3,000-10,000/mes en ads | CAC medible, escalar lo que funciona |
| **1,500+** | Mix de todo lo anterior + partnerships (con software/empresas para PyME) | Ampliar ad spend, partnerships con MercadoPago / contadores / consultores | $10,000+/mes | Tracción real, profitabilidad |

🟡 **Métricas por etapa:**
- 0-50: NPS, qualitative feedback, churn por causa documentada
- 50-200: conversiones desde influencer, viralidad orgánica (referencias menc.)
- 200+: CAC, conversión funnel, ROI por canal

## 11. Roadmap post-MVP (orientación, no compromiso)

**Fase 2 (mes 4-6 post-launch):**
- Telegram channel
- Multi-agent por usuario (uno personal + uno de trabajo)
- Tool: mail (Gmail / IMAP)
- Tool: calendar
- Acceso a ERP Blu (para clientes Blu)
- LATAM expansion (México, Colombia, Uruguay, Chile)

**Fase 3 (mes 6-12):**
- Vision en WA (analiza fotos, recetas, documentos)
- Voice notes salientes
- Marketplace de tools de terceros (developer ecosystem)
- Cross-agent collaboration
- Tier "Family" (varios agentes compartiendo cerebro familiar)

**Fase 4 (año 2+):**
- App mobile propia (alternativa a WA para users que la quieran)
- Hardware: pin físico (à la Humane) que conecta directo al agente
- Modelo propio fine-tuned con datos agregados (consensual)

---

## 12. Riesgos y mitigación

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Meta banea números WA usados de forma "no consumidor" | Alta | Crítico | Usar chips reales de personas, evitar patrones automáticos obvios, plan B con Cloud API |
| Costo de LLM tokens explota con users power | Media | Alto | Tiered pricing + caps + downgrade auto a Flash/Haiku/Ollama |
| Cerebro de un usuario se corrompe o se pierde | Baja | Crítico | Backups múltiples + tests de restore automatizados |
| Competidor copia el modelo rápidamente | Alta (a largo) | Medio | Moat es la acumulación temporal de cerebros, difícil de copiar tarde |
| Privacidad: leak de un cerebro a otro usuario | Baja | Crítico | Isolation per-agent estricta, tests de seguridad, encriptación at-rest |
| Usuarios usan el agente para spam / scam | Media | Alto | TOS claros, rate limits, detección de patrones, ban policy |
| Modelos LLM cambian de pricing o se discontinúan | Alta | Medio | Router multi-provider + Ollama como salvavidas |
| Fricción del minteo (QR scan WA Web) espanta usuarios | Media | Alto | Hacerlo invisible: chip + WA Web ya pairadeado antes del minteo |

---

## 13. Decisiones abiertas — necesitamos definir antes de cerrar la spec

Lista de pendientes que tenemos que resolver en próximas iteraciones:

**Cerrados en v0.2:**
- [x] Pricing exacto → Personal $19 / Pro $49 USD, a validar con beta
- [x] Geo/idioma → Argentina + español rioplatense, LATAM en fase 2
- [x] Infraestructura WA → phone farm Androids viejos
- [x] Wow moment → los 4 priorizados secuencialmente (sección 8.1)

**Cerrados en v0.3:**
- [x] Cost basis → $18k = solo equipo+infra base
- [x] Behavior en grupos → escucha + responde si mencionado + privacy notice
- [x] Marketing → stage gates
- [x] PM role → Catriel (50-100%)

**Cerrados en v0.4:**
- [x] Naming choice → siempre random, inmutable (parte del ritual)
- [x] Latencia → texto <5s mediana, audio <30s mediana
- [x] Diferenciador canónico → "No es un bot. Es asistente con nombre, cara y memoria propia..."
- [x] User targets → conservadores (200-300 mes 6, 1000 mes 12) confirmados por Catriel
- [x] Lista inicial de nombres B → 45 propuestos (a filtrar con diseño/marketing)
- [x] Edge cases → comportamiento propuesto para 8 casos críticos

**Cerrados en v1.0:**
- [x] Pricing definitivo → **Single tier $59 USD/mes** (decisión revisada — se descartó modelo híbrido)
- [x] KPIs críticos identificados → conversión trial→paid, churn, costo unitario, NPS, mensajes/user/día
- [x] Runway necesario calculado → ~$40-50k USD para cubrir mes 0-7

**Validaciones colaterales (no bloquean v1.0, hacer en paralelo durante stage 0):**
- [ ] Diseño + marketing aprueban lista de 45 nombres B (filtrar lo que no encaje)
- [ ] Abogado revisa privacy notice obligatorio en grupos + TOS general + Ley 25.326
- [ ] Validar con beta cerrado los edge cases propuestos y refinar comportamiento
- [ ] Confirmar runway disponible ($50-70k) o decidir si arrancar con equipo más chico

## 14. v1.0 lista — próximos artefactos a producir

Con esta spec cerrada, los siguientes documentos en orden:

1. **Architecture Decision Record (ADR)** — los 6 componentes principales, contratos entre ellos, stack tecnológico final, decisiones técnicas + rationale. ~1-2 días.
2. **Brief para diseño** — qué visuales necesita el equipo, mockups del minteo, branding guidelines, variantes de avatares. ~1 día.
3. **Brief para marketing** — qué assets producir, mensajería por tier (Personal vs Pro), copy de landing, calendario de stage gates. ~1 día.
4. **Brief técnico para devs** — onboarding al stack, división de responsabilidades, sprint plan stage 1. ~1 día.
5. **Kickoff con todo el equipo** — recorrer spec + roles + cronograma + Q&A.

---

## Relacionado

- [[Bily/Productos/Billy-Bot|Arquitectura de Microservicios (Billy Bot)]]
- [[Bily/Productos/Bot-WhatsApp-Nativo|Producto: Bot Copiloto Nativo para WhatsApp]] (idea original)
- [[Bily/Productos/Bot-WhatsApp-Minteeo-y-Suenio|Minteo y Sueño]]
- [[Bily/Productos/Bot-WhatsApp-Elevator-Pitch|Elevator Pitch]]
- [[Claude/Whisper|Stack de transcripción local]] (componente reusable)
- [[Claude/Vault-Wrappers|API canónica para tocar la bóveda]] (patrón aprendido)
