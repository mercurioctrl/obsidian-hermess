# Contexto

Contexto de negocio, decisiones del usuario y TODOs pendientes. No incluye cosas que ya están en el código — eso va en [[arquitectura]] o [[stack]].

## Por qué existen las cosas

- **Portal `/profesionales`** — pedido del cliente para emular el programa de giovegen.com/profesionales/. Objetivo: comisiones a profesionales de la salud que recomienden NAEVO, con material científico exclusivo, soporte dedicado y muestras gratuitas.
- **Página `/ciencia`** — el cliente quiere que "Basado en evidencia, formulado por expertos" tenga entidad propia (página dedicada) en vez de ser un bloque más del home. El link "Conocé nuestros estándares" del home ahora lleva ahí.
- **6 categorías en una sola línea** — antes estaban 5 arriba + 1 sola abajo ("Salud Digestiva" quedaba huérfana). Era rompedor visualmente.
- **Hover crossfade lifestyle↔producto** — referencia directa al estilo de horbaach.com "SHOP BY CATEGORY". Hace la sección más atractiva.
- **Hero más impactante** — el slider anterior era chico (`clamp(300px,42vw,600px)`) y el título se perdía. Ahora es `min-h-[85vh]` con tipografía `text-8xl` en desktop.
- **Unificación Quality + Certifications** — eran dos secciones separadas con propósito redundante. Ahora una sola con las promesas de calidad como feature cards y las certificaciones como row de badges abajo.
- **Blog preview fuera del home** — el cliente no quería que el blog compitiera con el catálogo en la página principal; el contenido editorial queda solo en `/blog`.

## TODOs pendientes (abril 2026)

### Críticos para completar la rama

- **Fotos reales para WellnessGoals** — hoy el crossfade hover muestra SVG fallbacks a ambos lados. Hay que subir fotos lifestyle + producto por categoría. Dos opciones:
  - Estáticas: `public/images/categories/{slug}-lifestyle.jpg` + `-producto.jpg`.
  - CMS: agregar columnas `lifestyle_image_url` / `product_image_url` a `wellness_goals` (+ seeder + admin UI).
- **Endpoint backend para Profesionales** — el formulario de `pages/profesionales.vue` apunta a `/api/professionals` que no existe. Falta crear controller + migration + route + email de notificación.
- **Seeder de certifications badges** — verificar que `trust_badges.certifications` traiga todos los esperados: GMP, ISO 9001, No GMO, Gluten Free, Vegano. Si faltan, actualizar el seeder del CMS.

### Mejoras futuras

- **Integraciones reales de shipping carriers** — hoy OCA/Andreani/Entregar tienen costos simulados. Implementar APIs reales cuando corresponda.
- **Doble opt-in en newsletter** — hoy es suscripción directa.

## Reglas del usuario (preferencias personales)

- **Nunca adjudicar autoría** — sin `Co-Authored-By` en commits, sin AI attribution, los commits son del usuario. ⚠️ Regla durable, aplica a todo el proyecto.
- **Hablar en español** — todas las interacciones, docs y notas en español.
- **Iterar rápido** — si algo no gusta, cambiar sin resistencia; no defender decisiones.
- **Simplicidad sobre complejidad** — no agregar features no pedidas, no sobre-diseñar.
- **Verificar antes de asumir** — curl la API antes de crear componentes, leer docs antes de tocar módulos (ver [[memoria]] para los gotchas).

## Workflow que ya aprendí

- **Frontend rebuild obligatorio** — después de cualquier cambio en Nuxt, `docker compose build --no-cache frontend && docker compose up -d frontend`. No hay hot reload en SSR.
- **Restore desde prod** — `./restore.sh` es interactivo (pide número de backup + password del `.env` + "si" para confirmar). Ejecutar con prefijo `!` en la sesión Claude.
- **Agregar página static** — además de crear `pages/foo.vue`, hay que agregar `foo` al array `reservedSlugs` en `pages/[slug].vue`, sino el catch-all intenta fetchearla como CMS page.
- **Auth middleware** — verificar que la ruta tenga `auth:sanctum` antes de asumir que `$request->user()` funciona. Las rutas de carrito NO tienen middleware y resuelven el user manualmente.

## Ver también

- [[naevo|Índice]]
- [[arquitectura|Arquitectura]]
- [[memoria|Memoria auto-guardada con gotchas y patterns]]
- [[changelog|Changelog]]
