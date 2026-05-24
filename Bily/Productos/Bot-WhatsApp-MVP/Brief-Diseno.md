# Brief Diseño — Bily (producto de Blu Studio Inc)

**Para:** Equipo de Diseño · **De:** Catriel + Claude · **Fecha:** 2026-05-24 (v2)
**Doc relacionado:** [[Bily/Productos/Bot-WhatsApp-MVP/Spec|Spec MVP v2.0]] (leer para contexto completo, NO obligatorio para arrancar)

> **Decisiones fundacionales** (cerradas en v2.0):
> - **Producto:** Bily (grafía oficial, 1 L) — empresa **Blu Studio Inc**
> - **Dominio:** `billy.blustudioinc.com`
> - **Pricing:** **$249 USD/mes** (~275k ARS) single tier premium
> - **Strategy:** **Apple-style** (premium + minimalismo obsesivo + experiencia sin friction)
> - **Brand identity:** Logo y colores básicos existen, no hay brand book formal → diseño formaliza
> - **Redes sociales:** Crear cuentas separadas para Bily (Blu Studio empresa tiene las suyas)

---

## 1. Contexto en 1 minuto

Construimos **Bily**: un asistente IA premium con identidad propia que vive en su propio WhatsApp. Cada usuario que se suscribe ($249/mes) recibe un agente con:
- **Nombre random** que empieza con B (inmutable)
- **Avatar único** generado automáticamente al instante (estilo space-invader, vía API existente)
- **Su propio número de WhatsApp dedicado**
- **Personalidad propia** (semi-randomizada)
- **Cerebro markdown** que crece con el uso

**Target:** dueños PyME + profesionales independientes premium (35-60 años, Arg primero).

**Strategy = Apple-style.** Premium minimal. Sin tier free. Sin descuentos. Sin demos. **El producto + experiencia + diseño venden solos.** Marketing minimal. Brand visual obsesivamente pulido.

**Tu trabajo es CRÍTICO:** sos quien hace que el unboxing del minteo sea memorable y que la marca se sienta premium desde el primer pixel.

---

## 2. Vibe Apple-style — lo que SÍ y lo que NO

✅ **SÍ:**
- Paleta limitada (3-4 colores max, neutros + 1 acento)
- Tipografía cuidada (1 sans premium tipo Inter/SF Pro/Söhne, máximo 2 weights)
- Mucho white space, NO clutter
- Iconografía consistent y minimal (línea fina, no glyphs heavy)
- Animaciones sutiles pero presentes (no static dead, no over-animated)
- Avatar único como hero del onboarding
- Microcopy pulido al milímetro
- Fotografía/render premium si se usa (NO clipart stock free)
- Brand voice "confidence without arrogance"

❌ **NO:**
- Paletas saturadas de gradients neon estilo crypto/web3
- Tipografías "techy/futuristas" tipo Orbitron/Eurostile
- Iconografía cartoon o emoji-style
- Layouts con 20 CTAs y popups
- "Hand-drawn" hipster aesthetic
- Long-form scroll endless tipo SaaS clásico
- Mascot animado (el avatar minteado es el hero, no necesitamos otro)
- Banners "OFERTAS!!!" o promos visuales gritonas

**Referencias visuales que nos inspiran:**
- Apple.com (claramente)
- Linear.app
- Cron (antes de ser Notion Calendar)
- Things 3 (Mac app)
- Vercel.com
- Stripe
- Mid-tier Aceptable: Notion, Raycast, Arc browser

**Referencias que NO queremos:**
- Most SaaS landing pages (over-designed, hard-sell)
- Crypto / Web3 aesthetic
- Hubspot / Mailchimp clipart style
- Bootcamps de programación (cartoonish)

---

## 3. Entregables esperados (priorizados)

### 🔴 Prioridad 1 — bloquean dev (semanas 1-2)

#### 3.1. Brand Identity Master (Blu Studio Inc + Bily)

**Dos niveles de brand:**

a) **Blu Studio Inc** — la marca paraguas (logo + paleta + tipo)
b) **Bily** — el producto, hijo de Blu Studio (logo propio que conviva)

Definir:
- Logo Blu Studio (versión principal + light/dark + símbolo solo + lockup)
- Logo Bily (relación visual con Blu — share color, share tipografía, evoluciona)
- Paleta de colores oficial (primarios + secundarios + neutros + semánticos)
- Tipografía oficial (1 sans premium + tipografía system fallback)
- Voice & visual tone documentado

