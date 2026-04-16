# Contexto

Contexto de negocio, decisiones del usuario y TODOs pendientes. No incluye cosas que ya están en el código — eso va en [[arquitectura]] o [[stack]].

## Por qué existen las cosas

- **Portal `/profesionales`** — pedido del cliente para emular el programa de giovegen.com/profesionales/. Objetivo: comisiones a profesionales de la salud que recomienden NAEVO, con material científico exclusivo, soporte dedicado y muestras gratuitas. Hero con foto real de una doctora con guardapolvo blanco (Unsplash).
- **Página `/ciencia`** — el cliente quiere que "Basado en evidencia, formulado por expertos" tenga entidad propia (página dedicada) en vez de ser un bloque más del home. El link "Conocé nuestros estándares" del home ahora lleva ahí.
- **6 categorías en una sola línea** — antes estaban 5 arriba + 1 sola abajo ("Salud Digestiva" quedaba huérfana). Era rompedor visualmente.
- **Hover crossfade lifestyle↔producto (Horbäach)** — referencia directa al estilo de horbaach.com "SHOP BY CATEGORY". Hace la sección más atractiva y muestra el producto NAEVO al hacer hover. Se replicó el CSS exacto del `theme.css` de ellos (zoom 1.01→1.07 con 950ms cubic-bezier, título slide + arrow reveal).
- **Frascos NAEVO transparentes en hover** — el cliente quería ver los productos reales (no stock bottles) al pasar el mouse. Los 6 frascos existentes se procesaron con Python PIL en el host para remover el fondo blanco y quedar como PNG transparente.
- **Sin card blanco en WellnessGoals** — versión anterior tenía cada categoría en un card con sombra; el cliente pidió quitarlo para que el estilo quedara más limpio tipo Horbäach.
- **Hero más impactante** — el slider anterior era chico (`clamp(300px,42vw,600px)`) y el título se perdía. Ahora es `min-h-[85vh]` con tipografía `text-8xl` en desktop.
- **Unificación Quality + Certifications** — eran dos secciones separadas con propósito redundante. Ahora una sola con las promesas de calidad como feature cards y las certificaciones como row de badges abajo.
- **Blog preview fuera del home** — el cliente no quería que el blog compitiera con el catálogo en la página principal; el contenido editorial queda solo en `/blog`.
- **Logo SVG + alto editable desde admin** — cliente quería que el logo escale limpio a cualquier tamaño (SVG) y poder ajustar su altura sin tocar código (admin settings). Se creó un patrón de "public settings whitelist" reutilizable.

## TODOs pendientes (abril 2026)

### Pendientes en la rama `feature/homepage-updates-abril-2026`

- **Endpoint backend para Profesionales** — el formulario de `pages/profesionales.vue` apunta a `/api/professionals` que no existe. Falta crear controller + migration + route + email de notificación al admin.
- **Seeder de certifications badges** — verificar que `trust_badges.certifications` traiga todos los esperados (GMP, ISO 9001, No GMO, Gluten Free, Vegano). Si faltan, actualizar el seeder del CMS.

### Mejoras futuras

- **Normalizar slug `antiestres-sueño`** — hoy tiene ñ en la DB pero los filenames en storage usan ASCII. Si se normaliza a ASCII, renombrar los archivos también.
- **Integraciones reales de shipping carriers** — OCA/Andreani/Entregar tienen costos simulados. Implementar APIs reales cuando corresponda.
- **Doble opt-in en newsletter** — hoy es suscripción directa.
- **Fotos lifestyle más alineadas a la marca** — hoy son de Unsplash stock (free license). Cuando haya fotos profesionales NAEVO, subir desde `/admin/objetivos` (flow ya funciona).

## Reglas del usuario (preferencias personales)

- **Nunca adjudicar autoría** — sin `Co-Authored-By` en commits, sin AI attribution, los commits son del usuario. ⚠️ Regla durable, aplica a todo el proyecto.
- **Hablar en español** — todas las interacciones, docs y notas en español.
- **Iterar rápido** — si algo no gusta, cambiar sin resistencia; no defender decisiones.
- **Simplicidad sobre complejidad** — no agregar features no pedidas, no sobre-diseñar.
- **Verificar antes de asumir** — curl la API antes de crear componentes, leer docs antes de tocar módulos (ver [[memoria]] para los gotchas).
- **Editabilidad CMS siempre que tenga sentido** — cuando se hace un cambio visual con contenido (ej. fotos de categorías), asegurar que sea editable desde el admin después.

## Workflow que ya aprendí

- **Frontend rebuild obligatorio** — después de cualquier cambio en Nuxt, `docker compose build --no-cache frontend && docker compose up -d frontend`. No hay hot reload en SSR.
- **Backend cambios vía cp para iteración rápida** — `docker compose cp` al container corriendo + `php artisan optimize:clear` funciona para iterar sin rebuildear. Al final del bloque de cambios, hacer un rebuild `--no-cache` de backend para que la imagen persista los cambios.
- **Restore desde prod** — `./restore.sh` es interactivo (pide número de backup + password del `.env` + "si" para confirmar). Ejecutar con prefijo `!` en la sesión Claude.
- **Agregar página static** — además de crear `pages/foo.vue`, hay que agregar `foo` al array `reservedSlugs` en `pages/[slug].vue`, sino el catch-all intenta fetchearla como CMS page.
- **Auth middleware** — verificar que la ruta tenga `auth:sanctum` antes de asumir que `$request->user()` funciona. Las rutas de carrito NO tienen middleware y resuelven el user manualmente.
- **macOS TCC bloquea Documents** — si el user pasa un path bajo `~/Documents/`, `~/Desktop/`, `~/Downloads/`, pedirle que mueva el archivo a `/tmp/` con `! mv ...` — ni siquiera `dangerouslyDisableSandbox` destraba TCC.
- **Python PIL en el host** para procesar imágenes — no hay ImageMagick instalado. `python3 -c "from PIL import Image"` funciona out of the box en macOS.
- **`apiResource` y rutas custom** — declarar la ruta custom (`POST upload-image`) **antes** del `apiResource` para que no se interprete como `{id}`.

## Ver también

- [[naevo|Índice]]
- [[arquitectura|Arquitectura]]
- [[memoria|Memoria auto-guardada con gotchas y patterns]]
- [[changelog|Changelog]]
