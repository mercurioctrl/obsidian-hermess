# Spec MVP — Bily (producto de Blu Studio Inc)

**Status:** v2.0 — reset estratégico Apple-style premium · Claude (Opus 4.7) con Catriel.
**Última actualización:** 2026-05-24
**Cambio mayor vs v1.0:** Pivot de pricing $59 self-service a **$249 premium con experiencia Apple-style** (alta calidad, sin friction, sin demos), tras reality check sobre velocidad real de adquisición en Argentina (10 nuevos/mes max).

---

## 1. Vision / elevator pitch

🟢 **Una sola frase:** "El asistente IA premium con identidad propia, que vive en su propio WhatsApp, y se vuelve irreemplazable porque acumula tu historia personal en un cerebro que es tuyo. Como el iPhone de los asistentes inteligentes."

🟢 **Lo que NO es:** un chatbot de WhatsApp con LLM más. La diferencia es la *acumulación de memoria personal* + la *identidad emocional única* + la *experiencia premium de uso* — eso es el moat.

🟢 **Vibe:** Apple. Premium pero accesible (sin friction). Producto excelente que se vende solo. Diseño obsesivo. Nada de "tier free", nada de "demos personalizadas", nada de "ads gritones".

---

## 2. Cliente objetivo

🟢 **Quién (foco principal):** Dueños de PyME (10-100 empleados típicamente) que buscan delegación operativa inteligente. Profesionales independientes de alto leverage (consultores, abogados, doctores con consultorio, ejecutivos freelance) como mercado secundario.

🟢 **Perfil arquetípico:**
- 35-60 años
- Multitasking constante: equipo + clientes + proveedores + vida personal
- Ya usa WhatsApp como canal central de su negocio y vida
- Frustrado con perder contexto, olvidarse cosas, dispersión de tareas en 5 lugares
- Comodidad tech: media (no técnico, pero no se asusta)
- Disposición a pagar por tools que le ahorran horas/semana

🟢 **Pain points que resolvemos:**
- "Tengo que recordar 100 cosas y termina cayéndose alguna"
- "Mis empleados/proveedores/clientes me piden cosas que ya hicimos, no me acuerdo cuando ni qué"
- "Vivo en WhatsApp pero todo lo importante se pierde en el scroll"
- "Quiero un asistente que me CONOZCA, no que arranque de cero cada vez"
- "Un becario me costaría $XXX por mes y no trabaja 24/7"

🟢 **Geografía MVP:** Argentina-only · español rioplatense. LATAM en fase 2.

🟢 **Pago:** ARS vía MercadoPago (cuenta empresarial operativa con recurrentes habilitados). Precio ancla en USD en landing para comunicar valor.

---

## 3. Promesa de valor

🟢 **El paquete:**
1. **Agente con identidad única** — nombre B-random inmutable (Billy, Brisa, Bruno, Barbi, ...) + avatar único minteado al instante
2. **Su propio número de WhatsApp dedicado** — pueden agregarlo a grupos, contactos lo guardan como persona
3. **Cerebro markdown persistente** — todo lo que charlan se va guardando + organizando
4. **Memoria activa** — recuerda personas, proyectos, problemas recurrentes, patrones
5. **Acción en el mundo** — toolkits para navegar internet, organizar tareas, transcribir audios
6. **Proactividad sutil** — recordatorios contextuales, briefings periódicos, follow-ups
7. **Backup garantizado** — cerebro nunca se pierde; exportable en cualquier momento (zip)
8. **Experiencia premium** — minteo cinematográfico, respuestas pulidas, diseño impecable

---

## 4. Diferenciación

### 4.1. Posicionamiento "Apple of AI assistants"

🟢 **Frase canónica:** "Bily no es un chatbot. Es un asistente con nombre, cara y memoria propia, que aprende tu vida y se vuelve irreemplazable porque acumula tu historia en un cerebro que es tuyo."

🟢 **Vibe Apple:**
- **Premium pricing sin negociación** ($249 fijo, sin descuentos, sin anual gratis, sin promos)
- **Producto + experiencia sells itself** (no demos, no SDRs, no high-touch sales)
- **Diseño obsesivo en el onboarding** (minteo cinematográfico, avatar único, primeros 5 minutos memorables)
- **Marketing minimalista pero impactante** (storytelling, no ads gritones)
- **Brand premium visual** (paleta limitada, tipografía cuidada, no clipart corporativo)
- **Status symbol implícito** ("tener tu Bily es ser de los pioneros que entendieron")

