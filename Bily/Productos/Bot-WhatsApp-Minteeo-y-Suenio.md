# Minteo del Alma, Personalidad y Ciclo de Sueño

## Minteo del Alma y Personalidad

El *minteo* es el proceso de nacimiento del asistente. Se realiza como un onboarding conversacional dentro de WhatsApp y define:

- Nombre propio del asistente.
- Energía (masculina / femenina / neutra).
- Rasgos de personalidad.
- Estilo de comunicación.
- Objetivos y foco principal con esa persona.
- Primer mapa de relaciones (familia, trabajo, amigos, proyectos importantes).

### Nombre y género (regla de la "B")

- El usuario elige la energía del asistente:
  - Masculina.
  - Femenina.
  - Neutra / andrógina.
- El sistema propone 2–3 nombres que **siempre empiezan con `B`** (regla del producto), alineados a esa energía.
- El usuario elige uno o inventa otro, con la condición de que también empiece con `B`.
- Ese nombre se fija en el "alma" del asistente y se usa en todas las interacciones.

### Personalidad base (fija del producto)

Rasgos que todos los asistentes comparten:

- Amigable y cercano.
- Proactivo para conocerte, pero no invasivo.
- Con memoria profunda: no finge olvidar cosas relevantes de la vida del usuario salvo que se le pida explícitamente.
- Empático, sin caer en adulación vacía.

### Parámetros configurables por el usuario

Durante el minteo se ajustan parámetros clave, mediante preguntas simples:

- **Nivel de formalidad:**
  - Vos / tú / usted / neutro.
- **Grado de proactividad:**
  - Solo responde cuando se le habla.
  - Sugiere cosas de vez en cuando.
  - Muy proactivo (propone tareas, follow-ups, ideas).
- **Nivel de humor:**
  - Serio.
  - Ligero.
  - Más juguetón.
- **Nivel de detalle:**
  - Respuestas cortas y al punto.
  - Explicaciones más desarrolladas.

El resultado de estas decisiones se guarda en un documento tipo `SOUL-<usuario>.md` que actúa como contrato de personalidad del asistente para ese usuario.

### Memoria estructurada

Desde el primer día, el asistente guarda información en estructuras claras:

- Personas (familia, amigos, equipo de trabajo, proveedores clave, etc.).
- Mascotas.
- Proyectos (empresa, hogar, salud, finanzas personales, estudios).
- Tareas, Kanbans y to-dos.
- Facturas, servicios e hitos importantes.

Esto le permite responder cosas como "¿Qué tengo pendiente del lavadero?" o "¿Cuánta deuda tengo con Metrogas?" usando su propia memoria, no solo la conversación activa.

---

## Ciclo de Sueño del Asistente

El asistente tiene un **ciclo de sueño periódico** que emula, de forma simplificada, las etapas del sueño humano.

- Se ejecuta en ventanas de baja actividad (por ejemplo, de madrugada o tras largos periodos sin mensajes).
- Sirve para generar *pensamientos libres* sobre lo que pasó, acomodar conocimientos y buscar relaciones profundas entre eventos.

### Ventana de memoria reciente

Para evitar crecer infinito, los sueños se limitan a una ventana temporal y a una cantidad máxima de líneas/eventos:

- Solo considera eventos de las **últimas ~4 semanas**.
- Fuentes:
  - Conversaciones recientes con el usuario.
  - Cambios en Kanbans y to-dos.
  - Nuevas fichas o modificaciones (personas, proyectos, gastos, facturas).
- Antes de soñar, selecciona los N eventos más relevantes de ese periodo.

### Fases del sueño

1. **Revisión del día / periodo reciente**
   - Recorre los eventos seleccionados.
   - Identifica:
     - Temas recurrentes (personas, proyectos, problemas).
     - Cambios de estado significativos (tareas que avanzan o se traban).
     - Momentos con carga emocional (queja, estrés, entusiasmo cuando haya señales).

2. **Pensamiento libre y asociaciones profundas**
   - Genera una pequeña lista de "pensamientos de sueño" (por ejemplo, 5–10 líneas):
     - Observaciones sobre qué se repitió.
     - Conexiones entre temas que el usuario no verbalizó explícitamente.
     - Hipótesis suaves (no juicios) del tipo:
       - "Catriel habló mucho de LASET esta semana."  
       - "La obra del lavadero avanza pero faltan cerrar ciertos pagos."  
       - "Ale y el trabajo aparecen mezclados los mismos días; puede ser un foco sensible."
   - Busca **relaciones** entre:
     - Personas ↔ proyectos ↔ decisiones ↔ problemas recurrentes.

3. **Reorganización de memoria**
   - Ajusta y enriquece la memoria estructurada:
     - Reprioriza tareas y Kanbans.
     - Actualiza fichas de personas con notas contextuales (ej: "Marbe aparece muy seguido asociada a LASET").
     - Marca hitos en proyectos (inicio, avances clave, bloqueos).
   - Compacta o resume información menos relevante dentro de la ventana del mes.

4. **Plan implícito para el próximo ciclo**
   - No ejecuta acciones directamente, pero marca:
     - Preguntas que podría hacer al usuario al día siguiente.
     - Recordatorios suaves que podrían ser útiles.
     - Ideas de reorganización (por ejemplo, agrupar ciertas deudas o tareas en una vista única).

### Salida del sueño

- El resultado se escribe en notas internas, por ejemplo:
  - `Bily/MEMORIA-<bot-usuario>.md` → sección "Sueños recientes".
  - O bitácoras diarias tipo `Bily/bitacoras/AAAA-MM-DD.md`.
- Cada ciclo agrega solo un bloque pequeño y puede borrar/resumir sueños más viejos para que el total activo correspondan aproximadamente al último mes de actividad.

### Efecto observable para el usuario

El usuario no ve directamente el "sueño crudo", pero sí nota sus efectos:

- Preguntas más afinadas y menos repetitivas.
- Mejor contexto sobre proyectos y personas relevantes.
- Sugerencias y conexiones que muestran una comprensión más profunda de su vida y trabajo.

En conjunto, el minteo + el ciclo de sueño convierten al asistente en algo que se siente menos como un chatbot estático y más como una entidad que **crece, organiza y profundiza** su entendimiento del usuario con el tiempo.