**Output:** archivo de branding (Figma + PDF) + tokens exportables (Tailwind config, CSS vars).

#### 3.2. Avatar System Guidelines

Cada Bily tiene un avatar único minteado automáticamente. Necesitamos:
- **Style guide del generador:** qué SÍ (formas geométricas, paleta limitada, "pixel art" feel), qué NO (caras humanas realistas, simbolos religiosos/políticos, imagery offensive)
- **Variantes de tamaño:** 64×64 (chat profile), 256×256 (intro card), 512×512 (landing/onboarding), 1024×1024 (print/marketing)
- **Treatment para fondos:** sobre claro / oscuro / colored
- **Animación del minteo:** cómo se anima el avatar cuando "nace" — esto es el HERO MOMENT del producto, debe ser memorable

**Coordinar con el equipo técnico que tiene la API de mint** — ellos pasan 10-20 ejemplos generados. Tu trabajo: validar que cumplen guidelines o iterar el prompt/modelo si no.

#### 3.3. Minteo Flow — Visuales y Cards (EL HERO DEL PRODUCTO)

**Esto es el "unboxing" Apple-style. Cada detalle cuenta.**

Aunque WhatsApp es texto, podemos mandar:
- Imágenes (PNG/JPG)
- Videos cortos (5-15 seg, autoplay)
- Cards / templates (vía media)
- Audios (cortos, opcional)

Cards a producir:
- **Card "Bienvenido a Bily"** (recibe el usuario al primer mensaje al bot público)
- **Card "Generando tu Bily..."** (loader animado mientras se mintea — 30 seg de espera)
- **Card "Conocé a [NombreAgente]"** con avatar minteado + nombre + tagline ("Hola, soy Brisa. Recién nací.")
- **Animación de "nacimiento" del avatar** (5-10 seg de loop subtil)
- **Card celebratoria** al cerrar onboarding inicial (después de las primeras 5 preguntas)

**Templates parametrizables** — el nombre y avatar cambian, layout es fijo.

**Esto es donde más invertimos. El minteo es nuestro "unboxing iPhone".**

#### 3.4. Iconografía core

Set inicial de ~30-50 iconos minimalistas (línea fina, no fill) para:
- Cards de minteo
- Admin panel
- Landing
- Documentación

Temas: tools del agente, conceptos (brain, memory, action, identity), navegación.

### 🟡 Prioridad 2 — necesario para launch (semanas 3-4)

#### 3.5. Landing Page Design

**Mood Apple-style minimal:**
- **Hero:** mensaje principal + CTA único "Crear mi Bily" + visual del avatar (animado idealmente)
- **Video corto** (5-15 seg) del minteo embedded
- **Sección "Cómo funciona"**: 3 pasos visualizados, NO 8
- **Sección "Qué hace"** (6 features con iconos minimalistas, NO 20)
- **Diferencia vs ChatGPT en WhatsApp** (tabla comparativa visual minimal)
- **Una historia de cliente** (cuando haya — UN testimonio bien contado, no 50)
- **Pricing:** card único con $249/mes destacado + "14 días free, sin tarjeta"
- **FAQ** minimal (8-10 preguntas)
- **Footer:** legal, contacto, redes

**Mood/feel:** premium + cálido. Tipo Linear / Vercel / Cron. NO Hubspot / Mailchimp / SaaS típico.

#### 3.6. Admin Panel UI (interno, para Catriel y equipo)

Panel interno simple para:
- **Lista de agentes activos** (avatar, nombre, owner, status, días desde minteo, MRR contribution, msgs/día)
- **Detalle de cada agente** (cerebro size, último msg, errores, billing status)
- **Pool de chips** (cuáles libres, cuáles asignados, health de cada Android)
- **Métricas globales** (MRR, churn, conversiones trial→paid, cost/user)
- **Logs / alertas** (qué necesita atención humana)

**Stack frontend:** Next.js 15 + Tailwind + shadcn/ui. Diseño component-first.

**Tone admin:** profesional pero NO frío. Es interno pero refleja el brand premium del producto.

### 🟢 Prioridad 3 — post-MVP / nice to have