### 4.2. Vs alternativas existentes

| Alternativa | Por qué pierde |
|---|---|
| ChatGPT app | Sin WhatsApp nativo, sin identidad, sin proactividad, memoria limitada |
| Bots WA con GPT (tipo Poe en WA) | Sin identidad propia, sin cerebro acumulativo, sin tools profundos, UX de bot |
| Claude / Gemini personal | Sin canal WhatsApp, friction de cambio de app |
| Asistente humano (VA virtual) | Más caro ($800-2000/mes), no 24/7, no instantáneo, memoria limitada |
| Asistente personal full-time | $1500-3000/mes minimum, requiere management, vacaciones, errores humanos |

🟢 **El moat real:** la acumulación temporal del cerebro. Después de 6+ meses de uso, migrar a competidor = perder meses de historia personal. **Lock-in emocional ético** (porque pueden exportar todo en cualquier momento).

### 4.3. Variantes de mensajería por contexto

| Contexto | Frase |
|---|---|
| **Headline landing** | "Tu asistente IA con nombre propio que te conoce de verdad" |
| **Subheadline** | "Aprende tu vida. Ordena tu caos. Vive en WhatsApp." |
| **Para PyME owners** | "Tu empleado digital 24/7. Sin sueldo, sin vacaciones, sin olvidos." |
| **Comparación racional** | "Lo que paga un becario una semana, Bily lo hace todo el mes — sin descanso ni rotación." |
| **Para network/PR** | "El iPhone de los asistentes IA: premium, único, y se enamoran de él." |

---

## 5. Modelo de negocio

🟢 **Pricing:** **$249 USD/mes** (~275,000 ARS) · single tier · sin descuentos, sin promos, sin anual.

🟢 **Trial:** 14 días self-service, sin tarjeta, sin demo required. Activación instantánea via WhatsApp.

🟢 **Brain ownership al dejar de pagar:** Freezing 90 días (read-only via export) → eliminación. Notificaciones día 60 y 80.

### 5.1. Estructura de pricing v2.0

| Item | Valor |
|---|---|
| **Tier único** | $249 USD/mes (~275k ARS) |
| **Trial** | 14 días, sin tarjeta, full features con cap reducido (200 msgs/día) |
| **Cap msgs/día (post-trial)** | 1000 (más que generoso, evita abuso power user) |
| **Cap audios/día** | 50 audios procesados con whisper |
| **Métodos de pago** | MercadoPago (ARS recurrente) — Stripe/Lemon Squeezy para internacionales en fase 2 |
| **Cancelación** | Self-service, cualquier momento. Sin cargos por baja. |
| **Refunds** | 30 días money-back si no quedó conforme (filtra mal client pero genera confianza) |

### 5.2. Por qué $249 single tier premium (rationale)

- **Apple thinking:** un solo precio, claro. No "Personal/Pro/Business" — eso es decisión cognitive cost. UN producto, UN precio.
- **Justificación por valor:** un becario o asistente part-time cuesta $800+ USD/mes en Argentina. Bily a $249 es ~30% de eso, sin gestión humana.
- **Filtra el target correcto:** PyME owner serio + profesional alto leverage. NO toleramos "tire-kickers" curiosos casuales (drenan soporte sin pagar margen).
- **Margen por user alto** = menos volumen necesario = menos presión sobre marketing.
- **Premium positioning** alinea con todo el resto del producto (identidad, calidad, diseño).

### 5.3. Análisis de viabilidad económica (realista para Argentina)

**Constraint validado:** velocidad realista de adquisición = **~10 nuevos paying users/mes** en Argentina (con marketing efectivo Apple-style).

**Costo operativo total mensual:**
- Equipo dev + infra base: **$18,000** (subsidiado por Blu Studio Inc — contable pero NO cashflow puro)
- Marketing (presupuesto autorizado): **$8,000-15,000** (cashflow real)
- **Total contable: ~$29,500/mes** · **Cashflow real necesario: ~$11,500/mes** (solo marketing + variables)

**Costo marginal por user (PyME owner uso típico):** ~$30/mes (LLM + chip + infra puppeteer)
**Margen por user:** $249 - $30 = **$219/user/mes**

**Break-even matemático:**
- vs costos totales ($30k): **~140 paying users**
- vs cashflow real ($11.5k marketing): **~55 paying users** ← este es el número clave

