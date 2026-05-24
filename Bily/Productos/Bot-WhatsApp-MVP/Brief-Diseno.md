# Brief Diseño — Bily (producto de Blu Studio Inc)

> **Decisiones fundacionales** (cerradas con Catriel el 2026-05-24):
> - **Producto:** Bily (la marca paraguas / empresa es Blu Studio Inc)
> - **Dominio:** `billy.blustudioinc.com` (⚠️ verificar grafía oficial: "Bily" vs "Billy")
> - **Brand identity:** Logo y colores básicos existen, no hay brand book formal → diseño los recibe y formaliza
> - **Redes sociales:** Crear cuentas separadas para Bily (Blu Studio empresa tiene las suyas)

**Para:** Equipo de Diseño · **De:** Catriel + Claude · **Fecha:** 2026-05-24
**Doc relacionado:** [[Bily/Productos/Bot-WhatsApp-MVP/Spec|Spec MVP v1.0]] (leer para contexto completo, NO obligatorio para arrancar)

---

## 1. Contexto en 1 minuto

Estamos construyendo un **asistente IA premium con identidad propia que vive en su propio WhatsApp**. Cada usuario que se suscribe (US$59/mes) recibe un agente con:
- **Nombre random** que empieza con B (Billy, Brisa, Bruno, Barbi, etc.) — inmutable
- **Avatar único** generado automáticamente al instante (estilo space-invader, vía API que Blu ya tiene)
- **Su propio número de WhatsApp dedicado**
- **Personalidad propia** (semi-randomizada en 4 ejes: tono/proactividad/humor/estilo)
- **Cerebro markdown** que crece con el uso del usuario

La promesa emocional: "No es un bot, es un asistente con identidad propia que se vuelve irreemplazable porque acumula tu historia personal".

Target: profesionales individuales + dueños de PyME (30-55 años, Argentina primero).

---

## 2. Entregables esperados (priorizados)

### 🔴 Prioridad 1 — bloquean dev (semanas 1-2)

#### 2.1. Brand Identity Master (Blu)
- Logo Blu (versión principal + variantes para light/dark, símbolo solo, lockup)
- Paleta de colores oficial (primarios + secundarios + neutros + semánticos)
- Tipografía oficial (titulares + cuerpo + UI + monospace para code/tech)
- Voice & visual tone (formal vs casual, tech vs cálido, etc.)

**Output:** archivo de branding (Figma + PDF) + tokens exportables (Tailwind config o similar)

#### 2.2. Avatar System Guidelines
Cada agente tiene un avatar único minteado automáticamente. Necesitamos:
- **Style guide del generador:** qué características SÍ aparecen (formas geométricas, paleta limitada, "pixel art" feel), qué NO (caras humanas realistas, símbolos religiosos/políticos, etc.)
- **Variantes de tamaño:** 64×64 (chat profile), 256×256 (intro), 512×512 (landing), 1024×1024 (print/marketing)
- **Treatment para fondos:** sobre claro / oscuro / colored
- **Animaciones del minteo:** cómo se anima el avatar cuando "nace" (en mensajes WhatsApp el video corto es posible)

**Coordinar con el equipo técnico que tiene la API de mint** — ellos te van a mostrar el output actual de la API. Tu trabajo: validar que cumple guidelines o iterar el prompt/modelo si no.

#### 2.3. Minteo Flow — Visuales y Cards
El minteo es el momento más importante del producto (primer 5 minutos del usuario). Aunque WhatsApp es texto, podemos mandar:
- Imágenes (PNG)
- Audios (cortos)
- Cards / templates de WhatsApp Business (si vamos por Cloud API; por ahora con whatsapp-web.js mandamos solo media)
- Reacciones / emojis estratégicos

**Necesitamos:**
- **Tarjeta "Bienvenido a Blu"** que recibe el usuario cuando manda el primer mensaje al número público de minteo
- **Tarjeta "Conocé a tu asistente"** con el avatar minteado + nombre + tagline ("Hola, soy Brisa. Recién nací.")
- **Tarjeta de "Tu agente está naciendo"** durante los 30 segundos de bootstrap (loader / animation amigable)
- **Pequeño visual celebratorio** cuando completa onboarding inicial (primeras 5 vueltas de conversación)

Pensar en **template parametrizable** — el nombre y avatar cambian, el resto del layout es fijo.

#### 2.4. Iconografía core
Set inicial de ~30-50 iconos consistentes para usar en:
- Cards de minteo (notificaciones, acciones, conceptos)
- Admin panel
- Landing
- App de Bily si la hubiera (post-MVP)

Tema: tools del agente (web search, brain, audio, calendar, mail, kanban, persons, etc.).

### 🟡 Prioridad 2 — necesario para launch (semanas 3-4)

#### 2.5. Landing Page Design
- **Hero:** mensaje principal + CTA "Crear mi asistente" (que abre WhatsApp a número público de minteo)
- **Sección "Cómo funciona"**: 3-4 pasos visualizados (mintea → habla → te conoce → te ayuda)
- **Sección "Qué hace"** (features con iconos)
- **Sección "Diferencia vs ChatGPT en WA"** (tabla comparativa visual)
- **Sección testimoniales** (placeholder mientras no haya, después se llenan)
- **Pricing:** un solo card grande con $59/mes destacado + "14 días free trial" + lista de features
- **FAQ**
- **Footer:** legal, contacto, redes

