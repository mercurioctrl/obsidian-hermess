# Landings HTML

Dos landings autocontenidas en la **raíz** del proyecto (`/var/www/d-link/`), con la paleta
corporativa real de D-Link (azul insignia `#4481a7` + neutros) e íconos SVG flat.

## `index.html` — cara al consumidor
Landing de conversión (índice del sitio). Claim "El WiFi que anda", 3 pilares, héroes
(Mesh M15/M30, R15/R18, cámara DCS), teaser del programa Partner y captura de newsletter.
Deriva a MercadoLibre. Contenido bajado de [[estrategia-marca]] y [[plan-campana]].

## `propuesta.html` — cara a D-Link (propuesta de Blu)
Versión web navegable del pitch, hecha por el estudio [[contexto|Blu]]. Es el archivo sobre el
que el usuario más itera.

**Flujo:** hero → diagnóstico → las **4 murallas** + la grieta → estrategia → qué hacemos (plan por
canal) → inversión (**6 bloques de servicio numerados 01–06**) → KPIs → cierre.

**Particularidades:**
- **Gate por token:** `?token=dlk-mkt-2026` en la URL, o input en la pantalla "Propuesta privada".
  Client-side (disuade, no es seguridad real; el enforcement real sería server-side en la plataforma de Blu).
- **Lockup "D-Link × Blu"** en header y footer (logo de Blu SVG inline).
- **Confetti / papel picado** al clickear el CTA "Avancemos →" del cierre.
- **Divergencias deliberadas** con el resto de entregables (NO propagar salvo pedido):
  - Presupuesto **USD 1.800/mes** (el resto: 2.000).
  - Alcance **Argentina y Chile** (el resto: solo Argentina).
  - Menciona garantía **"hasta 10 años"**.
- **Copy de cierre:** "No vamos a gritar más fuerte. Vamos a decir algo con más respaldo." →
  "D-Link. Conectividad que responde."

## Ver también
[[arquitectura]] · [[contexto]] · [[pitch-punchlines-propuesta]] · [[D-Link]]