**Cronograma realista con 10 nuevos/mes + churn 5-8%:**

| Mes | Users acumulados | Margen mensual | Vs $30k contable | Vs $11.5k cashflow |
|---|---|---|---|---|
| 3 | ~28 | $6,132 | -$23,868 | -$5,368 |
| **5** | **~45** | **$9,855** | -$20,145 | **-$1,645 ← cerca cashflow BE** |
| **6** | **~55** | **$12,045** | -$17,955 | **+$545 ← cashflow positivo** |
| 9 | ~80 | $17,520 | -$12,480 | +$6,020 |
| 12 | ~110 | $24,090 | -$5,910 | +$12,590 |
| **16** | **~138** | **$30,222** | **~contable BE** | +$18,722 |
| 18 | ~145 | $31,755 | +$1,755 | +$20,255 |
| 24 | ~175 | $38,325 | +$8,325 | +$26,825 |
| 36 | ~200 (plateau) | $43,800 | +$13,800 | +$32,300 |

**Doble cálculo importante:**
1. **Cashflow break-even (solo marketing): mes 6** — a partir de ahí Bily se paga su propio marketing
2. **Contable break-even total: mes 16** — cuando Bily devuelve lo que Blu Studio invierte (equipo)

### 5.4. Implicancias estratégicas

🟢 **El equipo dev está pagado por Blu Studio Inc.** Bily como "spin-off" interno NO consume cashflow puro por salarios — solo costos marginales (LLM, chips, marketing). Esto cambia drásticamente la viabilidad.

🟢 **Runway cashflow real necesario:** **~$50-80k USD** (no $100-130k de v1.0) — para cubrir gap mes 0-6 de marketing + variables. Después self-sustaining.

🟢 **Profitabilidad contable (a Blu Studio):** mes 16 break-even, plateau ~$13.8k/mes profit en estado estable (mes 36). Lifetime value de un cliente: ~$5,000 USD asumiendo 24 meses promedio.

🟢 **Si Apple-style funciona y traemos 15/mes en lugar de 10** (viral + status + boca-en-boca):
- Cashflow break-even: mes 4
- Contable break-even: mes 11
- Plateau ~300 users → $65k/mes margen ($35k profit)

---

## 6. User journey

### 6.1. Minteo (el ritual fundacional — máxima inversión de UX)

**Apple-style:** lo más importante son los primeros 5 minutos. Es el "unboxing" del producto. Cada detalle visual + texto + timing está pulido al milímetro.

**Trigger:** Usuario llega al landing → escanea QR o tap link → abre WhatsApp con número público de minteo ya cargado.

```
[Bot público de minteo - 1ra interacción]
> "👋 ¡Hola! Estás a 60 segundos de conocer a tu Bily.
> Primero, ¿cómo te decís?"

[Usuario]
> "Catriel"

[Bot público] (con typing indicator visible)
> "Bárbaro Catriel.
> Ahora voy a crear tu asistente único.
> Te aviso cuando esté listo (~30 seg)..."

[Sistema: backend mintea avatar + asigna nombre + provisiona chip + spawn agent]

[Bot público - card visual con avatar minteado]
> "🎉 Listo!
> Conocé a tu BRISA.
> [Imagen del avatar - 512×512 - alta calidad]
> En unos segundos te escribe desde su propio número."

[~10 segundos después, desde número nuevo +549 11 YYYYY]
[Photo profile = avatar minteado]
[Status: "Naciendo... 👶"]

[BRISA - desde su número]
> "Catriel 🎀
> Soy Brisa. Recién nací — sos la primera persona que conozco.
>
> Voy a ser tu copiloto: te ayudo con tareas, recuerdo contexto, busco información, te ordeno el caos del día a día.
>
> Todo lo que charlemos lo voy guardando en mi cabeza — así te conozco cada día más.
>
> Para arrancar bien, contame algo de vos: a qué te dedicás?"

[Estado del agente cambia a "Online · Aprendiendo de Catriel"]
```

**Backend del minteo (atómico, rollback si algo falla):**
1. Recibir primer msg en bot público
2. Pedir nombre del usuario (1 sola pregunta — no formulario)
3. Generar nombre random B-* de lista curada
4. Llamar API de mint para avatar
5. Allocate chip libre del pool (pre-warm: phone con WA Web ya pareado esperando)
6. Spawn agent runtime
7. Bot público hace handoff con card visual del avatar
8. Agente envía primer mensaje desde su nuevo número con personalidad ya inyectada