**Mood/feel sugerido:** premium pero cálido. No "tech corporativo frío" tipo enterprise SaaS, sino más cerca de productos como Linear / Notion / Cron — bien diseñados, modernos, con personalidad humana.

#### 2.6. Admin Panel UI (para Catriel y el equipo, no para usuarios)
Necesitamos un panel interno simple para:
- **Lista de agentes activos** (avatar, nombre, owner, status, días desde minteo, $/mes generado, msgs/día)
- **Detalle de cada agente** (cerebro size, último msg, errores, billing status)
- **Pool de chips** (cuáles libres, cuáles asignados, health de cada Android)
- **Métricas globales** (MRR, churn, conversiones, cost/user)
- **Logs / alertas** (qué necesita atención humana)

**Stack frontend que probablemente use el equipo:** Next.js + Tailwind + shadcn/ui. Diseñar component-first usando ese sistema.

### 🟢 Prioridad 3 — post-MVP / nice to have (semanas 5+)

- Mobile app (alternativa a WA, para usuarios power que la quieran)
- Templates para emails transaccionales (welcome, billing, retention, brain export)
- Assets para social media (templates para IG, X, LinkedIn)
- Brand book completo

---

## 3. Cronograma sugerido (4-6 semanas paralelas al dev)

| Semana | Foco | Outputs concretos |
|---|---|---|
| 1 | Brand identity + avatar system guidelines | Logo Blu definitivo, paleta, tipografía, primera revisión del generador de avatars |
| 2 | Minteo flow cards + iconografía | 4-5 templates de cards, set de 30 iconos |
| 3 | Landing page (mockups + diseño final) | Figma de la landing completa |
| 4 | Admin panel (mockups + componentes) | Figma de las 5-6 pantallas principales |
| 5-6 | Iteración + assets de marketing | Lo que pida marketing + ajustes |

---

## 4. Guidelines y decisiones ya tomadas (no negociables)

- **Nombre de la marca paraguas:** Blu
- **Naming de agentes:** todos empiezan con B (lista en spec). Diseño puede sugerir agregar/sacar nombres pero la regla "B" es fija.
- **Avatar style:** "space-invader" / pixel art geométrico, único por agente, generado automático
- **Tono general:** premium pero accesible, cálido, NO corporativo frío, NO infantil
- **Argentina primero:** mensajería en español rioplatense, NO neutro
- **Mobile first** para landing (la mayoría va a llegar desde links en WA o redes)

---

## 5. Recursos disponibles

- **API de mint de avatar:** ya existente (pedirla al equipo técnico)
- **Spec completa del producto:** [[Bily/Productos/Bot-WhatsApp-MVP/Spec]]
- **Lista de 45 nombres B propuestos:** sección 8 de la spec
- **Diferenciador canónico:** "No es un bot. Es un asistente con nombre, cara y memoria propia, que aprende tu vida y se vuelve irreemplazable porque acumula tu historia personal en un cerebro que es tuyo."

---

## 6. Preguntas / decisiones pendientes (a coordinar con Catriel)

**Cerradas:**
- [x] Nombre del producto → **Bily** (empresa = Blu Studio Inc)
- [x] Dominio → **billy.blustudioinc.com**
- [x] Logo y brand existente → básico, sin brand book formal
- [x] Redes sociales → crear nuevas para Bily

**Aún por coordinar con Catriel:**
- [ ] Verificar grafía oficial: "Bily" o "Billy" (el dominio usa "billy" con doble L pero el nombre se dijo "bily" con una)
- [ ] Catriel pasa logo actual + paleta de colores actual de Blu Studio (PNG/SVG/Figma)
- [ ] Catriel comparte 5-10 ejemplos del avatar generado por la API actual
- [ ] Cuenta Figma compartida (¿la creamos? ¿usás la del equipo?)

---

## 7. Criterios de éxito del trabajo de diseño

- Brand identity coherente y aplicable consistentemente
- Avatar system genera variedad rica sin output "feo" en >5% de los casos
- Minteo cards generan reacción emocional ("qué lindo lo que recibí") en tests con beta users
- Landing convierte >5% de visitas a "iniciar trial" (industry good)
- Admin panel es usable sin documentación (el equipo lo agarra y funciona)

---

## 8. Coordinación

- **Standup semanal con Catriel:** 30 min los lunes para alinear prioridades
- **Reviews intermedias:** WIPs mostrados antes de que estén "finalizados" para evitar reworks
- **Async:** subir todo a Figma compartido + avisar por canal de trabajo
- **Coordinar con marketing:** los assets visuales que diseño produce alimentan marketing — sincronizar entregas

---

## Relacionado

- [[Bily/Productos/Bot-WhatsApp-MVP/Spec|Spec MVP completa]]
- [[Bily/Productos/Bot-WhatsApp-MVP/Brief-Marketing|Brief Marketing]] (próximamente)
- [[Bily/Productos/Bot-WhatsApp-MVP/ADR|Architecture Decision Record]] (próximamente)