- Mobile app (alternativa a WA, post-MVP)
- Templates emails transaccionales (welcome, billing, retention, brain export)
- Assets para social media premium (IG/X templates minimalistas)
- Brand book completo (60+ páginas)

---

## 4. Cronograma sugerido (4-6 semanas paralelas al dev)

| Semana | Foco | Outputs concretos |
|---|---|---|
| 1 | Brand identity Blu + Bily + avatar system | Logo Blu + Bily definitivos, paleta, tipografía, primera revisión del generador de avatars |
| 2 | Minteo flow cards + iconografía + animación nacimiento avatar | 5-6 templates de cards, set de 30 iconos, video del nacimiento |
| 3 | Landing page (mockups + diseño final) | Figma de la landing completa con motion specs |
| 4 | Admin panel (mockups + componentes) | Figma de las 5-6 pantallas principales |
| 5-6 | Iteración + assets adicionales para marketing | Lo que pida marketing + ajustes basados en feedback dev/marketing |

---

## 5. Guidelines y decisiones ya tomadas (no negociables)

- **Marca paraguas:** Blu Studio Inc
- **Producto:** Bily (1 L)
- **Naming de agentes:** todos empiezan con B (lista de ~45 en spec). Diseño puede sugerir agregar/sacar pero la regla "B" es fija.
- **Avatar style:** "space-invader" / pixel art geométrico, único por agente, generado automático
- **Tone general:** premium + cálido + minimalismo Apple-style. NO corporate frío, NO infantil, NO crypto-vibe
- **Argentina primero:** mensajería en español rioplatense, NO neutro
- **Mobile first** para landing
- **Pricing:** $249/mes — comunicado con confianza, NO defensivamente

---

## 6. Recursos disponibles

- **API de mint de avatar:** ya existente (pedir al equipo técnico, deben pasar 10-20 ejemplos)
- **Spec completa del producto v2.0:** [[Bily/Productos/Bot-WhatsApp-MVP/Spec]]
- **Lista de 45 nombres B propuestos:** sección 8 de la spec
- **Diferenciador canónico:** "No es un chatbot. Es un asistente con nombre, cara y memoria propia, que aprende tu vida y se vuelve irreemplazable porque acumula tu historia personal en un cerebro que es tuyo."

---

## 7. Preguntas / decisiones pendientes (coordinar con Catriel)

**Cerradas:**
- [x] Nombre del producto → **Bily** (empresa = Blu Studio Inc)
- [x] Dominio → **billy.blustudioinc.com**
- [x] Logo y brand existente → básico, sin brand book formal
- [x] Redes sociales → crear nuevas para Bily
- [x] Strategy → Apple-style premium minimal

**Aún por coordinar con Catriel:**
- [ ] Catriel pasa logo actual + paleta de colores actual de Blu Studio Inc (PNG/SVG/Figma)
- [ ] Catriel comparte 10-20 ejemplos del avatar generado por la API actual
- [ ] Cuenta Figma compartida (¿la creamos? ¿usás la del equipo?)
- [ ] Aprobación de la dirección Apple-style minimal (referencias compartidas arriba)

---

## 8. Criterios de éxito del trabajo de diseño

- Brand identity coherente y aplicable consistently
- Avatar system genera variedad rica con quality bar alto (0% output "feo" o "raro")
- Minteo cards generan reacción emocional ("qué lindo lo que recibí, lo guardo") en tests con beta users
- Landing convierte >5% de visitas a "iniciar trial" (above industry good)
- Admin panel es usable sin documentación (el equipo lo agarra y funciona)
- Brand se percibe premium ("se nota que está cuidado")
- 0 elementos "obviamente templated" o stock-feeling

---

## 9. Coordinación

- **Standup semanal con Catriel:** 30 min los lunes para alinear prioridades
- **Reviews intermedias:** WIPs mostrados antes de "finalizados" para evitar reworks costosos
- **Async:** subir todo a Figma compartido + avisar por canal de trabajo
- **Coordinar con marketing:** los assets visuales que diseño produce alimentan marketing — sincronizar entregas + tone

---

## Relacionado

- [[Bily/Productos/Bot-WhatsApp-MVP/Spec|Spec MVP v2.0]]
- [[Bily/Productos/Bot-WhatsApp-MVP/Brief-Marketing|Brief Marketing v2]]
- [[Bily/Productos/Bot-WhatsApp-MVP/ADR|Architecture Decision Record]]