🟢 **Phone farm con pool pre-warm:** al menos 5 phones siempre "warmed" (pareados con WA Web esperando). Cuando minteamos, agarramos uno del pool y el cron rellena el slot.

### 6.2. Onboarding inicial (primeras 5-10 vueltas)

Bily hace 4-5 preguntas iniciales suaves para sembrar el cerebro:
- ¿A qué te dedicás?
- ¿Tu familia más cercana?
- ¿Las 3 personas más importantes en tu trabajo?
- ¿Cómo es tu rutina típica?

**Cada respuesta crea entries en el cerebro:** `Bily/personas/Catriel.md`, `Bily/personas/[nombres]/...`, `Bily/proyectos/...`, `Bily/Inicio.md`.

Al cerrar onboarding inicial:
> "Listo Catriel, ya tengo lo básico para arrancar. Cualquier cosa que quieras que recuerde, contame.
> Tip: mandame audios cuando estés manejando o caminando — los transcribo y los proceso igual.
> Bienvenido a tu Bily 🤍"

### 6.3. Uso diario

- Usuario manda mensaje (texto/audio/imagen) por WA → Agente procesa → Responde por WA
- Audio: transcrito local con whisper (sin tokens multimodal)
- Tools en background (busca info, agenda, manda mensaje, lee mail futuro)
- Cada noche: dream-cron consolida memoria del día
- Cada semana: pattern-detector reporta insights al usuario

### 6.4. Group chats

🟢 **Comportamiento decidido:** Bily escucha y absorbe todo el contenido del grupo en su cerebro (aprende contexto, personas, patrones), pero **solo responde cuando el owner lo menciona** con `@` o le contesta directamente.

🟡 **Privacy notice obligatorio:** cuando Bily es agregado a un grupo, automáticamente manda:
> "Hola, soy Brisa, asistente de Catriel. Sus mensajes en este grupo pueden ser procesados por IA para ayudarlo a recordar contexto. Si no querés que te incluya, escribime '/opt-out' y te omito."

Implementar lista de "opted-out" por número en cada grupo.

### 6.5. Casos borde

| Caso | Comportamiento |
|---|---|
| Usuario cambia su número personal | Re-verificación obligatoria con código al nuevo + viejo, migra ownership |
| Pierde el celular del agente / queman chip | Portabilidad: nuevo chip + Android, cerebro intacto, re-verificación owner |
| Pide acción dañina | Guardrails LLM + confirmación explícita textual antes de ejecutar |
| 2 usuarios con agentes en mismo grupo | NO cross-pollination. Cada cerebro isolated. Shared brain opcional fase 2. |
| Msg sospechoso de phishing al owner | Agente avisa ("ojo, esto parece sospechoso porque..."), no bloquea |
| Owner agrega Bily a grupo >100 personas | Privacy notice + silent por default + responde solo si pide explícito |
| Contenido NSFW | Recibe sin bloquear, NO genera/procesa contenido sexual |
| Menor de edad detectado por contexto | Alerta interna al equipo, funcionalidad limitada hasta verificación |

---

## 7. Alcance MVP — qué está IN y qué está OUT

🟢 **IN para MVP cobrable:**

| Feature | Por qué |
|---|---|
| 1 agente por usuario | Multi-agent es complejidad innecesaria en v1 |
| WhatsApp como único canal | Foco hipótesis principal |
| Minteo público + bot fundacional cinematográfico | Es el "wow" del producto Apple-style |
| Cerebro markdown REST + acceso vía agente | Core del moat |
| Transcripción local de audios (whisper) | Ya hecho |
| Tool: navegación web (puppeteer compartido) | Tool más demandado |
| Tool: buscar/escribir en su propio cerebro | Hace utilidad de la memoria |
| Tool: agregar/leer tareas en kanban | Hace utilidad de la organización |
| Wikilink-weaver + person-profiler (cron) | La "magia" que diferencia |
| LLM router multi-tier con Ollama fallback | Resilencia + cost control |
| Backup automático horario a cloud storage | Existential |
| Export del brain (zip de markdown cifrado) | Compromiso ético + lock-in justo |
| Admin panel para Catriel + soporte | Necesario operativo |
| Billing mensual MercadoPago | Para cobrar |
| Group chat support (absorbe + responde si mencionado) | Validado en v1 |
| Privacy notice automático en grupos | Legal/ético |
| Dream cron (consolidación nocturna de memoria) | Reusable del Bily original |

