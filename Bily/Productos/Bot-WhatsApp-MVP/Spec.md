# Spec MVP — Agente WhatsApp con cerebro propio (Producto Blu)

**Status:** v0.1 — draft inicial, iterando con Catriel · Claude (Opus 4.7).
**Última actualización:** 2026-05-24

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
- 🔴 [PENDIENTE] Geografía: ¿Argentina-only en MVP, o LATAM desde el día 1?

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

---

## 5. Modelo de negocio

🟢 **Modelo:** Suscripción mensual fija.

🔴 **[PENDIENTE] Pricing exacto** — necesito tu input. Opciones a discutir en próxima ronda de preguntas.

🟢 **Brain ownership cuando dejan de pagar:** Freezing 90 días → eliminación. Notificaciones al usuario en día 60 y 80 con opción de export.

🟡 **[PROPUESTA] Estructura de tiers:**
- **Trial:** 14 días free, full features
- **Personal:** $X/mes — 1 agente, modelos top-tier con cap diario, todos los tools básicos
- **Pro:** $Y/mes — modelos top-tier sin cap, tools avanzados (ERP/integraciones), prioridad de procesamiento
- **(Post-MVP) Business:** 1 cuenta + múltiples agentes (vos + el de tu negocio), shared brain opcional

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

🔴 **[PENDIENTE]** Cómo se pairea WhatsApp Web con el chip si el chip está en una phone farm vs GSM gateway. Esto es operacional, no UX, pero define el tiempo del minteo (30s o 5 min?).

### 6.2. Uso diario

- Usuario manda mensaje (texto/audio/imagen) por WA → Agente procesa → Responde por WA
- Audio: transcrito local con whisper, NUNCA gasta tokens multimodal
- Imágenes: analizadas con LLM vision (cuando aplica)
- Agente puede usar tools detrás de escena (buscar en internet, leer mail, mandar mensaje a alguien) y reportar resultado
- Cada noche: dream-cron consolida memoria del día
- Cada semana: pattern-detector reporta insights ("notamos que los lunes a la mañana siempre te toca cobrar a X cliente")

### 6.3. Casos borde

🔴 **[PENDIENTE]** Definir comportamiento para:
- Usuario cambia su número de WhatsApp personal → ¿el agente se entera? ¿hay que re-verificar?
- Usuario pierde el celular del agente / queman el chip → portabilidad del cerebro a nuevo chip
- Agente agregado a grupo → ¿responde solo si lo mencionan? ¿escucha todo siempre?
- Usuario pide acción dañina (eliminar archivos, mandar mail a X persona X cosa) → guardrails
- Dos personas hablando del mismo proyecto, ambas tienen agente → ¿cross-pollination? (probablemente NO en MVP)

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
| Group chats (escuchar/responder en grupos) | Comportamiento sutil + privacy → fase 2 |
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

🟢 **Naming convention:** Todos los nombres empiezan con B (alineado al brand Blu). Lista curada de ~50-100 nombres con vibe argentino + cálido. Inmutable una vez asignado.

🔴 **[PENDIENTE]** Lista exacta de nombres — propuesta inicial:
- Femeninos: Brisa, Barbi, Bea, Belu, Bruna, Bianca, Bauti, Benji, Bambi, Briana...
- Masculinos: Billy, Bruno, Beto, Bauti, Benji, Bilo, Bro, Beni, Borja, Baltasar...
- Neutros / gender-fluid: Bauti, Benji, Bilo, Beni, Bambi, Brett...

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

🔴 **[PENDIENTE] Performance:**
- Latencia objetivo de respuesta: ¿2s? ¿5s? ¿"cuando esté listo"?
- Transcripción de audio: ya medido ~5-10s para audio típico
- Concurrencia: ¿cuántos agentes simultáneos por server?

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

## 11. Roadmap post-MVP (orientación, no compromiso)

**Fase 2 (mes 4-6 post-launch):**
- Telegram channel
- Multi-agent por usuario (uno personal + uno de trabajo)
- Group chat support en WA
- Tool: mail (Gmail / IMAP)
- Tool: calendar
- Acceso a ERP Blu (para clientes Blu)

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

- [ ] **Pricing exacto** ($/mes por tier)
- [ ] **Geo/idioma** (Argentina-only vs LATAM, español-only vs multi)
- [ ] **Infraestructura WA**: phone farm vs GSM gateway (define el OPS de chips)
- [ ] **Lista final de nombres B**
- [ ] **Latencia objetivo** y SLA
- [ ] **Behavior en grupos** (responde solo si mencionado vs siempre escucha vs configurable)
- [ ] **Edge cases** (cambio de número del user, pérdida de chip, etc.)
- [ ] **Marketing channel** primario para los primeros 100 users (ads vs influencers vs orgánico vs referral)
- [ ] **Diferenciación específica** vs ChatGPT en WhatsApp (Poe, etc.)
- [ ] **Cuál es el "wow moment"** que convierte trial→paid (cosa concreta que demostremos)
- [ ] **Si el usuario quiere un nombre específico (Billy 2.0?)** — ¿se respeta o sigue siendo random?
- [ ] **Equipo & responsabilidades**: quién es el PM/product owner (vos? alguien del equipo?)

---

## Relacionado

- [[Bily/Productos/Billy-Bot|Arquitectura de Microservicios (Billy Bot)]]
- [[Bily/Productos/Bot-WhatsApp-Nativo|Producto: Bot Copiloto Nativo para WhatsApp]] (idea original)
- [[Bily/Productos/Bot-WhatsApp-Minteeo-y-Suenio|Minteo y Sueño]]
- [[Bily/Productos/Bot-WhatsApp-Elevator-Pitch|Elevator Pitch]]
- [[Claude/Whisper|Stack de transcripción local]] (componente reusable)
- [[Claude/Vault-Wrappers|API canónica para tocar la bóveda]] (patrón aprendido)