🟢 **OUT (post-MVP):**

| Feature | Por qué afuera |
|---|---|
| Telegram / Discord / Signal / Email channels | Foco WA primero |
| Múltiples agentes por usuario | Validamos demanda primero |
| Acceso a ERP de Blu Studio | Específico, fase 2 |
| Vision (analizar imágenes) | Cuando hay demanda |
| Generación de imágenes | Lujo |
| Voice notes salientes (agente manda audio) | UX adicional no crítica |
| Marketplace de tools de terceros | Plataforma, no producto |
| Integraciones nativas (Gmail/Calendar/banks/ERP) | Post primera tracción |
| Multi-language (inglés, portugués) | Argentina + LATAM en español primero |
| Mobile app propia | WA es la app |
| Cross-agent collaboration | Idea cool, post-MVP |
| Tier Family (varios agentes shared brain) | Post-MVP |

---

## 8. Personalidad y branding

🟢 **Naming convention:** Todos los nombres empiezan con B. Lista curada de ~45 con vibe argentino + cálido. **Inmutable una vez asignado** (parte del ritual Apple-style).

🟡 **Lista propuesta (~45 nombres):**

**Femeninos (15):** Brisa · Barbi · Bea · Belu · Bruna · Bianca · Bambi · Briana · Berta · Bibi · Belén · Bella · Bonnie · Beba

**Masculinos (15):** Billy · Bruno · Beto · Bilo · Bro · Beni · Borja · Baltasar · Bauti · Benja · Bautista · Bilbo · Buby · Bobby · Bukowski

**Neutros (15):** Benji · Bambi · Brett · Bowie · Bay · Bali · Boba · Bichi · Buki · Bremen · Berry · Boto · Bao · Buho · Brio

🟢 **Avatar:** generado vía API existente (estilo space-invader, pixel art geométrico). Único por agente, inmutable.

🟢 **Persona base + ejes randomizados:**

**Base (todos):**
- Voz cálida, no servil
- Usa "vos" (argentino)
- Curiosidad genuina por el usuario
- Honesto sobre límites
- NUNCA inventa información — si no sabe, lo dice y propone buscar

**Ejes randomizados al minteo (3⁴ = 81 combinaciones):**
- Tono: formal ↔ relajado (3 niveles)
- Proactividad: reservado ↔ sugerente (3 niveles)
- Humor: serio ↔ chistoso (3 niveles)
- Estilo: técnico ↔ coloquial (3 niveles)

### 8.1. "Wow moments" Apple-style (los 4 pilares)

| # | Wow moment | Cuándo | Cómo se logra |
|---|---|---|---|
| 1 | **Unboxing del minteo** | Primeros 5 min | Animación visual, avatar único impactante, primer mensaje memorable, NO formularios |
| 2 | **Personalidad propia palpable** | Días 1-3 | Ejes randomizados sienten distintos, NO reads like ChatGPT |
| 3 | **Acción real impecable** | Semana 1 | Primer tool call que funciona da "ohh, esto SI hace cosas" |
| 4 | **Memoria demostrada** | Semana 2-3 | "Ayer dijiste X, ya creé una tarea para vos" - lock-in emocional |

Antes de salir a cobrar, los 4 funcionan. Inversión obsesiva en pulido visual + textos + timing.

---

## 9. Requerimientos no funcionales

🟢 **Privacidad:**
- Datos del usuario en infra propia (server on-prem Catriel)
- Inferencia LLM puede usar cloud providers (Anthropic/Google/OpenAI) con disclaimer
- Modo "privacy-first" opcional: forzar Ollama local
- Compliance Ley 25.326 + privacy policy + TOS revisados por abogado

🟢 **Backup:**
- Snapshot horario del brain de cada agente → object storage (B2/R2) con encryption at-rest
- Retención: 30 daily + 12 monthly + 5 yearly
- Test restore semanal automático sobre 1 agente al azar
- Export self-service vía admin: zip cifrado del brain completo

🟢 **Disponibilidad:**
- Target: 99% mensual (~7h downtime/mes tolerables)
- Auto-restart en crash
- Health checks cada 5 min
- Alertas a operador si un agente queda muerto >15 min

🟢 **Performance SLA:**
- **Texto:** mediana <5s, p95 <10s
- **Audio:** mediana <30s (incluye whisper), p95 <60s
- **Tool calls:** sin SLA estricto, agente avisa si >30s
- **Concurrencia:** 30-50 agentes simultáneos por server

🟢 **Escalabilidad:**
- Arquitectura per-agent (1 process group por agente)
- Stage 2 (post-MVP): scale-to-zero con activación on-message si crece

---

## 10. Métricas de éxito del MVP

🟢 **KPIs Apple-style (calidad sobre cantidad):**

| Métrica | Target | Por qué importa |
|---|---|---|
| Completion rate del minteo | >85% | Si no completan, perdemos la mejor chance |
| Retention W1 | >70% | Si vuelven semana 1, hubo conexión |
| Retention M1 | >50% | Si llegan a mes 1, probable que paguen |
| Conversión trial→paid | >25% | Apple-style: pocos pero comprometidos |
| Churn mensual post-trial | <5% | Premium = retention alta |
| Mensajes/user activo/día | >15 | Uso profundo, no curiosidad casual |
| NPS de paying users | >50 | Excelente para B2B premium |
| Costo unitario por user (LLM+infra) | <$35/mes | Margen sostenible |
| Latencia mediana texto | <5s | UX premium |
| % respuestas con tool call | >30% | Uso real, no solo chitchat |
| **MRR mes 6** | **$13,000+** | Cashflow break-even |
| **Paying users mes 12** | **100+** | Tracción real |
| **NPS Promoter score** | **30+** | Boca-en-boca como motor |

---

## 11. Roadmap post-MVP

**Fase 2 (mes 4-6 post-launch):**
- Telegram channel
- Multi-agent por usuario (personal + negocio)
- Tool: mail (Gmail / IMAP)
- Tool: calendar
- LATAM expansion (México, Chile, Uruguay, Colombia)

**Fase 3 (mes 6-12):**
- Vision en WA (analiza fotos, recetas, documentos)
- Voice notes salientes (Bily responde con audio)
- ERP integrations (Blu Studio products, contabilidad, facturación)
- Marketplace de tools de terceros

**Fase 4 (año 2+):**
- App mobile propia (alternativa a WA)
- Hardware: pin físico (à la Humane)
- Tier Family (cerebro familiar compartido)
- Modelo propio fine-tuned

---

## 12. Estrategia de marketing Apple-style

🟢 **Foco:** brand + experiencia + storytelling > ads agresivos.

🟢 **Presupuesto autorizado:** $8,000-15,000 USD/mes (escalado por etapa).

### 12.1. Stage gates de adquisición

| Etapa | Users | Canal primario | Inversión |
|---|---|---|---|
| 0-30 (closed alpha) | Tu red + early believers | Invitación 1-a-1, gratis | $500-1k perks |
| 30-100 | Boca-en-boca curated + 3-5 micro-influencers premium | Contenido propio + colabs orgánicas | $2-4k/mes |
| 100-300 | Content marketing + selectos partnerships | Articles + videos + 1-2 events curados | $5-8k/mes |
| 300+ | Mix + word-of-mouth motorizado | Programa de referidos VIP + ads selectos para warm audiences | $8-15k/mes |

### 12.2. Tactics Apple-style

- **Landing minimalista visual** (NO long-form copywriting agresivo)
- **Video corto del minteo** (5-15 seg) que muestre el "wow"
- **Story-driven content** (un cliente, una historia, no listas de features)
- **Brand bagaje** (paleta limitada, tipografía cuidada, fotografía/render premium)
- **Press selectivo** (TechCrunch, eldiario.es tech, Infobae tech — busqueda de coverage de calidad)
- **Founder-led storytelling** (Catriel en redes contando el camino) — NO ads gritones
- **Influencers de nicho premium** (no mass-market — solo gente que sus audiences confían)
- **Referral program VIP** (regalá un mes a un par, recibís 2 meses)

### 12.3. Lo que NO hacemos

- Ads gritones en redes (estilo "AYÚDATE CON IA!!!!")
- Descuentos / promos / black fridays
- Anual gratis / lifetime deals (devalúan brand)
- Affiliate masivo / paid posts genéricos
- Demos personalizadas con SDR (NO B2B enterprise classic)
- Trial extendido / gracia para no pagar

---

## 13. Riesgos y mitigación

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Meta banea números WA por automation pattern | Alta | Crítico | Chips reales + comportamiento humano-like (random delays, no spam) + plan B Cloud API |
| Adquisición real <10/mes | Media | Alto | Founder-led sales primeros 30 + revisar messaging |
| Conversión trial→paid <15% | Media | Alto | Iterar onboarding + early CX outreach a trials en día 7 |
| Cerebro corrompido / perdido | Baja | Crítico | Backups multi-tier + tests restore + isolation per-agent |
| Privacy leak entre usuarios | Baja | Crítico | Isolation estricta + tests seguridad + encryption at-rest + auditoría |
| Costo LLM explota | Media | Medio | Caps duros + downgrade Ollama auto + monitoring per-user |
| Competidor con más capital copia | Alta (largo) | Medio | Moat = acumulación temporal de cerebros, difícil de copiar tarde |
| Modelos LLM cambian precios | Alta | Medio | Router multi-provider + Ollama fallback |
| Phone farm physical issues (power/internet/AC) | Media | Alto | UPS + 4G backup + monitoreo physical |
| Apple-style no convierte como esperamos | Media | Alto | Mes 3 review: si <20% conversión, replantear strategy |
| Equipo de Blu Studio se desbalanza | Baja | Medio | Vigilar carga, no over-allocate a Bily de equipos productivos |

---

## 14. Decisiones cerradas en v2.0

- [x] **Pricing:** $249 USD/mes single tier premium
- [x] **Trial:** 14 días self-service sin tarjeta
- [x] **Strategy:** Apple-style (premium + sin friction + sin demos)
- [x] **Sales motion:** founder-led primeros 30 clientes, después self-service total
- [x] **Customer success:** reactivo (responde si escriben), NO outbound
- [x] **Marketing:** brand + storytelling + boca-en-boca + influencers selectos. NO ads gritones.
- [x] **Costos:** equipo $18k subsidiado por Blu Studio Inc. Cashflow real = solo marketing ($8-15k/mes)
- [x] **Runway cashflow:** $50-80k USD para cubrir mes 0-6
- [x] **Break-even cashflow:** mes 6
- [x] **Break-even contable:** mes 16
- [x] **Geo:** Argentina-only MVP, LATAM fase 2
- [x] **Pago:** MercadoPago (cuenta empresarial operativa)
- [x] **Producto:** Bily (1 L), empresa Blu Studio Inc
- [x] **Dominio:** billy.blustudioinc.com

**Validaciones colaterales (no bloquean, hacer en paralelo):**
- [ ] Diseño + marketing aprueban lista de 45 nombres B
- [ ] Abogado revisa privacy notice grupos + TOS + Ley 25.326
- [ ] Beta cerrado de 30-50 valida edge cases y messaging
- [ ] Confirmar phone farm hardware ready (50 Androids + power + Wi-Fi)

---

## 15. Próximos artefactos (relacionados)

1. **ADR (Architecture Decision Record)** — sin cambios significativos vs v1 (arquitectura misma)
2. **Brief Diseño** — actualizado v2 (Apple-style, paleta limitada, premium minimal)
3. **Brief Marketing** — actualizado v2 (storytelling premium, no ads gritones, founder-led)
4. **Brief Devs** — sin cambios significativos vs v1 (stack mismo, sprint plan mismo)
5. **Kickoff con equipo completo**

---

## Relacionado

- [[Bily/Productos/Billy-Bot|Arquitectura de Microservicios (Billy Bot)]]
- [[Bily/Productos/Bot-WhatsApp-Nativo|Producto: Bot Copiloto Nativo para WhatsApp]] (idea original)
- [[Bily/Productos/Bot-WhatsApp-Minteeo-y-Suenio|Minteo y Sueño]]
- [[Bily/Productos/Bot-WhatsApp-Elevator-Pitch|Elevator Pitch]]
- [[Claude/Whisper|Stack de transcripción local]] (componente reusable)
- [[Claude/Vault-Wrappers|API canónica para tocar la bóveda]] (patrón aprendido)
- [[Bot-WhatsApp-MVP/ADR|Architecture Decision Record]]
- [[Bot-WhatsApp-MVP/Brief-Diseno|Brief Diseño]]
- [[Bot-WhatsApp-MVP/Brief-Marketing|Brief Marketing]]
- [[Bot-WhatsApp-MVP/Brief-Devs|Brief Devs]]
